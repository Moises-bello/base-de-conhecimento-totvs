---
article_id: 360025846812
category: Financeiro - Baixas a Receber
content_hash: 1bd99188eee949fc458d1cd926e6b446552cd999f1f339c60e585ec69ebd7ce7
fetched_at: '2026-06-28T22:37:43.687804+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN  - FINA070 - Como configurar
  o sistema para gerar movimento bancário ao realizar a baixa de títulos do tipo NCC
  e RA
type: support-article
updated_at: '2025-07-30T17:18:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025846812-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA070-Como-configurar-o-sistema-para-gerar-movimento-banc%C3%A1rio-ao-realizar-a-baixa-de-t%C3%ADtulos-do-tipo-NCC-e-RA
---

**Ocorrência**Como configurar o sistema para gerar movimento bancário ao realizar a baixa de títulos do tipo NCC e RA?  
  
**Ambiente**Cross Segmento – TOTVS Backoffice (Linha Protheus)  – Financeiro – FINA070 - Todas as versões

**Causa**

Ao realizar a baixa de um recebimento antecipado (devolução ao cliente), o sistema está registrando corretamente a movimentação bancária na tabela *SE5*. No entanto, o campo ***E5\_TIPODOC*** está sendo gravado com o valor **"BA"** em vez de **"VL"**, o que impede a geração da movimentação no banco correspondente e, consequentemente, a atualização do saldo bancário.

**Solução:**

1. Acesse a rotina **Baixas a Receber Manual (FINA070)**;
2. Pressione **F12** para acessar os parâmetros/perguntas da rotina;
3. Altere o parâmetro **"Gera Cheque p/ Adiantamento"** para **"Não"**;
4. Em seguida, realize a baixa do título do tipo **NCC** ou **RA** – dessa forma, o sistema gravará *E5\_TIPODOC* com o valor **"VL"**, permitindo a correta geração da movimentação bancária e atualização do saldo.
