---
content_hash: 4d2c937df363cafc6086e67b8102790cad95346d40ee3532713023bde7bfa8ee
fetched_at: '2026-06-29T00:08:29.412544+00:00'
page_id: '272145051'
product: rm
source: tdn-rm
title: 521382 MRH-7229 DT Qtde Faltas Cadastro Ferias
type: documentation
url: https://tdn.totvs.com/display/LRM/521382+MRH-7229+DT+Qtde+Faltas+Cadastro+Ferias
version: 110
---

# QTDE DE FALTAS NO CADASTRO DE FÉRIAS QUANDO POSSUI ESTORNO DE FALTAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Férias* |
| **Situação/Requisito:** | Na tela do cadastro de férias do executável, a quantidade de faltas estava somando a referência dos eventos com CC 8 (FALTAS) e subtraindo a referência dos eventos com CC 128 (ESTORNO DE FALTAS).  Entretanto na base do cliente os eventos com CC 128 estão cadastrados como Base de Cálculo. |
| **Solução/Implementação:** | Tratar na apuração das faltas do cadastro de férias do executável, para subtrair a referência do CC 128 somente quando o evento for do tipo Provento. |
| **Tickets relacionados:** | MRH-7229 |

divs
