---
content_hash: 8c91dd72844654fd0a696b82eda9a30a73d499a74d59b78f08821c2f6594893e
fetched_at: '2026-06-29T00:11:17.419506+00:00'
page_id: '680236652'
product: rm
source: tdn-rm
title: TPI - Alteração de status | Pagamento expirado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680236652
version: 5
---

Em casos de existir transações com status expirado no TOTVS, e no painel da Shipay já consta como aprovado (o que indica que houve repasse do pagamento), é necessário realizar um procedimento via banco de dados para que o sistema identifique e altere status no sistema:

PROCEDIMENTO

Se o título tiver sido baixado manualmente é necessário cancelar a baixa.

Em seguida, no banco de dados, realize um update para alterar o status da transação que estava expirada para **solicitada**.

Neste momento, é realizada a validação no portal da Shipay e logo em seguida atualizará o status.

UPDATE FINTEGRACAOCARTAO SET IDSTATUS = 1 WHERE REQUESTID = 'COLOCAR O IDENTIFICADOR DE TRANSAÇÃO TPD AQUI'

Obs: O TPD é o ID de pagamento indicado na coluna "Identificador transação TPD" no sistema TOTVS.

Em seguida, rodar o ajuste de transação para verificar se o pagamento foi identificado na shipay e no Totvs passou para **concluído** e fez a baixa.
