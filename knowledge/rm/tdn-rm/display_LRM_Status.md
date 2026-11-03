---
content_hash: ad995b1dafc25331697ed9af4205647539ed7b1930518292efa61f07527dfc30
fetched_at: '2026-06-29T00:09:24.468003+00:00'
page_id: '423937921'
product: rm
source: tdn-rm
title: Status
type: documentation
url: https://tdn.totvs.com/display/LRM/Status
version: 2
---

O cadastro de status permite informar ao sistema quais serão os status de Ordem de produção com os quais a empresa irá trabalhar.   
Através dos status serão estabelecidas as regras de alocação de capacidade produtiva, bem como as consultas de saldos existentes em estoque.   
O campo "Flag" determina os status que o fluxo da ordem de produção seguirá.   
Os seguintes status são gerados como padrão:

| Status | Descrição |
| --- | --- |
| 0 | Criada |
| 1 | Aguardando recursos |
| 2 | Pronta para iniciar |
| 3 | Parcialmente concluído |
| 4 | Interrompida |
| 5 | Concluída |
| 6 | Cancelada |

***Observação***: Só é possível realizar alteração no campo descrição, não é possível alterar os flags ou criar um novo.
