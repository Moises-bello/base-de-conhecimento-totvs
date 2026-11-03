---
article_id: 22079328691735
category: Financeiro - Aplicação / Emprestimos
content_hash: a278554cd10bd1e149506c486efed64682901b279e64f2dc8e47c336e680d9da
fetched_at: '2026-06-28T22:37:59.525149+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA716 - ExecAutoFINA181
  - JOB threads doesn't support remote/visual components. in file X:\build-dir\TP11-OF20320-TECXWIN64\interface\srvobject.cpp
  at line 30
type: support-article
updated_at: '2024-03-19T12:56:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22079328691735-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA716-ExecAutoFINA181-JOB-threads-doesn-t-support-remote-visual-components-in-file-X-build-dir-TP11-OF20320-TECXWIN64-interface-srvobject-cpp-at-line-30
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22079276259991) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao realizar a baixa do empréstimo na rotina FINA716 é gerado o error.log ExecAutoFINA181 - JOB threads doesn't support remote/visual components. in file X:\build-dir\TP11-OF20320-TECXWIN64\interface\srvobject.cpp at line 30  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22179319387927)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.2210  
  
**Causa**O problema é causado por alguma customização que pode ser da própria **FINA181** ou uma outra que esteja impactando a baixa ou alteração do FINA050.

**Solução**

Para identificar a raiz do problema, uma abordagem seria renomear o **RPOCUSTOM** para desativar as customizações. Alternativamente, pode-se utilizar **IXBLOG=LOGRUN** para determinar qual ponto de entrada está sendo acionado durante a baixa do empréstimo.

**SAIBA MAIS:**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como desativar customizações via Rpo Custom](Cross%20Segmentos%20-%20Backoffice%20Linha%20Protheus%20-%20SIGAFIN%20-%20Como%20desativar%20customiza%C3%A7%C3%B5es%20via%20Rpo%20Custom)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como ativar ou desativar customizações no Protheus](Cross%20Segmentos%20-%20Backoffice%20Linha%20Protheus%20-%20SIGAFIN%20-%20Como%20ativar%20ou%20desativar%20customiza%C3%A7%C3%B5es%20no%20Protheus)

[Empréstimos - FINA716](Empr%C3%A9stimos%20-%20FINA716)
