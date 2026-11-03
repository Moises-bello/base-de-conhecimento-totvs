---
content_hash: 6a65f4bc500a52d7682f063073970e8d3576ea5439713504c273f8e5b39654ed
fetched_at: '2026-06-29T00:10:43.193661+00:00'
page_id: '550306792'
product: rm
source: tdn-rm
title: Alteração CPF para eSocial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550306792
version: 32
---

## **ÍNDICE**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01.****VERSÕES :**

* 12.1.26.235
* 12.1.27.211
* 12.1.28.128
* e Superiores.

## **02.****VISÃO GERAL**

O CPF é um documento utilizado no eSocial como o principal identificador do trabalhador. O CPF é fundamental para a vinculação e aplicação de regras e validações do eSocial.

Em algumas situações, o CPF pode ser alterado pela Receita Federal do Brasil, impactando, assim, os cadastros desses trabalhadores no eSocial, por isso, o Comitê Gestor do eSocial orientou, por meio de Nota, quais os procedimentos necessários em casos de alteração de CPF do trabalhador no que tange o projeto.

Apesar da mudança no CPF ser um dado pessoal do trabalhador, essa alteração não pode ser feita através de um evento S-2205-Alteração de dado cadastrais.

Com isso, foi criado um processo no produto a fim de tratar esses casos excepcionais de alteração de número do CPF. Evitando assim, que o empregador tenha que excluir e reenviar com o novo CPF todos os eventos do trabalhador.

O procedimento foi baseado no envio de um evento de:

S-2299 – Desligamento seguido de um novo evento S-2200 – Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador ou

S-2399 - Trabalhador Sem Vínculo de Emprego/Estatutário seguido de um novo evento S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário - Início

**Atenção:**

Esse processo afeta todas as coligadas. Ao executa-lo serão alterados os campos CPF e matrícula eSocial.

Caso o CPF que está sendo processado seja encontrado em outras chapas e coligadas, a alteração também será aplicada a esses funcionários.

## **03. EXEMPLO DE UTILIZAÇÃO**

1true1Execução do scriptExecução do script

Para a liberação do processo de alteração CPF eSocial será necessário executar o script através do sistema RM.Atualizador.exe de sua versão.

true2ParametrizaçãoParametrização

Acesse o menu Serviços Globais | Segurança | Perfis

Selecione o sistema Folha de Pagamento, edite o perfil desejado, clique em Acesso a Menus e permita o acesso aos processos:

* 01.01.01.235 - Alteração CPF para eSocial: Visualizar e
* 01.01.01.236 -Alteração CPF para eSocial

3Execução do processoExecução do processo

Acesse o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários

Selecione o funcionário que deseja realizar a alteração de CPF, acesse Processos | Alteração de CPF eSocial

Cadastre o novo CPF e a data de alteração (essa data representa o inicio da validade do novo CPF) e clique em executar.

Sistema irá apresentar uma mensagem informando que a alteração ocorrerá em todas as chapas relacionadas ao CPF informado, isso para o caso do funcionário possuir múltiplos vínculos, mesmo que em outra coligada.

Para concluir a alteração clique em "Sim".

O processo será executado para a pessoa selecionada, mesmo no caso em que a pessoa esteja admitida em outra coligada a alteração será realizada.

Após a alteração o sistema irá:

1. Gerar um gatilho do evento S-2299 – Desligamento com o motivo 36 – “Mudança de CPF”, indicando na tag {novoCPF} o novo CPF do empregado;
2. Gerar um gatilho do evento S-2200 – Admissão, com a tag {tpAdmissao} preenchida com o valor 6 – “Mudança de CPF”, mantendo a data de admissão original do trabalhador;
3. Preencher o grupo {mudancaCPF} com os números de CPF e matrícula anteriores e com a data em que houve a alteração. O eSocial não permite que uma matrícula seja reaproveitada, portanto, quando o CPF é alterado, nova matrícula é atribuída ao trabalhador;

Deverá gerar os XMLs e enviar ao eSocial para a confirmação da alteração do CPF junto ao governo.

**Observação:**

* Caso possua algum evento não periódico com status "Gerado" na fila de eventos, o mesmo terá seu status retornado para "Pendente" para que seja gerado novamente com o CPF e Matricula eSocial atualizados.
* Caso possua algum evento periódico na fila de eventos, será necessário regerá-los, pois este evento não terá seu status alterado automaticamente.
* Não é possível a inclusão manual desses gatilhos com o tipo de operação Alteração CPF.
4Visualização da alteraçãoVisualização da alteração

Acesse o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários

Selecione o funcionário que deseja realizar a alteração de CPF vá em Anexos | Folha de Pagamento | Alteração de CPF eSocial

O sistema irá apresentará os campos abaixo referente a alteração realizada:

* CPF Anterior
* Matrícula eSocial Anterior
* Data Fim Validade: será o dia anterior ao dia informado no campo "Data de Alteração" na execução do processo de alteração de CPF.

5Alteração de CPF trabalhando com o mês caixaAlteração de CPF trabalhando com o mês caixaATENÇÃO - LEMBRETE

Para realizar a tratativa mencionada abaixo, é imprescindível executar o script por meio da versão correta do sistema RM.Atualizador.exe. Essa medida é necessária para criar um campo interno no produto, a fim de identificar o CPF  a ser considerado no evento S-1210.

**A partir dos patches:**

* 12.1.2209.235
* 12.1.2302.158
* 12.1.2306.103
* e Superiores

Quando ocorrer situação de troca de CPF em que um mês o funcionário tinha um número de CPF X, e no outro mês houver a alteração para novo número de CPF Y, o envio do  S-1210 deverá ser com o CPF da pessoa física pela qual as informações de base desse evento estejam atreladas com o que foi transmitida pelo S-1200.

**Exemplo:**

Funcionário tinha **CPF X** e teve alteração em 01/04/2023 para **CPF Y**

Envelope do mês 03 com pagamento em 04/2023

Envelope do mês 04 com pagamento em 04/2023

Envelope do mês 04 com pagamento em 05/2023

Serão gerados dois XML's do evento S-1210 para o mesmo <perApur> 04/2023, sendo um com o **CPF X**e <perRef> 03/2023 e outro com**CPF Y**e <perRef> 04/2023

1) Em 03/2023 o funcionário teve o envelope com a data de pagamento 05/04/2023:

2) Em 04/2023 o funcionário teve envelope com a data de pagamento 20/04/2023:

3) Em 04/2023 o funcionário teve o envelope com a data de pagamento 05/05/2023:

4) Em 01/04/2023, houve uma alteração de CPF para esse funcionário, ficando com histórico abaixo:

**Observação:** Devido à legislação de proteção de dados, não podemos exibir o código do CPF.

5) Geração do XML's:

Ao gerar o XML do evento S-1200 referente ao 03/2023, será informado o CPF anterior, conforme demostrado abaixo: 

**Observação:** Devido à legislação de proteção de dados, não podemos exibir o código do CPF.

Ao gerar o XML do evento S-1200 referente ao 04/2023, será informado o CPF atual, conforme demostrado abaixo: 

**Observação:** Devido à legislação de proteção de dados, não podemos exibir o código do CPF.

Ao gerar o XML do evento S-1210 para o período de apuração <perApur> 04/2023, serão gerados dois XML's, sendo um correspondente ao período referência 03/2023 e ao período referência 04/2023.

**Observação:** Devido à legislação de proteção de dados, não podemos exibir o código do CPF.

## **04. TABELAS UTILIZADAS**

* PFUNC, PFESOCIALCPF

|  |  |
| --- | --- |
|  | Informações Complementares |

---

[Funcionários](https://tdn.totvs.com/pages/viewpage.action?pageId=452719153)

]]>
