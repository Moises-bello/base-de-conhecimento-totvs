---
content_hash: 1e6b73f40d4a66e9876c6d94d596bff128b25a411e1260b6b93cc6f5410fae05
fetched_at: '2026-06-29T00:10:37.254928+00:00'
page_id: '538493587'
product: rm
source: tdn-rm
title: Meu Imóvel - Notificações de Comunicados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=538493587
version: 7
---

# **1) Visão Geral**

---

Disponível em **Utilitários / Parametrizações do App / Notificações de comunicados**, o processo de notificação de comunicados, consiste em enviar para o cliente uma notificação em seu celular, através do App Meu Imóvel, quando um novo comunicado está disponível para ser lido.  
O texto que será exibido nesta notificação é definido no campo "Texto para notificação (App Meu Imóvel), no [cadastro de comunicados do Portal do Cliente.](https://tdn.totvs.com/display/LRM/Portal+do+Cliente+-+PDC+-+Comunicados)

As notificações são enviadas para os comunicados cuja publicação seja anterior a data atual de execução do processo e sua expiração, posterior a data atual.  
Os envios serão feitos para cada usuário, de acordo com as configurações dos empreendimentos informados nos comunicados e caso o comunicado seja global, todos os usuários receberão a notificação.

Ao clicar em executar, o sistema listará quais comunicados foram enviados.

E a notificação então, é recebida no celular do cliente:

Ao clicar na notificação o usuário será levado ao aplicativo Meu Imóvel, podendo então ler o novo comunicado enviado.

* Este processo pode ser agendado e executado de forma recorrente, respeitando a ordem dos comunicados cadastrados (data de publicação), se já foi lido pelo usuário e se já foi disparado no mesmo processo. O processo não poderá ser disparado duas vezes para o mesmo comunicado e usuário.
* Caso ocorra erro no envio dos comunicados, eles ficarão pendentes para a próxima tentativa, sempre respeitando suas datas de publicação e expiração.
