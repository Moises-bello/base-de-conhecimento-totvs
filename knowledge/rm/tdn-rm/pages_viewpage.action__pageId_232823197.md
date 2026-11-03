---
content_hash: e260da44399ed1a8887ee3f9a4f7940e4f97170dc5b592834d03902ba54329e0
fetched_at: '2026-06-29T00:06:27.492450+00:00'
page_id: '232823197'
product: rm
source: tdn-rm
title: TTEWNQ_DT_Alteração_Global_De_Salarios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=232823197
version: 114
---

# ALTERAÇÃO GLOBAL DE SALÁRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Alteração Global de Salários* |
| **Situação/Requisito:** | Ao realizar "Alteração de Salários", marcando a opção "Salário Composto | Reprogramar evento que compõe Salário Composto", e clicar em "Avançar", o botão "Calcular percentual de aumento complementar" fica habilitado. E ao utilizar o "Tipo de Alteração Salário" igual a "Fórmula", o campo "Percentual" fica desabilitado, porém preenchido com o valor que foi calculado pelo botão "Calcular percentual de aumento complementar". |
| **Solução/Implementação:** | Quando marcado a opção "Salário Composto | Reprogramar evento que compõe Salário Composto" o botão "Calcular percentual de aumento complementar" deve estar desabilitado. Quando marcado a opção "Salário Composto" estiver marcada ou desmarcada e a opção "Tipo de Alteração Salário" igual a "Fórmula" ou "Tabelas Salariais do TOTVS Gestao de Pessoas(RM Vitae)" o botão "Calcular percentual de aumento complementar" deve estar desabilitado. Quando o botão "Calcular percentual de aumento complementar" estiver desabilitado, o campo Percentual deve estar vazio e a opção "Aumentar número de casas decimais" desmarcado. |
| **Chamados relacionados:** | TTEWNQ |

divs
