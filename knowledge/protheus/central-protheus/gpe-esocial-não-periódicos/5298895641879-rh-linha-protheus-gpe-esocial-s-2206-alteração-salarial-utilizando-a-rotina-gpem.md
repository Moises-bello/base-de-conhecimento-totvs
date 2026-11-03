---
article_id: 5298895641879
category: GPE - eSocial - Não Periódicos
content_hash: 038e461323e593387529ccd59afcc8f53ab5cdb8872909c75284eae163e00d67
fetched_at: '2026-06-28T22:45:04.669677+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2206 - Alteração salarial utilizando
  a rotina GPEM047 está gerando a tag dtAlteracao errada no evento
type: support-article
updated_at: '2026-06-16T11:52:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5298895641879-RH-Linha-Protheus-GPE-eSocial-S-2206-Altera%C3%A7%C3%A3o-salarial-utilizando-a-rotina-GPEM047-est%C3%A1-gerando-a-tag-dtAlteracao-errada-no-evento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25813891391767) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**Ao gerar uma alteração salarial através da rotina rotina GPEM047 (Geração Eventos S-2206/S-2306 Em Lote) o sistema está gerando a *tag* **dtalteracao** no xml do evento S-2206 com uma data errada.**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Ao utilizar a rotina GPEM047 (Geração Eventos S-2206/S-2306 Em Lote) o sistema está gerando a data de alteração incorreta no evento. Por definição de conceito, consideramos como **data de alteração**, a data de envio, pois este evento deve ser enviado logo que ocorre. Orientamos que o *JOB* **GPEM026B** seja agendado com recorrência diária para evitar inconsistências.   
[Como configurar o job schedule?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5220215589527)  
  
**Solução**Para evitar possíveis erros no cadastro do evento e transmissão ao governo, foi criado o parâmetro **MV\_DTALTSA,** onde será definido se o sistema deve considerar a data da alteração salarial ou a database para geração da informação no evento.  
[Documentação técnica MV\_DTALTSA](https://tdn.totvs.com/pages/releaseview.action?pageId=643755977)  
  
**Saiba mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes) 

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
