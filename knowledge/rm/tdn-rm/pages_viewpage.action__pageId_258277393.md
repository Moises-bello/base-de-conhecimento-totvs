---
content_hash: bbb807983a86a61816d09f74f4f97263e7493078c7d071f13d776d023e2fd8ff
fetched_at: '2026-06-29T00:08:17.716987+00:00'
page_id: '258277393'
product: rm
source: tdn-rm
title: EF_Portal x Nova Plataforma de Boletos de Pagamento-Cobrança Registrada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=258277393
version: 18
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Incorporação |
| **Versões:** | a definir |
| **Ocorrência:** | Nova Plataforma de Boletos de Pagamento-Cobrança Registrada |
| **Ambiente:** | RM |

# Objetivo

Atender a Nova Plataforma de Boletos de Pagamento-Cobrança Registrada estabelecida pela FEBRABAN, onde as cobrança bancária somente serão feitas por meio de cobrança registrada.

# Regra de Negócio

## Portal Atual

O Portal TOTVS Incorporação disponibiliza as incorporadoras os seguintes recursos:

* **2º via de Boleto**  
  Apresenta todas as parcelas vencidas e em aberto até a data do atual.  
  Permite selecionar uma parcela por vez e gerar a 2º via do Boleto via impressão de relatório do RM Reports
* **Antecipação de Pagamento**  
  Apresenta todas as parcelas em aberto, trazendo o valor para a Data Base informada.  
  Antes de apresentar as parcelas em aberto o usuário deverá escolher o Contrato e o Tipo de parcela;  
  O sistema apresenta por default como data base a data atual, mas o usuário poderá alterar para data futura desde que o sistema tenha índice de reajuste cadastrado para a data informada. Ao alterar a data base o portal atualiza as parcelas recalculando o valor dos componentes de correção como Correção Monetária e Juros Contratual, além dos valores financeiros de mora como multa, juros ou desconto.  
  É possível imprimir um boleto (relatório do RM Report) para cobrança não registrada, e esta forma não será mais possível a partir de janeiro de 2017.  
  O convênio da cobrança será definido no TIN via cadastro de Dados Bancários.

## Portal Proposto

### Unificação de Recursos

Afim de simplificar o processo de geração de boleto para o usuário cliente do portal, os dois menus deve ser unificados em um único menu = "Boletos", neste menu serão apresentadas as seguintes informações:

**Cabeçalho**

* Dados do cliente logado:Nome, Endereço, Telefones

* "Data Base" para calculo de atualização (reajuste e cobranças financeiras como Desconto, Juros e Multa
* Informações complementares já existentes hoje .....

**Lista de contratos**

* Apresentar todos os contratos do cliente logado em forma de "arvore" (treeview)
* Apresentar os seguintes dados:
  + nº da Subunidade;
  + Unidade;
  + Empreendimento;
  + Nº do Contrato;
  + Cod. Contrato;
  + Valor Total Financiado de todos os contratos apresentados \*;
  + Valor Total Pago de todos os contratos apresentados \*;
  + Saldo Devedor do Contrato de todos os contratos apresentados \*;
* Não filtrar Coligada;
* Exibir apenas vendas efetivadas, com contrato gerado e efetivado, com lançamentos financeiros gerados e desbloqueados  
  \**quem ainda tem saldo em aberto*

**Lançamentos Financeiros**

* Apresentar todos os lançamentos financeiros em aberto;  
  Campos:
  + Data de Vencimento
  + Nome do Comprador
  + Descrição do TIpo de Componente
  + nº da Parcela (1 /X
  + VR Parcela
  + VR Juros
  + VR Multa
  + VR Desconto
  + VR Atual (liquido)
* Permitir selecionar mais de um lançamento financeiro, mesmo que de vendas diferentes;

**Rodapé**

* Apresentar o somatório de todos os valores apresentados na lista;
* Apresentar quantidade de parcelas selecionadas;
* Apresentar total liquido das parcelas selecionadas;

Funções que devem estar disponível para o usuário:

* Reimprimir Boleto: apenas reimprime um boleto já existente usando o relatório padrão configurado no convenio financeiro.
* Gerar Boleto: gera um novo boleto do tipo "Registro On Line", ou seja, que terá comunicação com o banco via web para que o banco faça o registro on line.

### Parâmetros

Financeiros

Devem ser criados no Financeiro os seguintes parâmetros:

* **Relatório de Impressão**: Hoje temos 2 relatórios para impressão de boleto (2º via e Antecipação), mudar a parametrização para buscar um único relatório com informações do financeiro / boleto (contexto financeiro)  
  (Financeiro deve fornecer esta informação).
* **Convênio padrão para Registro On line**: A geração de um novo boleto com registro on line terá um convênio bancário padrão que deverá ser estabelecido nos parâmetros financeiros.  
  O usuário só poderá escolher entre convênios que tenham a opção de Registro on line marcado.  
  Não permitir desmarcar a configuração de registro on line do convenio que esteja sendo utilizado na parametrização;

  Não permitir desativas o convenio ou a conta financeira configurada no registro on line do convenio que esteja sendo utilizado na parametrização;  
  O cadastro existente hoje de Dados Bancários no TIN deverá ser descontinuado.

TIN

Devem ser criados no TIN os seguintes parâmetros:

* *****Permite gerar novo boleto para parcelas*****vencidas****: nem todas as empresas permitem que sejam gerados novos títulos para parcelas já vencidas sendo necessário a parametrização para que cada cliente estabeleça seus próprios critérios.
* ***Permite Antecipação de Pagamento no Portal TIN:*** Criar parâmetro no TIN, onde a incorporadora indica se o portal TIN deve ou não disponibilizar parcelas financeiras com vencimento futuro para antecipação do pagamento.   
  Para o correto funcionamento do recurso de Antecipação de Pagamento, o recurso de reajuste on line do financeiro deve estar ativado, caso contrário não haverá atualização dos valores contratuais  (Juros e CM)  de cada parcela.  
  *Considerar cliente que já usa o portal atualmente com este recurso.*
* Novos Boletos: poderão ser gerados via registro on line ou pelo relatório de boleto não registrado mantendo provisoriamente a função existente anteriormente.

## Tratamentos

2º Via (reimpressão de Boleto)

* O usuário deve selecionar as parcelas com vencimento menor ou igual a data atual para gerar a 2º via.
* Caso o usuário selecione parcelas com vencimento futuro o portal TIN deve informar ao usuário que não é possível gerar 2º via de parcelas futuras.
* A 2º via será gerada via Serviço Financeiro, utilizando relatório padrão parametrizado nos parâmetros Financeiros.  
  *Atendendo aos casos onde o usuário que perdeu seu boleto o imprima novamente, mas neste caso não re-gera um novo boleto com valor atualizado de juros e multa em caso de atraso.*
* Permite gerar o mesmo boleto com valor de Juros de mora e multa financeiras atualizados para o novo vencimento? (esta opção já existe hoje)?

Gerar novo Boleto

* Caso os parâmetros "***Permite Antecipação de Pagamento ..." e "***Permite gerar novo boleto para parcelas*****vencidas"*****não estiverem marcados a Opção de Gerar novo Boleto não deve ser disponibilizada e o  usuário poderá apenas re-imprimir os boletos.
* O usuário deve selecionar as parcelas  desejadas onde o sistema pode apresentar todas as parcelas em aberto do plano, conforme parâmetro "***Permite Antecipação de Pagamento no Portal TIN",*** ou apenas as parcelas em aberto até a data atual do sistema.
* Se marcar um dos dois parâmetros acima citados poderá informar se irá gerar novos boletos registrados (registro on line ) ou não registrados, ou seja, gera apenas um relatório sem a inclusão de novo boleto na base de dados.
* Caso o usuário selecione parcelas vencidas o sistema poderá gerar um novo boleto com todos os valores atualizados  (CM + juros do Contrato + Multa+ Juros de Mora) desde que o parâmetro "***Permite gerar novo boleto para parcelas*** **vencidas"** esteja marcado. O usuário deve ser informado de que não é possível gerar um novo boleto e que deve contatar a Incorporadora.
* Para novos boletos registrados de mesmo contrato, cliente e vencimento o sistema fará o agrupamento em um único boleto;
* O(s) novo(s) boleto(s) registrado (s) será (ão) gerado (s) via Serviço Financeiro e conforme convênio padrão parametrizado no financeiro. Conforme o banco associado ao convenio o sistema poderá apresentar o boleto já gerado e pronto para a impressão ou abrir a tela do banco de geração do boleto, pois isso dependerá dos recursos de integração disponibilizados por cada banco.

## Data Base

O campo de data base permite que as parcelas apresentadas na tela tenham a atualização de correção monetária, juros de contrato e encargos moratórios (juros e Multa) bem como descontos financeiros, desde que o parâmetro financeiro para reajuste on line esteja marcado.

O portal sempre traz a data base default o dia em que o usuário está acessando o sistema.

Se o usuário informar uma data base futura onde não haja índice para atualização (correção monetária) o sistema não fará o reajuste e voltará a data base para a data de hoje.

O contrato que não tiver suas parcelas reajustadas por algum motivo terá uma marcação para fácil identificação.

 Antes de iniciar o desenvolvimento a nova tela de lançamentos do portal deve ser prototipada e apresentada ao cliente IDIBRA , GDP e Evangelizador de C&P para ser aprovada.
