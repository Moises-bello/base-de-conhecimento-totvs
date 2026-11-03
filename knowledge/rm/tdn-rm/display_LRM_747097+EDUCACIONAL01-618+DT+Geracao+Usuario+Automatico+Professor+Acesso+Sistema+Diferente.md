---
content_hash: c1bb66f87dd2ced5c8e012efe43b522ce2a23186cbd8c6fce31b950d0c4958a7
fetched_at: '2026-06-29T00:08:32.610752+00:00'
page_id: '273993209'
product: rm
source: tdn-rm
title: 747097 EDUCACIONAL01-618 DT Geracao Usuario Automatico Professor Acesso Sistema
  Diferente
type: documentation
url: https://tdn.totvs.com/display/LRM/747097+EDUCACIONAL01-618+DT+Geracao+Usuario+Automatico+Professor+Acesso+Sistema+Diferente
version: 105
---

# PROFESSOR - GERAÇÃO AUTOMÁTICA DE USUÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Geração de lançamentos financeiros* |
| **Situação/Requisito:** | *Foi identificado que na geração automática de usuários para professores, o sistema não respeita a parametrização do campo "Permissão para acessar", se informar "Portal" ou "Sistema", o sistema sempre define como "SistemaPortal".* |
| **Solução/Implementação:** | **Foi identificado que ao salvar o professor, o método que faz a geração automática do usuário não está carregando todos os parâmetros corretamente, estava faltando o tipo de acesso, sendo assim, foi feito o ajuste para carregar também este parâmetro e gerar o usuário corretamente.** |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |

divs
