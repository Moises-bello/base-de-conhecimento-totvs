---
content_hash: ee698f987f8c3ffee642922d25641fabe768b8669f321b6800a419098769322c
fetched_at: '2026-06-29T00:10:25.850512+00:00'
page_id: '506143967'
product: rm
source: tdn-rm
title: Fila de eventos do eSocial Complementar -
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=506143967
version: 9
---

false

**A partir das Versões:**

* 12.1.23.240
* 12.1.24.189
* 12.1.25.123

# Objetivo:

---

Apresentar a fila de eventos complementar.

---

1true1Execução do scriptExecução do script

Para a liberação da fila de eventos complementar será necessário atualizar sua base de dados através do aplicativo RM.Atualizador.exe.

2Fila de eventos complementarFila de eventos complementar

A Fila de Eventos do eSocial Complementar irá guardar as informações contidas na Fila de Eventos do eSocial após a sua transferência pelo processo Transferência manual da Fila de Eventos do eSocial ou pela Liberação de Competência.

Para visualizar as informações acesse eSocial | Fila de Eventos Complementar | Fila de Eventos Complementar

3Liberação de CompetênciaLiberação de Competência

Para realizar a Transferência da Fila de Eventos do eSocial para a Fila de Eventos do eSocial Complementar no processo de Liberação de Competência será necessário marcar o parâmetro "Transferir Fila de Eventos do eSocial para Fila de Eventos do eSocial Complementar".

**Atenção:**

* Sistema verifica a data do evento (DATAEVENTO) para realizar a transferência.
4Transferência Manual da Fila de Eventos do eSocialTransferência Manual da Fila de Eventos do eSocial

Rotina que realiza a transferência dos registros da Fila de Eventos do eSocial (PESOCIALEVENTOS) para a Fila de Eventos do eSocial Complementar (PESOCIALEVENTOSCOMPL) de acordo com parâmetro "Meses a manter na Fila de Eventos", localizado em Parametrizador > eSocial > Configurações Gerais 1/6, que estipula o prazo de permanência dos registros na tabela PESOCIALEVENTOS.

Acesse eSocial | Fila de Eventos Complementar | Transferência manual da Fila de Eventos do eSocial

Clique em Executar.

5Restauração da Fila de Eventos do eSocialRestauração da Fila de Eventos do eSocial

Este processo consiste em transferir a movimentação que está na Fila de Eventos do eSocial Complementar para a Fila de Eventos do eSocial, de modo que o usuário possa realizar retificações e/ou envios quando necessário.  
   
Acesse eSocial | Fila de Eventos Complementar | Restauração da Fila de Eventos do eSocial

Selecione o Mês/Ano da competência inicial e final e clique em Executar.

É possível selecionar somente um evento para a restauração, com essa opção ficam desabilitados os campos competência inicial e competência final.
