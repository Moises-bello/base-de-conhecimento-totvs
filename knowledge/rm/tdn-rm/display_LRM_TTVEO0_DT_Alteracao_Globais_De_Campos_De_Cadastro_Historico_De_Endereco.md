---
content_hash: 3f1287aa94042d86bee6a0506807af1a464545bca024cc193ec94797e6515245
fetched_at: '2026-06-29T00:06:21.699165+00:00'
page_id: '223177196'
product: rm
source: tdn-rm
title: TTVEO0_DT_Alteracao_Globais_De_Campos_De_Cadastro_Historico_De_Endereco
type: documentation
url: https://tdn.totvs.com/display/LRM/TTVEO0_DT_Alteracao_Globais_De_Campos_De_Cadastro_Historico_De_Endereco
version: 1
---

# ALTERAÇÃO DE CAMPOS DE CADASTRO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Alteração de Campos de Cadastro |
| **Situação/Requisito:** | Ao realizar uma alteração de endereço o sistema gera um erro relacionado a gravação do histórico. A alteração do endereço é realizada corretamente, porém os dados de histórico são gerados em duplicidade. |
| **Solução/Implementação:** | Alteração na estrutura responsável por realizar a gravação do histórico de endereços.  Implementado tratativa para os casos onde no endereço tenha apóstrofo ('). Exemplo: Santa Bárbara D'Oeste. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTVEO0 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | 12.1.9 |

divs
