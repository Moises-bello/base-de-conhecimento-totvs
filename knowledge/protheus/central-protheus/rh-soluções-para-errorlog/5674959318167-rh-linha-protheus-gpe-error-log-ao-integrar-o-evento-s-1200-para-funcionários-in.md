---
article_id: 5674959318167
category: RH - Soluções para error.log
content_hash: 0ea87baa1d5c7013c3d4df299a4268bd0bd3d04e049e1bedf6d54356b308f89b
fetched_at: '2026-06-28T22:44:09.087222+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Error log ao integrar o evento S-1200 para funcionários
  intermitentes - invalid field name in Alias SCGNXXXXXX->RD_SEMANA on CORPOXML(GPEM036A.PRW)
type: support-article
updated_at: '2022-04-26T11:04:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5674959318167-RH-Linha-Protheus-GPE-Error-log-ao-integrar-o-evento-S-1200-para-funcion%C3%A1rios-intermitentes-invalid-field-name-in-Alias-SCGNXXXXXX-RD-SEMANA-on-CORPOXML-GPEM036A-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao tentar integrar o **evento S-1200,** através da rotina **GPEM034** para **funcionários intermitentes**gera *error log: **"******invalid field name in Alias* SCGNXXXXXX->RD\_SEMANA *on* CORPOXML(GPEM036A.PRW)"**  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O erro ocorre em ambientes com o fonte **GPEM036A** com data anterior a **20/04/2022**  
**Solução**Para solução do erro, será necessário efetuar aplicação do pacote abaixo:  
12.1.27: <https://suporte.totvs.com/portal/p/10098/download?e=1066135> ;  
12.1.33: <https://suporte.totvs.com/portal/p/10098/download?e=1066136> ;  
  
**Obs.:**Devido ao Ciclo de Vida de Software TOTVS estipulado e a data da expedição desta correção **(22/04/2022)**, esta correção **não** **estará disponível para a versão 12.1.25**:  
<https://tdn.totvs.com/display/public/PROT/Ciclo+de+Vida+de+Software+-+TOTVS+Linha+Protheus>   
  
**Informações complementares**  
Informações Técnicas sobre a correção: <https://tdn.totvs.com/pages/releaseview.action?pageId=682060923>  
Pacote de Expedição Contínua do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>   
Pacote de Expedição Contínua do eSocial: [https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-acumulado-do-eSocial)  
Pacote de Expedição Contínua do Medicina e Segurança do Trabalho:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773>  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
