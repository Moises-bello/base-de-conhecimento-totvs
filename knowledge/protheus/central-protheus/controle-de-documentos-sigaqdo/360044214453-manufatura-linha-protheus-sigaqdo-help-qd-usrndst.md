---
article_id: 360044214453
category: Controle de Documentos (SIGAQDO)
content_hash: 75a97af01d0e968f64015fa84da06d626b99d470d2c086e44e45fe933eabdc83
fetched_at: '2026-06-28T22:42:29.176861+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help QD_USRNDST
type: support-article
updated_at: '2021-08-23T16:31:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044214453-Manufatura-Linha-Protheus-SIGAQDO-Help-QD-USRNDST
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:20 min**  
**Ocorrência**No módulo **SIGAQDO - Controle de Documentos**, ao tentar realizar a distribuição do documento na rotina **QDOA110 - Distribuição de Documentos** é apresentado o *help* **QD\_USRNDST - O usuário atual não está cadastrado como distribuidor de documentos ou não existe pendências de Distribuição**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**Esse incidente ocorre em duas situações:

* Quando o usuário não está parametrizado para ser distribuidor de documentos;
* Ou quando não existe documento para este usuário onde o tipo da pendência seja igual à **I-Distribuição**, ou seja, nenhum documento onde o campo **QD1\_TPPEND - Tipo Pend** seja igual à **I**.

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse a rotina **QAXA010 - Cadastro de Usuários** e consulte o usuário em questão;  
2. Verifique no cadastro deste usuário se o campo **Distrib. Doc** está como **Sim**;  
3. Caso o campo **Distrib. Doc** já esteja como **Sim**, abra a tabela **QD1 - Distribuição por Usuário** via **APSDU** e filtre pelo campo **QD1\_MAT - Cod Usuário**, informando o código da matrícula deste usuário, e verifique se existe algum documento onde o campo **QD1\_TPPEND** seja igual à **I** e o campo **QD1\_PENDEN - Pendência** igual à **P - Pendente** .
