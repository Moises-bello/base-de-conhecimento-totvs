---
article_id: 7806581755543
category: Metrologia (SIGAQMT)
content_hash: f523aa2179882fc29e4d3eac482c20b9a0478a68fdecad55eea1d6f01869db6c
fetched_at: '2026-06-28T22:42:24.838202+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - QMTA010 - Help A010NEXCI
type: support-article
updated_at: '2022-07-29T18:19:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7806581755543-Manufatura-Linha-Protheus-SIGAQMT-QMTA010-Help-A010NEXCI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No módulo **SIGAQMT - Metrologia**, ao tentar excluir um instrumento na rotina **QMTA010 - Instrumentos** é apresentado o *help* **A010NEXCI**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Causa**Este *help* ocorre quando já existem medições relacionadas à este instrumento, realizadas na rotina **QMTA140 - Medições** e registradas na tabela **QM6 - Cabeçalho de Calibração**.  
  
**Solução**Para que seja permitido excluir um instrumento, o mesmo não deve ter calibração registrada na rotina **QMTA140** e também deve-se verificar o conteúdo do parâmetro **MV\_QAPQIEP - Antes da deleção do instrumento, verifica se os mesmos não estão sendo utilizados nos ambientes Inspeção de Entrada e Inspeção de Processos**. Se o parâmetro possuir conteúdo igual à **1**, serão verificados os registros relacionados deste instrumento nas tabelas **QET - Instrumentos x Resultados** e **QPT - Instrumentos Utilizados Medições**, caso contrário, a validação não será realizada.
