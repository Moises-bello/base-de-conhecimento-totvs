---
content_hash: d539f32264cf3eaabe2c9cd8589f7aa3a92c8e1613e316ea2f77a8a58302b76b
fetched_at: '2026-06-28T21:35:22.269801+00:00'
page_id: '235337765'
product: fluig
source: tdn-fluig
title: Identity | Autenticação CAS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235337765
version: 40
---

# Falando de autenticação CAS...

---

Para empresas que possuem um servidor de autenticação CAS *(Centralized Authentication System)*, o Identity permite utilizar o serviço existente de autenticação para autorizar o acesso aos seus recursos. O objetivo é permitir que um servidor CAS seja o responsável pela autenticação e provisionamento de usuários ao Identity.

Nas empresas em que autenticação CAS tenha sido habilitada, o recurso de [Autenticação multifator](https://tdn.totvs.com/x/J5LpEg) não poderá ser utilizado.

## Habilitar autenticação CAS

---

**[Assista ao vídeo](https://tdn.totvs.com/download/attachments/235337765/Cas.gif?version=2&modificationDate=1654004650172&api=v2)**

Para realizar essa configuração, é necessário possuir um servidor CAS instalado e configurado.

**01.**Acione o ícone **Configurações**no canto superior direito e selecione a opção **Segurança**. 

**02**. Acesse o recurso **Autenticação CAS.**

**03**. Marque o recurso **Habilitar autenticação CAS** para definir se será habilitada a autenticação CAS.

**04.** Caso a autenticação CAS tenha sido habilitada, preencha os campos abaixo.

#f2f2f2#f2f2f2

**Selecione o servidor CAS**  
Informe a versão do protocolo a ser utilizada (CAS 2.0 ou CAS 3.0).

**Selecione o Tipo de validação**Informe se o fluxo utilizado será Proxy Validade ou Service Validate.

**URL do serviço CAS de sua empresa**Informe a url do serviço CAS de sua empresa.

**Campo de seu CAS Response que representa o nome do usuário**Informe o campo que representa o nome do usuário no CAS Response.

****Campo de seu CAS Response que representa o sobrenome do usuário****Informe o campo que representa o sobrenome do usuário no CAS Response.

****Campo de seu CAS Response que representa o e-mail do usuário****Informe o campo que representa o e-mail do usuário no CAS Response.

**O sobrenome do usuário está informado no campo nome**Ao assinalar esta opção, o campo do sobrenome do usuário não ficará visível em tela, podendo ser informado direto pelo campo nome.

**04.** Após o preenchimento dos campos, acione **Salvar** para confirmar as informações.

#f2f2f2#f2f2f2

Caso haja algum erro relacionado ao redirecionamento do IDM após o login CAS com sucesso, será apresentado uma tela reportando a falha no login. Por exemplo, quando o e-mail principal não estiver corretamente cadastrado no parâmetro de habilitação do CAS, será apresentada a tela demonstrando o motivo da falha no login.**Veja a** **i****magem**

Após concluir a configuração, ao abrir a página de login do Identity, a tela do CAS será apresentada no lugar da tela padrão do TOTVS Identity.  **Veja a** **i****magem**

Ao efetuar *logoff*, dependendo da configuração do servidor CAS, o usuário será redirecionado para a página de sessão encerrada do CAS.  **Veja a** **i****magem**

]]>

## JSON do CAS Response

---

Para que a integração com o CAS seja feita com sucesso, é necessário que o JSON encodado no CAS Response esteja no seguinte formato:

Sendo os valores representativos:

| Campo | Descrição |
| --- | --- |
| rgUf | União federativa, estado |
| localidade | Cidade de localização |
| matricula | Identificador para o servidor CAS |
| emailCorporativo | E-mail do usuário / Login para o Identity |
| nome | Nome do Usuário |
| sobrenome | Sobrenome do Usuário |
| nomeComum | Nome para o sistema |

$("b:contains('oculto')").parent().parent().hide();
]]>
