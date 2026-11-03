---
article_id: 37775029286167
category: Meu RH - Login
content_hash: 273f828a1b4449c5e6ffa974132e806368d087c6d361cb0d856665d52163a3e7
fetched_at: '2026-06-28T22:47:27.220642+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: RH - RM - Meu RH - Erro "AADSTS700016" ao realizar login integrado com o Azure
type: support-article
updated_at: '2026-01-19T15:55:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37775029286167-RH-RM-Meu-RH-Erro-AADSTS700016-ao-realizar-login-integrado-com-o-Azure
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37775029274647) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao tentar realizar o login integrado no Meu RH com o Azure, é apresentado a seguinte mensagem de erro: "Message: AADSTS700016: Application with identifier 'xxxx' was not found in the directory 'Takenet'.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37775029276951)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**  
Esse incidente ocorre devido à parametrização do aplicativo externo, onde as informações de **Chave Pública** ou **Chave Privada** estão incorretas.  
  
**Solução**  
Para solucionar essa ocorrência, acesse no RM a aba **Gestão** > **Aplicativos**. Abra o aplicativo externo utilizado na integração, e atualize as credencias de **Chave Pública** e **Chave Privada.**

**Chave publica:** deverá informar o ID do aplicativo (Cliente) do Azure:

![](https://tdn.totvs.com/download/attachments/651942057/image2021-11-24_8-48-59.png?version=1&modificationDate=1637754540067&api=v2)

**Chave Privada:** deverá informar o Valor em Certificados e segredos do Azure:

![](https://tdn.totvs.com/download/attachments/651942057/image2021-11-24_8-52-5.png?version=1&modificationDate=1637866604813&api=v2)

**Saiba mais:**

[**Cross Segmentos - Backoffice RM - Integração - OAuth - RM x Azure: Configuração RM**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22590699409303-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-OAuth-RM-x-Azure-Configura%C3%A7%C3%A3o-RM)

[**RH - RM - Meu RH - Integração OAuth2, Meu RH X Microsoft Azure**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418231971991-RH-RM-Meu-RH-Integra%C3%A7%C3%A3o-OAuth2-Meu-RH-X-Microsoft-Azure)
