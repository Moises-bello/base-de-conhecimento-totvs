---
content_hash: 35e0e79a5b64dc0f9f65aee213e95c2f0bba6bfab00724da1ac3ea05d9c9abca
fetched_at: '2026-06-29T00:06:17.071849+00:00'
page_id: '212904406'
product: rm
source: tdn-rm
title: TTDJT8_DT_Rescisao_Complementar_Dissidio_Diferenca_Salarial_Mesmo_Periodo
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDJT8_DT_Rescisao_Complementar_Dissidio_Diferenca_Salarial_Mesmo_Periodo
version: 1
---

# RESCISÃO COMPLEMENTAR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Diferença Salarial, Rescisão Complementar, GRRF, SEFIP 650* |
| **Situação/Requisito:** | *Os valores da GRRF e Sefip 650 não estavam corretos para funcionários que tivessem cálculo de diferença salarial e cálculo de rescisão complementar no mesmo período.*  *Ao calcular a rescisão complementar após o cálculo de dissídio, os valores dos códigos de cálculo 69 eram sobrepostos em um mesmo evento, não sendo possível identificar qual era a verba de folha e qual era de rescisão, além de manter um valor incorreto no envelope.* |
| **Solução/Implementação:** | *Criar um novo parâmetro para definir qual o evento de código de cálculo 69 que irá para o envelope em cálculos de folha e em cálculos de rescisão, como pode ser visto abaixo:*  *Foram alterados então os cálculos de diferença salarial e rescisão complementar para lançarem nos códigos de cálculo correspondentes ao tipo de cálculo que está sendo efetuado.* |
| **Chamados relacionados:** | *TTDJT8* |
| **Versões/Release:** | *11.82.42* |

divs
