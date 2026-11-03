---
article_id: 22064256194967
category: RH - Provisão
content_hash: 759321a1ee899d32807d6652207b43d9fad3ec762e0cfa2ff48210ccb07f8f6e
fetched_at: '2026-06-28T22:43:56.853594+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Valores negativos de INSS e FGTS na provisão de
  férias para funcionários que gozaram férias no período
type: support-article
updated_at: '2025-08-21T12:45:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22064256194967-RH-Linha-Protheus-GPE-Valores-negativos-de-INSS-e-FGTS-na-provis%C3%A3o-de-f%C3%A9rias-para-funcion%C3%A1rios-que-gozaram-f%C3%A9rias-no-per%C3%ADodo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22064256182295) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Valores negativos de INSS e FGTS na provisão de férias para funcionários que gozaram férias no período  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**Ao efetuar o cálculo da provisão de férias , o sistema valida férias para 30 dias e sobre esses dias os encargos.   
  
Quando o funcionário tira 20 dias de férias e 10 dias de abono, **os 10 dias de abono não incidem FGTS e INSS** e desta forma como já foram provisionados e contabilizados, o sistema precisa abater no saldo contábil e por isso apresenta os valores negativos. Esses valores devem ser contabilizado conforme instrução abaixo:   
[RH - Linha Protheus - GPE - Como contabilizar valores negativos de provisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018522692-RH-Linha-Protheus-GPE-Como-contabilizar-valores-negativos-de-provis%C3%A3o)

Abaixo o comportamento da rotina de acordo com o conceito de provisão:  
  
1) Cálculo de férias 20 dias com abono pecuniário de 10 dias:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22373063268375)

2) No relatório de provisão é apresentado o desprovisionando dos valores de INSS e FGTS que não incidem sobre abono, de modo que ocorra o ajuste de saldo no contábil:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22373086703639)

**Saiba mais:**  
Para adquirir mais conhecimento e consultar incidências como apoio na configuração das verbas acesse o(s) *link*(s) abaixo:  
<https://tdn.engpro.totvs.com.br/download/attachments/234616759/TABELA%20INCIDENCIA%20-%20PDF.pdf?version=1&modificationDate=1567195001287&api=v2>
