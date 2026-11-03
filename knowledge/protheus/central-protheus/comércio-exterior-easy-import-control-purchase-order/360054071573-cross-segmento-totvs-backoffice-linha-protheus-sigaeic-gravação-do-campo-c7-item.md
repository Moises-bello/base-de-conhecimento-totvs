---
article_id: 360054071573
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: 5d58efde96a7f3901b5ca8de6e32600cd2b490990b56952fb042fed94337a44d
fetched_at: '2026-06-28T22:39:41.166186+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Gravação do campo
  C7_ITEMCTA
type: support-article
updated_at: '2022-06-02T13:25:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054071573-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Grava%C3%A7%C3%A3o-do-campo-C7-ITEMCTA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Ao gerar a Purchase Order não grava o campo C7\_ITEMCTA no pedido de compra?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control - Todas as versões  
  
**Solução**O módulo SIGAEIC não possui preenchimento na SW3 para o campo C7\_ITEMCTA , porém quando informado o conteúdo deste campo na Solicitação de Compra ao gerar a Purchase Order, será gravado o campo C7\_ITEMCTA  de acordo com o conteúdo da C1\_ITEMCTA.

Procedimento no módulo SIGACOM:  
1. Acesse Atualizações \ Solicitações \ Solicitação de Compras(MATA110);  
2. Selecione Incluir;  
3. Informe os dados de Unidade Requisitante, Cod. Comprador e Filial de Entrega;  
4. Informe o item importado e preencha o campo Item Conta (C1\_ITEMCTA), selecione o salvar:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089829013/mceclip0.png)  
5. Em Atualizações \ Solicitações \ Itens para Importação (MATA112);  
6. O filtro sera apresentado, configure o mesmo e selecione OK:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089829673/mceclip1.png)  
7. Marque a SC cadastrada e selecione Gerar, para que ocorra a integração a SI (EICSI400):  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088679494/mceclip2.png)  
  
Procedimento no módulo SIGAEIC:  
1. Acesse Atualizações \ Solic. Importacao \ Manutenção (EICSI400);  
2. Localize a SI e selecione o visualizar, no campo No. da SC (W0\_C1\_NUM) é gravado o número da solicitação de compra:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088680654/mceclip3.png)  
3. Acesse Atualizações \ Purchase Order \ Manutenção (EICPO400);  
4. Selecione Incluir;  
5. Favor preencher os dados de capa, após selecione o Salvar;  
6. Informe a unidade requisitante e Solicitação de Importação, selecione salvar:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088680914/mceclip4.png)  
7. Selecione o item após selecione o Salvar para gravação da PO:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088680994/mceclip5.png)  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088681054/mceclip6.png)  
  
8. Após gravação, acesse o módulo SIGACOM em Atualizações \ Pedidos \ Pedidos de Compra (MATA121);  
9. Localize o Pedido de Compra e selecione o visualizar, verifique que o campo C7\_ITEMCTA será gravado de acordo com o conteúdo da C1\_ITEMCTA:  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088681374/mceclip7.png)

Ponto de entrada da rotina EICPO400: <https://tdn.totvs.com/pages/releaseview.action?pageId=224102887>
