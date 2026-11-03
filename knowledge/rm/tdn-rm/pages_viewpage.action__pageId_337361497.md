---
content_hash: ff80c3610c9de48be92d9586cb89cdbd1a060a39ae5735490f4ec3479e7729aa
fetched_at: '2026-06-29T00:08:51.681388+00:00'
page_id: '337361497'
product: rm
source: tdn-rm
title: Como verificar as configurações do  Firewall do  Windows no servidor do TSS?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=337361497
version: 7
---

O Firewall é um método de segurança que utiliza regras para bloquear ou permitir conexões e transmissões de dados entre o servidor e a internet. As configurações repassadas no Firewall podem bloquear o envio dos eventos do eSocial. Avalie as configurações do Firewall seguindo os passos abaixo:

* Acesse o Painel de Controle e clique em Firewall do Windows:

* Verifique se o Firewall está habilitado:

* Se estiver habilitado, clique em Configurações Avançadas para avaliar as regras que foram criadas para atender as conexões e transmissões de dados entre o servidor e a internet:

* Selecione as opções de Regra de Entrada /Saída e clique em Nova Regra:

**Obs:** A sequência a seguir deverá ser executada tanto para as Regras de Entrada, quanto as de Saída.

* Informe o protocolo que será utilizado pelas conexões (TCP) e avance:

* Adicione as portas que estão configuradas na instalação do TAF e do TSS ou habilite todas as portas:

* Libere a permissão para conexão e avance:

* Aplique a regra para todos os perfis e avance:

* Conclua inserindo um nome para a regra do Firewall que foi criada:

**Obs:**Reinicie os serviços do TAF  e do TSS.

* Se o Firewall estiver desabilitado não é necessário realizar nenhuma configuração, pois dessa forma ele não barra as conexões:
