---
article_id: 360025728233
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 9f22d250a819c59f4b88cd5cba06e7e032e376903270a9fd5bc06c3ee1d8f8d8
fetched_at: '2026-06-28T22:39:44.326888+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Cálculo da Variação
  Cambial
type: support-article
updated_at: '2023-10-11T12:37:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025728233-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-C%C3%A1lculo-da-Varia%C3%A7%C3%A3o-Cambial
---

**Dúvida**Cálculo da Variação Cambial das despesas 701,702 e 703  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**A variação é calculada com a taxa na cotação de moeda  cadastrada para a data do desembaraço de acordo com  parâmetro MV\_DT\_VAR = W6\_DT\_DESE, subtraindo da taxa informada na invoice no campo W9\_TX\_FOB.   
  
Exemplo:   
Cotação de venda informada na data de 01/06/2019=3,50 na data do Desembaraço de acordo  com o campo" W6\_DT\_DESE"  
Taxa da invoice US$= 3,9673 na inclusão da Invoice de acordo campo "W9\_TX\_FOB".  
  
Em processo de US$ 100,00   
Cotação do dia - US$ 100,00 x 3,5000 = R$ 350,00  
Taxa da invoice - US$ 100,00 x 3,9673 = R$ 396,73  
  
Variação cambial R$ 396,73 - 350,00 = 46,73

No cenário de uma "Variação Cambial Financeira", a maioria das empresas utilizam da seguinte forma:  
Parâmetro MV\_EIC0013 = F (Quando desligado leva a taxa informada na invoice para o titulo gerado no Financeiro)  
Desta forma ao baixar o titulo no cambio o próprio Financeiro ira calcular a "Correção Monetária" e poderá ser contabilizada pelo LP de correção do modulo Financeiro.
