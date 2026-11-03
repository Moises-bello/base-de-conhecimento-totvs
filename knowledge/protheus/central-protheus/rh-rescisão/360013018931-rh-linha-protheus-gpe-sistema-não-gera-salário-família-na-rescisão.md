---
article_id: 360013018931
category: RH - Rescisão
content_hash: 0d19464ee19dc1bd4cc43db34f45ece1180db64eeb0aadbf152fea45f0ba6b4a
fetched_at: '2026-06-28T22:43:54.466905+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não gera salário família na rescisão
type: support-article
updated_at: '2025-04-16T13:59:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013018931-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-gera-sal%C3%A1rio-fam%C3%ADlia-na-rescis%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26735538553367)***Tempo aproximado para leitura: **00:01:00 min**

**Dúvida****GPEM040 -**Sistema não gera salário família na rescisão  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Primeiramente deverá ser analisado se o salário contratual do empregado, no **Cadastro do Funcionário**, no campo RA\_SALARIO é superior ao valor informado na **Tabela S003**, se sim, neste momento o empregado já perdeu o direito ao recebimento do benefício, mesmo que os valores gerados na rescisão sejam inferiores ao informado na S003.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26735563774999)  
  
Se o salário RA\_SALARIO for menor e o cadastro de verbas estiver com verbas configuradas com sim para Salario Família, o cliente deverá validar se o salário mais as verbas ultrapassam o limite estabelecido na S003.

O **id 0048 não** deve conter incidência para salário família.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26735538569239)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26735563786007)

**Saiba mais**  
Para adquirir informações adicionais, acesse o *link*:

<https://tdn.totvs.com/pages/releaseview.action?pageId=390403744>

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
