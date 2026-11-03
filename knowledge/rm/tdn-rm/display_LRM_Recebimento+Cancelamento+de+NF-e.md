---
content_hash: 69ed6431f4162818e1fcd60790246bc9178e748fb026c63e7515e73077ae6106
fetched_at: '2026-06-29T00:09:29.305864+00:00'
page_id: '423938871'
product: rm
source: tdn-rm
title: Recebimento Cancelamento de NF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Recebimento+Cancelamento+de+NF-e
version: 3
---

A ferramenta Neogrid faz uma verificação de NF-es autorizadas no site da SEFAZ.   
Se for constatado que uma NF-e autorizada foi cancelada será disponibilizado para o Gestão de Estoque, Compras e Faturamento um XML de cancelamento com status 399 e terá descrição evidenciando o cancelamento, sendo possível realizar se recebimento no Gestão de Estoque, Compras e Faturamento.   
Quando realizado o recebimento de um XML de Cancelamento o Gestão de Estoque, Compras e Faturamento realizará a busca do registro da NF-e cancelada na tabela TNFEENTRADA (para verificar na aplicação, basta acessar Compras, TOTVS Colaboração - Cadastro XML) através da chave de acesso.   
Se existir o registro na tabela o mesmo será cancelado.   
Se esse registro tiver um movimento vinculado, o mesmo será cancelado, desde que seja possível, pois serão verificadas as já existentes consistências do processo de cancelamento de movimento tais como contábil, fiscal, financeiro, etc).   
Caso o registro não seja encontrado na tabela TNFENTRADA, o sistema irá verificar na base de dados se existe movimento com o mesmo nº, série e fornecedor e cancelá-lo caso exista.   
Também irá incluir o registro do XML de cancelamento na tabela TNFENTRADA com o status cancelado e vincular com o movimento que foi cancelado.
