---
content_hash: a338ec416d7513a24014341a075457863c8dcbd763ace11de377876a35dcb5d5
fetched_at: '2026-06-29T00:10:38.914868+00:00'
page_id: '545621865'
product: rm
source: tdn-rm
title: MP 936 - Suspensão temporária do contrato de trabalho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=545621865
version: 22
---

Durante esse período, o empregador poderá acordar a suspensão temporária do contrato de trabalho de seus empregados, pelo prazo de 60 dias, que poderá ser fracionado em até dois períodos de 30 dias.

As empresas que tiver auferido, no ano calendário de 2019, receita bruta superior a R$ 4.800.000,00 (quatro milhões e oitocentos mil reais), somente poderá suspender o contrato de seus funcionários, mediante o pagamento de ajuda compensatória mensal no valor de 30% do valor do salário do empregado, durante o período da suspensão temporária de trabalho pactuado.

Relacionado a suspensão do contrato de trabalho do funcionário, ainda não houveram nenhum pronunciamento por parte do SEFIP, referente a qual tipo de afastamento utilizar, portanto, conforme novidades por parte dos sistemas governamentais, a documentação poderá ter alterações.

O Módulo TOTVS Folha de Pagamento permite fazer a suspensão do contrato através do cadastro do Funcionário no campo Situação. Temos os afastamentos do tipo: “**C - Contrato de Trabalho Suspenso**”.

**Afastamento do Tipo** **“C - Contrato de Trabalho Suspenso”**

Informar 'C' no campo situação e no campo Data da Mudança, informe a data de início do afastamento. Após clicar em **Salvar,** através do Histórico de Afastamento, poderá ser informado a Data Fim da suspensão, No exemplo exposto, foi informado a data 15/04/2020 e fim do afastamento dia 13/06/2020.

 

***Atenção***

Quando utilizado o afastamento do tipo **C – Contrato de Trabalho Suspenso**, o produto não irá estender a Data Limite do Período de Gozo. Conforme exemplo abaixo:

**Competência:** 04/2020  
**Período Aquisitivo Aberto:** 03/06/2018 à 02/06/2019  
**Data Limite para início das Férias:** 03/05/2020  
**Afastamento:** 15/04/2020 à 13/06/2020

Funcionário retornará da suspensão em 14/06/2020, ao marcar as Férias para a partir do dia 14/06, o produto vai automaticamente **pagar férias em dobro**, pois a data limite de início era 03/05/2020.

Quando a rotina de acerta período aquisitivo for executada, como houveram dias de afastamento suspenso, o produto criará um novo Período Aquisitivo Futuro e ficará fechado enquanto o anterior não for finalizado, neste novo Período Aquisitivo, o produto somará na data fim, a quantidade de dias de afastamento por suspensão. Seguindo o cenário de exemplo anterior, ao executar o Acerta Período Aquisitivo, ficará da seguinte forma:

**Parametrizando para a Suspensão Temporária manter o período aquisitivo de férias e os avos do 13º salário**

Marcando esses parâmetros e informando o motivo de afastamento que será utilizado no afastamento do funcionário, serão mantidos o cálculo do período aquisitivo de férias e os avos de direito ao 13º salário para o período afastado pelo motivo C – Contrato Suspensão.

**Exemplo:** Mês competência 05/2020 – Parâmetros marcados e motivo preenchido com 1 – Com perda de avos

Funcionário 1 – Período aquisitivo de 02/01/2020 a 01/01/2021 – Afastamento de 01/03/2020 a 29/04/2020 – 60 dias - Motivo de afastamento 1 – Com perda de avos

Funcionário 2 – Período aquisitivo de 02/01/2020 a 01/01/2021 – Afastamento de 01/03/2020 a 29/04/2020 – 60 dias - Motivo de afastamento 2 – Sem perda de avos

Executando o acerto de período aquisitivo:

Funcionário 1 – Período aquisitivo de 02/01/2020 a 02/03/2021 – Período estendido porque o motivo de afastamento era o mesmo do parametrizador.

Funcionário 2 – Período aquisitivo de 02/01/2020 a 01/01/2021 – Período não foi estendido porque o motivo de afastamento não era o mesmo do parametrizador.

Calculando 13º salário em dezembro/2020:

Funcionário 1 – 10 avos – Perda de 2 avos porque o motivo de afastamento era o mesmo do parametrizador.

Funcionário 2 – 12 avos – Avos completos porque o motivo de afastamento não era o mesmo do parametrizador.

Para a rescisão contratual deverá ser executado o acerto de período aquisitivo primeiro pois assim o período aquisitivo estará correto no momento do cálculo. E o cálculo do 13º salário rescisão seguirá do mesmo jeito do 13º salário normal.

**Realizar a Suspensão Temporária de forma Global**

O processo também poderá ser realizado de forma Global (vários funcionários de uma vez), basta acessar Administrador de Pessoal / Alteração Campos do Cadastro:

* Em seleção de funcionários, informe via filtros os funcionários que terão suspensão.
* Dados a serem alterados altere para: Funcionários
* O campo Data de Mudança: Informe a data de início do afastamento.
* Campos Disponíveis: informe Código da Situação – COSITUACAO
* No campo do lado direito, deverá informar uma Fórmula, o conteúdo dessa fórmula deverá retornar a nova situação do funcionário, portanto se retornar “C”, será cadastrado o afastamento **Contrato de Trabalho Suspenso.**

*Exemplo*

Criar a fórmula com código do afastamento. Deverá inserir o código com aspas simples.  Após execução da rotina, alterado o cadastro do funcionário inserindo as informações no cadastro de Histórico de Situação e Histórico de Afastamento.

 

**Observação:** Para alimentar a Data Fim do Afastamento de forma global, basta executar o mesmo procedimento novamente, informando no campo “Data de Mudança” a “data de retorno” do funcionário na Empresa e na fórmula, passar no conteúdo: ‘A’, porém esse procedimento deverá ser executado no mês de retorno do funcionário.

**Pagamentos**

Para Empresas com renda bruta superior a R$ 4,8 milhões em 2019, deverão realizar o pagamento da ajuda compensatória no valor de 30% do salário, para realizar esse procedimento via Produto, **seguem sugestões**:

Criar uma fórmula, que calcula a ajuda de custo e associar a um evento para ser lançado para o envelope de pagamento do funcionário suspenso:

No exemplo do teste da Fórmula, temos o funcionário nesse cenário:

**Salário:** 1500,00  
**Afastamento:** 15/04/2020 à 13/06/2020  
**Competência:** 04

* Fórmula de Valor: (((RC/30)\***DIASAFT**(**MTDATA** (01, MES, ANO),**MTDATA** (31, MES, ANO),'C')\*0.3))

Como foram 16 dias afastado no mês 04, a Fórmula irá encontrar o salário dia, multiplicar por 16 dias e proporcionalizar para 30%, então:

(1500/30) = 50 Salário dia

50 \* 16 (Dias Suspenso) = 800

800 \* 30% = **R$240,00**

* Fórmula de Referência: **DIASAFT**(**MTDATA** (01, MES, ANO),**MTDATA** (31, MES, ANO),'C')

Objetivo dessa fórmula, é referenciar no envelope, a quantidade de dias afastado, cenário de exemplo do funcionário. O retorno de 16 dias de suspensão relacionado ao afastamento do tipo **C - Contrato de Trabalho Suspenso.**

**Afastamento:** 15/04/2020 à 13/06/2020  
**Competência:** 04

 

Fazer o lançamento do evento para o envelope de pagamento do funcionário suspenso:

**Observações**

* Após, poderá lançar a Folha de Pagamento, pois conforme no exemplo exposto, ainda existem 14 dias trabalhados a serem lançados pelo fato do início da suspensão ter sido a partir de 15/04/2020 e benefícios, o código de cálculo 2 será calculado corretamente.
* Caso a Empresa tenha outros entendimentos, como exemplo: independente do início do afastamento, será realizado o pagamento de 30% sobre o salário, basta utilizar a fórmula RC\*0.30, frisamos que conforme a falta de detalhes na MP, fica a cargo da Empresa.

**Histórico de Provisões**

Para o Afastamento do tipo “C na Provisão, caso o funcionário tenha mais de 15 dias afastado validando o seu Período Aquisitivo e mês competência, ele poderá perder o Avo de 13° e postergar o avo de férias, conforme maiores detalhes abaixo:

*Exemplo*

**Competência:** 03/2020  
**Período Aquisitivo Aberto:** 03/06/2018 à 02/06/2019  
  
Histórico de Provisões do mês 03/2020:

* Tem direito as Férias Vencidas
* 10 Avos Proporcionais de Férias
* 3 Avos de 13°

**Competência:** 04/2020  
**Período Aquisitivo Aberto:** 03/06/2018 à 02/06/2019  
**Incluso Afastamento:** 15/04/2020 à 13/06/2020

Histórico de Provisões do mês 04:

* Tem direito a Férias Vencidas
* 10 Avos Proporcionais de Férias (**Importante:** Conforme será demonstrado no Log de Cálculo, o produto estende a data fim do Período Aquisitivo relacionado as Férias Proporcionais, portanto a contagem desse avo será postergada).
* 3 Avos de 13° (Funcionário perdeu o avo de 13° referente ao mês 04).

**Observação:** Se para o mesmo cenário anterior, o início do afastamento fosse 20/04/2020, na Provisão seria contabilizado 4 avos de 13° e 11 Avos de Férias, pois os dias de afastamento foram inferiores a 15 dias:

**eSocial**

**Observação:**Disponível a partir das versões 12.1.25.268, 12.1.26.212, 12.1.27.166 e 12.1.28.102

***Código de Afastamento***

Para o envio correto  das informações para o eSocial deverá ser cadastrado um De/Para em: **Configurações | Parametrizador | Folha de Pagamento | eSocial | De/Para | De/Para de afastamento** com o tipo de afastamento e motivo que serão vinculados ao funcionário. Conforme exemplos citados acima.

Após a vinculação acima e o cadastro do afastamento no funcionário, o evento S-2230 - Afastamento Temporário será gerado corretamente, com o motivo 37 – Suspensão temporária do contrato de trabalho nos termos da MP 936/2020.

***Rubrica para pagamento de Ajuda de Compensatória***

Para envio da verba de ajuda compensatória foi criada a rubrica 1619 - Ajuda Compensatória – MP 936: Ajuda compensatória paga pelo empregador ao empregado durante período de suspensão do contrato de trabalho ou redução proporcional de salário e jornada. Início de validade: 01/04/2020.

falseAtenção

Para geração do arquivo do Benefício Extraordinário Mensal (BEm), é necessário preencher o cadastro conforme orientado [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=545641381), seguindo a orientação do manual para os campos obrigatórios para o tipo de adesão.
