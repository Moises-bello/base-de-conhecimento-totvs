---
content_hash: e20533aa98c93a1d2499387218ed629a2155ada7aae70b854078b08307556493
fetched_at: '2026-06-29T00:08:28.804158+00:00'
page_id: '271853280'
product: rm
source: tdn-rm
title: 292250 MRH-3704 DT Diferenca Recesso Estagio
type: documentation
url: https://tdn.totvs.com/display/LRM/292250+MRH-3704+DT+Diferenca+Recesso+Estagio
version: 113
---

# DIFERENÇA DE RECESSO DE ESTÁGIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Diferença Salarial* |
| **Situação/Requisito:** | Não é calculada diferença quando o funcionário é Estagiário e recebe o evento de Recesso de Estágio. |
| **Solução/Implementação:** | Criação de novos códigos de cálculo para Diferença de Recesso de Estágio.   356 - DIFERENÇA DE RECESSO DE ESTÁGIO  -> Calculado pelo módulo de Diferença Salarial.  Será a diferença do evento de CC 332.   357 - DIFERENÇA DE RECESSO DE ESTÁGIO VENCIDO  358 - DIFERENÇA DE RECESSO DE ESTÁGIO PROPORCIONAL  -> Calculados pelo módulo de Rescisão Complementar.  Serão a diferença dos eventos de CC's 333 e 334. |
| **Tickets relacionados:** | MRH-3704 |

divs
