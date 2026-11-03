---
content_hash: b6263a006b3d91cd3f30b87c94c9dd8082b3042d69d83670d90ed85919ff004a
fetched_at: '2026-06-29T00:08:53.345252+00:00'
page_id: '344470162'
product: rm
source: tdn-rm
title: 2443842 FINANCEIRO01-5799 DT Carteira 104 Santander
type: documentation
url: https://tdn.totvs.com/display/LRM/2443842+FINANCEIRO01-5799+DT+Carteira+104+Santander
version: 2
---

# Cobrança com carteira 104 do banco Santander

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Geração de Código de Barras e IPTE |
| **Situação/Requisito:** | Cliente relata que o banco Santander modificou a geração do código de barras dos boletos e que agora a carteira é 104, mesmo aceitando a remessa com carteiras 101.  A remessa é realizada por arquivo de gerador de saídas com os dados da carteira na posição 58, ou seja, a remessa recebe valor 1, logo a alteração no sistema não modifica dados da remessa, apenas o preenchimento do código de barras e ipte. |
| **Solução/Implementação:** | Agora o sistema irá preencher os dados do código de barras e ipte com a carteira 104. Para isto é necessário preencher o campo "Tipo Carteira" da aba "Dados Adicionais" do convênio com o código da carteira igual a 104. Caso a carteira não seja a 104, o campo "Tipo Carteira" deve estar preenchido com o valor 101. Ou seja, o sistema passa a consistir o campo "Tipo Carteira" para cálculo do código de barras no caso das carteiras 101 e 104. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 2401679, 2368373, 2436190, 2421742 |
| **Requisito:** | FIN000024 |
| **Documento de Referência:** | N/A |
