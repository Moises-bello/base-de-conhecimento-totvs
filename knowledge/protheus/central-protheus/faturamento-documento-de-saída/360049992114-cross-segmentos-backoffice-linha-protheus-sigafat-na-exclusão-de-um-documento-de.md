---
article_id: 360049992114
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 0dd00a7ca2daffde08c5b5f0731a26c0a9c388b410582fa5c7cdfdddcaa6e833
fetched_at: '2026-06-28T22:38:43.976296+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: 'Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT - Na exclusão de um
  Documento de Saída, é apresentado o Help: NAOEXCL.'
type: support-article
updated_at: '2024-01-10T18:57:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049992114-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Na-exclus%C3%A3o-de-um-Documento-de-Sa%C3%ADda-%C3%A9-apresentado-o-Help-NAOEXCL
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**Ao tentar realizar a exclusão de um Documento de Saída, o sistema apresenta o **Help: NAOEXCL, como resolver?**

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - A partir da versão 12.

**Causa**

Este HELP informa que a Nota Fiscal não pode ser excluída, pois existe uma nota de devolução vinculada à ela:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075911514/mceclip0.png)

Neste processo foi realizada uma nota de saída, posteriormente foi realizada a devolução desta nota, agora o usuário esta tentando excluir a nota de saída que já foi devolvida e o sistema não permite essa ação.

**Solução**

1. Localize o Documento de Entrada (**MATA103**) que realiza a devolução da nota de saída (filtre a tabela pelo campo "Docto. Orig. [D1\_NFORI]", se a nota fiscal de saída a ser excluida é por exemplo "123456", deve ser preenchido para a procura "123456" no campo D1\_NFORI)

2. Depois de encontrar os documentos que fazem ligação com a nota fiscal de saída (pode ser mais de um), exclua os documentos de Entrada (**MATA103**);

3. Após este processo, o sistema permitirá a exclusão do Documento de Saída (**MATA521A**).
