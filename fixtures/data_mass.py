from faker import Faker

faker = Faker("pt_BR")

data = {
    "message": {
        "expectTitle": "zaplink-web",
        "expectNoticeName": "Nome é obrigatório",
        "expectNoticePhone": "Whatsapp é obrigatório",
        "expectNoticeDescription": "Assunto é obrigatório",
        "expectNotice": "Contato não encontrato",
        "expectMessage": "Email e/ou senha incorreto",
        "expectMessageEmail": "Oops. por favor informe seu e-mail",
        "expectMessagePassword": "Oops. por favor informe sua senha",
        "expectMessageAfterLogin": "Seu gerenciador digital de contatos"
    },

    "parameters": {
        "validUser": "junior@delcio.com.br",
        "validPassword": "delcio123",
        "contactNotRegistered": "84123456789",
        "wrongPassword": "abc123",
        "emptyEmail": "",
        "emptyPassword": ""
    },

    "contact": {
        "name": faker.first_name(),
        "number": faker.phone_number(),
        "description": faker.sentence(nb_words=5)
    }
}
