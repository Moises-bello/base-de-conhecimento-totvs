---
content_hash: 60422bca1786361f8e58dd4fa7b6cd9f33e586d5fab0c57dcbc3885f88e1fb66
fetched_at: '2026-06-29T00:08:38.310738+00:00'
page_id: '285647627'
product: rm
source: tdn-rm
title: 1084161 CONTROLADORIA01-341 DT INTEGRAR AQUISIÇÕES DE COMPRAS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285647627
version: 102
---

# Constituir Patrimônios

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Totvs Gestão Patrimonial. |
| **Função:** | Constituir Patrimônios. |
| **Situação/Requisito:** | No processo de integração dos patrimônios (Bonum/Nucleus), tem a opção de “Gerar o código do patrimônio a partir do título do patrimônio definido no produto” e a opção “Gerar código do patrimônio e patrimônio automaticamente”. Ocorre quando realizado a integração utilizando o novo processo de composição dos patrimônios, o sistema desconsidera o título informado no produto e verifica o título informado no grupo de patrimônio selecionado no processo de composição. Quando o “título amarrado” não está preenchido no grupo de patrimônio, nas condições acima, o sistema NÃO verifica o cadastro do produto, como foi selecionado nas opções. |
| **Solução/Implementação:** | Implementar a validação do parâmetro “Gerar o código do patrimônio a partir do título do patrimônio definido no produto” ao ser efetuada uma integração com constituição de um novo patrimônio a partir de outros produtos no movimento do RMNucleus. Esta implementação faz com que que sistema, caso não encontre o título amarrado ao grupo selecionado no patrimônio, busque pelo código do grupo do produto no RMNucleus. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |

divs
