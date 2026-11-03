---
content_hash: 30719cb1d6d1520025c6aa64c6c19bf78d7717a78bbc6ad91e8453876dcc3720
fetched_at: '2026-06-29T00:09:52.899740+00:00'
page_id: '439698918'
product: rm
source: tdn-rm
title: 04.1.06.01 - Pagamento com Cartão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439698918
version: 8
---

Na visão de boletos/lançamentos do Educa Mobile foi criado uma opção para pagar com Cartão os lançamentos em Abertos.

A instituição irá definir se permite o pagamento por essas opções, e se afirmativo, o usuário poderá realizar o pagamento com Cartão de Crédito ( à vista ou parcelado) ou Cartão de Débito.

Através do menu: Financeiro | Boletos é possível realizar o pagamento de mensalidade e outras taxas usando Cartão da operadora CIELO.

Esta funcionalidade poderá ser utilizada somente se estiver configurado para pagamentos com "Checkout Cielo", disponível nos **parâmetros 15.05.03 Integração | Financeiro | Educacional | Contas a Receber | Baixas | Cartão de Crédito/Débito | Configurações E-commerce**

A opção de pagamento com Cartão, será apresentado através do botão: "Pagamento com Cartão", que ficará disponível abaixo de cada lançamento.

Após selecionar o botão: "Pagar com Cartão", o usuário será encaminhado para a tela informado que o mesmo será redirecionado para a página da Cielo, onde neste momento ele tem a opção de "Efetuar o pagamento" (será redirecionado para a página da Cielo) ou Voltar (onde será redirecionando para a tela de visão de boletos em abertos).

Caso o usuário clique na opção: Efetuar pagamento, será apresentado a página da Cielo para que seja informado os dados do Cartão e os dados pessoais como: email, endereço e telefone.

Após efetuar o pagamento, o boleto será baixado automaticamente, caso ocorra a mensagem: Aguardando Liberação do Setor Financeiro, executar o processo em:

 **Totvs Gestão Financeira | Movimentações Bancárias | Cartão de Crédito / Débito | Ajuste de Transações**

Para que os boletos sejam baixados e o status seja alterado no Portal.

Observações:

• Nossa aplicação trabalha somente com o ambiente da operadora Cielo.

• Somente as bandeiras Visa e Mastercard podem ser configuradas.

 • Para a função débito no momento aceita somente a bandeira Visa ( Visa Electron) com cartões emitidos pelos bancos validados pela Cielo: Bradesco, Bando do Brasil, Santander e HSBC. Novos bancos certificados podem ser verificados no site [www.cielo.com.br](http://www.cielo.com.br/)

 • A digitação e validação dos dados do cartão ocorre no ambiente da sem interferência do aplicativo.

Para mais informações sobre o pagamento com Cartão, acesse o boletim técnico: [Integração Módulo E-Commerce](http://tdn.totvs.com/pages/viewpage.action?pageId=42043861).
