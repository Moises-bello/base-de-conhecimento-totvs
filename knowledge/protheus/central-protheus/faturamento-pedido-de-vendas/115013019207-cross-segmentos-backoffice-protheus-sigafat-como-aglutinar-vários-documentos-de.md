---
article_id: 115013019207
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: bdae13b0634ff81d2885eabd8e92455475a30a66353ae4621faad537a18a750d
fetched_at: '2026-06-28T22:38:39.679217+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como aglutinar vários documentos
  de saída em um único
type: support-article
updated_at: '2026-04-02T11:37:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115013019207-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-aglutinar-v%C3%A1rios-documentos-de-sa%C3%ADda-em-um-%C3%BAnico
---

**Dúvida**  
Como aglutinas pedidos iguais de um mesmo cliente para gerar uma única nota de saída?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as Versões  
  
**Solução**  
Para que mais de um Pedido sejam aglutinados na NF, validar os seguintes campos de forma que contenham o mesmo valor, para que sejam efetivamente considerados similares e aglutinados.

**OBSERVAÇÃO:**

De acordo com a lei **NT 2025.002, itens do pedido de venda com data de entrega (C6\_ENTREG) diferente entre si, serão repartidos e gerarão novas notas fiscais ao faturar, mesmo que todos os campos abaixo estejam de acordo.**

**Cheque:** [**Data prevista de entrega**](https://tdn.totvs.com/x/flCZP)

**Como aglutinar pedidos iguais de um mesmo cliente para gerar uma única nota de saída:**  
- Dt. Entrega **(C6\_ENTREG)**  
- Tipo Pedido (**C5\_TIPO**)  
- Cliente (**C5\_CLIENTE**)  
- Loja do Cliente (**C5\_LOJACLI**)

- Tipo Cliente (**C5\_TIPOCLI**)

- Cliente Entrega (**C5\_CLIENT**)  
- Loja Entrega (**C5\_LOJAENT**)

- Tipo Reajuste (**C5\_REAJUST**)

- Condição Pagamento (**C5\_CONDPAG**) [desde que seja diferente do Tipo 9, conforme faq em anexo]  
- Vendedores (**C5\_VEND'x'**) (Todos os pedidos devem ter a mesma quantidade de vendedores, registrados os mesmos códigos, e nos mesmos campos)  
- Tipo Frete (**C5\_TPFRETE**)

- Transportadora **(C5\_TRANSP)**  
- ISS Incluso **(C5\_INCISS)**  
- Recolhe ISS **(C5\_RECISS)**  
- Fornecedor ISS (**C5\_FORNISS**)  
- Presença Com **(C5\_INDPRES)**

**OBS**: Se o campo "Cod Intermed (**C5\_CODA1U)"** estiver preenchido nos pedidos de venda, este também deve estar igual aos demais.

Na preparação do documento, no browser da rotina **MATA460A**, selecione os pedidos que deverão ser aglutinados (checkbox), clique no botão "**Prep. Doc's**", selecione a pergunta "**Aglut. Ped. Iguais ?**" e deixe igual a "**Sim**", desta forma, o sistema gerará a uma única nota com os pedidos aglutinados.

**Integrações com o Pedido de Venda**

Pedidos gerados pelas integrações dos módulos **GCT** e **TMK** aglutinam Pedidos desde que as condições mencionadas acima sejam respeitadas .

O parâmetro **MV\_NUMITEN** que controla quebra de itens por nota, precisa estar configurado com um valor que comporte a quantidade de itens de pedidos a faturar.

**Saiba mais**:

[**FAT0008 Aglutinar Pedidos de Venda similares no mesmo Documento de Saída**](https://tdn.totvs.com/x/nkJtDQ)

[**Data prevista de entrega**](https://tdn.totvs.com/x/flCZP)
