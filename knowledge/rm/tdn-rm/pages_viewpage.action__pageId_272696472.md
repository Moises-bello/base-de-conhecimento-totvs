---
content_hash: 0b72bae81df4bd2bba5b8547b009a2630f9213f23393e6c97ee94a05c399b4b2
fetched_at: '2026-06-29T00:08:30.512029+00:00'
page_id: '272696472'
product: rm
source: tdn-rm
title: 590910 MEDU-3100 DT Sistema está contradizendo o comportamento dos parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272696472
version: 107
---

# SISTEMA ESTÁ CONTRADIZENDO O COMPORTAMENTO INFORMADO NOS PARÂMETROS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | Geração de lançamentos |
| **Situação/Requisito:** | Sistema está contradizendo o comportamento informado nos parâmetros de integração com o financeiro. Ao marcar a opção de tipo contábil por serviço, o sistema diz que os lançamentos do serviço que não tiverem o tipo contábil preenchido não serão gerados mas o sistema está gerando os lançamentos como "Não contábil". |
| **Solução/Implementação:** | Alteração da mensagem de alerta nos parâmetros do sistema quando o tipo contábil for por serviço deixando explícito que o não preenchimento do tipo contábil no serviço, fará com que o respectivo lançamento seja gerado como "Não contábil".    O não preenchimento do tipo contábil no serviço passou a ser informado como Warning (Aviso) na geração de lançamentos. A mensagem também foi alterada a fim de deixar claro que o respectivo lançamento será gerado como "Não contábil" |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
