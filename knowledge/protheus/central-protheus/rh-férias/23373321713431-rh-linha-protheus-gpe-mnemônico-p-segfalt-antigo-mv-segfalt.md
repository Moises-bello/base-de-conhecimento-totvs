---
article_id: 23373321713431
category: RH - Férias
content_hash: 58393656ef126648ac221fac2cfe3d41bc765908148306a533927ea39b561061
fetched_at: '2026-06-28T22:43:59.368247+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Mnemônico P_SEGFALT (Antigo MV_SEGFALT)
type: support-article
updated_at: '2025-10-02T17:31:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23373321713431-RH-Linha-Protheus-GPE-Mnem%C3%B4nico-P-SEGFALT-Antigo-MV-SEGFALT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23373321670423) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual a função do mnemônico **P\_SEGFALT** (Antigo MV\_SEGFALT)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.2210  
  
**Solução**O mnemônico irá gravar cada **falta com a sua respectiva data de ocorrência,** para garantir que fiquem **separadas conforme o período aquisitivo** do funcionário, e não gerar deduções indevidas nas Férias de funcionários que tiveram faltas no mês de término/início do período aquisitivo.   
  
Exemplo de faltas geradas no SIGAPON e integradas na Folha:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23472049963671)  
  
A partir do dia 01/06/2024, o mnemônico **P\_SEGFALT** passa a ter o conteúdo **automaticamente alterado** para **.T.** , impossibilitando assim o uso desativado.  
  
**Importante:**-As verbas de faltas, atrasos e outras que irão refletir diretamente na contagem de faltas (como por exemplo nas férias) devem ficar com o Lançamento Diário = Sim (RV\_LCTODIA). Com esta configuração garantimos que a data de referência seja preenchida nos lançamentos.  
-Para gerar as verbas de tipo falta no SIGAPON, é necessário utilizar a funcionalidade de **Contador de Faltas** [conforme esta documentação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015852071-RH-Linha-Protheus-PON-Como-utilizar-a-funcionalidade-de-Contador-de-Faltas-no-Ponto-Eletr%C3%B4nico)  
  
**Saiba Mais**[Obrigatoriedade de ativação de mnemônico P\_SEGFALT](https://tdn.totvs.com/pages/viewpage.action?pageId=839962203)  
[RH - Linha Protheus - GPE - Funcionamento do parâmetro MV\_SEGFALT nas faltas no Controle Dias de Direito](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgayLLUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDc3MTk5NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtRnVuY2lvbmFtZW50by1kby1wYXIlQzMlQTJtZXRyby1NVi1TRUdGQUxULW5hcy1mYWx0YXMtbm8tQ29udHJvbGUtRGlhcy1kZS1EaXJlaXRvBjsIVDoOc2VhcmNoX2lkSSIpMzU4NGFjNGEtNTU4Yi00NTljLTljNDctYjhhNTU1NTc1ZDc5BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJuUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIEZ1bmNpb25hbWVudG8gZG8gcGFyw6JtZXRybyBNVl9TRUdGQUxUIG5hcyBmYWx0YXMgbm8gQ29udHJvbGUgRGlhcyBkZSBEaXJlaXRvBjsIVDoScmVzdWx0c19jb3VudGkC6AM%3D--ead6022173f88fddb09de86c0c0683f03a627e0c)  
[RH - Linha Protheus - PON - Como utilizar a funcionalidade de Contador de Faltas no Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015852071-RH-Linha-Protheus-PON-Como-utilizar-a-funcionalidade-de-Contador-de-Faltas-no-Ponto-Eletr%C3%B4nico)  
[RH - Linha Protheus - GPE - Como conferir faltas do funcionário apresentadas no cálculo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjND9XUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBsGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzAxODU3My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1jb25mZXJpci1mYWx0YXMtZG8tZnVuY2lvbiVDMyVBMXJpby1hcHJlc2VudGFkYXMtbm8tYyVDMyVBMWxjdWxvLWRlLWYlQzMlQTlyaWFzBjsIVDoOc2VhcmNoX2lkSSIpMzU4NGFjNGEtNTU4Yi00NTljLTljNDctYjhhNTU1NTc1ZDc5BjsIRjoJcmFua2kKOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJuUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIEZ1bmNpb25hbWVudG8gZG8gcGFyw6JtZXRybyBNVl9TRUdGQUxUIG5hcyBmYWx0YXMgbm8gQ29udHJvbGUgRGlhcyBkZSBEaXJlaXRvBjsIVDoScmVzdWx0c19jb3VudGkC6AM%3D--ad91478c42bbb2d7d4dbbf5ba3c860e6a5f891c0)  
[RH - Linha Protheus - GPE - Como efetuar manutenção do Controle de Dias de Direito após o fechamento do período](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjle0vVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBw2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA2MDc3OTQ5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1lZmV0dWFyLW1hbnV0ZW4lQzMlQTclQzMlQTNvLWRvLUNvbnRyb2xlLWRlLURpYXMtZGUtRGlyZWl0by1hcCVDMyVCM3Mtby1mZWNoYW1lbnRvLWRvLXBlciVDMyVBRG9kbwY7CFQ6DnNlYXJjaF9pZEkiKTM1ODRhYzRhLTU1OGItNDU5Yy05YzQ3LWI4YTU1NTU3NWQ3OQY7CEY6CXJhbmtpDzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiblJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBGdW5jaW9uYW1lbnRvIGRvIHBhcsOibWV0cm8gTVZfU0VHRkFMVCBuYXMgZmFsdGFzIG5vIENvbnRyb2xlIERpYXMgZGUgRGlyZWl0bwY7CFQ6EnJlc3VsdHNfY291bnRpAugD--986169029e2b0ae19dab918b342eaaaff033d392)
