---
content_hash: 994443c225f4c299203730d91c2b1ff934e8d5536044b8f18d1502c17e24c462
fetched_at: '2026-06-29T00:09:26.703852+00:00'
page_id: '423938376'
product: rm
source: tdn-rm
title: Alteração da Unidade do Item na Cotação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938376
version: 9
---

Permite que o usuário edite unidade de cotação durante a inclusão de orçamentos do fornecedor, permitindo que a empresa consiga melhores preços comprando caixas fechadas ao invés de produtos avulsos, por exemplo.

**Parametrização do Sistema:** Para permitir a alteração da unidade de cotação o usuário deverá acessar os parâmetros da cotação em Gestão de compras | cotação | Definições Gerais 2/4: Permitir Alterar Unidade na Cotação e habilitar o recurso.

**Criação / Edição da Cotação:**   
Foram criados novos campos para informar a quantidade cotada, unidade cotada, quantidade negociada e unidade negociada(QUANTIDADEORC, CODUNDORC, QUANTIDADENEG, CODUNDNEG,). Os campos quantidade e unidade utilizados até o momento passam a se chamar quantidade solicitada e unidade solicitada, e serão apenas para leitura não sendo mais permitido alterá-los.

Na inclusão dos preços cotados/negociados será possível alterar a unidade cotada/negociada por outra unidade de mesma base. Quando isso ocorrer a quantidade cotada/ negociada será convertida para a unidade informada e arredondada para cima no  caso de ocorrerem dizimas.

Exemplo: digamos que seja solicitada a compra de 50 unidades de determinado produto. Porém o fornecedor consegue um preço melhor caso o cliente compre a caixa fechada com 60 unidades.  
Na inclusão da cotação o usuário (ou o próprio fornecedor no caso da cotação web), altera a unidade do produto para CX(caixa),  e automaticamente o sistema tenta converter a quantidade solicitada para adequar à nova unidade.

Na conversão, como as 50 unidades não representam uma caixa completa, o valor será convertido para 1 CX.   
**Unidade      Unidade Base     Fator Conversão**

UN               UN                       1,0000

CX60            UN                       60,0000

Fator de conversão de Unidades = 1/60 = 0,01667  
Quantidade orçada = 0,01667 \* 50 = 0,8333

**IMPORTANTE**: As colunas de valor cotado e valor negociado, devem ser preenchidas com base nos valores da unidade de medida orçada/negociada.  No cenário descrito acima, o fornecedor que trabalha com UN deve informar o preço da UN, o fornecedor que trabalha com CX60 (caixa de 60), deve informar o valor da CX60, independente da solicitação ser somente para 50 UN.

Para que a ordem de compra seja gerada com a quantidade arredondada, é necessário que o flag "Buscar default de casas decimais para quantidade em Unidades" esteja marcado em: Etapa 2 - Definições Gerais e o numero de casas decimais = 0, na unidade de medida. Neste exemplo, na unidade CX60.

**Agrupamento de Itens na Cotação**

Quando o usuário usar agrupamento de itens na cotação o sistema fará a conversão da quantidade negociada por item na alteração.

* **Ou seja, um cotação com dois itens iguais e quantidades diferentes foi incluída da seguinte forma**: Item Quantidade Unidade 01.01 20,0000 UN 01.01 30,0000 UN
* **Agrupando ficou da seguinte forma**: Item Quantidade Unidade 01.01 50,0000 UN
* **Ao alterar a unidade Negociada para caixa de 10 unidades cada. na tela as unidades são alteradas da seguinte forma**: Item Quantidade Unidade 01.01 5,0000 CX10
* **Porém no serviço de alteração as quantidades dos dois itens são gravadas individualmente na TITMORCAMENTO da seguinte forma**: Item Quantidade Unidade 01.01 01.01 2,0000 3,0000 CX10 CX10

Esse comportamento de visualizar os itens agrupados na tela e gravar os mesmos separadamente já é padrão do sistema, porém para esta implementação poderá ocasionar efeitos colaterais em situações especificas como por exemplo na seguinte situação:

* **Uma cotação foi feita com dois itens iguais e quantidades diferentes foi incluída da seguinte forma**: Item Quantidade Unidade 01.01 01.01 25,0000 25,0000 UN UN
* **Agrupando ficou da seguinte forma**: Item Quantidade Unidade 01.01 50,0000 UN
* **Ao alterar a unidade Negociada para caixa de 10 unidades cada. na tela as unidades são alteradas da seguinte forma**: Item Quantidade Unidade 01.01 6,0000 CX10
* **Isso ocorre por que no serviço de alteração as quantidades dos dois itens são gravadas individualmente na TITMORCAMENTO da seguinte forma**: Item Quantidade Unidade 01.01 01.01 3,0000 3,0000 CX10 CX10

Ou seja será gerada uma unidade a mais na gravação da cotação.

**Calculo da Melhor Oferta**

O calculo da melhor oferta passa a efetuar a conversão dos produtos cotados (de todos os fornecedores) para a unidade solicitada, e posteriormente efetuando o calculo da melhor oferta sobre o valor unitário calculado dos produtos. Neste ponto o calculo será o mesmo já utilizado na cotação. Por exemplo:   
A solicitação pedia 20 Unidades porém o fornecedor só tinha o produto vendido em caixas com 12 Unidades cada. Na cotação o mesmo informou a unidade do produto cotado e o sistema fez a conversão da quantidade solicitada .  
Unidade Base  
Unidade   
Fator Conversão  
UN CX12 UN UN 1,0000 12,0000   
Fator de conversão de Unidades = 1/12 = 0,083333  
Quantidade orçada = 0,083333 \* 20 =1,666 = ~ 2  
Além disso o mesmo também informou o preço de 12,00 a caixa.  
Valor Negociado = 2\* 12,00 = 24,00  
Neste casso ao efetuar o calculo da melhor oferta o sistema irá converter a quantidade negociada e o preço para a mesma unidade solicitada:  
2 CX  \* 12,00 cada  => 24 UN \* 1,00 cada  
A exibição do quadro comparativo também passa a apresentar a unidade  e a quantidade negociada utilizadas no calculo da melhor oferta. Além dos valores equalizados para compra na quantidade da unidade negociada e

**Interferência**

**Por Produto:**A interferência passa a bloquear a alteração da quantidade interferida quando algum fornecedor alterar a unidade. Assim somente poderá realizar interferência do item inteiro. A quantidade pedida é gravada na mesma unidade da negociação. Porém essa quantidade é convertida para a unidade solicitada na exibição do quadro comparativo que também passa a apresentar a unidade junto as quantidades requisitadas e pedida.

**Global:** Não sofreu alterações, mas a quantidade efetivada será gravada de acordo com a unidade negociada.

**Geração da Ordem de Compra:** A geração da Ordem de compra passa a considerar a quantidade e unidade negociada na cotação, gravando a quantidade e unidade do item na mesma quantidade e unidade que foi negociada e não mais na unidade solicitada.

**Cotação Web:** Também será possível alterar e importar a quantidade e unidade orçada na cotação web. Neste caso, se a condição de pagamento for por fornecedor ou parâmetro permita alterar a unidade de cotação estiver marcado, o sistema não apresentará a grid de itens da cotação mas continuará permitindo acessar a tela de edição do item de cotação para informar a unidade orçada.

**Estorno de Itens não Recebidos:** Foi feito um tratamento no serviço de estorno de forma a verificar qual foi a unidade da solicitação para no estorno atualizar a TITMMOVRELAC de acordo com a quantidade que esta sendo estornada.  
Além disso também foi feito um tratamento no serviço de alteração do movimento para impedir que itens parcialmente faturados sofram alteração na unidade. Este tratamento foi feito para impedir que haja inconsistência de quantidade na TITMMOVRELAC

**Item de Movimento Relacionado (TITMMOVRELAC)**

A tabela TITMMOVRELAC continua gravando a quantidade na unidade que foi solicitada, porém para que isso continuasse tendo o mesmo comportamento, no momento da geração do pedido é feita a conversão da unidade negociada para a unidade solicitada, para então gravar o valor corretamente.  
**Cancelamento da Ordem de Compra:**O cancelamento da cotação não sofreu alterações, mas o cancelamento do pedido de compras passa a verificar a unidade que foi gerada para reabrir a cotação e estornar a quantidade corretamente. Também foi feita a mesma consistência para gravar a TITMMOVRELAC, no momento do cancelamento do pedido é feita a conversão da unidade gerada para a unidade solicitada, para então gravar o valor corretamente.

**Relatórios do quadro Comparativo e geração de planilha MS Excel:**Os relatórios do quadro comparativo (Simples e Detalhado) foram alterados para apresentar as quantidade e unidades negociadas, da mesma forma que foram alterados no quadro comparativo.
