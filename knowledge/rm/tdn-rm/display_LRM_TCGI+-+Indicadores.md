---
content_hash: 91e8bdd642e333cb5d86988d6dadec7801132c796f50ba5c7276a22a75a391c1
fetched_at: '2026-06-29T00:11:38.010093+00:00'
page_id: '780787920'
product: rm
source: tdn-rm
title: TCGI - Indicadores
type: documentation
url: https://tdn.totvs.com/display/LRM/TCGI+-+Indicadores
version: 4
---

Com os indicadores é possível um melhor gerenciamento da cobrança, através de cubos e gráficos será possível realizar uma tomada de decisão precisa.

Importações

* Para importar o cubo é necessário acessar o módulo Inteligência de Negócios | Cadastro |Cubo clicar em processo "Importação de Cubos". Após a importação o cubo estará disponível na visão. Para executá-lo selecione o mesmo, clique duas vezes e preencha os parâmetros.
* Para importar o gráfico é necessário acessar o módulo Inteligência de Negócios | Gestão |Gráfico clicar em processo "Importação de Gráficos". Após a importação o Gráfico estará disponível na visão. Para executá-lo selecione o mesmo, clique duas vezes para alterar o parâmetro(filtro) após abrir o gráfico no cabeçalho da visão clique em **Parâmetros**.

Os indicadores possuem os seguinte parâmetros que são utilizados em sua geração:

| Campos: | Valor: |
| --- | --- |
| COLIGADA | -1 |
| CLIENTE | -1 |
| CONTRATO | -1 |
| IMOVEL\_EMPREEND | -1 |
| DATA\_INICIO\_VENCIMENTO | -1 |
| DATA\_FINAL\_VENCIMENTO | -1 |
| CALCULAR\_VALOR\_LIQUIDO | -1 |

* O valor informado como '-1' indica que ira retornar todos os registros, por exemplo,  Coligada = -1(Todas as Coligadas)
* Caso seja preciso filtrar apenas um registro de determinado campo é necessário informar o mesmo, por exemplo, Coligada = 2(Apenas registros da coligada 2)
* Caso seja preciso filtrar registros específicos é necessário informar o valores separados por virgula, por exemplo, Coligada = 2,4,5(Retorna registros das coligada 2, 4 e 5)
* Caso deseje que seja calculado o Valor liquido, o parâmetro CALCULAR\_VALOR\_LIQUIDO deve ser preenchido com:
  + Valor  1:  o sistema irá calcular o reajuste, juros e multa de atraso, de todas as parcelas em atraso e a performance será degradada;
  + Valor -1:  o sistema irá buscar o valor da posição atual da base , sem multa e juros de atraso (Usar sempre essa opção para melhor performance).

* [Inadimplência Financeira](https://tdn.totvs.com/pages/viewpage.action?pageId=559286431)
* [| Análise dos recebimentos por Empreendimento/Coligada](https://tdn.totvs.com/pages/viewpage.action?pageId=559286431)
* [| Recebimentos Previstos x Realizados](https://tdn.totvs.com/pages/viewpage.action?pageId=559286431)
* [| Análise da Inadimplência por Faixa de Atraso](https://tdn.totvs.com/pages/viewpage.action?pageId=559286431)
* [| Inadimplência Mensal por Empreendimento ou Imóvel/Coligada](https://tdn.totvs.com/pages/viewpage.action?pageId=559286431)
* [| Atendimentos Abertos x Concluídos](https://tdn.totvs.com/pages/viewpage.action?pageId=559286431)
* [| Cubo de Produtividade por Atendente](https://tdn.totvs.com/pages/viewpage.action?pageId=559286431)
* [| Indicadores](https://tdn.totvs.com/pages/viewpage.action?pageId=559286431)

Com o Cubo Inadimplência Financeira será possível acompanhar a inadimplência de seus clientes, com informações das parcelas vencidas que compõem a cobrança.

O cubo possui 5 cenários(Layouts) que são eles **Visão Padrão - Analítico**, **Cliente**, **Empreendimento**, **Coligada** e **Por Mês**. É importante ressaltar que o cubo possibilita a criação de novos cenários(Layouts) ou adequação dos cenários já existentes. 

O cubo possui colunas que irão facilitar a consolidação dos dados, para isso é necessário pegar a coluna e arrastar ela para a o "local" desejado, a seguir um exemplo:

Primeiramente deve ser selecionado o Cenário(Layout):

Em seguida o campo que deseja adicionar na visão:

O campo deve ser arrastado para o local desejado:
