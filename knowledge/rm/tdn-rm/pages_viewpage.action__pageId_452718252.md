---
content_hash: c79d03e95041ce22c76357c6df6456c1e5541e6ddca9e9894f5cb5c77fc5b62b
fetched_at: '2026-06-29T00:09:58.935925+00:00'
page_id: '452718252'
product: rm
source: tdn-rm
title: Fórmulas / Funções T
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718252
version: 13
---

**FUNÇÃO T**

Retorna valor de tabela.

T (‘CÓD. TABELA’,'VALOR')

**1º Parâmetro:** nome da tabela  
**2º Parâmetro:** valor  
   
**Exemplo:**   
A empresa Exemplo mantém a seguinte tabela de finalidade 0 - Sem finalidade específica, que está cadastrada nas Tabelas de Cálculo com código 0004.

Teto salarial      Percentual de desconto

R$500,00          10

R$700,00          20

R$1000.00        30

T (‘0004’, RC)

Supondo que o salário seja de R$751,20 retorna o resultado 751,2 \* 0,30 = 225,36

**Observação:** A função de fórmula é limitada ao valor final da tabela, sugerimos utilizar a função de fórmula T2 que calcula para valores acima do limite da tabela utilizando o último percentual cadastrado.

**FUNÇÃO T2**

Retorna valor de tabela considerando o teto.

T2 (STRING, VALOR)

**1º Parâmetro:** nome da tabela  
**2º Parâmetro:** valor

**Exemplo:**   
A empresa Exemplo mantém a seguinte tabela de finalidade 0 - Sem finalidade específica, que está cadastrada nas Tabelas de Cálculo com código 0004.

Teto salarial      Percentual de desconto

R$500,00          10

R$700,00          20

R$1000.00        30

T2 (‘0004’, RC)

Supondo que o salário seja de R$1100,00 retorna o resultado 1100 \* 0,30 = 330

**Observação:** A função de fórmula calcula para valores acima do limite da tabela utilizando o último percentual cadastrado.

**FUNÇÃO TABBANCO**

Retorna o conteúdo de um campo da tabela de bancos.

TABBANCO ('CÓD.DO BANCO','CAMPO DA TABELA)

**Exemplo:**

TABBANCO (‘001’, ’NOME’)

Retorna o Nome cadastrado no Banco 001.

**FUNÇÃO TABCALCULO**

Retorna o valor de um campo das Tabelas de Cálculo.

TABCALCULO ('CAMPO DA TABELA', 'CÓDIGO DA TABELA', 'INÍCIO DA VIGÊNCIA', 'NÚMERO DA FAIXA')

**1º Parâmetro:** Campo da tabela - É o campo da tabela de valores da tabela de cálculo que retornará o valor. O nome de ser colocado unidos (LIMITESUPERIOR)

**2º Parâmetro:** Código da tabela - Qual tabela de cálculo você quer saber o valor. Como por exemplo, : INSS, IRRF e etc.

**3º Parâmetro:** Início da vigência: Início da vigência da tabela de cálculo que você quer.

**4º Parâmetro:** Número da Faixa: É o número da faixa da tabela de valores da tabela de cálculo que você quer saber o valor.

**Exemplo:**

TABCALCULO ('LIMITESUPERIOR', 'INSS', '01/06/1999’, 4)

A fórmula retornará o limite superior da tabela de INSS com vigência 01/06/1999, na faixa 4.

**FUNÇÃO TABCARGO**

Retorna o conteúdo de um campo na tabela de cargo.

TABCARGO ('Código do Cargo', 'Campo da Tabela de Cargo')

**Exemplo:**

TABCARGO ('01', 'DESCRICAO')

Retorna a descrição que está cadastrada no Cargo "01".

**FUNÇÃO TABCODFIX**

Retorna conteúdo de um campo da tabela de Códigos fixos.

TABCODFIX ('CAMPO DA TABELA', 'MODO DE VER O RETORNO','CÓDIGO DO CÓD.FIXO')

**Exemplo:**

TABCODFIX ('NROVEZES', 'v', '0002')

Retorna o valor do número de vezes cadastrado no Código Fixo do evento '0002' em Funcionários.

**FUNÇÃO TABCOLIG**

Retorna o valor de um campo na tabela de coligada.

TABCOLIG ('Campo da Coligada')

**Exemplo:**

TABCOLIG ('CIDADE')

Retorna o nome da cidade cadastrada na Coligada.

**FUNÇÃO TABCOLIGADA**

Retorna o valor de uma Coluna da tabela GCOLIGADA da coligada corrente que o usuário tem acesso na GPERMISS

TABCOLIGADA (STRING, STRING)

**Exemplo:**

TABCOLIGADA ('NOME', 'S')

Retorna o nome da coligada corrente.

**FUNÇÃO TABCOMPL**

Retorna o conteúdo de um campo da tabela de campos complementares.

TABCOMPL ('CAMPO DA TABELA', 'MODO DE VER O RETORNO')

**Exemplo:**

TABCOMPL ('SANGUE','S')

Retorna no valor cadastrado no Campo Complementar ‘SANGUE’ que está em Funcionários.

**FUNÇÃO TABCOMPLDEPEND**

Retorna o conteúdo de um campo da tabela de campos complementares do dependente.

TABCOMPLDEPEND ('CAMPO DA TABELA', 'MODO DE VER O RETORNO', NRO DEPENDENTE)

**Exemplo:**

TABCOMPLDEPEND ('AUXILIOCRECHE', 'S', 3)

Retorna o valor cadastrado no Campo Complementar ‘AUXILIOCRECHE’ que está no Dependente nº 3.

**FUNÇÃO TABCOMPLORC**

Retorna o valor de um campo complementar no orçamento.

TABCOMPLORC (STRING, STRING)

TABCOMPLORC ('CAMPO DA TABELA', 'MODO DE VER O RETORNO')

**FUNÇÃO TABDEP**

Retorna o campo da tabela de dependentes.

TABDEP ('CAMPO DA TABELA', 'MODO DE VER O RETORNO', NÚMERO IDENTIFICADOR DO DEPENDENTE')

**Exemplo:**

TABDEP ('NOME’, 'S’, 1)

Retorna o nome do primeiro dependente no cadastro do funcionário.

**FUNÇÃO TABEMPRESTIMO**

Retorna o valor de empréstimos de um determinado código no cadastro de funcionários e que poderá ser útil em fórmulas de correção de valores de empréstimos.

TABEMPRESTIMO ('CAMPO DA TABELA', 'MODO DE VER O RETORNO', 'CÓDIGO DE EMPRÉSTIMO')

**Exemplo:**

TABEMPRESTIMO (‘VALORORIGINAL’,'V', '01’)

Retorna o valor do campo Valor Original do cadastro do código de empréstimo 01 no cadastro de funcionários em anexo de Empréstimos.

**FUNÇÃO TABEVTPROG**

Retornar o valor de um campo da tabela de Eventos Programados.  
TABEVTPROG (STRING, STRING, STRING, STRING)

**1º Parâmetro:** Deverá informa o campo da tabela que desejar;  
**2º Parâmetro:** Informar o modo de retorno. Sendo V(valor), S(string), I(inteiro) ou D(data);  
**3º Parâmetro:** Informar o código do evento programado.  
**4º Parâmetro:** Informar o ID do evento programado. Isso porque pode existir o mesmo evento mais de uma vez para o mesmo funcionário, e o sistema precisa saber a qual evento refere-se a fórmula.  
Quando a fórmula for utilizada no processo de Alteração Global de Eventos Programados deverá informar neste campo a variável EVTPROGCORRENTE ('ID');  
   
**Exemplo:**  
TABEVTPROG('VALOR','S','1133',1)  
O sistema irá retornar o valor do primeiro evento programado 1133 encontrado para o funcionário com o formato em String.

**FUNÇÃO TABFUNC**

Retorna o conteúdo de um campo da tabela de funcionários.

TABFUNC ('CAMPO DA TABELA', 'MODO DE VER O RETORNO')

**Exemplo 1:**

TABFUNC (‘SALDOFGTS’, ‘V’)

Retorna o saldo de FGTS. Tipo retorno: Valor

**Exemplo 2:**

TABFUNC ('DATAINICIODESCEMPRESTIMO', 'D')

**Observação:**

Quando o usuário tiver restrição de acesso a campos do cadastro dos funcionários, o sistema não permitirá que o usuário utilize esta variável.

**FUNÇÃO TABFUNCAO**

Retorna o conteúdo de um campo da tabela de funções.

TABFUNCAO (‘CÓDIGO DA FUNÇÃO’,‘CAMPO DA TABELA')

**Exemplo 1:**

TABFUNCAO (TABFUNC ('CODFUNCAO','S') , 'NUMPONTOS')

Retorna o número de pontos de determinada função cadastrada em Função. Onde a fórmula TABFUNC ('CODFUNCAO','S') retorna o número da função do funcionário.

**Exemplo 2:**

TABFUNCAO (‘0024’, ‘NOME’)

Retorna o nome da função de código 0024.

**FUNÇÃO TABPESSOA**

Retorna um campo da tabela de pessoas. Pode ser usada em caso de integração com o RM Vitae. Não será possível, porém, acessar campos de registros de pessoas que não estejam com status de funcionário.

TABPESSOA ('CAMPO DA TABELA', 'MODO DE VER O RETORNO')

**Exemplo:**

TABPESSOA ('CPF','S')

Retorna o CPF da pessoa.

**FUNÇÃO TABPRGAVISO**

Retorna os dados da tabela PPRGAVISO que contém as programações de avisos automáticos

TABPRGAVISO ('CAMPO DA TABELA', 'MODO DE VER O RETORNO', ID DO AVISO AUTOMÁTICO)

**Exemplo 1:**

TABPRGAVISO ('DTPROXEXEC', 'D', 3)

A fórmula irá retornar o campo Data da Próxima Execução do Aviso Automático ID =3

**Exemplo 2:**

TABPRGAVISO ('DESCRICAO', 'S', 1)

A fórmula irá retornar à Descrição do Aviso Automático ID=1

**FUNÇÃO TABSECAO**

Retorna o valor de um campo da seção. Útil na busca de campos na tabela de seção, nome de colunas, tipo de dado e código de seção.

TABSECAO (‘CAMPO DA TABELA', 'MODO DE VER O RETORNO', 'CODIGO DA SECAO')

**Exemplo:**

TABSECAO ('DESCRIÇÃO', 'S', '01.04')

Retorna a descrição da seção de código ’01.04’.

**FUNÇÃO TAMSTR**

Retorna o tamanho de uma string.

TAMSTR (STRING)

**Exemplo:**

TAMSTR ('TOTVS SA')

Retorna 8, contando inclusive o espaço.

**FUNÇÃO TCASA**

Retorna anos de casa.

TCASA

**Exemplo:**

SE CHAPA = '00001'

ENTAO TCASA

FIMSE

Retorna o tempo de casa do funcionário de chapa ‘00001’

**Observação:** Quando o parâmetro **'Estorna Tempo de Serviço'** disponível em RM | RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Anexos | Históricos | Histórico de Afastamentos estiver marcado, será descontado o período de afastamento na contagem do tempo de serviço do empregado.

**Exemplo:**  
Supondo que a empresa resolva oferecer participação nos lucros apenas para funcionários com um ano ou mais de tempo de serviço.  
Se um funcionário admitido na empresa há 1 (um) ano esteve afastado por 3 (três) meses e o campo 'Estorna Tempo de Serviço' foi habilitado, o sistema descontará o período de afastamento.  
O sistema considerará, então, que o empregado tem 9 (nove) meses de tempo de serviço e, portanto, não terá direito à participação nos lucros.

**FUNÇÃO TETO**

Arredonda para cima.

TETO (número)

**Exemplo:**

TETO (RC)

Se o salário do empregado for R$751,20, retornará R$752,00.

**FUNÇÃO TFUNC**

Retorna o tipo de funcionário. (Normal, Autônomo, Estatutário, etc.)

TFUNC

**Exemplo:**

TFUNC

Se for selecionado um funcionário tipo N – Normal o retorno será N.

**FUNÇÃO TI**

Retorna o valor de INSS calculado com o valor da alíquota normal.

TI (VALOR)

**Exemplo:**

**TI** (SM)

Parametrização:

No cadastro do Valor Fixo com finalidade Valor do salário mínimo está informado R$1.100,00 e

Na tabela INSS – INSS tem a primeira incidência 7,5% até R$1.100,00

O valor retornado será 1100 \* 7,5 /100 = 82,50

**FUNÇÃO TI2**

Retorna o valor do INSS calculado com o valor da alíquota com o CPMF.

TI2 (VALOR)

**Exemplo:**

**TI2** (SM)

Parametrização:

No cadastro do Valor Fixo com finalidade Valor do salário mínimo está informado R$1.100,00 e

Na tabela INSS – INSS tem a segunda incidência 8% até R$1.100,00

O valor retornado será 1100 \* 8/100 = 82,50

**FUNÇÃO TIPOCALCFERIAS**

Tipo do Cálculo de Férias, ou seja, retorna se no momento da execução da fórmula está sendo calculada férias vencidas ou proporcionais.

TIPOCALCFERIAS

Tipo de retorno:

1 = Férias Vencidas

2 = Férias Proporcionais

**Exemplo:**

No momento do cálculo de uma rescisão ou histórico de provisão será calculado utilizando o cálculo da CALCMED com o parâmetro 1 para Férias se o tipo de cálculo for férias vencidas e utilizando o cálculo da CALCMED com o parâmetro 5 para Férias Proporcionais se o tipo de cálculo for férias proporcionais. È apropriado utilizar essa função somente em situações que possuem cálculos diferenciados para férias vencidas e férias proporcionais.

Criando a fórmula abaixo e informando no Parametrizador / Férias / Fórmulas adicionais:

SE ((PROCESSO = 'PROVISAO') OR (PROCESSO = 'RESCISAO'))

ENTAO  
              SE (TIPOCALCFERIAS = 1)

              ENTAO CALCMED(1)

              SENAO CALCMED(5)

FIMSE

**Observação:** A fórmula acima somente pode ser utilizada se no Parametrizador / Folha Normal / Cálculo 2/2 o parâmetro "Ignora fórmulas adicionais no cálculo de médias" estiver marcado porque possui a função CALCMED. Caso contrário irá fazer com que a execução entre em recursividade.

No momento do cálculo do histórico de provisões o retorno no log será:

**Saldo vencido: 30,00**  
  
              Calculando evento: 0038 - FERIAS  
              Código de Cálculo 38 - Prioridade 0  
  
              Salário Base: 1918,74  
  
                      Execução da fórmula adicional TIPOCALC  
                      Processando variável PROCESSO  
                      Processo que está sendo executado no momento: PROVISAO  
                      Processando variável PROCESSO  
                      Processo que está sendo executado no momento: PROVISAO  
                      Processando variável TIPOCALCFERIAS  
**Tipo do Cálculo de Férias: 1**

**Saldo proporcional: 17,50**  
  
                Calculando evento: 0038 - FERIAS  
                Código de Cálculo 38 - Prioridade 0  
  
                Salário Base: 1918,74  
  
                      Execução da fórmula adicional TIPOCALC  
                      Processando variável PROCESSO  
                      Processo que está sendo executado no momento: PROVISAO  
                      Processando variável PROCESSO  
                      Processo que está sendo executado no momento: PROVISAO  
                      Processando variável TIPOCALCFERIAS  
                      **Tipo do Cálculo de Férias: 2**

**FUNÇÃO TOTALFALTAS**

Esta variável facilita o desconto das faltas do funcionário quando o cliente não tem integração com o Automação de Ponto e utiliza o Controle de faltas para cálculo de avos.

TOTALFALTAS (DATA, DATA, VALOR)

**1º Parâmetro:** Deverá informa data início para verificação da falta;

**2º Parâmetro:** Deverá informa data fim para verificação da falta;

**3º Parâmetro:** Informar 0(zero) para não considerar as faltas abonadas e 1(um) para considerar as faltas abonadas no anexo Controle de faltas para cálculo de avos.

**Exemplo:**

TOTALFALTAS ('01/07/2010,'31/07/2010',0)

O sistema irá retornar o total de faltas cadastradas no anexo Controle de faltas para cálculo de avos do funcionário e que não estão abonadas, ou o total do evento com código de cálculo 8.

**Observação:**

Para períodos anteriores ao mês de início da utilização do Controle de faltas para cálculo de avos o sistema irá busca a quantidade de faltas do evento com código de cálculo 8. O mesmo ocorrerá para quem não utiliza o Controle de faltas para cálculo de avos.

**FUNÇÃO TOTDESC**

Retorna o total de descontos do período atual.

TOTDESC

**Atenção:**

As variáveis de fórmula que são relativas à movimentação do funcionário, como a TOTDESC, não devem ser utilizadas para fórmula de seleção. Porque no momento da seleção, o sistema ainda não executou a movimentação do funcionário. Desta forma, estas funções/variáveis irão retornar sempre "zero".

**FUNÇÃO TOTPROV**

Retorna o total de proventos do período atual.

TOTPROV

**Atenção:**

As variáveis de fórmula que são relativas à movimentação do funcionário, como a TOTPROV, não devem ser utilizadas para fórmula de seleção. Porque no momento da seleção, o sistema ainda não executou a movimentação do funcionário. Desta forma, estas funções/variáveis irão retornar sempre "zero".

**FUNÇÃO TOTREPOSITORIO**

Total de um Evento no Gerenciador de Movimento. Utilizado quando o parâmetro "Utiliza Gerenciador de Movimento"  estiver marcado no parametrizador em Folha normal - Cálculo 2/2.

TOTREPOSITORIO (STRING, STRING, STRING, VALOR, VALOR, VALOR)

TOTREPOSITORIO (Par1, Par2, Par3, Par4, Par5, Par6)

**1º Parâmetro:** Código do Evento

**2º Parâmetro:** Se R retorna Referência do evento, se H retorna Hora do evento, se V retorna Valor do evento

**3º Parâmetro:** Centro de Custo (Se vazio, considera todos)

**4º Parâmetro:** Mês Competência

**5º Parâmetro:** Ano Competência

**6º Parâmetro:** Período (Se zero, considera todos)

**Exemplo:**

TOTREPOSITORIO ('0002', 'R', '01.1', 7, 2021, 1)

Retorna a referência do evento 0002 que tem o centro de custo 01.1 lançado no repositório no período 1 do mês 07 do ano 2021.

**FUNÇÃO TQUEBRA**

Testa o código de quebra.

TQUEBRA (‘CÓD. SEÇÃO, ‘CÓD. DE QUEBRA’)

**Exemplo:**

SE TQUEBRA (TABFUNC ('CODSECAO', 'S'), '01.01') = VERDADE ENTAO RC\*1.2 SENAO RC\*1.1 FIMSE

O sistema pesquisará a seção do funcionário (retornada pela função CODSECAO), comparando-a com o código de quebra informado: 01.01.

Se a comparação for positiva (código da seção coincidir com quebra), o salário será acrescido de 20%. Caso contrário, será multiplicado por 10%.

**Observação:**

Poderá substituir uma parte da seção por interrogações. Exemplo: 01.??.

**FUNÇÃO TRUNCVALOR**

Esta função trunca um valor (1º Parâmetro) dado um número de casas decimais (2º Parâmetro).

TRUNCVALOR (VALOR, VALOR)

**Exemplo:**

TRUNCAVALOR (1235.4756, 3)

O sistema irá truncar o valor 1235,4756 (1º Parâmetro) na terceira casa decimal (2º Parâmetro). Logo o resultado apresentado para esta fórmula é 1235,475
