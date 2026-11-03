---
article_id: 360018836892
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 8a6dba75b468d286d121deaf0c5f9f35b4c6c76a462797aa79264727652f5845
fetched_at: '2026-06-28T22:39:22.190378+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Código de lançamento
  inválido ao inserir código de ajuste na Apuração do ICMS (MATA953)
type: support-article
updated_at: '2021-07-15T17:52:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018836892-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%B3digo-de-lan%C3%A7amento-inv%C3%A1lido-ao-inserir-c%C3%B3digo-de-ajuste-na-Apura%C3%A7%C3%A3o-do-ICMS-MATA953
---

**Dúvida**

Ao inserir um código de ajuste na apuração do ICMS (MATA953) é apresentada a seguinte mensagem:

Código de lançamento inválido!

Verifique a UF, o reflexo e o tipo de apuração do lançamento selecionado.

**Ambiente**Protheus - Livros Fiscais -  Todas as versões  
  
   
**Solução**

A mensagem é apresentada quando a UF configurada no parâmetro MV\_ESTADO não condiz com o código de ajuste utilizado na apuração do ICMS.

Importante: É necessário que seja criado um parâmetro MV\_ESTADO para cada filial.

Outro ponto importante é verificar se o código de ajuste utilizado é de fato correspondente a linha da apuração na qual está sendo informada.

Caso seja informado um código de ajuste referente a Débito em uma linha de Crédito na apuração do ICMS a mesma mensagem será apresentada.
