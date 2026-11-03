---
content_hash: eaeb5d1cff73b2ea64c550986dd78d92e1b6739cd00665b14bc7fc70f289dda6
fetched_at: '2026-06-29T00:11:22.523104+00:00'
page_id: '705447633'
product: rm
source: tdn-rm
title: Alterações S-2299-S-1.1
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=705447633
version: 20
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
| Grupo {remunAposDeslig} incluído campo (indRemun) | - | Indicativo de situação de remuneração após o desligamento. Valores válidos: 1 - Quarentena 2 - Desligamento reconhecido judicialmente com data anterior a competências com remunerações já informadas no eSocial 3 - Aposentadoria de servidor com data anterior a competências com remunerações já informadas no eSocial Validação: Informação obrigatória se dtDeslig >= [2023-01-16] |
| Grupo {remunAposDeslig} incluído campo (dtFimRemun) | - | Preencher com a data final da quarentena a que está sujeito o trabalhador. No caso de desligamento reconhecido judicialmente ou de concessão de aposentadoria de servidor com data anterior a competências com remunerações já informadas no eSocial, informar o último dia trabalhado.  Validação: Deve ser uma data posterior a dtDeslig |

Foi criado no cadastro de rescisão o campo indicativo de situação de remuneração após o desligamento, que ao ser preenchido a informação sairá na tag <indRemun> conforme exemplo abaixo:

  XML

No menu Parametrizador | eSocial | De/Para Desligamento foi incluído o motivo 44 (Agrupamento contratual)
