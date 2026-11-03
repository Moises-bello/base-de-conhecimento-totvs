---
article_id: 4406900205975
category: RH - Funcionários
content_hash: b9fd1335e34391a13da11b8a2c1b245e632930f6ac66243f3f344f563fa97a65
fetched_at: '2026-06-28T22:43:28.642894+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Parâmetros envolvidos no processo de Configuração
  para Matrícula automática
type: support-article
updated_at: '2025-04-17T12:48:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406900205975-RH-Linha-Protheus-GPE-Par%C3%A2metros-envolvidos-no-processo-de-Configura%C3%A7%C3%A3o-para-Matr%C3%ADcula-autom%C3%A1tica
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31481619715607) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Quais são os parâmetros envolvidos no processo de configuração para Matrícula Automática?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Os parâmetros envolvidos são:   
  
**MV\_MATRICU** - Indica como será o controle de numeração da Matricula.  
0 = Usuário informará  
1 = Automática por Filial  
2 = Automática por Empresa  
3 = Automática por Grupo de Empresa;  
  
**MV\_MATAUT -** Indica a partir de qual matricula deve iniciar o cadastramento dos autônomos.  
Conteúdo padrão = 90000  
  
**MV\_MATUNIC -** Indicar a partir de qual matricula deve iniciar o sequencial automático de Funcionários e Autônomos.

No **módulo Configurador**, acesse o menu **Ambientes/ Cadastros/ Parâmetros** para alterar os parâmetros.

**Saiba Mais**[RH - Linha Protheus - GPE - Como utilizar o parâmetro MV\_MATUNIC](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhpvb3UUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBhmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MTQ5MDE1My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby11dGlsaXphci1vLXBhciVDMyVBMm1ldHJvLU1WLU1BVFVOSUMtBjsIVDoOc2VhcmNoX2lkSSIpNjUwYzUwNzQtMjYyZS00ZmUyLThkNWItYzhiZTQwMzgwNjM4BjsIRjoJcmFua2kHOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIPTVZfTUFUVU5JQwY7CFQ6EnJlc3VsdHNfY291bnRpAvIE--88e4036a889d3957ae114b3aab92f0669155ea0e)  
[RH - Linha Protheus - GPE - Configuração para Matrícula automática de funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgfQGbTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBq2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODk3OTIzMS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29uZmlndXJhJUMzJUE3JUMzJUEzby1wYXJhLU1hdHIlQzMlQURjdWxhLWF1dG9tJUMzJUExdGljYS1kZS1mdW5jaW9uJUMzJUExcmlvcwY7CFQ6DnNlYXJjaF9pZEkiKTMzZTU5ZDU0LWU0NjAtNDJkMi1iYjk2LTQwYjI5OTQ4ZGE3ZQY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiXFJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb25maWd1cmHDp8OjbyBwYXJhIE1hdHLDrWN1bGEgYXV0b23DoXRpY2EgZGUgZnVuY2lvbsOhcmlvcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--badf55126308403c4f4a5dc8f55186a605979bc9)  
[RH - Linha Protheus - GPE - Configuração para Matrícula Automática Autônomos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhUcGHTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBpWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODY2Mzg5Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29uZmlndXJhJUMzJUE3JUMzJUEzby1wYXJhLU1hdHIlQzMlQURjdWxhLUF1dG9tJUMzJUExdGljYS1BdXQlQzMlQjRub21vcwY7CFQ6DnNlYXJjaF9pZEkiKWRiZTZiNDQ2LTJkMjItNDVhZC05MTg0LTQ0OTk3MzRiODA2MAY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiVlJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb25maWd1cmHDp8OjbyBwYXJhIE1hdHLDrWN1bGEgQXV0b23DoXRpY2EgQXV0w7Rub21vcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--39beb46e50705a5d2a6e59bf1d25c16623183808)
