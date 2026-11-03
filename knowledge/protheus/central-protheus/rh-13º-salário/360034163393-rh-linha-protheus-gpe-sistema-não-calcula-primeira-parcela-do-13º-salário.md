---
article_id: 360034163393
category: RH - 13º salário
content_hash: 3c3a75a8efdd94c7465d838f48342e329c1d879d321d17eaae2be9ce0c85e85a
fetched_at: '2026-06-28T22:44:01.636728+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não calcula primeira parcela do 13º salário
type: support-article
updated_at: '2025-08-15T19:06:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034163393-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-calcula-primeira-parcela-do-13%C2%BA-sal%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18726268077079) Tempo aproximado para leitura: 00:05:00 min**

**Dúvida**O que analisar quando o cálculo da primeira parcela de 13º não é gerado para alguns funcionários.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**1. Verifique nos parâmetros de cálculo do roteiro 131 (primeira parcela do 13º) se o campo D**ata Referência** esta preenchido no ultimo mês do ano, exemplo 31/12/2024.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29304261559959)  
  
Esse exemplo de preenchimento, faz com que o sistema busque 12 avos para realizar o cálculo do percentual informado.  
Caso a data de referência esteja em 30/11 o sistema considera **11 meses** sendo 50% para primeira parcela, totalizando **5,5 avos**.  
  
2. Extraia a Ficha Financeira e veja se o 13º foi pago durante o ano ou nas férias; Informe os roteiros 131 / 132 / FOL / FER - [RH - Linha Protheus - GPE - Como emitir Relatório Ficha Financeira](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiX1INgAQQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBiGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDM5NjA3MzA3NzUtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZW1pdGlyLVJlbGF0JUMzJUIzcmlvLUZpY2hhLUZpbmFuY2VpcmEGOwhUOg5zZWFyY2hfaWRJIik5NTg1YmQyOS03ZTc1LTRmMWUtYjUxMi1hMTY0NTQ3ZWE0Y2IGOwhGOglyYW5raQw6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhVmaWNoYSBmaW5hbmNlaXJhBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--03d164d1a783c28ea9afbf454e5093cb167040ec)

3. Verifique se há Afastamentos para este funcionário dentro do ano, e se o Tipo de Ausência está configurado para abater avos do 13º;

4. Verifique através da Ficha Financeira, se existem faltas e atrasos em excesso no período;

5. Verifique a Data de Admissão (o funcionário deve ter pelo menos 15 dias trabalhados em cada mês para obter o direito ao avo).  
  
6. Verifique nas tabelas **SRC** ou **RGB** se possui algum lançamento com o campo código da verba vazio, ou então algum registro de 13º de anos anteriores, caso tenha, apague. Gere sempre via consulta genérica - [RH - Linha Protheus - GPE - Consulta de informações em arquivos por Consulta Genérica](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg1wMbUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBpGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MjA4MDY5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29uc3VsdGEtZGUtaW5mb3JtYSVDMyVBNyVDMyVCNWVzLWVtLWFycXVpdm9zLXBvci1Db25zdWx0YS1HZW4lQzMlQTlyaWNhBjsIVDoOc2VhcmNoX2lkSSIpNGRkMTJjNzEtYmM1MS00NjliLWE3ZjUtOGRiNDIxYmE3OGVlBjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIfY29uc3VsdGEgZ2VuZXJpY2EgcGxhbmlsaGEGOwhUOhJyZXN1bHRzX2NvdW50aQK3AQ%3D%3D--f371157f74499499e991704ea497f2b12d7232ea)

7. Verifique no cadastro do funcionário ou na tabela SRA se o campo **RA\_MESTRAB** está preenchido, o padrão desse campo é vazio.

**Saiba Mais**Acesse o link a seguir com mais artigos sobre 13º: [RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio?page=1#articles)  
  
Para **mais documentações**, acesse a **Carolina** via **Protheus** ou Central de Atendimento.  
Veja como acessar: <https://www.youtube.com/watch?v=T7b4zMlphTI>
