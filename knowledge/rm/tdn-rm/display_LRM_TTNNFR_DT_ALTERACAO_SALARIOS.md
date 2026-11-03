---
content_hash: 941c99af58ff45df50b80ec55eb52a5d949176f9c19283f1041282429aaef97d
fetched_at: '2026-06-29T00:06:23.472705+00:00'
page_id: '224103151'
product: rm
source: tdn-rm
title: TTNNFR_DT_ALTERACAO_SALARIOS
type: documentation
url: https://tdn.totvs.com/display/LRM/TTNNFR_DT_ALTERACAO_SALARIOS
version: 121
---

# ALTERAÇÃO GLOBAL DE SALÁRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Alteração global de salários* |
| **Situação/Requisito:** | Ao processar a alteração salarial o sistema incluiu um salário MAIOR do que definido na tabela salarial (prints anexo).  Pelo que percebemos isso acontece quando o funcionário tem uma promoção e em seguida aumento por dissidio (retroativo) .  Nesse caso o sistema considera o percentual de aumento como se não houvesse controle por tabela salarial, quando deveria verificar a tabela |
| **Solução/Implementação:** | Otimizada rotina de alteração global de salários, para alteração com tabela salarial do VITAE.  A alteração foi realizada para que o sistema verifique o percentual de aumento do salário atual para o salário da tabela salarial, e aplique esse percentual de aumento para os meses retroativos |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTNNFR TUBJKL TTLLC0 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.10 11.82.43* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
