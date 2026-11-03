---
content_hash: 62f350032d03ed3d0947ac8066a0e7c9d57b88147c2ecbe7262a9a37e054c547
fetched_at: '2026-06-29T00:06:27.542367+00:00'
page_id: '233734545'
product: rm
source: tdn-rm
title: TUIJJ6_DT_ACESSO_PORTAL_FUNCIONARIO_DEMITIDO
type: documentation
url: https://tdn.totvs.com/display/LRM/TUIJJ6_DT_ACESSO_PORTAL_FUNCIONARIO_DEMITIDO
version: 117
---

# ACESSO AO PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Acesso ao RM Portal* |
| **Situação/Requisito:** | Quando um funcionário possui data de demissão já cadastrada para um dia futuro na competência atual, ao acessar algumas páginas do portal o funcionário recebia a mensagem de erro de que estava demitido. |
| **Solução/Implementação:** | *Foi adicionada uma validação da situação do funcionário para o portal, onde é verificada também se a data de demissão já passou ou ainda está por vir, pois antes era verificado apenas se estava na competência atual* |
| **Chamados relacionados:** | TUIJJ6 |

divs
