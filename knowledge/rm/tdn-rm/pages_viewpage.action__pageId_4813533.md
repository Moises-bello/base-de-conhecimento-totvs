---
content_hash: bb44710309deab6cb67d9c9aad675b0eb7542a295b2c0d6c1ff4a8006653f296
fetched_at: '2026-06-29T00:10:19.383460+00:00'
page_id: '4813533'
product: rm
source: tdn-rm
title: Como é feito o cálculo da classe ABC dos produtos no ressuprimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813533
version: 4
---

BLOCK

Como é feito o cálculo da classe ABC dos produtos no ressuprimento

FAQ: **Como é feito o cálculo da classe ABC dos produtos no ressuprimento**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.20 |

Avaliação

**Como Fazer**Como implantar e conferir o Calculo da Classe ABC dos Produtos no Ressuprimento.

Solução

**Descrição do Processo**O Ressuprimento contempla o cálculo da classificação ABC que é uma ferramenta de controle de estoques. Ela baseia-se no princípio de que a maior parte do investimento em materiais está concentrada em um pequeno número de itens, dividindo o estoque de acordo com sua quantidade e o seu valor monetário.

Sobre a Curva ABC:

*Trata-se de classificação [estatística](http://pt.wikipedia.org/wiki/Estat%C3%ADstica) de materiais, baseada no [princípio de Pareto](http://pt.wikipedia.org/wiki/Princ%C3%ADpio_de_Pareto), em que se considera a importância dos materiais, baseada nas quantidades utilizadas e no seu valor.*

*Numa [organização](http://pt.wikipedia.org/wiki/Organiza%C3%A7%C3%A3o), a curva ABC é muito utilizada para a administração de estoques, mas também é usada para a definição de políticas de vendas, para o estabelecimento de prioridades, para a programação de produção, etc. Para a administração de estoques, por exemplo, o [administrador](http://pt.wikipedia.org/wiki/Administrador) a usa como um [parâmetro](http://pt.wikipedia.org/wiki/Par%C3%A2metro) que informa sobre a necessidade de aquisição de itens - [mercadorias](http://pt.wikipedia.org/wiki/Mercadoria) ou [matérias-primas](http://pt.wikipedia.org/wiki/Mat%C3%A9ria-prima) - essenciais para o controle do estoque, que variam de acordo com a [demanda](http://pt.wikipedia.org/wiki/Demanda) do [consumidor](http://pt.wikipedia.org/wiki/Consumidor).*

*A curva ABC, no caso de administração de estoques, apresenta resultados da demanda de cada item nas seguintes áreas:*

* *Giro no estoque;*
* *Proporção sobre o faturamento no período;*
* *Margem de lucro obtida;*

*Os itens são classificados como (Carvalho, 2002, p. 227):*

* *Classe A: de maior importância, valor ou quantidade, correspondendo a 20% do total (podem ser itens do estoque com uma demanda de 65% num dado período);*
* *Classe B: com importância, quantidade ou valor intermediário, correspondendo a 30% do total (podem ser itens do estoque com uma demanda de 25% num dado período);*
* *Classe C: de menor importância, valor ou quantidade, correspondendo a 50% do total (podem ser itens do estoque com uma demanda de 10% num dado período).*

*OBS: Os parâmetros acima não são uma regra matematicamente fixa, pois podem variar de organização para organização nos percentuais descritos.*

*O que importa é que a análise destes parâmetros propicia o trabalho de controle de estoque do analista cuja decisão de compra pode se basear nos resultados obtidos pela curva ABC. Os itens considerados de Classe A merecerão um tratamento preferencial. Assim, a conseqüência da utilidade desta técnica é a otimização da aplicação dos recursos financeiros ou materiais, evitando desperdícios ou aquisições indevidas e favorecendo o aumento da lucratividade.*

Fonte: *Wikipédia - <http://pt.wikipedia.org/wiki/Brasil>*

A análise ABC feita pelo sistema determinar o método mais econômico para controlar itens de estoque. Através da classificação torna-se possível reconhecer que nem todos os itens estocados merecem a mesma atenção. Assim permite separar os itens de estoque em grupos de acordo com o valor de demanda do período definido.

**Parametrização Necessária**

A parametrização de Custo da Classe ABC se encontra no menu | Opções | Parâmetros | RM Nucleus | Gestão de Estoque | 04.04.02 – Ressuprimento. Neste caso acessar a parametrização conforme nível de Gestão definido em Gestão de Estoque | Definições de Estoque, campo “Nível de Gestão”, que pode ser Por Coligada, Por Filial e Por Local.

**Custo Classe ABC**

Nesta opção será selecionado o custo a ser utilizado na formação da curva ABC dos Produtos. As opções disponíveis são Custo Médio ou um dos 5 preços definidos no Cadastro do Produto, pasta “Preços”.

A curva ABC será calculada com base no histórico de consumo dos produtos em um determinado período. Esse período é dado em meses e ele poderá variar de acordo com o grupo de classificação ABC. O cálculo da classe ABC poderá ser divido em grupos distintos. Nesse caso cada grupo poderá configurar parâmetros diferenciados de classificação ABC. Cada grupo de classe ABC poderá ser configurado em tipos de aplicação diferente.

**Calculo da Classe ABC dos Produtos**

1. Todos os produtos que participam de gestão de estoque (somente produtos ativos, de último nível e cujo tipo de aplicação participa de gestão de estoque) serão selecionados;  
2. Para cada produto é obtido o somatório das quantidades consumidas do período definido no cadastro de Grupo de Classe ABC, ou seja, se for definido 3 meses o sistema considera o 3 meses anterior ao corrente;  
3. Esse somatório de consumo deverá ser multiplicado por um dos preços do produto (custo médio, preço1, preço2, preço3, preço4, preço5) definidos nos parâmetros do Ressuprimento;  
4. Esse montante deverá ser ordenado em ordem decrescente na forma que os produtos de maior valor (consumo \* preço) permaneçam no início da lista;  
5. Será feito um estudo de acordo com os percentuais de classificação ABC cadastrados no grupo de classe ABC.

**Grupo de Classe ABC**

Esta localizado no menu | Cadastro | Tabelas de Ressuprimento | Grupo de Classe ABC, onde existem os seguintes campos a serem definidos.

Qtde Mês Consumo = Deverá ser informado o número de meses de consumo para obter a quantidade consumida do(s) produto(s) deste grupo.

Tipo Consumo Classe ABC

**Normal** = Utilizado para produtos que tenha saída normal de estoque, seja por venda ou consumo

**Anormal** = Utilizado para produtos que tenha saída dependendo da sazonalidade ou consumo de produtos para projetos internos na empresa. Exemplo de produto com sazonalidade: Chocolate, pois na Páscoa é superior aos outros meses do ano. Sendo assim, o consumo de chocolates na Páscoa corresponde a um consumo anormal pois a quantidade consumida nesse período poderá influenciar no valor do consumo médio.

**Ambos** = Utilizados para os dois tipos de produtos acima.

Percentual

**Classe A** = Informar o percentual em que os itens possuem alto valor de demanda ou consumo no período.  
**Classe B** = Itens que possuem um valor de demanda ou consumo no período intermediário;  
**Classe C** = Itens que possuem um valor de demanda ou consumo anual baixo ou ainda que não foram consumidos no período.

Como definir o percentual sobre as Classes:

Utilizaremos como exemplo o percentual de 80% para classe A, 15% para Classe B e 5% para Classe C

**Classe A:** Quando essa soma chegar a 80% do somatório total da lista, esses produto são de classe A.   
**Classe B:** Quando a soma chegar a 95% (80% + 15%), esses produtos da faixa de 80% até a 95% serão de classe B.   
**Classe C:** Quando a soma chegar a 100% (95% + 5%), esses produtos da faixa de 95% até a 100% serão de classe C;

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Produtos** | **Preço Unt.** | **Qtd X-1** | **Qtd X-2** | **Qtd X-3** | **Qtd Total** | **Preço Total** |
| Biscoito | R$ 1,00 | 5 | 10 | 34 | 50 | R$ 50,00 |
| Iogurte | R$ 2,50 | 5 | 0 | 1 | 6 | R$ 15,00 |
| Danete | R$ 2,50 | 0 | 1 | 1 | 2 | R$ 5,00 |
| Queijo | R$ 10,00 | 1 | 1 | 1 | 3 | R$ 30,00 |
| Requeijão | R$ 3,00 | 0 | 0 | 0 | 0 | R$ - |
| **TOTAIS** | R$ 19,00 | 11 | 12 | 37 | 60 | R$ 100,00 |
|  |  |  |  |  |  |  |
| **\*Onde 'x' é o mês atual** |  |  |  |  |

- Classificando os produtos em ordem decrescente e aplicando a Classe correspondente:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Produtos** | **Preço Total** | **Percentual** | **Percentual Acumulado** | **Classe ABC** |
| Biscoito | R$ 50,00 | 50% | 50% | A |
| Iogurte | R$ 30,00 | 30% | 80% | A |
| Danete | R$ 15,00 | 15% | 95% | B |
| Queijo | R$ 5,00 | 5% | 100% | C |
| Requeijão | R$ - | 0% | 100% | D |
| **TOTAIS** | R$ 100,00 | 100% | 100% | - |

OBS: A Classe D foi informada para o produto por não existir consumo para o mesmo durante o período definido, assim ele irá se destacar dos demais que tiveram movimentação, porem para efeito de atualização de tempos os produtos com classificação “D” irão utilizar os mesmos dados da Classe C.

* Considerações Gerais: Deve-se tomar cuidado ao procedimento da análise, pois o desprezo para os itens classificados como C podem acarretar os muitos problemas, devido ao grau de criticidade do item no processo de manutenção.
* Vejamos, um biscoito possui baixo valor, porém é de grande importância para o calculo.
* Então deveremos realizar uma análise de criticidade para os itens utilizados pela empresa, a qual deverá  ser acordada com os usuários dos itens.
* Desta forma verificamos que poderemos obter a classificação A, B C por duas formas de análise. Não descartamos  a possibilidade da empresa em definir outras variáveis que levem a classificação ABC dos estoques, pois a necessidade e atividade são também variáveis a cada empresa.

**Amarração da Classe ABC ao Produto**

Após a criação do Grupo de Classe ABC, acessar o menu | Cadastro | Tabelas de Ressuprimento | Tipo de Aplicação, habilitar a opção para “**Atualizar Classe ABC**” e informar no campo “**Grupo de Classe ABC**” a classe desejada.

Depois de informado o Grupo de Classe ABC no Tipo de Aplicação, basta acessar o cadastro de produto pasta “Detalhes” subpasta “Outros Dados” no campo “**Tipo de Aplicação**”,e informar o tipo de aplicação ser utilizado, assim durante a rotina de atualização da Classe ABC o campo “**Classe ABC**” do anexo “Informações de Estoque” do produto será atualizado.

**Atualização da Classe ABC**

Para atualizar a **Classe ABC** aos níveis de estoque definidos para o(s) produto(s), anexo “Informações de Estoque”, será necessário acessar o menu Ressuprimento | Processos, habilitar a opção “Calcular Curva ABC” e em seguida “Avançar” executar o processo e terminar o processo.

OBS1: Para que o sistema calcule corretamente a Curva ABC dos produtos, no período parametrizado no Grupo de Classe ABC, o calculo do Consumo deste mesmo período já dever ter sido executado anteriormente ou juntamente com a atualização da Curva ABC.

OBS2: Ao executar o processo de “**Calcular Curva ABC**”o sistema preenche na tabela TCALCULOCLASSEABC as informações de Valor Consumido, campo TCALCULOCLASSEABC VALORCONSUMO, do período parametrizado, bem como do preço utilizado, campo TCALCULOCLASSEABC.PRECOUSADO, conforme parâmetros do Ressuprimento.

**Informações Adicionais**

Somente produtos ativos, de último nível e cujo tipo de aplicação participa de gestão de estoque irá atualizar a Classe ABC

\*Data de Produção do Documento: 29/12/2010
