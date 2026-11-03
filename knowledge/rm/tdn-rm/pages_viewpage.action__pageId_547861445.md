---
content_hash: ae48563aacb2aa9c1030b87bd800d3616b35eb08d7831124242df8ef6f9b5ef7
fetched_at: '2026-06-29T00:10:42.851053+00:00'
page_id: '547861445'
product: rm
source: tdn-rm
title: 2.13 Baixa de Lançamento por Sessão de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547861445
version: 27
---

|  |  |
| --- | --- |
| Descrição | Sessão de Caixa |
| Observações | O objetivo do Módulo de Caixa (sessão de caixa) é, por meio de uma interface simples e objetiva, facilitar os recebimentos e pagamentos pela Tesouraria/Secretária, face às suas atribuições. |

Para realizar este procedimento, o usuário deverá acessar o Módulo Gestão Financeira e selecionar: Caixa |  Abrir Nova e seguir os passos abaixo.

O Sistema apresentada a tela de abertura de nova sessão de caixa, o usuário deve preencher os campos conforme a seguir:

* **Operador:** Clicar no ícone () para selecionar o operador do caixa;
* **Conta Caixa:** Clicar no ícone () para selecionar a conta caixa;
* **Caixa Nº**: Informar o número do caixa;
* **Código da Filial:** Informar a filial a ser utilizada na sessão de caixa;
* **Permissão**:
  + **Recebimentos:** Selecionar esta opção para registrar apenas os recebimentos na Sessão de Caixa;
  + **Pagamentos:** Selecionar esta opção para registrar apenas o pagamento na Sessão de Caixa;
  + **Ambos:** Selecionar esta opção para registrar pagamentos e recebimentos na Sessão de Caixa;
  + **Fechamento:** Selecionar esta opção se será permitido pelo operador fazer o fechamento da Sessão de Caixa;
  + **Emissão de Relatório de Fechamento de Caixa**: Selecionar esta opção se será permitido emitir o relatório de fechamento de caixa;
  + **Consulta Saldo:** Selecionar esta opção para permitir ao usuário consultar saldos da conta caixa;
  + **Estorna Lançamento Baixado em outra Sessão:** Selecionar esta opção se será permitido estornar baixa de lançamentos realizadas em outra sessão de caixa;
  + **Saldo Inicial:** Informar o saldo inicial do caixa que está sendo iniciado;
  + **Saldo por Operador:** Clicando neste botão, será carregado o saldo do operador sem que seja considerado número da caixa ou valor informado no campo saldo inicial;
  + **Saldo por nº de caixa**: Clicando neste botão, será carregado o saldo do caixa para o campo saldo inicial.
  + **Habilita PIX:** Marcar essa opção ao abrir a sessão de caixa para realizar o recebimento com PIX, e ao fazer a baixa deverá ser selecionado um meio de pagamento cadastrado com o tipo primitivo *PIX*. Atenção: O TOTVS Pagamento Digital deve estar configurado.

Após preencher todas as informações da Sessão de Caixa, o usuário deve clicar no botão “Abrir” no ícone , para abrir nova sessão.

# 2.13.1 Ativar Sessão de Caixa

Para ativar a sessão de caixa o usuário deverá selecionar a opção "ativar:

Assim que ativada será aberta a sessão de caixa para que o usuário possa realizar as operações financeiras através da sessão de caixa.

 Clicando neste botão, será apresentada a tela com as informações a respeito da Sessão de Caixa, tais como: valores já baixados, saldo de lançamentos a receber e pagar baixados, operador, conta caixa, permissões que o operador/usuário possui na sessão, entre outras.

Clicando neste botão, será apresentada tela com todos histórico da sessão de caixa. Apresentando todas as baixas, inclusões, entre outras.

# 2.13.2 Baixas de Lançamentos na Sessão de Caixa

Para registrar as baixas de lançamentos através da sessão de caixa, é necessário realizar a busca dos lançamentos que deseja baixar.

Para isso, o usuário de utilizador um ou mais campos de pesquisa disponíveis na tela da sessão de caixa.

* **Número do Documento:** Informar o número do documento que deseja pesquisar;
* **Cliente/Fornecedor:** Informar o cliente que deseja pesquisar;
* **Código de barra:** Realizar a leitura do código de barras de um boleto;
* **Lançamento:** Informar a referência do lançamento financeiro que deseja pesquisar;
* **IPTE:** Informar a linha de digitação do boleto que deseja pesquisar;
* **Nosso número:** Informar o nosso número do boleto que deseja pesquisar.

Em casos de lançamentos originados do Módulo Educacional, o usuário pode pesquisar também através da pasta Educacional na área de pesquisa conforme tela a seguir.

# 

Nesta pasta Educacional, o usuário pode informar seguintes os campos:

* **Aluno:** Informar o aluno que deseja pesquisar;
* **Responsável pelo(s) lançamento(s) do aluno:** Este campo será preenchido automaticamente com o responsável financeiro do aluno, entretanto em casos que o aluno tem mais de um responsável poderá escolher qual responsável deseja pesquisar.
* **Status Lançamento:**
  + **Aberto/Baixa Parcial:** Marcando esta opção serão listados lançamentos com estes status.
  + **Baixados:** Marcando esta opção serão listados os lançamentos baixados.

Após informar os campos necessários, o usuário deve clicar no botão “Pesquisar” no ícone .

Ao realizar a pesquisa, o Sistema apresentará a tela com os lançamentos encontrados.

Os lançamentos serão apresentados na tela da sessão de caixa para que sejam baixados. O usuário deve selecionar o(s) lançamento(s) que deseja baixar e clicar no botão “Baixa” no ícone , em seguida, será apresentada a tela para registro da baixa.

Nesta etapa serão visualizadas as informações dos lançamentos e boletos que estão sendo baixados.

Após clicar em “Avançar”, o usuário deve informar o meio de recebimento utilizado para receber os valores.

Será apresentada a tela para edição do meio de pagamento, o usuário deve escolher o meio de pagamento (Ex.: Dinheiro, Cheque, Cartão, etc).

* **Valor:** Informar o valor que está sendo baixado neste meio de pagamento;
* **Conta Caixa:** Informar a conta caixa que está recebendo os valores. Sempre será carregada a conta caixa do lançamento financeiro;
* **Compensar no Extrato:** Marcando esta opção Sistema já irá compensar o extrato bancário;
* **Data Compensação Extrato:** Informar a data de compensação do extrato bancário.

Para os casos de baixa realizadas em cheque, o procedimento mudará apenas neste momento da seleção do meio de pagamento.

O usuário deve selecionar o meio de pagamento “Cheque” e clicar no botão “Cheque” para preencher as informações descritas a seguir.

Será apresentada a tela com as informações do cheque a serem preenchidas, tais como:

* **Número do Documento:** Informar o número do cheque;
* **Valor:** Será preenchido de acordo com o valor informado na baixa;
* **Filial:** Será preenchida automaticamente;
* **Departamento:** Informar o departamento;
* **Centro de Custo:** Informar o centro de custo.

Na aba “Dados Adicionais”, o usuário deve preencher:

* **Banco:** Informar o banco do cheque;
* **Agência:** Informar a agência do cheque;
* **Data de Vencimento:** Informar a data de vencimento/Compensação do cheque.

Neste momento, o Sistema apresenta novamente a tela de baixa do lançamento com o meio de pagamento informado. O usuário deve clicar em “Avançar” para dar continuidade à baixa.

O Sistema apresentará a tela com informação o processo de baixa de lançamento foi realizado com sucesso.

Ao final do processo de baixa, o usuário poderá visualizar/imprimir o recibo disponibilizado na visão.

# 2.13.3 Estorno de Baixa pela Sessão de Caixa

Para realizar o estorno (cancelamento), o usuário deve pesquisar os lançamentos conforme instruções de pesquisa, entretanto buscando apenas os lançamentos com status baixados.

O Sistema retornará apenas lançamentos baixados. O usuário deve selecionar os lançamentos que deseja estonar a baixa e clicar no botão “Estorno” no ícone .

O Sistema apresentará a tela com as informações contábeis de estorno.

Após clicar em “Executar”, o processo de estorno de baixa será finalizado.

O Sistema retornará com a informação do estorno da baixa do lançamento realizado com sucesso.

# 2.13.4 Inclusão de Lançamentos de Serviço Extra Através da Sessão de Caixa

Ainda na sessão de caixa, é possível a inclusão de novos lançamentos financeiros de serviços extra que são vinculados ao contrato do aluno no Módulo Educacional do Sistema. Para realizar esta inclusão de um serviço extra no contrato do aluno, o usuário deve clicar no botão “Serviço Extra” no ícone.

Nesta etapa, o Sistema abre a tela para inclusão do serviço extra e usuário deve preencher:

* **Filial:** Informar a filial do lançamento;
* **Nível de Ensino:** Informar o nível de ensino do aluno que será inserido o serviço extra;
* **Período Letivo:** Informar o período letivo do aluno;
* **Aluno:** Informar o aluno para o qual será inserido o serviço extra;
* **Contrato:** Será apresentado neste campo o contrato educacional para o qual será inserido uma parcela de serviço extra;
* **Parcela:** Informar qual o número da parcela será inserido o serviço extra criado;
* **Cota:** Informar a cota da parcela;
* **Data de Emissão:** Será carregada com a data atual;
* **Data de Vencimento:** Informar a data de vencimento do lançamento de serviço extra que está sendo inserido;
* **Serviço:** Informar o serviço extra que será utilizado;
* **Valor: I**nformar o valor da parcela que está sendo inserido.

Após inserir as informações, o usuário deve clicar no botão “Adicionar” e em seguida no botão “Executar” para que seja inserida a parcela de serviço extra para o aluno.

# 2.13.5 Desativar e Fechar Sessão de Caixa

Para desativar e fechar uma sessão de caixa, o usuário deve utilizar os botões a seguir.

Clicando neste botão, a sessão de caixa aberta para o operador/usuário será desativada, fechando a tela. Entretanto não é feito o encerramento da sessão e o operador/usuário poderá abrir novamente essa mesma sessão.

Clicando neste botão, a sessão de caixa será encerrada e o operador/usuário não conseguirá mais abrir essa mesma sessão. Este processo é irreversível, não podendo abrir mais uma sessão encerrada.

No momento em que fechar a sessão de caixa, o Sistema exibirá a mensagem solicitando a confirmação do fechamento da sessão de caixa. Clicando no botão “Sim” a sessão será encerrada.

Exibindo a imagem a seguir.
