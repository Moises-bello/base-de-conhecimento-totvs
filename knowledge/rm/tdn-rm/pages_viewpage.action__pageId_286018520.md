---
content_hash: ac94232de8766a7b0f7bb1f38896a3a05f358d27a451fa7f6ed6150a1ed66838
fetched_at: '2026-06-29T00:08:39.398190+00:00'
page_id: '286018520'
product: rm
source: tdn-rm
title: DT Movimentações bibliotecárias - WebService
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286018520
version: 109
---

* # Movimentações

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Bibliotecária |
| **Rotina:** | |  | | --- | | **Rotina** | | Movimentações | |
| **Cadastros Iniciais:** | Publicações / Exemplares / Usuários / Regras de empréstimos |
| **Parâmetro(s):** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | N/A |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER / ORACLE |
| **Tabelas Utilizadas:** | LEMPRESTIMOS |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada melhoria para possibilitar que as movimentações bibliotecárias (empréstimos, renovações, devoluções, cancelamentos e reservas) sejam consumidas via webservices disponibilizada pelos dataservers.

## Procedimento para Implantação

Estas melhorias estão disponíveis à partir da versão 12.1.18, é necessário somente ter os webservices publicados e disponíveis para acesso.

## Procedimento para Utilização

É possível realizar todas as movimentações bibliotecárias utilizando os dataserver consumindo via webservice, para que seja possível estas tarefas foram criados dataservers de movimentações e ajustado o dataserver de reserva.

DataServers utilizados:

**BibMovimentacaoWSEmprestimo** - Exclusivo para a movimentação de empréstimo.

**BibMovimentacaoWSDevRenCan** - Exclusivo para as movimentações de devoluções, renovações e cancelamento de empréstimos.

**BibReservaData** - Exclusivo para realizar reservas.

**Exemplo de utilização**

## **BibMovimentacaoWSEmprestimo:**

Este dataserver realiza somente empréstimos, ou seja, define uma publicação e um exemplar como emprestado para um determinado usuário, segue abaixo a descrição da funções:

**ReadView**: Retorna exatamente o mesma visão que o menu "visão de empréstimo" no RM.exe, neste item é possível obter informações sobre todos os empréstimos utilizando qualquer filtro possível.

Utilizando a ferramenta SOAP UI é possível verificar os resultados da função readview:

**ReadRecord**: A função readrecord carrega o objeto empréstimo validando regras de empréstimos e carregando todas as informações necessárias para a chamada da função saverecord para de fato confirma a operação, caso existam impedimentos com relação ao usuário ou a publicação e exemplar estes já serão validados também nesta função, estas mesmas regras também serão revalidadas na função saverecord, para garantir o máximo de integridade na operação.

Esta operação requer como chave primária o **código do usuário, código da publicação e código do exemplar** conforme pode ser verificado abaixo:

Exemplo de validação de impedimento financeiro: (parâmetro para validar impedimentos habilitado)

**SaveRecord**: Esta função utiliza os dados gerados pelo readrecord para confirmar a operação de empréstimo, ao confirmar o empréstimo será retornado a chave primária enviada na operação do readrecord.

## **BibMovimentacaoWSDevRenCan:**

Este dataserver realiza somente as operações de devoluções, renovações e cancelamentos, ou seja, utiliza de  empréstimos existentes para realizar as operações

**ReadView:**Retorna exatamente a mesma visão que o menu "visão de empréstimo" no RM.exe, neste item é possível obter informações sobre todos os empréstimos utilizando qualquer filtro possível. Exatamente como descrito no item readview do dataserver BibMovimentacaoWSEmprestimo.

**ReadRecord**: Esta função carrega o empréstimo que já existe no formato corretado para devolução, renovação ou cancelamento, é necessário que o empréstimo exista e esteja como "emprestado" (STATUSEMP = E), nesta função é necessário informar qual tipo de operação (TIPOMOVIMENTACAO) está sendo realizada:

* D = Devolução
* R = Renovação
* C = Cancelamento

Este campo é obrigatório e compõem a chave primária pois o sistema já irá fazer validações para cada tipo de operação, principalmente para o tipo de movimentação renovação.

Para a execução desta operação é necessário passar a chave primária como o **tipo da operação, código do empréstimo, código do usuário, código da publicação e código do e****xemplar**, os dados retornados devem ser utilizados para a operação de saverecord.

**SaveRecord**: A operação saverecord utiliza o xml gerado pelo readrecord para confirmar a operação definida no campo TIPOMOVIMENTACAO, ao confirmar a operação será retornado a chave informada no readrecord.

Se a devolução gerar algum tipo de valor financeiro é necessário configurar a tag <add key="**WebServiceCulture**" value="**Invariant**" /> conforme o documento: [Como Expor os Web Services](http://tdn.totvs.com/pages/viewpage.action?pageId=89620766).

Integração TOTVS Gestão Educacional

A partir da versão 12.1.2302 caso TOTVS Gestão Bibliotecária esteja integrado ao TOTVS Educacional, será necessário realizar o cadastro de Serviços Taxas de Bibliotecária para gerar a Taxa de cadastro de usuário, Taxa de empréstimo ou Taxa de multa.

Para saber mais [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=710556941).

Quando o usuário do empréstimo for um aluno, será exibido no XML do ReadRecord a(s) matrícula(s) desse aluno.

Para realizar o SaveRecord e o sistema conseguir salvar e gerar as parcelas referente as taxas bibliotecárias, deve ser passado no XML, as informações IDPERLET, CODTIPOCURSO e CODFILIALMATRIC.

**Observação:** Em alguns cenários, o aluno poderá estar matriculado em uma filial diferente da filial do TOTVS Gestão Bibliotecária onde ocorreu o empréstimo. Neste caso, o campo CODFILIALMATRIC deverá ser informado para indicar em qual filial serão gerados os contratos/parcelas das taxas bibliotecárias.

Caso o aluno, possua somente uma matrícula, esses campos já virão preenchidos.

Caso o aluno possua mais de uma matrícula, esses campos virão zerados e eles deverão ser informados manualmente, escolhendo em qual período letivo e qual nível de ensino deve ser gerado o contrato e as parcelas. Essa informação estará na tabela SMATRICPL exibida no XML.

**BibReservaData**

Este dataserver é responsável por criar reservas.

**ReadView**: Retorna a visão de reservas exatamente como no RM.exe.

**ReadRecord**: Carrega os dados de uma determinada reserva, neste método é necessário utilizar o **código da coligada e o código da reserva** como chave primária.

**SaveRecord**: Este método utiliza a estrutura gerada pelo readrecord para confirmar a reserva.

divs
