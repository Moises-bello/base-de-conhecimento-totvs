---
article_id: 31410288426519
category: Financeiro - Viagens
content_hash: c7851416994a0f6a5a8394e50e5d0355ba6dff12dc176a4b56f89cd62799a0c0
fetched_at: '2026-06-28T22:38:21.470042+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - HELP: RD0_FVIAJ'
type: support-article
updated_at: '2025-04-15T10:06:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31410288426519-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-HELP-RD0-FVIAJ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31410284511127) Tempo aproximado para leitura: **00****:03:00 min****Ocorrência**Na rotina de cadastro de participantes APDA020, ao salvar cadastro sem preencher o campo RD0\_FVIAJ, ocorre o HELP a seguir.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31410284514583)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
  
**Causa**O cadastro de participantes é o cadastro primário, que visa identificar os colaboradores da empresa nas rotinas de Viagens do módulo Financeiro. Dado este fato, os **apps Minha Prestação de Contas e Meu Protheus** também consideram esse cadastro para seguir o mesmo padrão de comportamento do módulo, já que a regra de negócio é a mesma e o app é somente uma interface móvel para o processo de prestação de contas.  
Para que o processo de **Viagens / Prestação de contas** funcione da forma adequada, a amarração entre o usuário Protheus e o cadastro do participante, deve ser de um para um.  
  
E no caso, não estava acontecendo isso, o sistema estava permitindo ter mais de um **código SIGA** amarrado em **participantes** ativos diferentes.  
  
Para a correção deste cenário, foi necessário ajustes em programas fontes e a criação de um dicionário **campo RD0\_FVIAJ.**

Abaixo segue link da documentação da correção e informações do campo:  
[APDA020 - Codigo de usuario Siga sendo incluso em mais de um participante ativo causando problemas no App MPC](https://tdn.totvs.com/display/public/PROT/18148281+DSFIN-5772+DT+P12.1.2210+-+APDA020+-+Codigo+de+usuario+Siga+sendo+incluso+em+mais+de+um+participante+ativo+causando+problemas+no+App+MPC)  
  
Por conta disso, se faz atualmente obrigatório o preenchimento deste campo, seja **"SIM" ou "NAO".**
