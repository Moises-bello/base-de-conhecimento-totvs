---
article_id: 360028940832
category: RH - Lançamentos
content_hash: 90233bb8f417b181728e7a267a3eee4c89560b9ae109574439846d7566ae8c4e
fetched_at: '2026-06-28T22:43:31.236586+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar o Lançamento Fixo de uma verba
type: support-article
updated_at: '2025-11-19T14:26:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028940832-RH-Linha-Protheus-GPE-Como-parametrizar-o-Lan%C3%A7amento-Fixo-de-uma-verba
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26079963478935)** Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como parametrizar o Lançamento Fixo de uma verba?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**  
Para efetuar o cálculo de uma verba mensal por tempo indeterminado é necessário seguir os procedimentos abaixo:  
  
1. Acesse: **Atualizações >Definições de Cálculos >Verbas** e Cadastre uma verba para efetuar o lançamento que será pago na folha de pagamento para o funcionário;  
  
2. Acesse: **Atualizações >Lançamentos >Lançamentos Fixos >Incluir** e cadastre o lançamento que será calculado mensalmente na folha do funcionário.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7430953260183)  
  
Principais Campos:  
**Calc. Autom.**: Define se o cálculo deverá gerar automaticamente a verba para o funcionário.

**Roteiro:** Informe o Roteiro de Cálculo para este Lançamento.

**Tipo Calc.**: Determina a regra para geração dos valores da verba no cálculo, sendo por:

1. Valor Fixo
2. Dias
3. Horas
4. Tabela
5. Acumulador
6. Percentual do Salário Base
7. Percentual do Salário Mínimo

**Cod. Verba**: Informe a verba para lançamento fixo.

**Proporcional**: Informe se o valor do lançamento deverá ser proporcionalizado de acordo com a quantidade de dias trabalhados no mês.

**Dt. Ini. Pagto**.: Informe a data de inicio da geração da verba para o funcionário.

**Dt. Fim Pagto**.: Informe a data fim da geração da verba para o funcionário, caso seja indeterminado, este campo **deverá estar em branco,** pois caso seja informada data com ano **9999** (31/12/9999 por exemplo), o Sistema pode entrar em ***looping***e não conseguir finalizar a gravação dos dados incluídos.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7431054040215)

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Lançamentos Fixos - Campo Proporcional](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgRsKrUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBhWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MDI0MTU1My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTGFuJUMzJUE3YW1lbnRvcy1GaXhvcy1DYW1wby1Qcm9wb3JjaW9uYWwGOwhUOg5zZWFyY2hfaWRJIiljNWM2N2I0Yy1jMDMwLTRhZWUtOTYwMS04YTk4OWJhNzRmZjIGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhVsYW7Dp2FtZW50byBmaXhvBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--52519706e89bd4214701b67636829c8d60b51d8f)  
[RH - Linha Protheus - GPE - Qual é a rotina para Lançamentos de Verbas para o cálculo da folha?](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXbVVv4Qs6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBsGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEzMDYyODYzNDE2NTk5LVJILUxpbmhhLVByb3RoZXVzLUdQRS1RdWFsLSVDMyVBOS1hLXJvdGluYS1wYXJhLUxhbiVDMyVBN2FtZW50b3MtZGUtVmVyYmFzLXBhcmEtby1jJUMzJUExbGN1bG8tZGEtZm9saGEtBjsIVDoOc2VhcmNoX2lkSSIpZTUxNWI0YjEtYjZlNi00YTdiLWI5YmMtYjUzNGQ0NWRlYzhiBjsIRjoJcmFua2kPOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIMZ3BlYTU4MAY7CFQ6EnJlc3VsdHNfY291bnRpAg0D--2a7ec57589c2bd529d798b5503190b3d745d0955)  
[RH - Linha Protheus - GPE - Como abrir uma nova tela para que seja informado os dados do outro Empregador na rotina de lançamentos fixos](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXXu2wAgQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBzmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDk2MDQ3OTE4MzEtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tYWJyaXItdW1hLW5vdmEtdGVsYS1wYXJhLXF1ZS1zZWphLWluZm9ybWFkby1vcy1kYWRvcy1kby1vdXRyby1FbXByZWdhZG9yLW5hLXJvdGluYS1kZS1sYW4lQzMlQTdhbWVudG9zLWZpeG9zBjsIVDoOc2VhcmNoX2lkSSIpZGZiY2NlNDEtMmEwOS00YzYyLWIyN2QtYWM1NTRhOTU5NDQ2BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIMZ3BlYTU1MAY7CFQ6EnJlc3VsdHNfY291bnRpAugC--68503a09d92505a609f08438e758970bd3f0e7d4)
