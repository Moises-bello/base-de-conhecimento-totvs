---
content_hash: 3ef251998a6b5637b0d7c48624131f20900987914e0cd1fe337f370346bc6611
fetched_at: '2026-06-29T00:10:22.525302+00:00'
page_id: '496818401'
product: rm
source: tdn-rm
title: Meu Imóvel - Notificações de Boleto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496818401
version: 7
---

# **1) Procedimentos para utilização**

---

Neste parâmetro, poderemos definir as mensagens que serão enviadas aos clientes que possuem boletos vincendos, em atraso e que vencem na data atual.

Lembrando que para que as notificações sejam enviadas, é preciso executar o [processo de envio de notificação.](https://tdn.totvs.com/pages/viewpage.action?pageId=497921887)

Para acessar a customização de mensagens o usuário deverá acessar **Parâmetros / Portal do Cliente / Notificações de Boleto.**

Nesta tela será possível configurar um texto que será enviado ao cliente, referente aos seus boletos. Há um limite de 200 caracteres por mensagem.

Como podemos ver, será possível também inserir mnemônicos. Os mnemônicos disponíveis são:

* Os mnemônicos abaixo podem ser utilizados tanto para boletos oriundos de Contratos de Vendas quanto Contratos de Aluguel:

1. **[VCT]**: Data do vencimento do boleto;
2. **[VLR]**: Valor do boleto;
3. **[MES]**: Mês de competência;
4. **[EMP]**: Nome do Empreendimento.

* Estes mnemônicos devem ser utilizados **apenas** para boletos de Aluguel:

1. **[NCL]:** Número do Contrato de Locação**;**
2. **[DSP]:** Descrição da Despesa.

Após esta configuração, e após disparo / agendamento do [processo de envio de notificações](https://tdn.totvs.com/pages/viewpage.action?pageId=497921887),  O sistema irá mostrar a mensagem customizada no celular do usuário, como no exemplo abaixo:

Mensagem sendo exibida no celular do usuário
