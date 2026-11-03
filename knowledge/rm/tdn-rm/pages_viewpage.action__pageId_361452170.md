---
content_hash: 12933ca2ff05224a34c446fdce9946dfd307a480b7348545c7be0430bca25812
fetched_at: '2026-06-29T00:08:58.905345+00:00'
page_id: '361452170'
product: rm
source: tdn-rm
title: 'RM - Erro: "Ocorreu erro que impediu a execução do processo. System.Net.WebException:
  Impossível conectar-se ao servidor remoto ---> System.Net.Sockets.SocketException..."'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=361452170
version: 3
---

Erros e AçõesErro

Erro: Ocorreu erro que impediu a execução do processo. System.Net.WebException: Impossível conectar-se ao servidor remoto ---> System.Net.Sockets.SocketException: Nenhuma conexão pôde ser feita porque a máquina de destino as recusou ativamente 127.0.0.1:9090

em System.Net.Sockets.Socket.DoConnect(EndPoint endPointSnapshot, SocketAddress socketAddress)  
 em System.Net.ServicePoint.ConnectSocketInternal(Boolean connectFailure, Socket s4, Socket s6, Socket& socket, IPAddress& address, ConnectSocketState state, IAsyncResult asyncResult, Exception& exception)  
 --- Fim do rastreamento de pilha de exceções internas ---  
 em System.Net.HttpWebRequest.GetRequestStream(TransportContext& context)  
 em System.Net.HttpWebRequest.GetRequestStream()  
 em RM.Fop.Esocial.JSONHelper.Post(String url, String user, String password, String jsonContent)  
 em RM.Fop.Esocial.FopEsocialIntegrarTafMod.Enviar(Int16 codColigada, String codUsuario, List`1 eventosList, RMSExecProgress progress, RMSServerLog log, Int32& numErros, Int32& totalIntegracaoTaf, String ticketCode, DateTime dataIntegracao)

Ação

Ação:

* Verifique se o serviço TAF - Ws está iniciado no servidor de instalação do TAF:

* Teste a URL de conexão com Web Service em seu navegador de internet, verifique se ela conecta e apresenta as informações:

* Verifique se a URL informada nos parâmetros de integração do RM está correta:

OBS: Lembrando que no parametrizador deve ser informada a URL testada no navegador + a api referente ao TAF (WSTAFST2):

Exemplo: <http://localhost:9090/rest/wstafst2>
