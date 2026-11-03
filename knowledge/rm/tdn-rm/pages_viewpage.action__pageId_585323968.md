---
content_hash: a3eacbc6e144f915590d440bc97b4a3bc494f6eec4abc8e34709ca51fb7e7830
fetched_at: '2026-06-29T00:10:53.791943+00:00'
page_id: '585323968'
product: rm
source: tdn-rm
title: 'Servidores e Portas API-APP:'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=585323968
version: 7
---

Após a instalação da BibliotecaRM, serão criados :

a)Pasta Pto-integração .

   Será criada no caminho conforme definido pelo usuário no momento da instalação.  
    Exemplo da instalação na pasta padrão:  
C:\totvs\CorporeRM\RM.Net\wwwroot\pto-integracao

b)Tags HTTPORT e APIPORT no Rm.host.config.

Será criado as tags conforme exemplo .

Essas portas serão utilizadas na configuração API e APP no menu Configurações/Parametrizador-outros parâmetros.

<add key="HTTPPort" value="8051" />  
<add key="ApiPort" value="8052" />

**Importante:**Para visualizar as informações do menu "Batidas fora do Perímetro " é obrigatório que  o **HOST** seja iniciado como administrador, caso contrário, será demonstrada na tela a mensagem para o usuário  "carregando" e nada será exibido.

O caminho do servidor será o mesmo  local da  instalação da BibliotecaRM.

Print da tela instalação BibliotecaRM Local.
