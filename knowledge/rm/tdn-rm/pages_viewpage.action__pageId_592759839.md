---
content_hash: 88c81477e7a75d01279aedb8c5a350f2b98c451c4a0621d6ad778867314bf1e6
fetched_at: '2026-06-29T00:10:56.751939+00:00'
page_id: '592759839'
product: rm
source: tdn-rm
title: Roteiro para configuração dos Custos PEPS e UEPS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=592759839
version: 10
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Parâmetros Sistema**
   1. **Definições de Estoque \ Custos**
4. **Tela Produto**
   1. **Cadastro de Produto pasta Custos**
5. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Passo a Passo para configuração dos Custos PEPS (Primeiro a entrar e primeiro a sair) e UEPS (Último a entrar e primeiro a sair).

No RM módulo **BackOffice \ Gestão de Estoque, Compras e Faturamento,** acesse o menu **Ambiente / Parâmetros / Gestão de Estoque, Compras e Faturamento / 04.04 - Gestão de Estoque / Definições de Estoque**, na **Etapa Custos** marque as seguintes opções:

* Editar Custos no Cadastro
* Utilizar método de cálculo do custo definido no produto.

No cadastro de **Produto** na pasta **Custos**, deverá informar para o campo **Cálculo do Custo** qual será o custo a ser calculado.

**Cálculo do Custo:**

Informe qual método será utilizado para o cálculo do custo unitário do produto. As opções para este campo são:

* **Custo Médio:** o cálculo do custo unitário do produto será feito através do custo médio.
* **PEPS:** o cálculo do custo unitário do produto será feito considerando que o primeiro produto a entrar será o primeiro a sair.
* **UEPS:** o cálculo do custo unitário do produto será feito considerando que o último produto a entrar será o primeiro a sair.
* **Custo Padrão:** o cálculo do custo unitário do produto levará em consideração o preço selecionado no campo "custo Padrão".
* **Custo Específico:** O cálculo do custo através deste método só faz sentido para produtos que utilizam números de séries.
* **Custo de Aquisição:** Com esta opção marcada a avaliação de estoque do produto será pelo Custo de Aquisição e será levado em consideração o último custo unitário da tabela de estoque. No relatório de ficha física-financeira deverá aparece o título da coluna de custo como "**C. Aquisi.**" com o valor do custo de aquisição para os movimentos de saída.

Após de configurar todos os produtos,  poderá incluir as movimentações.   
Caso alguns tenham sido movimentados, será necessário efetuar a regeração de saldos e custos.

Para visualizar estes cálculos deverá gerar a ficha física financeira.

## **02. EXEMPLO DE UTILIZAÇÃO**

Suponha que em 11/10/2020 seja incluído um movimento Compra Nota Fiscal com o produto 1.01(cálculo do custo feito por PEPS) com quantidade 10 e valor unitário 5 e no dia 12/10/2020 seja incluído um outro movimento de Compra Nota Fiscal com o produto 1.01 quantidade 15 e valor unitário 13. Ao efetuar um movimento de venda com quantidade 12, ao emitir a Ficha Física Financeira deste produto será gerado para este movimento de venda duas linhas. A 1ª linha com quantidade 10 e valor unitário 5 e a 2ª com quantidade 2 , valor unitário 13,00.

Se o campo cálculo do custo estiver em branco, o cálculo será feito através do custo médio. Se o método for alterado para PEPS ou UEPS é aconselhável a regeração total dos saldos e custos do produto.  
Se o método utilizado para o cálculo do custo unitário do produto for PEPS ou UEPS não será permitido trabalhar com controle de produto por lote.

Os métodos mais comuns são:

* Custo médio.
* Primeiro a entrar, primeiro a sair (PEPS).
* Último a entrar, primeiro a sair (UEPS).

### **Custo Médio**

Este método, também chamado de método da média ponderada ou média móvel, baseia-se na aplicação dos custos médios em lugar dos custos efetivos. O método de avaliação do estoque ao custo médio é aceito pelo Fisco e usado amplamente.

Para ilustrar numericamente, suponha-se que uma empresa, no início do mês de março, possua um estoque (inicial) de 20 unidades de certa mercadoria avaliada a R$ 20 cada uma, ou seja, um total de R$ 400 de Estoque Inicial. A movimentação dessa mesma mercadoria em março é a seguinte:

| Data | Operação |
| --- | --- |
| 05/03 | Compra de 30 unidades a R$ 30,00 cada |
| 11/03 | Venda de 10 unidades |
| 17/03 | Venda de 20 unidades |
| 23/03 | Compra de 30 unidades a R$ 35,00 cada |
| 29/03 | Venda de 10 unidades |

Suponha as seguintes informações:

As 10 unidades vendidas dia 11/03 saíram do lote comprado dia 05/03;   
As 20 unidades vendidas dia 17/03 saíram do estoque inicial;   
As 20 unidades vendidas dia 29/03. saíram do lote comprado dia 23/03.

Agora vejamos como registrar a movimentação físico financeira:

| DATAS | ENTRADAS | | | SAÍDAS | | | SALDOS | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Quantidade | Valores R$ | | Quantidade | Valores R$ | | Quantidade | Valores R$ | |
|  |  | Unitário | Total |  | Unitário | Total |  | Unitário | Total |
| Saldo Anterior | - | - | - | - | - | - | 20 | 20,00 | 400,00 |
| 05/03 | 30 | 30,00 | 900,00 |  |  |  | 50 | 26,00 | 1300,00 |
| 11/03 | - |  |  | 10 | 26,00 | 260,00 | 40 | 26,00 | 1040,00 |
| 17/03 | - |  |  | 20 | 26,00 | 520,00 | 20 | 26,00 | 520,00 |
| 23/03 | 30 | 35,00 | 1050,00 |  |  | 0,00 | 50 | 31,40 | 1570,00 |
| 29/03 | - |  |  | 10 | 31,40 | 3140,00 | 40 | 31,40 | 1256,00 |

### **Primeiro a entrar, primeiro a sair (PEPS)**

Com base nesse critério, dá-se saída no custo da seguinte maneira: o primeiro que entra é o primeiro que sai (PEPS). À medida que ocorrem as vendas, vamos dando baixas no estoque a partir das primeiras compras, o que equivaleria ao raciocínio de que vendemos/compramos primeiro as primeiras unidades compradas/produzidas, ou seja, a primeira unidade a entrar no estoque é a primeira a ser utilizada no processo de produção o ou a ser vendida.

Dentro desse procedimento, o estoque é representado pelos mais recentes preços pagos apresentando, dessa forma, uma relação bastante significativa com o custo de reposição. Obviamente, com a adoção desse método, o efeito da flutuação dos preços sobre os resultados é significativo, as saídas são confrontadas com os custos mais antigos, sendo esta uma das principais razões pelas quais alguns contadores mostra-se contrários a esse método. Entretanto, não é objeto do o procedimento em si, e sim o conceito do resultado (lucro).

As vantagens do método são:

* Os itens usados são retirados do estoque e a baixa é dada nos controles de maneira lógica e sistemática;
* O resultado obtido espelha o custo real dos itens específicos usados nas saídas;
* O movimento estabelecido para os materiais, de forma contínua e ordenada, representa uma condição necessária para o perfeito controle dos materiais, especialmente quando estes estão sujeitos a deterioração, decomposição, mudança de qualidade, etc. Primeiro a entrar, primeiro a sair (PEPS).

Agora vejamos como registrar a movimentação físico financeira:

| DATAS | ENTRADAS | | | SAÍDAS | | | SALDOS | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Quantidade | Valores R$ | | Quantidade | Valores R$ | | Quantidade | Valores R$ | |
|  |  | Unitário | Total |  | Unitário | Total |  | Unitário | Total |
| Saldo Anterior | - | - | - | - | - | - | 20 | 20,00 |  |
| 05/03 | 30 | 30,00 | 900,00 |  |  |  | 20 |  |  |
|  |  |  |  |  |  |  | 30 |  |  |
|  |  |  |  |  |  |  | 50 |  |  |
| 11/03 | - |  |  | 10 | 20,00 | 200,00 | 10 |  |  |
|  |  |  |  |  |  |  | 30 |  |  |
|  |  |  |  |  |  |  | 40 |  |  |
| 17/03 | - |  |  | 10 | 20,00 | 200,00 | 20 |  |  |
|  |  |  |  | 10 | 30,00 | 300,00 |  |  |  |
|  |  |  |  | 20 |  | 600,00 |  |  |  |
| 23/03 | 30 | 35,00 | 1.050,00 | - | - | - | 20 |  |  |
|  |  |  |  |  |  |  | 30 |  |  |
|  |  |  |  |  |  |  | 50 |  |  |
| 29/03 | - | - | - | 10 | 30,00 | 300,00 | 10 |  |  |
|  |  |  |  |  |  |  | 30 |  |  |
|  |  |  |  |  |  |  | 40 |  |  |

Ponto de Atenção: No relatório de FFF não são apresentando o valor de Total Saldo a cada movimentação, porque o custo será especifico por movimentação.

### **Último a entrar, primeiro a sair (UEPS)**

O UEPS (último a entrar, primeiro a sair) é um método de avaliar estoque muito discutido. O custo do estoque é determinado como se as unidades mais recentes adicionadas ao estoque (últimas a entrar) fossem as primeiras unidades vendidas (saídas) (primeiro a sair). Supõe-se, portanto, que o estoque final consiste nas unidades mais antigas e é avaliado ao custo destas unidades. Segue-se que, de acordo com o método UEPS, o custo dos itens vendidos/saídos tende a refletir o custo dos itens mais recentemente comprados (comprados ou produzidos, e assim, os preços mais recentes). Também permite reduzir os lucros líquidos relatados por uma importância que, se colocada à disposição dos acionistas, poderia prejudicar as operações futuras da empresa.

O método UEPS não alcança a realização do objetivo básico, porque são debitados contra a receita os custos mais recentes de aquisições e não o custo total de reposição de todos os itens utilizados.

As vantagens e desvantagens do método UEPS são:

* É uma forma de se custear os itens consumidos de maneira sistemática e realista;
* Nas indústrias sujeitas a flutuações de preços, o método tende a minimizar os lucros das operações;
* Em períodos de alta de preços, os preços maiores das compras mais recentes são apropriados mais rapidamente às produções reduzindo o lucro;
* O argumento mais generalizado em favor do UEPS é o de que procura determinar se a empresa apurou, ou não, adequadamente, deus custos correntes em face da sua receita corrente. De acordo com o UEPS, o estoque é avaliado em termos do nível de preço da época, em que o UEPS foi introduzido.

Aplicando-se o método UEPS aos dados do exemplo anterior, os seguintes resultados são obtidos:

| DATAS | ENTRADAS | | | SAÍDAS | | | SALDOS | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Quantidade | Valores R$ | | Quantidade | Valores R$ | | Quantidade | Valores R$ | |
|  |  | Unitário | Total |  | Unitário | Total |  | Unitário | Total |
| Saldo Anterior | - | - | - | - | - | - | 20 | 20,00 |  |
| 05/03 | 30 | 30,00 | 900,00 |  |  |  | 20 |  |  |
|  |  |  |  |  |  |  | 30 |  |  |
|  |  |  |  |  |  |  | 50 |  |  |
| 11/03 | - |  |  | 10 | 30,00 | 300,00 | 20 |  |  |
|  |  |  |  |  |  |  | 20 |  |  |
|  |  |  |  |  |  |  | 40 |  |  |
| 17/03 | - |  |  | 20 | 30,00 | 600,00 | 20 |  |  |
| 23/03 | 30 | 35,00 | 1.050,00 | - | - | - | 20 |  |  |
|  |  |  |  |  |  |  | 30 |  |  |
|  |  |  |  |  |  |  | 50 |  |  |
| 29/03 | - | - | - | 10 | 35,00 | 350,00 | 20 |  |  |
|  |  |  |  |  |  |  | 20 |  |  |
|  |  |  |  |  |  |  | 40 |  |  |

Ponto de Atenção: No relatório de FFF não são apresentando o valor de Total Saldo a cada movimentação, porque o custo será especifico por movimentação.

## **03.****TELA PARÂMETROS SISTEMA**

**Definições  de Estoque / Custos**

## 

## **04. TELA PRODUTO**

****Cadastro de Produto pasta Custos:****

## **05. TABELAS UTILIZADAS**

* TLOTEPEPSUEPS - Lotes PEPS/UEPS
* TITMLOTEPEPSUEPS - Item de movimento de Lotes PEPS/UEPS

]]>
