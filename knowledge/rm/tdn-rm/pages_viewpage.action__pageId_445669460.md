---
content_hash: 5f48d35ad28a0f9196634e945ad59d63fd122230819de5449c75f30213184df4
fetched_at: '2026-06-29T00:09:54.968013+00:00'
page_id: '445669460'
product: rm
source: tdn-rm
title: 4135184 FOPCALCULO01-5415 Lançamento Centro de Custo (Folha Educacional)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=445669460
version: 2
---

# Lançamento Centro de Custo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Plataforma RH |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Lançamento Centro de Custo (Educacional) |
| **Situação/Requisito:** | Ao efetuar a associação de tabelas salariais aos professores, utilizando o mesmo nível e informando faixas diferentes, ao lançar a reprogramação salarial, o sistema apresenta valores diferentes nos lançamentos por centros de custo.  Realizamos o lançamento da folha do educacional, onde primeiramente populamos a tabela de salário composto através da rotina Folha Educacional / Processos / Reprogramação Salarial, depois realizamos o lançamento por centro de custo através da rotina de Folha Educacional / Processos / Lançamentos por centros de custo. Ao conferir o lançamento do centro de custo que consta na ficha financeira do funcionário, o mesmo está divergente do que está no salário composto. |
| **Solução/Implementação:** | Mensagem de aviso ao usuário para Lançamento de Centro de Custo quando o funcionário possuir rateio por centro de custo com evento do tipo Hora. |
| **Tickets relacionados:** | 4135184 |
