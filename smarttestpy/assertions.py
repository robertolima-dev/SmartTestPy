# 📦 smarttestpy/assertions.py

def assert_status_code(response, expected_status):
    """
    ✅ Valida se o código de status da resposta é o esperado.

    Args:
        response: Objeto de resposta (ex.: response do requests).
        expected_status (int): Código de status esperado.

    Raises:
        AssertionError: Se o código de status não corresponder.
    """
    actual_status = getattr(response, 'status_code', None)
    assert actual_status == expected_status, (
        f"❌ Código de status inválido: esperado {expected_status}, obtido {actual_status}."
    )


def assert_in_response(response, content):
    """
    🔍 Verifica se um conteúdo está presente na resposta.

    Args:
        response: Objeto de resposta com atributo 'text'.
        content (str): Texto esperado na resposta.

    Raises:
        AssertionError: Se o conteúdo não for encontrado na resposta.
    """
    response_text = getattr(response, 'text', '')
    assert content in response_text, (
        f"❌ Conteúdo '{content}' não encontrado na resposta."
    )


def assert_equal_with_message(actual, expected, message="Valores não correspondem."):
    """
    ⚡ Compara dois valores e exibe mensagem personalizada em caso de falha.

    Args:
        actual: Valor real.
        expected: Valor esperado.
        message (str): Mensagem exibida em caso de falha.

    Raises:
        AssertionError: Se os valores não forem iguais.
    """
    assert actual == expected, (
        f"❌ {message} Esperado: {expected}, Obtido: {actual}."
    )


# 🌟 Exemplo de uso básico
if __name__ == "__main__":
    class MockResponse:
        def __init__(self, status_code, text):
            self.status_code = status_code
            self.text = text

    response = MockResponse(200, "Dados processados com sucesso!")
    assert_status_code(response, 200)
    assert_in_response(response, "processados")
    assert_equal_with_message(2 + 2, 4, "A soma não corresponde ao esperado.")

    print("✅ Todos os testes passaram!")
