---
article_id: 360007836431
category: Contabilidade Gerencial - Entidades
content_hash: 4eb47275a739f2a0ec6c646929ec7e0ff119a9826e4558df627a892b8178aeb5
fetched_at: '2026-06-28T22:40:49.697789+00:00'
product: protheus
section_id: 1500001537661
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Parâmetros de máscara
  contábil
type: support-article
updated_at: '2022-11-23T12:47:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007836431-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Par%C3%A2metros-de-m%C3%A1scara-cont%C3%A1bil
---

**Dúvida**

O parâmetro MV\_MASCARA, MV\_MASCCUS e MV\_MASCCTD podem ter máscaras diferentes?

**Ambiente**

Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
**Solução**

Estes parâmetros tratam-se apenas das máscaras, influenciando apenas na impressão dos relatórios e consultas, ou seja, não há problema algum que os mesmos estejam com máscaras distintas, configure-os de forma que facilite a visualização nos relatórios da empresa.

As mascaras determinam o nivel  das entidades na emissão dos relatórios e consultas

Exemplo:

Para a conta contábil que utiliza o parametro   MV\_MASCARA =  11123, a conta será exibida no relatório neste formato: **1.1.1.01.001**

Se o parâmetro MV\_MASCARA = 1, a conta será exibida neste formato **11101001**, sem pontos.

Parâmetros

|  |  |  |
| --- | --- | --- |
| **MV\_MASCARA** | Definição da máscara contábil. Deverá ser informado o número de dígitos para cada nível. Utilizada somente para impressão de relatórios e consultas. | 11123 |
| **MV\_MASCCUS** | Definição da máscara de centro de custo. Deverá ser informado o número de dígitos para cada nível. Utilizada somente para impressão de relatórios e consultas. | 1111 |
| **MV\_MASCCTD** | Definição da máscara de Item Contábil. Deverá ser informado o número de dígitos para cada nível. Utilizada somente para impressão de relatórios e consultas. | 1111 |
| **MV\_MASCCTH** | Definição da máscara de Classe de Valor. Deverá ser informado o número de dígitos para cada nível. Utilizada somente para impressão de relatórios e consultas. | 1111 |
