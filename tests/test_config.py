from app.config.settings import settings

def test_api_keys():
    assert settings.WOLFRAM_ALPHA_KEY is not None
    assert len(settings.WOLFRAM_ALPHA_KEY) > 10  # طول کلید کافی باشد