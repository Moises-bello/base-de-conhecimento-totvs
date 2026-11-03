---
article_id: 1500009129162
category: RH - Provisão
content_hash: 347cb094482fef57f70aa40075c6ed7586aac2007038132e14dcec8fc229cf1e
fetched_at: '2026-06-28T22:43:55.566307+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus  - GPE - Valores negativos de INSS e FGTS na provisão de
  férias para funcionários demitidos
type: support-article
updated_at: '2024-07-19T18:11:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009129162-RH-Linha-Protheus-GPE-Valores-negativos-de-INSS-e-FGTS-na-provis%C3%A3o-de-f%C3%A9rias-para-funcion%C3%A1rios-demitidos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25020812875159) Tempo aproximado para leitura: 00:02:00 min  
  
Ocorrência**No cálculo da provisão de férias, os valores de FGTS e INSS são apresentados negativos para funcionários que foram demitidos no mês.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Causa**Quando o parâmetro MV\_PROVRES está configurado com S, os valores dos encargos nas provisões de férias são apresentados negativos na linha "No Mês" uma vez que em rescisão não há incidência de FGTS e INSS para férias indenizadas.  
  
**Solução**1. Parâmetro MV\_PROVRES:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25020715452823)

2. Veja no Relatório de Provisão, que como não há recolhimento de INSS Patronal, nem depósito de FGTS sobre as férias indenizadas em rescisão, os encargos provisionados até o mês anterior é apresentado com valor negativo na linha "No Mês", para que o saldo Atual seja zerado:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500015973481)

Para mais informações sobre o parâmetro MV\_PROVRES [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007260472-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Provis%C3%A3o-no-m%C3%AAs-de-Desligamento#:~:text=O%20par%C3%A2metro%20MV_PROVRES%20possibilita%20ao,m%C3%AAs%20de%20demiss%C3%A3o%20do%20empregado.&text=Como%20n%C3%A3o%20est%C3%A1%20sendo%20provisionado,valor%20provisionado%20no%20m%C3%AAs%20anterior).

**Saiba mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
