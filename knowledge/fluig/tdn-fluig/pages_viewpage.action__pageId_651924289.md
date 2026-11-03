---
content_hash: c1c88ec90ba1890354a2a24124b75ebe38bfbf957c987aa9865778d69b70c9b6
fetched_at: '2026-06-28T21:35:28.314500+00:00'
page_id: '651924289'
product: fluig
source: tdn-fluig
title: Controle de expiração de senha
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=651924289
version: 9
---

# Índice

true.\*ndicenone

# Controle de expiração de senha

---

Nesse exemplo, vamos utilizar recursos da plataforma **TOTVS Fluig**, como eventos globais e formulários, para efetuar um controle customizado de expiração de senha de acesso dos usuários.

O usuário administrador poderá definir o tempo em dias que uma senha será válida, ou seja, uma vez expirada, o usuário não conseguirá realizar o *[login](https://tdn.totvs.com/pages/viewpage.action?pageId=389547065#Plataforma%E2%9D%99Loginnaplataforma-Fazerlogin)*, com isso, aparecerá uma [mensagem](https://tdn.totvs.com/download/attachments/651924289/image2021-11-23_9-18-45.png?version=1&modificationDate=1637669953723&api=v2) informativa de expiração de senha, a qual indicará a utilização da função "Esqueci minha senha". 

Ao acionar a função "Esqueci minha senha", o usuário receberá uma mensagem no endereço de e-mail cadastrado com o procedimento de [recuperação de senha pessoal](https://tdn.totvs.com/pages/viewpage.action?pageId=389547065#Plataforma%E2%9D%99Loginnaplataforma-Recupera%C3%A7%C3%A3odesenhapessoal).

Neste exemplo, por questões de segurança, as senhas históricas não são armazenadas e não é feito comparativo se a senha foi realmente alterada no evento de atualização do usuário.

# Técnicas abordadas

---

* Interceptação do login de um usuário;
* Interceptação da alteração do cadastro de um usuário;
* Uso de eventos globais;
* Compartilhamento de função no contexto;
* Criação e atualização do [registro de formulário](https://tdn.totvs.com/x/9ryFDg) via webservice SOAP.

# Componentes utilizados

---

Vamos exemplificar o uso dos seguintes componentes Fluig:

* Criação de evento global (afterUpdateUser, beforeLogin);
* Datasets customizados (fluig\_create\_card e fluig\_update\_card);
* Uso de serviço SOAP Fluig - ECMCardService (métodos createCard e updateCardData);
* Formulário (politica\_senha e controle\_senha).

# Validação da senha expirada

---

Ao realizar o *login* no **TOTVS Fluig** e a senha estiver expirada, será exibida a seguinte mensagem de erro: "Sua senha expirou! Utilize a função 'Esqueci minha senha' para redefini-la", com isso, o usuário deverá proceder com a [recuperação de senha pessoal:](https://tdn.totvs.com/pages/viewpage.action?pageId=389547065#Plataforma%E2%9D%99Loginnaplataforma-Recupera%C3%A7%C3%A3odesenhapessoal)

# Desenvolvimento

---

Os desenvolvimentos que foram necessários para criar esse controle estão disponíveis para visualização e download. Desta forma, você pode baixá-los, ajustar ao seu negócio ou as suas necessidades e utilizá-lo no seu dia a dia!

#f2f2f2#f2f2f2

**[Clique aqui](https://git.fluig.com/projects/SAMPLES/repos/projetos/browse/evento-global-login-validacao-expiracao-senha)** para ver e baixar o código fonte dos desenvolvimentos desse processo.

Dica!

O arquivo **README.md** – existente no repositório – contém informações técnicas mais detalhadas. Ao longo dos próprios códigos fonte também existem várias explicações para auxiliar no entendimento e na utilização desse exemplo.
