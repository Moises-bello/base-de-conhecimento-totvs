---
content_hash: cb7c3954e2bf774ef597c0a67d0124b071fa38dcb501ba4820c4fc53bd87fd26
fetched_at: '2026-06-29T00:09:32.690587+00:00'
page_id: '425458901'
product: rm
source: tdn-rm
title: Configurar Webservice
type: documentation
url: https://tdn.totvs.com/display/LRM/Configurar+Webservice
version: 6
---

O modo WebService é uma das formas de se executar uma prova, através do Executor de Avaliações e Pesquisa.

Este modo permite ao usuário executar uma prova disponibilizada através de um serviço web, podendo estar localizado no computador local ou algum outro remoto.  
   
Para que seja realizado a configuração do ambiente Webservice instale a versão mais atual do TOTVS Avaliação e Pesquisa, para que você tenha acesso à pasta do WebService.  
   
**Configurações IIS**   
O primeiro passo para criar o ambiente WebService é configurar o serviço **IIS** (Internet Information Services), a versão do IIS vária de acordo com o sistema operacional:  
- Para o sistema operacional Windows XP a versão compatível do IIS é a 6.

- Para o sistemas operacionais Windows Vista, 7 e Server 2008 a versão compatível é a 7.

   
**Configurações do arquivo Web.config**   
Após realizadas as configurações anteriores, é preciso configurar o arquivo **Web.config**, localizado na pasta **C:\totvs\CorporeRM\RMTestis\ Webservice**.  
Edite o arquivo Web.config e retire todas as tags  que estão em "appSettings" exceto a tag <add key="Alias" value="CorporeRM" /> e substitua pelas que estão em "appSettings"  dos arquivos RM.Host.exe.config/ RM.Host.Service.exe.config localizados na pasta C:\totvs\CorporeRM\RM.Net.

Ex:  
...  
<appSettings>  
<!-Configurações de Remoting→  
**<add key="Alias" value="CorporeRM" />**

<add key="Port" value="8050" />

<add key="Host" value="localhost" />

<add key="JobServer3Camadas" value="false" />

</appSettings>  
…  
**Importante**  
   
Na tag <add key="Alias" value="CorporeRM" /> o valor de "value" deverá ser substituído pelo valor da tag "Alias" do arquivo Alias.dat localizado em C:\totvs\CorporeRM\WebService.  
No exemplo abaixo do arquivo Alias.dat "CorporeRm Exemplo" é o valor a ser utilizado na tag "Alias do arquivo Web.config.  
   
<DbConfig>     <Alias>CorporermExemplo</Alias>  
...  
</DbConfig>  
   
Depois das alterações realizadas o conteúdo do Web.config ficará da seguinte forma:  
…  
<appSettings>  
<!-Configurações de Remoting->           
  
 <add key="Alias" value="CorporeRmExemplo" />

<add key="Port" value="8050" />

<add key="Host" value="localhost" />

<add key="JobServer3Camadas" value="false" />

</appSettings>  
...  
   
**Observação importante:** Os arquivos **Web.config** do WebService e **RM.Host.exe.config/** **RM.Host.Service.exe.config** devem possuir as mesmas tags de configuração.  
   
**Configurações a serem efetuadas na(s) Máquinas em que será(ão) realizada(s) a(s) prova(s) (MÁQUINA CLIENTE):**  
**Passo 1:**  
Caso ainda não esteja instalado, instalar a última versão do RM Executor.  
**Passo 2:**  
Abra o RM Executor e informe a inscrição do candidato gerado pelo TOTVS Avaliação e pesquisa. Selecione o tipo de acesso: WebService (online).  
Neste momento será aberta uma janela para que seja informado o endereço do WebService definido na etapa de configuração do IIS: [{+}](http://localhost/Webservice/TstExecWebService.asmx)<http://localhost/Webservice/TstExecWebService.asmx+>, e clique em OK para fechar a janela.  
**Passo 3:**  
Clique no botão "OK" e depois no botão "Iniciar" para dar início a prova. Siga os passos normais para executar a prova.

**Erros conhecidos**

1.     Erro 500.0: Este erro ocorreu em um servidor com sistema operacional de 64bits com IIS versão 7 ou superior. Será necessário modificar o pool de aplicativos para habilitá-lo a rodar aplicações 32bits. Acesse o IIS, remova o diretório virtual e configure o mesmo novamente de acordo com as orientações do passo 4.

 Veja também

---

[Configuração WebService 12.1.1](http://tdn.totvs.com/pages/releaseview.action?pageId=210055215)
