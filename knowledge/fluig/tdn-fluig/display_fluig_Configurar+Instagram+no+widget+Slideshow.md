---
content_hash: e262a99d3a9637f2c4215833c7a934c8afacfdd8039eaa33c1ac2548ad2a6fbb
fetched_at: '2026-06-28T21:35:24.973669+00:00'
page_id: '273310668'
product: fluig
source: tdn-fluig
title: Configurar Instagram no widget Slideshow
type: documentation
url: https://tdn.totvs.com/display/fluig/Configurar+Instagram+no+widget+Slideshow
version: 27
---

# Índice

4true.\*ndicenone

# Objetivo

---

O objetivo deste guia é orientar os desenvolvedores sobre como realizar a integração de uma conta do Instagram com o *widget Slideshow* do Kit Intranet. Lembrando que não há suporte para a configuração de múltiplas contas no *widget* *Slideshow* padrão.

# Widget Slideshow

---

Para exibir imagens de uma conta do Instagram, é necessário selecionar a opção **Instagram** no campo **Este *Widget* Integra com** nas propriedades do *widget* *Slideshow* e publicar a página para salvar a configuração.

**Propriedades do widget Slideshow do Kit Intranet**

# Serviço REST servico

---

Ao importar o Kit Intranet com o *widget* *Slideshow*, é criado automaticamente um serviço de demonstração do Instagram (instagram.demo) na página  do Painel de Controle do Fluig. Embora seja apenas um exemplo, este serviço pode ser adaptado por um desenvolvedor para exibir as fotos de outra conta desta rede social.

Para isso, é necessário obter os seguintes dados da conta desejada e substituí-los nas propriedades do serviço instagram.demo:

* *Client* ID (ID cliente)
* Token de acesso (*Access token*)

**Propriedades do serviço REST instagram.demo**

# Obter dados do Instagram

---

Importante

Os procedimentos abaixo são de responsabilidade do fornecedor (Instagram), não da plataforma Fluig, e portanto estão sujeitos à alteração sem aviso prévio.

O *widget* *Slideshow* realiza a autenticação com o Instagram através do protocolo OAuth 2.0, portanto é necessário possuir uma conta no portal do desenvolvedor deste serviço ([developers.facebook.com](https://developers.facebook.com/)) para obtenção dos dados de integração*: Client* ID, *Client Secret* e *Access Token*.

Na documentação abaixo, será apresentado uma das formas de obtenção destes dados como exemplo para os desenvolvedores que desejam utilizar essa integração.

### Criar aplicativo do Facebook

Antes de configurar seu Client ID e Client Secret é necessário criar um aplicativo do Facebook e a partir dele, ir adicionando os produtos como o **Exibição básica do Instagram**. O material para consulta pode ser encontrado em: <https://developers.facebook.com/docs/instagram-basic-display-api>. 

Antes de prosseguir para os próximos passos é necessário criar um usuário teste e autenticar, para isso siga a [etapa 3 e etapa 4](https://developers.facebook.com/docs/instagram-basic-display-api/getting-started#etapa-3--adicionar-um-usu-rio-de-teste-do-instagram) da documentação do fornecedor

### Client ID e Client Secret client\_id

Após o cadastro no portal de desenvolvedor do Facebook, o desenvolvedor poderá registrar um novo produto, para o qual serão fornecidos o ***Client* ID** e ***Client Secret***.

new clientRegistrar novo cliente

**Tela de registro de novo produto no aplicativo**

Caso o único objetivo deste cliente seja obter os dados para integração do Instagram com o *widget* *Slideshow*, a URL do servidor Fluig pode ser informada no campo ***Configurações de OAuth do cliente***. O endereço preenchido nesse campo será utilizado mais adiante para gerar o token de acesso (*access token*).

Propriedades do cliente

**O Client ID e Client Secret estarão o disponíveis após o registro do cliente**

Antes de prosseguir para os próximos passos é necessário criar um usuário teste e autenticar, para isso siga a [etapa 3 e etapa 4](https://developers.facebook.com/docs/instagram-basic-display-api/getting-started#etapa-3--adicionar-um-usu-rio-de-teste-do-instagram) da documentação do fornecedor.

### Token de Acesso token

Siga os passos abaixo para obter o *token* de acesso.

access tokenPasso 1

* Abra uma nova aba do navegador e informe a URL abaixo, substituindo CLIENT-ID pelo Client ID obtido anteriormente e REDIRECT-URI pela URL de redirecionamento informada no cadastro do cliente.

Passo 2

* Ao acessar esta URL, o navegador será redirecionado para o endereço abaixo, de onde poderá ser copiado o **Code**, disponível no final da URL (CODE):

* Exemplo de URL com o code gerado.

Ao capturar o code os caracteres **#\_** no final devem ser retirados.Passo 3

* Com o code em mãos é hora de obter o access code, para isso utilize algum aplicativo que aceita solicitações de cURL e realize a seguinte requisição POST. Na URL fazer a troca dos respectivos parâmetros **Client-id, Cliente-Secret, Code e Redirect-Url**

* O retorno deve ser um JSON semelhante a esse:

Caso utilize o Postman passe os parâmetros no **body**, e não em params. Certifique-se de que a x-www-form-urlencoded esteja habilitada

Uma vez de posse do ID Cliente, *Client Secret* e Token de acesso, basta substituí-los no serviço **instagram.demo** na página de  do Painel de Controle para que as imagens da conta do Instagram sejam exibidas no *widget* *Slideshow*.

Dúvidas?

Caso tenha dúvidas ou problemas relacionados à obtenção dos dados de autenticação do Instagram, consulte a [documentação completa](https://www.instagram.com/developer/authentication/) do fornecedor.
