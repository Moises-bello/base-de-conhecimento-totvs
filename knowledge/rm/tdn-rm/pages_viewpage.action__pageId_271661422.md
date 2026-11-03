---
content_hash: f348e30de5581d441795d13c149777b6961fc19f270516ab80e3eb0e2bfcfc97
fetched_at: '2026-06-29T00:08:28.130676+00:00'
page_id: '271661422'
product: rm
source: tdn-rm
title: 422949 MEDU-2542 DT Geração de Lançamento quando da erro não gera para as parcelas
  ok
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271661422
version: 114
---

# Geração de Lançamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Geração de Lançamento em massa |
| **Situação/Requisito:** | Ao gerar lançamentos em massa para todos os alunos do ensino médio, o sistema exibiu algumas mensagens de erro específicas para alguns alunos conforme exemplo abaixo:   * Não foi possível gerar a parcela porque o contrato está cancelado * Responsável financeiro da parcela inativo   Essas mensagens realmente barram a geração de lançamentos para o aluno apontado nas mesmas até que o ajuste seja efetuado. Porém na execução do processo para todos os alunos, as mensagens de erro barraram a geração de lançamentos até dos alunos que estavam com esses cadastros corretos. |
| **Solução/Implementação:** | Identificamos que o processo está apresentando uma mensagem de não conformidade que não está relacionada as validações do sistema, e com isso nenhum lançamento é gerado.  Esta situação está relacionada ao convenio que será vinculado ao lançamento, o cenário ocorre somente quando o CNAB Carteira é do banco Santander. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 422949 / MEDU-2542 |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
