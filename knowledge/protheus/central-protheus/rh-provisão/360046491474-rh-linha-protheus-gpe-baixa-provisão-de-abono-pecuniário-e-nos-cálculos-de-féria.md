---
article_id: 360046491474
category: RH - Provisão
content_hash: af63984dd4f7b46050f04e08113d0871de078cf7a17a67f3baade3ba5443a052
fetched_at: '2026-06-28T22:43:55.633561+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Baixa provisão de Abono Pecuniário e nos Cálculos
  de Férias
type: support-article
updated_at: '2025-11-03T12:02:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046491474-RH-Linha-Protheus-GPE-Baixa-provis%C3%A3o-de-Abono-Pecuni%C3%A1rio-e-nos-C%C3%A1lculos-de-F%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25949969803543) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como é realizada a baixa dos valores de Abono Pecuniário nas Provisões de Férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
O parâmetro **MV\_TPBXFER** determina se a baixa de férias na provisão ocorrerá de forma total no mês inicial das férias ou se será efetuado a baixa parcial conforme férias partidas.  
  
Sendo assim, quando o conteúdo do parâmetro estiver configurado com 1, a baixa será realizada de forma total no primeiro mês das férias, e quando está configurado com 2, a baixa será realizada de forma parcial, isto é, será dividida entre mês e mês seguinte.  
  
Quando há concessão de Abono Pecuniário, e o parâmetro MV\_TPBXFER estiver configurado com 2, o sistema poderá apresentar duas formas de Baixas.  
  
**Exemplo 1**: 20 dias férias e 10 dias de abono pecuniário (Férias iniciando em 10/09/2020 à 29/09/2020).  
Como não há dias de férias em Outubro (apenas abono pecuniário recairá no mês seguinte), a Baixa dos valores do Abono será realizada no mês de início das Férias, em Setembro.

**Exemplo 2**: 20 dias férias e 10 dias de abono pecuniário (Férias iniciando em 16/09/2020 à 05/10/2020).  
A baixa será realizada de forma parcial, dividida entre o 1º e 2º mês das férias.  
Ao calcular a provisão de férias em 09/2020, será realizada a baixa de 15 dias de férias e em 10/2020, será realizada a baixa de 5 dias de férias e 10 dias de abono.

**Saiba Mais**[MV\_TPBXFER](https://tdn.totvs.com/pages/releaseview.action?pageId=545632704#exemplos-2)   
[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
