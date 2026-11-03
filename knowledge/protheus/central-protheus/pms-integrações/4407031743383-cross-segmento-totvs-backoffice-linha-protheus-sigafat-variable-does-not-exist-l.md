---
article_id: 4407031743383
category: PMS - Integrações
content_hash: ce883476606c9d2777e945f4235da70a5c0d2a0bfa1c1950be21840f3f0e65b9
fetched_at: '2026-06-28T22:37:16.683407+00:00'
product: protheus
section_id: 1500001550742
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - variable does
  not exist __LTOPCONN on PMS203DFIM(PMSA203.PRW)
type: support-article
updated_at: '2021-08-25T20:20:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407031743383-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-variable-does-not-exist-LTOPCONN-on-PMS203DFIM-PMSA203-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00min****Ocorrência**

Ao importar um projeto no PMS através do **MS Project** e ao alterar uma **EDT** ocorre o erro:

**variable does not exist \_\_LTOPCONN on PMS203DFIM(PMSA203.PRW) 13/03/2020 11:31:36 line : 3906**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Todas as versões  
  
**Causa**O erro ocorre quando o parâmetro **MV\_PMSCALE**, provavelmente o seu esta = .T.   
Esse parâmetro indica se usará o novo calendário (tabela **AEG**) do módulo **SIGAPMS**.  
O calendário que ele esta usando com o parâmetro = .T. é da **SH7** e esse não é mais usado no sistema, o padrão é o **AEG**, sendo assim, pode alterar o parâmetro para .F. para usar o novo formato de calendário.

**Solução**  
Para solucionar essa ocorrência, efetue a alteração do parâmetro **MV\_PMSCALE** para .F.
