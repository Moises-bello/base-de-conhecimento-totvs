---
article_id: 30760627788183
category: Financeiro - Conciliador Backoffice
content_hash: 8bb308ce9f328ee87619f51115af44f049770fd4b07b7f889339c00d1c4346b9
fetched_at: '2026-06-28T22:37:47.147428+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 -  Não consta
  o título no conciliador. O que validar?
type: support-article
updated_at: '2026-03-31T13:04:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30760627788183-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-N%C3%A3o-consta-o-t%C3%ADtulo-no-conciliador-O-que-validar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30760620077975) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
O que validar quando não consta o título no novo conciliador?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.2210.  
  
**Solução**  
Para solucionar essa dúvida, realizar as validações a seguir:

* Verificar se a tabela FK5 gerou o novo campo **MSUIDT**. Caso não tenha sido gerado, executar o **Wizard do Conciliador** para sua criação.
* Certificar-se de que a data de disponibilização está preenchida na tabela **FK5**.
* Caso a FK5 não tenha sido gerada, proceder com a validação da próxima etapa.
* Analisar o conteúdo do campo **E5\_TIPODOC** na tabela **SE5**. Para que o movimento seja registrado no **Conciliador**, o tipo de movimento deve resultar em movimentação bancária. Caso contrário, o registro não será encaminhado ao **Conciliador**.

**Tipos de movimentos.**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Descrições dos tipos de movimentações do campo E5\_TIPODOC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022538171-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Descri%C3%A7%C3%B5es-dos-tipos-de-movimenta%C3%A7%C3%B5es-do-campo-E5-TIPODOC)

**Saiba mais**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Conciliador Backoffice Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23945644752279/live_preview/01JPQ8Y3806VR0MYFWX2MAB7YX)
