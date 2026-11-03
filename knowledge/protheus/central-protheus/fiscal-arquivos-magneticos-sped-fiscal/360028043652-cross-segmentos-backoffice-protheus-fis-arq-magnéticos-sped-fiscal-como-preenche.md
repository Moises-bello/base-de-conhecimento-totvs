---
article_id: 360028043652
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: cd2605da0a43089b4507778d1d5f9296db0869ca476814f843026fc5c2e6b96e
fetched_at: '2026-06-28T22:42:02.302467+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Sped Fiscal
  - Como preencher o campo CST_ICMS nos Registros C170 e C190
type: support-article
updated_at: '2025-02-11T21:19:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028043652-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Como-preencher-o-campo-CST-ICMS-nos-Registros-C170-e-C190
---

**Dúvida**Como preencher o campo **CST\_ICMS** nos Registros **C170** e **C190** do **Sped Fiscal**?  
   
 **Ambiente**Microsiga Protheus – Financeiro – A partir da versão 11.80  
  
**Solução**Preencha os campos **B1\_ORIGEM** (Cadastro do Produto) e **F4\_SITTRIB** (Cadastro da **TES**), depois do preenchimento desses campos o sistema grava a tabela **FT\_CLASFIS**, com a informação do **B1\_ORIGEM**+**F4\_SITTRIB**.

Portanto se o campo estiver em branco, ocasionará erro de validação.

Para notas antigas preencha o campo **FT\_CLASFIS**,  pela rotina de Acertos Fiscais, pelo Banco de Dados ou via **APSDU** e assim gerará corretamente o campo quando preenchido **B1\_ORIGEM** e **F4\_SITTRIB**.
