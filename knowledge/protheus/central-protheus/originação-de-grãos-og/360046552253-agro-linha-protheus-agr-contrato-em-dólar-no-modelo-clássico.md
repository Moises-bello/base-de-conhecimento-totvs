---
article_id: 360046552253
category: Originação de Grãos (OG)
content_hash: 6769ff699b465d608b2136aefeba0c8715f79f4a28a1cb2fc35113d0bfdae443
fetched_at: '2026-06-28T22:45:38.838866+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Contrato em dólar no modelo clássico
type: support-article
updated_at: '2025-06-24T20:36:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046552253-Agro-Linha-Protheus-AGR-Contrato-em-d%C3%B3lar-no-modelo-cl%C3%A1ssico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20194205335959)**Tempo aproximado para leitura:**00:01:00 min**  
**Dúvida**Como incluir um **contrato em dólar** no modelo clássico?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Para incluir um contrato em moeda estrangeira, foi usado o **OGA290 - Contrato de Venda**, para outros tipos de contrato o procedimento é semelhante.  
Ao incluir um contrato em moeda estrangeira dólar, temos que informar no contrato, na pasta **Dados** **Negócios Financeiro**, no campo **Moeda** o tipo de moeda do contrato, que no caso é 2 dólares.

![CLASS.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7542239969559)

Em seguida, para que seja gerada notas em dólar tem que informar uma cotação, na tela de **Composição de Preços**.

![CLASS1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7542241334935)

Ao gerar um **OGA250 - Romaneio**, ao consultar a nota no **MATA920 - Notas Fiscais de Saída estão** com o preço o preço convertido em reais.

![CLASS2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7542193387031)
