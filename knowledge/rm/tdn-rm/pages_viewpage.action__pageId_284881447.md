---
content_hash: 73b44b38925a00bad642e5bfef520719d4db3b882d3273b7518c3cf9977d739c
fetched_at: '2026-06-29T00:08:37.685662+00:00'
page_id: '284881447'
product: rm
source: tdn-rm
title: 925383 EDUCACIONAL01-1092 DT Contabilização Por Competência Contrato Não Contabiliza
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284881447
version: 101
---

# Geração de Contabilização Por Competência

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Geração de Contabilização por Competência |
| **Situação/Requisito:** | No Educacional fazemos a contabilização por competência, a maioria dos contratos estão contabilizando, porém existe alguns contratos que quando mandamos contabilizar o sistema dá a mensagem de processo executado com sucessos, porém não gera nenhuma informação na contabilização.  Já conferimos os eventos, os defaults, as fórmulas e está tudo correto, pois pra 90% dos casos está contabilizando. |
| **Solução/Implementação:** | Em determinado momento o sistema permitiu que mesmo o evento contábil não processando nenhuma informação contábil, as informações contábeis fossem gravadas somente do lado do educacional e com o idoperacao nulo, ou seja, sem informação no modulo contábil (isto é uma inconsistência), e não emitia nenhuma mensagem ao usuário.  Com isso mesmo se o usuário tentasse contabilizar a competência novamente o sistema não apresentava nenhum erro (mostrava processo executado com sucesso), pois entendia que o contrato/parcela já foram contabilizados.  Neste caso o correto seria o usuário estornar e contabilizar novamente, portanto adicionamos uma validação no sistema para que se isto ocorrer seja apresentada uma mensagem no log do processo explicando e orientando ao usuário a fazer o estorno. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |

divs
