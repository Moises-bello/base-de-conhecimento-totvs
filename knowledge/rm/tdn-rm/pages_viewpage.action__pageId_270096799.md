---
content_hash: 4040f4626479f911e523f375693c248be07374eb30d09a77edead41ea4805817
fetched_at: '2026-06-29T00:08:23.892445+00:00'
page_id: '270096799'
product: rm
source: tdn-rm
title: MEDU-684_DT_Melhoria_no_Processo_de_Fechamento_e_Aberto_de_Período
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270096799
version: 114
---

# Melhoria no Processo de Fechamento e Aberto de Período

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Melhoria no Processo de Fechamento e Aberto de Período |
| **Situação/Requisito:** | É necessário que todas as tabelas do RM tenham chave primaria para que seja possível seu funcionamento na nuvem. No caso a tabela CSALDOEXERCICIO não possui PK. |
| **Solução/Implementação:** | Modificado o processo de fechamento do exercício contábil para que a tabela de saldo de exercício preencha o campo IDSALDOEXERCICIO.  Foi adicionado a chave primaria a tabela de saldo do exercício CSALDOEXERCICIO. |
| **Conversores e Parâmetros:** | Necessário base de dados para versão 12.1.15 e verificar se o script 'SD.2016.11\_01' foi executado com sucesso. |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | N/A |

divs
