---
article_id: 18893492234903
category: LOGIN
content_hash: 1ed730532564fa71d5f738c22fde46de14b43f3e4eaf9f963c14cc5708009c06
fetched_at: '2026-06-28T22:44:40.476394+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - Meu RH - É possível na mesma configuração do Meu RH,
  termos uma conexão interna e uma conexão externa
type: support-article
updated_at: '2026-06-23T21:20:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18893492234903-RH-Linha-Protheus-Meu-RH-%C3%89-poss%C3%ADvel-na-mesma-configura%C3%A7%C3%A3o-do-Meu-RH-termos-uma-conex%C3%A3o-interna-e-uma-conex%C3%A3o-externa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18893521347351) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**É possível na mesma configuração do Meu RH, termos uma conexão interna e uma conexão externa?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**Quando é realizado mais de uma configuração, **para o Meu RH no appserver.ini**, sendo uma **conexão interna como** *localhost* **ou o IP interno do servidor**, e outra **conexão externa via IP externo ou DNS**, também é necessário **termos *URL's* diferentes do serviço *REST*** e, consequentemente **pastas diferentes dentro da protheus\_data\web**.  
  
Conexão interna e externa no mesmo *appserver.ini*:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29900436484503)  
  
Pasta \*web*:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29900436485399)  
  
*URL* do *REST* configurada no arquivo *properties.json* da pasta PortalMeuRH01:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29900436486295)  
  
URL do REST configurada no arquivo *properties.json* da pasta PortalMeuRH01\_ext:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29900436487063)  
  
Ou seja, cada pasta terá seu *REST* correspondente e conforme a conexão:

* IP *localhost* 127.0.0.1 - aponta para a pasta PortalMeurh01 - nela temos um *properties.json* com a *URL* do *REST* também como 127.0.0.1
* *DNS* meurh.totvs.com.br - aponta para a pasta PortalMeurh01\_ext - nela temos um *properties.json* com a *URL* do *REST* também com *DNS* - meurh.totvs.com.br

**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
