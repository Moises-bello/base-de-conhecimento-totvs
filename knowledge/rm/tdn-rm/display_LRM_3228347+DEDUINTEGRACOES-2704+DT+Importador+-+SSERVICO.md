---
content_hash: 5a2df4e6a8ada147e2dd71a788b14fef4c95e6da6832f9cb1f88952a3711c5d7
fetched_at: '2026-06-29T00:09:02.857167+00:00'
page_id: '381027177'
product: rm
source: tdn-rm
title: 3228347 DEDUINTEGRACOES-2704 DT Importador - SSERVICO
type: documentation
url: https://tdn.totvs.com/display/LRM/3228347+DEDUINTEGRACOES-2704+DT+Importador+-+SSERVICO
version: 2
---

# IMPORTADOR - SSERVICO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Importador - SSERVICO* |
| **Situação/Requisito:** | Ao tentar importar um registro na tabela SSERVICO ocorria o seguinte erro: A coluna 'PGCARTAODEBITO' não permite DBNull.Value |
| **Solução/Implementação:** | Ajuste no importador para a inclusão dos campos APROVEITACONTACORRENTE, CONSIDERAPARCELAFIXA, DISPONIVELEXTENSAO, DESCONSIDERACREDITORETROATIVO,  PGCARTAODEBITO, PGCARTAOCREDITO, CONSIDERADESCANTECIPACAO na tabela SSERVICO, permitindo informar os valores obrigatórios para a tabela através do arquivo. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
