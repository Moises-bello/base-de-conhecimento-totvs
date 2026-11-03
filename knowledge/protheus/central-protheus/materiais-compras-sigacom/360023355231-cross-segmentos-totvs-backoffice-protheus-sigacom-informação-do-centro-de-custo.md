---
article_id: 360023355231
category: Materiais - Compras (SIGACOM)
content_hash: 25ccd4dbca3389dbec2a4b99150536bf7d68254675daec09c548c35ca921d0cc
fetched_at: '2026-06-28T22:41:08.968481+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Informação do centro
  de custo no Documento de Entrada não é carregado para o título a pagar
type: support-article
updated_at: '2025-10-08T21:24:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023355231-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Informa%C3%A7%C3%A3o-do-centro-de-custo-no-Documento-de-Entrada-n%C3%A3o-%C3%A9-carregado-para-o-t%C3%ADtulo-a-pagar
---

**Dúvida**

**Por que a informação do centro de custo que consta no documento de entrada, não é carregado para o título a pagar, e apresentado na rotina FINA050 ?**

**Ambiente**Protheus - Compras - A partir da versão 11.08  
  
**Solução**

Por padrão, o sistema não leva a informação do campo D1\_CC para o campo E2\_CCUSTO, quando o título é gerado pelo documento de entrada, bem como as demais entidades Contábeis informadas na NF, pois a nota pode conter vários itens e em cada item, podem ter entidades diferentes, ou seja, centro de custos diferentes, visto que essa informação é preenchida no item da nota. Neste caso haveria conflito para gravar apenas um Centro de Custo no Financeiro.

Devido ser conceitual, a saída sugerida é tratar a gravação da informação, por meio de implementação de ponto de entrada.

**MT100GE2 - Complementa a Gravação dos Títulos Financeiros a Pagar  
Link: <http://tdn.totvs.com/pages/viewpage.action?pageId=6085781>**

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
