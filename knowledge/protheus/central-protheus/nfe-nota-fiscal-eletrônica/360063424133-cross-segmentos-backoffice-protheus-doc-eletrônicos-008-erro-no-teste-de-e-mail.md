---
article_id: 360063424133
category: NFe - Nota Fiscal Eletrônica
content_hash: 244224071c2fc86ab8fc2a0cdb0894e085a8d93582e1dc98b68422bb2101a456
fetched_at: '2026-06-28T22:40:03.132803+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  008 - erro no teste
  de e-mail de envio
type: support-article
updated_at: '2026-03-04T18:21:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063424133-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-008-erro-no-teste-de-e-mail-de-envio
---

**Dúvida**Como corrigir o erro ao configurar o SMTP  008 - erro no teste de e-mail é apresentado ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

Ao configurar o **Wizard Config. na rotina de transmissão de notas** é apresentada a mensagem abaixo:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104215853)**

1- O erro **008 - erro no teste de****e-mail** é apresentado quando existe alguma configuração inconsistente  nos dados **do seu e-mail SMTP**

Neste caso, será necessário verificar com o seu **provedor de e-mail** quais as configurações corretas para:

Endereço de **SMTP e porta**

Conta de **e-mail e senha**

**Requer autenticação ?**

**Conexão segura SSL ?**

**Conexão segura TLS ?**

Após confirmar estas configurações com seu provedor **realize um novo teste de configuração.**

* **Saiba mais:**  
    
  **Segue exemplos** de configuração de **SMTP na rotina SPEDNFE** para alguns servidores **de e-mail:**  
   **Terra**  
  Servidor SMTP: smtp.terra.com.br:587  
  login do email: emailteste  
  Senha: \*\*\*\*\*\*  
  Conta de email: [emailteste@terra.com.br](mailto:emailteste@terra.com.br)  
  Autenticação requerida: Sim  
  Utiliza Conexão segura: Sim  
  Utiliza Conexão segura TLS: Sim  
    
  **Gmail**  
  Ao configurar o SMTP do provedor GMAIL, isso esta ocorrendo pois Google criou uma ferramenta de segurança que deve ser ativado no email no cliente para que seja possível o TSS autenticar com esse SMTP, segue abaixo link para ativação da ferramenta:  
    
  <https://www.google.com/settings/security/lesssecureapps>  
    
  \***Importante**A partir do dia **30 de maio de 2022,** o Google passa a exigir autenticação em 2 fatores para aplicativos que efetuam login no email, neste caso é necessario seguir os procedimentos descritos no video abaixo:  
    
    
    
  Servidor SMTP: smtp.gmail.com:587  
  Login do email: emailteste  
  Senha: **\*\*\*\*\*\***  
  Conta de e-mail: [emailteste@gmail.com](mailto:emailteste@gmail.com)  
  Autenticação requerida: Sim  
  Utiliza Conexão segura: Sim  
  Utiliza Conexão segura TLS: Sim  
    
  **Outlook**  
    
  Servidor SMTP: pod51028.outlook.com:587  
  login do email: [emailteste@suaempresa.com.br](mailto:emailteste@suaempresa.com.br)  
  Senha: **\*\*\*\*\*\***  
  Conta de email: [emailteste@suaempresa.com.br](mailto:emailteste@suaempresa.com.br)  
  Autenticação requerida: Sim  
  Utiliza Conexão segura: Sim  
  Utiliza Conexão segura TLS: Sim  
    
  **Locaweb**  
    
  Servidor SMTP:smtplw.com.br:587  
  login do email: emailteste  
  Senha: **\*\*\*\*\*\***  
  Conta de email: [emailteste@suaempresa.com.br](mailto:emailteste@suaempresa.com.br)  
  Autenticação requerida: Sim  
  Utiliza Conexão segura: Sim  
  Utiliza Conexão segura TLS: Sim
