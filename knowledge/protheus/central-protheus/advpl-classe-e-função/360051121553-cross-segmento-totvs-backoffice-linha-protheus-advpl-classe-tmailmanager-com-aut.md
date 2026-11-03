---
article_id: 360051121553
category: ADVPL - Classe e Função
content_hash: 17c05eea35d6ecbde57049f846aa1dcec6cec43012f7f05091c4664b905fdbb4
fetched_at: '2026-06-28T22:40:15.445947+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Classe TMailManager
  com autenticação OAuth
type: support-article
updated_at: '2024-06-14T19:01:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051121553-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classe-TMailManager-com-autentica%C3%A7%C3%A3o-OAuth
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**A classe **TMailManager** só consegue autenticar no servidor se a opção acesso de aplicativos menos seguros" estiver habilitada (**LSA - less secure apps**). Esta opção será descontinuada pelo Google em 2021, e deve ser autenticado por **OAUTH**, existe alguma opção de **OAUTH** para a classe?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.33  
  
**Solução**Foi Implementado na classe **TMailManager** o método **SetOAuthToken**, que define o token **OAuth2** que será utilizado para os protocolos IMAP, POP e SMTP, e implementada na classe **TMailMng** a propriedade **cOAuthToken**, que permitirá definir e ler o token **OAuth2**que será utilizado. Sendo necessário a atualização do binário para versão 20.3.0.14.  
  
**Saiba mais**  
[TMailManager:SetOAuthToken](https://tdn.totvs.com/display/tec/TMailManager%3ASetOAuthToken)   
[Application Server - E-mail - Office 365](https://tdn.totvs.com/display/tec/Application+Server+-+E-mail+-+Office+365)
