---
article_id: 9068056419223
category: eSocial - Gerar XML/ Integração Evento
content_hash: 4eebf5b315139b21f370828ca408a3c91cc139382da6056d996ed5d7038478c2
fetched_at: '2026-06-28T22:47:12.941997+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Erro Impossível conectar-se ao servidor remoto ao
  enviar eventos
type: support-article
updated_at: '2024-09-26T17:23:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9068056419223-RH-RM-FOP-eSocial-Erro-Imposs%C3%ADvel-conectar-se-ao-servidor-remoto-ao-enviar-eventos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23953968108951) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao transmitir eventos ao Governo ou na integração com o TAF é apresentada a mensagem **Ocorreu erro que impediu a execução do processo. RM.Lib.RMSApplicationException: Impossível conectar-se ao servidor remoto**

**emRM.Fop.Esocial.JSONHelperMiddleware.Post(String servidor, String porta, String usuario, String senha, String jsonContent, Boolean usarHttps, String token)**

**em RM.Fop.Esocial.FopEsocialIntegrarMiddlewareMod.Enviar(Int16 codColigada, String codUsuario, List`1 eventosList, IRMSExecProgress progress, IRMSServerLog log, String ticketCode, Int32& numErros, Int32& totalIntegrado, Boolean& possuiAvisos, Boolean& possuiEventosForaDoPrazo).****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Este incidente ocorre quando há uma falha de conexão entre o ERP e TAF/TSS que impossibilita a comunicação e transmissão dos eventos ao eSocial.   
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos para reinicialização do serviço conforme demonstrado no vídeo abaixo:

* Confira se os dados informados na Integração com o TAF estão corretos;  
  [Parametrizador eSocial: Integração com TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7380202283799-RH-RM-FOP-eSocial-Parametrizador-eSocial-Integra%C3%A7%C3%A3o-com-TAF?source=search)
* Caso esteja tudo correto, reinicie os serviços TAF e TSS;  
  [Erro de conexão - Reinicialização dos serviços TAF-TSS](https://www.youtube.com/watch?v=egIMkckF2ok)
* Caso o erro persista, será necessário contato com a Equipe TAF/TSS.
