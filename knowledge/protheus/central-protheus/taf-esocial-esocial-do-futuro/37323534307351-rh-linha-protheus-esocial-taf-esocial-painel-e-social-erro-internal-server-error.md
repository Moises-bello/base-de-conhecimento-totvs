---
article_id: 37323534307351
category: TAF - eSocial - eSocial do Futuro
content_hash: e424024f99ee2b4c8d850b9e5a73c88c3a49f406f0acf323ccbfab1f8500d796
fetched_at: '2026-06-28T22:45:15.899826+00:00'
product: protheus
section_id: 1500001537001
source: central-protheus
title: RH (Linha Protheus) - eSocial - TAF eSocial - Painel E-social - Erro Internal
  Server Error ou Aguardando Retorno na transmissão de eventos variable does not exist
  CVERORI on GRAVAERR TAFPROC5.PRW variable does not exist CLOCALERR on GRAVAOCORR202(TAFPROC5
type: support-article
updated_at: '2026-06-26T11:41:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37323534307351-RH-Linha-Protheus-eSocial-TAF-eSocial-Painel-E-social-Erro-Internal-Server-Error-ou-Aguardando-Retorno-na-transmiss%C3%A3o-de-eventos-variable-does-not-exist-CVERORI-on-GRAVAERR-TAFPROC5-PRW-variable-does-not-exist-CLOCALERR-on-GRAVAOCORR202-TAFPROC5
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37323534291863) Tempo aproximado para leitura: 00**:01:10 min**  
  
**Ocorrência**  
Ao transmitir eventos no Painel eSocial gera o erro Internal Server Error 500 ou os eventos ficam como "Aguardando Retorno" e no console.log gera o erro "variable does not exist CVERORI on GRAVAERR(TAFPROC5.PRW) 06/11/2025 23:55:29 line : 1228"  
variable does not exist CLOCALERR on GRAVAOCORR202(TAFPROC5.PRW) 06/11/2025 23:55:29 line : 1342  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Painel E-social (TAFA552A)- Todas as versões  
  
**Causa**  
O erro ocorre após aplicar a expedição contínua do mês 12/2025

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37323534292631)  
  
**Solução**  
  
1. Caso esteja na versão 12/2025 com data 04/12/2025, aplique os pacotes abaixo conforme a sua release:

O pacote pode ser acessado no endereço: 12.1.2210:<https://r.totvs.io/p/1231227> ; 12.1.2310:<https://r.totvs.io/p/1231228> ; 12.1.2410:<https://r.totvs.io/p/1231226> ; 12.1.2510:<https://r.totvs.io/p/1231229> ;

**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Para conhecimento dos eventos futuros, acessa a nossa página [**TOTVS Informa**](https://informa.totvs.com/)selecione em categorias a área e pesquise por "**Eventos**"  
  
Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina:[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
