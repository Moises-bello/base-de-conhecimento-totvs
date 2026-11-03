---
content_hash: 9bc62b35b42228167dbb221ae926cd75b2fa1256d1ad50b139b76d5939ec9add
fetched_at: '2026-06-29T00:08:05.901050+00:00'
page_id: '236421548'
product: rm
source: tdn-rm
title: TURTYD_DT_Fontes_Geradoras
type: documentation
url: https://tdn.totvs.com/display/LRM/TURTYD_DT_Fontes_Geradoras
version: 118
---

# FONTES GERADORAS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Segurança e Saúde Ocupacional |
| **Função:** | Edição de Fontes Geradoras |
| **Situação/Requisito:** | Ao realizar a edição de uma Fonte Geradora do tipo Situação Geradora, o sistema está carregando no campo Cód. Esocial, a descrição (Valor inválido para o campo de lookup.) |
| **Solução/Implementação:** | Verificado que o sistema não aplicava corretamente o filtro de acordo com o tipo Situação Geradora ou Agente Gerador, dessa forma, ao tentar recuperar a informação do lookup gerava esta inconsistência.  Como correção, foi realizado a aplicação do filtro. |
| **Chamados relacionados:** | TURTYD |

divs
