---
content_hash: 90c3843047af1ded33bb85ad88355bd92d5dbaf19c03b57b43b20bf2ba284c16
fetched_at: '2026-06-29T00:08:15.100790+00:00'
page_id: '244730107'
product: rm
source: tdn-rm
title: TVFSZC_DT_Matricula_Lista_Espera_Disiciplina_Correquisito
type: documentation
url: https://tdn.totvs.com/display/LRM/TVFSZC_DT_Matricula_Lista_Espera_Disiciplina_Correquisito
version: 114
---

# MATRÍCULA EM LISTA DE ESPERA - DISCIPLINA COM CORREQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Matrícula em Lista de Espera - Disciplina com Correquisito* |
| **Situação/Requisito:** | *Quando o aluno já cursou a disciplina de correquisito o sistema não está permitindo que ele seja colocado na lista de espera mesmo com o parâmetro "Bloquear matricula em lista de espera de disciplina com correquisito" marcado.* |
| **Solução/Implementação:** | *Ajuste na validação quando o parâmetro "Bloquear matricula em lista de espera de disciplina com correquisito" estiver marcado, para que seja verificado se o aluno já cursou o correquisito, sendo positivo, o mesmo será incluído na lista de espera, caso contrário não será inserido.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
