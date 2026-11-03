---
content_hash: e47a5db5ca40672ac34e442c029e7de934d29139fefefef116a5bdc58e46e7c6
fetched_at: '2026-06-29T00:08:23.230191+00:00'
page_id: '269553030'
product: rm
source: tdn-rm
title: 96442_DT_Relatório_Balancete
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269553030
version: 113
---

# Relatório Balancete

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Relatório Balancete |
| **Situação/Requisito:** | Ao gerar o balancete com grau 4 por exemplo (não pode ser conta analítica) e marcar a opção Totalizar Totais das contas sintéticas embaixo o relatório é gerado praticamente sem dados, somente os campos Conta, Descrição e Reduzido saem com informação, o restante sai em branco.Se desmarcar a opção Totais das contas sintéticas embaixo mesmo com grau 4 a emissão é perfeita |
| **Solução/Implementação:** | Ajuste do relatório para que ao utilizar a opção "Totais das contas sintéticas embaixo" combinada com geração do relatório com grau parcial, ou seja, diferente de Total, o mesmo seja capaz de imprimir a totalização das contas sintéticas abaixo. O ajuste consiste em implementar a rotina que combina essas duas opções pois hoje o relatório não esta preparado para totalizar as sintéticas abaixo caso não possua pelo menos uma conta analítica na lista de impressão. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | N/A |

divs
