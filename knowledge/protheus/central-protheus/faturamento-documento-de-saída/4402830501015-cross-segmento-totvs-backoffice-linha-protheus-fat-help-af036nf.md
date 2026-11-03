---
article_id: 4402830501015
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: bda823084b62cf23bc0e4ff5f4519ea384a5540ea0f917bc7f608e9f33dfedf8
fetched_at: '2026-06-28T22:38:43.811601+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FAT- Help AF036NF
type: support-article
updated_at: '2022-05-11T17:40:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402830501015-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FAT-Help-AF036NF
---

**Dúvida**Help AF036NF na Exclusão da NF de Saída .  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Faturamento - Todas as versões  
  
**Solução**  
Verificar se a nota fiscal foi gerada a partir da rotina  **ATFA036** de baixa de ativo.

O sistema valida para exclusão, a integridade da **SF2** com a **FN6**, além disso, quando uma nota é gerada no faturamento  possui uma sequência estruturada, começando pelo pedido (SC5 e SC6), depois é liberado gerado SC9, e depois faturado pelo MATA461 gerando SD2 e SF2, além das integrações como financeiro(SE1, SE2, SE3), fiscal (SF3 e SFT), entre outros.

Quando há exclusão desta nota, o sistema desfaz todas essas integrações retornando o pedido para em aberto (SC5 e SC6) ou apto a faturar (SC9), em nenhum momento tem ligação com a FN6 do ativo.  
  
No ativo, dependendo da informação do campo **FN6\_GERANF,** que definirá se a nota será gerada a partir da baixa do ativo, é um processo a parte do faturamento, todo a geração parte do Ativo fixo, então a exclusão via sistema tem que partir do módulo que gerou.  
  
Se o campo estiver gravado com 1 ,Configure o parâmetro **MV\_ATFVLNF** com ".T.";  
  
Na rotina de baixa, faça o cancelamento da baixa. Consultando novamente a **FN6**, verifique o campo **FN6\_STATUS**, onde este deve ser alterado para "2".
