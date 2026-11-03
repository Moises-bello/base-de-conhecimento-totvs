---
content_hash: f91e57e2f9bf73fa363c377426ea603cf365b45bdcd0e856a3d486803e96b3fb
fetched_at: '2026-06-29T00:08:27.269812+00:00'
page_id: '271404766'
product: rm
source: tdn-rm
title: 377451 MRH-5560 DT INSS Ferias Terceiro Mes
type: documentation
url: https://tdn.totvs.com/display/LRM/377451+MRH-5560+DT+INSS+Ferias+Terceiro+Mes
version: 111
---

# INSS FÉRIAS DO TERCEIRO MÊS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Férias* |
| **Situação/Requisito:** | Ao calcular férias que pegam 3 competências, por exemplo de 31/01 a 01/03, o INSS de Férias não está considerando o parâmetro "Limita desconto do INSS ao teto (férias em meses partidos)", para limitar o valor total ao teto. |
| **Solução/Implementação:** | Ajuste no cálculo do INSS férias, para tratar o parâmetro "Limita desconto do INSS ao teto (férias em meses partidos)", quando o periodo de férias atingir 3 competências. |
| **Tickets relacionados:** | 377451 |

divs
