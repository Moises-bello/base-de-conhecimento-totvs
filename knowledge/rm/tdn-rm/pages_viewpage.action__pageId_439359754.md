---
content_hash: 5076f46ac77aa398b5a71b6752a25c5e0d92743f8697d24c6b15dd0ee4156a82
fetched_at: '2026-06-29T00:09:52.401017+00:00'
page_id: '439359754'
product: rm
source: tdn-rm
title: Simulação de parcelas de contratos utilizando plano de pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439359754
version: 20
---

## Visão Geral

O objetivo desse serviço é simular valores de parcelas de contratos de alunos através da configuração de parcelas de planos de pagamentos e concessão de bolsas futuras, informando o plano de pagamento, período letivo, matriz aplicada e uma lista de turmas disciplinas bem como um determinado status de matrícula na disciplina.

Esse serviço possibilita ao usuário do mesmo simular os valores a serem pagos pelo aluno antes de efetuarem a matrícula nas disciplinas de determinadas turmas, ou seja, não é necessário ter matrícula nas disciplinas bem como não é necessário se ter contrato para que o cálculo das parcelas seja feito.

O cálculo dos valores de parcelas segue a mesma regra da simulação de parcelas de contratos, ao selecionar uma determinada parcela na visão de parcela e clicar no botão para simular o cálculo, o qual realiza a simulação dos valores de parcelas baseados no plano de pagamento informado, bem como suas turmas disciplinas e um status de matrícula a ser considerado.

É possível parametrizar o TOTVS Educacional para que ao criar as parcelas no contrato do aluno a partir do plano de pagamento, sejam consideradas do plano de pagamento somente as parcelas com vencimento a partir do mês da inclusão do plano de pagamento no contrato.

Para saber mais [clique aqui](https://tdn.totvs.com/display/LRM/Tesouraria).

Dúvidas para exposição de webservices podem ser esclarecidas através do link: **Como Expor os Web Services do RM através do Host**

Dúvidas para configuração do host podem ser esclarecidas através do link**:   
[Ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

### Método SimularValoresPlanoPgtoTurmaDisc

O método **SimularValoresPlanoPgtoTurmaDisc** presente no webservice do TOTVS Educacional (**wsEdu**) realiza a simulação dos valores de parcelas baseados no plano de pagamento informado, bem como suas turmas disciplinas e um status de matrícula a ser considerado. Como informações obrigatórias no XML, devem ser informados o contexto do TOTVS Educacional a ser considerado, RA do aluno, Código do Período Letivo, Código do Plano de pagamento, lista de turmas disciplinas e código do status de matrícula.

Segue abaixo uma descrição dos parâmetros a serem passados para a simulação de valores de parcelas:

* **contextoSrv**: Contexto do TOTVS Educacional a ser executada a simulação. Possui o seguinte formato: [coligada],[código da filial],[Código do nível de ensino].  
    Exemplo: 1,1,1 (coligada = 1, código da filial = 1, código do nível de ensino = 1)
* **ra**: Registro acadêmico do aluno
* **idPerLet**: Id. do período letivo
* **codPlanoPgto**: Código do plano de pagamento
* **idHabilitacaoFilial**: Identificador da matriz aplicada que será vinculada ao contrato do aluno após matrícula.Necessário SOMENTE para simulação de valores de parcelas por crédito, ou seja, o mesmo não é obrigatório para a simulação de valores baseados em planos de pagamentos de parcelas fixas.
* **strListaIdTurmaDisc**: Lista contendo os identificadores de turmas disciplinas a serem consideradas separadas por vírgula.  
    Exemplo: <IdTurmaDisc1>,<IdTurmaDisc2>
* **consideraDescontoAntecipacao**: Parâmetro opcional. Indica se descontos por antecipação deverão ser considerados na simulação de valores de parcelas.   
  Os descontos por antecipação considerados serão aqueles informados no campus / polo da matriz aplicada informada ou na matriz aplicada caso existam descontos por antecipação vinculados à matriz aplicada e não existam no campus / polo dessa matriz aplicada.  
  Poderá ter os valores (**S** - Considera valores de descontos por antecipação, **N** - Desconsidera valores de descontos por antecipação).  
  Caso não seja informado ou seja passado um valor vazio, o valor default para o mesmo é "**S**"
* **consideraDescontoAntecipacaoBolsa**: Parâmetro opcional, indica se descontos por antecipação deverão ser considerados no cálculo de valores de bolsas na simulação de valores de parcelas, para bolsa do tipo somar bolsa ou Aplicar somente a maior Bolsa.  
  Poderá ter os valores (**S** - Considera valores de descontos por antecipação no cálculo de valores de bolsas, **N** - Desconsidera valores de descontos por antecipação no cálculo de valores de bolsas).  
  Caso não seja informado ou seja passado um valor vazio, o valor default para o mesmo é "**N**"
* **tipoBolsaContrato**: Parâmetro opcional. Comportamento das bolsas no contrato.  
  Poderá ter os valores (**S** - Somar Bolsas, **C** - Aplicar bolsas em cascata, **M** - Aplicar somente a maior bolsa).  
  Caso não seja informado ou seja passado um valor vazio, o valor default para o mesmo é "**S**"
* **codStatusMatriculaDisc**: Código de status de matrícula na disciplina a ser considerado na simulação de valores.

**Exemplo de parâmetros de simulação preenchidos (utilizando o aplicativo SOAPUI)**:

XML




1,1,3

20180320

104

PLAN

94

4560

S

N

S

123
]]>

Na imagem acima observe que:

* A tag "**contextoSrv**" contém a informação 1,1,3 que significa:  
  + Código da coligada igual a 1
  + Código da filial igual a 1
  + Código do nível de ensino (codtipocurso) igual a 3
* A tag "**ra**" contém a informação:
  + RA do aluno igual a 20180320
* A tag "**idPerLet**" contém a informação:
  + Id. do período letivo igual a 104
* A tag "**codPlanoPgto**" contém a informação:
  + Código do plano de pagamento igual a PLAN
* A tag "**idHabilitacaoFilial**" contém a informação:
  + Identificador da matriz aplicada igual a 94
* A tag "**strListaIdTurmaDisc**" contém a informação 4560 que significa que:  
  + Será considerada a turma disciplina com o idTurmaDisc igual a 4560
* A tag "**consideraDescontoAntecipacao**" contém a informação S que significa que:
  + Serão considerados valores de desconto por antecipação informados no campus / polo da matriz aplicada ou na matriz aplicada
* A tag "**consideraDescontoAntecipacaoBolsa**" contém a informação N que significa que:
  + NÃO serão considerados valores de desconto por antecipação no cálculo dos valores de bolsas
* A tag "**tipoBolsaContrato**" contém a informação S que significa que:
  + Será considerada a opção "Somar Bolsas" de contratos para cálculo dos valores de bolsas
* A tag "**codStatusMatriculaDisc**" contém a informação:
  + Código do status de matrícula na disciplina igual a 123.

    O status ou situação de matrícula na disciplina, no caso de simulação de parcelas calculadas por valor de crédito, deverão ter a opção de contar como créditos financeiros (cobrança por crédito) marcada. Vide imagem abaixo:

    Caso essa opção não esteja marcada, o serviço retornará os valores zerados para as parcelas.

    Parcelas com valor fixo retornarão o seu próprio valor desconsiderando quaisquer valores de créditos ou informações contidas nas turmas disciplinas.

Validações feitas pelo serviço:

1. **Sistema não encontra as parcelas informadas**: Caso não sejam encontradas parcelas com os identificadores de parcelas informados para o serviço será exibida a seguinte mensagem "**Não foram encontrados registros a serem simulados**" conforme abaixo
2. **Contexto do Educacional não informado**: Caso o contexto do TOTVS Educacional não tenha sido informado será exibida a mensagem "**Contexto do serviço deve ser informado.**" conforme abaixo:
3. **Registro acadêmico não informado**: Caso não seja informado o RA do aluno, será exibida a mensagem "**RA deve ser informado."** conforme abaixo:
4. **Código do período letivo não informado**: Será exibida a mensagem "**Código do período letivo deve ser informado**" conforme abaixo:
5. **Código do plano de pagamento não informado**: Será exibida a mensagem "**Código do plano de pagamento deve ser informado**" conforme abaixo:
6. **Identificador da matriz aplicada não é um número inteiro**: Será exibida a mensagem "****Identificador da matriz aplicada não é um número inteiro****" conforme abaixo:
7. **Código da situação de matrícula nas disciplinas (status) não informado**: Será exibida a mensagem "**Status de matrícula na disciplina deve ser informado.**" conforme abaixo:
8. **Erros devido a inconsistências diversas**. Será exibida a mensagem conforme abaixo:

### XML de retorno do serviço de simulação:

Conforme foi dito acima, o serviço **SimularValoresPlanoPgtoTurmaDisc** de wsEdu retorna os valores simulados conforme regra de simulação de valores de parcelas de contratos da visão de parcelas  sem dependência de quaisquer matrículas em disciplinas nem de contratos existentes.

Abaixo seguem alguns dados utilizados em uma simulação utilizando o serviço:

(PLANO DE PAGAMENTO)

* Identificador da Matriz Aplicada (IdHabilitacaoFilial): 94
* Considera desconto por antecipação: Marcado
* Considerar o valor do desconto por antecipação no valor base para calcular o valor da(s) bolsa(s): Desmarcado
* Tipo da Bolsa: Somar Bolsas

(PARCELA DO PLANO)

* Valor fixo: 600,00
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

* Identificador do Desconto: 20
* Descrição: PRIMEIRO VENCIMENTO
* Valor do desconto: 10%
* Dia Fixo: 28

Parâmetros passados para o serviço:

XML




1,1,3

20180320

104

PLAN

94

4560

S

N

S

123
]]>

Após execução do serviço, o sistema retorna o seguinte XML:

xmlXML de retorno

1
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


20
371,664
30/07/2018
41,76
]]>

Abaixo segue uma explicação de cada tag do XML de retorno do serviço.

* <SIMULACAO>Contém a marcação inicial e a marcação final do XML de retorno do serviço de simulação.</SIMULACAO>
* <PARCELA>Contém a marcação inicial e a marcação final para os dados simulados de cada parcela</PARCELA>

  + <CODCOLIGADA>Código da coligada</CODCOLIGADA>
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

    Essa Tag **BOLSAS**exibirá os valores da bolsa referente ao primeiro vencimento do desconto por antecipação quando o desconto por calculado pelo sistema conforme as parametrizações realizadas. As bolsas consideradas serão as cadastradas na concessão de bolsa futura para o aluno
  + <DESCONTOPORANTECIPACAO>Contém a marcação inicial e a marcação final do XML para os dados de descontos por antecipação</DESCONTOPORANTECIPACAO>

    - <ITEMDESCONTO>Contém a marcação inicial e a marcação final para cada item de desconto por antecipação calculado para a parcela<ITEMDESCONTO>

      * <IDDESCONTO>Identificador do item de desconto</IDDESCONTO>
      * <VLRPGTOPORDESCPONTUAL>Valor a ser pago para esse item de desconto (vencimento por antecipação)</VLRPGTOPORDESCPONTUAL>
      * <DTDESCPONTUAL>Data limite calculada para o item de desconto com base no dia informado no formato (dd/mm/yyyy)</DTDESCPONTUAL>
      * <VALORDESCPONTUAL>Valor do desconto calculado para o item de desconto</VALORDESCPONTUAL>
