---
content_hash: b568cdd3f537fced11e6061a8b5900bf89fea180b8763aa7f794ec86517ce39e
fetched_at: '2026-06-29T00:05:54.113201+00:00'
page_id: '1074619661'
product: rm
source: tdn-rm
title: Atualização Movimento Dados NFS-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1074619661
version: 12
---

## **Conteúdo**

Conteúdo

## **01. Dados NFS-e**

Quando utilizado movimento do tipo: 2.2.xx, ao realizar o processo de Consulta da NFS-e Autorizada ou ao editar o registro de NFS-e e alterar o status para "Autorizado", o movimento será atualizado.

Menu integrações | Dados da NFS-e, será preenchida com os seguintes valores:

Número da NFS-e: Numero da NFS-e retornado pela prefeitura no XML de autorização.

Data Emissão da NFS-e: Tag: DataEmissao do grupo: InfNfse, retornado pela prefeitura no XML de autorização, caso não retorne a tag/grupo usa data de emissão do movimento.

Data Competência da NFS-e: Tag: Competência do grupo: InfNfse, retornado pela prefeitura no XML de autorização, caso não retorne a tag/grupo usa data de emissão do movimento.

## **02. Atualização Alíquota**

Quando se tratar de prefeitura que utiliza o layout Nacional, a aliquota do ISS é atualizada com a aliquota aplicada pela prefeitura para o serviço:

Regras:

* Com Base de Calculo maior que zero.
* Alíquota igual a zero.

**IMPORTANTE**: Caso possua mais de um ISS, a regra será aplicada ao primeiro registro da lista.

## **03. Histórico NFS-e**

Incluído um registro no Histórico da NFS-e, informando os que os campos foram atualizados, apresentando os respectivos valores.
