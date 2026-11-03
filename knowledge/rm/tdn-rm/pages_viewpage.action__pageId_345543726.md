---
content_hash: 67f4eec297366ac955d15dc360d6e4869a759a02e31cca0bfce3bfa6a66f0aaf
fetched_at: '2026-06-29T00:08:53.797311+00:00'
page_id: '345543726'
product: rm
source: tdn-rm
title: 2469233 FINANCEIRO01-5903 Default dados bancários em filiais diferentes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=345543726
version: 1
---

# Default dados bancários em filiais diferentes

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Inclusão de lançamento. |
| **Situação/Requisito:** | Na geração do lançamento para uma parcela do contrato do aluno onde no seu respectivo cliente/fornecedor tem cadastrados dados bancários e default de dados bancários sem filial em ambos os cadastrados.  O sistema gera o lançamento com dados bancários com Débito Automático, mas o tipo do boleto está como Boleto de Cobrança. |
| **Solução/Implementação:** | Otimização no processo de inclusão de um boleto via geração de lançamento. A alteração foi adaptar o sistema para carregar o default da forma de pagamento do cliente/fornecedor que tem filial por prioridade ou sem filial informada. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000268 |
| **Documento de Referência:** | N/A |
