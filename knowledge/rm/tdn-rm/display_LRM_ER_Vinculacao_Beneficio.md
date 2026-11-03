---
content_hash: 3a2ba079d6ec1559279f22a7ae4921a1083817ff0d0c32330b66d2f3bb08b479
fetched_at: '2026-06-29T00:06:09.398644+00:00'
page_id: '203753539'
product: rm
source: tdn-rm
title: ER_Vinculacao_Beneficio
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Vinculacao_Beneficio
version: 3
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** |  | | |
| **Projeto1** |  | **IRM1** |  |
| **Requisito1** |  | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** |  |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Atualmente no sistema de Gestão de Pessoas existe o controle de benefícios onde são registrados os benefícios que a empresa possui e os mesmos são vinculados a seção, cargo/função e funcionário/dependente. Esta vinculação é feita de forma a informar que a entidade escolhida pode ter aquele benefício.

Além da vinculação existe a possibilidade de lançar o benefício ao funcionário/dependente de forma direta ou indireta, da qual o benefício é lançado para o funcionário/dependente proveniente de uma entidade como seção e/ou cargo/função.

Tanto a vinculação quanto o lançamento são feitos hoje através de processos existentes no sistema, dificultando um pouco o dia-a-dia do usuário, pois o mesmo tem que entrar em um assistente de processo para vincular ou lançar o benefício ao funcionário/dependente.

O objetivo deste projeto é que seja criada a vinculação e lançamento de benefícios através de cadastros, utilizando as telas de anexos que já existem atualmente, mas que apenas apresentam a visão do que foi gerado através dos processos mencionados acima.

Para melhor esclarecimento, o vínculo de benefício serve para informar a elegibilidade de um benefício para o funcionário/dependente e o lançamento do benefício é a efetivação do benefício dado ao funcionário/dependente.

Lembrando que um benefício vinculado pode ser associado ao funcionário/dependente por um tempo determinado.

Outra informação relevante é que para o dependente receber o benefício o mesmo não necessariamente precisa estar para o funcionário, mas é necessário que no cadastro de benefício o mesmo esteja marcado como extensivo ao dependente.

## Definição da Regra de Negócio

Lembrando que um benefício vinculado pode ser associado ao funcionário por um tempo determinado.

Com esta evolução também será possível consumir os webservices padrões do RM para manipular tanto a vinculação quanto o lançamento de benefícios.

**Req. 01: Cadastro de vinculação de benefício ao funcionário**

Através da visão de funcionários é possível abrir o anexo de Benefícios Vinculados ao Funcionário, onde será possível realizar a manutenção destes benefícios.

Não será permitido a edição do registro, caso a informação seja cadastrada de forma errada, deve-se realizar a exclusão do registro. Sendo que esta exclusão deverá ser feita utilizando o processo de **Desvincular Beneficio**, que será melhor detalhado no Requisito 03 desta documentação.

As demais regras de validação do cadastro estão registradas no Req. 05.

**Fluxo Principal:**

1. O usuário acessa a visão de funcionários.
2. O sistema exibirá a tela de visão de funcionários.
3. O usuário seleciona um funcionário.
4. O usuário seleciona o anexo: Benefícios / Benefícios vinculados ao funcionário.
5. O sistema mostrará a visão onde o usuário poderá incluir o vínculo de um benefício.
6. Na inclusão o sistema permitirá apenas o cadastro de benefícios ainda não vinculados.
7. O usuário informará o benefício ainda não vinculado e a data de vinculação.
8. O usuário salva o vínculo de benefício.
9. O sistema grava as informações no banco de dados.
10. O sistema grava o histórico da informação registrada no banco de dados.

**Req. 02: Cadastro de lançamento de benefício ao funcionário**

Através da visão de funcionários é possível abrir o anexo de Benefícios Lançados ao Funcionário, onde será possível realizar a manutenção destes benefícios.

Não será permitido a edição do registro, caso a informação seja cadastrada de forma errada, deve-se realizar a exclusão do registro. Sendo que esta exclusão deverá ser feita utilizando o processo de **Cancelar Beneficio**, que será melhor detalhado no Requisito 04 desta documentação.

De acordo com o benefício lançado a ser selecionado o sistema irá calcular automaticamente o valor do benefício, caso ele seja da natureza monetária e a opção da formula esteja selecionada no cadastro do benefício.

O sistema não permitirá a vinculação de um mesmo benefício com data de vigência (data início e fim) ainda em andamento.

Caso esteja configurado para validar o saldo de benefício e o mesmo tenha superado o limite o sistema também não permitirá o lançamento.

As demais regras de validação do cadastro estão registradas no Req. 06.

**Fluxo Principal:**

1. O usuário acessa a visão de funcionários.
2. O sistema exibirá a tela de visão de funcionários.
3. O usuário seleciona um funcionário.
4. O usuário seleciona o anexo: Benefícios / Benefícios lançados ao funcionário.
5. O sistema mostrará a visão onde o usuário poderá incluir lançamento de um benefício.
6. Na inclusão o sistema permitirá apenas o cadastro de benefícios ainda não lançados.
7. O usuário seleciona um benefício e o sistema de acordo com a configuração pode ou não calcular o valor do mesmo.
8. O usuário deve informar a data de lançamento e data de vigência (data início e fim, esta não sendo obrigatória). Caso deseje o usuário também deve informar a periodicidade e a identificação do benefício lançado.
9. O usuário salva o lançamento de benefício.
10. O sistema realiza as validações relativas a saldo (caso exista) e validação das datas informadas.
11. O sistema grava as informações no banco de dados.
12. O sistema grava o histórico da informação registrada no banco de dados.

**Req. 03: Processo de Desvincular Benefício do funcionário**

Através da visão de funcionários é possível abrir o anexo de Benefícios Vinculados ao Funcionário, onde será possível executar o processo de Desvinculação do Benefício.

Este processo servirá para realizar a exclusão do benefício previamente vinculado ao funcionário.

**Fluxo Principal:**

1. O usuário acessa a visão de funcionários.
2. O sistema exibirá a tela de visão de funcionários.
3. O usuário seleciona um funcionário.
4. O usuário seleciona o anexo: Benefícios / Benefícios vinculados ao funcionário.
5. O sistema mostrará a visão onde o usuário deverá escolher um benefício vinculado.
6. O usuário deverá executar o processo nesta visão, selecionando Processos / Desvincular Benefício.
7. O sistema irá abrir a tela de processo para que o usuário informe a data de desvinculação do benefício.
8. O usuário informa uma data de desvinculação e clica em executar.
9. O sistema realiza a exclusão da informação e atualiza o registro de histórico (caso exista) com a data de desvinculação.

**Req. 04: Processo de Cancelar Benefício do funcionário**

Através da visão de funcionários é possível abrir o anexo de Benefícios Lançados ao Funcionário, onde será possível executar o processo de Desvinculação do Benefício.

Este processo servirá para realizar a exclusão do benefício previamente lançado ao funcionário.

**Fluxo Principal:**

1. O usuário acessa a visão de funcionários.
2. O sistema exibirá a tela de visão de funcionários.
3. O usuário seleciona um funcionário.
4. O usuário seleciona o anexo: Benefícios / Benefícios lançados ao funcionário.
5. O sistema mostrará a visão onde o usuário deverá escolher um benefício lançado.
6. O usuário deverá executar o processo nesta visão, selecionando Processos / Cancelar Benefício.
7. O sistema irá abrir a tela de processo para que o usuário informe a data de cancelamento do benefício, caso a mesma já não tenha sido informada como data de termino.
8. O usuário informa uma data de cancelamento e clica em executar.
9. O sistema realiza a exclusão da informação e atualiza o registro de histórico (caso exista) com a data de cancelamento informada no campo de data termino.

**Req. 05: Regras de validação de cadastro da vinculação do benefício ao funcionário/dependente.**

* Não será permitido a vinculação do mesmo benefício com mesma data de vinculação. Caso exista a necessidade de vincular novamente com mesma data de vinculo, deverá ser previamente excluído o histórico da vinculação no cadastro de histórico de vínculo de benefício ao funcionário.
* Tanto o benefício quanto a data de vinculação são obrigatórios de preenchimento. Caso não seja preenchido a data o sistema irá considerar a data atual do banco de dados para vinculação.
* Para os dependentes somente serão vinculados os benefícios extensíveis ao dependente, definidos no cadastro de benefício.

**Req. 06: Regras de validação de cadastro do lançamento do benefício ao funcionário/dependente.**

* Não será permitido a vinculação do mesmo benefício com mesma data de vinculação. Caso exista a necessidade de vincular novamente com mesma data de vinculo, deverá ser previamente excluído o histórico da vinculação no cadastro de histórico de vínculo de benefício ao funcionário.
* Os seguintes campos são obrigatórios: Benefício, data do cadastro e data início validade. Tanto a data do cadastro quanto a data de início de validade, caso não sejam preenchidas serão atribuídas com a data atual do banco de dados.
* A data fim de validade não pode ser menor que a data início de validade.
* A data de cadastro não pode ser maior que a data de início de validade.
* Caso exista integração dom o sistema de Folha de pagamento não será permitido lançamento fora da competência do sistema de Folha de pagamento.
* Caso o benefício selecionado seja do tipo monetário o sistema irá definir o valor com o valor informado no benefício ou calcular a formula para o valor do benefício.
* Caso o benefício selecionado não seja do tipo monetário não será possível informar um valor para o mesmo, ficando o campo desabilitado.
* O sistema irá validar o lançamento do benefício lançado para o funcionário através das regras de validação do grupo de benefícios.
* Caso esteja habilitado o sistema irá validar o controle de pontuação de benefícios.

**Req. 07: Cadastro de vinculação de benefício ao dependente**

Através da edição de funcionários é possível abrir o grid de dependente e por este anexo é possível abrir o anexo de Benefícios Vinculados ao dependente, onde será possível realizar a manutenção destes benefícios.

Não será permitido a edição do registro, caso a informação seja cadastrada de forma errada, deve-se realizar a exclusão do registro. Sendo que esta exclusão deverá ser feita utilizando o processo de **Desvincular Benefício**, que será melhor detalhado no Requisito 09 desta documentação.

As demais regras de validação do cadastro estão registradas no Requisito 05.

**Fluxo principal**

1. O usuário acessa a visão de funcionários.
2. O sistema exibirá a tela de visão de funcionários.
3. O usuário seleciona um funcionário.
4. O usuário edita o registro do funcionário.
5. O usuário seleciona a opção de dependentes.
6. O usuário edita um dependente.
7. O usuário seleciona o anexo: Benefícios / Benefícios vinculados ao dependente.
8. O sistema mostrará a visão onde o usuário poderá incluir o vínculo de um benefício.
9. Na inclusão o sistema permitirá apenas o cadastro de benefícios ainda não vinculados e os benefícios que estiverem marcados com a opção de extensão para o dependente.
10. O usuário informará o benefício ainda não vinculado e a data de vinculação.
11. O usuário salva o vínculo de benefício.
12. O sistema grava as informações no banco de dados.
13. O sistema grava o histórico da informação registrada no banco de dados.

**Req. 08: Cadastro de lançamento de benefício ao dependente**

Através da edição de funcionários é possível abrir o grid de dependentes e por este abrir o anexo de Benefícios Lançados ao dependente, onde será possível realizar a manutenção destes benefícios.

Não será permitido a edição do registro, caso a informação seja cadastrada de forma errada, deve-se realizar a exclusão do registro. Sendo que esta exclusão deverá ser feita utilizando o processo de **Cancelar Benefício**, que será melhor detalhado no Requisito 10 desta documentação.

De acordo com o benefício lançado a ser selecionado o sistema irá calcular automaticamente o valor do benefício, caso ele seja da natureza monetária e a opção da formula esteja selecionada no cadastro do benefício.

O sistema não permitirá a vinculação de um mesmo benefício com data de vigência (data início e fim) ainda em andamento.

Caso esteja configurado para validar o saldo de benefício e o mesmo tenha superado o limite o sistema também não permitirá o lançamento.

As demais regras de validação do cadastro estão registradas no Requisito 06.

**Fluxo principal**

1. O usuário acessa a visão de funcionários.
2. O sistema exibirá a tela de visão de funcionários.
3. O usuário seleciona um funcionário.
4. O usuário edita o registro do funcionário.
5. O usuário seleciona a opção de dependentes.
6. O usuário edita um dependente.
7. O usuário seleciona o anexo: Benefícios / Benefícios lançados ao dependente.
8. O sistema mostrará a visão onde o usuário poderá incluir lançamento de um benefício.
9. Na inclusão o sistema permitirá apenas o cadastro de benefícios ainda não lançados.
10. O usuário seleciona um benefício e o sistema de acordo com a configuração pode ou não calcular o valor do mesmo.
11. O usuário deve informar a data de lançamento e data de vigência (data início e fim, esta não sendo obrigatória). Caso deseje o usuário também deve informar a periocidade e a identificação do benefício lançado.
12. O usuário salva o lançamento de benefício.
13. O sistema realiza as validações relativas a saldo (caso exista) e validação das datas informadas.
14. O sistema grava as informações no banco de dados.
15. O sistema grava o histórico da informação registrada no banco de dados.

**Req. 09: Processo de Desvincular Benefício do dependente**

Através da edição de funcionários é possível abrir o grid de dependentes e por ela abrir o anexo de Benefícios Vinculados ao dependente, onde será possível executar o processo de Desvinculação do Benefício.

Este processo servirá para realizar a exclusão do benefício previamente vinculado ao dependente.

**Fluxo principal**

1. O usuário acessa a visão de funcionários.
2. O sistema exibirá a tela de visão de funcionários.
3. O usuário seleciona um funcionário.
4. O usuário edita o funcionário.
5. O usuário seleciona o grid de dependentes
6. O usuário edita um dependente.
7. O usuário seleciona o anexo: Benefícios / Benefícios vinculados ao dependente.
8. O sistema mostrará a visão onde o usuário deverá escolher um benefício vinculado.
9. O usuário deverá executar o processo nesta visão, selecionando Processos / Desvincular Benefício.
10. O sistema irá abrir a tela de processo para que o usuário informe a data de desvinculação do benefício.
11. O usuário informa uma data de desvinculação e clica em executar.
12. O sistema realiza a exclusão da informação e atualiza o registro de histórico (caso exista) com a data de desvinculação.

**Req. 10: Processo de Cancelar Benefício do dependente**

Através da edição de funcionários é possível selecionar o grid de dependentes e por ele abrir o anexo de Benefícios Lançados ao dependente, onde será possível executar o processo de Desvinculação do Benefício.

Este processo servirá para realizar a exclusão do benefício previamente lançado ao dependente.

****Fluxo principal****

1. O usuário acessa a visão de funcionários.
2. O sistema exibirá a tela de visão de funcionários.
3. O usuário seleciona um funcionário.
4. O usuário edita o registro do funcionário.
5. O usuário seleciona o grid de dependentes.
6. O usuário edita um dependente.
7. O usuário seleciona o anexo: Benefícios / Benefícios lançados ao dependente.
8. O sistema mostrará a visão onde o usuário deverá escolher um benefício lançado.
9. O usuário deverá executar o processo nesta visão, selecionando Processos / Cancelar Benefício.
10. O sistema irá abrir a tela de processo para que o usuário informe a data de cancelamento do benefício, caso a mesma já não tenha sido informada como data de termino.
11. O usuário informa uma data de cancelamento e clica em executar.
12. O sistema realiza a exclusão da informação e atualiza o registro de histórico (caso exista) com a data de cancelamento informada no campo de data termino.

## Protótipo de Tela

## Fluxo do Processo

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
