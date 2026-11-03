---
content_hash: 6f619b1a10e5f4a88c8702b5c1f3295f4c4b646003e8b28aaa2a5d7495c1e25d
fetched_at: '2026-06-29T00:05:52.978696+00:00'
page_id: '1062884953'
product: rm
source: tdn-rm
title: FOPTRP0034 - Pedido de Demissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1062884953
version: 1
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. VERSÕES**

**A partir dos patches:**

+ 12.1.2606 e Superiores
+ [DT - Smart View - Pedido de Demissão](https://tdn.totvs.com/pages/viewpage.action?pageId=1062884795)

## **02. V****ISÃO GERAL**

Utilizando o objeto de negócio [Ficha de Registro do Funcionário](https://tdn.totvs.com/pages/viewpage.action?pageId=1046819891), o relatório Pedido de Demissão irá formalizar o pedido de demissão pelo funcionário, contendo os seus dados, a data do pedido de demissão e a opção por cumprir o aviso prévio ou não.

#### **Regras de Filtro (Importante)**

Para garantir a performance e a segurança dos dados, o objeto possui uma lógica de filtros obrigatórios:

**Importante - Regras de Preenchimento:** O objeto exige que todos os parâmetros declarados recebam um valor para processar a requisição. Para alternar entre os tipos de filtro, utilize a lógica abaixo:

* **Filtrar por Matrícula:**Preencher com a chapa do funcionário ou -1 para todos.
* **Filtrar por CPF:** Informar o número do CPF  do funcionário ou -1 para todos.
* **Código Seção:** Selecionar uma seção ou as seções desejadas.
* **Código Situação:**Selecionar a situação do funcionário que deseja que o relatório retorne.
* **Filial :**Selecionar a filial
* **Tipo Funcionário:** Selecionar o tipo de funcionário que deseja que o relatório retorne.
* **Data Admissão:** Este campo retorna PFUNC.DATAADMISSAO >= a data informada.
* **Utiliza aviso prévio:** Selecionar Verdadeiro ou Falso para informar se vai cumprir o aviso prévio ou não.
* **Imprimir parâmetros:** Ao selecionar essa opção, os valores dos parâmetros serão impressos antes da primeira página do relatório

|  |  |  |
| --- | --- | --- |
| Matrícula | PFUNC.CODFUNCAO | Filtra pela chapa do funcionário. |
| CPF | PPESSOA.CPF | Filtra pelo CPF. |
| Seção | PFUNC.SECAO | Filtra o código da seção de lotação do funcionário. |
| Código  Situação | PFUNC.CODSITUACAO | Filtra pelo código de situação do funcionário. |
| Filial | PFUNC.FILIAL | Filtra pela Filial. |
| Tipo Funcionário | PFUNC.CODTIPO | Filtra pelo tipo funcionário. |
| Data Admissão | PFUNC.DATAADMISSAO | Filtra utilizando a PFUNC.DATAADMISSAO >= a data informada. |
| Utiliza aviso prévio | - | Informa a opção por cumprir o aviso prévio (Verdadeiro) ou não (Falso) |
| Imprimir parâmetros | - | Os valores dos parâmetros serão impressos antes da primeira página do relatório |

A visualização do relatório será baseada no filtro inserido pelo usuário na visão do Smart View. 

Nesse relatório temos os seguintes campos nos objetos de negócio disponíveis:

| Campo do Relatório | Campo da Tabela | Complemento |
| --- | --- | --- |
| DADOS EMPRESARIAIS | | |
| --- | --- | --- |
| Nome da empresa | GCOLIGADA.NOMEFANTASIA | Lista o nome da empresa |
| Nome | PPESSOA.NOME | Lista o nome do funcionário |
| RG | PPESSOA.CARTIDENTIDADE | Lista o número cédula de identidade do funcionário |
| CTPS | PPESSOA.CARTEIRATRAB | Lista o número da carteira de trabalho do funcionário |
| SERIE | PPESSOA.SERIECARTTRAB | Lista a série da carteira de trabalho do funcionário |

## **03.  EXEMPLO DE UTILIZAÇÃO**

1)Acesse RH | Folha de Pagamento | Gestão | Smart View, e realize a importação do relatório.

2) Acesse RH | Folha de Pagamento | Gestão | Smart View, para geração do relatório.

Escolha o relatório FOPTRP0034 e vá em 'Mais Ações', selecione a opção Executar no Smart View, configure os filtros necessários e ao final clique em 'Enviar' para iniciar o processo de geração do relatório. 

3) Filtros:

4) Relatório emitido

**DICAS:**

* É necessário que todos os campos do filtro sejam preenchidos.  Para adicionar um filtro, clique no ícone correspondente.
* Para gerar todos os resultados, configure o filtro com a opção "-1" nos parâmetros em que esta opção estiver entre parênteses. Caso contrário, clique na lupa, onde abrirá um janela pop-up com as opções disponíveis para seleção. Após selecionadas, ao clicar no botão Selecionar, a janela pop-up se fechará.
* A impressão da logo só ocorrerá caso a coligada atual tenha a logo disponível.
* Os ícones  do relatório oferecem diversas opções, como pesquisa, impressão, salvar, entre outros serviços disponíveis.

## **04. TABELAS UTILIZADAS**

* GCOLIGADA
* PFUNC
* PPESSOA
