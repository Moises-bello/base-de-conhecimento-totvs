---
content_hash: c6f19b82d14060970e6151a1dd4cba2292a23ed076f7111e81c499a4d5de8022
fetched_at: '2026-06-29T00:12:15.414881+00:00'
page_id: '977859148'
product: rm
source: tdn-rm
title: FISCAL01-24809 - NFCom - Edição de movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=977859148
version: 1
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão de Estoque, Compras e Faturamento |
| Função: | Envio NFCom |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-24809 |

## **02. SITUAÇÃO/REQUISITO**

Realizar consistências ao Editar, Cancelar e Excluir movimentos que possuam NFCom associada.

## **03. SOLUÇÃO**

As consistências são realizadas quando o tipo de movimento estiver parametrizado em: Etapa 67 - Fiscal - Nota Fiscal Eletrônica (Fis - NF-e), campo NFcom = Integrado.

Só é permitido Editar, cancelar ou excluir movimentos cujo o status da NFCom seja diferente de: Pendente, Autorizado, Cancelamento Pendente e Cancelado.

Editar: Ao editar um movimento, o status da NFCom é alterado para Editado.

Cancelar: Ao cancelar um movimento, o status da NFCom é mantido.

Excluir: Ao excluir um movimento, a NFCom é excluida.
