---
content_hash: f44e6308f3f0f2560d3cdb08d0cbf20657bbcd122423ad0736be05c9730e38f4
fetched_at: '2026-06-29T00:10:36.356282+00:00'
page_id: '532035637'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-6618 DT Funções de Fórmula para o Processamento do Valor Auxiliar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=532035637
version: 41
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Educacional |
| Função: | Fórmula para o Valor Auxiliar |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : |  |

## **02. SITUAÇÃO/REQUISITO**

Em função da evolução do TOTVS Educacional para permitir a criação de [valor auxiliar](https://tdn.totvs.com/display/LRM/DEDUINTEGRACOES-6614+DT+Valor+Auxiliar) para "Bolsa" e "Desconto por Antecipação" é necessário que seja disponibilizado novas funções de fórmula que deverão ser executadas sobre o contexto das tabelas **SBOLSALAN** e **SLANDESCPONTUAL**.

## **03. SOLUÇÃO**

Disponibilizamos novas funções de fórmulas que tem como objetivo exclusivo de auxiliar na implementação de novas fórmulas que serão utilizadas no processamento do valor auxiliar para bolsa ou desconto por antecipação.

Funções para valor auxiliar aplicados em “Bolsa” ou “Desconto por Antecipação”

As funções de fórmula abaixo poderão ser utilizadas em ambos contexto, seja para processamento do valor auxiliar de bolsa ou desconto por antecipação.

Todas as funções abaixo terão como contexto a informação de processamento da tabela **SBOLSALAN**(para bolsas) ou **SLANDESPONTUAL** (para descontos por antecipação) processada para a parcela do contrato do aluno.

| Nome | Descrição | Parâmetros | Exemplo |
| --- | --- | --- | --- |
| VAUXTABCONTRATO | Tem como objetivo retornar o conteúdo de um determinado campo do contrato do aluno (tabela: SCONTRATO). | * **Nome do campo**. * **Tipo**: Tipo do valor do campo informado.   + **"V"**: Valor   + **"I"**: Inteiro   + **"D"**: Data   + **"S"**: Texto | VAUXTABCONTRATO('IDHABILITACAOFILIAL','I') |
| VAUXTABPARCELA | Tem como objetivo retornar o conteúdo de um determinado campo da parcela do contrato do aluno (tabela: SPARCELA). | * **Nome do campo**. * **Tipo**: Tipo do valor do campo informado.   + **"V"**: Valor   + **"I"**: Inteiro   + **"D"**: Data   + **"S"**: Texto | VAUXTABPARCELA('DTVENCIMENTO','D') |
| VAUXTABFLAN | Tem como objetivo retornar o conteúdo de um determinado campo do lançamento financeiro vinculado a parcela do contrato do aluno (tabela: FLAN). | * **Nome do campo**. * **Tipo**: Tipo do valor do campo informado.   + **"V"**: Valor   + **"I"**: Inteiro   + **"D"**: Data   + **"S"**: Texto | VAUXTABFLAN('VALORORIGINAL','V') |
| VAUXVLRINTEGRACAOLAN | Tem como objetivo retornar o valor de integração processado para o lançamento financeiro vinculado a parcela do contrato do aluno. | * **Identificador do campo do valor de integração.** | VAUXVLRINTEGRACAOLAN(45)  45 corresponde ao id. do campo do valor de integração cadastrado no TOTVS Gestão Financeira. |
| VAUXVALORBOLSA | Tem como objetivo retornar o valor processado para a bolsa.  Importante:  Quando existir desconto por antecipação processado para o contrato o sistema executará a fórmula vinculada ao valor auxiliar para cada vencimento do desconto por antecipação, neste caso, o valor da bolsa retornado por esta função será o valor da bolsa processado para o dia do vencimento do desconto por antecipação. | * **Código da Bolas** | Exemplo 1:  VAUXVALORBOLSA('45')    Exemplo 2:  VAUXVALORBOLSA('')  Se o “Código da bolsa” for passado vazio (conforme o exemplo acima), será considerado a bolsa do contexto de execução da fórmula (Registro da SBOLSALAN). |
| VALORBASECALCULOBOLSA | Tem como objetivo retornar o valor base de cálculo utilizado para calcular a bolsa.  Importante:  Quando existir desconto por antecipação processado para o contrato o sistema executará a fórmula vinculada ao valor auxiliar para cada vencimento do desconto por antecipação, neste caso, o valor base de cálculo retornado por esta função será o valor processado para o dia do vencimento do desconto por antecipação. |  | VALORBASECALCULOBOLSA() |

Funções especificas para valor auxiliar aplicados na “Bolsa”

As funções de fórmula abaixo poderão ser utilizadas especificamente para processar valores auxiliares aplicados em bolsa.

O contexto  para processamento da fórmula corresponde aos dados gravados na tabela **SBOLSALAN**que serão gerados durante a criação do lançamento financeiro processado  para a parcela do contrato do aluno.

Exemplo

Se a parcela do contrato do aluno possuir a "**BOLSA A**" e "**BOLSA B**" internamente ao gerar o lançamento financeiro o sistema vai incluir dois registros na tabela **SBOLSALAN** e consequentemente para cada registo será processada a fórmula vinculada ao valor auxiliar.

| Nome | Descrição | Parâmetros | Exemplo |
| --- | --- | --- | --- |
| VAUXTABBOLSALAN | Tem como objetivo retornar o conteúdo de um determinado campo da tabela SBOLSALAN | * **Nome do Campo** * **Tipo**: Tipo do valor do campo informado.   + **"V"**: Valor   + **"I"**: Inteiro   + **"D"**: Data   + **"S"**: Texto | VAUXTABBOLSALAN('VALOR', 'V') |
| VAUXTABBOLSA | Tem como objetivo retorna o conteúdo de um determinado campo do cadastro da bolsa (tabela: SBOLSA) | * **Nome do campo**: * **Tipo**: Tipo do valor do campo informado.   + **"V"**: Valor   + **"I"**: Inteiro   + **"D"**: Data   + **"S"**: Texto | VAUXTABBOLSA('CODBOLSA', 'S') |
| VAUXTABBOLSACOMPL | Tem como objetivo retornar o conteúdo de um determinado campo complementar do cadastro da bolsa (tabela:SBOLSACOMPL) | * **Nome do campo complementar**. * **Tipo**: Tipo do valor do campo informado.   + **"V"**: Valor   + **"I"**: Inteiro   + **"D"**: Data   + **"S"**: Texto | VAUXTABBOLSACOMPL('TIPOX', 'S') |
| VAUXDESCPARCELABOLSALAN | Tem como objetivo retornar o valor de desconto da parcela vinculada a bolsa processada.  ***Obs.******.***: Caso tenhamos uma parcela com mais de um responsável financeiro será retornado o desconto aplicado ao lançamento do contexto corrente da bolsa processada. | * **Tipo valor**: Tipo do valor de retorno *(**V**=Valor/ **P**=Percentual)* | VAUXDESCPARCELABOLSALAN('V') |
| VAUXVALORAUXBOLSA | Tem como objetivo retornar o conteúdo do valor auxiliar já processado para a bolsa .  Se o código da bolsa não for informado será considerado a bolsa do contexto corrente da **SBOLSALAN**. | * **Código do valor auxiliar** * **Código da bolsa** | VAUXVALORAUXBOLSA('CODAUX001', 'BOLSAX') |
| VAUXVALORAUXBOLSA Quando utilizar esta função de fórmula recomendamos que ao cadastrar o valor auxiliar o campo "Ordem de processamento" seja preenchido estabelecendo um critério de ordem de processamento.  Exemplo:  Valor auxiliar: VAUX001 - Ordem 1  Valor auxiliar: VAUX002 - Ordem 2  Desta forma posso na fórmula do valor auxiliar "VAUX002" utilizar a função VAUXVALORAUXBOLSA('VAUX001', 'BOLSAXPTO') , pois o valor auxiliar "VAUX001" já vai ter processado. | | | |
| VAUXTOTALBOLSASPORCAMPOCOMPL | Tem como objetivo retornar o somatório dos valores das bolsas conforme conteúdo do campo complementar informado. | * **Nome do campo complementar da bolsa**; * **Conteúdo do campo complementar que se deseja filtrar;** * **Tipo valor**: Tipo de valor de retorno  *(**V** =Valor/ **P**= Percentual)* | VAUXTOTALBOLSASPORCAMPOCOMPL('FIES', 'T', 'P') |
| VAUXTOTALBOLSASPORCAMPOCOMPL Exemplo:  Bolsa 1 | Campo Complementar: Classificação = A | Valor da Bolsa R$ 100,00  Bolsa 2 | Campo Complementar: Classificação = A | Valor da Bolsa R$ 100,00  Bolsa 3 | Campo Complementar: Classificação = B | Valor da Bolsa R$ 100,00    Baseado no exemplo acima poderíamos utilizar a função de fórmula assim: **VAUXTOTALBOLSASPORCAMPOCOMPL('Classificação', 'A','V')**  O resultado da execução será de R$ 200,00 | | | |

Funções especificas para valor auxiliar aplicados no “Desconto por antecipação”

As funções de fórmula abaixo poderão ser utilizadas especificamente para processar valores auxiliares do aplicados n desconto por antecipação.

O contexto  para processamento da fórmula corresponde aos dados gravados na tabela **SLANDESCPONTUAL**que serão gerados durante a criação do lançamento financeiro processado  para a parcela do contrato do aluno.

Exemplo

Considerando que o contrato do aluno possui o desconto por antecipação abaixo:

1º Desconto por antecipação - Vencimento 05 - 10 %

2º Desconto por antecipação - Vencimento 10 - 7 %

3º Desconto por antecipação - Vencimento 20 - 5 %

4º Desconto por antecipação - Vencimento 30 - 2 %

Durante a geração de lançamento o sistema irá executar para cada linha do desconto apresentado acima ( cada vencimento ) a fórmula associada ao valor auxiliar.

Obs.. As informações dos desconto por antecipação processados para a parcela são gravadas na tabela **SLANDESCPONTUAL**.

| Nome | Descrição | Parâmetros | Exemplo |
| --- | --- | --- | --- |
| VAUXTABLANDESCPONTUAL | Tem como objetivo retornar uma informação do desconto por antecipação processados para a parcela do aluno (Tabela: SLANDESCPONTUAL). | * **Nome do Campo** * **Tipo**: Tipo do valor do campo informado.   + **"V"**: Valor   + **"I"**: Inteiro   + **"D"**: Data   + **"S"**: Texto | VAUXTABLANDESCPONTUAL('VALORDESCONTOCALCULADO', 'V') |
| VAUXDESCANTECIPACAOLANDESCPONTUAL | Tem como objetivo retornar o valor do desconto por antecipação processado. | * **Tipo**: Tipo de retorno do valor do desconto por antecipação. *(**V** =Valor/ **P**=Percentual)* * **Nº vencimento**: Número do vencimento que deseja recuperar a informação. ***Exemplo***:    1º Vencimento (Até o dia 5)   => Vencimento = 1 2º Vencimento (Até o dia 10) => Vencimento = 2 3º Vencimento (Até o dia 15) => Vencimento = 3 4º Vencimento (Até o dia 20) => Vencimento = 4   Se o nº do vencimento não for informado, por exemplo, VAUXDESCANTECIPACAOLANDESCPONTUAL('V', '') , será considerado o valor do desconto por antecipação que esta sendo processado para o contexto de execução da fórmula. | Exemplo 1:  Valor do desconto por antecipação aplicado no vencimento 3 (Até o dia 15)  VAUXDESCANTECIPACAOLANDESCPONTUAL('V', '3')    Exemplo 2:  Considerando que a fórmula está sendo executada para o 2º vencimento, e não foi informado na função de fórmula o dia do vencimento.  VAUXDESCANTECIPACAOLANDESCPONTUAL('V', '')  Para este exemplo será retornado o valor do desconto por antecipação aplicado no 2º vencimento. |
| VAUXVALORAUXDESCANTECIPACAO | Tem como objetivo retornar o conteúdo do valor auxiliar já processado para o desconto por antecipação conforme o número de vencimento informado.  Caso seja informado o número de vencimento com valor "0" (Zero) será retornado o valor do valor auxiliar do desconto por antecipação do contexto corrente.  ***Exemplo***:  1º Vencimento (Até o dia 5)   => Vencimento = 1 2º Vencimento (Até o dia 10) => Vencimento = 2 3º Vencimento (Até o dia 15) => Vencimento = 3 4º Vencimento (Até o dia 20) => Vencimento = 4 | * **Código do valor auxiliar.** * **Nº vencimento**: Número do vencimento que deseja recuperar a informação. | VAUXVALORAUXDESCANTECIPACAO('CODAUX005', 3) |
| VAUXVALORAUXDESCANTECIPACAO Exemplo:  Considerando que já temos os seguintes valores auxiliares processados para os vencimentos do desconto por antecipação:  1º Desconto por antecipação -  VAUX001 - R$ 50,00  2º Desconto por antecipação -  VAUX001 - R$ 25,00  3º Desconto por antecipação -  VAUX001 - R$ 15,00  4º Desconto por antecipação -  VAUX001 - R$ 5,00  Para recuperar o valor auxiliar do 3º vencimento utilizamos **VAUXVALORAUXDESCANTECIPACAO('VAUX001', 3)**, o resultado será R$ 15,00. | | | |

**Recomendamos priorizar a utilização das funções de fórmula que relatamos anteriormente ao invés de carregar as informações através de consulta SQL, pois as funções de fórmula utilizam mecanismo de cache que tem como objetivo melhorar a performance da execução.IMPORTANTE!**

div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
.aui-tabs.horizontal-tabs>.tabs-menu>.menu-item.active-tab a::after {
background: #FF9900; !important
}
.menu-item.active-tab {
border-bottom: none !important;
}
]]>
