---
content_hash: aced88603296757c02cfd0df41e99e5d95f33ba0c95ee463847b5c2c1008ab7d
fetched_at: '2026-06-29T00:10:27.743599+00:00'
page_id: '516642227'
product: rm
source: tdn-rm
title: CAGED - Exame toxicológico de desligamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516642227
version: 4
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Definir qual CNPJ do Laboratório será levado para o CAGED, quando o funcionário se recusar a realizar o exame na demissão. |
| **Situação/Requisito:** | Quando o CAGED era gerado para funcionários motoristas alocadas em seções identificadas por CEI e que se recusarão a realizar o exame toxicológico na demissão era considerado para este campo o CEI da seção do funcionário. Este comportamento gerava um erro ao importar o CAGED no programa ACI informando que o CNPJ era inválido. No sistema também era apresentada uma mensagem de alerta informando que o CNPJ do laboratório do exame deveria ser preenchido. |
| **Solução/Implementação:** | Foi criado um parâmetro no processo de geração do CAGED para que nesta situação o usuário possa definir qual CNPJ deve ser levado para o campo 'CNPJ do Laboratório',já que é um campo obrigatório. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | FOPROTINAS01-10023 |
| **Requisito:** | FOPROTINAS01-10023 |
| **Documento de Referência:** | <https://tdn.totvs.com/pages/releaseview.action?pageId=452719356> |
| **Pacote:** | N/A |
