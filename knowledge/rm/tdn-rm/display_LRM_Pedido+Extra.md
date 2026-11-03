---
content_hash: e935c33339a15ed4869479133094afbaa58dfc5440396c88c1939c2151845d98
fetched_at: '2026-06-29T00:09:14.260472+00:00'
page_id: '421385173'
product: rm
source: tdn-rm
title: Pedido Extra
type: documentation
url: https://tdn.totvs.com/display/LRM/Pedido+Extra
version: 12
---

---

A aba **Pedido Extra** é composta pelos campos abaixo:

**Exibe obras e etapas para pedido extra:**

Este campo quando marcado exibe as obras e etapas no Pedido de Extra.

**Utilizar fluxo de aprovação para pedido extra:**

Este campo quando habilitado permite utilização de fluxo de aprovação manual, automática gerando um movimento único ou automática gerando um movimento por data de entrega, sendo:

- Manual: após a aprovação o pedido extra deve ser gerado manualmente pelo usuário através da opção Gerar Integração com Suprimentos/Faturamento;

- Automática Movimento Único: Assim que o pedido extra for aprovado, o sistema automaticamente irá efetuar a integração com Suprimentos/Faturamentos, gerando um único movimento com todos os itens do pedido extra;

- Automática Movimento por Data de Entrega: Assim que o pedido extra for aprovado, o sistema automaticamente irá efetuar a integração com Suprimentos/Faturamentos, gerando vários movimentos conforme a data de entrega definida para os itens do pedido extra;

* Ao ativar a aprovação do Pedido Extra, após verificar que não existem mais pedidos pendentes de aprovação nativa, o sistema deve dar mensagem informando que a aprovação nativa será desabilitada e permitindo que o usuário confirme ou cancele.
* Se confirmar, nos parâmetros de Projeto referentes ao Pedido Extra, a parte relativa à aprovação nativa deve ser desabilitada e deve aparecer a bolinha informando porquê esses campos estão desabilitados.

**Permitir aprovação de pedido extra através de senha:**

Este campo quando habilitado permite aprovação de pedido extra utilizando senha.

**Permite motivo de pedido extra vazio:**

Este campo quando habilitado permite gerar pedido extra com o campo motivo vazio.

**Permite alterar preço em pedido extra para produtos sem insumo:**

Este campo quando habilitado permite alterar preço em pedido extra para produtos sem insumo.

**Envia e-mail para aprovadores pedido extra:**

Este campo quando habilitado envia e-mail para aprovadores do pedido extra.

**Relatório de e-mail de aprovação:**

No envio de e-mail de aprovação é possível informar um relatório personalizado para envio do e-mail.

Informações

* O e-mail do usuário deve estar cadastrado;  
  Para configurar o e-mail do usuário acesse o modulo de Serviços Globais | Segurança | Acesso | Usuário.
* O campo e-mail do cadastro da Coligada deve estar preenchido;  
  Acesse o modulo de Serviços Globais | Administração | Cadastros | Coligadas.
* Os parâmetros globais deve esta configurado para envido de e-mail.  
  Para configurar acesse, Totvs Obras e Projetos | Ambiente | Parâmetros | Parâmetros Globais | Envio de E-Mails.
Veja um exemplo

**Nome movimento Pedido Extra :** Nome do tipo de movimento default para Pedido Extra.

**Tipo de Movimento do Pedido Extra :** Campo que define qual o tipo de movimento será considerado default para geração de movimento Pedido Extra.

Sempre que for criar um pedido extra por default sempre virá o tipo de movimento informado neste parâmetro.

É importante destacar que quando estiver integrado com o backoffice Protheus esse parâmetro não estará visível.

Imagem de um ambiente integrado com Protheus.

 

---
