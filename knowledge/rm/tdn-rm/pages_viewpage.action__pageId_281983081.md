---
content_hash: 30b902a0fef98b34195a94a8abf364900305e487fd2ec9304ce090f6b5ea4aa0
fetched_at: '2026-06-29T00:08:35.576537+00:00'
page_id: '281983081'
product: rm
source: tdn-rm
title: 938810 MSAU-9747 DT Geração Arquivo IPASGO Procedimentos Mesma Via
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=281983081
version: 108
---

# Geração arquivo IPASGO Procedimentos Mesma Via

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Faturamento IPASGO |
| **Situação:** | Ao realizar o faturamento para o convênio IPASGO de honorários com a mesma data, repetindo o mesmo procedimento, o sistema agrupava os procedimentos e lançava apenas um destes, o que ocasionava não conformidades ao enviar o arquivo para o convênio. |
| **Solução:** | Alterado o sistema para quando for gerado o arquivo de faturamento IPASGO o sistema não agrupar honorários lançados no mesmo dia, lançando duas linhas no arquivo com o mesmo procedimento. |

divs
