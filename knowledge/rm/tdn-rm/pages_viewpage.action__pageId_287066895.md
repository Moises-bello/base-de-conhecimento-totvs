---
content_hash: 25794da5f1c352eeccc906deb33e83ac5abcaf0683b3c9ab69efe6c271988d76
fetched_at: '2026-06-29T00:08:42.264935+00:00'
page_id: '287066895'
product: rm
source: tdn-rm
title: 1183538 MATESTCNTFTOF01-569 DT Erro modulo Integração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=287066895
version: 91
---

# IMPORTAR OBJETO DE MANUTENÇÃO VIA CONCEITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Manutenção. |
| **Função:** | Processar Novo Conceito. |
| **Situação/Requisito:** | Ao fazer a leitura do registro, quando não encontrado o registro pela PK o DataServer de Objeto de Manutenção cria uma nova linha com os valores defaults. Assim, na hora de salvar o DataSet com as linhas importadas do arquivo, o DataSet contem uma linha a mais, fazendo com que gere o erro de coluna não preenchida. |
| **Solução/Implementação:** | Ao fazer a leitura do registro, quando não for encontrado o registro pela primary key enviada, não será criado pelo DataServer do Objeto de Manutenção uma linha contendo os valores defaults. |
| **Conversores e Parâmetros:** | Desnecessário. |
| **Tickets relacionados:** | 1183538. |
| **Requisito:** | Objeto de Manutenção (MntObjOficinaAction).  Processar Novo Conceito - importação via DataServer (ConConceptProcessAction) |

divs
