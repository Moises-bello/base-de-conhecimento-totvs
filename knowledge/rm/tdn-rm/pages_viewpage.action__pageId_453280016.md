---
content_hash: 0395d3eb483591189d894181b6acc8fdc9e141b98ee207787fa6f01806ecb275
fetched_at: '2026-06-29T00:10:11.719132+00:00'
page_id: '453280016'
product: rm
source: tdn-rm
title: Rateio por Tomador de Serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=453280016
version: 63
---

false

**A partir das Versões:**

* + 12.1.22.221
  + 12.1.23.148
  + 12.1.24.000

# Objetivo:

---

Ratear a movimentação para os funcionários que trabalharam em Tomadores de Serviço. A movimentação do funcionário deverá ser informada proporcionalmente aos dias trabalhados em cada Tomador de Serviço.

Este rateio é utilizado na geração de encargos e do eSocial.

teste1true1A partir da versão 12.1.22 // 12.1.23A partir da versão 12.1.21 // 12.1.22 // 12.1.23deck02true1Execução do script para liberação do histórico de tomadorExecução do script para liberação do histórico de tomador

Para a criação da tabela para a utilização do histórico de tomador de serviço será necessário executar o script 'LB.2019.01\_02' através do sistema RM.Script.Executor.exe.

2Conversor Histórico Rateio TomadorConversor Histórico Rateio Tomador

Foi criado um processo para preencher o histórico de tomador de serviço conforme abaixo:

Acesse o menu Configurações | Conversão | Conversor Histórico Rateio Tomador

Nessa tela é possível realizar a seleção dos funcionários e a forma de conversão.

* **Considerar apenas rateio atual:** O sistema irá verificar o cadastro do rateio de tomador atual e preencherá o histórico.
* **Considerar movimento distribuído de competências anteriores:** O usuário deverá informar a**"Competência Inicial"** e o "**Evento base para Rateio**", com isso o sistema irá alimentar o histórico a partir da competência informada até a competência anterior a atual com os tomadores encontrados no Movimento Distribuído por Tomador para o evento selecionado. Para a competência atual o sistema alimenta o histórico com o rateiro atual de tomador.
* **Regerar histórico:** Está opção deleta todos os históricos existentes, conforme filtro cadastrado e refaz o processo de conversão conforme opções acima.

**Observações:** Para preenchimento do campo "Competência Inicial" no histórico o sistema verifica a opção selecionada, conforme abaixo:

* Ao selecionar a opção "Considerar apenas rateio atual" preencherá com o mês e ano da competência atual.
* Ao selecionar a opção "Considerar movimento distribuído de competências anteriores" preencherá com o mês e ano competência existente no movimento do tomador, para a competência atual o sistema alimenta com o mês e ano competência atual.

Caso seja necessária alguma alteração poderá ser feita manualmente pelo histórico ou pela importação de dados.

3Rateio de TomadoresRateio de Tomadores

Acesse o menu Administração de Pessoal | Cadastros | Funcionários

Selecione o funcionário que deseja visualizar o rateio do tomador de serviço, acesse o Anexos | Folha de pagamento | Rateio Tomador

Nesta tela é possível realizar o somente a visualização do rateio de tomadores do período atual, a edição será liberada na versão 12.1.24.

4Histórico de Rateio por TomadorHistórico de Rateio por Tomador

Acesse o menu Administração de Pessoal | Cadastros | Funcionários

Selecione o funcionário que deseja visualizar o histórico de tomador de serviço, acesse Anexos |  Históricos | Históricos de rateio por tomador

É possível realizar a inclusão ou edição de um histórico cadastrado.

5Alteração Global de TomadoresAlteração Global de Tomadores

O processo de alteração global de tomadores pode ser usado caso haja necessidade de alterar o cadastro de um número maior de funcionários;

Acesse o menu Administração de Pessoal | Alterações Cadastrais | Alteração Tomadores

Nessa tela é possível realizar a seleção dos funcionários, opções de processamento e a forma de alteração:

* **Consiste dias de tomadores:**Essa flag faz a validação se o total de dias a distribuir (campo **valor**) colocados no processo é maior que o total de dias a ratear (campo **total de dias a Ratear**; este campo vem do mês comercial ou fórmula cadastrada no parametrizador em **Parametrizador | Folha de pagamento | Folha Normal | Tomador de serviços**)
* **Determinar distribuição a todos os funcionários processados:** Esta forma dentro desta seleção, sobrescreverá qualquer outra informação relativa à distribuição por tomadores no cadastro de funcionários pela informação especificada na rotina, ou seja, se existirem tomadores de serviço cadastrados nas respectivas pastas dos funcionários, estas informações serão apagadas e no lugar destas serão incluídas as informações cadastradas neste módulo.  
  **Observação:** Caso possua algum tomador que tenha data inicio anterior a competência atual, o processo irá criar uma data fim para esse tomador, para preservar o histórico e criará um novo com data atual.
* **Alterar apenas dias de distribuição:**Será alterado apenas os dias de distribuição. Neste caso somente será aceito um código que está sendo utilizado no Cadastro dos Funcionários em Tomadores de Serviços no campo tomador.   
  **Avisos:**
  1. Se não informar nenhum tomador a alteração será realizada para todos os tomadores de serviços cadastrados no registro do funcionário. As informações de De/Para somente estarão disponíveis para alteração de apenas dias de distribuição. Confira o exemplo [De/Para](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718512).
  2. A alteração dos dias a serem distribuídos pelo tomador pode ser feita através de fórmula, como por exemplo, considerando os dias trabalhados do funcionário em determinado mês, deverá montar uma fórmula com o valor = ND. Confira o exemplo [Fórmula ND](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718599) Dicas: 1.    Alteração de 30 para 31 dias em empresas que tem funcionários horistas e mensalistas. 2.    Alterações de dias utilizando a formula ND para funcionários ativos, afastados no mês, retornos de afastamento, férias no mês, admitidos no mês e etc.

**Atenção:**

* Caso o tomador selecionado no processo não exista no cadastro de [Lotação Tributaria](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452719628), será disparado um [gatilho](http://tdn.totvs.com.br/display/LRM/Gerar+Gatilhos+Eventos+Iniciais) de inclusão.
6Distribuir SefipDistribuir Sefip

De acordo com o cadastro no histórico de tomador de serviços deverá ser feita a distribuição por tomador de serviços dos valores pagos em meses anteriores dos funcionários.

Acesse o menu Encargos | Sefip | Distribuir Sefip

Será distribuído conforme regras abaixo:

1. Competência atual – distribuição conforme rateio de tomadores cadastrados no anexo do funcionário.
2. Rateio de Eventos – distribuição referente ao período da retificação que deverá ser entre 10000 e 30000.
3. Histórico de Tomador – distribuição conforme histórico do rateio de tomadores cadastrados no anexo do funcionário. Neste caso existe a possibilidade de geração deste histórico com o processo “Conversor Histórico Rateio Tomador” em Configurações.

2A partir da versão 12.1.24A partir da versão 12.1.24deck032Conversor Histórico Rateio TomadorConversor Histórico Rateio Tomador

Foi criado um processo para preencher o histórico de tomador de serviço conforme abaixo:

Acesse o menu Acesse o menu Configurações | Conversão | Conversor Histórico Rateio Tomador

Nessa tela é possível realizar a seleção dos funcionários e a forma de conversão.

* **Considerar apenas rateio atual:** O sistema irá verificar o cadastro do rateio de tomador atual e preencherá o histórico.
* **Considerar movimento distribuído de competências anteriores:** O usuário deverá informar a**"Competência Inicial"** e o "**Evento base para Rateio**", com isso o sistema irá alimentar o histórico a partir da competência informada até a competência anterior a atual com os tomadores encontrados no Movimento Distribuído por Tomador para o evento selecionado. Para a competência atual o sistema alimenta o histórico com o rateiro atual de tomador.
* **Regerar histórico:** Está opção deleta todos os históricos existentes, conforme filtro cadastrado e refaz o processo de conversão conforme opções acima.

**Observações:** Para preenchimento do campo "Competência Inicial" no histórico o sistema verifica a opção selecionada, conforme abaixo:

* Ao selecionar a opção "Considerar apenas rateio atual" preencherá com o mês e ano da competência atual.
* Ao selecionar a opção "Considerar movimento distribuído de competências anteriores" preencherá com o mês e ano competência existente no movimento do tomador, para a competência atual o sistema alimenta com o mês e ano competência atual.

Caso seja necessária alguma alteração poderá ser feita manualmente pelo histórico ou pela importação de dados.

true3Rateio de TomadoresRateio de Tomadores

Acesse o menu Administração de Pessoal | Cadastros | Funcionários

Selecione o funcionário que deseja visualizar o rateio do tomador de serviço, acesse o Anexos | Folha de pagamento | Rateio Tomador

Nesta tela é possível realizar o cadastro ou edição somente do rateio de tomadores do período atual.

É possível editar o rateio de tomador e realizar alterações. Porém, caso altere alguma informação que a vigência tenha inicio anterior a competência atual, será necessário informar a data fim para esse rateio, para que não interfira no rateio de meses anteriores e crie um novo para a competência atual.

4PermissõesPermissões

Acesse o menu Serviços Globais | Segurança | Perfis

As permissões do rateio de tomador e histórico do rateio de tomador serão liberadas através do menu abaixo:

Observação:  as permissões para histórico de tomador foram ajustas a partir dos patch's :

* 12.1.27.103
* 12.1.26.162
* 12.1.25.216
5Histórico de Rateio por TomadorHistórico de Rateio por Tomador

Acesse o menu Administração de Pessoal | Cadastros | Funcionários

Selecione o funcionário que deseja visualizar o histórico de tomador de serviço, acesse Anexos |  Históricos | Históricos de rateio por tomador

É possível realizar a inclusão ou edição de um histórico cadastrado.

6Alteração Global de TomadoresAlteração Global de Tomadores

O processo de alteração global de tomadores pode ser usado caso haja necessidade de alterar o cadastro de um número maior de funcionários;

Acesse o menu Administração de Pessoal | Alterações Cadastrais | Alteração Tomadores

Nessa tela é possível realizar a seleção dos funcionários, opções de processamento e a forma de alteração:

* **Consiste dias de tomadores:**Essa flag faz a validação se o total de dias a distribuir (campo **valor**) colocados no processo é maior que o total de dias a ratear (campo **total de dias a Ratear**; este campo vem do mês comercial ou fórmula cadastrada no parametrizador em **Parametrizador | Folha de pagamento | Folha Normal | Tomador de serviços**)

* **Determinar distribuição a todos os funcionários processados:** Esta forma dentro desta seleção, sobrescreverá qualquer outra informação relativa à distribuição por tomadores no cadastro de funcionários pela informação especificada na rotina, ou seja, se existirem tomadores de serviço cadastrados nas respectivas pastas dos funcionários, estas informações serão apagadas e no lugar destas serão incluídas as informações cadastradas neste módulo.  
  **Observação:** Caso possua algum tomador que tenha data inicio anterior a competência atual, o processo irá criar uma data fim para esse tomador, para preservar o histórico e criará um novo com data atual.
* **Alterar apenas dias de distribuição:**Será alterado apenas os dias de distribuição. Neste caso somente será aceito um código que está sendo utilizado no Cadastro dos Funcionários em Tomadores de Serviços no campo tomador.   
  **Avisos:**
  1. Se não informar nenhum tomador a alteração será realizada para todos os tomadores de serviços cadastrados no registro do funcionário. As informações de De/Para somente estarão disponíveis para alteração de apenas dias de distribuição. Confira o exemplo [De/Para](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718512).
  2. A alteração dos dias a serem distribuídos pelo tomador pode ser feita através de fórmula, como por exemplo, considerando os dias trabalhados do funcionário em determinado mês, deverá montar uma fórmula com o valor = ND. Confira o exemplo [Fórmula ND](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718599) Dicas: 1.    Alteração de 30 para 31 dias em empresas que tem funcionários horistas e mensalistas. 2.    Alterações de dias utilizando a formula ND para funcionários ativos, afastados no mês, retornos de afastamento, férias no mês, admitidos no mês e etc.

**Atenção:**

* Caso o tomador selecionado no processo não exista no cadastro de [Lotação Tributaria](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452719628), será disparado um [gatilho](http://tdn.totvs.com.br/display/LRM/Gerar+Gatilhos+Eventos+Iniciais) de inclusão.
7Distribuir SefipDistribuir Sefip

De acordo com o cadastro no histórico de tomador de serviços deverá ser feita a distribuição por tomador de serviços dos valores pagos em meses anteriores dos funcionários.

Acesse o menu Encargos | Sefip | Distribuir Sefip

Será distribuído conforme regras abaixo:

1. Competência atual – distribuição conforme rateio de tomadores cadastrados no anexo do funcionário.
2. Rateio de Eventos – distribuição referente ao período da retificação que deverá ser entre 10000 e 30000.
3. Histórico de Tomador – distribuição conforme histórico do rateio de tomadores cadastrados no anexo do funcionário. Neste caso existe a possibilidade de geração deste histórico com o processo “Conversor Histórico Rateio Tomador” em Configurações.
