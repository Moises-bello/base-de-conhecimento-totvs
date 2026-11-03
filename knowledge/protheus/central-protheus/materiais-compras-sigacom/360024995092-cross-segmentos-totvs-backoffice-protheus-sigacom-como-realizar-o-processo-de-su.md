---
article_id: 360024995092
category: Materiais - Compras (SIGACOM)
content_hash: 18bad31f86bb32c587d8626e32e8e8e78e8b99d03f033caf1c1a28aed3105e56
fetched_at: '2026-06-28T22:41:08.677444+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como realizar o processo
  de Sugestão de Compras (MATA297) ?
type: support-article
updated_at: '2022-05-16T21:58:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024995092-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-o-processo-de-Sugest%C3%A3o-de-Compras-MATA297
---

**Dúvida**Como realizar o processo de Sugestão de Compras (MATA297) ?  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**Para configurar a base para o processo de Sugestão de compras verificar o procedimento :

1. Cadastro de Produtos :

Cadastre novo produto com saldo inicial, preenchendo obrigatoriamente os seguintes campos:

**Pasta Cadastrais :** Custo Stand / Preço Venda / Ult. Preço / Prod. Importado / Tipo Sugestão = 1 – Normal, Status para Venda = (Sugestão de Compra)      **N**- Normal;  **P-** Promoção;**D-**Descarte;    Eliminado.  
  
**Pasta MRP :**Tipo Prazo / Prazo Entrega / Qtde. Embalag

**Pasta Outros :**Status Venda = 1 - Normal, sendo este o status utilizado p/ Sugestão de Compra:

**1=** Normal entra na sugestão

**2=** Cancelado não entra na sugestão

**3=** Novo não entra na sugestão;

**4=**Lucrativo não entra na sugestão

**Cadastro de TES:**  
Cadastre ou utilize um TES com a seguinte configuração:  
**Atu. Pr. Compr = S**

Na **Amarração Fornecedor X Produto**, vincule o produto cadastrado a um fornecedor.

Inclua o movimento de Entrada e Saída de 3 meses anteriores para este produto, ou seja, cadastre **Solicitações de Compra**, **Pedidos de Compra**e **Notas de Entrada** (se entrada), ou **Pedido de Vend**a e **Nota de Saída**(se saída), 

Saiba mais em :

* [Sugestão de Compras](https://tdn.totvs.com.br/pages/releaseview.action?pageId=229147298)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
