---
content_hash: 4ddb116e96218a04e1a0af8b96ab5bda832dd9ca630c4c905927d4f8ffb6c914
fetched_at: '2026-06-29T00:09:18.718784+00:00'
page_id: '421388760'
product: rm
source: tdn-rm
title: Ativar Sessão de Caixa 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388760
version: 17
---

Descontinuação do Módulo de Caixa 1.0

A partir da release 12.1.2510, o **Módulo de Caixa 1.0** será **descontinuado** e não estará mais acessível no TOTVS Gestão Financeira.

A solução oficial e mantida pela TOTVS para os recebimentos presenciais será exclusivamente o **Módulo de Caixa 2.0**, já disponível e que oferece mais recursos, melhor performance e maior aderência às melhores práticas.

Recomendamos que as empresas realizem a migração para o **Módulo de Caixa 2.0** o quanto antes, garantindo continuidade operacional, suporte técnico e acesso às inovações da solução.

Para mais informações sobre a nova funcionalidade, consulte a [documentação nesse link](https://tdn.totvs.com/pages/viewpage.action?pageId=744486517).

Ao ativar a Sessão de Caixa se marcado o parâmetro "Obrigatória a impressão de abertura do caixa" a tela para autenticação será exibida. Se o operador não imprimir a autenticação na abertura do Caixa o sistema inviabilizará as operações.

**Guia Financeiro**

Interface do Caixa

Na parte superior serão apresentados os dados da sessão de caixa aberta:

Operador

Será apresentado o nome do usuário que está operando a sessão aberta.

Sessão

Será apresentado o número da sessão de caixa aberta.

Caixa nº

O número do caixa corresponde à quantidade de caixas abertos na conta caixa selecionada.

Conta Caixa

Será apresentado o código da conta caixa selecionada na abertura.

Data e Hora da Abertura

Será apresentada a data em que o módulo de caixa está operando. Ao ativar a Sessão de Caixa essa data é apresentada por default com a data do sistema, podendo ser alterada a conforme configuração definida no perfil de acesso do usuário.

Informação

Este ícone possibilita visualizar as dados da sessão caixa as permissões definidas na abertura e os saldos atuais, como saldo inicial, saldo dos lançamentos a pagar e o saldo dos lançamentos a receber, se houver permissão concedida.

Histórico

Este ícone possibilita visualizar todas as movimentações realizadas na sessão de caixa que está aberta.

**Processos**

Após ativar a sessão o operador poderá dar início às atividades:

Baixa

Será possível baixar os lançamentos que foram pesquisados através da tela de pesquisa. Conforme definido nos parâmetros poderá imprimir o recibo de baixa e a autenticação mecânica da baixa do lançamento. No momento da baixa de vários lançamentos pode escolher "Gerar um extrato de caixa para cada lançamento" ou "Gerar um extrato de caixa para todos os lançamentos".

Estorno

Será possível estornar os lançamentos selecionados na tela de pesquisa inclusive os lançamentos baixados em outra sessão se a permissão para esta função estiver sido marcada na abertura do caixa.

Incluir Lançamento

Será possível incluir lançamentos de qualquer natureza se o usuário tiver permissão aos campos incluir lançamentos a pagar e incluir lançamentos a receber.

Editar Lançamento

Será possível editar um lançamento incluído pela sessão de caixa ou mesmo através da Visão Geral de Lançamentos.

Serviço Extra

Este menu possibilita a geração de lançamentos financeiros a receber através do serviço do Classis Ensino Básico/Superior.

Estes lançamentos gerados poderão ser serviços extras que não foram incluídos no plano de pagamento do aluno como aula de reforço etc.

Para executar o processo é preciso preencher os campos:

* **Filial:** Informar a filial do lançamento;
* **Nível de Ensino:** Informar o nível de ensino do aluno que será inserido o serviço extra;
* **Período Letivo:** Informar o período letivo do aluno;
* **Aluno:** Informar o aluno para o qual será inserido o serviço extra;
* **Contrato:** Será apresentado neste campo o contrato educacional para o qual será inserido uma parcela de serviço extra;
* **Parcela:** Informar qual o número da parcela será inserido o serviço extra criado;
* **Cota:** Informar a cota da parcela;
* **Data de Emissão:** Será carregada com a data atual;
* **Data de Vencimento:** Informar a data de vencimento do lançamento de serviço extra que está sendo inserido;
* **Serviço:** Informar o serviço extra que será utilizado;
* **Valor:** Informar o valor da parcela que está sendo inserido.

Melhoria

O  processo de geração de lançamento do financeiro, foi evoluido, para permitir inserir mais de uma parcela, cota ou serviço no mesmo processo, sem ter a necessidade que fecha-lo e abrir-lo novamente.

Esta melhoria está disponível apartir do patch:

* Versão 12.1.31 => **12.1.31.204**
* Versão 12.1.32 => **12.1.32.140**

Incluir Extrato

Poderá incluir extrato de caixa de qualquer natureza desde que tenha permissão de acesso ao campo e imprimir recibo de extrato.

Valor Líquido

Poderá visualizar a tela de calculo do valor líquido do lançamento selecionado através da tela de pesquisa.

Desativar Sessão

Poderá desativar a sessão de caixa aberta de forma que a mesma não será encerrada e poderá ativar esta sessão a qualquer momento pelo operador designado na abertura.

Fechar sessão

Poderá encerrar a sessão de caixa aberta se a permissão de acesso estiver marcada.

Recebimento via cheque

Esta funcionalidade permitirá ao usuário efetuar o recebimento via cheque para lançamentos a receber.

A permissão de Recebimento via cheque na sessão de caixa está disponível no cadastro do perfil do usuário que será associado ao usuário do operador do caixa.  
A opção de Recebimento via cheque estará disponível na interface da sessão de caixa, após a habilitar a permissão de acesso.

As opções de agrupamento do cheque serão:

* Um cheque para todos os lançamentos;
* Um cheque para cada lançamento;
* Um cheque para cada cliente / fornecedor.

Para as duas últimas opções de agrupamento, será disponibilizada as opções de:

* Informar dados somente uma vez;
* Replicar banco, agencia, conta corrente e forma de pagamento para todos os cheques.   
  Para a baixa de lançamento que possui recebimento via cheque, será apresentada uma caixa de diálogo, para que o operador possa confirmar a baixa, caso não tenha certeza basta clicar em não.

**Guia Educacional**

Após integrar os módulos será possível pesquisar lançamentos do Educacional além de poder executar processos de baixa, estorno e edição. A pesquisa poderá ser feita pelo nome do aluno ou pelo responsável financeiro do mesmo.

**Status Boleto**

O filtro serve para buscar os boletos relacionados ao lançamento.

Caso o parâmetro em Contas a Receber | Baixas | Baixa a receber | "Não gerar outro boleto para lançamento após a baixa parcial" estiver marcado, ao realizar o filtro pelo "Status Boleto", será apresentado na visão da sessão de caixa o lançamento com Status "Baixado Parcialmente".Se o parâmetro "Não gerar outro boleto para lançamento após a baixa parcial" estiver desmarcado o sistema irá apresentar o lançamento financeiro com cada boleto associado, sendo que cada boleto terá seu status ("Em aberto" e "Baixado").

Atenção ao uso do campo DATAHORAULTIMAATIVIDADE 

Até a release 12.1.2506, o campo **DATAHORAULTIMAATIVIDADE** da tabela **FSESSAOCAIXA** era atualizado sempre que a sessão era ativada. A partir da release 12.1.2510, esse campo deixará de ser atualizado no momento da ativação da sessão de caixa. Caso essa informação seja utilizada em relatórios ou consultas, recomenda-se revisá-los antes da descontinuação.
