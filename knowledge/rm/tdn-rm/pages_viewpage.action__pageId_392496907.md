---
content_hash: bc8deda849004348ea13a251ce23c8cf9d222708ec49ddbec9e863b1c69e7943
fetched_at: '2026-06-29T00:09:09.097839+00:00'
page_id: '392496907'
product: rm
source: tdn-rm
title: Simulação de parcelas de contratos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=392496907
version: 29
---

## Visão Geral

O objetivo desse serviço é simular valores de parcelas de contratos existentes, através de uma lista de parcelas a terem os valores simulados e uma lista de turmas disciplinas bem como em um determinado status de matrícula na disciplina.

Esse serviço possibilita ao usuário do mesmo simular os valores a serem pagos pelo aluno antes de efetuarem a matrícula nas disciplinas de determinadas turmas, ou seja, não é necessário ter matrícula nas disciplinas para que o cálculo das parcelas seja feito.

O cálculo dos valores de parcelas segue a mesma regra da simulação de parcelas de contratos, ao selecionar uma determinada parcela na visão de parcela e clicar no botão  para cálculo, o qual realiza a simulação dos valores de parcelas baseados no plano de pagamento informado, bem como suas turmas disciplinas e um status de matrícula a ser considerado.

OBSERVAÇÃO

A simulação de parcelas de contratos vinculados a uma matriz aplicada e contratos de matrícula livre (sem vínculo com matriz aplicada) poderá retornar valores diferentes para uma mesma turma disciplina com o parâmetro "Usar valor do crédito financeiro da matriz curricular do aluno", isto porque, se a simulação estiver sendo feita para a parcela do contrato com vínculo à matriz aplicada, o sistema buscará os valores de créditos da disciplina da matriz curricular do aluno e, no segundo caso (contrato sem vínculo à matriz aplicada), o sistema poderá buscar o valor de créditos da matriz curricular da turma disciplina (se a mesma estiver vinculada a uma matriz aplicada) ou da turma disciplina (caso seja uma turma livre - sem vínculo a uma matriz aplicada).

Dúvidas para exposição de webservices podem ser esclarecidas através do link: **Como Expor os Web Services do RM através do Host**

Dúvidas para configuração do host podem ser esclarecidas através do link**:   
[Ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

### Método SimularValoresContratoTurmaDisc

O método **SimularValoresContratoTurmaDisc** presente no webservice do TOTVS Educacional (**wsEdu**) realiza a simulação dos valores de parcelas de contratos baseados em turmas disciplinas e um status de matrícula a ser considerado. Como informações obrigatórias no XML, devem ser informados o contexto do TOTVS Educacional a ser considerado, lista de parcelas, lista de turmas disciplinas e código do status de matrícula.

Segue abaixo uma descrição dos parâmetros a serem passados para a simulação de valores de parcelas:

* **contextoSrv**: Contexto do TOTVS Educacional a ser executada a simulação. Possui o seguinte formato: [coligada],[código da filial],[Código do nível de ensino].  
    Exemplo: 1,1,1 (coligada = 1, código da filial = 1, código do nível de ensino = 1)
* **strListaIdParcela**: Lista contendo os identificadores de parcelas a terem seus valores simulados com os valores separados por vírgula. Caso uma parcela da lista de parcelas não exista na base de dados, os dados referentes ao identificador informado não serão retornados.  
    Exemplo: <IdParcela1>,<IdParcela2>
* **strListaIdTurmaDisc**: Lista contendo os identificadores de turmas disciplinas a serem consideradas separadas por vírgula.  
    Exemplo: <IdTurmaDisc1>,<IdTurmaDisc2>
* **codStatusMatriculaDisc**: Código de status de matrícula na disciplina a ser considerado na simulação de valores.

**Exemplo de parâmetros de simulação preenchidos (utilizando o aplicativo SOAPUI)**:

Na imagem acima observe que:

* A tag "**contextoSrv**" contém a informação 1,1,1 que significa:  
  + Código da coligada igual a 1
  + Código da filial igual a 1
  + Código do nível de ensino (codtipocurso) igual a 1
* A tag "**strListaIdParcela**" contém a informação:  
  + Parcelas a serem processadas com idparcela1 = 19335 e idparcela2 = 19339

    Parcelas com valor fixo retornarão o seu próprio valor desconsiderando quaisquer valores de créditos ou informações contidas nas turmas disciplinas.
* A tag "**strListaIdTurmaDisc**" contém as informações 2575,2576,2580 que significa que:  
  + Serão consideradas as três turmas disciplinas com os respectivos "idTurmaDiscs" informados 2575, 2576 e 2580
* A tag "**codStatusMatriculaDisc**" contém a informação:
  + Código do status de matrícula na disciplina igual a 1.

    O status ou situação de matrícula na disciplina, no caso de simulação de parcelas calculadas por valor de crédito, deverão ter a opção de contar como créditos financeiros (cobrança por crédito) marcada. Vide imagem abaixo:

    Caso essa opção não esteja marcada, o serviço retornará os valores zerados para as parcelas.

Validações feitas pelo serviço:

1. **Sistema não encontra as parcelas informadas**: Caso não sejam encontradas parcelas com os identificadores de parcelas informados para o serviço será exibida a seguinte mensagem "**Não foram encontrados registros a serem simulados**" conforme abaixo
2. **Contexto do Educacional não informado**: Caso o contexto do TOTVS Educacional não tenha sido informado será exibida a mensagem "**Contexto do serviço deve ser informado.**" conforme abaixo:
3. **Lista de parcelas não informada**: Caso não seja informada a lista de parcelas, será exibida a mensagem "**Lista de parcelas deve ser informada."** conforme abaixo:
4. **Lista de Turmas Disciplinas não informada**: Será exibida a mensagem "**Lista de turmas disciplinas deve ser informada.**" conforme abaixo:
5. **Código da situação de matrícula nas disciplinas (status) não informado**: Será exibida a mensagem "**Status de matrícula na disciplina deve ser informado.**" conforme abaixo:
6. **Erros devido a inconsistências diversas**. Será exibida a mensagem conforme abaixo:

### XML de retorno do serviço de simulação:

Conforme foi dito acima, o serviço **SimularValoresContratoTurmaDisc** de wsEdu retorna os valores simulados conforme regra de simulação de valores de parcelas de contratos da visão de parcelas  sem dependência de quaisquer matrículas em disciplinas.

Abaixo seguem alguns dados utilizados em uma simulação utilizando o serviço:

(CONTRATO)

* Identificador da Matriz Aplicada (IdHabilitacaoFilial): 21
* Considera desconto por antecipação: Marcado
* Considerar o valor do desconto por antecipação no valor base para calcular o valor da(s) bolsa(s): Desmarcado
* Tipo da Bolsa: Somar Bolsas

(PARCELA)

* Identificador da Parcela: 19335
* Valor calculado por número de créditos: 600,00
* Número da Parcela: 1
* Cota: 1
* Código do Serviço: 1
* Nome do Serviço: Mensalidade
* Id. do período letivo: 104
* Código do período letivo: 2018/2
* Data de vencimento: 30/11/2018
* Valor automático: N (Parcela fixa)
* Data de competência: 11/2018

(BOLSA)

* Código da Bolsa: 37
* Nome: Desconto Incondicional
* Valor: 10%

(DESCONTO POR ANTECIPAÇÃO)

(ITEM DE DESCONTO 1)

* Identificador do Desconto: 62
* Descrição: PRIMEIRO VENCIMENTO
* Valor do desconto: 50%
* Dia Fixo: 5

(ITEM DE DESCONTO 2)

* Identificador do Desconto: 63
* Descrição: SEGUNDO VENCIMENTO
* Valor do desconto: 10%
* Dia Fixo: 10

(ITEM DE DESCONTO 3)

* Identificador do Desconto: 64
* Descrição: TERCEIRO VENCIMENTO
* Valor do desconto: 5%
* Dia Fixo: 20

Parâmetros passados para o serviço:

Após execução do serviço, o sistema retorna o seguinte XML:

xmlXML de retorno

1
19335
1
1
600,00
0,00
240,00
0
60,00
104
2018/2
1
Mensalidade
30/11/2018
N
01/11/2018
0


37
60,00


62
240,00
06/08/2018
300,00

63
480,00
10/08/2018
60,00

64
510,00
20/08/2018
30,00
]]>

Abaixo segue uma explicação de cada tag do XML de retorno do serviço.

* <SIMULACAO>Contém a marcação inicial e a marcação final do XML de retorno do serviço de simulação.</SIMULACAO>
* <PARCELA>Contém a marcação inicial e a marcação final para os dados simulados de cada parcela</PARCELA>

  + <CODCOLIGADA>Código da coligada</CODCOLIGADA>
  + <IDPARCELA>Identificador da parcela</IDPARCELA>
  + <PARCELA>Número da parcela</PARCELA>
  + <COTA>Número da cota</COTA>
  + <VALORORIGINAL>Valor original calculado para a parcela</VALORORIGINAL>
  + <VLRDESCONTO>Valor calculado do desconto informado na parcela</VLRDESCONTO>
  + <VLRLIQUIDO>Valor líquido a ser pago pelo aluno. (Considera o valor original subtraindo todos os descontos e bolsas calculadas)</VLRLIQUIDO>
  + <VLRBOLSACONDICIONAL>Valor total das bolsas condicionais</VLRBOLSACONDICIONAL>
  + <VLRBOLSAINCONDICIONAL>Valor total das bolsas incondicionais</VLRBOLSAINCONDICIONAL>
  + <IDPERLET>Id. do período letivo</IDPERLET>
  + <CODPERLET>Código do período letivo</CODPERLET>
  + <CODSERVICO>Código do Serviço</CODSERVICO>
  + <NOMESERVICO>Nome do Serviço</NOMESERVICO>
  + <DTVENCIMENTO>Data de vencimento</DTVENCIMENTO>
  + <VALORAUTOMATICO>Indica se a parcela é calculada por número de créditos (S: Calculada por número de créditos, N: Parcela Fixa)</VALORAUTOMATICO>
  + <DTCOMPETENCIA>Data de competência da parcela no formato (dd/mm/yyyy)</DTCOMPETENCIA>
  + <VLRCREDRETROATIVO>Valor de crédito retroativo da parcela</VLRCREDRETROATIVO>

    Essa tag **VLRCREDRETROATIVO** só estará visível se a base do cliente estiver parametrizada para utilizar o modelo de bolsa retroativa sem alteração de parcelas baixadas utilizando devolução para os créditos retroativos.
  + <BOLSAS>Contém a marcação inicial e a marcação final do XML para os dados de bolsas de cada parcela</BOLSAS>
    - <BOLSA>Contém a marcação inicial e a marcação final para cada bolsa da parcela</BOLSA>
      * <CODBOLSA>Código da bolsa</CODBOLSA>
      * <VALORBOLSA>Valor da bolsa</VALORBOLSA>

    Essa Tag **BOLSAS**exibirá os valores da bolsa referente ao primeiro vencimento do desconto por antecipação quando o desconto por calculado pelo sistema conforme as parametrizações realizadas
  + <DESCONTOPORANTECIPACAO>Contém a marcação inicial e a marcação final do XML para os dados de descontos por antecipação</DESCONTOPORANTECIPACAO>

    - <ITEMDESCONTO>Contém a marcação inicial e a marcação final para cada item de desconto por antecipação calculado para a parcela<ITEMDESCONTO>

      * <IDDESCONTO>Identificador do item de desconto</IDDESCONTO>
      * <VLRPGTOPORDESCPONTUAL>Valor a ser pago para esse item de desconto (vencimento por antecipação)</VLRPGTOPORDESCPONTUAL>
      * <DTDESCPONTUAL>Data limite calculada para o item de desconto com base no dia informado no formato (dd/mm/yyyy)</DTDESCPONTUAL>
      * <VALORDESCPONTUAL>Valor do desconto calculado para o item de desconto</VALORDESCPONTUAL>

OBSERVAÇÕES

O número de casas decimais para os valores respeitará o parâmetro do TOTVS Gestão Financeira (Contas a Receber → Manutenção de Lançamentos → Opções Gerais → Nº Casas Decimais)
