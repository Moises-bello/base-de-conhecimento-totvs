---
content_hash: 7a2699b7bbc6613996a35018f488902f04dfcbc96c4def92516d52859d926ee4
fetched_at: '2026-06-29T00:10:22.095001+00:00'
page_id: '496396386'
product: rm
source: tdn-rm
title: Integração do aplicativo do ADFS (Azure) com o RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496396386
version: 12
---

# Índice:

---

.\*ndice:

# Objetivo

---

       A seguir será apresentado como configurar uma conexão oauth com o ADFS (Azure)

       Para mais informações sobre as opções de login, acesse o .

Importante

Não iremos mostrar nessa documentação como criar um aplicativo no ADFS, somente como integrar um ADFS já configurado com o RM.  
Por se tratar de uma customização na integração entre sistemas, sugerimos que verifique com a equipe responsável pelo desenvolvimento da mesma quais informações deverão ser preenchidas, pois o documento serve apenas como um guia e as configurações são de responsabilidade do cliente.

# Configurando o RM para integrar com o ADFS (Azure)

---

O modelo para a integração do ADFS (Azure) é mostrado abaixo através da imagem:

Urls de Retorno com Letras Maiusculas

Atenção a urls de retorno que contenham letras em maiusculo. Verificar se a url de retorno cadastrada no RM é o mesmo cadastrado no aplicativo do ADFS.

## Informações Variáveis

---

| ID | Nome | Descrição |
| --- | --- | --- |
| **1** | **{chave\_publica}** | Identificação do aplicativo externo. (Client Id). |
| **2** | **{chave\_privada**} | Chave secreta do aplicativo externo. (Client Secret) |
| **3** | **{tenant}** | Identificador da Empresa no ADFS. |
| 4 | **{url\_de\_retorno}** | Url de Retorno. Essa url tem que estar cadastrada também no ADFS. Dê preferência a URLS próprias, sem quaisquer redirecionamentos. |
| 5 | **{nome\_do\_provider}** | Nome do Provider. |

## Informações Fixas

---

| ID | Nome | Descrição |
| --- | --- | --- |
| **1** | **Provedor do aplicativo** | Obrigatoriamente para esse caso, o valor será **(0 - Custom)** |
| **2** | **Url de Autorização** | Url para recuperar o código de autorização para o aplicativo. Obrigatoriamente para esse caso, o valor será **(<https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize>)** |
| **3** | **Url de Recuperação do Token de Acesso** | Url para recuperar o token de acesso para o aplicativo. Obrigatoriamente para esse caso, o valor será **(<https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token>)** |
| **4** | **Url de Recuperação de Informações da Conta do Usuário** | Url para recuperar as informações do usuário que serão utilizadas na sincronização com o usuário do RM. Obrigatoriamente para esse caso, o valor será **(<https://graph.microsoft.com/v1.0/me>)** |
| **5** | **Escopo Padrão** | Escopo de Permissões utilizado pelo aplicativo. Obrigatoriamente para esse caso, o valor será **(user.read)** |
| **6** | **Campo de Correspondência do Provedor** | Para realizar a sincronização entre os usuários do aplicativo e do RM, um campo de correspondência deve ser escolhido. Obrigatoriamente para esse caso, o valor será **(1 - Email)** |

# Configurando as Correspondências entre Usuários

---

Após configurar a integração do aplicativo externo com o RM, agora temos que configurar a correspondência entre os usuários do RM e Aplicativos Externos.

Escolha o usuário que será sincronizado com o usuário do aplicativo externo. Lembre-se que o campo de correspondência para o ADFS (Azure) é o E-mail.

## Informações Variáveis

---

| ID | Nome | Descrição |
| --- | --- | --- |
| **1** | **{email\_a\_ser\_sincronizado}** | O mesmo e-mail utilizado no login do aplicativo do Azure tem que ser cadastrado no usuário que será sincronizado. |

## Verificar Sincronização de Usuários

---

Para verificar se a correspondência entre o usuário do ADFS e do RM foi realizada corretamente, ir em << Aplicativos Externos >> <<Anexos>> <<Correspondência entre Usuários>>.

## 

Observe que no formulário <<Correspondência entre Usuários>>, tem três campos:

| ID | Nome | Descrição |
| --- | --- | --- |
| **1** | **Identificador do Aplicativo** | Identificador do Aplicativo Externo no RM. **Disponível em <<Aplicativos Externos>> | Aba: Identificação | Campo: ID** |
| **2** | **Identificador do Usuário no Provedor** | Identificador do Usuário no ADFS (Azure). **Disponível na Configuração de Usuários do Próprio Azure.** |
| **3** | **Identificador do Usuário no RM** | Identificado do Usuario na Biblioteca RM (MDI). **Disponível em: <<Usuários>> | Aba: Identificação | Campo: Usuário** |

# Particularidades nos produtos RM em relação aos tipos de resposta (Oauth)

---

Para a MDI e o Portal (Corpore RM), o tipo de resposta é "CODE".

Para o portal educacional, o tipo de resposta é "TOKEN".

Para contemplar esses dois fluxos, configurar o ADFS da seguinte forma:

1) No aplicativo cadastrado no ADFS, vá em **"Manifest"**. Um editor JSON irá se abrir.

2) Procure o parâmetro **"oauth2AllowImplicitFlow"**.

3) Mude o valor desse parâmetro de **"false"**para **"true"**. Caso o parâmetro não exista, basta adicioná-lo.
