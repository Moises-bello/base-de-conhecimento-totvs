---
content_hash: a0d1e0579d8ef3a80d321724f59e289258996a4d464a04dd23594ae8782f1fe6
fetched_at: '2026-06-29T00:06:29.598603+00:00'
page_id: '234613778'
product: rm
source: tdn-rm
title: TUFZMP_DT_FIltro_Estado_Natal_Nacional
type: documentation
url: https://tdn.totvs.com/display/LRM/TUFZMP_DT_FIltro_Estado_Natal_Nacional
version: 119
---

# CADASTRO DE CANDIDATOS E RESPONSÁVEIS - PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Cadastro de candidatos e responsáveis pelo portal* |
| **Situação/Requisito:** | *Filtro de estados natais que sejam somente nacionais* |
| **Solução/Implementação:** | *Foi criado um parâmetro para que se marcado irá filtrar no portal do processo seletivo na lista de "Estado natal" no cadastro de candidato e responsáveis, somente estados com a flag "nacional" marcados no cadastro de estados e o estado que será considerado a exceção do cadastro estrangeiro, necessário para que o campo de CPF funcione corretamente, obrigando ou não o preenchimento. Sendo assim, ao marcar o parâmetro o sistema irá tornar obrigatório o preenchimento do estado estrangeiro e após marcar o parâmetro e definir o estado estrangeiro, o sistema irá exibir na lista somente estados nacionais e um estado estrangeiro.*  ***Obs: caso o parâmetro seja marcado e algum candidato que já exista na condição de estrangeiro tente se cadastrar novamente o sistema irá incluir uma nova validação de unicidade, será feita a validação pelo "Nome", "Data de nascimento" e "Naturalidade". Validação esta que tentará garantir que o candidato não se cadastre novamente, ressaltando que esta só será ativada caso o parâmetro de filtro de estado natal esteja ativo.***  ***Tela de parâmetros do processo seletivo:***      ***Tela do portal do processo seletivo:*** |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
