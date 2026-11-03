---
content_hash: ce5c4e79581078a834f79632b34a775ebb2d24098b05423719262611342e5a9e
fetched_at: '2026-06-29T00:09:33.454697+00:00'
page_id: '425459032'
product: rm
source: tdn-rm
title: Configura Webservice IIS 7
type: documentation
url: https://tdn.totvs.com/display/LRM/Configura+Webservice+IIS+7
version: 2
---

Para configurar o Webservice em um servidor utilizando o IIS 7, devem ser realizados os seguintes passos:

1 - Compartilhar a pasta **Webservice,** localizada em **C:\totvs\CorporeRM\RMTestis**, com os usuários que irão acessar o servidor para executar as provas.

2 - Acesse o **IIS (Gerenciador do Serviços de Informações da Internet)** do **Windows** através do caminho **Iniciar > Todos os programas > Ferramentas administrativas > Gerenciador do Serviços de Informações da Internet**.

3 - Crie um novo diretório virtual. Para isso:

      a - Abra **Computador local**.  
    
       b - Abra pasta **Sites da Web**.  
    
       c - Selecione o **Site da Web Padrão** (ou **Default Web Site**), clicar com o botão direito do mouse, escolher a opção **Adicionar aplicativo**.  
    
       d - Digite na caixa de texto **Alias** o nome do serviço (Exemplo **Webservice)** e selecione o caminho físico **C:\totvs\CorporeRM\RMTestis\Webservice**.  
    
       e - Abra a opção "Pesquisa no diretório" e clique na opção "Habilitar"   
    
       f - Clique em **OK** para confirmar as alterações e feche o **IIS**.  
    
 4 - Para verificar se o servidor foi configurado corretamente, abra o browser (por exemplo, **Internet Explorer**) e digite o endereço onde se encontra o arquivo **TstExecWebService.asmx**.

**Exemplo**

[{+}](http://localhost/Webservice/TstExecWebService.asmx)<http://localhost/Webservice/TstExecWebService.asmx+>, onde **localhost** é o nome do servidor e **Webservice** é o nome da pasta do Webservice.
