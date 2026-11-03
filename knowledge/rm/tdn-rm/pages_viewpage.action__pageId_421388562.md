---
content_hash: 2145d060c32fdad886e1a338dbf64b694d79a196e777b5ca11f12b0833c7ba8a
fetched_at: '2026-06-29T00:09:17.021562+00:00'
page_id: '421388562'
product: rm
source: tdn-rm
title: Módulo de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388562
version: 16
---

Descontinuação do Módulo de Caixa 1.0

A partir da release 12.1.2510, o **Módulo de Caixa 1.0** será **descontinuado** e não estará mais acessível no TOTVS Gestão Financeira.

A solução oficial e mantida pela TOTVS para os recebimentos presenciais será exclusivamente o **Módulo de Caixa 2.0**, já disponível e que oferece mais recursos, melhor performance e maior aderência às melhores práticas.

Recomendamos que as empresas realizem a migração para o **Módulo de Caixa 2.0** o quanto antes, garantindo continuidade operacional, suporte técnico e acesso às inovações da solução.

Para mais informações sobre a nova funcionalidade, consulte a [documentação nesse link](https://tdn.totvs.com/pages/viewpage.action?pageId=744486517).

O objetivo do Módulo de Caixa é, por meio de uma interface simples e objetiva, facilitar os recebimentos e pagamentos pela Tesouraria, face às suas atribuições.  
   
Através da Interface do Caixa o usuário operador da Sessão poderá registrar Recebimentos e/ou Pagamentos, baixando e incluindo Lançamentos Financeiros, Extrato de Caixa Manual entre outros. Será possível pela busca da sessão de caixa procurar lançamentos pela referência do lançamento, referência do boleto (apenas status em aberto) e pelo tipo de documento.  
   
O saldo inicial da sessão de caixa será passível de alteração mediante marcação o parâmetro Informar Saldo Inicial nas opções do cadastro de perfil.  
   
O sistema permite que seja atribuído a cada operador um nível de acesso aos recursos através das definições do perfil.  
Você poderá criar um perfil para Supervisor, aquele que irá gerenciar as Sessões e um perfil para Operador, com acesso limitado.  
   
Para configurar o perfil acesse: Serviços Globais | Segurança | Perfis - Usuários.

Operador Supervisor

É necessário cadastrar um perfil que tenha acesso aos principais menus do Módulo de Caixa, cadastrar o usuário definindo que o mesmo será supervisor, indicar a coligada e associá-lo ao perfil criado.

Operador de Caixa

Será necessário cadastrar um perfil para o Operador, permitindo ou restringindo acesso aos principais menus do Caixa, cadastrar o usuário e associá-lo ao perfil criado.

**Parâmetros**

Acessar o menu:  Ambiente | Parâmetros | Gestão Financeira | Contas a Receber | Caixa | Módulo de Caixa.

**Autenticação do caixa**

Autenticação Mecânica

Ao marcar esta opção será usada a autenticação mecânica no caixa, na abertura no encerramento, na baixa e estorno de lançamentos.

Permite não imprimir autenticação

Ao marcar esta opção a impressão da autenticação mecânica não será solicitada. - Permite reimprimir autenticação Ao marcar esta opção será possível reimprimir a autenticação mecânica no caixa.

Obrigatória a impressão de abertura do caixa

Ao marcar esta opção a autenticação na abertura da sessão de caixa será obrigatória, não será possível fazer nenhuma movimentação na sessão sem que a mesma seja executada.

Saída de impressão

É necessário selecionar a porta de saída de impressão da autenticação mecânica no caixa.

**Configuração Layout**

Selecione as funções que serão impressas na autenticação de abertura, baixa e estorno.

**Número Autenticações**

Será preciso selecionar onde será impresso a autenticação do caixa, se em documento ou em Bobina.

**Relatórios do Caixa**

Balanço de Sessão de Caixa

Será preciso definir qual relatório será emitido no encerramento da sessão de caixa.

Usa Recibo

Marcar está opção se for necessária a impressão de recibo para Baixa, Estorno e Extrato.

**Recebimentos de Cheques Pré-datados via sessão de caixa**

Como a data dos cheques "pré-datados" não são previsíveis na situação real do seu recebimento, podendo ser qualquer data acordada entre o cliente e fornecedor, o campo "Data de Vencimento" é preenchido automaticamente ao selecionar a flag de "Pré-Datado" para auxiliar no processo.

Desta forma, a inclusão de cheque Pré-datado segue as seguintes regras quando selecionado mais de um Lançamento financeiro:

* Utilizando a opção de "Um cheque para cada lançamento", será utilizada a data de cada lançamento correspondente ao cheque selecionado;
* Utilizando a opção de "Um cheque para todos os lançamentos", sempre será utilizada a menor data de vencimento dentre os lançamentos;
* Utilizando a opção de "Um cheque para cada Cliente/Fornecedor", sempre será utilizada a menor data de vencimento dentre os lançamentos daquele Cliente/Fornecedor.

Obs: O parâmetro de cheque "*Cheque Pré-Datado*" em 02.02 Contas a Receber | Cheque , influência diretamente no processo definindo a data Default de vencimento do cheque.

Veja Também

 Informações Complementares

* [Recebimento com SiTef pela Sessão de Caixa](https://tdn.totvs.com/display/LRM/TEF)
