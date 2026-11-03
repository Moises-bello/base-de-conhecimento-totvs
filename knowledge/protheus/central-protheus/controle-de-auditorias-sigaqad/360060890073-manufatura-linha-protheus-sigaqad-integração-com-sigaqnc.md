---
article_id: 360060890073
category: Controle de Auditorias (SIGAQAD)
content_hash: e335cdcbb5df9bc2e7e0c964f4372a0be37c5eb13fb96df5489b1b39c727ca50
fetched_at: '2026-06-28T22:42:30.858350+00:00'
product: protheus
section_id: 360005876634
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQAD - Integração com SIGAQNC
type: support-article
updated_at: '2021-08-16T12:09:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060890073-Manufatura-Linha-Protheus-SIGAQAD-Integra%C3%A7%C3%A3o-com-SIGAQNC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:37 min**  
**Dúvida**Como realizar a integração do módulo **SIGAQAD - Controle de Auditorias** com o módulo **SIGAQNC - Controle de Não Conformidades**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Auditorias (SIGAQAD) - Todas as versões  
  
**Solução**Para realizar a integração do módulo **SIGAQAD** com o módulo **SIGAQNC** ative o parâmetro **MV\_QADQNC - Indica se as não conformidades na questão serão geradas no QNC.**   
Este parâmetro quando ativado, ou seja, quando houver integração com o **SIGAQNC**, deixará os campos **QUG\_CODNC - Código da NC** e **QUG\_REVNC - Revisão NC** da tela de **Resultados de Auditorias** apenas como visualização, caso contrário os mesmos ficam alteráveis, permitindo que o usuário informe alguma auditoria já cadastrada.  
Se o parâmetro for desativado no meio do processo, será gerada uma **Não Conformidade** e subscrito o valor informado pelo usuário.
