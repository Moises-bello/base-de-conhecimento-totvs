---
content_hash: ed90a26c7de199ca930a3c42619da807607692f5e56662d65658e150bc0d3921
fetched_at: '2026-06-29T00:09:38.042139+00:00'
page_id: '425459688'
product: rm
source: tdn-rm
title: Configurar Webservice II6
type: documentation
url: https://tdn.totvs.com/display/LRM/Configurar+Webservice+II6
version: 4
---

Para configurar o Webservice em um servidor utilizando o IIS 6, devem ser realizados os seguintes passos:

1 - Compartilhar a pasta **Webservice**, localizada em **C:\totvs\CorporeRM\RMTestis**, com os usuários que irão acessar o servidor para executar as provas.

2 - Acesse o **IIS** (**Internet Information Services**) do **Windows** através do caminho **Iniciar > Todos os programas > Ferramentas administrativas > Internet Information Services**.

3 - Crie um novo diretório virtual. Para isso:

      a - Abra **Computador local**.  
    
       b - Abra a pasta **Sites da Web**.  
    
       c - Selecione o **Site da Web Padrão**, clicar com o botão direito do mouse, escolher a opção **Novo > Diretório Virtual** e clicar no botão **Avançar**.  
    
       d - Digite na caixa de texto **Alias** o seguinte: **Webservice** e clique em **Avançar**.  
    
       e - Para preencher a caixa de texto **Diretório**, clicar no botão **Procurar** e abrir a pasta **C:\totvs\CorporeRM\RMTestis\Webservice**. Clicar em **Avançar**.  
    
       f - Na etapa de **Permissão de Acesso**, marcar as opções de **Leitura**, **Execução de Scripts** e **Execução de Aplicativos** e depois clicar em **Avançar**.  
    
       g - Clique em **Concluir** e feche o **IIS**.

4 - Para verificar se o servidor foi configurado corretamente, abra o navegador (por exemplo, **Internet Explorer**) e digite o endereço onde se encontra o arquivo **TstExecWebService.asmx**.

Exemplo

[{+}](http://localhost/Webservice/TstExecWebService.asmx)<http://localhost/Webservice/TstExecWebService.asmx+>, onde **localhost** é o nome do servidor e **Webservice** é o nome da pasta do Webservice.
