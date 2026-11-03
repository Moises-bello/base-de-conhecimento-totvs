---
content_hash: 41dd6f5d4594b803b833178f5192d221bf89840d5345a31fcbff5e910e82982e
fetched_at: '2026-06-29T00:08:48.843158+00:00'
page_id: '329024425'
product: rm
source: tdn-rm
title: NFE0035_NF-e_Conexão_com_TSS_Encerrada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=329024425
version: 7
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 12.1.17 |
| **Ocorrência:** | Ao executar um processo de NF-e ocorre o erro  The underlying connection was closed: A connection that was expected to be kept alive was closed by the server. |
| **Passo a passo:** | **Introdução:**  Este documento irá detalhar a solução do problema de conexão entre RM e TSS através da instalação do Aplicativo ProxyMon.  O procedimento a seguir aplica-se a casos em que o problema ocorre de forma esporádica ou constante. A solução descrita neste documento pode não ser efetiva em determinados ambientes, pois existem várias causas para o problema como: Anti vírus, firewall, concorrência em portas (TCP/HTTP, SSL) etc. Caso a solução não seja efetiva entre em contato com nosso suporte.  **Procedimentos**   1. Faça o Download do Aplicativo ProxyMon através do Link: <https://www.dropbox.com/s/zfs22msbho3ocf2/ProxyMon.zip?dl=0> 2. Na maquina onde o TSS estiver instalado, crie uma pasta no C:\ com o nome "ProxyMon". Ficará "C:\ProxyMon". 3. Edite o arquivo "C:\ProxyMon\nginx\conf\nginx.conf" através do notepad do windows. Crie um alias para a conexão com o TSS conforme abaixo.     1. Na seção "Server", configuração "l**isten**" coloque uma porta HTTP para conexão entre o RM e o ProxyMon (Deverá ser diferente da porta utilizada pelo TSS)    2. Na seção "Server", configuração "**proxy\_pass**" coloque o endereço de comunicação com o TSS (é o endereço que informamos nos parâmetros da filial para comunicação com o TSS) 4. Executar o seguinte comando no prompt do windows (**Como administrador**): sc [\\localhost](file:///\\localhost) create ProxyMon binPath= "C:\ProxyMon\proxyMon.exe" displayname= "ProxyMon" 5. Abra o gerenciador de serviços e inicar o serviço ProxyMon 6. Alterar a configuração do RM para utilizar o TSS através da nova porta informada na configuração do proxy reverso ( se fosse com base na ilustração acima, onde o endereço original é [http://bhd000002100:8080](http://bhd050101849:8080), o correto seria atualizar para [http://bhd000002100:8081](http://bhd050101849:8081) |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
