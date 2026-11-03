---
article_id: 360028698432
category: Escrita Fiscal - Impostos - ICMS - Difal
content_hash: 4df9426b09487b1faef27949cc1b1540d524f15082ee571d7db46937c791c01f
fetched_at: '2026-06-28T22:39:19.277193+00:00'
product: protheus
section_id: 1500001549902
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como gerar o título
  do DIFAL ou ICMS ST no Financeiro (contas a pagar) por operação? '
type: support-article
updated_at: '2023-05-16T10:42:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028698432-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gerar-o-t%C3%ADtulo-do-DIFAL-ou-ICMS-ST-no-Financeiro-contas-a-pagar-por-opera%C3%A7%C3%A3o
---

**Dúvida**

MP - FIS - Como gerar o título do DIFAL ou ICMS ST no Financeiro (contas a pagar) por operação?

**Ambiente**

Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Solução**

Para que seja gerado título no financeiro deve ser alterado parâmetro Gera Titulo para SIM no momento de preparar documento.

Sistema utiliza o parâmetro **MV\_RECST??**para definir fornecedor padrão de cada estado para titulo do Fundo combate a pobreza e diferencial de alíquota do estado de destino, neste parâmetro é necessário informar o **Código** e a **Loja do Fornecedor Padrão** para geração dos títulos de **Substituição Tributária** para cada **Estado** e que terá o seguinte formato:

**Exemplo**

**CCCCCC;LL**sendo **CCCCCC** o **Código do Fornecedor** e **LL** a **Loja do Fornecedor.**

É muito importante que os **códigos do Fornecedor** e da **Loja** sejam informados exatamente com o tamanho dos campos **A2\_COD** e **A2\_LOJA**, disponibilizados no sistema.

No exemplo acima, o campo **A2\_COD** tem 6 caracteres e o campo **A2\_LOJA,** 2 caracteres.

**Sugestão de conteúdo**: 000001;01
