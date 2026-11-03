---
content_hash: 9e8773c3215dfeae29c1255fa4e71632c95a658b8ade3c103aa3040d978f5280
fetched_at: '2026-06-29T00:11:23.037676+00:00'
page_id: '706146430'
product: rm
source: tdn-rm
title: Gerar QRCode de configuração - Minha Contagem de Estoque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=706146430
version: 5
---

Antes mesmo de logar no aplicativo o usuário precisa configurar a rota para o servidor, a configuração da rota pode ser facilmente compartilhada através de QRCode e o app configurado apenas apontando a câmera para o QRCode no momento da sua configuração.

A criação do QRCode pode ser feita facilmente utilizando recurso nativo do sistema, veja os passos:

1) Acessar o processo de geração do QRCode

* Clique em executar
* Em localizar digite "QR Code", ao iniciar a digitação já vai localizar o processo.
* Clique em Estoque > "QR Code para Configuração Automática"

2) Agora na tela de processo basta seguir os passos:

* Preencha o IP da máquina que está rodando o "RM.Host.exe" ou "RM.Host.Service.exe".
* Preencha a porta utilizada na configuração "ApiPort".
* Marque "Usar HTTPS" apenas se o servidor existe uma conexão segura e foi configurado para isso.
* Clique em "Gerar QR Code", vai gerar o "QR Code" no espaço em branco do lado direito da tela.
* Clique em "Copiar para área de transferência", o "QR Code" vai ser copiado como uma imagem e pode ser enviado por e-mail, vinculado a uma documentação, impresso entre outros.
* Prontinho, agora você tem seu QR Code de configuração rápida que pode ser utilizado para configurador o app Minha Contagem de Estoque.
* Clique em Fechar para encerrar o processo.
