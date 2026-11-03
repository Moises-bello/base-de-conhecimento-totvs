---
content_hash: 30f6acd2011359d38634b2bb84be693f38136004355d5021604cb7208af5d1ae
fetched_at: '2026-06-29T00:10:06.733908+00:00'
page_id: '452719334'
product: rm
source: tdn-rm
title: Fórmulas / Funções – C
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719334
version: 4
---

**Função C**   
Retorna valor de um evento no movimento atual. Retorno do tipo valor. As variáveis de fórmula que são relativas a movimentação do funcionário, como a **C**, não devem ser utilizados para fórmula de seleção. Porque no momento da seleção, o sistema ainda não executou a movimentação do funcionário. Desta forma, estas funções/variáveis irão retornar sempre "zero".  
C (CÓD. DO EVENTO)  
   
**Exemplo:**  
C ('0034')  
Retornará valor do evento '0034' no mês de competência.   
   
   
**Função CALCMED**  
Retorna o valor da Média referente ao Sindicato. CALCMED (Valor utilizado para o retorno dos tipos de médias Grupo de Média).  
Onde os valores utilizados para o retorno dos tipos de médias pela CALCMED são:  
1 para Férias  
2 para13º Salário  
3 para Aviso Prévio  
4 para Licença maternidade  
5 para férias proporcionais  
   
**Exemplo:**   
CALCMED(201) - Retornará o valor da média de 13o salário do grupo 1.   
CALCMED(105) - Retornará o valor da média de férias do grupo 5.    
CALCMED(304) - Retornará o valor da média de Aviso Prévio do grupo 4.   
CALCMED(519) - Retornará o valor da média de Férias Proporcionais do grupo 19.   
   
**Observações:**  
-A variável CALCMED poderá ser usada apenas com os valores do primeiro parâmetro.  
   
CALCMED(1) - Retornará o valor total da média de férias.  
CALCMED(2) - Retornará o valor total da média de 13º salário.  
CALCMED(3) - Retornará o valor total da média do Aviso Prévio.  
O tratamento da variável CALCMED é diferente para o cálculo das médias de Licença Maternidade. Para que o sistema retorne o valor das médias de Licença Maternidade nesta variável é necessário efetuar o lançamento do salário maternidade com média no primeiro mês do Afastamento, assim o sistema guardará automaticamente o valor das médias no campo em Funcionários | Parâmetros campo "Média Salário Maternidade".  
   
   
**Função CALCMEDDATA**  
Retorna do valor da média de acordo com sindicato e com a data informada.  
CALCMEDDATA (VALOR1, VALOR2, DATA)  
VALOR1: Informar o tipo de média que será calculado.  
VALOR2: Informar o tipo de processo (férias, cálculo da folha ou rescisão) que será calculado.  
DATA: Informar a data que será realizado o cálculo da Média.  
   
**VALOR1 -** Neste campo poderão ser usados os seguintes valores de retorno**:**  
1 para Férias  
2 para13º Salário  
3 para Aviso Prévio  
5 para férias proporcionais  
   
**VALOR2 -** Neste campo poderão ser usados os seguintes valores de retorno:  
1 para Férias  
2 para13º Salário  
3 para Rescisão  
5 para férias proporcionais  
**DATA -** Informar a data que será realizado o cálculo da Média, exemplo: TABFUNC ('DATADEMISSAO'), TABFUNC ('INICPROGFERIAS1' ou 0(ZERO) para que o cálculo seja   
   
**Exemplos:**  
-CALCMEDDATA (1, 1, TABFUNC ('INICPROGFERIAS1', 'D'))  
  Retorna as médias de férias(1) no cálculo das Férias(1) observando o início de gozo do funcionário.   
-CALCMEDDATA (1 ,3, TABFUNC ('DATADEMISSAO', 'D'))  
  Retorna as média de Férias(1) na rescisão(3), verificando a data de demissão do funcionário.  
-CALCMEDDATA (2 ,3, 0)  
   Retorna as médias de 13º Salário (2) na Rescisão (3), verificando a data da competência atual.   
-CALCMEDDATA (3 ,3, TABFUNC ('DATADEMISSAO', 'D'))  
  Retorna as médias de Aviso Prévio (3) na Rescisão (3), verificando a data de demissão do funcionário.

**Função CALCMEDJOR**  
Media de carga horaria de professor.  
CALCMEDJOR (VALOR, VALOR, STRING, STRING)  
**VALOR**: Informar o tipo de média que deve ser considerada. Sendo os tipos:  
1-Férias  
2-13º Salário  
3-Aviso Prévio  
4-Licença Maternidade  
5-Férias Proporcionais  
   
**VALOR**: Informar a quantidade de meses a ser selecionado na ficha financeira para calcular a média.  
Caso informe 0(zero) o sistema considera os meses do sindicato do funcionário.  
   
**STRING**: Informar a referência dos eventos lançados na ficha financeira do funcionário para o cálculo das médias. Deverão ser separados por ( Ponto e Vírgula e ('') aspas simples.  
Exemplo: '0001;0002;0003'  
   
**STRING**: Informar uma sequência de parâmetros, sendo eles:  
   
**1º Parâmetro** => Informar se deseja que o resultado da média seja em valor.  
Caso informe S, o sistema retorna média em valor. (Quantidade de horas dos eventos X salário hora atual)  
Caso informe N, o sistema retorna média em hora. (Quantidade de horas)  
   
**Exemplo:**   
A)    O evento informado no primeiro parâmetro **STRING** é do tipo HORA e o parâmetro é 'S'  
O sistema busca a quantidade de horas do evento, multiplica pelo salário hora atual e multiplicar pelo percentual informado no evento.  
B)    O evento informado no primeiro parâmetro **STRING é** do tipo HORA e o parâmetro é 'N'  
O sistema busca a quantidade de horas do evento.  
C)    O evento informado no primeiro parâmetro **STRING** é do tipo VALOR e o parâmetro é 'S'  
O sistema busca o valor do evento.  
D)    O evento informado no primeiro parâmetro **STRING** é do tipo VALOR e o parâmetro é 'N'  
O sistema retorna zero.  
   
**Observação I:**  
Quando o funcionário utiliza salário composto, e tem um evento do tipo hora/dia/referência, e este evento NÃO está cadastrado em Funcionários |Anexo| Folha de Pagamento| Salario composto, e neste evento NÃO tem nada informado em 'Base de salário composto', o sistema busca o salário total do funcionário no momento do cálculo.  
   
Quando o funcionário utiliza salário composto, e tem um evento do tipo hora/dia/referência, e este evento NÃO está cadastrado em Funcionários |Anexo| Folha de Pagamento| Salario composto, e neste evento TEM eventos informado em 'Base de salário composto', o sistema busca o valor do evento informado em 'Base de salário composto' no momento do cálculo.  
   
Quando o funcionário utiliza salário composto, e neste evento tem um evento do tipo hora/dia/referência, e este evento ESTA cadastrado em Funcionários |Anexo| Folha de Pagamento| Salario composto, independente se existe eventos informado em 'Base de salário composto', o sistema busca o valor do próprio evento no momento do cálculo.  
   
   
**Observação II:**  
No momento do cálculo serão verificados os parâmetros do sindicato do funcionário.  
Exemplo: Parâmetros relacionados à afastamentos, considera mês atual, etc.  
   
**Observação III:**  
Lembrando que, quando o evento é do tipo DIA/REFERÊNCIA o tratamento é feito utilizando o campo REFERÊNCIA.   
   
   
**2º Parâmetro** => Informar se deseja que o sistema considere as fórmulas adicionais.  
             
           Caso informe S, o sistema busca o valor das fórmulas adicionais para somar ao salário e calcular o valor.   
           Caso contrário é utilizado apenas o salário do funcionário.  
   
**3º Parâmetro** => Informar se deseja que o sistema calcule a média verificando a quantidade de meses do evento que teve o maior número de meses no período informado.  
   
Caso informe S, o sistema pega o valor do evento e divide pela quantidade de meses do evento que teve o maior número de meses no período informado no segundo parâmetro **VALOR**.  
Caso contrário é utilizado a quantidade de meses informado no segundo parâmetro **VALOR.**  
   
**4º Parâmetro** => Definir se permite ou não a comparação dos valores de média, considerando as 3 colunas de nº de meses parametrizadas no Sindicato.  
   
Caso informe S, o sistema fará a comparação da maior média para o cálculo.  
                                                                                                                                  
**Exemplo:**  
CALCMEDJOR (1,0,'0062', 'SNNS')  
Essa fórmula retornará:  
·          **1** - A média de férias,   
·          **0** - Os meses do sindicato;  
·          **0062 -** O valor do evento 0062;  
·          **S** - Retorna a média em valor;  
·          **N** - Não utiliza as fórmulas adicionais no cálculo;  
·          **N -** Não verifica a quantidade de meses do evento que teve o maior número de meses no período informado;  
·          **S** – Permite a comparação dos valores de média considerando as colunas de nº de meses parametrizadas no sindicato.

**Função CCUSTOCORRENTE**  
A função CCUSTOCORRENTE é utilizada em fórmulas vinculadas ao processo de cálculo da Folha de Pagamento no TOTVS RM, retornando o centro de custo vigente para a matrícula (CHAPA) informada, de acordo com a configuração e hierarquia de rateio.

**Exemplo:**

CCUSTOCORRENTE(CHAPA)

Essa fórmula retornará:  (Código do centro de custo - string).

**Hierarquia de Origem do Centro de Custo**

A função busca o centro de custo de acordo com a seguinte ordem de prioridade:

* Rateio fixo do funcionário;
* Envelope de eventos (rateio vinculado ao evento);
* Seção vinculada ao funcionário;
* Centro de custo informado manualmente no evento.

**Particularidades Técnicas**

* A função depende do processamento da folha para retornar valores válidos.
* Testes realizados diretamente no cadastro de fórmulas resultarão em retorno nulo.
* A função só retorna dados se a competência em processamento estiver configurada com rateio válido.
* Alterações manuais em eventos ou envelopes podem influenciar diretamente no resultado da função.

**Situações ocasionais e possíveis soluções**

|  |  |  |
| --- | --- | --- |
| **Situação** | **Comportamento** | **Solução** |
| Teste via botão "Resultado" no cadastro de fórmula | Retorno nulo | Realizar teste em cálculo da folha |
| Funcionário possui centro de custo cadastrado mas função retorna vazio | Rateio não válido na competência atual | Verificar data de vigência e regras de rateio |
| Centro de custo informado no evento não aparece | Hierarquia considera rateio fixo ou envelope antes | Ajustar configuração de prioridade |

Observações Importantes:

* Utilize a função somente em contextos de cálculo.
* Documente as regras de rateio em cada projeto para facilitar a rastreabilidade.
* Valide previamente os centros de custo via relatórios de rateio antes de aplicar em fórmulas.
* Realize simulações de folha para validar fórmulas que envolvam CCUSTOCORRENTE.

**Função CF**  
Retorna valor de código fixo.   
CF ('CÓD. DO EVENTO).  
   
   
**Função CHAPA**  
Retorna chapa do funcionário.  
   
   
**Função CHR**  
Retorna o caractere representado pelo número. Retorno String.   
CHR(valor)  
   
   
**Função CODCALCULOCORRENTE**  
É o código de cálculo do evento que está sendo calculado no momento.  
Se esta função for executada fora do cálculo do envelope ou do recibo de férias o retorno será sempre zero**.**  
   
   
**Função CODSEÇAO**  
Retorna código da seção do funcionário. Retorno String.  
CODSECAO  
   
   
**Função CODEMPRCORRENTE**  
Esta variável só deve ser usada para o campo "Fórmula de Correção" em Funcionários | Empréstimo. Seu resultado só será atualizado quando se lançar o empréstimo.  
**Exemplos:**  
DECL CODIGO, PERC;  
SETVAR(CODIGO, CODEMPRCORRENTE );  
SETVAR(PERC, TABEMPRESTIMO ( 'SALDODEVEDOR' ,'V', CODIGO));   
SE PERC > 0   
ENTAO PERC \* 0.10  
SENAO 0  
FIMSE  
Ao processar em folha Mensal | Lançamento | grupo de Eventos campo Lançar empréstimo o sistema irá buscar o valor do código corrente de empréstimo e aplicar 10% ao seu valor original e realizar o desconto do empréstimo de acordo com as parcelas restantes.  
Seguem os cálculos realizados pelo sistema, conforme a fórmula acima:  
1) Empréstimo 1 =>Saldo Devedor de R$ 1000,00, com 5 parcelas e Fórmula de correção com 10% do saldo devedor    
    (R$1000,00 + R$100,00) / 5 = R$ 220,00  
   
2) Empréstimo 1 =>Saldo Devedor de R$ 440,00, com 5 parcelas, 3 parcelas já pagas e   
   Fórmula de correção com 10% do saldo devedor   
  (R$440,00+ R$ 44,00) / (5 - 3) = R$ 242,00  
   
   
**Função Concat**  
Concateia, isto é, junta, duas strings. Recebe dois parâmetros tipo string e devolve outra.  
**Exemplo:**  
CONCAT ('T', CONCAT ('O', 'TVS'))  
Resultado = 'TOTVS'  
   
   
**Função COLIGADACORRENTE**  
Retorna o número da coligada corrente. Retorno Valor  
   
**Função CONCAT5**  
Concatena 5 (cinco) strings  
CONCAT5 ( STRING,STRING,STRING,STRING,STRING )  
**Exemplo:**  
CONCAT5 ('1997', '-', TABPESSOA ('NOME', 'S'),' ', TABBANCO ('0001', 'CODAGENCIA'))    
Concatenará o ano, traços, nome da pessoa, traços, código da agência:  
1997ITAMAR MENDES DA SILVEIRA--- 0433  
**Observação:**  
É necessário informar cinco strings ou funções que retornam strings). Lembre-se: espaços em branco também são strings.  
   
**Função CONCATVT**  
Concatenar valores dos campos de Vale Transporte.  
CONCATVT (STRING, STRING, INDEFINIDO)  
   
**Função CONTEMVALOR**  
Procura determinador valor em um conjunto de valores.   
CONTEMVALOR (STRING, INDEFINIDO, STRING)  
   
**Função COTACAOMOEDA**  
Cotação de uma moeda.  
COTACAOMOEDA (STRING, DATA)  
   
**Função CREC**  
Retorna código de recebimento do funcionário  
   
   
**Função CSIND**  
Retorna código do sindicato do funcionário. Retorna STRING.
