---
content_hash: 3ab7f617aed809989f08612d7e106fd3c6195ebaf61c57e3af7502ab7d650071
fetched_at: '2026-06-29T00:10:59.775928+00:00'
page_id: '615919977'
product: rm
source: tdn-rm
title: MP 1046 - Pagamento de 1/3 de Férias, abono pecuniário e 1/3 de abono pecuniário
  na Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=615919977
version: 15
---

Conforme a MP 1046, Art. 10, na hipótese de dispensa do empregado, o empregador pagará, juntamente com o pagamento dos haveres rescisórios, os valores ainda não adimplidos relativos às férias.

No TOTVS Folha de Pagamento, quando as férias são finalizadas, o período é fechado e é aberto um novo período aquisitivo. O cálculo das verbas rescisórias verifica somente o período aquisitivo de férias aberto para calcular as férias proporcionais e/ou indenizadas.

Para atender a MP, orientamos fazer o lançamento do evento calculado por fórmula na rescisão se os mesmos forem devidos, usando uma das opções: Entrada de movimento, Grupo de eventos, Código Fixos, Eventos Programados, Incluir no Envelope de Pagamento, Importação de Movimento ou inserir nos Eventos Adicionais no parametrizador.

Considerando o cenário, onde o funcionário teve as férias de 2021 e 2022 concedidas, sem o pagamento de 1/3 de férias e de 1/3 de abono pecuniário. 

No período vencido, o funcionário tinha 30 dias de direto, porém vendeu 10 dias. O mesmo foi concedido em Maio/2021 com pagamento em Junho/2021. Os eventos de Base de 1/3 de Férias, Base de abono pecuniário e 1/3 de Abono pecuniário foram lançados no recibo e envelope de pagamento:

Após a finalização das férias concedidas acima foi criado um novo período aquisitivo de férias entre 01/09/2020 a 31/08/2021. Este período foi antecipado concedendo ao empregado 30 dias de férias, na competência de Junho/2021 com pagamento para 07/07/2021 sem o pagamento do 1/3 de férias. Neste caso não teve o pagamento de abono. O Evento de base de 1/3 de férias foi lançado no recibo e envelope:

Ao finalizar as férias concedidas acima, foi criado um novo período aquisitivo de férias: 01/09/2021 a 31/08/2022:

Em Julho/2021 o funcionário foi demitido. O produto não irá calcular nenhuma verba de férias para o funcionário, pois o período aberto inicia em Setembro/2021.

Abaixo exemplificaremos fórmulas para calcular o adicional de férias devido.

falseObservação

Conforme o paragrafo único do Art. 10 da Medida provisória nº 1406/21, as férias antecipadas gozadas cujo período não tenha sido adquirido serão descontadas das verbas rescisórias devidas ao empregado no caso de pedido de demissão.

Desta forma entendemos que, no cenário apresentado nesta documentação, o adicional de férias do período aquisitivo 01/09/2020 a 31/08/2021 só é devido o pagamento para o funcionário que não fez o pedido de demissão, ou seja demissão diferente do tipo 4.

Com relação desconto de férias antecipadas referente a este paragrafo iremos documentar em outro link.

### **Fórmula para adicional de férias antecipado que deve ser pago de forma proporcional**

Passo 1:  Criar a consulta SQL para retornar os funcionários que tiveram as férias concedidas antecipadas. Nesta consulta é retornado somente os funcionários com o período antecipado e o evento de base de Cálculo que tem o 1/3 de férias lançado, conforme orientado no documento 

sqlConsulta SQL- Pagamento de 1/3 de Férias Proporcionais

Passo 2: Criar a fórmula abaixo que retorna os dados da consulta SQL criada no passo 1, que é referente ao valor de 1/3 de férias do período antecipado e que a data final do período aquisitivo é maior que a data de demissão:

Fórmula - Pagamento 1/3 Férias Proporcionais CHAPA
ENTAO
0
SENAO
SE TPDEMISSAO = 4
ENTAO
0
SENAO
SE FIMPERAQUIS1 > DTD E ( DATAPGTOFERIAS >= MTDATA(27,04,2021) E DATAPGTOFERIAS <= MTDATA(25,08,2021))
ENTAO
VALOREVENTO]]>

Executando a fórmula a mesma retornou o valor do evento de Base de Cálculo B099 lançado na Ficha Financeira do pagamento de férias antecipadas:

Passo 3: Criar um evento de provento e associar a fórmula neste provento:

### **Fórmula para adicional de abono pecuniário antecipado que deve ser pago de forma proporcional**

Passo 1: Criar a consulta SQL para retornar o valor do 1/3 abono pecuniário de férias que não foi pago nas férias proporcionais. Nesta consulta é retornado somente os funcionários com o período antecipado e o evento de base de Cálculo que tem o 1/3 abono pecuniário de férias lançado, conforme orientado no documento 

sqlConsulta SQL- Pagamento de 1/3 de Abono de Férias Proporcionais

Passo 2: Criar a fórmula abaixo que retorna os dados da consulta SQL criada no passo 1, que é referente ao valor de 1/3 de abono pecuniário de férias do período antecipado e que a data final do período aquisitivo é maior que a data de demissão:

Fórmula - Pagamento 1/3 de Abono de Férias Proporcionais CHAPA
ENTAO
0
SENAO
SE TPDEMISSAO = 4
ENTAO
0
SENAO
SE FIMPERAQUIS1 > DTD E ( DATAPGTOFERIAS >= MTDATA(27,04,2021) E DATAPGTOFERIAS <= MTDATA(25,08,2021))
ENTAO
VALOREVENTO
]]>

Passo 3: Criar um evento de provento e associar a fórmula neste provento:

### **Fórmula para adicional de abono pecuniário antecipado que deve ser pago de forma proporcional**

Passo 1: Criar a consulta SQL para retornar o valor do abono pecuniário de férias que não foi pago nas férias proporcionais. Nesta consulta é retornado somente os funcionários com o período antecipado e o evento de base de Cálculo que tem o abono pecuniário de férias lançado, conforme orientado no documento 

sqlConsulta SQL- Pagamento de Abono de Férias Proporcionais

Passo 2: Criar a fórmula abaixo que retorna os dados da consulta SQL criada no passo 1, que é referente ao valor de abono pecuniário de férias do período antecipado e que a data final do período aquisitivo é maior que a data de demissão:

Fórmula - Pagamento 1/3 de Abono de Férias Proporcionais CHAPA
ENTAO
0
SENAO
SE TPDEMISSAO = 4
ENTAO
0
SENAO
SE FIMPERAQUIS1 > DTD E ( DATAPGTOFERIAS >= MTDATA(27,04,2021) E DATAPGTOFERIAS <= MTDATA(25,08,2021))
ENTAO
VALOREVENTO]]>

### 

Passo 3: Criar um evento de provento e associar a fórmula neste provento:

### **Fórmula para adicional de férias antecipado que deve ser pago de forma indenizadas**

Passo 1:  Criar a consulta SQL para retornar os funcionários que tiveram as férias concedidas antecipadas. Nesta consulta é retornado somente os funcionários com o período vencido e o evento de base de Cálculo que tem o ⅓ de férias lançado, conforme orientado no documento 

sqlConsulta SQL - Pagamento de 1/3 de Férias Vencidas FIMPERAQUIS AND PFFINANC.CODEVENTO = 'B099']]>

Passo 2: Criar a fórmula abaixo que retorna os dados da consulta SQL criada no passo 1, que é referente ao valor de ⅓ de férias do período vencido e que a data final do período aquisitivo é menor que a data de demissão, ultrapassando 2 períodos vencidos:

Fórmula - Pagamento de 1/3 de Férias Vencido CHAPA
ENTAO
0
SENAO
SE (DATAINICIOFERIAS > FIMPERAQUIS1 OU FIMPERAQUIS1 > DTD) E ( DATAPGTOFERIAS >= MTDATA(27,04,2021) E DATAPGTOFERIAS <= MTDATA(25,08,2021))
ENTAO
VALOREVENTO
]]>

Executando a fórmula a mesma retornou o valor do evento de Base de Cálculo B099 lançado na Ficha Financeira do pagamento de férias Vencidas:

Passo 3: Criar um evento de provento e associar a fórmula neste provento:

### **Fórmula para adicional de abono pecuniário de férias antecipado que deve ser pago de forma indenizadas**

Passo 1:  Criar a consulta SQL para retornar os funcionários que tiveram as férias concedidas antecipadas. Nesta consulta é retornado somente os funcionários com o período vencido e o evento de base de Cálculo que tem o 1/3 de abono pecuniário de férias lançado, conforme orientado no documento 

sqlConsulta SQL - Pagamento de 1/3 de Abono de Férias Vencidas FIMPERAQUIS AND PFFINANC.CODEVENTO = 'B199']]>

Passo 2: Criar a fórmula abaixo que retorna os dados da consulta SQL criada no passo 1, que é referente ao valor de 1/3 de abono pecuniário de férias do período vencido e que a data final do período aquisitivo é menor que a data de demissão, ultrapassando 2 períodos vencidos:

Fórmula - Pagamento de 1/3 de abono pecuniário de Férias Vencido CHAPA
ENTAO
0
SENAO
SE (DATAINICIOFERIAS > FIMPERAQUIS1 OU FIMPERAQUIS1 > DTD) E ( DATAPGTOFERIAS >= MTDATA(27,04,2021) E DATAPGTOFERIAS <= MTDATA(25,08,2021))
ENTAO
VALOREVENTO
]]>

Passo 3: Criar um evento de provento e associar a fórmula neste provento:

### **Fórmula para o Abono Pecuniário de férias antecipado que deve ser pago de forma indenizadas**

Passo 1:  Criar a consulta SQL para retornar os funcionários que tiveram as férias concedidas antecipadas. Nesta consulta é retornado somente os funcionários com o período vencido e o evento de base de Cálculo que tem o ⅓ de férias lançado, conforme orientado no documento 

sqlConsulta SQL - Pagamento de Abono de Pecuniário Vencidas FIMPERAQUIS AND PFFINANC.CODEVENTO = 'B198']]>

Passo 2: Criar a fórmula abaixo que retorna os dados da consulta SQL criada no passo 1, que é referente ao valor de abono pecuniário de férias do período vencido e que a data final do período aquisitivo é menor que a data de demissão, ultrapassando 2 períodos vencidos:

Fórmula - Pagamento de abono pecuniário de Férias Vencido CHAPA
ENTAO
0
SENAO
SE (DATAINICIOFERIAS > FIMPERAQUIS1 OU FIMPERAQUIS1 > DTD) E ( DATAPGTOFERIAS >= MTDATA(27,04,2021) E DATAPGTOFERIAS <= MTDATA(25,08,2021))
ENTAO
VALOREVENTO
]]>

Passo 3: Criar um evento de provento e associar a fórmula neste provento:

***Calculando rescisão***

Funcionário com tipo de demissão 2 - Iniciativa do empregador

Quando executar o cálculo da rescisão inserindo o evento em algumas daquelas entradas sugeridas, os eventos serão lançados conforme o retorno das fórmulas acima:

Funcionário com tipo de demissão 4 - Iniciativa do empregado

Quando executar o cálculo da rescisão inserindo o evento em algumas daquelas entradas sugeridas, o evento de 1/3 de férias proporcionais (referente ao 2º período de gozo exemplificado acima) que era devido, não é lançado. Este tratamento foi feito pois o período aquisitivo ainda não foi adquirido, logo entendemos que conforma a publicação da MP, o mesmo não precisa ser pago:
