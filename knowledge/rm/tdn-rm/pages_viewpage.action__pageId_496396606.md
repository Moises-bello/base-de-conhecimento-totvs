---
content_hash: e99c47aa4f8e1735acbb2bbbf498b20c3f9a001afbb15b8db5cfb6029bef6431
fetched_at: '2026-06-29T00:10:22.101389+00:00'
page_id: '496396606'
product: rm
source: tdn-rm
title: Importação de Resultado de Exames - Estrutura Arquivo XML
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496396606
version: 9
---

<?xml version="1.0" encoding="ISO-8859-1" ?>  
***<REGISTRO>***  
**<CONSULTA>**  
<IDCONSULTA></IDCONSULTA>  
<CODENTIDADE></CODENTIDADE>  
<CODCONSULTA></CODCONSULTA>  
<CODPESSOA></CODPESSOA>  
<CHAPA></CHAPA>  
<CODMEDICO></CODMEDICO>  
<CODTIPOCONSULTA></CODTIPOCONSULTA>  
<CODTIPOCONSULTAESOCIAL></CODTIPOCONSULTAESOCIAL>  
<DATACONSULTA></DATACONSULTA>  
<APTO></APTO>  
<DATAASO></DATAASO>  
<OBSERVACAO></OBSERVACAO>  
**</CONSULTA>**  
**<RESULTADO>**  
<IDCONSULTA></IDCONSULTA>  
<CODCONSULTA></CODCONSULTA>  
<CODPESSOA></CODPESSOA>  
<EXAME></EXAME>  
<TIPOEXAME></TIPOEXAME>  
<CID></CID>  
<CODENTIDADE></CODENTIDADE>  
<DATAEXAME></DATAEXAME>  
<EXAMEREFERENCIAL></EXAMEREFERENCIAL>  
<ATIVOOCUPACIONAL></ATIVOOCUPACIONAL>  
<RESULTNORMAL></RESULTNORMAL>  
<TIPOANORMALIDADE></TIPOANORMALIDADE>  
<APTO></APTO>  
<DESCANORMAL></DESCANORMAL>  
<OBSERVACAO></OBSERVACAO>  
<CODLAUDOEXAME></CODLAUDOEXAME>  
<CODPROCEDMENTO></CODPROCEDMENTO>  
<CAMPOTEXTOLONGO></CAMPOTEXTOLONGO>  
<CAMPONUMERICO></CAMPONUMERICO>  
<CAMPOTEXTO></CAMPOTEXTO>  
<CAMPOTABDINAM></CAMPOTABDINAM>  
**</RESULTADO>**  
***</REGISTRO>***

Todo exame está vinculado à uma consulta, sendo assim, os dados das consultas deverão preceder os dados dos exames e estar contidos nas tags **<CONSULTA></CONSULTA>** e **<CODPESSOA></CODPESSOA>**. Toda consulta realizada deve estar no arquivo XML seguida imediatamente pelo(s) exame(s) relacionado(s) à mesma. Cada exame deve estar contido numa tag <RESULTADO></RESULTADO> com todos os seus dados, sendo ilimitado o número de exames para cada consulta e, consequentemente o número de tags **<RESULTADO></RESULTADO>** também.   
É obrigatória a existência das tags **<CODCONSULTA></CODCONSULTA>** e **<CODPESSOA></CODPESSOA>** em todos os registros do arquivo. Já nos registros de exame, estas tags existem para identificar à qual consulta e pessoa está relacionado o exame em questão, sendo assim ela deve estar obrigatoriamente preenchida com um valor de uma consulta e pessoa existente no arquivo, caso esta tag não esteja preenchida ou esteja preenchida com um valor que não existe, não será possível concluir o processo. A repetição de valores das tags **<CODCONSULTA></CODCONSULTA>** e **<CODPESSOA></CODPESSOA>**nos registros exame será permitida uma vez que vários exames podem estar relacionados à mesma consulta.   
É obrigatória a existência da tag **<EXAME></EXAME>** em todos os registros de exame do arquivo. Esta tag serve para relacionar cada exame do arquivo a um exame existente no sistema, sendo assim os exames do arquivo a serem relacionados ao mesmo exame do sistema devem possuir o mesmo valor para esta tag. Caso esta tag não esteja preenchida, não será possível concluir o processo.   
Caso ocorra a existência de dados decimais no arquivo XML, os mesmo devem possuir pontos e não vírgulas.

## **Campos de Consulta**

**IDCONSULTA**: É o identificador da consulta (VCONSULTASPRONT.IDCONSULTA), um código que não pode se repetir.   
Se este campo estiver em branco, uma consulta é criada para cada exame informado. Entretanto, se este campo estiver preenchido, o processo de importação de exames não criará uma consulta, mas apenas irá adicionar os exames à consulta cujo o “idConsulta” seja correspondente ao informado no XML.

**CODENTIDADE**: É o código da entidade relacionada ao exame e será visualizado no prontuário médico campo "Serviço de saúde responsável (eSocial)". Esse campo será utilizado no leiaute do eSocial evento S-2220 -Monitoramento da Saúde do Trabalhador .

**CODCONSULTA**: É o código da consulta (VCONSULTASPRONT.CODCONSULTAPRONT), deve ser preenchido com um valor que garanta a unicidade das consultas contidas no arquivo. Preenchimento obrigatório.

**CODPESSOA**: É o código da pessoa a qual a consulta pertence. Deve ser preenchido com o valor do código de uma pessoa cadastrada no sistema (RM | Segurança e Medicina do Trabalho | Cadastros | Pessoas), caso o valor informado não esteja cadastrado, não será possível concluir o processo e o sistema retornará uma mensagem ao usuário. Preenchimento obrigatório.

**CHAPA**: Permite identificar qual funcionário se encontra vinculado ao prontuário .A informação será visualizada no campo "Funcionário". Esse campo será utilizado no leiaute do eSocial evento S-2220 -Monitoramento da Saúde do Trabalhador .

**CODMEDICO**: É o código do médico responsável pela realização da consulta. Deve ser preenchido com o valor do código de um profissional de saúde cadastrado no sistema (RM | Segurança e Medicina do Trabalho | Cadastros | Profissional de Saúde). Caso o valor informado não esteja cadastrado, não será possível concluir o processo e o sistema retornará uma mensagem ao usuário. Preenchimento opcional.

**CODTIPOCONSULTA**: É o código do tipo da consulta. Deve ser preenchido com um valor cadastrado em uma tabela dinâmica do sistema. Preenchimento obrigatório.

**CODTIPOCONSULTAESOCIAL**: É o código do tipo da consulta e-social. Deve ser preenchido com um valor cadastrado em uma tabela dinâmica do sistema. Preenchimento opcional.

**DATACONSULTA**: É a data da realização da consulta. Deve ser preenchido no formato dd/mm/aaaa. Preenchimento obrigatório

**APTO**: Indica a situação final da consulta realizada. Deve ser preenchido com os valores 1, 2 ,3 ou 4 (1 = Apto, 2 = Inapto, 3 = Apto com Restrição, 4 = Pendente). Preenchimento obrigatório.

**DATAASO**: Campo para preenchimento do campo data aso no cadastro da consulta. Seu preenchimento é obrigatório para a geração do ASO e também para a geração do gatilho do evento S-2220.

**OBSERVACAO**: Campo para preenchimento de eventuais observações existentes na consulta. Preenchimento opcional.

## **Campos de Exame**

**IDCONSULTA**: É o identificador da consulta (VCONSULTASPRONT.IDCONSULTA), um código que não pode se repetir.   
Se este campo estiver em branco, uma consulta é criada para cada exame informado. Entretanto, se este campo estiver preenchido, o processo de importação de exames não criará uma consulta, mas apenas irá adicionar os exames à consulta cujo o “idConsulta” seja correspondente ao informado no XML.

**CODCONSULTA**: É o código da consulta à qual o exame em questão está relacionado, deve ser preenchido com o valor de uma das consultas existentes no arquivo. Caso o valor informado não seja localizado nas consultas do arquivo, não será possível concluir o processo. Preenchimento obrigatório.

**CODPESSOA**: É o código da pessoa a qual a consulta e exame pertencem. Deve ser preenchido com o valor do código de uma pessoa cadastrada no sistema (RM | Segurança e Medicina do Trabalho | Cadastros | Pessoas), caso o valor informado não esteja cadastrado, não será possível concluir o processo e o sistema retornará uma mensagem ao usuário. Preenchimento obrigatório.

**EXAME**: É o identificador que relacionará os exames do arquivo aos exames do sistema (Ex.: 001 = Hemograma, 002 = Audiometria). Pode ser preenchido com qualquer valor, garantindo que todos os exames relacionados a um mesmo exame do sistema possuam sempre o mesmo valor, por exemplo: Se um exame de Hemograma é preenchido com valor “001” nesta tag, então todos os exames do arquivo que forem Hemograma também deverão ser preenchidos com o valor “001”. Este campo será utilizado para ordenar a exibição dos exames na tela de relacionamento dos campos. Preenchimento obrigatório.

**TIPOEXAME**: É o tipo do exame, deve ser preenchido com um dos valores a seguir: A, D, I, M, P ou R (A = Admissional; D = Demissional; I = Não informado, M = Mudança de Função, P = Periódico, R = Retorno ao Trabalho). Preenchimento Obrigatório.

**CID**: É o código da doença presente no exame. Deve ser preenchido com o código de uma doença cadastrada no sistema (RM | Segurança e Medicina do Trabalho |PCMSO | CID). Preenchimento opcional.

**CODENTIDADE**: É o código da entidade relacionada ao exame. Deve ser preenchido com o código de uma entidade cadastrada no sistema (RM | Gestão de Pessoas | Desenvolvimento | Entidades). Preenchimento obrigatório.

**DATAEXAME**: É a data de realização do exame, deve ser preenchido no formato dd/mm/aaaa. Preenchimento obrigatório.

**EXAMEREFERENCIAL**: Indica se é exame referencial ou não. Deve ser preenchido com 0 ou 1 (0 = Não, 1 = Sim). Preenchimento opcional.

**ATIVOOCUPACIONAL**: Indica se é atividade ocupacional ou não (0 = Não, 1 = Sim). Preenchimento opcional.

**RESULTNORMAL**: Indica se o resultado do exame é normal ou anormal (0 = Normal, 1 = Anormal). Preenchimento opcional.

**TIPOANORMALIDADE**: Indica o tipo da anormalidade (0 = Estável, 1 = Agravamento). Preenchimento opcional.

**APTO**: É o resultado do exame, indica se o funcionário/pessoa está apto ou não (0 = Não, 1 = Sim). Preenchimento opcional.

**DESCANORMAL**: É a descrição da anormalidade, campo para digitação de texto. Preenchimento opcional.

**CODLAUDOEXAME**: Campo destinado ao preenchimento do número do laudo do exame toxicológico(padrão Denatran) . Esse campo é necessário para a geração correta do evento S-2221.

**CODPROCEDMENTO**: Campo para preenchimento do código de procedimento utilizado para realização do exame. Deve ser um código existente na tabela 27 (Procedimentos Diagnósticos) do eSocial. Esse campo é obrigatorio para a geração do evento S-2220 do eSocial.

**OBSERVACAO**: Campo para preenchimento de eventuais observações existentes no exame. Preenchimento opcional.

**CAMPOTEXTOLONGO**, **CAMPONUMERICO**, **CAMPOTEXTO**, **CAMPOTABDINAM**: São campos opcionais que podem ser relacionados a algum campo do sistema, inclusive campos de informação clínica.  
  
Observação:  
- As consultas serão incluídas no cadastro de Consultas Médicas com o campo **CODCONSULTA** sequencial por pessoa, ou seja, o campo **CODCONSULTA** do arquivo XML se refere somente para vinculação dos exames na consulta a ser importada.  
- As consultas serão incluídas no cadastro de Consultas Médicas com o campo **TIPO** (VCONSULTASPRONT.TIPO) preenchido como "Consulta Médica Ocupacional".
