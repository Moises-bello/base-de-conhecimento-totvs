---
article_id: 6573655208855
category: Gestão de Distribuição (SIGAOMS)
content_hash: 371c86382eac5d289800ab2552715b5e8a66fee7102507c87f3a36438ca17657
fetched_at: '2026-06-28T22:45:49.826225+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Exclusão de Documentos de Saída - Carga
type: support-article
updated_at: '2025-08-14T12:47:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6573655208855-Log%C3%ADstica-Linha-Protheus-OMS-Exclus%C3%A3o-de-Documentos-de-Sa%C3%ADda-Carga
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22352591973143) Tempo aproximado para leitura: **00:02:54 min** **Dúvida**Quais os comportamentos do Sistema na **Exclusão de Documentos de Saída - Carga - MATA521B**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**  
No programa de **Exclusão de Documentos de Saída - Carga - MATA521B** existem parâmetros que podem ser configurados ao pressionar a tecla **F12.** Para a exclusão da carga, o pergunte **Retornar Ped. Venda?** é que influenciará de acordo com a opção escolhida. Quando selecionado:

* **Apto a Faturar**: a nota fiscal será eliminada e a carga será mantida na rotina **OMSA200 - Montagem de Carga** com o *status* igual a **Aberto.** O pedido de venda será preservado na carga, bem como a sua liberação. Exceto pedidos com algum **tipo de Bloqueio** que necessitarão serem liberados novamente. Com isso, o Sistema reativará a tabela **SC9 - Liberação de Pedidos** com o bloqueio para esse pedido de venda. Esse é conceito do módulo de **Faturamento - SIGAFAT**.
* **Carteira**: a nota fiscal será eliminada e a carga será excluída do programa **OMSA200**. A liberação do pedido será desfeita, isto é, o pedido de venda voltará para situação de **Não Liberado.**

![5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22356532316823)

**Importante**Ao usar a opção **Apto a Faturar**, considere os seguintes comportamentos**:**

* Se a carga faturada contém apenas um pedido de venda com bloqueio estoque ou crédito, ao excluir via MATA521B, a tabela SC9 será reativada com o bloqueio para nova liberação. Como há apenas um pedido, a carga será excluída.
* Se a carga faturada contém vários pedidos e algum deles está bloqueado, após a exclusão, a SC9 será reativada para nova liberação. Apenas o pedido bloqueado será removido da carga, já que a carga é gerida pela tabela SC9.
* Para excluir documentos específicos dentro da carga, utilize a rotina Exclusão de Documentos de Saída - Docs - MATA521A. Somente o documento selecionado será excluído, mantendo os demais faturados e o status da carga como Faturada. Para refaturar o pedido relacionado ao documento excluído, ative o parâmetro MV\_MANCARG, exclua o pedido da carga via OMSA200 e, em seguida, inclua-o em uma nova carga para seguir o fluxo normal de faturamento.

**Saiba mais**  
Mais informações poderão ser acessadas nos *links:*[Logística - Linha Protheus - OMS - Faturamento por carga no TOTVS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027664131-Log%C3%ADstica-Linha-Protheus-OMS-Faturamento-por-carga-no-TOTVS-OMS) [OMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027664131-Log%C3%ADstica-Linha-Protheus-OMS-Faturamento-por-carga-no-TOTVS-OMS)  
[Logística - Linha Protheus - OMS - Exclusão de Documento de Saída - Carga apresenta mensagem de Falta Índice 3 para tabela DK1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410652120215-Log%C3%ADstica-Linha-Protheus-OMS-Exclus%C3%A3o-de-Documento-de-Sa%C3%ADda-Carga-apresenta-mensagem-de-Falta-%C3%8Dndice-3-para-tabela-DK1)
