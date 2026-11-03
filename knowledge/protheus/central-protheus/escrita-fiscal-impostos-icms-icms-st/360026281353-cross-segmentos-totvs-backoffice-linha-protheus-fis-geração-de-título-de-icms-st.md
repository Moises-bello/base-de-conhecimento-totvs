---
article_id: 360026281353
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 23b49f247e397be80681caeaeb5aa37e7a8cd43e341af40a2484eeb992f2fc5e
fetched_at: '2026-06-28T22:39:20.296002+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Geração de Título
  de ICMS-ST no Contas a Pagar pelo Documento de Saída?
type: support-article
updated_at: '2021-07-13T17:27:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026281353-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Gera%C3%A7%C3%A3o-de-T%C3%ADtulo-de-ICMS-ST-no-Contas-a-Pagar-pelo-Documento-de-Sa%C3%ADda
---

**Dúvida**

Como gerar titulo de ICMS-ST no contas a pagar via documento de saída?

**Ambiente**

Protheus – Faturamento – A partir da versão 11.80  
  
**Solução**

No momento da geração do documento de saída alterar a pergunta Gera Título = Sim.

Verifique também o parâmetro **MV\_RECST??**  indica o **Fornecedor Padrão** de cada **Estado** para geração dos **Títulos a Pagar do ICMS com Substituição Tributária.**

Na configuração deste parâmetro precisamos informar o **Código** e a **Loja do Fornecedor Padrão** para geração dos títulos de **Substituição Tributária** para cada **Estado** e que terá o seguinte formato:

**Exemplo**

**CCCCCC;LL**sendo **CCCCCC** o **Código do Fornecedor** e **LL** a **Loja do Fornecedor.**

É muito importante que os **códigos do Fornecedor** e da **Loja** sejam informados exatamente com o tamanho dos campos **A2\_COD** e **A2\_LOJA**, disponibilizados no sistema.

No exemplo acima, o campo **A2\_COD** tem 6 caracteres e o campo **A2\_LOJA,** 2 caracteres.

**Sugestão de conteúdo**: 000001;01

Se a Inscrição Estadual for preenchida para esta UF e for informada no parâmetro MV\_SUBTRIB, o título será gerado pela Apuração de ICMS. Outra condição em que não haverá a geração do título refere-se à operação dentro do Estado.
