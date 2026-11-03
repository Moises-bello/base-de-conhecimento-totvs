---
content_hash: fa046d5ad159aaffcc38d00e9097e07d996a41628b7e2a3a0e6e6dd9773f5d7f
fetched_at: '2026-06-29T00:11:22.537296+00:00'
page_id: '705458608'
product: rm
source: tdn-rm
title: Alterações S-2399-S-1.1
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=705458608
version: 16
---

false

**A partir das Versões:**

* 12.1.34.232
* 12.1.2205.175
* 12.1.2209.117
* e Superiores.

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupo {quarentena} e  campo {dtFimQuar} foi excluído | Grupo {quarentena} e respectivo campo {dtFimQuar} | - |
| Grupo {remunAposTerm} incluído campo (indRemun) | - | Indicativo de situação de remuneração após o término. Valores válidos: 1 - Quarentena 2 - Término reconhecido judicialmente com data anterior a competências com remunerações já informadas no eSocial Validação: Informação obrigatória se dtDeslig >= [2023-01-16] |
| Grupo {remunAposTerm} incluído campo (dtFimRemun) | - | Preencher com a data final da quarentena a que está sujeito o trabalhador. No caso de término reconhecido judicialmente com data anterior a competências com remunerações já informadas no eSocial, informar o último dia trabalhado.  Validação: Deve ser uma data posterior a dtTerm |

 Foi criado no cadastro de rescisão o campo indicativo de situação de remuneração após o desligamento.

  XML:

No menu Parametrizador | eSocial | De/Para Desligamento Incluir o motivo 44
