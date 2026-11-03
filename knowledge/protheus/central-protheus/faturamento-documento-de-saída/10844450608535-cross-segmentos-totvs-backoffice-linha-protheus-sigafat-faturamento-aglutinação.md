---
article_id: 10844450608535
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 61ad5623aa56bec3a90e9dfa72cde0f645dc6ebf55495a12d639019c5f95a4ca
fetched_at: '2026-06-28T22:38:45.377613+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento)
  - Aglutinação de pedidos de venda no faturamento
type: support-article
updated_at: '2026-03-25T14:26:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10844450608535-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Aglutina%C3%A7%C3%A3o-de-pedidos-de-venda-no-faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15523718727575) Tempo aproximado para leitura: **00:00:10 min**  
  
**Dúvida**  
Como aglutinar pedidos de venda no faturamento?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Protheus 12.  
  
**Solução**

**Exemplo:**

Pedido de Venda Liberado 1  
Pedido de Venda Liberado 2

**> Faturamento com as condições favoráveis acontece**

É gerado um documento de saída contendo itens do pedido 1 e 2 no registro.

Para que mais de um Pedido de venda seja aglutinado na NF, validar os seguintes campos de forma que contenham o mesmo valor, para que sejam efetivamente considerados similares e aglutinados:

**OBSERVAÇÃO:**

De acordo com a lei **NT 2025.002, itens do pedido de venda com data de entrega (C6\_ENTREG) diferente entre si, serão repartidos e gerarão novas notas fiscais ao faturar, mesmo que todos os campos abaixo estejam de acordo.**

**Cheque:**[**Data prevista de entrega**](https://tdn.totvs.com/x/flCZP)

* Tipo Pedido (**C5\_TIPO**)
* Cliente (**C5\_CLIENTE**)
* Loja do Cliente (**C5\_LOJACLI**)
* Tipo Cliente (**C5\_TIPOCLI**)
* Cliente Entrega (**C5\_CLIENT**)
* Loja Entrega (**C5\_LOJAENT**)
* Tipo Reajuste (**C5\_REAJUST**)
* Condição Pagamento (**C5\_CONDPAG**) [desde que seja diferente do Tipo 9 conforme descrito abaixo]
* Vendedores (**C5\_VEND'x'**) (Todos os pedidos devem ter a mesma quantidade de vendedores, registrados os mesmos códigos, e nos mesmos campos)
* Tipo Frete (**C5\_TPFRETE**)
* Transportadora **(C5\_TRANSP)**
* ISS Incluso **(C5\_INCISS)**
* Recolhe ISS **(C5\_RECISS)**
* Fornecedor ISS (**C5\_FORNISS**)
* Presença Com **(C5\_INDPRES)**

**Além disso, considerar:**

1. Em casos de moedas diferentes da Padrão (1), em "Atualizações > Cadastros > Moedas" a Moeda em questão (X) do Pedido de venda deve estar com uma Taxa Cadastrada para a Data em que está emitindo a nota fiscal
2. Parâmetro MV\_MOEDA(x) precisa estar devidamente preenchido e compatível com o Pedido de venda
3. Na rotina MATA455 (Liberação de Estoque) os Status dos Pedidos devem estar Liberados
4. A condição de pagamento deve ser diferente do Tipo 9 a qual não é considerada para esta operação
5. Na preparação do documento, no browser da rotina **MATA460A**, selecione os pedidos que deverão ser aglutinados (checkbox), clique no botão "**Prep. Doc's**", selecione a pergunta "**Aglut. Ped. Iguais ?**" e deixe igual a "**Sim**", desta forma, o sistema gerará uma única nota com os pedidos aglutinados
6. Com a NF Layout 3.10 o SEFAZ valida se o CFOP está compatível com o tipo da NF que é indicado na TAG FinNFE. Desta forma, em adaptação ao SEFAZ, as NFs com CFOP de Devolução, devem ser geradas com a TAG com conteúdo = 4 (devolução) e os CFOPs de Venda com TAG = 1 (Normal), não podendo mais ser em uma mesma NF. Assim, não ocorre a aglutinação se os Pedidos não tiverem CFOPs compatíveis (todos de devolução, por exemplo)
7. O parâmetro **MV\_NUMITEN**, onde é informado o número máximo de itens por Nota fiscal para controlar a quebra de nota automaticamente, deve estar com um conteúdo que comporte a quantidade de itens dos Pedidos a Faturar
8. **Integrações com o Pedido de Vendas**: Pedidos gerados pelas integrações dos módulos **SIGAGCT** e **SIGATMK**, aglutinam Pedidos em uma mesma nota desde que, as condições mencionadas acima (campos) sejam respeitadas

**Saiba mais:**

**TDN:** [**FAT0008 Aglutinar Pedidos de Venda similares no mesmo Documento de Saída**](https://tdn.totvs.com/x/nkJtDQ)  
**KCS:** [**Aglutinar\_quantidades\_do\_mesmo\_produto\_na\_NF\_Documento\_de\_Saída**](https://totvssuporte.zendesk.com/knowledge/articles/10844135008023/pt-br?brand_id=1509248)  
  
**Importante:** Devido à nova tag **<**`dPrevEntrega`**>** — que representa a **data prevista de entrega** no cabeçalho da Nota Fiscal Eletrônica (NF-e) — introduzida pela Reforma Tributária (**Nota Técnica "NT 2025.002**"), o sistema passou a validar a **data de entrega**para a geração do documento de saídaquando o campo "**Tipo Frete**  
[**Cross Segmentos - Backoffice Protheus - SIGAFAT - Pedido gerando várias notas**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37036634978711-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Pedido-gerando-v%C3%A1rias-notas)
