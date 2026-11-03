---
article_id: 360004989432
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: bafdab1dd9c11295d4fc0f2cd847deb9a166846264f9b4a60f9c8252176d676a
fetched_at: '2026-06-28T22:37:54.995244+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - CNAB - Help: FA200OCORR'
type: support-article
updated_at: '2021-12-23T17:57:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004989432-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Help-FA200OCORR
---

**Ocorrência**Ao realizar a geração do CNAB é exibido o Help: FA200OCORR  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – A partir da versão 11.80  
  
**Causa**Ocorrência retornada pelo banco não cadastrada ou cadastrada incorretamente.

**Solução**

Verificar se há ocorrência **SEB**está devidamente cadastrada **para FILIAL que está efetuando** o processamento do retorno bancário, lembrando que a ocorrência para retorno de cobrança deve conter **EB\_TIPO = RETORNO**.

Caso não esteja cadastrado

Para solucionar essa ocorrência, realize os seguintes passos:  
1. Abra o Protheus **modulo 06 FINANCEIRO;**  
2. Acesse o menu **Atualizações>Cadastros>Ocorrências CNAB**;  
3. Ajuste o tipo de ocorrência de **R(Retorno)  ou P (Pagar)**.

Verificar se há ocorrência na **SEB** se está devidamente cadastrada para FILIAL que efetua o processamento do retorno bancário, pois que a ocorrência para retorno de cobrança deve conter **EB\_TIPO = RETORNO**.   
  
**Importante:**  
Se o código da ocorrência conter na **SEB** mas estiver com **EB\_TIPO** diferente de RETORNO, o HELP também será apresentado.

**Saibas mais:**

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020502652-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Como-configurar-as-Ocorr%C3%AAncias-CNAB>
