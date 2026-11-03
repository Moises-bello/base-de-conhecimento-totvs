---
content_hash: 0d0d71e54df64bf7db6df3610e359af45c2521f3b7e6bd0965c33482e3bf7bdc
fetched_at: '2026-06-29T00:08:57.287001+00:00'
page_id: '353289673'
product: rm
source: tdn-rm
title: 2622863 PORTALMOBILE01-4311 DT Inscricao Novo Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/2622863+PORTALMOBILE01-4311+DT+Inscricao+Novo+Portal
version: 1
---

# INSCRIÇÃO NOVO PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Inscrição no novo portal |
| **Situação/Requisito:** | Se os dados de algum dos responsáveis fossem obrigatório e o outro não, quando o candidato informava que o responsável que era obrigatório usaria os mesmos dados do outro responsável que não era obrigatório o sistema não informava que os dados passariam a ser obrigatórios. |
| **Solução/Implementação:** | Ajuste na validação de obrigatoriedade de campos dos responsáveis na inscrição do candidato, pois algum responsável pode ignorar a regra de obrigatoriedade devido parametrização, e esse responsável ser indicado como outro responsável que obriga o preenchimento dos campos, nesse caso deve-se obrigar o preenchimento. Exemplo. Nos parâmetros esta definido que os dados do pai ignoram a obrigatoriedade dos campos, e o responsável financeiro não. Se na inscrição for indicado que o responsável financeiro vai ser o pai do candidato, deve-se obrigar os campos no cadastro de pai e não deixar finalizar a inscrição. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
