---
content_hash: f7001e7dd8a9c184cd266b0c311fd37c36c8173178ae0ce3e315614e1c6518ec
fetched_at: '2026-06-29T00:08:04.658029+00:00'
page_id: '235575913'
product: rm
source: tdn-rm
title: TUQWOK_Responsavel_Estrangeiro_Nao_Vincula_Corretamente
type: documentation
url: https://tdn.totvs.com/display/LRM/TUQWOK_Responsavel_Estrangeiro_Nao_Vincula_Corretamente
version: 117
---

# CADASTRO DE RESPONSÁVEIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Cadastro de responsáveis* |
| **Situação/Requisito:** | *Foi verificado que no portal do processo seletivo no "Quero me inscrever", após efetuar o cadastro do candidato o sistema direciona para o cadastro da mãe (Deve estar marcado nos parâmetros do processo seletivo), ao informar os dados da mãe como estrangeira e não informar o CPF (não é obrigatório quando estrangeiro) o sistema não cadastrava a mãe do candidato, vai direto para o cadastro do pai ou responsável financeiro.* |
| **Solução/Implementação:** | *Foi incluído uma validação para que se o CPF é obrigatório para desconsiderar caso o cadastro seja estrangeiro.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
