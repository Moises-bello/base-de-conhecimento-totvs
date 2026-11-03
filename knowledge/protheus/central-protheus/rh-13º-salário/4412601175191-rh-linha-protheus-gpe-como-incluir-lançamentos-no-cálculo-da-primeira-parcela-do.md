---
article_id: 4412601175191
category: RH - 13º salário
content_hash: 57713f10d722b338e5fc545a4faae9eae8715cb5192fb088271d0e8e9b3244a6
fetched_at: '2026-06-28T22:44:00.660939+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como incluir lançamentos no cálculo da Primeira
  Parcela do 13° Salario
type: support-article
updated_at: '2025-11-05T12:41:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412601175191-RH-Linha-Protheus-GPE-Como-incluir-lan%C3%A7amentos-no-c%C3%A1lculo-da-Primeira-Parcela-do-13-Salario
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18896752258711)Tempo aproximado para leitura: 00:01:00 min****Dúvida**Como incluir lançamentos no cálculo da Primeira Parcela do 13° Salario?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Os valores podem ser lançados via rotina de Lançamentos por funcionário (GPEA580), Lançamentos por Verba (GPEA590) ou Importação (GPEA210).  
Para que o sistema possa realizar o calculo, obrigatoriamente os **lançamentos** devem ser feitos no **Roteiro 131**. **![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412583965847)**  
  
A verba criada não deve possuir identificador de cálculo, e o **campo Ref 13º** deve estar com conteúdo igual a **SIM**.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412588484887)  
  
As **incidências** podem ser **iguais** ao **identificador de cálculo 0022,** e dessa maneira o sistema utilizará essas informações para gerar o cálculo da primeira parcela contendo o valor lançado e também irá compor a base de encargos corretamente para valores de 13º Salario.  
  
  
No exemplo abaixo, tivemos 50% do salário + valor do prêmio como proventos.   
A base de FGTS é a soma dos proventos pois a configuração das incidências da verba de premio, é a mesma da verba de identificador 0022.  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412594132759)

**Observação:** Assim como foi realizado o lançamento manual da verba de provento no roteiro 131, no roteiro 132 uma verba de desconto deve ser lançada contendo o valor já antecipado, pois o sistema **não gera de forma automática** o desconto da antecipação de verbas lançadas sem ID de calculo no roteiro 131.  **Saiba Mais**[RH - Linha Protheus - GPE - Como incluir lançamento no cálculo da Segunda Parcela](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057052394-RH-Linha-Protheus-GPE-Como-incluir-lan%C3%A7amento-no-c%C3%A1lculo-da-Segunda-Parcela?source=search)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo da 1ª parcela do 13° Salário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXpNm%2FAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIByWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDk4NTUxNTczOTktUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRhcy1hby1jJUMzJUExbGN1bG8tZGEtMSVDMiVBQS1wYXJjZWxhLWRvLTEzLVNhbCVDMyVBMXJpbwY7CFQ6DnNlYXJjaF9pZEkiKTU2OGFlNTEyLTg2OTgtNGIwNi1iMjZhLTY2ZDdlMWQ4ZmFmZgY7CEY6CXJhbmtpCzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiEGZhbHRhcyAxM8K6BjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--aaeb12c870ef47b22b00c8165dbf1889f85e2d77)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionados ao cálculo da 2ª parcela do 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXmUm%2BAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBz2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDk4Mjg5NDAwNTUtUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRvcy1hby1jJUMzJUExbGN1bG8tZGEtMiVDMiVBQS1wYXJjZWxhLWRvLTEzJUMyJUJBLVNhbCVDMyVBMXJpbwY7CFQ6DnNlYXJjaF9pZEkiKTNhMGI3ZjBlLWJhYTQtNGFjOC1hZjQ4LTIwZTk3NzhkMTliNQY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiW1JIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBRdWFpcyBzw6NvIGFzIGRvY3VtZW50YcOnw7VlcyByZWxhY2lvbmFkYXMgYW8gY8OhbGN1bG8gZGEgBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--e8618fa86d99f9e9c2d245f0fe90ba4ad5112b40)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo do complemento de 13º](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXkGzzAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBvmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTA3MjA0MjM5NTktUkgtTGluaGEtUHJvdGhldXMtR1BFLVF1YWlzLXMlQzMlQTNvLWFzLWRvY3VtZW50YSVDMyVBNyVDMyVCNWVzLXJlbGFjaW9uYWRhcy1hby1jJUMzJUExbGN1bG8tZG8tY29tcGxlbWVudG8tZGUtMTMlQzIlQkEGOwhUOg5zZWFyY2hfaWRJIik4ZTZjNTk0My03NTlkLTQ2ZmYtOGZjMS1hMGMzMjhjMzZmZTkGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIlpSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gUXVhaXMgc8OjbyBhcyBkb2N1bWVudGHDp8O1ZXMgcmVsYWNpb25hZGFzIGFvIGPDoWxjdWxvIGRvBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--cf0823d89f98b1b34d8bc0d5d26cd8a42c3cca1d)
