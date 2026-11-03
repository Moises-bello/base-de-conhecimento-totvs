---
content_hash: 63fb8747bee8aac5c58de5457c6107c1cdeac7e66987089c77b2fcb64ffc2217
fetched_at: '2026-06-29T00:08:31.739861+00:00'
page_id: '273307952'
product: rm
source: tdn-rm
title: CONTROLADORIA01-77 DT Não calcular/atualizar a capa de lote automaticamente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273307952
version: 111
---

# Não calcular/atualizar a capa de lote automaticamente ao abrir a visão de lotes

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Não calcular/atualizar a capa de lote automaticamente ao abrir a visão de lotes |
| **Situação/Requisito:** | Alteração do ID do parâmetro de tela 179 para 181 na classe CPARAM pois foi criado um ID com código 179 para parâmetro interno que é verificado no conversor e isso pode com o tempo vir a causar inconsistência no sistema. |
| **Solução/Implementação:** | Ajuste da tabela CPARAM substituindo o ID = 179 que foi utilizado para parâmetro de tela para o código 181 e criação de script para selecionar os valores do parâmetro 179 para serem atribuídos para o 181 por coligada exceto para coligada 0 zero. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados**: | N/A |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
