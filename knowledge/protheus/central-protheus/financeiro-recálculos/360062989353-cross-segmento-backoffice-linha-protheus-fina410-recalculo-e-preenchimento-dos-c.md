---
article_id: 360062989353
category: Financeiro - Recálculos
content_hash: d58dad100eda91dae6ed2498157947ae093beed09e1b106903df2aec5ce5a6b8
fetched_at: '2026-06-28T22:38:20.133796+00:00'
product: protheus
section_id: 1500001550362
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA410 - Recalculo e preenchimento
  dos campos A1_MSALDO, A1_MCOMPRA e A1_MAIDUPL.
type: support-article
updated_at: '2026-02-13T12:40:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062989353-Cross-Segmento-Backoffice-Linha-Protheus-FINA410-Recalculo-e-preenchimento-dos-campos-A1-MSALDO-A1-MCOMPRA-e-A1-MAIDUPL
---

**Dúvida**  
Ao executar a rotina **Refaz Dados Cliente**/**Fornecedor** (**FINA410**), o sistema não realiza o recálculo dos campos **A1\_MSALDO**, **A1\_MCOMPRA** e **A1\_MAIDUPL**?  
  
**Ambiente**  
Microsiga Protheus – Financeiro – FINA910 – A partir da versão 12.1.17  
  
**Solução**  
Na rotina de cadastro de clientes **(MATA030)**, é obrigatório verificar o campo **A1\_MOEDALC**. Este campo deve estar preenchido com o valor 1; caso seja identificado qualquer valor diferente, deverá ser efetuada a devida correção.

Importante:  
O preenchimento correto e o recálculo dos campos citados devem seguir rigorosamente as orientações descritas na documentação correspondente.

**Saiba Mais**  
[Refaz dados cliente/fornecedor (FINA410)](https://tdn.totvs.com/pages/releaseview.action?pageId=254607843)  
[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Composição dos Campos de saldo e vendas na tabela SA1 (MATA030)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000676288)
