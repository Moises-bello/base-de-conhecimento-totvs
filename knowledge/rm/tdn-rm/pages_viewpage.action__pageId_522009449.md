---
content_hash: 5d6694d4ae7029022cd27b34df683fd39322394db1368f9d240462884e4ab68d
fetched_at: '2026-06-29T00:10:31.851682+00:00'
page_id: '522009449'
product: rm
source: tdn-rm
title: R-9000 Exclusão de Evento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=522009449
version: 5
---

O Evento R-9000 será incluído através do "**R-9000 Exclusão de Evento**" e durante a inclusão o mesmo já será integrado com o TSS. Diferentemente dos demais Eventos, o histórico deste será registrado no histórico do Evento pai vinculado.

Se o processo for executado com sucesso o "Evento Principal" terá o seu status alterado para "Pendente Exclusão" e o registro do R-9000 será incluído com status "Pendente".   
  
Em caso de erro será registrado um R-9000 "Inconsistente" e vai ser alterado no "Evento Principal". Em ambos os casos o histórico será gravado no "Evento Principal".

Sempre que o "Evento Principal" estiver com o Status "Pendente Exclusão" ou "Excluído" o mesmo irá apresentar um lookup para o Evento de Exclusão R-9000 no qual ele está associado.

O processo poderá ser executado em lote e através dos associados no Evento R-5011/R-9011 e R-9015 para vários Eventos Periódicos simultaneamente (detalhes na especificação do R-5011/R-9011 e R-9015).

**Regras**

* Cada "Evento Periódico" poderá ter somente um R-9000 associado e no caso de já existir um "Inconsistente" ou "Rejeitado" o mesmo será substituído.
* O R-9000 poderá ser gerado somente para Eventos com Status "Autorizado";
* O Evento R-9000 deve ser executado somente para os eventos do tipo: R-2010 ao R-2070, R-3010, R-4010, R-4020 e R-4080.
