---
content_hash: 98ec35700d0975a6202e9b901f2d8879782bcc213d0dad9da922b4d169f2b56b
fetched_at: '2026-06-29T00:08:04.073271+00:00'
page_id: '235335255'
product: rm
source: tdn-rm
title: Correção de falha ao logar no RM Portal - Erro 500 19 500 21
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235335255
version: 16
---

# Correção de falha ao logar no RM Portal - Erro 500-19

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 11.XX; 12.1.XX |
| **Ocorrência:** | Correção de falha ao logar no RM Portal - Erro 500-19 500-21 |
| **Ambiente:** | Portal WEB - Gestão de Conteúdos |
| **Passo a passo:** | Inicialmente, verifique o caminho físico, para Default Web Site - %SystemDrive%\inetpub\wwwroot    Verifique o caminho físico, para CorporeRM - %SystemDrive%\totvs\CorporeRM\Corpore.Net    Confirme se os componentes do Windows estão instalados corretamente:        Verificando o pool de aplicativos, favor seguir as setas abaixo (conforme o PRINT) e verificar se o pool de aplicativos está com a versão ASP.NET v4.0.  Caso não esteja, favor alterar para ASP.NET v4.0.    Para alterar o pool de aplicativos para a ASP.NET v4.0.  clique no ícone    referente a seta 3 (Print acima) irá abrir um Poq up para que seja feita a alteração, após indicar ASP.NET v4.0 clique em OK:    Caso realizou todo o procedimento acima e ainda está de deparando com o erro 500.19, então deverá ativar o IIS (Segue o procedimento abaixo):  **Para ativação do IIS:**  1 - Acesse a pasta:  Caso seja Windows 64Bits: C:\Windows\Microsoft.NET\Framework64\v4.0.30319  Caso seja Windows 32Bits: C:\Windows\Microsoft.NET\Framework\v4.0.30319  2 - Localize e execute o arquivo: **aspnet\_regiis.exe**    3 - Copie o caminho onde o arquivo está localizado:  Windows 64Bits C:\Windows\Microsoft.NET\Framework64\v4.0.30319  Windows 32Bits C:\Windows\Microsoft.NET\Framework\v4.0.30319  4 – Abra o promt de comando com usuário administrador  5 – Digite CD, pressione a tecla “Espaço” cole o caminho e pressione a tecla “Enter”  6 – Execute o comando:  Windows Server 2008, 2008R2 e 2012  **aspnet\_regiis.exe -i**  Windows Server 2012R2 e superiores:  **dism /online /enable-feature /featurename:IIS-ASPNET45 /all**      **Reinicie o IIS:**  Executar: CMD (Prompt de Comando DOS)  Digite o comando: IISRESET  Se o problema persistir, favor conceder as permissões na pasta C:\totvs (Permissão total – Leitura e Gravação):        **Agora, peço por gentileza, que abra o browser (Ex: Internet Explorer) e acesse o portal digitando o endereço:**  [**http://localhost/corpore.net/Login.aspx**](http://localhost/corpore.net/Login.aspx)     Erro 500.19 em ambiente com IIS customizado Ambientes com instalações customizadas podem apresentar o erro 500.19, conforme exemplo abaixo:   |  |  | | --- | --- | | Erro de Configuração | Não é possível adicionar a entrada de coleção duplicada do tipo 'add' com o atributo de chave exclusivo 'name' definido como 'X-Xss-Protection' |   Configuration Error Unable to add duplicate collection entry of type 'add' with unique key attribute 'name' set to 'X-Xss-Protection'    A inconsistência ocorre pois o ambiente utiliza customizações no Portal (IIS) diferentes de uma instalação padrão.  Em uma instalação padrão, o aplicativo Corpore.Net é criado no Default Web Site e não dentro do FrameHTML.    Durante a instalação do patch do RM Portal é apresentada a mensagem abaixo para Habilitar Segurança:   ​  Ao clicar em Sim, as tags são definidas com os seguintes valores:   * X-Frame-Options = SAMEORIGIN * X-Content-Type-Options = nosniff * X-Xss-Protection = 1; mode=block   Mais detalhes no link abaixo:    Vide item:**Portal Corpore.Net e Web API**  Essas tags estão disponíveis no arquivo Web.config.  No IIS, por ser customizado, ocorre o conflito dos valores da tag, para os arquivos Web.config (Corpore.Net e FrameHTML).  **Importante:** Não prestamos suporte a customizações do RM Portal, somente a instalação padrão. |
| **Observações:** | Esse erro está relacionado ao IIS e não ao aplicativo Totvs. Para mais informações consulte o link <https://docs.microsoft.com/pt-br/troubleshoot/iis/http-error-500-19-webpage> ou <https://docs.microsoft.com/en-us/dynamics-nav/troubleshooting-http-error-500.21-internal-server-error-aspnetcore-handler> |
