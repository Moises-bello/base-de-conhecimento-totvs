---
content_hash: f0babc62350551360b62e3e1264f285dffd084ff32b39e1418f93335c19793cc
fetched_at: '2026-06-29T00:06:03.961068+00:00'
page_id: '200903336'
product: rm
source: tdn-rm
title: TSXFG8_DT_Script_Adapter_Integracao_Protheus
type: documentation
url: https://tdn.totvs.com/display/LRM/TSXFG8_DT_Script_Adapter_Integracao_Protheus
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Conector* |
| **Módulo:** | *Integração* |
| **Função:** | *Integração com Protheus - Mensageria* |
| **Situação/Requisito:** | O Scripts C# (adapter) de FinancingTrading estava utilizando a classe CultureInfo da Framework .NET sem utilizar o seu namespace completo. |
| **Solução/Implementação:** | Incluído um "Using System.Globalization;" no script para que não ocorra erro no Build do Script. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | N/A |
| **Versões/Release:** | *11.83.55* |
