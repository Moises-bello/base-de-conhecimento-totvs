---
content_hash: 495af695be13d1c01dfd53cd4ca97a2ec3c1de978ae0a6fe4384ce535f5a46a1
fetched_at: '2026-06-29T00:10:39.034303+00:00'
page_id: '545641381'
product: rm
source: tdn-rm
title: MP 936 - Benefício Extraordinário Mensal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=545641381
version: 66
---

Para o recebimento do Benefício Emergencial, caberá o empregador informar o Ministério da Economia a redução da jornada de trabalho e de salário, ou a suspensão temporária do contrato de trabalho, no prazo de dez dias a contar da data do acordo individual ou coletivo.

O Benefício Emergencial de Preservação do Emprego e da Renda (B.E.M.) será pago quando houver acordos entre trabalhadores e empregadores nas situações de:

* redução proporcional de jornada de trabalho e de salário;
* suspensão temporária do contrato de trabalho.

**Adequação no módulo TOTVS Folha de****Pagamento**

Importante

**Os campos e o Layout foram disponibilizados a partir dos patchs abaixo:**

* **12.1.24.305**
* **12.1.25.294**
* **12.1.26.257**
* **12.1.27.239**
* **12.1.28.148**

**É necessário executar o RM.Atualizador. exe e importar o Layout no Gerador de Saídas.**

**Portaria 10.486/20**

Foi publicada a Portaria 10.486/20 da Secretaria Especial de Previdência e Trabalho, que dispõem regras para processamento do Programa de Emergencial de Manutenção e da Renda, instituído pela medida provisória 936/20.  
Esta Portaria traz clareza a diversos pontos da MP, porém não há orientação clara em termos operacionais de como agir, principalmente em acordos já enviados ao Governo.  
Desta forma, o intuito deste documento é apresentar alternativas, para que o produto seja aderente aos procedimentos que nossos usuários adotarem, principalmente  em relação ao 4º artigo da referida Portaria, que discorre acerca dos trabalhadores que têm direito ao Benefício.

Art. 4º O BEm não será devido ao empregado com redução proporcional de jornada e de salário ou suspensão do contrato de trabalho que:

I - também esteja ocupando cargo ou emprego público, cargo em comissão de livre nomeação e exoneração ou seja titular de mandato eletivo;  
  
II - tiver o contrato de trabalho celebrado após a data de entrada em vigor da Medida Provisória 936, de 2020;  
  
III - estiver em gozo de:

a) benefício de prestação continuada do regime geral de previdência social ou dos Regimes Próprios de Previdência Social, ressalvados os benefícios de pensão por morte e auxílio acidente.  
  
b) seguro-desemprego, em qualquer de suas modalidades; ou  
  
c) bolsa de qualificação profissional de que trata o art. 2º-A da Lei nº 7.998, de 1990.

Orientamos que procurem o corpo jurídico de suas empresas para ajudá-los nessa importante tomada de decisão relacionada a acordos já firmados, que somente agora, com a publicação da Portaria, traz de forma clara requisitos que dão direito ao Benefício.

Abaixo, detalhamos, as possibilidades de processamento para envio de novos acordos ou retificação de dados enviados.

*Cadastro de Funcionários - Dados do Registro*

No cadastro de Funcionários foi feito a adequação para retornar mensagem de validação para funcionários não elegíveis. Esta validação Verificar as seguintes situações:

* Funcionário com data de admissão maior ou igual a 02/04/2020
* Funcionário com afastamento diferente de 'T' ou 'C'
* Funcionário em período de gozo de Férias
* Funcionário com data de acordo maior igual que a data de demissão

Abaixo iremos mostrar um exemplo de um funcionário admitido no dia 02/04 e teve o acordo do B.E.M para o dia 15/04/2020:

Na aba B.E.M foi preenchido a data de acordo. Ao clicar em Salvar, retorna a mensagem abaixo:

falseObservação

Clicando em 'Sim' na mensagem acima, o cadastro não é salvo. Clicando em 'Não', o cadastro é salvo. A validação retorna a mensagem para o usuário verificar os dados antes de salvar. Caso o mesmo queira salvar mesmo com o aviso, o módulo Folha de Pagamento não impedirá

*Alteração Global Campos do Cadastro*

Utilizando o processo de alteração de campos do cadastro, será retornado um log de aviso para os casos acima e o cadastro será alterado.

**Cadastro de Funcionários - B.E.M**

 Para primeiro registro de Acordo disponibilizamos os campos discriminados abaixo no Cadastro de Funcionários, que devem ser preenchidos com as informações da Redução de Jornada ou Suspensão de Contrato de Trabalho conforme acordado com o funcionário. 

Os campos acima podem ser preenchidos de forma global, através do processo de Alteração Global de Cadastro, usando fórmulas. Abaixo exemplificaremos algumas sugestões de fórmulas, porém as mesmas devem ser desenvolvidas/adaptadas pelo usuário de forma a atender a sua necessidade:

Data da mudança: Data que foi feita a mudança no sistema. Esta data é para preenchimento de histórico. Deverá ser informada ao executar a alteração global de dados do funcionário ou preenchida manualmente.

Tipo de adesão: Irá receber o Tipo de Redução, podendo ser Suspensão de Contrato ou Redução de Jornada. No caso de usar o processo de Alteração Global de Cadastro, a fórmula deverá retornar 1.

* Fórmula: **1 /\* TIPO DE ADESÃO  1 - REDUÇÃO DE JORNADA ACORDADO ENTRE EMPREGADO E EMPRESA\*/**
* Fórmula: **0 /\* TIPO DE ADESÃO  0 - SUSPENSÃO DE CONTRATO DE TRABALHO ACORDADO ENTRE EMPREGADO E EMPRESA\*/**

Data do acordo: Irá receber a data do acordo da redução Jornada/Salário, corresponde ao início do período de redução de salário e jornada.

* Fórmula:  **"13/04/2020" /\*INFORME UMA DATA REDUÇÃO JORNADA ACORDADO ENTRE EMPREGADO E EMPRESA\*/**

Percentual de Redução da Jornada: irá receber o percentual utilizado para redução de Jornada/Salário. Para o tipo de adesão 'Suspensão de Contrato' este campo não deve ser preenchido, conforme a orientação do manual.

* Fórmula: **25,00 /\*INFORME O PERCENTUAL DE REDUÇÃO JORNADA ACORDADO ENTRE EMPREGADO E EMPRESA\*/**

Dias de duração do acordo: Irá receber a quantidade de dias que irá durar a Redução de Jornada. Este campo não limita a quantidade estabelecida na MP, ficando a cargo do usuário observar as regras para preenche-lo.

* Fórmula: **30 /\*TEMPO DE DURAÇÃO DA REDUÇÃO DE CONTRATO ACORDADO ENTRE EMPREGADO E EMPRESA\*/**

Valor Reduzido: Irá receber o salário que foi reduzido: Exemplo, funcionário com Salário de 2000,00 e teve a redução de 25%. Este campo recebe o valor de 500,00. Para o tipo de adesão 'Suspensão de Contrato' este campo não deve ser preenchido, conforme a orientação do manual.

* Fórmula:

**/\*EXEMPLO REDUÇÃO JORNADA/SALARIO EM ATÉ  25%. No exemplo abaixo 20%.**

Quando a redução é inferior a 25% o governo não complementa com a ajuda emergencial.

Dessa forma, com a redução da jornada de 20%, os rendimentos a pagos  no mês não poderão ficar menor que o salário mínimo

/\* Exemplo de fórmula para redução de jornada/salário em até 25%  
Para demais reduções deverá ser adequado para contemplar o percentual.  
A fórmula respeita a redução não deixando o salário pago no mes menor   
que o salário mínimo \*/

/**\*EXEMPLO REDUÇÃO JORNADA/SALARIO EM ATÉ 25%**

/\* Exemplo de fórmula para redução de jornada/salário em até 25%

Para demais reduções deverá ser adequado para contemplar o percentual.

A fórmula respeita a redução não deixando o salário pago no mes menor

que o salário mínimo \*/

DECL NovoSalario;

DECL ValorReduzido;

DECL PercReducao;

DECL Adesao;

**SETVAR**(PercReducao,20);

**SETVAR**(NovoSalario,(RC \* (100 - PercReducao) / 100 ) );

**SETVAR**(Adesao, **TABFUNC** ('TIPOADESAOBEM', 'I'));

**SE** ((Adesao = 1) **E** (PercReducao < 25) **E** (NovoSalario <  SM) )

ENTAO

**SETVAR**(ValorReduzido,(RC - SM))

SENAO

**SE** (Adesao = 1) **E** (PercReducao = 25)

  ENTAO

**SETVAR**(ValorReduzido,(RC - NovoSalario))

  SENAO 0

  FIMSE;

## **Cancelamento, Redução ou Prorrogação (Manual de Leiaute do Arquivo B.E.M  - Versão 3.0)**

Foi  estabelecido pelo Manual de Leiaute do Arquivo B.E.M Versão 3.0 os layouts para Cancelamento, Redução de Vigência e Prorrogação para casos de edição do primeiro registro de acordo B.E.M. Para isso foi necessária a criação de três novos campos (Data de Antecipação, Data de Cancelamento e Dias de Prorrogação) em **RH | Administração de Pessoal | Funcionário | Registro | aba B.E.M** :

Os campos novos criados, podem ser preenchidos de forma global, através do através do próprio cadastrado de funcionários ou pelo processo de Alteração Global de Cadastro, usando fórmulas. Abaixo exemplificaremos algumas sugestões de fórmulas, porém as mesmas devem ser desenvolvidas/adaptadas pelo usuário de forma a atender a sua necessidade:

Data da Antecipação: Irá receber a data de antecipação do término do contrato entre o empregado e a empresa.

* Fórmula:  **"26/06/2020" /\* INFORME UMA DATA DE ANTECIPAÇÃO DO TÉRMINO DO CONTRATO ACORDADO ENTRE EMPREGADO E EMPRESA \*/**

Data do Cancelamento: Irá receber a data de cancelamento do acordo do contrato acordado entre o empregado e a empresa.

* Fórmula:  **"26/06/2020" /\* INFORME A DATA DE CANCELAMENTO DO CONTRATO ACORDADO ENTRE EMPREGADO E EMPRESA \*/**

Dias de Prorrogação: Irá receber a quantidade de dias em que será prorrogado o contrato acordado em empregado e empresa. Este campo não limita a quantidade estabelecida na MP, ficando a cargo do usuário observar as regras para preenchê-lo, de acordo com a legislação vigente.

* Fórmula:  **30 /\* QUANTIDADE DE DIAS DE PRORROGAÇÃO DO CONTRATO ACORDADO ENTRE EMPREGADO E EMPRESA \*/**

**Observações:**

**Para primeiro registro de acordo não enviado para o governo:**

Caso necessite de edição realizada no cadastro do acordo poderá ser informada a data de mudança do primeiro registro do acordo. Com isso, não será criado um novo registro. Consequentemente os campos atualizados serão: Tipo de Adesão, Valor Reduzido, Data de Acordo, Percentual de Jornada e/ou Dias de Duração de Acordo.

**Para registros já enviado para o governo:**

Para cada registro de edição realizada no cadastro do acordo é extremamente necessário que seja informada uma nova data de mudança para o registro no histórico. Para que assim seja criado um novo registro no histórico. Consequentemente os campos atualizados serão: Dias de Prorrogação,  Data do Cancelamento ou Data de Antecipação.

**Para registro de Cancelamento, Antecipação ou Prorrogação não enviado para o governo:**

Para cada registro de edição realizada no cadastro do acordo, poderá ser utilizada a mesma data do ultimo registro cadastrado. Assim o ultimo registro será editado e não criará um novo. Consequentemente os campos atualizados serão: Dias de Prorrogação,  Data do Cancelamento ou Data de Antecipação.

Importante

**O processo de Alteração Global irá preencher e/ou editar apenas os campos selecionados e preenchidos na tela. Para inclusão de registro favor selecionar filtro apenas de funcionários que não tiverem adesão ao B.E.M. Para edição de registro, selecione filtro apenas de funcionários que já aderiram ao B.E.M.**

**Considerações para Geração do Arquivo**

Antes de inciarmos as orientações de como gerar o arquivo B.E.M é relevante pontuarmos os itens abaixo:

Conta bancária: Será opcional o preenchimento de dados bancários e o relatório irá aceitar essa informação em branco.

Importante

Conforme orientação do Empregador Web serão aceitas apenas contas bancárias do tipo Corrente e Poupança. Não será aceito contas do tipo Salário ou de Terceiros.  
Caso não sejam informados dados bancários ou os dados informados estejam incorretos, o pagamento do benefício será efetuado através de conta digital, aberta pelo próprio Ministério da Economia. A conta aberta será em nome do trabalhador e pertencente ao Banco do Brasil ou Caixa Econômica Federal.

O relatório B.E.M. irá considerar os dados bancários existentes no cadastro do Funcionário, conforme print abaixo.  
Para os casos em que a conta do funcionário for do tipo salário, ou seja, uma conta não aceita pelo Empregador Web. Deverá ser mantido o campo "Tipo de Conta" sem preencher (campo NULO), desta forma o relatório será gerado sem os dados bancários. Sendo assim, este funcionário deverá receber o benefício através de conta digital, conforme sinalizado anteriormente. 

Foi disponibilizado um recurso para desmarcar a informação "Tipo de conta bancária", para os casos em que a conta do funcionário for do tipo Salário:

**Gerador de Saídas**

Para atender esta demanda, disponibilizamos o Layout B.E.M (versao Oficial).TotvsGen conforme a [especificação](https://sd.mte.gov.br/sdweb/validador/Manual_EmpregadorWeb_BEM.pdf) do Ministério da Economia e do Trabalho,  que deve ser gerado pelo Recurso Gerador de Saídas. 

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

* *Filtro do Usuário:* Neste campo é permitido fazer filtros dos funcionários que serão contemplados neste relatório

Após preencher os campos, e executar o processo, irá retornar o aquivo gerado conforme abaixo:

  

O arquivo gerado no diretório informado em formato .txt:

Conforme a especificação do Layout, o sistema do Empregador Web ao qual o arquivo deve ser importado só aceita arquivos na extensão .csv. Desta forma, para alterar a extensão do arquivo, deve proceder conforma abaixo:

Passo 1: Abrir o arquivo no bloco de notas, ir em arquivo e salvar como:

Passo 2: Após clicar em 'Salvar como' irá abrir a tela abaixo. Deve mudar o Tipo Documento para Todos os arquivos (\*.\*)  e a o nome alterar, mudando .txt para .csv:

  

Após salvar, o arquivo será apresentado conforme abaixo:

Após a alteração, o arquivo pode ser validado neste [link](https://sd.maisemprego.mte.gov.br/sdweb/validador/validadorReqEmergencial.jsf) disponibilizado pelo Empregador Web:

**Gerador de Saídas -****Cancelamento, Redução ou Prorrogação**

Para atender aos layouts disponibilizados na [especificação](https://sd.mte.gov.br/sdweb/validador/Manual_EmpregadorWeb_BEM.pdf) do Ministério da Economia e do Trabalho,  foram criados três NOVOS relatórios que deve ser gerado pelo Recurso Gerador de Saídas, que são:

* Antecipação/Redução:
* Prorrogação:
* Cancelamento:

Para fazer a importação deve acessar Gestão | Gerador de Saídas | Processo | Importar Layout

Após a importação, para gerar o arquivo deve selecionar o layout desejado, ir em Processo | Geração de Saídas. O processo irá abrir a tela abaixo. Nesta tela poderá alterar o caminho onde deseja que o relatório seja armazenado após a geração:

**Antecipação ou Redução**

Ao avançar, irá apresentar a tela abaixo com os parâmetros da geração, que devem ser preenchidos pelo usuário:

No nosso exemplo, selecionei o arquivo Layout B.E.M Antecipacao.TotvsGen, então vou filtrar, utilizando o 'Filtro do Usuário', criando o filtro com o campo 'Data da Antecipação' = '26/06/2020':

O arquivo gerado no diretório informado em formato .txt:

Conforme a especificação do Layout, o sistema do Empregador Web ao qual o arquivo deve ser importado só aceita arquivos na extensão .csv. Desta forma, para alterar a extensão do arquivo, deve proceder conforma abaixo:

Abrir o arquivo no bloco de notas, ir em arquivo e salvar como e em seguida mudar o Tipo Documento para Todos os arquivos (\*.\*)  e a o nome alterar, mudando .txt para .csv:

Após salvar, o arquivo será apresentado conforme abaixo:

Após a alteração, o arquivo pode ser validado neste [link](https://sd.maisemprego.mte.gov.br/sdweb/validador/validadorReqEmergencial.jsf) disponibilizado pelo Empregador Web:

Observação: Para validar a opção de antecipação do término do contrato, deverá ser selecionada a opção 'Redução' no validador.

**Prorrogação**

Ao avançar, irá apresentar a tela abaixo com os parâmetros da geração, que devem ser preenchidos pelo usuário:

No nosso exemplo, selecionei o arquivo Layout B.E.M Prorrogação.TotvsGen, então vou filtrar utilizando o 'Filtro do Usuário', criando o filtro com o campo 'Dias de Prorrogação' = '30':

O arquivo gerado no diretório informado em formato .txt:

Conforme a especificação do Layout, o sistema do Empregador Web ao qual o arquivo deve ser importado só aceita arquivos na extensão .csv. Desta forma, para alterar a extensão do arquivo, deve proceder conforma abaixo:

Abrir o arquivo no bloco de notas, ir em arquivo e salvar como e em seguida mudar o Tipo Documento para Todos os arquivos (\*.\*)  e a o nome alterar, mudando .txt para .csv:

Após salvar, o arquivo será apresentado conforme abaixo:

Após a alteração, o arquivo pode ser validado neste [link](https://sd.maisemprego.mte.gov.br/sdweb/validador/validadorReqEmergencial.jsf) disponibilizado pelo Empregador Web:

Observação: Para validar a opção de antecipação do término do contrato, deverá ser selecionada a opção 'Prorrogação' no validador.

**Cancelamento**

Ao avançar, irá apresentar a tela abaixo com os parâmetros da geração, que devem ser preenchidos pelo usuário:

No nosso exemplo, selecionei o arquivo Layout B.E.M Cancelamento.TotvsGen, então vou filtrar, utilizando o 'Filtro do Usuário', criando o filtro com o campo 'Data do Cancelamento' = '26/06/2020':

O arquivo gerado no diretório informado em formato .txt:

Conforme a especificação do Layout, o sistema do Empregador Web ao qual o arquivo deve ser importado só aceita arquivos na extensão .csv. Desta forma, para alterar a extensão do arquivo, deve proceder conforma abaixo:

Abrir o arquivo no bloco de notas, ir em arquivo e salvar como e em seguida mudar o Tipo Documento para Todos os arquivos (\*.\*)  e a o nome alterar, mudando .txt para .csv:

Após salvar, o arquivo será apresentado conforme abaixo:

Após a alteração, o arquivo pode ser validado neste [link](https://sd.maisemprego.mte.gov.br/sdweb/validador/validadorReqEmergencial.jsf) disponibilizado pelo Empregador Web:

Observação: Para validar a opção de antecipação do término do contrato, deverá ser selecionada a opção 'Cancelamento' no validador.

*Usando consulta SQL para gerar o arquivo*

Passo 1: Criar uma consulta SQL que retorna as chapas contempladas para na adesão do BEM. No exemplo abaixo selecionamos as chapas não considerando algumas situações, data de admissão após a data da publicação da MP e se o mesmo é aposentado:

sqlSQL - Seleção de Funcionários - BEm '01/04/2020']]>

Passo 2: No Filtro do BEm, selecionar o campo Chapa do Funcionário, o operador IN (SQL) e a consulta SQL criada acima. Ao executar o processo será considerado somente a chapas da consulta:

 

Usando Campos do Filtro

Passo 1: Criar um filtro usando os campos disponíveis no recurso de Filtros. No exemplo abaixo usei os campos ' Data de admissão, data de acordo e situação. Ao executar o processo será considerado somente a chapas retornadas pelo filtro criado.

 

falseImportante

**eSocial**

Conforme a orientação do eSocial, o empregador deverá enviar um evento de alteração contratual (S-2206) com Data de Alteração igual ao início do período de redução de salário e jornada e, neste evento, informar o valor do salário reduzido e a nova jornada a ser cumprida pelo trabalhador durante esse período.

No campo observação deverá informar o prazo pactuado para a referida redução e o percentual definido para essa redução proporcional. Mais informações sobre a geração do evento S-2206 [acesse aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=556391463)
