---
content_hash: 5f1b8f190719f39de471eb4034e76f64e44529653beb0928b671bdd40087c635
fetched_at: '2026-06-29T00:11:20.661236+00:00'
page_id: '687165792'
product: rm
source: tdn-rm
title: PDC (Portal do Cliente) - Subindo o Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/PDC+%28Portal+do+Cliente%29+-+Subindo+o+Portal
version: 10
---

Este documento tem como objetivo demonstrar como montar o ambiente de debug para o PDC e como montar o ambiente como o cliente.

* **Para Debugar**  
    
  1 - Dar o get nos fontes em '$/RM/Atual/Release/FrameHTML/**web\_src**/app/Imb/PortalCliente' no TFS e clonar os fontes do git em totvstfs.visualstudio.com>>Construcao-e-Projetos>>portalcliente (indicado clonar para: "C:\RM\Atual\Release\FrameHTML\web\_src\app\Imb\PortalCliente")  
  2 - Rode o restore para o FrameHtml e para o Corpore.Net somente dlls pasta bin.  
  3 - Dê todas as permissões necessárias para o IIS em: Painel de Controle | Programas e Recursos | Ativar ou desativar recursos do windows >> Marque todos os checkbox da opção "Serviços de Informações da Internet".  
  4 - Abra o IIS >> No canto superior direito expanda o nome da maquina e verá uma pasta "Sites", botão direito sobre Sites, clique em 'Adicionar Site...', dê o nome que você desejar (Nome do site), no campo Caminho físico → escolha o caminho onde se encontra os arquivos que foram baixados para sua maquina, exemplo: "C:\RM\Legado\12.1.32\FrameHTML", no campo Porta, informe uma porta que será utilizada para encontrar o seu site no browser, exemplo: "8032" .  
  5 - Antes de acessar o portal no browser, vamos verificar as rotas. Abra no bloco de notas, Web.config (C:\RM\Legado\12.1.32\FrameHTML), RM.Host.exe (C:\RM\Legado\12.1.32\Bin) e totvs-app.global.config (C:\RM\Legado\12.1.32\FrameHTML\web\_src\js).  
  6 - Verifique se DefaultDB do Host está igual ao valor de ServiceAlias do Web.config  
  7 - Verifique se Port do Host está igual a Porta do Web.config  
  8 - Verifique se Host do Host.config está igual a Host do Web.config  
  9 - No arquivo totvs-app.global.config retire a parte do caminho dos folders que indica FrameHtml.   
  Exemplo de caminho errado: var CONST\_GLOBAL\_URL\_BASE\_APP = '/FrameHTML/web\_src/';  
  Exemplo de caminho correto: var CONST\_GLOBAL\_URL\_BASE\_APP = '/web\_src/';

* **Ambiente do cliente:**  
  Seguir todos os passos citados para debugar, mas a pasta utilizada agora será **web** e não **web\_src** como em destaque no primeiro passo.

Para acessar o portal no browser na maquina local, execute o host como administrador e você poderá utilizar o camiho como localhost e a porta que configurou para o site mais o restante do caminho que se deseja dentro da pasta FrameHtml:  
**Exemplo:** http://localhost:8032/web\_src/app/Imb/PortalCliente

[Padrão TCGI - SmartUI APIs/CRUD](https://tdn.totvs.com/pages/viewpage.action?pageId=808001405)

**Erros/Soluções:**

erro: O inicializador de tipo de 'System.Text.Encodings.Web.DefaultJavaScriptEncoder' acionou uma exceção.

response no console dev: "Message": "Não foi possível carregar arquivo ou assembly 'System.Runtime.CompilerServices.Unsafe, Version=4.0.4.1, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a' ou uma de suas dependências. A definição do manifesto do assembly localizado não corresponde à referência do assembly. (Exceção de HRESULT: 0x80131040)",

Solução: verificar qual o Pool de aplicativo está associado ao seu site, dê preferencia sempre ao pool criado no momento em que você criou o seu site.  
após a correção do Pool de aplicativo o portal volta a responder normalmente.

**Para configurar dois ou mais PDC no mesmo ambiente:**

1. abrir arquivo hosts da pasta "C:\Windows\System32\drivers\etc\";
2. Adiciona os seguintes subdomínios (retirar #):  
       127.0.0.1   [comum.sitecliente.com.br](http://comum.sitecliente.com.br)  
       127.0.0.1   [luxo.sitecliente.com.br](http://luxo.sitecliente.com.br)
3. No ISS, criar um Site para cada subdomínio configurado e em "Nome do host" colocar o respectivo subdomínio (Não precisa especificar um porta).
4. Configurar o MultiPortal seguindo a documentação [Configuração MultiPortal](https://tdn.totvs.com/pages/viewpage.action?pageId=941245873#Configs-external_config)
5. Após isso deve ser possível acessar cada PDC utilizando o subdomínio configurado, ex.: [http://comum.sitecliente.com.br/web/app/Imb/PortalCliente/#/](http://comum.sitecliente.com.br/web_src/app/Imb/PortalCliente/#/) e logar normalmente.
