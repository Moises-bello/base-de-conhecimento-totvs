---
content_hash: f7dd1274458b91a3f15a63b734681adf531952ae56359e8e28100493e91b8174
fetched_at: '2026-06-29T00:10:31.007008+00:00'
page_id: '520659261'
product: rm
source: tdn-rm
title: Contrato de Locação - Gestão - Parcelas do Contrato de Locação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520659261
version: 2
---

Este anexo possibilita a visualização das parcelas envolvidas em um Contrato de Locação. Um parcela pode possuir N lançamentos distribuídos para Locador e Locatário.  
   
 **Comportamento do sistema em relação ao repasse Condicional**

O repasse irá criar um ou vários lançamentos, que serão vinculados da mesma forma que o lançamento a pagar gerado atualmente, utilizando-se a tabela existente XALGEVENTOFINANCEIRODISTRIBUIC; Esta tabela terá o novo campo TIPO, que será preenchido com as seguintes opções:

* Gerador: Refere-se à distribuição de parcela a receber que é geradora de um repasse;
* Condicional: Refere-se à distribuição gerada por um repasse financeiro e é ligada à uma distribuição geradora;
* Individual: Refere-se à distribuição de lançamentos isolados, que não são e nem geram repasse condicional.

Para identificar distribuições de repasse condicional, será feito o relacionamento da tabela XALGEVENTOFINANCEIRODISTRIBUIC com a tabela XALGEVENTOFINANCEIRODISTRIBUICREPASSE, fazendo a ligação da distribuição do gerador com a distribuição do repasse.

A exclusão dos lançamentos e distribuição dos eventos (mesmo na regeração dos lançamentos financeiros, onde primeiro é feita a exclusão), deverá validar se os lançamentos a pagar foram criados pelo repasse e, caso positivo, deverá ser excluído o repasse, que automaticamente cancela o lançamento e posteriormente, o lançamento cancelado deverá ser excluído.

Todo o tratamento realizado atualmente para eventos agregados continua válido e deve continuar seguindo a regra atual, onde um evento agregado é associado ao lançamento como um valor de integração e se tal lançamento for excluído (seja de repasse ou não), o evento agregado deverá voltar a situação e ficar disponível para ser considerado e cobrado / descontado em lançamentos gerados posteriormente.

O rateio por centro de custo deverá seguir as regras atuais e seu comportamento deverá ser mantido.

O repasse será utilizado também em eventos avulsos, considerando a definição já feita no contrato de administração (conforme parametrizado no campo "Modelo de repasse do contrato").

Será considerado o rateio do lançamento a receber, onde o repasse condicional será criado para cada lançamento gerado, podendo gerar vários lançamentos pequenos, conforme parametrização (Caso o evento seja parametrizado para cobrar de dois locatários, serão gerados dois lançamentos a receber e cada um irá gerar um repasse e cada repasse pode gerar N lançamentos a pagar, conforme definição de locadores e beneficiários).
