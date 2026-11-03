---
content_hash: 1fe65c433e7cf1290251a1230baf1ab9c4a65059d7d16d33418f5142db45b4ca
fetched_at: '2026-06-29T00:06:22.386820+00:00'
page_id: '223916119'
product: rm
source: tdn-rm
title: TTUXOI_ReferenciaBibliografica_Nao_Exibe_Volume
type: documentation
url: https://tdn.totvs.com/display/LRM/TTUXOI_ReferenciaBibliografica_Nao_Exibe_Volume
version: 125
---

# REFERÊNCIA BIBLIOGRÁFICA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Referência bibliográfica* |
| **Situação/Requisito:** | *Foi identificado que ao gerar a referência bibliográfica o sistema não estava exibindo corretamente os dados de volume da publicação.* |
| **Solução/Implementação:** | Conforme ABNT6023 nos itens:  \* 8.7.2 - "Quando o documento for publicado em mais de uma unidade física, ou seja, mais de um volume, indica-se a quantidade de volumes, seguida da abreviatura v. Exemplo: 4 v." \* 8.7.3 - "Se o número de volumes bibliográficos diferir do número de volumes físicos, indica-se primeiro o número de volumes bibliográficos, seguido do número de volumes físicos. Exemplo: 5 v. em 3"     Sendo assim foi feito o ajuste na geração da referência bibliográfica para que se o valor dos volumes for um número inteiro, este será acrescido do ' v.' para que fique conforme definição do item 8.7.2 da ABNT6023, caso o valor dos volumes não contenha somente números, este será mantido e exibido como está, para atender ao item 8.7.3 que o volume poderá ser exibido no formato exemplo: "5 v. em 3", sendo que no momento da criação do volume no cadastro de publicação, deve ser feito seguindo as normas da ABNT para estes casos, pois a criação incorreta irá impactar na exibição incorreta da referência. |
| **Conversores e Parâmetros:** | *Informe os conversores/parâmetros.* |
| **Chamados relacionados:** | *TTZA31* |
| **Requisito (ISSUE):** | *Informe o requisito relacionado.* |
| **Versões/Release:** | *11.82.43*  *12.1.10* |
| **Versão Corrigida:** | *11.82.43*  *12.1.10* |
| **Versão Expedida:** | *11.82.43*  *12.1.10* |

divs
