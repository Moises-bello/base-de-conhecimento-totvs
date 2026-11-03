---
article_id: 360055751574
category: Integrações Nativas
content_hash: 76942a1891e85f1db6f92c389198ab87a7583910b621f8275c6ceffaff99a78e
fetched_at: '2026-06-28T22:42:35.525448+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Relação do campo T1_TURNO com o campo R6_TURNO
type: support-article
updated_at: '2021-09-06T18:25:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055751574-Manufatura-Linha-Protheus-MNT-Rela%C3%A7%C3%A3o-do-campo-T1-TURNO-com-o-campo-R6-TURNO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:40 min**  
**Dúvida**O campo **Turno - T1\_TURNO** tem relação com o campo **Turno - R6\_TURNO**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Versão 12  
  
**Solução**O campo **T1\_TURNO** da tabela **Funcionários - ST1**, é utilizado apenas para ações pertinentes ao módulo **Manutenção de Ativos - SIGAMNT** como, por exemplo, uma ordem de serviço ou plano de manutenção que envolvam funcionários e respectivamente o bloqueio dos mesmos durante o período de execução da ação. Esse turno não consiste com o campo **Turno de Trabalho - R6\_TURNO** da tabela **Turnos de trabalho - SR6** do módulo **Gestão de Pessoas - GPE**. O cadastro de funcionários da manutenção permite inclusive o cadastramento de funcionários não inclusos no **GPE**.
