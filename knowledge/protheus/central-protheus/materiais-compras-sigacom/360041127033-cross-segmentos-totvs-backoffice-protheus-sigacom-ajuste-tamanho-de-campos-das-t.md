---
article_id: 360041127033
category: Materiais - Compras (SIGACOM)
content_hash: 761f7d7edae08d890539ed6caa3896b03e4b0f6367cfa201b90fef33f028f47f
fetched_at: '2026-06-28T22:41:13.117535+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ajuste tamanho de campos
  das tabelas SCX, SCH, SDE e CNZ
type: support-article
updated_at: '2022-05-16T21:13:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041127033-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ajuste-tamanho-de-campos-das-tabelas-SCX-SCH-SDE-e-CNZ
---

**Dúvida**

Ajuste tamanho de campos das tabelas SCX, SCH, SDE e CNZ

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054424913/mceclip0.png)

**Ambiente**  
Protheus – Compras – A partir da versão 12  
  
**Solução**

No documento de Entrada, quando utilizado rateio com múltiplas naturezas conforme habilitado parâmetro **MV\_MULNATP**os valores da tabela **SEZ** relacionada a distribuição de Naturezas em centros de custo estão sendo gravados com divergência de valores.

Para que os valores entre as tabelas de rateio **SCX, SCH, SDE**e**CNZ** possam se relacionar corretamente com a tabela **SEZ**, devem conter o mesmo número de casas decimais nos campos de percentual. 

**SEZ**  - Distribuição de Naturezas em CC

**SCX** - Rateio Solicitação de Compra  

**SCH** - Rateio Pedido de Compra  

**SDE** - Rateios da Nota Fiscal  

**CNZ** - Rateios itens do Contrato 

Para essa situação foi gerado um pacote de Dicionário contendo a alteração da propriedade de edição **X3\_DECIMAIS**dos seguintes campos:

* **CX\_PERC**
* **CH\_PERC**
* **DE\_PERC**
* **CNZ\_PERC**

**Para esse processo atualize o dicionário de dados, para download [clique aqui e consulte dentro do pacote acumulado conforme sua versão](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)**

**Atenção**

*Todo o processo deve ser validado primeiramente em ambiente de homologação.*
