---
content_hash: 7bee7800f8570f2b33e15fb2c5b2f718e15e27a983a90e598498037120c70e3f
fetched_at: '2026-06-29T00:10:38.905385+00:00'
page_id: '545621517'
product: rm
source: tdn-rm
title: MP 936/1.045 - Redução Proporcional de Jornada de Trabalho e Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=545621517
version: 111
---

Durante esse período (calamidade), o empregador poderá acordar no prazo de 90 dias a redução proporcional da jornada de trabalho e a redução de salário.

Devendo respeitar os seguintes requisitos:

* A preservação do salário hora de trabalho;
* Pactuação por acordo individual escrito entre as partes, que deverá ser encaminhada ao empregado com no mínimo de antecedência de 2 dias corridos;
* Redução da jornada de trabalho e salário, exclusivamente nos seguintes percentuais : 25% , 50% ou 70%.

A jornada de trabalho e o salário que eram pagos anteriormente antes desse período (calamidade), serão restabelecidos, sendo:

* No prazo de dois dias corridos, contando da cessão do estado de calamidade pública;
* Na data estabelecida no acordo individual com termo de encerramento que foi realizado no período e redução pactuado;
* Na data de comunicação do empregador que informe ao empregado sobre a sua decisão de antecipar o fim do período de redução pactuado.

**Procedimentos na Folha de Pagamento**

Caso o empregador faça a adesão a redução de jornada/salário deverá seguir os procedimentos abaixo:

**01.  Cadastro do F****uncionário |****Dados "B.E.M."**

Preencher os campos na aba [B.E.M.](https://tdn.totvs.com/pages/viewpage.action?pageId=545641381), eles serão necessários para informação da redução da jornada tanto para o eSocial como para o cálculo na folha.

falseImportante

**eSocial**

Conforme a orientação do eSocial, o empregador deverá enviar um evento de alteração contratual (S-2206) com Data de Alteração igual ao início do período de redução de salário e jornada e, neste evento, informar o valor do salário reduzido e a nova jornada a ser cumprida pelo trabalhador durante esse período.

No campo observação deverá informar o prazo pactuado para a referida redução e o percentual definido para essa redução proporcional. Mais informações sobre a geração do evento S-2206 [acesse aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=556391463)

**Cálculo da Folha de Pagamento**

Como não houve alteração de Jornada no Cadastro do Funcionário, o módulo Folha de Pagamento não irá calcular os dias trabalhados considerando a Redução de Jornada acordada para o cálculo de salário mensal. Neste contexto, orientamos os clientes a criarem uma verba complementar, para descontar o proporcional da redução da Jornada/Salário do funcionário, utilizando fórmula.

Para os funcionários que tiveram a jornada reduzida e foram feitas as apurações das horas trabalhadas pelo Módulo Automação de Ponto não ha necessidade de lançar a verba de desconto.

As orientações de como fazer a redução de jornada através do Módulo Automação de Ponto encontram-se no [Link](https://tdn.totvs.com/pages/releaseview.action?pageId=545257629). Para essas empresas, será necessário a observância do usuário para a utilização do parâmetro "Desconsiderar % de redução no cálculo da jornada - MP 936/20 (Integração com TOTVS Automação de Ponto)":

Caso utilizar integração com o Totvs Automação de Ponto e marcá-lo, o sistema não olhará o valor informado no campo "Percentual de Redução da Jornada" no Histórico do cadastro do B.E.M. para calcular a tag <qtdHrsSem> no evento S-2206.

Exemplo: Somando a jornada cadastrada no horário do funcionário, corresponde a um total de 20 horas semanais após a alteração do horário do funcionário para o período do B.E.M.. No campo de Percentual de Redução da Jornada foi informado o valor de 50%. Nesse caso será levado para a tag <qtdHrsSem> o valor de 20 horas semanais pois não irá considerar esse percentual no cálculo.

Caso utilizar integração com o Totvs Automação de Ponto e não marcá-lo, o sistema olhará o valor informado no campo "Percentual de Redução da Jornada" no Histórico do cadastro do B.E.M. para calcular a tag <qtdHrsSem> no evento S-2206.

Exemplo: Somando a jornada cadastrada no horário do funcionário, corresponde a um total de 20 horas semanais após a alteração do horário do funcionário para o período do B.E.M.. No campo de Percentual de Redução da Jornada foi informado o valor de 50%. Nesse caso será levado para a tag <qtdHrsSem> o valor de 10 horas semanais pois será aplicado novamente a redução de 50% sobre as horas semanais da jornada do funcionário.

Obs.: Caso a empresa não utilizar integração com o Totvs Automação de Ponto, sempre será considerado o campo "Percentual de Redução da Jornada" no Histórico do cadastro do B.E.M. para calcular a tag <qtdHrsSem> no evento S-2206.

Atenção

As fórmulas e abordagens apresentadas abaixo são sugestões para exemplificar o funcionamento do processo, ficando a critério do usuário em usar, modificar ou até mesmo desenvolver outras fórmulas ou soluções conforme a sua necessidade.

Como exemplo iremos considerar que o funcionário tem o salário mensal de R$2.000,00, sendo o salário hora R$9,09 e Jornada de 220:00.

Antes de executar os passos abaixo, os campos criados na aba B.E.M. foram preenchidos considerando a redução de 25% da Jornada de trabalho, com data do acordo dia 13/04/2020:

*Lançar evento de desconto complemento*

Neste caso poderá lançar um evento de desconto considerando o valor da redução. O evento de pagamento de Salário Mensal irá pagar de forma integral o salário. Assim, o módulo da Folha de Pagamento irá abater dos proventos o valor que foi reduzido.

A informação do valor no evento poderá ser feita através de Códigos Fixos, Entrada de dados, etc. ou poderá utilizar uma fórmula para calcular o valor considerando as informações do acordo preenchidos no cadastro do Funcionário.

Abaixo exemplificaremos uma sugestão de Fórmula:

Fórmula Criada a inserida no evento de desconto de dias trabalhados.

**Mensalista ou Horista**

Fórmula - Valor Reduzido para descontar do Pagamento Mensal - Funcionário Mensalista 0)
ENTAO
SETVAR (DataFimAcordo,(DataInicioProrroga + DiasProrrog));
SENAO
SE (DataCancelamento <> DATANULA)
ENTAO
SETVAR (DataFimAcordo,DataCancelamento);
SENAO
SE (DataAntecipacao <> DATANULA)
ENTAO
SETVAR (DataFimAcordo,(DataAntecipacao + 1));
FIMSE;
FIMSE;
FIMSE;
/\*Verifica se é o mesmo acordo e teve antecipação, prorrogação ou cancelamento no seguinte \*/
SE ((DataInicioAcordo = DataInicioAcordoAnt) E ((DataAntecipacao = DATANULA) OU (DiasProrrog = 0) OU (DataCancelamento = DATANULA)))
ENTAO
SETVAR(ConsideraAcordo,0)
FIMSE;
/\*Considera acordo no cálculo \*/
SE (ConsideraAcordo = 1)
ENTAO
SE (DataInicioAcordo <= ULTDIAMES(MTDATA(1,MES,ANO)) E DataFimAcordo >= MTDATA(1,MES,ANO) )
ENTAO
SETVAR(DatainicioReducao,DataInicioAcordo);
SETVAR(DataFimReducao,DataFimAcordo);
/\*Atribui início redução \*/
SE (DataInicioAcordo <= MTDATA(1,MES,ANO))
ENTAO
SETVAR(DatainicioReducao,MTDATA(01,MES,ANO))
FIMSE;
/\*Atribui fim redução \*/
SE (DataFimAcordo > ULTDIAMES(MTDATA(1,MES,ANO)))
ENTAO
SETVAR(DataFimReducao,ULTDIAMES(MTDATA(1,MES,ANO)))
FIMSE;
/\* calcula dias redução no mes\*/
SE (DIADT(ULTDIAMES(MTDATA(1,MES,ANO))) = 30) OU (DIADT(ULTDIAMES(MTDATA(1,MESDT(DataInicioAcordo),ANODT(DataInicioAcordo)))) = 30)
ENTAO
SETVAR(DiasReducaoMes, SUBTRAIDATAS(DataFimReducao,DatainicioReducao)+1)
SENAO
SETVAR(DiasReducaoMes, SUBTRAIDATAS(DataFimReducao,DatainicioReducao))
FIMSE;
SETVAR(ValorReduzido,(ValorReduzido / 30) \* MIN(DiasReducaoMes,30));
/\* calcula dias redução no mês desconsiderando férias\*/
SETVAR(DiasReducaoMes,(DiasReducaoMes - DIAFERPER(DatainicioReducao,DataFimReducao)));
/\* calcula dias redução no mês desconsiderando afastamento\*/
SETVAR(DiasReducaoMes,(DiasReducaoMes - DIASAFT(DatainicioReducao,DataFimReducao,'PTO')));
/\* Soma dois períodos de redução no mês \*/
SETVAR(Valor,Valor + ValorReduzido);
SENAO 0
FIMSE;
FIMSE;
SETVAR (DataInicioAcordoAnt,DataInicioAcordo);
ATE ProxRegSQL('BEM' ) = Falso
FIMSE;
Valor;
Fórmula associada ao evento que será lançado no movimento do Funcionário.]]>

Envelope lançou o valor referente ao período que considera a Jornada reduzida:

*Diferença Salarial por Dissídio x  Redução de Jornada/Salário*

A MP 936 convertida em Lei n° 14.020 , foi criada com o objetivo de preservar o emprego e renda dos trabalhadores, garantir as atividades empresariais e laborais, e reduzir os impactos sociais da calamidade pública decorrentes ao COVID-19.

A MP com a conversão da Lei não traz a questão do dissídio retroativo, dessa forma o entendimento é que ela veio flexibilizar algumas regras trabalhistas, e devemos nos atentar o que diz o artigo 471 da CLT.

Art. 471 - Ao empregado afastado do emprego, são asseguradas, por ocasião de sua volta, todas as vantagens que, em sua ausência, tenham sido atribuídas à categoria a que pertencia na empresa.

Link Consultoria 

No produto,  a diferença salarial por dissídio será calculada considerando o salário integral.

A fórmula que calcula o valor redutor não reduzirá a jornada/salário considerando o reajuste salarial,  conforme entendimento acima.

Caso a empresa tenha interpretação jurídica diferente do exposto, poderá usar recursos de fórmulas do produto e customizar o cálculo considerando o aumento salarial no desconto redutor de jornada/salário.

Abaixo roteiro para utilização deste recurso.
