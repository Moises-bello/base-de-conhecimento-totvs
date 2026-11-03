---
content_hash: d01a3b065e5fc9362b8273440f6a30aa7365c9071600a53c7feb1a95ebbb9305
fetched_at: '2026-06-29T00:06:25.534933+00:00'
page_id: '224440721'
product: rm
source: tdn-rm
title: TUDWF8_DT_Funcionario_Apenas_Com_Molestia_Grave_DIRF
type: documentation
url: https://tdn.totvs.com/display/LRM/TUDWF8_DT_Funcionario_Apenas_Com_Molestia_Grave_DIRF
version: 123
---

# DIRF/INFORME DE RENDIMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF/Informe de Rendimentos* |
| **Situação/Requisito:** | Ao gerar a DIRF em arquivo, selecionando o filtro TODOS, não está sendo levado o funcionário que contém o evento de aposentadoria por moléstia grave no campo 4 – Linha 03 – Pensão, Proventos de Aposentadoria ou Reforma por Moléstia Grave e Aposentadoria ou Reforma por Acidente em Serviço. Mesmo o evento não obtendo incidência em IRRF esse evento deve ser levado para o arquivo da DIRF, e ao gerar o Informe de rendimentos o campo é preenchido com o valor corretamente conforme deveria. |
| **Solução/Implementação:** | *Ajustada geração da DIRF em Arquivo quando o funcionário tem apenas o valor referente a moléstia grave.  Quando selecionar a opção todos será levado se o valor for maior que zero.*  *Quando selecionar outra opção de seleção será levado se o valor for maior que R$28.123,91* |
| **Chamados relacionados:** | *TUDWF8,TUCWAR* |

divs
