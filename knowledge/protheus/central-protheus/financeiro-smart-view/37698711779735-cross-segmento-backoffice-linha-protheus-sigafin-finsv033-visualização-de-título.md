---
article_id: 37698711779735
category: Financeiro - Smart View
content_hash: 58838bf000acdbb4f5aa1fcc62562bbfefbd4b67168b0e3f1176bb5df673cf27
fetched_at: '2026-06-28T22:37:44.631463+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINSV033 - Visualização
  de títulos envolvidos na compensação entre carteiras
type: support-article
updated_at: '2026-01-15T16:29:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37698711779735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINSV033-Visualiza%C3%A7%C3%A3o-de-t%C3%ADtulos-envolvidos-na-compensa%C3%A7%C3%A3o-entre-carteiras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37701350639895) Tempo aproximado para leitura: **00:05 min**

**Dúvida**  
Como visualizar todos os títulos envolvidos em uma operação de compensação entre carteiras?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as Versões  
  
**Solução**

No Protheus, a visualização detalhada dos títulos envolvidos em uma compensação entre carteiras pode ser realizada por meio de **consulta ou relatório via Smart View**.

Para esse cenário, deve ser utilizado o recurso **FINSV033 – Compensação Entre Carteiras**, que disponibiliza as informações e os valores referentes às compensações realizadas entre as carteiras **a pagar e a receber**, originadas no processo **FINA450**.

Essa consulta exibe, dentro do mesmo processo, os títulos “compensados” de ambas as carteiras. As informações são **aglutinadas por processo de compensação**, apresentando inicialmente os títulos da carteira **a pagar** que participaram do processo e, na sequência, os títulos da carteira **a receber**.

Cada linha da consulta corresponde a um título (seja a pagar ou a receber), sempre **agrupado pelo número do processo de compensação**.

É possível aplicar filtros por **número da compensação, data, situação e moeda**, facilitando a análise e a conferência.

Essa rotina permite a **rastreabilidade completa dos títulos de origem** (contas a pagar ou contas a receber) que foram liquidados ou baixados mutuamente durante o processo de compensação, garantindo maior controle, conferência de saldos e validação dos documentos relacionados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37698754117015)
