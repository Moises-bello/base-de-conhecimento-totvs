---
content_hash: af5053a97aea346e52756522eeb809018b8d113720ba23ca3bec78bd61b43684
fetched_at: '2026-06-29T00:06:15.683404+00:00'
page_id: '211060108'
product: rm
source: tdn-rm
title: TTIDEC_DT_Rescisao_Complementar_Aumento_Vigencia_Aviso_Previo
type: documentation
url: https://tdn.totvs.com/display/LRM/TTIDEC_DT_Rescisao_Complementar_Aumento_Vigencia_Aviso_Previo
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
| **Chamados relacionados:** | *TTIDEC* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** | *11.82.42* |
| **Versão Expedida:** | *11.82.42* |

divs
