---
content_hash: c28dc78f91795aa1ab9aa6910cbd60974c2758b7c2398ad43032d7d708c40797
fetched_at: '2026-06-29T00:08:23.290501+00:00'
page_id: '270073908'
product: rm
source: tdn-rm
title: MEDU-1103_DT_Inscricao_Responsavel_Portal_Procecesso_Seletivo
type: documentation
url: https://tdn.totvs.com/display/LRM/MEDU-1103_DT_Inscricao_Responsavel_Portal_Procecesso_Seletivo
version: 116
---

# INSCRIÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo - Portal* |
| **Função:** | *Inscrição* |
| **Situação/Requisito:** | *Ao acessar o portal utilizando o cadastro de um responsável, na tela de inscrição, é exibido uma lista com os seus dependentes, porém se o responsável desejar se inscrever, é necessário que ele selecione a linha vazia na lista, porém, ao selecionar esta opção, o botão de confirmar a inscrição fica desabilitado, mesmo selecionando as demais opções da inscrição, impedindo assim a inscrição do responsável.* |
| **Solução/Implementação:** | *Foi identificado uma inconsistência na função javascript que faz a validação das opções de inscrição juntamente com a faixa etária da área de interesse, caso a lista ficasse na posição que identifica o 'não selecionado' o sistema considerava que não poderia validar a opções da inscrição, sendo assim, foi feito o ajuste na função para que permita a seleção do item vazio e assim permitir também a inscrição do responsável porém mantendo todos as devidas validações da inscrição.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
