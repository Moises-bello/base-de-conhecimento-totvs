---
article_id: 360028698112
category: GPE - eSocial - Carga Inicial
content_hash: 9c059cf70be6f88b5a00d3be38b3eb9a439b953bfabda878c4cbabe1694d35dd
fetched_at: '2026-06-28T22:45:03.273889+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1010 - Inconsistência do RET 110 -
  O numero de processo judicial informado nao foi localizado no cadastro do empregador
  no periodo
type: support-article
updated_at: '2025-07-28T18:49:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028698112-RH-Linha-Protheus-GPE-eSocial-S-1010-Inconsist%C3%AAncia-do-RET-110-O-numero-de-processo-judicial-informado-nao-foi-localizado-no-cadastro-do-empregador-no-periodo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33773181549975) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**O numero de processo judicial informado não foi localizado no cadastro do empregador no período.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**A inconsistência ocorre por que o evento de rubrica (S-1010) que está tentando encaminhar com a informação do Processo (S-1070) está com data anterior ao inicio de validade informado no evento S-1070.  
  
Por exemplo, enviei um evento S-1070 em 05/2019 e ele foi aceito pelo RET (Governo), porém tento retificar uma Rubrica (S-1010) com inicio de validade em 01/2019 vinculando ao processo enviado pelo evento S-1070, ao enviar para o RET (Governo) haverá a inconsistência 110.  
  
**Solução**Acesse o cadastro de Processos Administrativo/Judicial e envie um evento S-1070 com data de inicio igual ou anterior aos períodos afetados por ele.  
![](https://totvssuporte.zendesk.com/attachments/token/t4ApGQfcSvBvAEca0h2sTtcet/?name=inline1584543302.png)​  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
  
  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
