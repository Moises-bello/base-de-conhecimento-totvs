---
content_hash: 84b7beb2e6309a5e22a851eba91f697a649ef6fe05449e8f6b7b8bce5d722b5b
fetched_at: '2026-06-29T00:11:51.537525+00:00'
page_id: '849087431'
product: rm
source: tdn-rm
title: Envio do Código Próprio IPERGS (Antigo Código Brasíndice)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=849087431
version: 3
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Configuração**
3. **Geração Remessa**

iteVisão GeralAviso!

Conforme [publicação do IPERGS](https://www.ipesaude.rs.gov.br/instrucoes-normativas#:~:text=Instru%C3%A7%C3%A3o%20Normativa%20N%C2%BA04%20%2D%20Disp%C3%B5e%20sobre,Grande%20do%20Sul%20%E2%80%93%20IPE%20Sa%C3%BAde.), os medicamentos informados no **ANEXO ÚNICO da IN04** deixam de ser precificados pela revista Brasíndice e passam a ter os seus preços definidos em tabela própria. Essa mudança foi expedida nos patchs de 24/05/2024 do RM Saúde.

## **01. VISÃO GERAL**

Regra para preenchimento da coluna Código Brasíndice do layout do arquivo de Despesas.

Configuração

## **02. CONFIGURAÇÃO**

Acessar no menu Cadastros -> Produto -> Informações TOTVS Saúde -> Tabela de Preço

Localizar os medicamentos a ser configurado e preencher o campo Código TUSS com o valor "**00000701"**, esse código **é um coringa que** indica ao nosso sistema que será enviado o código próprio informado no campo **Código Específico (20 dígitos)**.

Preencher os campos **Código Específico (20 dígitos)** e **Preço** conforme tabela própria do IPERGS.

Geração Remessa

## **03. GERAÇÃO DA REMESSA**

Na geração da remessa, o código próprio será informado no arquivo TXT campo "13 - Cód. BRASINDICE".
