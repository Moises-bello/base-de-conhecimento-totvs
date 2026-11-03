---
content_hash: b5772bd68b4dc0095c3c3a4f7a2a24afbfe51dfe65aba62dcef38e149f7c79e5
fetched_at: '2026-06-29T00:09:41.833743+00:00'
page_id: '431678407'
product: rm
source: tdn-rm
title: Abertura Período
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=431678407
version: 12
---

Na abertura de um período, o sistema irá alterar o seu status para encerrado e atualizar o seu saldo credor/Devedor.  
Para manter a integridade de saldo dos períodos, sabendo que este é atualizado no momento do seu encerramento, o sistema irá fazer algumas consistências antes de Encerrar um período:

* Na utilização do campo Usa Lotes no módulo: Opções | Parâmetros | Gerais/Tabelas | Escrituração - o sistema somente permitirá o encerramento de um período, se os todos os lotes referenciados a este estiverem com Status de Liberado.
* O sistema somente permitirá o encerramento de um período, se os todos os períodos anteriores estiverem com Status de Encerrado, **com exceção dos períodos do tributo INSS**.
* O sistema somente permitirá a reabertura de um período se todos os períodos posteriores estiverem em aberto, **com exceção dos períodos do tributo INSS**.
* Não será possível alterar o Status do Período na tela de cadastrado, o status será alterado somente quando abrir ou encerrar um Período através dos processos.
* Ao encerrar o período de IRRF da Filial Matriz, todos os períodos deste tributo das outras filiais, com as mesmas datas inicial e final, serão também encerrados. Isto se o parâmetro "Filial" não estiver marcado através do menu Opções | Parâmetros | Gerais/ Tabelas / Apuração de Tributos - IRRF - Guias de Recolhimento 4/4 - Regras de geração DARF.

O processo não permitirá reabrir o período para os tributos abaixo quando são utilizados pela rotina federal REINF:

FUNRURAL: Se existir evento R-2050 filho do R-5011 encerrado, com status diferente de excluído.

Contribuição Previdenciária - CPRB: Se existir evento R-2060 filho do R-5011 encerrado, com status diferente de excluído.

***Observação*:**O campo Fim Período somente poderá ser alterado se não existirem lançamentos em datas posteriores a "nova data", ou a data final do Lote (caso utilize lote no sistema) associado ao período for menor ou igual a nova data.  
Para os tributos que são apurados através de eventos tributários ( PIS, COFINS, CSSL, IRPJ, OUTROS E RET) no encerramento é necessário verificar a existência de Vigência Eventos Tributários para a correta apuração.
