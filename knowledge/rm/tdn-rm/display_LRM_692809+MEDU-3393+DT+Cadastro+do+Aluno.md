---
content_hash: 76139e0eca58350d575d88f8c72ae3d7efebb4178e5aa62386a61cb5786a4cbc
fetched_at: '2026-06-29T00:08:30.912483+00:00'
page_id: '272705540'
product: rm
source: tdn-rm
title: 692809 MEDU-3393 DT Cadastro do Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/692809+MEDU-3393+DT+Cadastro+do+Aluno
version: 115
---

# CADASTRO DO ALUNO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Cadastro do Aluno* |
| **Situação/Requisito:** | *Ao inserir/editar um aluno e em sua certidão de nascimento/casamento informar um número com 14 caracteres ocorre o seguinte erro: "Index and length must refer to a location within the string.".* |
| **Solução/Implementação:** | *Ajuste no cadastro do aluno para que seja feita a validação da certidão de nascimento/casamento apenas no modelo novo e não no modelo antigo como estava sendo feito. Além disso, foi ajustado a validação do modelo novo que estava considerando o campo 14º do número da certidão e não o 15º na validação do tipo de certidão.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
