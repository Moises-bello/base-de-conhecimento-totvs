---
content_hash: ff29fba5027b2fa57601a73177f54f098b69ca8b7f0f66f18c0e4d6e11b71177
fetched_at: '2026-06-29T00:08:42.299697+00:00'
page_id: '287068585'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-38 DT Regeração de lançamentos financeiros com boletos emitidos
  ou registrados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=287068585
version: 118
---

# Regeração de Lançamentos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geraração de Lançamento* | *Geraração de Lançamento* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Bolsa Retroativa* | *Bolsa Retroativa* | |  |  | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** |  |
| **Ponto de Entrada:** |  |
| **Tickets relacionados** |  |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** |  |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** |  |
| **Tabelas Utilizadas:** |  |
| **Sistema(s) Operacional(is):** |  |

## Descrição

Em função da evolução da nova plataforma de cobrança implementada pela FEBRABAN que por motivos de segurança prevê que os boletos sejam todos registrados, foram realizadas evoluções nos procedimentos de regeração de lançamentos financeiros realizada diretamente no TOTVS Educacional para lançamentos que tenham boletos com status igual a “Remetido” ou “Registrado”.

**Evolução:**

Com objetivo de dar mais agilidade no processo de regeração do lançamento financeiro foram realizadas algumas evoluções:

* **Cancelamento automático da remessa**

Foi disponibilizado no menu ***Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin - Geral 1/4***o parâmetro "***Cancelar Remessa automaticamente ao regerar o lançamento financeiro quando o boleto estiver com status Remetido ou Registrado***".

Com este parâmetro marcado ao regerar um lançamento pelo TOTVS Educacional em que o status do boleto seja igual a “Remetido” ou “Registrado” o sistema automaticamente executará o cancelamento desta remessa, modificando o status do boleto para *‘Pendente Remessa’* e prosseguirá com a regeração do lançamento.

Quando este cenário ocorrer, o processo que realizou a alteração do lançamento finalizará com o status de atenção (warning) e será apresentado no LOG os boletos que tiveram a remessa cancelada.

Com isso simplificamos os procedimentos de regeração de lançamentos com boleto já remetidos ou registrados nos bancos.

* **Inclusão de novo boleto na regeração de lançamento**

Alguns bancos não aceitam remessa para *alteração* de valores do boleto. Neste caso, quando houver alterações de valores em lançamento cujo boleto já tenha sido remetido ou registrado no banco, uma remessa de *cancelamento de boleto* deve ser enviada ao banco, cancelando o envio do boleto anterior. Posteriormente deve ser enviada uma nova remessa ao banco incluindo o novo boleto que teve seus valores alterados.

Para atender o cenário acima o TOTVS Gestão Financeira realizou uma evolução no cadastro de convênio disponibilizando a opção ***‘Cancelar boletos pendentes de remessa ao alterar valores dos lançamentos’***, possibilitando assim a execução automática do cancelamento do boleto que teve sua remessa cancelada e imediata inclusão de um novo boleto, de status ‘Não Remetido’, com os valores atualizados.

O TOTVS Educacional foi evoluído e através de parametrização específica, é possível que na regeração de lançamentos, havendo mudança de valores em boletos que possuem status igual a “Remetido” ou “Registrado”, o sistema cancele automaticamente a remessa destes boletos modificando os seus status para *‘Pendente Remessa’*. Aliado a esta nova opção criada no cadastro de convênio, o boleto original que teve seu status alterado para ‘Pendente Remessa’ será então *cancelado* automaticamente e imediatamente após será *incluído* um novo boleto contemplando as alterações.

Ressaltamos que o novo boleto será incluído com o status igual à ‘Não Remetido’, sendo necessário posteriormente que seja feito o seu envio ao banco.

  

* **Processo de Inclusão/Exclusão de Bolsa Retroativa**  

  Ao realizar a inclusão ou exclusão de uma bolsa retroativa o sistema altera o lançamento financeiro no qual a bolsa está sendo incluída ou excluída, e para os casos em que o status do boleto deste lançamento seja igual a “Remetido” ou “Registrado”, serão aplicadas as mesmas regras da regeração de lançamento descritas nos tópicos acima.

  Ao término do processo o sistema apresentará no LOG informações com os lançamentos/boletos que tiveram a sua remessa cancelada automaticamente.

## Importante

Relembrando: para que seja incluído um novo boleto na regeração de lançamento:

* O boleto original deve estar com status igual a "Remetido" ou "Registrado";
* Deve haver alterações que impactam em valores;
* O parâmetro "***Cancelar Remessa automaticamente ao regerar o lançamento financeiro quando o boleto estiver com status Remetido ou Registrado***" deve estar marcado;
* O convênio deve estar com a opção ***‘Cancelar boletos pendentes de remessa ao alterar valores dos lançamentos’*** marcada;
* O procedimento de inclusão de um novo boleto ocorrerá somente na regeração de lançamentos financeiros executadas diretamente no TOTVS Educacional;

  

| Atenção  **É importante ressaltar que nos casos em que o TOTVS Educacional efetuar o cancelamento automático da remessa dos boletos já registrados ou remetidos ao banco, o cliente deverá, através do TOTVS Gestão Financeira, enviar para o banco a remessa de cancelamento dos boletos afetados.**  **Este controle poderá ser realizado através do TOTVS Gestão Financeira filtrando os boletos com status igual "Pendente Remessa".**  **Destacamos ainda que se ocorrer pelo TOTVS Educacional o cancelamento automático da remessa de boleto, serão apresentados no LOG os boletos que tiveram sua remessa cancelada e o processo finalizará com o status de atenção (Warning).**    **Contate o Help Desk em caso de dúvidas** |
| --- |

## Visão Geral

## Vídeo

**Parte 1**

**Parte 2**

divs
