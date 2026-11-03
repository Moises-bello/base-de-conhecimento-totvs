---
article_id: 32635437145239
category: SIGAEST - CUSTOS
content_hash: 6a24d02768c0888d136ffcea489aa264de00b0f56fcef7f2b05de2790bedf971
fetched_at: '2026-06-28T22:39:02.036930+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 Acompanha
  Custos chave LOGPROFILER e CONSOLEMAXSIZE
type: support-article
updated_at: '2025-06-06T14:59:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32635437145239-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Acompanha-Custos-chave-LOGPROFILER-e-CONSOLEMAXSIZE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32635399916567) Tempo aproximado para leitura: **00:02:30 min**

**Dúvida**

Ao acessar a rotina ACOMPNHA CUSTOS (MATA038) apresenta o alerta **Chave LOGPROFILER e CONSOLEMAXSIZE** e não avança para o processo de Fechamento, como devo ajustar?

![acompanha custos consolemaxsize.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32636577250839)  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Solução**

Para não exibir esse alerta, ajustar no **arquivo APPSERVER.INI** na **Seção GENERAL** a chave **ConsoleMaxSize=104857600** e **Consolelog=1** e na seção **ENVIROMENT** a chave **Logprofiler=1,** abaixo um exemplo de configuração e também link da Documentação dessas chaves:

|  |
| --- |
| [Environment] ... **LogProfiler=1**   [General] ... **Consolelog=1** **Consolemaxsize=104857600** |

CONSOLEMAXSIZE:  
**<https://tdn.totvs.com/x/Ropc>**

LOGPROFILER:  
[**https://tdn.totvs.com/x/J1IXEQ**](https://tdn.totvs.com/x/J1IXEQ)

**Observações:** O alerta também pode ser apresentado se o tamanho da chave CONSOLEMAXSIZE estiver **diferente de 104857600**

![CONSOLEMASXSIE.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/32637594807063)

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre CUSTOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[SIGAEST - MATA038 - "Ocorrências" X "Soluções" no Acompanha Custos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12093061866135-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Ocorr%C3%AAncias-X-Solu%C3%A7%C3%B5es-no-Acompanha-Custos)

[Webinar MP - SIGAEST- Nova Jornada de Fechamento (MATA038) TOTVS Backoffice -Linha Protheus](https://youtu.be/UnhQvuoT5UE?si=XVpuU-FZwKjd8xYX)
