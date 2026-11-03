---
article_id: 12382578156695
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: f4b97854c2a05a6c1454613071bdd83dba1768e43768410fb4f29cb76fae3a1a
fetched_at: '2026-06-28T22:38:39.859724+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGAFAT - Help: A410VLDIF no faturamento'
type: support-article
updated_at: '2026-04-10T20:04:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12382578156695-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-A410VLDIF-no-faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15277923096215) Tempo aproximado para leitura: **00:03:30 min**  
  
**Ocorrência**  
Ao devolver uma compra aparece o Help: A410VLDIF, como retornar o item pelo pedido de venda?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões  
  
**Causa**

O sistema verifica se a **quantidade do C6\_PRCVEN** é diferente do resultado obtido nas duas verificações abaixo respectivas, se for diferente, o erro ocorre:

![ocorre.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12382032063255)

**Para que esse Help ocorra, temos três possíveis causas e elas podem ocorrer ao mesmo tempo**:

Causa 1 - Total do documento de entrada errado

Ao referenciar um documento de entrada para devolução **(Em um pedido de vendas tipo D)**, o valor total do documento de entrada **"Total (D1\_TOTAL)**" é levado ao valor total do pedido de venda **"Valor (C6\_VALOR)"**.

O conteúdo de quantidade do item no documento de entrada **"Quantidade (D1\_QUANT)"** até a quantidade do item no pedido de venda **"Quantidade (C6\_QTDVEN)"**.

Porém, o total no documento de entrada é informado pelo usuário, pelo pedido de vendas é feito a partir do cálculo da quantidade vezes o preço **(C6\_QTDVEN \* C6\_PRVEN)**.

Ao retornar, os valores trazidos do documento de entrada são:

**D1\_TOTAL -> C6\_VALOR**

**D1\_DESC -> C6\_VALDESC**

**D1\_VUNIT -> C6\_PRUNIT**

**D1\_QUANT -> C6\_QTDVEN** .

No retornar do pedido de venda, a partir da divisão do valor total pela quantidade **(C6\_VALOR / C6\_QTDVEN)** é encontrado o preço do item **(C6\_PRCVEN)**, que pode estar diferente do preço do item no documento de entrada **(D1\_VUNIT)** pois o cálculo do total do pedido é feito automaticamente (Total dividido pela quantidade) e o do documento de entrada é manual, ocasionando o erro.

**ATENÇÃO:** Os campos de preço de lista **(C6\_PRUNIT)** e preço de venda **(C6\_PRCVEN)** ao retornar no pedido de vendas, devem ser iguais ao campo **D1\_VUNIT** do documento de entrada.

***Exemplo**:*  
*Documento de entrada (MATA103):*

*![ocorre1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12382072261143)*

* D1\_QUANT == 3,67 (Levado ao C6\_QTDVEN)
* D1\_VUNIT = 99,99 (Levado ao C6\_PRUNIT)
* D1\_TOTAL = 366,90 [Errado] (Levado ao C6\_VALOR)
* D1\_DESC = 0 [Vazio no exemplo] (C6\_VALDESC)

*Pedido de Vendas (MATA410) [Ao usar a função Retornar]:*

*![ocorre2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12382109923479)*

* C6\_QTDVEN = **3,67**
* C6\_PRCVEN = **99,97** [99,972752043 (...) calculado pela divisão do total (366,90) pelo valor do item (3,67), que veio errado do documento de entrada e, depois o sistema ainda ajusta para duas casas decimais que é a quantidade decimal do campo no ambiente do exemplo]
* C6\_PRUNIT = **99,99**
* C6\_VALOR = **366,90**
* C6\_VALDESC = **0**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12406030336407)**

**99,99** [Resultado da fórmula acima] é diferente de **99,97** [C6\_PRCVEN] então o Help acontecerá.

Causa 2 - Decimais de todos os campos com quantidade decimal diferentes entre si.

Causa 3 - Customizações em campos e gatilhos da tabela SC6 sobre campos/gatilhos de preços, quantidades e totalizadores.  
  
  
**Solução**  
Solução da causa 1:

* A - Exclua a devolução dos pedidos de venda que referenciam o documento de entrada.
* B - Crie um novo documento de entrada informando corretamente o total do item **(D1\_TOTAL)** corretamente, truncando ou arredondando com margem máxima de 0,01.

Solução da causa 2:

* A - Ajustar todos os campos com a mesma quantidade decimal de acordo com a documentação: [**FAT068 - Aumento de decimais**](https://tdn.totvs.com/display/PROT/FAT0068_Aumento_de_Casas_Decimais_no_ambiente_Faturamento_SIGAFAT)
* B - Rodar as rotinas de recálculo de saldos de acordo com a documentação: [**FAT068 - Aumento de decimais**](https://tdn.totvs.com/display/PROT/FAT0068_Aumento_de_Casas_Decimais_no_ambiente_Faturamento_SIGAFAT)

Solução da causa 3:

* A - Retirar/validar as customizações nos fontes do faturamento.
* B - Retirar/validar as customizações nos campos/gatilhos da tabela SC6.
* C - Retirar/validar as customizações nos campos/gatilhos da tabela SD1.
