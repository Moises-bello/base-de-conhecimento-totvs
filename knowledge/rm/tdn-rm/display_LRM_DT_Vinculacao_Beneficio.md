---
content_hash: 54b683154d8e44150c7dbcfeb7d7955b62cee9553939f1ea9a66f5d033adea94
fetched_at: '2026-06-29T00:06:23.374637+00:00'
page_id: '224101206'
product: rm
source: tdn-rm
title: DT_Vinculacao_Beneficio
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Vinculacao_Beneficio
version: 3
---

# VINCULAÇÃO DE BENEFÍCIO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Benefícios* | *Benefícios* | |
| **Versões/Release:** | 12.1.9 |

## Descrição

O controle de benefícios serve para registrar os benefícios que a empresa possui e vinculá-los a uma seção de cargo/função e funcionário/dependente. Esta vinculação é feita para informar que a entidade escolhida pode ter aquele benefício.  
Além da vinculação existe a possibilidade de lançar o benefício ao funcionário/dependente de forma direta ou indireta, da qual o benefício é lançado para o funcionário/dependente proveniente de uma entidade como seção e/ou cargo/função.  
O vínculo de benefício serve para informar a elegibilidade de um benefício para o funcionário/dependente e o lançamento do benefício é a efetivação do benefício dado ao funcionário/dependente.

Um benefício vinculado pode ser associado ao funcionário/dependente por um tempo determinado. Com esta evolução, é possível consumir os web-services padrões do RM para manipular tanto a vinculação quanto o lançamento de benefícios.

Para o dependente receber o benefício o mesmo não necessariamente precisa estar para o funcionário, mas é necessário que no cadastro de benefício o mesmo esteja marcado como extensivo ao dependente.

## Procedimento para Utilização

**Cadastro de vinculação de benefício ao funcionário**

Através da visão de funcionários é possível abrir o anexo de Benefícios Vinculados ao Funcionário, onde será possível realizar a manutenção destes benefícios.  
Não é permitido a edição do registro, caso a informação seja cadastrada de forma errada, o mesmo tem que ser excluído. Sendo que esta exclusão é feita utilizando o processo de **Desvincular Beneficio.**

Acesse a visão de funcionários no sistema, selecione um funcionário, depois selecione o anexo: Benefícios / Benefícios vinculados ao funcionário. A partir daí, o sistema mostra a visão onde pode incluir o vínculo de um benefício.  
Na inclusão, o sistema permite apenas o cadastro de benefício não vinculados. Depois de informar o benefício não vinculado e a data da vinculação e salvar, o sistema irá grava as informações e o histórico das informações no banco de dados.

**Cadastro de lançamento de benefício ao funcionário**

Acesse RH / Gestão de Pessoas / Acompanhamento / Funcionários / Anexos / Benefícios Lançados ao Funcionário. Neste caminho é possível realizar a manutenção destes benefícios.

De acordo com o benefício lançado a ser selecionado, o sistema calcula automaticamente o valor do benefício, caso ele seja da natureza monetária e a opção da fórmula esteja selecionada no cadastro do benefício.  
O sistema não permite a vinculação de um mesmo benefício com data de vigência (data início e fim) ainda em andamento.   
Caso esteja configurado para validar o saldo de benefício e o mesmo tenha superado o limite, o sistema também não permite o lançamento.

Acesse RH / Gestão de Pessoas / Acompanhamento / Funcionários / Anexos / Benefícios Lançados ao Funcionário. Na inclusão o sistema permite apenas o cadastro de benefícios ainda não lançados.  
Depois que selecionar um benefício, o sistema de acordo com a configuração pode ou não calcular o valor do mesmo.   
Informe a data de lançamento e data de vigência (data início e fim, esta não sendo obrigatória). Caso deseje, o usuário também deve informar a periodicidade e a identificação do benefício lançado.   
Salve o lançamento de benefício que o sistema realiza as validações relativas a saldo (caso exista) e validação das datas informadas. Depois, o sistema irá gravar as informações e o histórico das informações no banco de dados.

**Processo de Desvincular Benefício do funcionário**

Através da visão de funcionários é possível abrir o anexo de Benefícios Vinculados ao Funcionário, onde o usuário pode executar o processo de Desvinculação do Benefício. Este processo serve para realizar a exclusão do benefício previamente vinculado ao funcionário.

**Processo de Cancelar Benefício do funcionário**

É possível executar o processo de Desvinculação do Benefício. Este processo serve para realizar a exclusão do benefício previamente lançado ao funcionário.

**Regras de validação de cadastro da vinculação do benefício ao funcionário/dependente.**

Tanto o benefício quanto a data de vinculação são obrigatórios de preenchimento. Caso não seja preenchido a data o sistema irá considerar a data atual do banco de dados para vinculação.  
Para os dependentes serão vinculados somente os benefícios extensíveis ao dependente, definidos no cadastro de benefício.

**Regras de validação de cadastro do lançamento do benefício ao funcionário/dependente.**

Os seguintes campos são obrigatórios: Benefício, data do cadastro e data início validade. Tanto a data do cadastro quanto a data de início de validade, caso não sejam preenchidas serão atribuídas com a data atual do banco de dados.  
A data fim de validade não pode ser menor que a data início de validade.  
A data de cadastro não pode ser maior que a data de início de validade.  
Caso exista integração dom o sistema de Folha de pagamento não é permitido lançamento fora da competência do sistema de Folha de pagamento.  
Caso o benefício selecionado seja do tipo monetário o sistema irá definir o valor com o valor informado no benefício ou calcular a formula para o valor do benefício.  
Caso o benefício selecionado não seja do tipo monetário não será possível informar um valor para o mesmo, ficando o campo desabilitado.  
O sistema irá validar o lançamento do benefício lançado para o funcionário através das regras de validação do grupo de benefícios.  
Caso esteja habilitado o sistema irá validar o controle de pontuação de benefícios.

**Cadastro de vinculação de benefício ao dependente**

Através da edição de funcionários é possível abrir o grid de dependente e por este anexo é possível abrir o anexo de Benefícios Vinculados ao dependente, onde é possível realizar a manutenção destes benefícios.  
Não é permitido a edição do registro, caso a informação seja cadastrada de forma errada, deve-se realizar a exclusão do registro. Sendo que esta exclusão deverá ser feita utilizando o processo de **Desvincular Benefício.**

**Cadastro de lançamento de benefício ao dependente**

Através da edição de funcionários é possível abrir o grid de dependentes e por este abrir o anexo de Benefícios Lançados ao dependente, onde é possível realizar a manutenção destes benefícios.  
Não é permitido a edição do registro, caso a informação seja cadastrada de forma errada, deve-se realizar a exclusão do registro. Sendo que esta exclusão deverá ser feita utilizando o processo de **Cancelar Benefício**

De acordo com o benefício lançado a ser selecionado o sistema irá calcular automaticamente o valor do benefício, caso ele seja da natureza monetária e a opção da fórmula esteja selecionada no cadastro do benefício.  
O sistema não permite a vinculação de um mesmo benefício com data de vigência (data início e fim) ainda em andamento.  
Caso esteja configurado para validar o saldo de benefício e o mesmo tenha superado o limite o sistema também não permitirá o lançamento.

**Processo de Desvincular Benefício do dependente**

Através da edição de funcionários é possível abrir o grid de dependentes e por ela abrir o anexo de Benefícios Vinculados ao dependente, onde é possível executar o processo de Desvinculação do Benefício. Este processo serve para realizar a exclusão do benefício previamente vinculado ao dependente.

É possível selecionar o grid de dependentes e por ele abrir o anexo de Benefícios Lançados ao dependente, onde é possível executar o processo de Desvinculação do Benefício. Este processo serve para realizar a exclusão do benefício previamente lançado ao dependente.
