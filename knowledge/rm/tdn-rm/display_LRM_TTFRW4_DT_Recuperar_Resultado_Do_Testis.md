---
content_hash: 01a94b729a1fdeb7917e95d6784458cb24a0ae5de4ff6c7d8924418a521d7e79
fetched_at: '2026-06-29T00:06:14.717276+00:00'
page_id: '210050316'
product: rm
source: tdn-rm
title: TTFRW4_DT_Recuperar_Resultado_Do_Testis
type: documentation
url: https://tdn.totvs.com/display/LRM/TTFRW4_DT_Recuperar_Resultado_Do_Testis
version: 1
---

# RECUPERAR RESULTADO DO TESTIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Função:** | *Recuperar Resultado do Testis* |
| **Situação/Requisito:** | *Ao executar o processo “Recuperar Resultado do Testis”, o sistema apresenta a mensagem que o processo foi executado com sucesso, mas ao acessar o cadastro de “Avaliações da Etapa” -> Anexos -> Candidatos avaliados, o campo “Aproveitamento” permanece como “0” mesmo quando o candidato possui nota no “Testis”.* |
| **Solução/Implementação:** | *Ajuste no processo "Recuperar Resultado do Testis". Foi inserida uma nova validação no processo. Quando o candidato ainda não finalizou a prova no Testis, nenhuma nota é trazida na seleção.* *Criado um script para remover a nota "0" dos candidatos que ainda não finalizaram a prova.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTFRW4* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |

divs
