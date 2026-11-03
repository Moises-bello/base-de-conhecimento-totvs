---
content_hash: 5d2848d0d4e8390be2b8202ab3b1ce34fc1cb6679be12cd2e0033275a6f4ab1d
fetched_at: '2026-06-29T00:08:11.290687+00:00'
page_id: '242388998'
product: rm
source: tdn-rm
title: TVCL46_DT_Atestado
type: documentation
url: https://tdn.totvs.com/display/LRM/TVCL46_DT_Atestado
version: 112
---

# ATESTADO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Segurança e Saúde Ocupacional* |
| **Função:** | *Atestados* |
| **Situação/Requisito:** | *Ao cadastrar um atestado para o funcionário com data fim igual ao primeiro dia do mês de competência, o sistema altera a situação do funcionário para P (afastamento) e cria um histórico de situação. Porém ao verificar o histórico de afastamento, foi gerado histórico sem data final do afastamento.* |
| **Solução/Implementação:** | *Ajuste no cadastro de afastamento. Ao cadastrar afastamento para um funcionário no mesmo mês da competência, é perguntado ao usuário se ele deseja voltar a situação para a situação inicial ou não.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TVCL46; TVDN38* |
| **Requisito (ISSUE):** |  |

divs
