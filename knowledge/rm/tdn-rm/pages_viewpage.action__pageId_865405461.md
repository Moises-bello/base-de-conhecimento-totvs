---
content_hash: 0391b4d25a73c8eec7c6641a205665d55051e7f43c5109276bd9ef9bb5178373
fetched_at: '2026-06-29T00:11:56.368092+00:00'
page_id: '865405461'
product: rm
source: tdn-rm
title: PI - Proposta - Condições de Pagamento - Adiantamento (Versão 12.1.2410 ou
  superior)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=865405461
version: 20
---

# *Gerando Boleto de Adiantamento via PI*

Novidade

### Boleto Híbrido no PI (Portal de Imóveis) - liberada a partir da versão 12.1.2506

Com essa nova funcionalidade, na tela de **Gerar Adiantamento**, será exibida uma nova opção chamada **"Boleto Híbrido"**. Após selecionar essa opção e gerar o boleto, o portal exibirá automaticamente as seguintes funcionalidades:

* **QR Code PIX**, permitindo o pagamento instantâneo via PIX.
* **Botão para Copiar QR Code PIX**, Para copiar o código do pix, facilitando pagamentos instantâneos.
* **Botão para Copiar Código de Barras**, para pagamentos através de boleto bancário tradicional.
* **Botão para Baixar o Boleto**, permitindo o download do documento para pagamento ou armazenamento.

Dessa forma, o cliente tem mais flexibilidade para optar pela forma de pagamento que melhor atende suas necessidades, garantindo rapidez e segurança nas transações financeiras.

* Para configurar o uso do boleto híbrido no portal, acesse: [Totvs Incorporação - Parâmetros - Portal do Cliente](https://tdn.totvs.com/pages/viewpage.action?pageId=435105047).
* Para saber mais sobre o funcionamento e vantagens do boleto híbrido, acesse: [Boleto Híbrido](https://tdn.totvs.com/pages/releaseview.action?pageId=908344227#0--345649096).
* Parâmetro para escolha do Meio de Pagamento do Adiantamento de Sinal: [Boleto Híbrido ou PIX/Boleto Online](https://tdn.totvs.com/pages/viewpage.action?pageId=801997247#:~:text=depois%20da%20entrega.-,Meios%20de%20Pagamento,-%3A%20Define%20quais)

**É importante que o relatório associado à impressão deste tipo de boleto esteja parametrizado para apresentar tanto a imagem do código de barras, quanto a imagem do qr code pix.**

Configuraçãp necessária **→** parâmetros para geração do adiantamento: [Tipo de Documento Adiantamento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105033#:~:text=Tipo%20de%20Documento%20de%20Adiantamento)

Os valores defaults para geração do lançamento financeiro é copiado da regra de entrada, mas se precisar mudar o tipo de histórico e tipo de contabilização pode definir o componente de adiantamento em Parâmetros Gerais=>Contrato de Venda => Adiantamento.  Esse componente será utilizado para buscar a parametrização do tipo parcela e só é permitido o componente do tipo de entrada

A partir do Release 12.1.2410, ao acessar a aba de Condições de Pagamento de uma proposta, o Portal de Imóveis, o sistema permite que se cadastre um **[Adiantamento de Sinal](https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Dados+Gerais+-+Adiantamento)** para garantir a venda do imóvel que o cliente tem interesse.

Para acessar esta opção selecione o imóvel desejado e simule uma proposta:

Em Condições de Pagamento, depois de selecionar a Modalidade, acione a opção Adiantamento para que possa incluir:

O PI exibe ao usuário a tela abaixo com as seguintes opções para gerar a parcela de **Adiantamento de Sinal**, que devem ser preenchidas de forma consciente, pois esses dados serão enviados à banco para cobrança:

* **Valor do Adiantamento de Sinal:** Informe o valor do adiantamento da parcela de sinal. Importa ressaltar as regras abaixo, para gerar este adiantamento:
  + Para gerar a parcela de adiantamento, não é necessário gerar um plano de pagamento, ou seja, o adiantamento pode ser gerado sem uma modalidade de pagamento associada à proposta;
  + O valor informado deve corresponder exatamente ao valor de uma parcela do tipo Sinal, que deve ser única, ou seja, não deve ter quantidade diferente de 1;
  + Esta parcela de adiantamento não poderá ter desconto de comissão associada a ela. Caso seja necessário descontar a comissão do sinal, deverá ser criado um outro grupo de parcelas deste tipo para realizar esta ação;
* **Data de Vencimento:** Informe a data de vencimento do boleto ou PIX a ser gerado, sendo que não é possível a geração com um vencimento posterior à data de execução desta ação. Ou seja, não é possível de se gerar esta parcela em atraso;
* **Forma de Pagamento:** Selecione a forma de pagamento na qual será realizada a cobrança desta parcela, conforme as parametrizações aplicadas na aba de *[Dados Bancários](https://tdn.totvs.com/pages/viewpage.action?pageId=514742343)*, do cadastro do empreendimento deste imóvel. As opções são:
  + **Boleto:** ao selecionar esta opção será gerado um boleto bancário; ou
  + **PIX:** ao selecionar esta opção será gerado a cobrança via PIX.
  + **Boleto Híbrido:** ao selecionar esta opção será gerado um [Boleto Híbrido](https://tdn.totvs.com/pages/releaseview.action?pageId=908344227#0-1) proporcionando ao cliente a flexibilidade de escolher sua forma preferida de pagamento, seja pela agilidade do PIX ou pela praticidade e prazo mais longo do boleto tradicional, sem comprometer a segurança e integridade da transação.
* **Gerar:** Após preencher e revisar opções acima, utilize este botão para gerar a cobrança bancária.

Esta tela exibe as orientações abaixo:

Atenção!

**Restrições:**  
- O adiantamento poderá ser gerado sem obrigação de gerar um plano de pagamento.  
- Para gerar o plano de pagamento valido, poderá ter mais de um sinal para o plano de pagamento, mas um deles deverá corresponder ao valor do adiantamento.  
- A parcela de sinal que corresponde ao valor de adiantamento não poderá ter desconto de comissão e desconto de venda..  
**Informações:**  
- O valor de adiantamento será utilizado para o abatimento automático do sinal, assim que o contrato for efetivado.

Após gerado o Boleto ou o PIX, o sistema exibe, além do o valor e da data de vencimento do mesmo, as opções abaixo:

* **Baixar Boleto:** ao clicar nesta opção o sistema irá baixar o arquivo em formato PDF do relatório associado à geração deste boleto. Este botão não exibido na geração do PIX;
* **Copiar Código de Barras/Copiar Código PIX:** ao clicar nesta opção, o sistema irá copiar as informações do código de barras deste boleto ou do QR Code do PIX para a área de transferência do sistema operacional. Caso o site do PI não tenha permissão para copiar informações para a área de transferência, será exibia uma mensagem de exceção informando que é necessário dar permissão no navegador (Google Chrome, Mozilla Firefox, Microsoft Edge, Ópera, etc.) para que a página do PI possa realizar esta ação; e
* **Cancelar Adiantamento:** ao clicar nesta opção, o sistema exibirá ao usuário a opção para cancelar o boleto ou PIX gerado, caso o cliente desista da operação ou caso o valor tenha sido gerado com um valor ou data incorreta.

No TCGI, essa ação é refletida na aba de [Adiantamento](https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Dados+Gerais+-+Adiantamento), da tela de cadastro de Vendas, onde é possível de se verificar os dados do boleto associado à transação PIX, do lançamento de adiantamento,

O boleto gerado para este lançamento de adiantamento, fica com Status de Remessa, Não Remetido:

Este boleto é associado à uma [Transação PIX](https://tdn.totvs.com/pages/viewpage.action?pageId=727916895), que fica com Status de Pagamento Solicitado, com tempo de expiração de cerca de 1 hora:

Ao acionar o botão **Cancelar Adiantamento,** o sistema exibe a mensagem de alerta abaixo, informando ao usuário que ao realizar esta ação, o boleto ou o PIX a ser cancelado já está enviado e registrado a banco:

*Você está prestes a cancelar o adiantamento já gerado. O boleto ou PIX associado a essa transação foi enviado ao banco. Deseja realmente continuar com o cancelamento?*

A Parcela de Adiantamento gerada é exibida na aba **[Adiantamento](https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Dados+Gerais+-+Adiantamento)**, do agrupador *Dados Gerais*, do TCGI:
