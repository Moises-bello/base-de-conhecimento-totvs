---
article_id: 360035627653
category: GPE - eSocial - Não Periódicos
content_hash: f07445cd6252ef51044637d1750a145a40e96e796dcc71ae28813b840e34607f
fetched_at: '2026-06-28T22:45:05.729557+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2230 - Como realizar o envio de férias
  programadas para o TAF
type: support-article
updated_at: '2026-06-16T13:35:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035627653-RH-Linha-Protheus-GPE-eSocial-S-2230-Como-realizar-o-envio-de-f%C3%A9rias-programadas-para-o-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41262160126871) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como realizar o envio de **férias programas** para o **TAF**?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
Criação do parâmetro **MV\_INTFEPR** para indicar se o evento**S-2230** deve ser integrado ao TAF **no momento do cálculo da programação de férias**, ou se deve ser enviada via job (schedule).

| Nome | MV\_INTFEPR |
| --- | --- |
| Tipo | Lógico |
| Conteúdo | .F. |
| Descrição | Indica se deve ser integrado ao TAF o evento S-2230 ao calcular férias programadas. |

Este parâmetro será criado com conteúdo padrão = Falso (.F.). Caso opte por enviar o evento ao calcular a programação de férias, altere seu conteúdo para **verdadeiro (.T.)**.  
  
**Observação:** Mesmo com parâmetro habilitado, caso a data de início ultrapasse 60 dias do envio do evento S-2230, o mesmo será enviado via job na **data de início das férias**.  
Após a configuração do parâmetro, para ocorrer o envio correto das informações é necessário estar com o último acumulado do eSocial no link [eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
  
Para mais informações sobre a configuração do job, acesse: [eSocial | Protheus - Entregas Legais - Schedule GPE](http://tdn.totvs.com/x/dQdFFw).   
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[MV\_INTFEPR para envio de evento S-2230 de férias programadas](https://tdn.totvs.com/pages/viewpage.action?pageId=513433334)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "****Eventos****".*
