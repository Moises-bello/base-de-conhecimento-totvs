---
article_id: 360021788672
category: ADVPL - Classe e Função
content_hash: d4ff911ae01ce9f6adcb0cab631875af623db030aa17b850b35e72bbb452ea33
fetched_at: '2026-06-28T22:40:18.335599+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro de conexão
  DEV Studio em ambiente Cloud
type: support-article
updated_at: '2022-01-06T20:18:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021788672-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-de-conex%C3%A3o-DEV-Studio-em-ambiente-Cloud
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Ao tentar aplicar um Fonte .**PRW** no **DEV STUDIO**, está informando um erro de Conexão - Erro indeterminado.   
![err_dev.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360018739451/err_dev.png)  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Causa**   
Esse incidente ocorre, pois a ambiente em questão se encontra alocado na plataforma **INTERA** , o mesmo por segurança não permite acesso ao sistema via **TDS** ou **DEVStudio**.  
  
**Solução**Para solucionar essa ocorrência, o processo de atualização deve ser feito em ambiente de **desenvolvimento** e posteriormente replicado para a **produção**.  
Em caso de aplicação de patchs a mesma pode ser feita em produção através do **COCKPIT** no link [https://portal.cloudtotvs.com.br](https://portal.cloudtotvs.com.br/).

Obs.: O erro de conexão ocorre no ambiente Cloud somente na modalidade Intera, pois na modalidade padrão o erro de conexão não ocorre.
