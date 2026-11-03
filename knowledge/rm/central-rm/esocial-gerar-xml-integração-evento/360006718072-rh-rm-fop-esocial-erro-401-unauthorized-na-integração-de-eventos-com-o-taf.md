---
article_id: 360006718072
category: eSocial - Gerar XML/ Integração Evento
content_hash: b3b19078bc32189e8ff9d8693a2448ceb3b996ccb90761305ec931c6b36571bb
fetched_at: '2026-06-28T22:47:12.079606+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Erro (401) Unauthorized na integração de eventos
  com o TAF
type: support-article
updated_at: '2024-06-28T18:44:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006718072-RH-RM-FOP-eSocial-Erro-401-Unauthorized-na-integra%C3%A7%C3%A3o-de-eventos-com-o-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24510798363799) Tempo aproximado para leitura: 00:02:00 min  
  
Ocorrência**Ao tentar integrar os eventos do eSocial com o TAF é apresentada a mensagem de erro **Ocorreu erro que impediu a execução do processo. System.Exception: System.Net.WebException: The remote server returned an error: (401) Unauthorized**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042130613)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir da release 12.1.22  
  
**Causa**Este incidente ocorre quando há alguma divergência relacionada ao usuário ou senha informados no parametrizador do RM para integração com TAF. O TAF possui uma senha ou um usuário específico, porém no RM falta o preenchimento destas informações ou estão incorretas.  
  
**Solução**Para resolver esta ocorrência, acesse **Configurações | Parametrizador | 06.07 - eSocial | Integração com TAF** e verifique os campos **Usuário** e **Senha** estão preenchidos corretamente de acordo com o usuário e senha do TAF.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24510798367383)

**Importante**Para clientes Smart, é necessário a abertura de um ticket com a Equipe Smart eSocial.
