---
content_hash: bd81cda5bef389db1bcdfa15604c66d4dc04c2d9e45f5428b6fb524bd605d451
fetched_at: '2026-06-29T00:06:15.700798+00:00'
page_id: '211060309'
product: rm
source: tdn-rm
title: TTOJYZ_DT_Rescisao_Complementar_Aumento_Vigencia_Aviso_Previo
type: documentation
url: https://tdn.totvs.com/display/LRM/TTOJYZ_DT_Rescisao_Complementar_Aumento_Vigencia_Aviso_Previo
version: 1
---

# RESCISÃO COMPLEMENTAR COM AUMENTO SALARIAL NO MÊS POSTERIOR À DEMISSÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Rescisão Complementar* |
| **Função:** | *Rescisão Complementar* |
| **Situação/Requisito:** | *Quando o aumento salarial ocorre no mês posterior à demissão do funcionário, durante o periodo de vigência do aviso prévio indenizado, ao processar a Rescisão Complementar, no recálculo do envelope da rescisão original os eventos adicionais que possuem fórmula estão ficando zerados.*  *Com isto, estão sendo lançados eventos de diferença com os valores negativos.* |
| **Solução/Implementação:** | *Ajuste no processo da Rescisão Complementar para manter o mesmo valor do envelope original de rescisão nos eventos adicionais que possuem fórmula, quando o aumento salarial ocorre no mês posterior à demissão do funcionário.*  *Neste caso, não deve ser lançado nenhum valor de diferença.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TTOJYZ* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.9* |
| **Versão Expedida:** | *12.1.9* |

divs
