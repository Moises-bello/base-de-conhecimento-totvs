---
content_hash: 5210626ae2d8ef14ff7f6a1dd3969f99026e552039b703a9d4b53ae1d034cd8f
fetched_at: '2026-06-29T00:11:20.638752+00:00'
page_id: '687158765'
product: rm
source: tdn-rm
title: Histórico Dados Cadastrais Futuro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687158765
version: 96
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de Utilização**
4. **Tabelas Utilizadas**

## **01.****VERSÕES**

false

**A partir dos patches:**

* 12.1.2310.120
* e Superiores.

## **02.** **VISÃO GERAL**

Possibilitar a realização de alterações dos dados cadastrais do funcionário para competências futuras, sem a necessidade de alterar diretamente no cadastro do funcionário (PFUNC).

Para facilitar esse processo, disponibilizamos o parâmetro "Utiliza controle de Alteração de Dados Cadastrais futuro". Com essa configuração, o sistema passa a armazenar as alterações cadastrais futuras em um novo cadastro.

Para atualizar o cadastro do funcionário com essas alterações, o usuário pode parametrizar a atualização na liberação de competência ou executar o processo "Efetivar Dados Cadastrais".

É importante observar que nenhuma rotina do produto buscará o salário desse novo cadastro, continuando a buscar o salário do cadastro original do funcionário.

## **03. EXEMPLO DE UTILIZAÇÃO**

11ParametrizaçãoParametrização

1) Para atender essa demanda foi necessário a criação do anexo "Histórico Dados Cadastrais Futuro ", e para a liberação desse anexo é necessário a execução do script pelo aplicativo RM.Atualizador.exe.

2) Acesse o menu RH | Funcionário | Restrições Cadastrais  e marque o parâmetro  "**Utiliza Controle de Dados Cadastrais Futuro**".

3) Acesse o menu Serviços Globais| Segurança | Perfis

Selecione o sistema Folha de pagamento, edite o perfil desejado, vá em Acesso a Menus e permita o acesso (01.01.01.264 - Histórico Dados cadastrais Futuro: Visualizar | 01.01.01.265 - Histórico Dados cadastrais Futuro: Inserir | 01.01.01.266 - Histórico Dados cadastrais Futuro: Excluir | 01.01.01.267 - Histórico Dados cadastrais Futuro: Editar)

2Histórico Dados Cadastrais FuturoHistórico Dados Cadastrais Futuro

Para realizar o cadastro ou visualização manual para competência futura, deverá acessar o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Anexos | Históricos | Histórico Dados Cadastrais Futuro.

Visualize ou cadastre conforme demonstração abaixo. Nesta tela podemos alterar (Salario, Seção, Função e ou Rateio Fixo Futuro).

**ATENÇÃO:**

* Não poderá alterar o salário, função, seção ou rateio diretamente no cadastro do funcionário.
* Não poderá inserir alterações futuras diretamente nos anexos de Históricos de Salario, Histórico de Seção ou Histórico de Função.
* Para habilitar a aba Rateio Fixo Futuro deverá acessar o parametrizador Recursos Humanos | Configurações | Requisições|Requisições 2 e marcar o parâmetro "Habilitar o rateio de centro de custos em requisições".
3Alteração Global de SalárioAlteração Global de Salário

Para realizar a alteração salarial global para competência futura, deverá acessar o menu RH | Folha de Pagamento | Administração de Pessoal l Alteração de Salário.

1) Ao preencher o campo "**Data da Mudança**" com uma data posterior a competência atual, será apresentada a mensagem abaixo:

2) Ao avançar poderá realizar a alteração utilizando "Percentual | Fórmula ou Tabelas Salariais":

3) Ao finalizar o processo será apresentada a mensagem abaixo:

4Efetivação de RequisiçãoEfetivação de Requisição

Para realizar a alteração de dados cadastrais futuro através de requisições, deverá acessar o menu Gestão de Pessoas | Valorização | Requisições:

1) Realizar a requisição para competências posteriores a competência atual, em "Efetivar Transferência c/ Alterações de Dados Funcionais"s.

Nesta requisição é possível alterar: Salario, Seção, Função e Rateio Fixo.

2) Após a efetivação será apresentada a mensagem abaixo:

3) O sistema irá preencher os dados no "Histórico Dados Cadastrais Futuro" existente no cadastro do funcionário.

**OBSERVAÇÃO:**

* Quando houver mais de uma alteração na mesma data, o sistema irá acrescentar os minutos no campo data e será criado uma nova linha no Histórico de Dados Cadastrais Futuro.
* Esta implementação contemplará apenas quando houver mudança de seção para o mesmo CNPJ.
5Efetivar Dados CadastraisEfetivar Dados Cadastrais

Disponibilizado o processo RH | Administração Pessoal | Alterações Cadastrais | Efetivar Dados Cadastrais, que deverá ser utilizado quando o usuário não realizar a efetivação da alteração no momento da liberação de competência.

Após a execução deste processo o sistema irá:

* atualizar os dados cadastrais (PFUNC) que foram alterados através de uma requisição;
* criar o registro nos anexos dos históricos (Salarial, Seção, Função) que foram alterados na requisição;
* atualizar o rateio fixo no cadastro do funcionário;
* limpar os dados do anexo "Histórico Dados Cadastrais Futuro".

**OBSERVAÇÕES:**

* A efetivação somente poderá ser realizada quando a data de alteração for dentro da competência atual.
* O sistema não irá inserir registro nos anexos dos históricos com data anterior à próxima competência.
6Liberação de CompetênciaLiberação de Competência

No menu Folha Mensal | Liberação de Competência foi disponibilizado o parâmetro "**Efetivar Dados Cadastrais**", que ficará marcado como default, para que o usuário não esqueça de realizar a efetivação.

Quando o parâmetro estiver marcado, o sistema irá:

* atualizar os dados cadastrais (PFUNC);
* criar o registro nos anexos dos históricos (Salarial, Seção, Função)
* limpar os dados do anexo "Histórico Dados Cadastrais Futuro".

Quando o parâmetro estiver desmarcado, o sistema irá apresentar a mensagem de alerta abaixo:

7Transferência de FuncionáriosTransferência de Funcionários

Na rescisão individual por transferência, caso o funcionário que tenha alteração de dados cadastrais futuro, o sistema irá apresentar uma mensagem de alerta para que o usuário verifique a necessidade de excluir ou concluir (efetivar) a alteração dos dados cadastrais futuro antes de prosseguir com a transferência.

Caso queira apenas transferir o histórico de dados cadastrais futuro para a nova chapa basta clicar em <Sim> e prosseguir com a transferência.

**OBSERVAÇÃO:** Os históricos dos dados cadastrais somente são efetivado na competência atual ou na liberação de competência, ou seja, se houver um histórico de dados cadastrais futuro com data para o próximo mês, esta alteração não deve ser transferida para a chapa destino, o mesmo deverá ser excluído.

Na rescisão coletiva por transferência, caso o funcionário tenham alteração de dados cadastrais futuro, no final da execução do processo o sistema irá apresentar uma mensagem de alerta no log indicando a necessidade de excluir ou concluir (efetivar) a alteração de dados cadastrais futuro da chapa destino.

**OBSERVAÇÃO:** Como o processo coletivo não pode ser interrompido para excluir/efetivar o histórico de dados cadastrais futuro na chapa origem, caso o usuário deseje que essa informação não seja transferida para a chapa destino, sugerimos validar esse histórico antes de efetuar a rescisão coletiva por transferência.

## **04. TABELAS UTILIZADAS**

* PFHSTSALFUT, PFUNC.PFHSTSAL,PFUNC.CODSECAO, PFUNC.CODFUNCAO e PFRATEIOFIXO.CODCCUSTO
