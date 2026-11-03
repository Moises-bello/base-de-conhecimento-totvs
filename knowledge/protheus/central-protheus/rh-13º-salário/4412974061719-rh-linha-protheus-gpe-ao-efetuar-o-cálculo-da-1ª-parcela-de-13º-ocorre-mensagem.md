---
article_id: 4412974061719
category: RH - 13º salário
content_hash: 057d10325d1d6a92a06d05df5b9e563ceef7e25046dc1a6f071620e18e4508e2
fetched_at: '2026-06-28T22:44:00.416886+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao efetuar o cálculo da 1ª Parcela de 13º ocorre
  mensagem: O período selecionado é diferente do último período em aberto'
type: support-article
updated_at: '2026-06-25T11:08:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412974061719-RH-Linha-Protheus-GPE-Ao-efetuar-o-c%C3%A1lculo-da-1%C2%AA-Parcela-de-13%C2%BA-ocorre-mensagem-O-per%C3%ADodo-selecionado-%C3%A9-diferente-do-%C3%BAltimo-per%C3%ADodo-em-aberto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18675110899863) Tempo aproximado para leitura: 00:02:00 min**  
  
**Ocorrência**  
Ao tentar calcular a 1ª Parcela de 13º ocorre mensagem: **O período selecionado é diferente do último período em aberto**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412973918615)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**  
Este incidente ocorre, pois ao Sistema encontra **outro período que ainda consta aberto para o roteiro 131**, diferente do que está **definido nos parâmetros de cálculo.**  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Verifique primeiramente se o **período selecionado nos parâmetros de Cálculo**, por exemplo 202111 consta aberto em **Atualizações> Definições Cálculo> Períodos;**  
  
**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412981838487)**  
  
Campo **Status - RFQ\_STATUS** no cabeçalho deve estar com **1 - Aberto**  
Campo **Data Fecham - RCH\_DTFECH** deve estar **sem conteúdo**  
Campo **Per. Ativo? - RCH\_PERSEL** deve estar com **1 - Sim**  
Campo **Status - RCH\_STATUS** deve estar com **0 - Normal**  
  
2. Além disso, verifique também, para os **demais períodos que tem o roteiro 131 cadastrado**, **anteriores** a este em aberto, se os campos acima estão configurados como **fechado, à exemplo, temos o roteiro 131 de 202011;**  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412974043927)  
  
Campo **Status - RFQ\_STATUS** no cabeçalho deve estar com **2 - Fechado**  
Campo **Data Fecham - RCH\_DTFECH** deve estar **Preenchido com a data de Fechamento do roteiro**  
Campo **Per. Ativo? - RCH\_PERSEL** deve estar com **2 - Não**  
Campo **Status - RCH\_STATUS** deve estar com **5 - Fechado**  
  
3. Estando correta as configurações acima, o Sistema calculará corretamente o roteiro 131 do ano atual.

**Saiba Mais**

[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo da 1ª parcela do 13° Salário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXpNm%2FAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIByWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDk4NTUxNTczOTktUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRhcy1hby1jJUMzJUExbGN1bG8tZGEtMSVDMiVBQS1wYXJjZWxhLWRvLTEzLVNhbCVDMyVBMXJpbwY7CFQ6DnNlYXJjaF9pZEkiKWNjYjIyOTQwLTY4MmUtNDUxYi04NjljLWY4ZDMwMjhiNDU1MwY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkid1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBRdWFpcyBzw6NvIGFzIGRvY3VtZW50YcOnw7VlcyByZWxhY2lvbmFkYXMgYW8gY8OhbGN1bG8gZGEgMcKqIHBhcmNlbGEgZG8gMTPCsCBTYWzDoXJpbwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--aa9ec391e5b1f2d521f6ca5e469a73f3b425cb4d)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionados ao cálculo da 2ª parcela do Décimo Terceiro](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXmUm%2BAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBzmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDk4Mjg5NDAwNTUtUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRvcy1hby1jJUMzJUExbGN1bG8tZGEtMiVDMiVBQS1wYXJjZWxhLWRvLUQlQzMlQTljaW1vLVRlcmNlaXJvBjsIVDoOc2VhcmNoX2lkSSIpMmQ5OGI2ODItOTliMi00M2JiLTg2NDMtMzgzNGQzZmU1MzYxBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJ6UkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIFF1YWlzIHPDo28gYXMgZG9jdW1lbnRhw6fDtWVzIHJlbGFjaW9uYWRvcyBhbyBjw6FsY3VsbyBkYSAywqogcGFyY2VsYSBkbyBEw6ljaW1vIFRlcmNlaXJvBjsIVDoScmVzdWx0c19jb3VudGkCuQc%3D--788f1035c55828746d9da0e76b0deca9df7dcce2)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo do complemento de 13º](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXkGzzAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBvmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTA3MjA0MjM5NTktUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRhcy1hby1jJUMzJUExbGN1bG8tZG8tY29tcGxlbWVudG8tZGUtMTMlQzIlQkEGOwhUOg5zZWFyY2hfaWRJIik4NGY3OGZlMy01Nzc5LTQxM2QtOGJkYi02MzRjZjE0ZmRhMmYGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIm5SSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gUXVhaXMgc8OjbyBhcyBkb2N1bWVudGHDp8O1ZXMgcmVsYWNpb25hZGFzIGFvIGPDoWxjdWxvIGRvIGNvbXBsZW1lbnRvIGRlIDEzwroGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--2102dd993f29e8a59b1a01d84c1261785bf9526d)  
**Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento:**[**https://www.youtube.com/watch?v=T7b4zMlphTI**](https://www.youtube.com/watch?v=T7b4zMlphTI)
