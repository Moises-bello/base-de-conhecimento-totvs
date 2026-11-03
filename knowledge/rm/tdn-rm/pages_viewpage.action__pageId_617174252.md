---
content_hash: f668774a5d005c52a50dd962a6bbc6c073d72e4c9ce1ef7a65d26ba6b45feac9
fetched_at: '2026-06-29T00:11:02.412284+00:00'
page_id: '617174252'
product: rm
source: tdn-rm
title: MP 1045 - Benefício Emergencial de Manutenção do Emprego e da Renda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=617174252
version: 27
---

Conforme a Medida Provisória 1045, para que o funcionário tenha direito ao recebimento do Benefício Emergencial Mensal (B.E.M.), caberá o empregador informar o Ministério da Economia a redução da jornada de trabalho e de salário, ou a suspensão temporária do contrato de trabalho, no prazo de dez dias a contar da data do acordo individual ou coletivo.

O B.E.M será pago quando houver acordos entre trabalhadores e empregadores nas situações de redução proporcional de jornada de trabalho e de salário e/ou suspensão temporária do contrato de trabalho.

O Benefício Emergencial de Manutenção do Emprego e da Renda será pago ao empregado independentemente do:

I - cumprimento de qualquer período aquisitivo;

II - tempo de vínculo empregatício; e

III - número de salários recebidos.

IV - O empregado com mais de um vínculo formal de emprego poderá receber cumulativamente um Benefício Emergencial de Manutenção do Emprego e da Renda para cada vínculo com redução proporcional de jornada de trabalho e de salário ou com suspensão temporária do contrato de trabalho.

O Benefício Emergencial de Manutenção do Emprego e da Renda não será devido ao empregado que esteja:

I - ocupando cargo ou emprego público ou cargo em comissão de livre nomeação e exoneração ou seja titular de mandato eletivo; ou

II - em gozo:

a) de benefício de prestação continuada do Regime Geral de Previdência Social ou dos regimes próprios de previdência social, ressalvado o disposto no parágrafo único do [art. 124 da Lei nº 8.213, de 24 de julho de 1991](http://www.planalto.gov.br/ccivil_03/leis/L8213compilado.htm);

b) do seguro-desemprego, em quaisquer de suas modalidades; ou

c) do benefício de qualificação profissional de que trata o [art. 2º-A da Lei nº 7.998, de 1990](http://www.planalto.gov.br/ccivil_03/leis/L7998compilado.htm).

III - O empregado com contrato de trabalho intermitente a que se refere o [§ 3º do art. 443](http://www.planalto.gov.br/ccivil_03/decreto-lei/Del5452compilado.htm) da Consolidação das Leis do Trabalho, aprovada pelo [Decreto-Lei nº 5.452, de 1943](http://www.planalto.gov.br/ccivil_03/decreto-lei/Del5452compilado.htm), não faz jus ao Benefício Emergencial de Manutenção do Emprego e da Renda.

## **Adequação no módulo TOTVS Folha de****Pagamento**

O intuito deste documento é apresentar alternativas no produto aderentes aos procedimentos que nossos usuários adotarem acerca dos funcionários que têm direito ao Benefício.

Abaixo, detalhamos, as possibilidades de processamento para envio de novos acordos, prorrogação, cancelamentos, antecipação ou retificação de dados enviados.

**Cadastro de Funcionários - B.E.M**

Para o registro dos dados do acordo disponibilizamos os campos discriminados abaixo no Cadastro de Funcionários, menu Registro, aba B.E.M., que devem ser preenchidos com as informações da Redução de Jornada e Salário ou Suspensão de Contrato de Trabalho conforme acordado com o funcionário para que os mesmos sejam considerados nos arquivos do B.E.M.

Campos:

*Tipo de adesão*: Informe se a adesão será redução de Jornada ou Suspensão de Contrato

*Data da Mudança*: Por default o sistema retorna a data atual, porém é possível alterar a data da mudança quando estiver fazendo a edição de qualquer campo. Esta data de mudança é para fins de histórico não sendo considerada no arquivo do B.E.M. 

*Data do acordo*: Irá receber a data do acordo da redução Jornada/Salário, corresponde ao início do período de redução de salário e jornada. Esta data que é informada no arquivo do B.E.M.

*Percentual de redução de Jornada*: Irá receber o percentual utilizado para redução de Jornada/Salário, podendo ser 25%, 50% ou 70%. Para o tipo de adesão 'Suspensão de Contrato' este campo não deve ser preenchido, conforme a orientação do manual. 

*Valor reduzido*:  Irá receber o valor reduzido do salário.

Exemplo: funcionário com Salário de 2000,00 e teve a redução de 25%. Este campo deve ser preenchido com 500,00

Este valor não é levado para o arquivo do B.E.M., porém, é utilizado internamente para fins de cálculo de desconto de complemento orientado neste [link](https://tdn.totvs.com/pages/viewpage.action?pageId=545621517). Para suspensão de contrato não há necessidade de preencher este campo. 

*Dias de duração do acordo*: Irá receber a quantidade de dias que irá durar a Redução de Jornada ou Suspensão de Contrato. Este campo não limita a quantidade estabelecida na MP, ficando a cargo do usuário observar as regras para preenche-lo. 

*Data da Antecipação*: Irá receber a data de antecipação do término do contrato entre o empregado e a empresa. 

*Dias de Prorrogação*: Irá receber a quantidade de dias em que será prorrogado o contrato acordado entre o empregado e empresa. Este campo não limita a quantidade estabelecida na MP, ficando a cargo do usuário observar as regras para preenchê-lo, de acordo com a legislação vigente.

*Data Prorrogação BEM*: Este campo deve ser preenchido com a data início da prorrogação, a cada prorrogação feita.

Exemplo: Acordo celebrado dia 03/05/2021, com 30 dias de duração

Em Junho é feito uma prorrogação deste acordo com mais 30 dias de duração, então no campo Dias de Prorrogação será preenchido com 30 e no campo Data Prorrogação com 01/06/2021

Em Julho é feita uma segunda prorrogação do mesmo acordo por mais 30 dias de duração. Neste caso, como o campo Dias de Prorrogação já está preenchido, então só é necessário alterar a data de Prorrogação para o dia 01/07/2021.

Este campo não é levado para o B.E.M., porém foi necessário cria-lo para que, conforme o exemplo acima, fosse inserido no histórico do B.E.M. o registro referente a segunda prorrogação, uma vez que os dados da segunda prorrogação são os mesmos da primeira prorrogação, não havendo assim edição de nenhum campo, e em consequência não habilitando a data de mudança que permite inserir um novo registro no histórico do B.E.M.

*Data do Cancelamento*: Irá receber a data de cancelamento do acordo do contrato acordado entre o empregado e a empresa.

No Cadastro de Funcionários foi feito a adequação para retornar mensagem de validação para funcionários não elegíveis. Esta validação Verificar as seguintes situações:

* Funcionário com data de admissão maior ou igual a 28/04/2020
* Funcionário com afastamento diferente de 'T' ou 'C'
* Funcionário em período de gozo de Férias
* Funcionário com data de acordo maior igual que a data de demissão

Abaixo iremos mostrar um exemplo de um funcionário admitido no dia 03/05/2021 e teve o acordo do B.E.M para o dia 17/05/2021:

Na aba B.E.M foi preenchido a data de acordo. Ao clicar em Salvar, retorna a mensagem abaixo:

falseObservação

* O Ajuste da mensagem está disponível a partir dos patchs:

  + 12.1.29.249
  + 12.1.31.154
  + 12.1.32.100

* Clicando em 'Sim' na mensagem acima, o cadastro não é salvo. Clicando em 'Não', o cadastro é salvo. A validação retorna a mensagem para o usuário verificar os dados antes de salvar. Caso o mesmo queira salvar mesmo com o aviso, o módulo Folha de Pagamento não impedirá
* Utilizando o processo de Alteração Global de Campos do Cadastro, será retornado um log de aviso para os casos validados para funcionários elegíveis conforme especificado acima. O cadastro será alterado, mesmo se o funcionário não for elegível

**Alteração Global Campos do Cadastro**

Os campos acima podem ser preenchidos de forma global, através do processo de Alteração Global de Cadastro, usando fórmulas. Abaixo exemplificaremos algumas sugestões de fórmulas, porém as mesmas devem ser desenvolvidas/adaptadas pelo usuário de forma a atender a sua necessidade:

Data da mudança: Deverá ser informada ao executar a alteração global de dados do funcionário ou preenchida manualmente.

Tipo de adesão:

* Fórmula: **1 /\* TIPO DE ADESÃO  1 - REDUÇÃO DE JORNADA ACORDADO ENTRE EMPREGADO E EMPRESA\*/**
* Fórmula: **0 /\* TIPO DE ADESÃO  0 - SUSPENSÃO DE CONTRATO DE TRABALHO ACORDADO ENTRE EMPREGADO E EMPRESA\*/**

Data do acordo:

* Fórmula:  **"17/05/2021" /\*INFORME UMA DATA REDUÇÃO JORNADA ACORDADO ENTRE EMPREGADO E EMPRESA\*/**

Percentual de Redução da Jornada:

* Fórmula: **25,00 /\*INFORME O PERCENTUAL DE REDUÇÃO JORNADA ACORDADO ENTRE EMPREGADO E EMPRESA\*/**

Dias de duração do acordo:

* Fórmula: **30 /\*TEMPO DE DURAÇÃO DA REDUÇÃO DE CONTRATO ACORDADO ENTRE EMPREGADO E EMPRESA\*/**

Valor Reduzido:  Exemplo de fórmula para redução de jornada/salário em até 25%. Para demais reduções deverá ser adequado para contemplar o percentual. A fórmula respeita a redução não deixando o salário pago no mês menor que o salário mínimo

* Fórmula:

Fórmula - Valor reduzido Salário

Data da Antecipação:

* Fórmula:  **"26/06/2021" /\* INFORME UMA DATA DE ANTECIPAÇÃO DO TÉRMINO DO CONTRATO ACORDADO ENTRE EMPREGADO E EMPRESA \*/**

Data do Cancelamento:

* Fórmula:  **"26/06/2021" /\* INFORME A DATA DE CANCELAMENTO DO CONTRATO ACORDADO ENTRE EMPREGADO E EMPRESA \*/**

Dias de Prorrogação:

* Fórmula:  **30 /\* QUANTIDADE DE DIAS DE PRORROGAÇÃO DO CONTRATO ACORDADO ENTRE EMPREGADO E EMPRESA \*/**

Importante

**O processo de Alteração Global irá preencher e/ou editar apenas os campos selecionados e preenchidos na tela. Para inclusão de registro favor selecionar filtro apenas de funcionários que não tiverem adesão ao B.E.M. Para edição de registro, selecione filtro apenas de funcionários que já aderiram ao B.E.M.**

**Histórico**

Quando é feito o preenchimento dos campos acima, seja direto no Cadastro de Funcionário ou pelo processo Alteração Global de Campos do Cadastro, o sistema armazena a cada alteração de qualquer campo da aba B.E.M. um registro no histórico de Adesão ao Benefício Extraordinário Mensal B.E.M. Caso a data de mudança seja a mesma de um registro já existente, será feito somente a atualização dos dados, mesmo se o tipo de acordo, data do acordo sejam o mesmo.

Este histórico é necessário estar preenchido corretamente para os devidos cálculos referente a MP 1045, como o desconto do complemento da redução de Jornada, dias de estabilidade, verba indenizatória, etc.

## **Geração do arquivo do B.E.M**

**Gerador de Saídas**

Para atender esta demanda, disponibilizamos o FOPLAY0085 - Layout B.E.M (versao Oficial).TotvsGen conforme a [especificação](https://sd.mte.gov.br/sdweb/validador/Manual_EmpregadorWeb_BEM.pdf) do Ministério da Economia e do Trabalho,  que deve ser gerado pelo Recurso Gerador de Saídas. 

Para fazer a importação deve acessar Gestão | Gerador de Saídas | Processo | Importar Layout.

Após a importação, para gerar o arquivo deve selecionar o layout, ir em Processo | Geração de Saídas. O processo irá abrir a tela abaixo. Nesta tela poderá alterar o caminho onde deseja que o relatório seja armazenado após a geração. Ao avançar, irá apresentar a tela abaixo com os parâmetros que devem ser preenchidos pelo usuário:

* *Formula para Remuneração (Último)*: Neste campo deve informar a última remuneração do funcionário. O mesmo deve ser retornado através de fórmula. Conforme o layout este campo é de preenchimento obrigatório.
  + Exemplo de Fórmula para informação do último salário. Nesta fórmula retorna o salário contratual somando com os valores eventos pagos de outras verbas, como hora-extra, gratificação:

Fórmula - Retorna a Ultima Remuneração 0 ENTAO
RC + (MV(MES,ANO,'0084')+MV(MES,ANO,'0083')+MV(MES,ANO,'0082'))
SENAO
ACUMFF(MES,ANO,'03')
FIMSE]]>

* *Formula para Remuneração (Penúltimo)*: Neste campo deve informar a penúltima remuneração do funcionário. O mesmo deve ser retornado através de fórmula.
  + Exemplo de Fórmula para informação do penúltimo salário. Nesta fórmula retorna o salário contratual somando com os valores eventos pagos de outras verbas, como hora-extra, gratificação:

Fórmula - Penúltimo Salário 0
ENTAO SAL
SENAO SE ACUMFF(MM,AA,'4')> 0
ENTAO ACUMFF(MM,AA,'4')
SENAO ''
FIMSE]]>

* *Formula para Remuneração (Antepenúltima)*: Neste campo deve informar a antepenúltima remuneração do funcionário. O mesmo deve ser retornado através de fórmula.
  + Exemplo de Fórmula para informação do antepenúltimo salário. Nesta fórmula retorna o salário contratual somando com os valores eventos pagos de outras verbas, como hora-extra, gratificação:

Fórmula - Antepenúltimo Salário 0
ENTAO SAL
SENAO
SE ACUMFF(MM,AA,'4')> 0
ENTAO ACUMFF(MM,AA,'4')
SENAO ''
FIMSE]]>

* *Filtro do Usuário:* Neste campo é permitido fazer filtros dos funcionários que serão contemplados neste relatório.

Após preencher os campos, e executar o processo, irá retornar o arquivo gerado conforme abaixo:

 

O arquivo gerado no diretório informado em formato .txt:

Conforme a especificação do Layout, o sistema do Empregador Web ao qual o arquivo deve ser importado só aceita arquivos na extensão .csv. Desta forma, para alterar a extensão do arquivo, deve proceder conforma abaixo:

Passo 1: Abrir o arquivo no bloco de notas, ir em arquivo e salvar como:

Passo 2: Após clicar em 'Salvar como' irá abrir a tela abaixo. Deve mudar o Tipo Documento para Todos os arquivos (\*.\*)  e a o nome alterar, mudando .txt para .csv:

 

Após salvar, o arquivo será apresentado conforme abaixo:

Após a alteração, o arquivo pode ser validado neste [link](https://sd.maisemprego.mte.gov.br/sdweb/validador/validadorReqEmergencial.jsf) disponibilizado pelo Empregador Web:

## **Cancelamento, Redução ou Prorrogação (Manual de Leiaute do Arquivo B.E.M  - Versão 3.0)**

Para atender aos layouts disponibilizados na [especificação](https://sd.mte.gov.br/sdweb/validador/Manual_EmpregadorWeb_BEM.pdf) do Ministério da Economia e do Trabalho,  foram criados três NOVOS relatórios que deve ser gerado pelo Recurso Gerador de Saídas, que são:

* Antecipação/Redução:
* Prorrogação:
* Cancelamento:

**Gerador de Saídas -****Cancelamento, Redução ou Prorrogação**

Para fazer a importação deve acessar Gestão | Gerador de Saídas | Processo | Importar Layout

Após a importação, para gerar o arquivo deve selecionar o layout desejado, ir em Processo | Geração de Saídas. O processo irá abrir a tela abaixo. Nesta tela poderá alterar o caminho onde deseja que o relatório seja armazenado após a geração:

**Antecipação ou Redução**

Ao avançar, irá apresentar a tela abaixo com os parâmetros da geração, que devem ser preenchidos pelo usuário:

No nosso exemplo, selecionei o arquivo Layout B.E.M Antecipacao.TotvsGen, então vou filtrar, utilizando o 'Filtro do Usuário', criando o filtro com o campo 'Data da Antecipação' = '26/06/2020':

O arquivo gerado no diretório informado em formato .txt:

Conforme a especificação do Layout, o sistema do Empregador Web ao qual o arquivo deve ser importado só aceita arquivos na extensão .csv. Desta forma, para alterar a extensão do arquivo, deve proceder conforma abaixo:

Abrir o arquivo no bloco de notas, ir em arquivo e salvar como e em seguida mudar o Tipo Documento para Todos os arquivos (\*.\*)  e a o nome alterar, mudando .txt para .csv:

Após salvar, o arquivo será apresentado conforme abaixo:

Após a alteração, o arquivo pode ser validado neste [link](https://sd.maisemprego.mte.gov.br/sdweb/validador/validadorReqEmergencial.jsf) disponibilizado pelo Empregador Web. Para validar a opção de antecipação do término do contrato, deverá ser selecionada a opção 'Redução' no validador.

**Prorrogação**

Ao avançar, irá apresentar a tela abaixo com os parâmetros da geração, que devem ser preenchidos pelo usuário:

No nosso exemplo, selecionei o arquivo Layout B.E.M Prorrogação.TotvsGen, então vou filtrar utilizando o 'Filtro do Usuário', criando o filtro com o campo 'Dias de Prorrogação' = '30':

O arquivo gerado no diretório informado em formato .txt:

Conforme a especificação do Layout, o sistema do Empregador Web ao qual o arquivo deve ser importado só aceita arquivos na extensão .csv. Desta forma, para alterar a extensão do arquivo, deve proceder conforma abaixo:

Abrir o arquivo no bloco de notas, ir em arquivo e salvar como e em seguida mudar o Tipo Documento para Todos os arquivos (\*.\*)  e a o nome alterar, mudando .txt para .csv:

Após salvar, o arquivo será apresentado conforme abaixo:

Após a alteração, o arquivo pode ser validado neste [link](https://sd.maisemprego.mte.gov.br/sdweb/validador/validadorReqEmergencial.jsf) disponibilizado pelo Empregador Web. Para validar a opção de antecipação do término do contrato, deverá ser selecionada a opção 'Prorrogação' no validador:

**Cancelamento**

Ao avançar, irá apresentar a tela abaixo com os parâmetros da geração, que devem ser preenchidos pelo usuário:

No nosso exemplo, selecionei o arquivo Layout B.E.M Cancelamento.TotvsGen, então vou filtrar, utilizando o 'Filtro do Usuário', criando o filtro com o campo 'Data do Cancelamento' = '26/06/2020':

O arquivo gerado no diretório informado em formato .txt:

Conforme a especificação do Layout, o sistema do Empregador Web ao qual o arquivo deve ser importado só aceita arquivos na extensão .csv. Desta forma, para alterar a extensão do arquivo, deve proceder conforma abaixo:

Abrir o arquivo no bloco de notas, ir em arquivo e salvar como e em seguida mudar o Tipo Documento para Todos os arquivos (\*.\*)  e a o nome alterar, mudando .txt para .csv:

Após salvar, o arquivo será apresentado conforme abaixo:

Após a alteração, o arquivo pode ser validado neste [link](https://sd.maisemprego.mte.gov.br/sdweb/validador/validadorReqEmergencial.jsf) disponibilizado pelo Empregador Web. Para validar a opção de antecipação do término do contrato, deverá ser selecionada a opção 'Cancelamento' no validador:

**Considerações para Geração do Arquivo**

*Conta bancária*

Importante

Trabalhador pode indicar ao empregador uma conta corrente, ou conta poupança, em que seja o titular. O BEM não será pago em contas de terceiros. Na hipótese de não validação ou de rejeição do crédito na conta indicada, a Caixa Econômica Federal e o Banco do Brasil S.A. poderão utilizar outra conta poupança de titularidade do beneficiário, identificada por meio de processo de levantamento e conferência da coincidência de dados cadastrais para o pagamento do benefício emergencial. Na hipótese de não ser localizada conta poupança de titularidade do beneficiário, **o pagamento será feito em uma conta digital aberta pelo Ministério da Economia**, em nome do trabalhador, junto ao Banco do Brasil ou à Caixa Econômica.

Conforme o manual do B.E.M., o preenchimento dos dados da conta Bancário é opcional.

O relatório B.E.M. irá considerar os dados bancários existentes no cadastro do Funcionário, conforme print abaixo. Para os casos em que a conta do funcionário for do tipo salário, ou seja, uma conta não aceita pelo Ministério da Economia, o relatório não irá desconsiderar esta conta, enviando as informações de conta para pagamento para o arquivo.

 Caso não queira que a conta não seja levado para o arquivo, foi disponibilizado um recurso para 'desmarcar' a informação Tipo de conta bancária:

*Usando consulta SQL para gerar o arquivo*

Passo 1: Criar uma consulta SQL que retorna as chapas contempladas para na adesão do BEM. No exemplo abaixo selecionamos as chapas não considerando algumas situações, data de admissão após a data da publicação da MP e se o mesmo é aposentado ou tem contrato intermitente:

 

Passo 2: No Filtro do BEm, selecionar o campo Chapa do Funcionário, o operador IN (SQL) e a consulta SQL criada acima. Ao executar o processo será considerado somente a chapas da consulta:

sqlSeleção de Funcionário - BEm '28/04/2021']]>

*Usando Campos do Filtro*

Passo 1: Criar um filtro usando os campos disponíveis no recurso de Filtros. No exemplo abaixo usei os campos Data de admissão, data de acordo, Contrato intermitente e situação. Ao executar o processo será considerado somente a chapas retornadas pelo filtro criado.

**Observações:**

**Para primeiro registro de acordo não enviado para o governo:**

Caso necessite de edição realizada no cadastro do acordo poderá ser informada a data de mudança do primeiro registro do acordo. Com isso, não será criado um novo registro. Consequentemente os campos atualizados serão: Tipo de Adesão, Valor Reduzido, Data de Acordo, Percentual de Jornada e/ou Dias de Duração de Acordo.

**Para registros já enviado para o governo:**

Para cada registro de edição realizada no cadastro do acordo é extremamente necessário que seja informada uma nova data de mudança para o registro no histórico. Para que assim seja criado um novo registro no histórico. Consequentemente os campos atualizados serão: Dias de Prorrogação,  Data do Cancelamento ou Data de Antecipação.

**Para registro de Cancelamento, Antecipação ou Prorrogação não enviado para o governo:**

Para cada registro de edição realizada no cadastro do acordo, poderá ser utilizada a mesma data do ultimo registro cadastrado. Assim o ultimo registro será editado e não criará um novo. Consequentemente os campos atualizados serão: Dias de Prorrogação,  Data do Cancelamento ou Data de Antecipação.

**Cancelamento de Aviso Prévio**

A MP 1045, o empregador e empregado, em comum acordo, poderão optar pelo cancelamento do aviso prévio em curso. O TOTVS folha de pagamento possuí o processo para cancelar o aviso prévio. Caso a rescisão já esteja cadastrada, deverá cancelar a rescisão antes do cancelamento do aviso prévio.  Mais informações: [Aviso Prévio - Cancelamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026073953-RM-FOP-Aviso-Pr%C3%A9vio-Cancelamento)

Com relação ao eSocial, o envio do evento S-2250 passou a ser opcional a partir da [NT19/2019](https://tdn.totvs.com/pages/releaseview.action?pageId=521127413)

falseImportante

**eSocial**

Conforme a orientação do eSocial, o empregador deverá enviar um evento de alteração contratual (S-2206) com Data de Alteração igual ao início do período de redução de salário e jornada e, neste evento, informar o valor do salário reduzido e a nova jornada a ser cumprida pelo trabalhador durante esse período.

No campo observação deverá informar o prazo pactuado para a referida redução e o percentual definido para essa redução proporcional. Mais informações sobre a geração do evento S-2206 [acesse aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=556391463)
