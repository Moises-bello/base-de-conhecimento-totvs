---
content_hash: df55663c3f67e9f8864b4463105ffb0d4a6da0947f5df79c69bf8d3b30e51c4c
fetched_at: '2026-06-29T00:09:11.307204+00:00'
page_id: '403746457'
product: rm
source: tdn-rm
title: 2007742 FOPCALCULO01-3017 Função MH
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403746457
version: 1
---

# Função MH

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Função de Fórmula MH |
| **Situação/Requisito:** | Quando executa a Funcionário de Fórmula MH(18,'ANO','CODEVENTO') no mês de Janeiro está retornando o valor do ano anterior, não considerando o parâmetro desmarcado no sindicato 'Considera ano anterior para o cálculo de médias'. Como é em janeiro, deveria desconsidera o ano anterior, mesmo marcado o parâmetro e retornar somente o valor de janeiro ou zero, dependendo se o parâmetro 'Considera mês atual para média' está marcado ou não. |
| **Solução/Implementação:** | Ajuste na fórmula MH para considerar variável de ano anterior quando mês atual for janeiro |
| **Tickets relacionados:** | 2007742 |
