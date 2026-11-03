---
content_hash: 3486ff5657ae3a2fbbfbcba4396b6a30db5a32da3e2f5dda0eb17c273478a09e
fetched_at: '2026-06-29T00:10:13.178216+00:00'
page_id: '454843964'
product: rm
source: tdn-rm
title: Desfazer Reajuste de Preços (Contratos)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454843964
version: 3
---

Após realizar o reajuste é possível desfazer e retornar os itens de contrato a um estado anterior.

O processo Desfazer Reajuste de Preços será realizado através de processo em Manutenção de contrato | Processos → Desfazer Reajuste de Preços.

O processo deve receber como parâmetros a Moeda Índice (mesma informada na aba Informações adicionais | Reajuste), e a data do último reajuste realizado.

A data de reajuste deve ser a ultima data de reajuste realizado. Caso tenha sido realizado vários reajustes para o mesmo item, estes deverão ser desfeitos um a um na ordem inversa do reajuste.

Caso alguma parcela já tenha sido faturada após o reajuste, o processo não irá desfazer o reajuste da parcela faturada.

Ao término do processo o contrato vai ser afetado da seguinte forma:

* Histórico do reajuste será excluído.
* Data de último reajuste no item do contrato vai ser atualizada para data do último reajuste anterior ao desfeito ou a data vai ser elimina se não houver reajuste anterior.

**Permissões**:

O processo de "**Desfazer Reajuste de Preços**", conta com recurso de segurança e seu acesso precisa ser liberado através de permissão no perfil associado ao usuário.
