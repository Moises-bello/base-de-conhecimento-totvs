---
content_hash: ce5815a4845b52e7c60e46cf9e4679ba0466f8737ea43a55f876c3d3184a630a
fetched_at: '2026-06-29T00:08:59.634581+00:00'
page_id: '364908560'
product: rm
source: tdn-rm
title: S-3000 – Exclusão de Eventos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364908560
version: 4
---

* Utilizado para tornar sem efeito um evento enviado indevidamente, o qual deve estar incluído entre as faixas S-1200 a S-2400, com exceção dos eventos S-1299 – Fechamento dos Eventos Periódicos e S-1298 – Reabertura dos Eventos Periódicos.
* O Prazo de envio: sempre que necessária a exclusão de algum evento enviado indevidamente. Pré-requisitos: envio anterior do evento a ser excluído.

Procedimentos para geração do eventos:

1ºPasso:  Acesse Totvs Folha de Pagamento | eSocial | Eventos periódicos.

Sistema apresentará os eventos periódicos já gerados no sistema conforme período selecionado.

Para gerar o gatilho de exclusão basta selecionar o evento desejado e clicar em excluir

Sistema apresentará uma mensagem de confirmação. Após clicar em sim será gerado um gatilho de Exclusão S-3000 referente a esse evento.

Para ter acesso ao gatilho Acesse Totvs Folha de Pagamento | eSocial | Fila de eventos.

Sistema gerou o gatilho do evento S-3000, para o indicador do evento S-1200 excluido.

Veja mapeamento dos campos informados:
