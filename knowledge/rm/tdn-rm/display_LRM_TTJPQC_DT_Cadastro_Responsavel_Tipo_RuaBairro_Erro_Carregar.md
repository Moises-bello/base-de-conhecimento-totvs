---
content_hash: c5008b352bfc5e39c2f25c63abae5fae8cf0e27d6cbfbdfcf2ca76e6c363e1db
fetched_at: '2026-06-29T00:06:14.509443+00:00'
page_id: '210046528'
product: rm
source: tdn-rm
title: TTJPQC_DT_Cadastro_Responsavel_Tipo_RuaBairro_Erro_Carregar
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJPQC_DT_Cadastro_Responsavel_Tipo_RuaBairro_Erro_Carregar
version: 1
---

# CADASTRO DE RESPONSÁVEIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Cadastro de responsáveis* |
| **Situação/Requisito:** | *Ao cadastrar um responsável no portal do processo seletivo o sistema estava exibindo um erro não tratado html quando é carregado os campos 'Tipo rua' e 'Tipo bairro', também está ocorrendo problema neste campos ao carregar dados de um usuário que já existe, não preenchendo corretamente os campos com as informações do usuário.* |
| **Solução/Implementação:** | *Foi verificado que o erro html era gerado por tentar carregar o campo mais de uma vez, sendo assim, foi feito o ajuste no método que carrega os componentes para carregar somente uma vez, evitando assim o erro. Com relação ao erro ao carregar os dados de um usuário já existente foi identificado que não existia funções para carregar o 'Tipo rua ' e 'Tipo bairro', as funções foram criadas e os dados passaram e ser carregados corretamente quando o usuário em questão no processo seletivo já existir na base de dados do cadastro de pessoa.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** | *11.82.42* |
| **Versão Expedida:** | *11.82.42* |

divs
