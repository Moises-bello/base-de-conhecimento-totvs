---
article_id: 360050771994
category: RH - Férias
content_hash: ae07df3d8e07d9e4cf41cb6f5eb53f0c83a83154037fa7df99e5b8448d75595b
fetched_at: '2026-06-28T22:43:58.289249+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Funcionamento do mnemônico P_SEGFALT nas faltas
  no Controle Dias de Direito
type: support-article
updated_at: '2025-06-30T19:38:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050771994-RH-Linha-Protheus-GPE-Funcionamento-do-mnem%C3%B4nico-P-SEGFALT-nas-faltas-no-Controle-Dias-de-Direito
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23761164882199) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Como funciona o mnemônico P\_SEGFALTA para as faltas no Controle Dias de Direito?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O mnemônico **P\_SEGFALT** (antigo MV\_SEGFALT) foi criado para determinar como as Faltas serão consideradas no Controle Dias de Direito.  
  
**P\_SEGFALT=.T.** = O sistema considera o campo **Data de Referencia** no lançamento da Verba de Falta, desta forma, ao fechar o período, a quantidade de Faltas irá para o período aquisitivo que pertence a Data de Referencia informada:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079519673)  
  
  
  
**P\_SEGFALT=.F.** = O sistema considera o **Período de lançamento** da Verba de Falta, desta forma, ao fechar o período, a Falta irá para o período aquisitivo movimentado no fechamento:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079519933)

**IMPORTANTE:** A partir do dia 01/06/2024, o mnemônico P\_SEGFALT (antigo MV\_SEGFALT) passa a ter o conteúdo **automaticamente alterado para .T. , impossibilitando assim o uso desativado.** Importante as verbas de faltas, atrasos e outras que irão refletir diretamente nas medias estarem configuradas como lançamento diário = Sim (RV\_LCTODIA). Com está configuração garantimos que a data de referência será preenchida nos lançamentos.

**Saiba Mais:**[RH - Linha Protheus - GPE - Mnemônico P\_SEGFALT (Antigo MV\_SEGFALT)](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXt4kGQhU6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBiGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzIzMzczMzIxNzEzNDMxLVJILUxpbmhhLVByb3RoZXVzLUdQRS1NbmVtJUMzJUI0bmljby1QLVNFR0ZBTFQtQW50aWdvLU1WLVNFR0ZBTFQGOwhUOg5zZWFyY2hfaWRJIik3YzcwNzIwZi03NzdlLTQ0YTMtYTQ5Zi02NjI0Y2NjMjNmZTYGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIgxTRUdGQUxUBjsIVDoScmVzdWx0c19jb3VudGkM--c185826c5de772ac1a23e2a043be976b322c04c3)  
[RH - Linha Protheus - GPE - Como conferir faltas do funcionário apresentadas no cálculo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjND9XUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBsGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzAxODU3My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25mZXJpci1mYWx0YXMtZG8tZnVuY2lvbiVDMyVBMXJpby1hcHJlc2VudGFkYXMtbm8tYyVDMyVBMWxjdWxvLWRlLWYlQzMlQTlyaWFzBjsIVDoOc2VhcmNoX2lkSSIpNWNiM2I4M2ItNTAzYS00MGI0LTk0ZTgtNWZmZjcxMGMxYmEwBjsIRjoJcmFua2kKOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIbcmVlbWJvbHNvIGZhbHRhIGZlcmlhcwY7CFQ6EnJlc3VsdHNfY291bnRpZQ%3D%3D--f756a8023567cc8f9b833e8595909da35b581f21)[RH - Linha Protheus - GPE - Dias de Faltas injustificadas não estão abatendo nas Férias da Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhrFarSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBt2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNjY0NzUzMS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtRGlhcy1kZS1GYWx0YXMtaW5qdXN0aWZpY2FkYXMtbiVDMyVBM28tZXN0JUMzJUEzby1hYmF0ZW5kby1uYXMtRiVDMyVBOXJpYXMtZGEtUmVzY2lzJUMzJUEzbwY7CFQ6DnNlYXJjaF9pZEkiKWNkY2RiZDdiLWUzNzYtNGViYi05OGY1LTE5ZTAzODc3YTU2MAY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiD01WX1NFR0ZBTFQGOwhUOhJyZXN1bHRzX2NvdW50aQLuBA%3D%3D--1a39e0dc776447a823b0df71496b2addbd326f2b)  
[RH - Linha Protheus - GPE - Parâmetro MV\_SEGFALT na funcionalidade de contador das faltas do Ponto para a Folha e Cálculo das Férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwitCUM%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB1Gh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDQ5NDQzMDEtUkgtTGluaGEtUHJvdGhldXMtR1BFLVBhciVDMyVBMm1ldHJvLU1WLVNFR0ZBTFQtbmEtZnVuY2lvbmFsaWRhZGUtZGUtY29udGFkb3ItZGFzLWZhbHRhcy1kby1Qb250by1wYXJhLWEtRm9saGEtZS1DJUMzJUExbGN1bG8tZGFzLUYlQzMlQTlyaWFzBjsIVDoOc2VhcmNoX2lkSSIpOTUzZjQyNDgtMzY2Zi00YzM0LTk2YTItZjRiZmM5ZDE5YmU1BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIBh1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBQYXLDom1ldHJvIE1WX1NFR0ZBTFQgbmEgZnVuY2lvbmFsaWRhZGUgZGUgY29udGFkb3IgZGFzIGZhbHRhcyBkbyBQb250byBwYXJhIGEgRm9saGEgZSBDw6FsY3VsbyBkYXMgRsOpcmlhcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--618e2413890b0ff5909ea5fb651b044f4922a419)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
<https://tdn.totvs.com/pages/releaseview.action?pageId=839962203>
