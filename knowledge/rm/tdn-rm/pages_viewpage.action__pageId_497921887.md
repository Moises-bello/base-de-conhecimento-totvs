---
content_hash: a42d0dba8e760cc30d225706576c02c11e7c36e912caba6777a77fd37635e5c8
fetched_at: '2026-06-29T00:10:22.626189+00:00'
page_id: '497921887'
product: rm
source: tdn-rm
title: Processos - Notificações de Boleto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=497921887
version: 8
---

# Procedimentos para utilização

---

O sistema pode ser parametrizado para enviar notificações de boletos vencidos e vincendos, para os clientes que possuem o app instalado. Para configurar e disparar as notificações, basta acessar **Utilitários / Parametrizações do App / Notificações de Boleto.**Ao clicar em executar, o sistema irá verificar a data de vencimento dos boletos de acordo com a parametrização escolhida e disparar notificações para todos os usuários que possuem boletos nas condições dispostas.

Para habilitar este menu, deverá ser habilitada a permissão de perfil do usuário, em **Utilitários - Portal / App - Notificações de Boletos**, como mostra a imagem abaixo:

Importante

Caso queira customizar o texto de envio destas notificações, basta acessar 

# Exemplos de utilização e descrição dos parâmetros

---

**Seguem alguns exemplos e uma breve descrição sobre as opções presente para este processo:**

* **Enviar no dia do vencimento:** Envia notificações para os usuários, alertando que o boleto vence no dia atual, ou seja, a notificação irá chegar na data de vencimento do boleto;
* **Dias antes do vencimento:** Determina que, a partir de x dias, serão enviadas notificações aos usuários, sobre seus boletos que irão vencer.

Exemplos!

* Situação A:
  + Boleto X irá vencer no dia 20/06;
  + Boleto Y irá vencer no dia 22/06;
  + Hoje é 19/06;
  + O parâmetro de notificação do Meu Imóvel foi definido para 3 dias antes do vencimento;
  + O sistema irá consultar quais boletos estão para vencer, dentro de 3 dias contados a partir da data atual;
  + O sistema irá enviar a notificação do boleto X e do boleto Y para o usuário e armazenar a informação de que a notificação destes boletos foi enviada na tabela de boletos enviados;
  + Caso o registro dos boletos já se encontrem nesta tabela, não serão enviadas novas notificações.
* Situação B:
  + Boleto A irá vencer no dia 20/06;
  + Boleto B irá vencer no dia 22/06;
  + Hoje é 19/06;
  + O parâmetro de notificação do Meu Imóvel foi definido para 2 dias antes do vencimento;
  + O sistema irá consultar quais boletos estão para vencer, dentro de 2 dias contados a partir da data atual;
  + O sistema irá enviar a notificação apenas do boleto A para os usuários e armazenar a informação de que a notificação deste boletos foi enviada na tabela de boletos enviados.
  + Caso o registro do boleto já se encontre nesta tabela, não será enviada nova notificação.

* **Dias após o vencimento:** Determina que, a partir de x dias de vencido, serão enviadas notificações aos usuários, sobre seus boletos em atraso.

Exemplos!

* Situação A:
  + Boleto X venceu no dia 15/06;
  + Hoje é 19/06;
  + O parâmetro de notificação do Meu Imóvel foi definido para 5 dias após o vencimento;
  + O sistema irá consultar quais boletos estão vencidos, passados 5 dias ou mais a partir da data de vencimento;
  + O sistema não irá enviar nenhuma notificação, visto que o boleto ainda não tem 5 dias de vencido no sistema.

* Situação B:
  + Boleto A venceu no dia 01/06;
  + Boleto B venceu no dia 15/06;
  + Hoje é 19/06;
  + O parâmetro de notificação do Meu Imóvel foi definido para 4 dias após o vencimento;
  + O sistema irá consultar quais boletos estão vencidos, passados 4 dias ou mais a partir da data de vencimento;
  + O sistema irá enviar a notificação do boleto A e do boleto B para os usuários e armazenar a informação de que a notificação destes boletos foi enviada na tabela de boletos enviados;
  + Caso o registro dos boletos já se encontrem nesta tabela, não serão enviadas novas notificações.

*Tela do processo de Notificação do Meu Imóvel.*

*Um exemplo do aplicativo Meu Imóvel, no Android, recebendo e exibindo as notificações para um cliente, após disparo do processo. Neste caso o cliente possui três boletos, um vencido, um vencendo hoje e outro a vencer..*

Observação: Este processo poderá ser agendado e executado de forma automática e recorrente.
