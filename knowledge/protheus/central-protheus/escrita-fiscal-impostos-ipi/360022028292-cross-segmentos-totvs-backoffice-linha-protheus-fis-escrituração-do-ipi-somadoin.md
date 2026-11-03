---
article_id: 360022028292
category: Escrita Fiscal - Impostos - IPI
content_hash: 8e5113c297926a29a524b8a07f36a8b5aa309f92ffb221a9fbfd58ba2911a83b
fetched_at: '2026-06-28T22:39:29.035793+00:00'
product: protheus
section_id: 1500001538641
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Escrituração do IPI
  somado/incidir ao ICMS na coluna Outros do Livro Fiscal
type: support-article
updated_at: '2022-10-19T17:21:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022028292-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Escritura%C3%A7%C3%A3o-do-IPI-somado-incidir-ao-ICMS-na-coluna-Outros-do-Livro-Fiscal
---

**Dúvida**

Como escriturar/incidir o IPI na coluna Outros do ICMS?   
  
**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Inclusão de nota fiscal de entrada com cálculo de ICMS e IPI, no qual o IPI deve ser somado à base de cálculo do ICMS, destacando o valor na coluna **Outros** do Livro Fiscal.

**Cadastro de TES:**

**Calcula ICMS**= SIM;

**Calcula IPI**= SIM;

**L. Fisc. ICMS**= OUTROS;

**L. Fisc. IPI**= OUTROS/ISENTO;

**IPI na Base**= SIM;

**Agrega Valor**= SIM;

**IPI S/N. Trib**= SIM.

1)  Incluir uma nota fiscal por meio dos módulos **Compras** ou **Livros Fiscais**;

2)  Informe os dados da nota e inclua a TES cadastrada, conforme configurações acima;

3)  Verifique na aba **Livros Fiscais**que o valor destacado na coluna **Outros** é referente ao valor de ICMS + IPI calculado.

**Resultado esperado:**

Escrituração do IPI somado ao ICMS na coluna **Outros** do Livro Fiscal.
