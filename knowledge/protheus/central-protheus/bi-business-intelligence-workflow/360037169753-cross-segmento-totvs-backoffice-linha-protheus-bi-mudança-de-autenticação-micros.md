---
article_id: 360037169753
category: BI - Business- Intelligence - Workflow
content_hash: d53805dd8b9680ba494be88724043b547fa2ccd7693f89cdadfc74cfe378d836
fetched_at: '2026-06-28T22:37:03.058991+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Mudança de autenticação
  Microsoft para o uso do Office365 no Workflow
type: support-article
updated_at: '2026-01-27T18:54:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037169753-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Mudan%C3%A7a-de-autentica%C3%A7%C3%A3o-Microsoft-para-o-uso-do-Office365-no-Workflow
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22678312241687)Tempo aproximado para leitura: **00:02:00min**  
  
**Dúvida**  
É possível utilizar o Workflow do Protheus com contas de e-mail do Microsoft Office 365?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - BI - Workflow - Todas as versões  
  
**Ocorrência**   
Devido às atualizações de segurança da Microsoft que descontinuaram o suporte à **Autenticação Básica (Basic Auth)**, a configuração nativa do Workflow (via módulo Configurador) tornou-se incompatível com contas do Microsoft Office 365 (Exchange Online).

**Contas Pessoais (Outlook.com, Hotmail, Live)**

* **Estado Atual:** A Microsoft implementou a "**Iniciativa Futuro Seguro**", que tornou obrigatória a Autenticação Moderna a partir de **16 de setembro de 2024**.
* **Impacto no Protheus:** Qualquer configuração nativa do Workflow que utilize um endereço `@hotmail.com` ou `@outlook.com` com a senha habitual do utilizador (ou mesmo senhas de aplicação antigas em protocolos depreciados) **deixou de funcionar**. O servidor **SMTP** recusa a conexão se esta não for feita via **OAuth2**.

O motor de Workflow legado do Protheus utiliza exclusivamente o protocolo de autenticação básica (usuário e senha) para o tráfego de mensagens. Atualmente, a Microsoft exige o uso de **Autenticação Moderna (OAuth2)**, bloqueando conexões que não utilizam tokens de segurança atualizados.

**Solução**   
Para restabelecer o envio de e-mails, deve-se adotar uma das alternativas abaixo:

* **1. Utilização de Provedores Alternativos** Uso de provedores de e-mail ou servidores **SMTP** locais que ainda permitam autenticação básica ou o uso de "Senhas de Aplicativo" (Ex.: Gmail com senha de app).
* **2. Customização via TLPP/AdvPL (Recomendado)** Substituição do processo de Workflow padrão pelo desenvolvimento de rotinas customizadas utilizando as classes de e-mail atualizadas da TOTVS (**TMailManager**, **TMailMessage**). Estas classes possuem suporte nativo para autenticação moderna via Token (**OAuth2**) através dos métodos `SetOAuthToken` e `cOAuthToken`.

**Passos:**  
Caso opte pela adaptação via customização (**AdvPL**), siga a lógica de implementação abaixo:

1. Utilize a classe `TMailManager` para estabelecer a conexão.
2. Implemente o método `SetOAuthToken` para validar a autenticação moderna junto à Microsoft.
3. Realize o envio da mensagem através da classe `TMailMessage`.

**Saiba mais:**  
[Os Métodos de Autenticação Modernos, aplicações de e-mail não Microsoft](https://support.microsoft.com/pt-br/office/os-m%C3%A9todos-de-autentica%C3%A7%C3%A3o-modernos-agora-necess%C3%A1rios-para-continuar-a-sincronizar-o-e-mail-do-outlook-em-aplica%C3%A7%C3%B5es-de-e-mail-n%C3%A3o-microsoft-c5d65390-9676-4763-b41f-d7986499a90d)  
[Substituição da Autenticação básica no Exchange Online](https://learn.microsoft.com/pt-br/exchange/clients-and-mobile-in-exchange-online/deprecation-of-basic-authentication-exchange-online)  
[Configuração Básica de conta para envio de WorkFlow pelo Gmail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037067513-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Configura%C3%A7%C3%A3o-B%C3%A1sica-de-conta-para-envio-de-WorkFlow-pelo-Gmail)  
[Application Server - E-mail - Office+365](https://tdninterno.totvs.com/display/tec/Application+Server+-+E-mail+-+Office+365)  
[TMailMessage - Envio do Email](https://tdn.totvs.com/display/tec/Classe+TMailMessage)  
[TMailMangager - SetOAuthToken](https://tdn.totvs.com/display/tec/TMailManager%3ASetOAuthToken)  
[TMailMng - cOAuthToken](https://tdn.totvs.com/display/tec/TMailMng%3AcOAuthToken)
