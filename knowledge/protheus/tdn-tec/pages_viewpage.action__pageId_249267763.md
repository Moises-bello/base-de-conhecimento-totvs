---
content_hash: 5d3237e17a7be9c734c19ef973f2f579169560e42a22dfa48d06de2bb70af4e8
fetched_at: '2026-07-02T19:24:20.454688+00:00'
page_id: '249267763'
product: protheus
source: tdn-tec
title: Access violation na geração de stack de erro ADVPL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=249267763
version: 3
---

Access violation na geração de stack de erro ADVPL

|  |  |
| --- | --- |
| Situação | Access violation na geração de stack de erro ADVPL |
| Ocorrência | Após um erro sistêmico, ao tentar gerar o stack, utilizava um objeto que já havia sido destruído |
| Correção | Alteração para pegar a informação de uma outra forma, garantindo a integridade do stack ADVPL e evitando o access violation. |
| Informações adicionais | * Referente ao chamado: SSIM-364 * Referente à ocorrência: não há ocorrência associada * Disponível em builds superiores a  7.00.131227A - 1.0.3 |
