---
content_hash: d30afb8dd78b7336cd3d51b5ecd9774aa7c23de131dd7e00ee6acbab10836718
fetched_at: '2026-06-29T00:08:10.854248+00:00'
page_id: '241697391'
product: rm
source: tdn-rm
title: TVBLVX_DT_Guia_Inss
type: documentation
url: https://tdn.totvs.com/display/LRM/TVBLVX_DT_Guia_Inss
version: 110
---

# Guia de INSS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Guia de INSS* |
| **Situação/Requisito:** | O sistema está usando o evento de código de cálculo 322 - 2ª Parcela 13º Salario Licença Maternidade, abatendo da base de inss, mesmo o evento já estando nos valores a deduzir na guia, ou seja, ele está deduzindo duas vezes. |
| **Solução/Implementação:** | Ajuste realizado para que o sistema não deixe de calcular os proventos de incidência de inss de 13° quando há segunda parcela de 13° (cc 102)  e quando há código de cálculo 322 no envelope |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TVBLVX TVDCTW |
| **Requisito (ISSUE):** |  |

divs
