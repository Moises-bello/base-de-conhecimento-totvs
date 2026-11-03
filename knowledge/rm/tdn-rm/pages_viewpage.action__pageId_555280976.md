---
content_hash: 3f6e4f4e065b3e29322a6aa8246b722e81357274927867511bb3e716f4f60619
fetched_at: '2026-06-29T00:10:46.674753+00:00'
page_id: '555280976'
product: rm
source: tdn-rm
title: Cópia de Alteração CPF para eSocial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=555280976
version: 1
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

## **04. TABELAS UTILIZADAS**

* PFUNC, PFESOCIALCPF

|  |  |
| --- | --- |
|  | Informações Complementares |

---

[Funcionários](https://tdn.totvs.com/pages/viewpage.action?pageId=452719153)

]]>
