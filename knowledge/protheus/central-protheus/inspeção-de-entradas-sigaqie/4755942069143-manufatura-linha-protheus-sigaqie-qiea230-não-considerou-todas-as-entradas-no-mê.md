---
article_id: 4755942069143
category: Inspeção de Entradas (SIGAQIE)
content_hash: b756a9c277098d219239b823377692a769fbee96f4c36e99f5aae21b0b776600
fetched_at: '2026-06-28T22:42:27.149481+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - QIEA230 - Não considerou todas as entradas
  no mês
type: support-article
updated_at: '2022-03-15T11:35:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4755942069143-Manufatura-Linha-Protheus-SIGAQIE-QIEA230-N%C3%A3o-considerou-todas-as-entradas-no-m%C3%AAs
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:40 min** **Dúvida**Por que ao executar a rotina **QIEA230 - Índices de Qualidade** não foram consideradas todas as entradas do fornecedor no mês indicado para processamento?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**Ao executar a rotina **QIEA230** serão consideradas as entradas cujo o laudo tenha sido realizado no mês selecionado para processamento, independente da data em que a nota foi incluída, levando em consideração as datas:  
**QEL\_DTENTR - Data Entrega = QEK\_DTENTR - Data Entrega**  
**QEL\_DTLAUD - Data Laudo >= primeiro dia do mês informado para processamento**  
**QEL\_DTLAUD <= último dia do mês informado para processamento**
