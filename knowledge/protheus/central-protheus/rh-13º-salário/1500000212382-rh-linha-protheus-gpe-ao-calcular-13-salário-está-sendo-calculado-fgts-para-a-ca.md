---
article_id: 1500000212382
category: RH - 13º salário
content_hash: e834f10e6cbf142e24488de6c1aa1defc187c7b6b01d9d3f9968a7c4687b3bea
fetched_at: '2026-06-28T22:44:00.403035+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Ao calcular 13° salário, está sendo calculado FGTS
  para a categoria Estagiario
type: support-article
updated_at: '2026-06-24T19:50:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000212382-RH-Linha-Protheus-GPE-Ao-calcular-13-sal%C3%A1rio-est%C3%A1-sendo-calculado-FGTS-para-a-categoria-Estagiario
---

**Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Ao calcular 13° salário, está sendo calculado FGTS para a categoria Estagiário  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O pagamento do 13° salário para estagiários e pro labores é opcional, legalmente não deve ser pago, logo, o Sistema calcula nos Identificadores padrão e com isso gera os encargos (INSS / IR e FGTS), pois entende-se que deve ser feito o recolhimento, considerado como funcionário Celetista.   
  
Como se trata da particularidade de algumas empresas, pagar o 13º para estas categorias, a solução é criar 3 verbas, sendo:

* 1° Parcela 13° Salario  (Tipo 1- Provento)
* 2° Parcela 13° Salario (Tipo 1 - Provento)
* Desconto Antecipação 13° Salario (Tipo 2 - Desconto)

Todas sem id de cálculo e sem incidência e realizar o lançamento via rotina de lançamentos por funcionário (GPEA580), no roteiro FOL para estagiários e/ou AUT para Pro Labores. 

[RH - Linha Protheus - GPE - Qual é a rotina para Lançamentos de Verbas para o cálculo da folha?](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXbVVv4Qs6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBsGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEzMDYyODYzNDE2NTk5LVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFsLSVDMyVBOS1hLXJvdGluYS1wYXJhLUxhbiVDMyVBN2FtZW50b3MtZGUtVmVyYmFzLXBhcmEtby1jJUMzJUExbGN1bG8tZGEtZm9saGEtBjsIVDoOc2VhcmNoX2lkSSIpNGE3NDVkZjUtZmYxYy00ZjExLTkzYjEtZTJkZjAxNWFlNTk1BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJnUkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIFF1YWwgw6kgYSByb3RpbmEgcGFyYSBMYW7Dp2FtZW50b3MgZGUgVmVyYmFzIHBhcmEgbyBjw6FsY3VsbyBkYSBmb2xoYT8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--834a76005707003196d377d02176fb9028e61584)

**Exemplos  
Calculo 1° Parcela:**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10792514075159)

**Calculo 2° Parcela:**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10795762374807)

**Saiba Mais**[RH - Linha Protheus - GPE - Como não realizar cálculo do 13º Salário para Estagiários, Pró-Labores e Autônomos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038026414-RH-Linha-Protheus-GPE-Como-n%C3%A3o-realizar-c%C3%A1lculo-do-13%C2%BA-Sal%C3%A1rio-para-Estagi%C3%A1rios-Pr%C3%B3-Labores-e-Aut%C3%B4nomos-?source=search)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo da 1ª parcela do 13° Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409855157399-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-as-documenta%C3%A7%C3%B5es-relacionadas-ao-c%C3%A1lculo-da-1%C2%AA-parcela-do-13-Sal%C3%A1rio?source=search)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionados ao cálculo da 2ª parcela do Décimo Terceiro](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXmUm%2BAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBzmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDk4Mjg5NDAwNTUtUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRvcy1hby1jJUMzJUExbGN1bG8tZGEtMiVDMiVBQS1wYXJjZWxhLWRvLUQlQzMlQTljaW1vLVRlcmNlaXJvBjsIVDoOc2VhcmNoX2lkSSIpMmQ5OGI2ODItOTliMi00M2JiLTg2NDMtMzgzNGQzZmU1MzYxBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSJ6UkggLSBMaW5oYSBQcm90aGV1cyAtIEdQRSAtIFF1YWlzIHPDo28gYXMgZG9jdW1lbnRhw6fDtWVzIHJlbGFjaW9uYWRvcyBhbyBjw6FsY3VsbyBkYSAywqogcGFyY2VsYSBkbyBEw6ljaW1vIFRlcmNlaXJvBjsIVDoScmVzdWx0c19jb3VudGkCuQc%3D--788f1035c55828746d9da0e76b0deca9df7dcce2)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo do complemento de 13º](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXkGzzAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBvmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTA3MjA0MjM5NTktUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRhcy1hby1jJUMzJUExbGN1bG8tZG8tY29tcGxlbWVudG8tZGUtMTMlQzIlQkEGOwhUOg5zZWFyY2hfaWRJIik4NGY3OGZlMy01Nzc5LTQxM2QtOGJkYi02MzRjZjE0ZmRhMmYGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIm5SSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gUXVhaXMgc8OjbyBhcyBkb2N1bWVudGHDp8O1ZXMgcmVsYWNpb25hZGFzIGFvIGPDoWxjdWxvIGRvIGNvbXBsZW1lbnRvIGRlIDEzwroGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--2102dd993f29e8a59b1a01d84c1261785bf9526d)  
Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>
