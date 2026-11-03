---
article_id: 4416022728855
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: b26b6d4b6fd020de0713efa840d947671686f488793afa5d7e4808f78af1d3ca
fetched_at: '2026-06-28T22:39:22.179106+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Notas Fiscais Denegadas
  sendo apresentadas no relatório P9 (MATR940)
type: support-article
updated_at: '2021-12-15T16:36:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416022728855-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Notas-Fiscais-Denegadas-sendo-apresentadas-no-relat%C3%B3rio-P9-MATR940
---

**Dúvida**

Notas Fiscais Denegadas sendo apresentadas no relatório P9 (MATR940)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - Todas as versões  
  
**Solução**

Verificar o conteúdo dos campos **F3\_CODRSEF, F3\_OBSERV e F3\_DTCANC**

No sistema Protheus as notas Denegadas devem ser excluídas para que o sistema estorne as movimentações da nota (estoque, financeiro, contabilização, entre outros processos).

Ficará registrado na tabela (SF3) Livros Fiscais no campo **F3\_CODRSEF**= 301; 302 ou 205

**F3\_OBSERV**= NF DENEGADA e **F3\_DTCANC=** a data de Exclusão da Nota Fiscal

Caso a Nota Fiscal Denegada não seja Excluída no sistema o campo **F3\_DTCANC** ficará vazio e a Nota Fiscal Denegada será considerada no relatório

**Informações adicionais:**

Uma NF-e pode ser denegada não apenas por irregularidade fiscal do emitente, mas também por irregularidade fiscal do destinatário, de acordo com a rejeição:

* 301 - Uso Denegado: Irregularidade fiscal do emitente;
* 302 - Uso Denegado: Irregularidade fiscal do destinatário;

Existe também o código:

* 205 - Rejeição: NF-e está denegada na base de dados da SEFAZ (este será apresentado quando há tentativa de nova transmissão de uma nota que já foi denegada no sistema).

Assim, se uma empresa que estiver em situação regular emitir uma NF-e, mas informar nos dados do destinatário uma Inscrição Estadual baixada, então essa nota está sujeita a ser denegada. Nesse caso, o emitente pode corrigir os dados do destinatário e emitir uma nova nota.

Vale atentar-se ao fato de que a denegação é diferente da rejeição. Uma nota que foi rejeitada pode ser corrigida e retransmitida com o mesmo número.

**Uma nota que foi denegada não pode ser retransmitida com o mesmo número**. Esta ficará com situação de “Denegada”.

**Parecer da Consultoria de Segmentos da  TOTVS  referente a este tipo de nota:**

[http://tdn.totvs.com/pages/viewpage.action?pageId=134152528](https://tdn.totvs.com/pages/viewpage.action?pageId=134152528)
