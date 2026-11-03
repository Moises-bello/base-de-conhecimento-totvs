---
content_hash: db91c0e5e1486cc697a18d32e52dc92479eb1b176106b562330939e078630767
fetched_at: '2026-06-29T00:08:28.800701+00:00'
page_id: '271853167'
product: rm
source: tdn-rm
title: 511213 MEDU-2683 DT Boletos Processo Seletivo FBOLETO tabela principal
type: documentation
url: https://tdn.totvs.com/display/LRM/511213+MEDU-2683+DT+Boletos+Processo+Seletivo+FBOLETO+tabela+principal
version: 109
---

# BOLETOS DO PROCESSO SELETIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Boletos do processo seletivo* |
| **Situação/Requisito:** | *Foi identificado que com a utilização de boletos registrados, os relatórios de boleto devem utilizar a tabela FBOLETO como tabela principal (master), porém o sistema valida a tabela master dos relatórios como sendo FLAN e FLANBOLETO, o que impede a geração de boletos com essa nova tabela master.* |
| **Solução/Implementação:** | *Foi feito uma alteração nas validações para que a tabela master de boletos seja exclusivamente a FBOLETO, sendo assim, relatórios que utilizam a FLAN e FLANBOLETO não serão gerados. Foi incluído uma mensagem de alerta ao acessar o sistema com esta informação.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
