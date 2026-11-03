---
article_id: 360015471312
category: RH - Fechamento Período
content_hash: 75ded52f3afbfbf394f9359c551b2dc94fe4a886d1ef7a89168609cecdba4f4f
fetched_at: '2026-06-28T22:43:24.520440+00:00'
product: protheus
section_id: 360011909793
source: central-protheus
title: RH - Linha Protheus - GPE - Após fechamento da folha, sistema gera período
  aquisitivo desde admissão do funcionário com status  Ativo
type: support-article
updated_at: '2025-08-04T21:53:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015471312-RH-Linha-Protheus-GPE-Ap%C3%B3s-fechamento-da-folha-sistema-gera-per%C3%ADodo-aquisitivo-desde-admiss%C3%A3o-do-funcion%C3%A1rio-com-status-Ativo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**No módulo Gestão de Pessoal, após fechamento da folha sistema **gera período aquisitivo desde  admissão** do funcionário com status Ativo.**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Esse incidente ocorre quando o sistema **não encontra** período aquisitivo Ativo para o funcionário, sendo então **gerados** todos os períodos aquisitivos do funcionário a partir de sua data de admissão com status Ativo.  
  
**Solução**Verifique se **o último período aquisitivo**válido encontra-se Ativo, pois é a partir deste registro que o sistema realiza o controle dos períodos pendentes a pagar.

Na versão 12, o Protheus mantém um histórico dos períodos aquisitivos do funcionário através do cadastro **Controle de Dias de Direito (SRF)**.  
O período aquisitivo passa a ser **atualizado a cada fechamento de período da Folha,** atualizando por exemplo, os dias vencidos e dias proporcionais, e criando novos períodos aquisitivos.  
Para isso, o sistema verifica funcionário a funcionário **qual o último período aquisitivo aberto** (1 - Ativo) e a partir deste período, realiza a atualização do cadastro, gerando novos períodos  quando necessário.

**Importante:**Entende-se como funcionário **ativo** aquele que **não foi desligado da empresa**, ou seja, possui o campo Situação Folha (RA\_SITFOLH) diferente de **D** e **não** possui rescisão calculada.  
Apenas funcionários **desligados** possuem o cadastro de Controle de Dias de Direito com **todos períodos encerrados** uma vez que os valores remanescentes são pagos durante a rescisão.  
  
**Observações:**Em casos de sistemas migrados para o Protheus, nem sempre o cadastro de Controle de Dias de Direito é populado por completo, mantendo apenas os períodos aquisitivos a partir de uma certa data.  
  
**Saiba Mais**  
[RH - Linha Protheus - GPE - Como Funciona a Rotina Controle de Dias de Direito](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhbL5vSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBjmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNTY3MTEzMS1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1GdW5jaW9uYS1hLVJvdGluYS1Db250cm9sZS1kZS1EaWFzLWRlLURpcmVpdG8GOwhUOg5zZWFyY2hfaWRJIikyM2IwMzEyYy1lYWEwLTQzNTQtODA2Ni04NjFjMGEyZDJhMzMGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIiBjb250cm9sZSBkZSBkaWFzIGRlIGRpcmVpdG8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--610a5c909b8e7b2975ccf43be27c1a7c439f66f0)  
[RH - Linha Protheus - GPE - Relatório de dias de direito Férias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgXV5qkdgc6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBimh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzgyMDYxNDkxMTM2MjMtUkgtTGluaGEtUHJvdGhldXMtR1BFLVJlbGF0JUMzJUIzcmlvLWRlLWRpYXMtZGUtZGlyZWl0by1GJUMzJUE5cmlhcwY7CFQ6DnNlYXJjaF9pZEkiKTk0NWM2OWMwLWE3OGYtNGZmMy05MTA4LWM1YjUyNWZhNmY4NgY7CEY6CXJhbmtpDDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiCFNSRgY7CFQ6EnJlc3VsdHNfY291bnRpOA%3D%3D--7fb7ce08accc2611a54c321ac5a45af9e6913432)  
[RH - Linha Protheus - GPE - Ordem Padrão dos campos da Tabela SRF - Controle dias de Direito](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjqSVvVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBn2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA2MTgxNTI3NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtT3JkZW0tUGFkciVDMyVBM28tZG9zLWNhbXBvcy1kYS1UYWJlbGEtU1JGLUNvbnRyb2xlLWRpYXMtZGUtRGlyZWl0bwY7CFQ6DnNlYXJjaF9pZEkiKTk0NWM2OWMwLWE3OGYtNGZmMy05MTA4LWM1YjUyNWZhNmY4NgY7CEY6CXJhbmtpCzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiCFNSRgY7CFQ6EnJlc3VsdHNfY291bnRpOA%3D%3D--3a57eb4127f9fde7d5d62cbf5a702d2e8dff7689)  
[RH - Linha Protheus - GPE - Como efetuar manutenção do Controle de Dias de Direito após o fechamento do período](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjle0vVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBw2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA2MDc3OTQ5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1lZmV0dWFyLW1hbnV0ZW4lQzMlQTclQzMlQTNvLWRvLUNvbnRyb2xlLWRlLURpYXMtZGUtRGlyZWl0by1hcCVDMyVCM3Mtby1mZWNoYW1lbnRvLWRvLXBlciVDMyVBRG9kbwY7CFQ6DnNlYXJjaF9pZEkiKTIzYjAzMTJjLWVhYTAtNDM1NC04MDY2LTg2MWMwYTJkMmEzMwY7CEY6CXJhbmtpCjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiIGNvbnRyb2xlIGRlIGRpYXMgZGUgZGlyZWl0bwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--ff52b7dbfe1badcdaca4c806d3630b02a9248960)
