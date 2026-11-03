---
article_id: 360028043752
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 9eba108b0710251e7efcefcc55f8895b9d158be82f49ed9c67e2c4bfa84e9c8e
fetched_at: '2026-06-28T22:42:05.146974+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Como preencher o campo CST_ICMS nos Registros C170 e C190
type: support-article
updated_at: '2023-01-04T13:16:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028043752-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Como-preencher-o-campo-CST-ICMS-nos-Registros-C170-e-C190
---

**Dúvida**Como preencher o campo **CST\_ICMS** nos Registros **C170** e **C190** do **EFD Contribuições**?  
   
 **Ambiente**Microsiga Protheus – Financeiro – A partir da versão 11.80  
  
**Solução**Preencha os campos **B1\_ORIGEM** (Cadastro do Produto) e **F4\_SITTRIB** (Cadastro da **TES**), depois do preenchimento desses campos o sistema grava a tabela **FT\_CLASFIS**, com a informação do **B1\_ORIGEM**+**F4\_SITTRIB**.

Portanto se o campo estiver em branco, ocasionará erro de validação.

Para notas antigas preencha o campo **FT\_CLASFIS**,  pela rotina de Acertos Fiscais, pelo Banco de Dados ou via **APSDU** e assim gerará corretamente o campo quando preenchido **B1\_ORIGEM** e **F4\_SITTRIB**.
