---
content_hash: c5ae19a9ccea50157f5e0878210fdf41294f5a5a7162af5a5b66cb9014f15f3b
fetched_at: '2026-06-29T00:06:22.400258+00:00'
page_id: '223916492'
product: rm
source: tdn-rm
title: TTSKBX_DT_Erro_Calculo_Quantidade_Questoes_ProvaDinamica_Incorreto
type: documentation
url: https://tdn.totvs.com/display/LRM/TTSKBX_DT_Erro_Calculo_Quantidade_Questoes_ProvaDinamica_Incorreto
version: 122
---

# EXECUTOR - WEB SERVICE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Avaliação e Pesquisa* |
| **Função:** | *Executor - Web service* |
| **Situação/Requisito:** | *Ao carregar uma prova do tipo dinâmica utilizando o webservice, o sistema não estava carregando corretamente a quantidade de questões, retornava o valor 0.* |
| **Solução/Implementação:** | *Foi identificado que o número de questões para prova dinâmica não era carregado corretamente pois a prova dinâmica armazena em um local diferente as definições de questões, foi feito o ajuste para que se a prova for dinâmica o sistema busque a quantidade de questões pela tabela BHISTORICO, que armazena a quantidade de questões geradas dinamicamente para o identificador de execução da prova, ou seja, para o usuário.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TTOP39* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.43*  *12.1.10* |
| **Versão Corrigida:** | *11.82.43*  *12.1.10* |
| **Versão Expedida:** | *11.82.43*  *12.1.10* |

divs
