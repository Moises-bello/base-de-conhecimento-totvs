---
article_id: 360020130151
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 529388ddc267af38717a6dc56627c8e59cb984d8e11b6b69e6f9122f130fbcdb
fetched_at: '2026-06-28T22:38:43.968809+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Restaurando
  nota fiscal excluída indevidamente
type: support-article
updated_at: '2026-03-23T18:14:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020130151-Cross-Segmentos-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Restaurando-nota-fiscal-exclu%C3%ADda-indevidamente
---

**Dúvida**

Como restaurar Nota Fiscal Excluída Indevidamente do Sistema?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT – todas as versões.

**Causa**

A nota foi indevidamente excluída do sistema porém está Autorizada no SEFAZ e não pode/não deve ser Cancelada.

**Solução**

A exclusão do Documento de Saída do Protheus em relação ao Status da Nota junto ao SEFAZ são distintos.

Se o usuário exclui o documento de saída do sistema, então, para o sistema, este documento está cancelado, deste modo é preenchido o campo **F3\_OBSERV** com "NF CANCELADA".

Porém, a transmissão e autorização desse cancelamento junto ao SEFAZ é uma etapa posterior e independente.

Para restaurar a nota no sistema, efetue os seguintes procedimentos:

1 - Altere a Data Base para o dia da emissão do Pedido/Nota

2 - Incluir e liberar um Pedido de Vendas (**MATA410**) com todos os dados da Nota em excluída

3 - Acionar a Preparação do Documento de Saída com a mesma numeração de saída do documento de saída excluido indevidamente (**MATA460A**).

No momento de "Preparar documento de saída" é aberta uma janela para selecionar a *'Série   |   Núméro de nota'* que irá gerar.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9033646384279)

***OBS1:** Avalie se o número sugerido é o número que realmente corresponde à esta Nota no SEFAZ.*

***OBS2:*** Caso seja necessário editar a numeração manualmente para que fique compatível ao SEFAZ.

* Caso seu parâmetro esteja (MV\_TPNRNFS = 1 ou 2) dê 2 cliques em cima do número da Nota e o campo será aberto para alteração.
* Caso seu parâmetro esteja (MV\_TPNRNFS = 3), deixe o parâmetro (MV\_MUDANUM = .T.) e dê 2 cliques em cima do número da Nota e o campo será aberto para alteração.  
  [**FAT0049 Controle de Numeração de Documento de Saída no Protheus**](https://tdn.totvs.com/pages/viewpage.action?pageId=329024579)  
    
  ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9033862750359)

4 - Digitar manualmente o número correto da nota

5 - Preparar o Documento de Saída

**Saiba Mais:**  
[**Restaurar Nota excluída indevidamente do sistema**](http://tdn.totvs.com/pages/releaseview.action?pageId=364928856)
