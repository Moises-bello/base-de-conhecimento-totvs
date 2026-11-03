---
content_hash: 2f7f5a6bb7f1299bd6fe9cc34e896d9fe93a8c169b23daf6c2aa1676519f2050
fetched_at: '2026-06-29T00:10:19.633595+00:00'
page_id: '484681807'
product: rm
source: tdn-rm
title: DT Sincronismo Automático de Apontamento de Equipamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=484681807
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Construção e Projetos |
| Módulo: | Gestão de Obras e Projetos |
| Função: | Sincronismo de Apontamentos de Equipamento |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [TOPORCAPLAN001-6459](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-6459 "Monitor de Obras - Sincronismo automático de Equipamento") |

## **02. SITUAÇÃO/REQUISITO**

Necessidade de sincronizar o apontamento inicial de Equipamento, isto é, o apontamento com apenas a informação da hora inicial, sem a a hora final .

## **03. SOLUÇÃO**

Para que o Monitor de Obras possa informar em tempo real a situação de cada equipamento dentro do projeto, é necessário que a entrada do apontamento de equipamento possa ser sincronizado sem depender do fechamento do apontamento, isto é, sem ter que encerrar o mesmo. Após salvar a entrada do apontamento, basta realizar o sincronismo de informações,  que será enviado ao TOTVS Obras e Projetos o registro do apontamento do equipamento somente com a hora inicial do apontamento.

No TOP existe o status "Em Andamento" para os apontamentos que estão pendentes de fechamento, onde para esses apontamento não são permitidas alterações nos mesmos.

## **04. DEMAIS INFORMAÇÕES**

## **05. ASSUNTOS RELACIONADOS**
