---
content_hash: 93fa138cfba5b5188c81164082328add8825b8511232bdf898114c316e63c9b0
fetched_at: '2026-06-29T00:09:13.337894+00:00'
page_id: '419547299'
product: rm
source: tdn-rm
title: Detalhamento dos valores da parcela do contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Detalhamento+dos+valores+da+parcela+do+contrato
version: 36
---

## **Visão Geral**

O objetivo desse serviço é mostrar o detalhamento dos valores da parcela do contrato com lançamentos financeiros gerado, através de uma lista de parcelas a terem os valores calculados conforme a data de pagamento.

Esse serviço retorna o detalhamento dos valores das parcelas de contrato com os seus valores financeiros para entender os valores que serão pagas na mensalidade.

OBSERVAÇÃO

O detalhamento dos valores da parcela será somente para as parcelas de contrato com lançamentos financeiros gerados.

Dúvidas para exposição de webservices podem ser esclarecidas através do link:

Dúvidas para configuração do host podem ser esclarecidas através do link**:   
[Ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

### Método RetornaDetalhamentoCalculoParcelas

O método **RetornaDetalhamentoCalculoParcelas** presente no webservice do TOTVS Educacional (**wsEdu**) retorna o detalhamento dos valores da parcelas de contrato com lançamentos financeiros gerados baseados em turmas disciplinas, bolsas condicionais, bolsa incondicionais, desconto por antecipação ou conta corrente. Como informações obrigatórias no XML, devem ser informados o contexto do TOTVS Educacional a ser considerado, lista de parcelas e data de pagamento para cálculo.

Segue abaixo uma descrição dos parâmetros a serem passados para o detalhamento dos valores de parcelas:

* **contextoSrv**: Contexto do TOTVS Educacional a ser executada o detalhamento. Possui o seguinte formato: [coligada],[código da filial],[Código do nível de ensino].  
    Exemplo: 1,1,1 (coligada = 1, código da filial = 1, código do nível de ensino = 1)
* **strListaIdParcela**: Lista contendo os identificadores de parcelas a terem seus valores detalhados com os valores separados por vírgula. Caso uma parcela da lista de parcelas não exista na base de dados, os dados referentes ao identificador informado não serão retornados.  
    Exemplo: <IdParcela1>,<IdParcela2>
* **dataPagamento**: Data de pagamento no formato (yyyy-mm-dd) para ser considerada no cálculo do detalhamento dos valores.  
    Exemplo: 2018-10-05

**Exemplo de parâmetros do detalhamento preenchidos (utilizando o aplicativo SOAPUI)**:

Na imagem acima observe que:

* A tag "**contextoSrv**" contém a informação 1,1,1 que significa:  
  + Código da coligada igual a 1
  + Código da filial igual a 1
  + Código do nível de ensino (codtipocurso) igual a 1
* A tag "**strListaIdParcela**" contém a informação:  
  + Parcelas a serem processadas com idparcela1 = 19901, idparcela2 = 19902.
* A tag "**dataPagamento**" contém a data de pagamento a ser utilizada para cálculo do detalhamento dos valores:  
  + Data de pagamento: 2018-10-05

VALIDAÇÕES FEITAS PELO SERVIÇO:

1. **Sistema não encontra as parcelas informadas**: Caso não sejam encontradas parcelas com os identificadores de parcelas informados para o serviço será exibida a seguinte mensagem "**Não foram encontradas parcelas para exibição do detalhamento",**conforme abaixo
2. **Contexto informado inválido ou incompleto:**Caso não seja informado contexto no formado correto, será exibida a seguinte mensagem "Contexto informado inválido. Favor informar, [Código da coligada], [Código da Filial], [Código do Nível de Ensino]", conforme abaixo:
3. **Não foram informados parcelas:**Caso não seja informado o ID da parcela, será exibida a seguinte mensagem "Lista de parcelas deve ser informada", conforme abaixo:
4. **Data informada no formado incorreto:**Caso não seja informado data no formado correto, será exibida a seguinte mensagem "Data de pagamento inválida. Favor informar a data de pagamento no formato   
   (Ano-Mes-Dia). Ex.: 2018-10-01 (1º de Outubro de 2018)", conforme abaixo:
5. **Sistema só encontra uma parcela no contexto informado:**Caso informe duas parcelas que estão em contextos diferente, ou, duas parcelas que esteja no mesmo contexto e uma delas não esteja gerada, será exibida a seguinte mensagem "Não foram encontradas informações referentes à parcela no contexto informado", conforme abaixo:

### XML de retorno do serviço de detalhamento:

Conforme foi dito acima, o serviço **RetornaDetalhamentoCalculoParcelas** de wsEdu retorna o detalhamento dos valores das parcelas de contrato com lançamento financeiro gerados.

Após execução do serviço, o sistema retorna o seguinte XML:

xmlXML de retornotrue



1
19901
1
1
C
2630
D003
6,000
476,720
2860,320
6
476,720

N

1
19901
2
1
C
2632
D004
2,000
476,720
953,440
6
158,907

N

1
19901
3
1
C
2642
D001
4,000
500,000
2000,000
6
333,333

N

1
19901
4
1
C
2643
D005
2,000
476,720
953,440
6
158,907

N

1
19901
5
1
C
2644
D006
2,000
500,000
1000,000
6
166,667

N

1
19901
6
1
C
2645
D002
2,000
476,720
953,440
6
158,907

N

1
19901
7
1
C
2646
D007
3,000
476,720
1430,160
6
238,359

N

1
19901
0,000
0,000
121,476
0,000
0,000
1691,800


1
19901
37
N


Desconto Incondicional

P
10,000
121,476
121,476


1
19901
35
N


Desconto Condicional

P
5,000
0,000
0,000

1
19901
5
R
C00520
1
FIES

P
15,000
0,000
0,000


1
19901
21069
1
C01866
LFS Papai Noel
1691,800
1193,286
0,000
0,000
0,000
0,000
0,000
0,000
100,000
0,000
0,000
0,000
0,000
0
N
1
1193,286
289,587
121,476

1
19901
21070
1
C00520
CAIXA ECONÔMICA FEDERAL
225,652
225,652
0
0
0
0
0
0
0
0
0
0
0
0
S
0
0
0
289,587
121,476


45
Valor integracao 1
F
2

46
Valor integracao Oficial
F
2


1
19901
21069
4
10
Até dia 5
1093,286
05/07/2018 00:00:00
187,451

1
19901
21069
4
11
Até dia 10
1166,237
10/07/2018 00:00:00
97,109

1
19901
21069
4
12
Até dia 20
1204,899
20/07/2018 00:00:00
49,231

1
19901
21069
4
13
Até dia 30
1244,652
30/07/2018 00:00:00
0,000
]]>

Abaixo segue uma explicação de cada tag do XML de retorno do serviço.

DETALHAMENTO

* <DETALHAMENTO>Contém a marcação inicial e a marcação final do XML de retorno do serviço de retorno detalhamento cálculo da parcela.</DETALHAMENTO>
PARCELA

* <PARCELA>Contém a marcação inicial e a marcação final para os valores para cada parcela</PARCELA>
DISCIPLINA

* <DISCIPLINAS>Contém a marcação inicial e a marcação final das disciplinas presente na matrícula do aluno</DISCIPLINAS>

  + <DISCIPLINA>Contém os dados de cada disciplina presente na matrícula do aluno</DISCIPLINA>

    - <CODCOLIGADA>Código da coligada</CODCOLIGADA>
    - <IDPARCELA>Identificador da parcela</IDPARCELA>
    - <SEQUENCIAL>Identificador único para cada parcela</SEQUENCIAL>
    - <ORIGEM>Origem do item de cálculo</ORIGEM>
    - <TIPOITEM>Tipo do item de cálculo</TIPOITEM>
    - <IDTURMADISC>Identificador da turma disciplina</IDTURMADISC>
    - <CODDISC>Código da disciplina</CODDISC>
    - <NUMCREDITOCOB>Número de crédito de cobrados</NUMCREDITOCOB>
    - <VALORCREDITO>Valor crédito</VALORCREDITO>
    - <VALORTOTALCONTRATO>Valor total da disciplina calculado para o contrato</VALORTOTALCONTRATO>
    - <QTDPARCELASCONSIDERADA>Quantidade de parcelas consideradas</QTDPARCELASCONSIDERADA>
    - <VALORTOTALPORPARCELA>Valor total da disciplina para a parcela</VALORTOTALPORPARCELA>
    - <IDFAIXACREDITO>Identificador da Faixa de Crédito</IDFAIXACREDITO>
    - <INCONSISTENTE>Inconsistente</INCONSISTENTE>

      Informação

      Para as tag's das disciplinas são os campos usados no .
VALORESEDUCACIONAIS

* <VALORESEDUCACIONAIS>Contém a marcação inicial e a marcação final do XML para os dados dos valores educacionais para cada parcela</VALORESEDUCACIONAIS>
  + <CODCOLIGADA>Código da coligada</CODCOLIGADA>
  + <IDPARCELA>Identificador da parcela</IDPARCELA>
  + <VALORDESCONTOPARCELA>Valor do desconto da parcela</VALORDESCONTOPARCELA>
  + <VALORBOLSASCONDICIONAIS>Valor das bolsas condicionais da parcela</VALORBOLSASCONDICIONAIS>
  + <VALORBOLSASINCONDICIONAIS>Valor das bolsas incondicionais da parcela</VALORBOLSASINCONDICIONAIS>
  + <VALORCREDITOCONTACORRENTE>Valor do crédito da conta corrente para pagamento a maior da parcela</VALORCREDITOCONTACORRENTE>
  + <VALORDEBITOCONTACORRENTE>Valor do débito da conta corrente para pagamento a menor da parcela</VALORDEBITOCONTACORRENTE>
  + <VALORPARCELA>Valor total da parcela</VALORPARCELA>
BOLSASCONDICIONAIS

* <BOLSASCONDICIONAIS>Contém a marcação inicial e a marcação final do XML para os dados das bolsas condicionais para cada parcela</BOLSASCONDICIONAIS>

  + <BOLSA>Contém os dados de cada bolsa para cada parcela<BOLSA>

    - <CODCOLIGADA>Código da coligada</CODCOLIGADA>
    - <IDPARCELA>Identificador da parcela</IDPARCELA>
    - <CODBOLSA>Código da bolsa</CODBOLSA>
    - <TIPOSAC>Tipo sacado da bolsa (N - Nenhum, A - Aluno, R - Outro Sacado)</TIPOSAC>
    - <CODCFO>Código do Cliente / Fornecedor para o campo outro sacado</CODCFO>
    - <CODCOLCFO>Coligada do Cliente / Fornecedor para o campo outro sacado</CODCOLCFO>
    - <NOME>Nome da bolsa</NOME>
    - <ORDEMPERDA>Ordem de perda da bolsa</ORDEMPERDA>
    - <TIPODESC>Tipo de Desconto (P - Percentual, V- Valor)</TIPODESC>
    - <DESCONTO>Valor do desconto conforme o campo tipo de desconto</DESCONTO>
    - <VALORCALCULADO>Valor calculado para a bolsa</VALORCALCULADO>
    - <VALORBAIXA>Valor baixado da bolsa</VALORBAIXA>

      Informação

      As mesmas informações citadas acima se aplicam a estrutura BOLSASINCONDICIONAIS
VALORESFINANCEIROS

* <VALORESFINANCEIROS>Contém a marcação inicial e a marcação final do XML para os dados do lançamento financeiro para cada parcela</VALORESFINANCEIROS>  
  + <LANCAMENTO>Contém os dados de cada lançamento financeiro para cada parcela<LANCAMENTO>
  + <CODCOLIGADA>Código da coligada</CODCOLIGADA>
  + <IDPARCELA>Identificador da parcela</IDPARCELA>
  + <IDLAN>Identificador do lançamento financeiro</IDLAN>
  + <CODCOLCFO>Código da coligada do cliente</CODCOLCFO>
  + <CODCFO>Código do cliente</CODCFO>
  + <NOMERESPONSAVEL>Nome do responsável financeiro</NOMERESPONSAVEL>
  + <VALORORIGINAL>Valor Original</VALORORIGINAL>
  + <VALORLIQUIDO>Valor líquido</VALORLIQUIDO>
  + <VALORJUROS>Valor do juros</VALORJUROS>
  + <VALORMULTA>Valor da multa</VALORMULTA>
  + <VALORDESCONTO>Valor do desconto</VALORDESCONTO>
  + <VALOROP1>Valor opcional 1</VALOROP1>
  + <VALOROP2>Valor opcional 2</VALOROP2>
  + <VALOROP3>Valor opcional 3</VALOROP3>
  + <VALOROP4>Valor opcional 4</VALOROP4>
  + <VALOROP5>Valor opcional 5</VALOROP5>
  + <VALOROP6>Valor opcional 6</VALOROP6>
  + <VALOROP7>Valor opcional 7</VALOROP7>
  + <VALOROP8>Valor opcional 8</VALOROP8>
  + <VALORDESCANTECIPACAO>Valor do desconto por antecipação</VALORDESCANTECIPACAO>

    Valores de Integração

    Se o lançamento financeiro tiver valores de integração, os mesmos serão apresentados na tag <VALORINTEGRACAO + Identificador do valor integração>.

    Exemplo: No lançamento financeiro tem o valor de integração 11 - Pagamento a menor. Desta forma, a tag deste valor de integração ficará <VALORINTEGRACAO11>99,99</VALORINTEGRACAO11>.
  + <LANBOLSACREDITO>Identifica se o lançamento é de bolsa de crédito (N - Não, S - Sim)</LANBOLSACREDITO>
  + <STATUSLAN>Status do lançamento financeiro (Aberto = 0, Baixado = 1, Cancelado = 2, Baixado por acordo = 3, Baixado parcialmente = 4 )</STATUSLAN>
  + <VALORBAIXADO>Valor baixado (preenchido quando o lançamento estiver baixado)</VALORBAIXADO>
  + <VALORDEVOLUCAO>Valor devolução de bolsa retroativa</VALORDEVOLUCAO>
DESCONTOSPORANTECIPACAO

* <DESCONTOSPORANTECIPACAO>Contém a marcação inicial e a marcação final do XML para os dados dos desconto por antecipação para cada parcela</DESCONTOSPORANTECIPACAO>

  + <DESCONTOPORANTECIPACAO>Contém os dados de cada desconto por antecipação para cada parcela<\DESCONTOPORANTECIPACAO>

    - <CODCOLIGADA>Código da coligada</CODCOLIGADA>
    - <IDPARCELA>Identificador da parcela</IDPARCELA>
    - <IDLAN>Identificador do lançamento financeiro</IDLAN>
    - <IDAGRUPADESCPONTUAL>Identificador do agrupamento do desconto por antecipação</IDAGRUPADESCPONTUAL>
    - <IDDESCONTO>Ientificador do item do desconto por antecipação</IDDESCONTO>
    - <DESCRICAO>Nome do item do desconto por antecipação</DESCRICAO>
    - <VLRPGTOPORDESCPONTUAL>Valor a ser pago para esse item de desconto (vencimento por antecipação)</VLRPGTOPORDESCPONTUAL>
    - <DTDESCPONTUAL>Data limite calculada para o item de desconto com base no dia informado no formato (dd/mm/yyyy)</DTDESCPONTUAL>
    - <VALORDESCPONTUAL>Valor do desconto calculado para o item de desconto</VALORDESCPONTUAL>
CONFIGVALORINTEGRACAO

* + <CONFIGVALORINTEGRACAO>Contém a marcação inicial e a marcação final do XML para os dados dos valores de integração financeiros. </CONFIGVALORINTEGRACAO>
    - <VALORINTEGRACAO>Contém os dados de cada valor de integração para cada lançamento da parcela</VALORINTEGRACAO>
    - <IDCAMPO>Contém o ID do campo do valor integração parametrizado</IDCAMPO>
    - <DESCRICAO>Contém a descrição do valor de integração parametrizado </DESCRICAO>
    - <CODSISTEMA>Contém o código do sistema que é dono do valor de integração parametrização</CODSISTEMA>
    - <ACAO>Contém a constante da Ação informada no valor de integração (0 - Nada, 1 - Soma, 2 - Desconta)</ACAO>

OBSERVAÇÕES

O número de casas decimais para os valores respeitará o parâmetro do TOTVS Gestão Financeira (Contas a Receber → Manutenção de Lançamentos → Opções Gerais → Nº Casas Decimais)
