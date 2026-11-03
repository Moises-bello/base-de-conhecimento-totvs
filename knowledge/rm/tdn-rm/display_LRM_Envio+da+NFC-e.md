---
content_hash: db1fee2f82b3c4ca43ce8718130c61cd3dd9175984fc7be2bb694f04d822d210
fetched_at: '2026-06-29T00:09:20.125548+00:00'
page_id: '422545672'
product: rm
source: tdn-rm
title: Envio da NFC-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Envio+da+NFC-e
version: 3
---

Através deste processo os movimentos criados no TOTVS Gestão de Compras são convertidos em NFC-e e enviadas à SEFAZ do Contribuinte.  
Para executar o envio da NFC-e siga os seguintes passos:

* Carregue o TOTVS Gestão de Compras, Estoque e Faturamento;
* Vá até o menu Vendas | Faturamento e escolha a opção SPED NF-e (Estadual);
* Crie um filtro a sua escolha ou execute um filtro pré-existente;
* No botão Processos escolha a opção Enviar;
* Preencha as opções de filtro na tela e confirme o envio: Filial, Tipo de Movimento, Data de Emissão Inicial, Data de Emissão Final, Número Inicial e Final;
* A NFC-e funciona de forma síncrona, ou seja, no momento do envio da nota já é recebido o retorno da SEFAZ com o XML de autorizando ou rejeitando a NFC-e.

Após enviada a NFC-e o XML criado no processo é gravado o registro é criado na visão. Para consultá-lo basta editar o registro e acessar a aba XML.  
 Após ser executado o envio da NFC-e o registro assume alguns status.   
 Se ocorrer algum erro de validação feita pelo RM o registro assumirá o status Inconsistente. Se o envio for bem sucedido o registro assumirá o status Autorizada.     
 Veja aqui a explicação dos [status](http://tdn.totvs.com.br/display/LRM/Imagens+dos+Status+da+NF-e)[da NFC-e.](http://tdn.totvs.com.br/display/public/rm/Imagens+dos+Status+da+NF-e)

Parametrização

[Parametrização do Tipo de Movimento para o envio da NFC-e](http://tdn.totvs.com/display/LRM/TSW546_DT_Parametrizacao_Movimento_NFC-e)
