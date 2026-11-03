---
content_hash: ab5a60cd84828d65293e972af6bd9ad3213e6f3692d1b07489cd1743f6d9e833
fetched_at: '2026-06-29T00:06:17.640816+00:00'
page_id: '213982194'
product: rm
source: tdn-rm
title: TTJICF_DT_FUNCAO_NDDIRFERIAS
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJICF_DT_FUNCAO_NDDIRFERIAS
version: 1
---

# Função de Fórmula

|  |  |
| --- | --- |
| **Linha de Produto:** | *Construção e Projetos* |
| **Segmento:** | *RM* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Retorno da função de Fórmula NDDIRFERIAS* |
| **Situação/Requisito:** | Foi identificado que o Delphi considerava todo o intervalo tanto de férias vencidas com proporcionais no caso: 09/04/2015 a 31/08/2015 totalizando 17 avos.  Já o .net obtinha primeiro os avos vencidos do período aquisitivo em aberto de 09/04/2015 a 21/12/2014 o que dá 8 avos depois os proporcionais de 22/12/2014 a 31/08/2015 o que dá 8 avos e ao todo 16 avos que multiplicado por 2.5 igual a 40 dias e menos 14 já gozados resulta em 26 dias.*.* |
| **Solução/Implementação:** | A função de formula NDDIRFERIAS em delphi passa a calcular os avos separadamente em vencidos e proporcionais após ter cada uma é então feito a soma. Tal atualização se fez necessário para acompanhar a mesma tratativa que é dada a mesma função de formula .Net. *.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTJICF.* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
