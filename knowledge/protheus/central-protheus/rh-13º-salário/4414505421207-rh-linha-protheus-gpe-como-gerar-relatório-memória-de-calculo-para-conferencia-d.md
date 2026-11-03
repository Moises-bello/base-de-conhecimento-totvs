---
article_id: 4414505421207
category: RH - 13º salário
content_hash: 9707f6275e17b2f17630f9fdf5dab324feba4a785b95311e4ec58b06b62af2fb
fetched_at: '2026-06-28T22:44:00.653064+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar relatório memória de calculo para conferencia
  de medias da segunda parcela
type: support-article
updated_at: '2025-08-20T13:25:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414505421207-RH-Linha-Protheus-GPE-Como-gerar-relat%C3%B3rio-mem%C3%B3ria-de-calculo-para-conferencia-de-medias-da-segunda-parcela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18958975118999) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Relatório de Memória de Cálculo no 13º segunda parcela  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que possamos entender as médias geradas no cálculo do 13º, devemos gerar a **memória de cálculo** das médias.  
  
Quando o mnemônico **P\_LMEMCALC**for ativado, as fórmulas serão atualizadas para executar a gravação do Log de Cálculo por Funcionário. Se o mnemônico **P\_LMEMCALC**estiver desativado, a chamada para gravação de log não ocorrerá.

1. Acesse: **Atualizações >Definições de Cálculo >Mnemônicos (GPEA300)**  
2. Altere o Mnemônico **P\_LMEMCALC** para **.T.** para que possa ser recriadas as fórmulas com o *Log* Ativado.  
  
**Observação:** Ao salvar a alteração, o processo pode demorar um pouco pelo fato do sistema recriar as fórmulas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18959014141591)  
  
  
Após parametrização faça a geração do relatório ou consulta da memoria de calculo:  
1. Acesse: **Consulta > Cálculo > Por Funcionário (GPEA580)**  
2. Selecione o funcionário e clique em Outras Ações > Relatório Memória de Cálculo  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18959014146199)  
  
Na tela Memoria de Calculo por Funcionário : clique em Outras Ações > Parâmetros.  
Informe a matricula caso queira somente de um ou alguns funcionários.   
  
![mceclip0.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414505388951)

Segue link contendo passo a passo para parametrização da memoria de calculo: <https://tdn.totvs.com/pages/releaseview.action?pageId=330831446>

**Saiba Mais:**[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo da 1ª parcela do 13° Salário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXpNm%2FAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIByWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDk4NTUxNTczOTktUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRhcy1hby1jJUMzJUExbGN1bG8tZGEtMSVDMiVBQS1wYXJjZWxhLWRvLTEzLVNhbCVDMyVBMXJpbwY7CFQ6DnNlYXJjaF9pZEkiKWNjYjIyOTQwLTY4MmUtNDUxYi04NjljLWY4ZDMwMjhiNDU1MwY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkid1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBRdWFpcyBzw6NvIGFzIGRvY3VtZW50YcOnw7VlcyByZWxhY2lvbmFkYXMgYW8gY8OhbGN1bG8gZGEgMcKqIHBhcmNlbGEgZG8gMTPCsCBTYWzDoXJpbwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--aa9ec391e5b1f2d521f6ca5e469a73f3b425cb4d)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionados ao cálculo da 2ª parcela do Décimo Terceiro](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXmUm%2BAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBzmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDk4Mjg5NDAwNTUtUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRvcy1hby1jJUMzJUExbGN1bG8tZGEtMiVDMiVBQS1wYXJjZWxhLWRvLUQlQzMlQTljaW1vLVRlcmNlaXJvBjsIVDoOc2VhcmNoX2lkSSIpMmQ5OGI2ODItOTliMi00M2JiLTg2NDMtMzgzNGQzZmU1MzYxBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJ6UkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIFF1YWlzIHPDo28gYXMgZG9jdW1lbnRhw6fDtWVzIHJlbGFjaW9uYWRvcyBhbyBjw6FsY3VsbyBkYSAywqogcGFyY2VsYSBkbyBEw6ljaW1vIFRlcmNlaXJvBjsIVDoScmVzdWx0c19jb3VudGkCuQc%3D--788f1035c55828746d9da0e76b0deca9df7dcce2)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo do complemento de 13º](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXkGzzAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBvmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTA3MjA0MjM5NTktUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRhcy1hby1jJUMzJUExbGN1bG8tZG8tY29tcGxlbWVudG8tZGUtMTMlQzIlQkEGOwhUOg5zZWFyY2hfaWRJIik4NGY3OGZlMy01Nzc5LTQxM2QtOGJkYi02MzRjZjE0ZmRhMmYGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIm5SSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gUXVhaXMgc8OjbyBhcyBkb2N1bWVudGHDp8O1ZXMgcmVsYWNpb25hZGFzIGFvIGPDoWxjdWxvIGRvIGNvbXBsZW1lbnRvIGRlIDEzwroGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--2102dd993f29e8a59b1a01d84c1261785bf9526d)
