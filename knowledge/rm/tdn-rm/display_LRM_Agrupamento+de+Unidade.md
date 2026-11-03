---
content_hash: aa597cef014a71c9ebf3204f9ebf380e8ae4ebc798748025c07234082cfbb951
fetched_at: '2026-06-29T00:10:31.221152+00:00'
page_id: '521115451'
product: rm
source: tdn-rm
title: Agrupamento de Unidade
type: documentation
url: https://tdn.totvs.com/display/LRM/Agrupamento+de+Unidade
version: 20
---

## **01. Visão Geral**

Algumas instituições de ensino restringem o acesso de funcionários por contexto e de acordo com suas funções a algumas funcionalidades do sistema. Porém, como o cadastro de alunos e professores estão relacionados apenas a coligada, e não ao contexto completo, usuários de contextos diferente dentro da mesma coligada possuem acesso a todos alunos/professores da coligada. Para atender a essa necessidade das instituições de ensino foi criado o conceito de Agrupamento de Unidade.

## **02. Exemplo de Utilização**

O funcionário da secretaria João Silva, pertencente ao contexto A (coligada 1, filial 1 e nível de ensino 1), deve ter acesso apenas aos alunos e professores do seu contexto. Para isso ser possível basta criar o agrupamento "Unidade A" e associar a ele o usuário do João da Silva, os alunos que possui matrícula do contexto A e os professores que possuem turma no contexto A. Dessa forma, o funcionário da secretaria poderá realizar os processos de sua competência apenas sobre os alunos/professores que fazem parte do agrupamento que o seu usuário foi associado.

## **03. Habilitando o sistema para funcionar com o agrupamento de unidade**

A aplicação do filtro nas telas do sistema, que possuem a seleção de alunos ou professores, de acordo com as configurações previamente realizadas de agrupamento de unidade para a coligada e usuário logado será realizada após a marcação do parâmetro "Educacional | Secretária | Geral 6/6 | Habilita filtro de agrupamento de unidade".

O parâmetro será habilitado apenas se **todos** os contextos da coligada corrente estiverem configurados como item de agrupamento de pelo menos um agrupamento de unidade cadastrado.

## **04. Tela de agrupamento de unidade**

Para limitar o acesso dos usuários aos alunos/professores, foi criado o cadastro de agrupamento de unidade em TOTVS Educacional | Configurações | Agrupamento de unidade:

Esse cadastro cria unidades na instituição de ensino que terão associados a ele, através do anexo da tela, contextos, alunos e professores relacionadas a ela, dessa forma, limita-se o acesso dos usuários aos alunos/professores das unidades relacionadas a ele:

Existem algumas restrições na relação entre o agrupamento de unidade e seus itens:

* O cadastro de agrupamento é por coligada.
* O agrupamento de unidade só pode ter itens da sua coligada.
* Um mesmo item não pode fazer parte de dois agrupamentos diferentes.

O controle de acesso de visibilidade do menu, inclusão, exclusão e alteração de agrupamento de unidade e itens do agrupamento é feito através do perfil do usuário:

## **05. Tela de vínculo do usuário com agrupamento de unidade**

Para realizar a associação entre o usuário e o agrupamento criado, foi criado um cadastro que pode ser acessado via visão de agrupamentos de unidades (Configurações | Agrupamento de Unidade | Anexo | Usuário) ou via visão do usuário (Serviços Globais | Segurança | Usuário | Anexos | Agrupamento de Unidade):

## **06. Tela de vínculo do perfil com agrupamento de unidade**

Para realizar a associação entre o perfil e o agrupamento criado, foi criado um anexo na visão do perfil (Serviços Globais | Segurança | Perfil | Anexos | Agrupamento de Unidade).

Somente será considerado o agrupamento do perfil, quando o usuário não possui nenhum agrupamento criado diretamente em seu cadastro.

Exemplo:

Supondo que o usuário X possui um agrupamento 1 vinculado. O perfil deste usuário X possui um agrupamento 2 vinculado.

O sistema irá apenas considerar o agrupamento 1 do usuário. Caso seja, excluído o agrupamento 1 do usuário, o sistema passa a considerar o agrupamento do 2 que está no perfil deste usuário.

## **07****. Tela de vínculo do aluno com o agrupamento de unidade**

Para realizar a associação entre agrupamento de unidade e aluno, basta acessar o cadastro via anexo Aluno existente no cadastro de Agrupamento de Unidade ou pelo anexo Agrupamento de unidade existente no cadastro de Aluno:

#### **Associação automática de alunos**

Foi implementado a funcionalidade para associar ao aluno no momento da sua criação um agrupamento, este agrupamento no caso da criação de um aluno diretamente pelo cadastro de alunos, será o contexto atual da operação, no caso de um aluno que está sendo criado através da matrícula do processo seletivo RM ou do processo seletivo seletivo terceirizado, o sistema irá considerar o contexto da habilitação filial que o aluno está sendo matriculado.

## **08. Tela de vínculo do professor com o agrupamento de unidade**

Para realizar a associação entre agrupamento de unidade e professor, basta acessar o cadastro via anexo Professor existente no cadastro de Agrupamento de Unidade ou pelo anexo Agrupamento de unidade existente no cadastro de Professor:

#### **Associação automática de professores**

Foi implementado a funcionalidade para associar ao professor no momento da sua criação um agrupamento, este agrupamento será o contexto atual da operação.

## **09. Tela de sincronismo de aluno/professor com o agrupamento de unidade**

O processo de sincronismo (TOTVS Educacional | Configurações | Agrupamento de Unidade | Sincronizar) entre alunos/professores e agrupamento de unidade irá percorrer a coligada corrente em busca dos registros que são elegíveis para serem sincronizados (alunos/professores que não estão associados a nenhum agrupamento de unidade). Uma vez listados, os registros serão associados ao agrupamento de unidade do contexto que estão inseridos conforme regra citada anteriormente.

O controle de permissão para execução do processo é feito através do perfil do usuário:

**Observação:**

Para que o processo tenha efetividade na sua execução, deve-se configurar previamente os agrupamentos de unidades e os itens de agrupamento em cada um. Apenas dessa forma será possível localizar o agrupamento de unidade relacionado ao contexto do aluno/professor e realizar a associação entre eles.

]]>
