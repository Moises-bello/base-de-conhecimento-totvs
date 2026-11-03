---
content_hash: 7d7c759b070b2e56090d801bf51c4f4e767b95309ba7144e348604ed0223f31f
fetched_at: '2026-06-29T00:11:20.517364+00:00'
page_id: '686468342'
product: rm
source: tdn-rm
title: 6- Validação do Extrato de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=686468342
version: 5
---

O próximo passo a ser validado é a geração do extrato de caixa, acessando:

**Movimentações Bancárias -> Extrato de Caixa**

Para validação do extrato de caixa, criar um filtro buscando Id da Transação conforme exemplo abaixo.

Após a criação do filtro copiar o código TID na tela de transações

Executar o filtro e informar o código.

O extrato de Caixa gerado abaixo informa que o valor bruto de 1,12 que está disponível na conta transitória, já provisionado o valor 0,40 parametrizado da taxa. O valor a ser repassado para a conta banco é o valor líquido já deduzindo a taxa da transação, sendo repassado para a conta banco definida o valor de 0,72. 

Para criação das partidas de saque transferência e deposito transferência, o processo de Conciliação precisa ser executado.
