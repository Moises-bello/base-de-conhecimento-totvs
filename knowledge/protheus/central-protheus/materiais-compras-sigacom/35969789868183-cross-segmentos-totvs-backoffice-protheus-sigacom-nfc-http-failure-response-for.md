---
article_id: 35969789868183
category: Materiais - Compras (SIGACOM)
content_hash: e7de8a22e4afb0a1c03972a049d8163dff198b2fd383694bd0c1cf9f89f9548f
fetched_at: '2026-06-28T22:41:21.814604+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Http failure
  response for http://linknfc 401 Unauthorized
type: support-article
updated_at: '2026-02-05T18:07:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35969789868183-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Http-failure-response-for-http-linknfc-401-Unauthorized
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35969789851159) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Ao enviar email da cotação para os fornecedores via Workflow no Novo Fluxo de Compras, sistema gera erro Http failure response for http://linknfc 401 Unauthorized. Como corrigir?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35969761342871)  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2310  
  
**Solução**  
Para corrigir esse erro, efetue os dois procedimentos abaixo:

**1º passo:** Por gentileza realize teste em ambiente de Homologação com as atualizações a seguir:

- [Acumulado Compras conforme sua versão](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)  
- [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526) | [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168735)

Obs: Recomendamos backup e validação primeiramente em ambiente teste.

**2º passo:****Acesse o cadastro dos fornecedores** participantes dessa cotação e verifique se há caracteres especiais na **Razão Social** ou **Nome Fantasia**. Se houver, **r****emova o caractere especial** identificado (por exemplo, o símbolo **&**), **s****alve as alterações** e **realize um novo teste** no processo de cotação. **Valide** se o problema foi solucionado.

Conforme demonstra na documentação: [Cadastro de fornecedor - Retirada de caracteres especiais](https://tdn.totvs.com/display/public/PROT/DT+Cadastro+de+fornecedor+-+Retirada+de+caracteres+especiais), o time de produto realizou um tratamento para que caracteres especiais sejam removidos da rotina de cadastro de fornecedores. Portanto se trata de um novo comportamento do sistema. As rotinas do NFC não permitirão caracteres especiais.

***Saiba Mais:***

[Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
