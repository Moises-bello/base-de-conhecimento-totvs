---
article_id: 360047906813
category: Call Center - Help Desk
content_hash: 548e898ed1247b305761f4d6fa3ff90c9e73112e7797e033edaf14950ac6b106
fetched_at: '2026-06-28T22:41:27.637648+00:00'
product: protheus
section_id: 1500001537181
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Configuração Básica para
  efetuar o atendimento na Central de Serviços
type: support-article
updated_at: '2024-04-25T14:05:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047906813-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Configura%C3%A7%C3%A3o-B%C3%A1sica-para-efetuar-o-atendimento-na-Central-de-Servi%C3%A7os
---

**Dúvida**

Qual a configuração para conseguir gerar um atendimento na Central de Serviços(TMKA510a)?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12

**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

1 - No padrão do sistema, já existe um Serviço Padrão ( **Modelo de Atendimento**-

**CFGX503**) para uso, basta incluir no grupo de atendimento;

2 - Associar o Grupo de Atendimento com o Operador, e garantir que seu atendimento seja para ***Todos os atendimentos ou só Service Desk***;

3 - Em Telemarketing, criar uma **Ocorrência**, uma **Ação** e associar os cadastros para que possa ocorrer o Atendimento na Central de Serviços( **antigo Service Desk** );

4 - Em Help Desk, ***Assunto x Grupo(******TMKA510B)***, associe o Grupo de Atendimento com a tabela de Assunto, Service Desk( **SKK**);

5 - Acesse Atendimento, **Central de Serviços**( ***antigo Service Desk***), e efetue a inclusão de um atendimento, através de Outras ações, Incluir;

![](https://tdn.totvs.com/download/attachments/547850583/incl%20atend%20serv%20desk.gif?version=1&modificationDate=1588775255519&api=v2)

6 - Veja que o atendimento foi incluído.

**Obs: Para acesso as demais telas de configuração, acesse:**

**[**TMK0076\_Configuração\_Básica\_para\_efe**tuar\_o\_atendimento\_na\_Central\_de\_Serviços](https://tdn.totvs.com/pages/viewpage.action?pageId=547850583)**
