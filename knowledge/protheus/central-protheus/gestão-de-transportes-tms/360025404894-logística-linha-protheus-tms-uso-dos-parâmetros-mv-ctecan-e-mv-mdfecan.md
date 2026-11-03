---
article_id: 360025404894
category: Gestão de Transportes (TMS)
content_hash: c7f74535092ed6ebe5a549855196a9d8110897949ac0735871f6550d29b8fc10
fetched_at: '2026-06-28T22:45:33.436007+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Uso dos parâmetros MV_CTECAN e MV_MDFECAN
type: support-article
updated_at: '2024-06-03T19:48:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025404894-Log%C3%ADstica-Linha-Protheus-TMS-Uso-dos-par%C3%A2metros-MV-CTECAN-e-MV-MDFECAN
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23922754298775)**Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Como utilizar os parâmetros **MV\_CTECAN** e **MV\_MDFECAN**?  
  
**Ambiente**

TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Os parâmetros **MV\_CTECAN** e **MV\_MDFECAN**, são utilizados com o **TSS - TOTVS Service SOA** ou **TOTVS Colaboração 2.0.**Quando um destes parâmetros estiverem ativos, para realizar a exclusão de documentos será necessário obrigatoriamente o retorno de autorização da **SEFAZ - Secretaria da Fazenda** aplicados para os tipos de documentos **CT-e - Conhecimento de Transporte Eletrônico** ou **MDF**-**e -****Manifesto de Documento Fiscal Eletrônico.** Durante a tentativa de exclusão haverá um alerta que orientará o usuário a abrir o **monitor de transmissão do CT-e ou MDF-e** e aguardar a autorização da **SEFAZ.** O processo deve ser feito através do **botão monitor**, existente ambos os processos de transmissão **CT-e** ou **MDF-e**.

![image2018-11-9_17-10-53.png](http://tdn.totvs.com/download/attachments/435104360/image2018-11-9_17-10-53.png?version=1&modificationDate=1541790653737&api=v2)

**MV\_CTECAN** - Habilita validação da exclusão do **CT-e** autorizado pela **SEFAZ**.  
  
**MV\_MDFECAN** - Habilita a exclusão do manifesto somente após a autorização do cancelamento do **MDF-e** pela **SEFAZ**.  
  
Validação **CT-e**, alerta para transmissão de cancelamento:  
  
Quando já autorizado o **CT-e**:

![image2018-11-12_9-30-25.png](http://tdn.totvs.com/download/attachments/435104360/image2018-11-12_9-30-25.png?version=1&modificationDate=1542022225947&api=v2)

Quando ainda aguarda o retorno da **SEFAZ**:

![image2018-11-9_16-56-43.png](http://tdn.totvs.com/download/attachments/435104360/image2018-11-9_16-56-43.png?version=1&modificationDate=1541789803860&api=v2)

Nos casos onde o cancelamento de **CT-e** não for autorizado pela **SEFAZ**, sendo retornado rejeição por perda de prazo **220 - CT-e autorizado há mais de 168 horas - 7 dias** foi implementada melhoria para que o retorno do status do **CT-e** retorne para autorizado no **ERP - Enterprise Resource Planning.Enterprise resource planning.** Documentação sobre este processo está disponível no *link* : [Logística - Linha Protheus - TMS - Parametro MV\_RTCTEID - Retorno de Status de CT-e](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024696894-MP-TMS-Parametro-MV-RTCTEID-Retorno-de-Status-de-CT-e) Validação **MDF-e**, alerta para transmissão de **Cancelamento**:

[![image2018-11-9_17-1-44.png](http://tdn.totvs.com/download/attachments/435104360/image2018-11-9_17-1-44.png?version=1&modificationDate=1541790104507&api=v2)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024696894-MP-TMS-Parametro-MV-RTCTEID-Retorno-de-Status-de-CT-e)

A utilização destes parâmetros visa melhor controle das operações, evitando que o registro de documentos seja excluído equivocadamente do **ERP** sem aprovação do órgão validador **SEFAZ** - evitando assim a existência de status divergentes **ERP** x **SEFAZ**.  
  
**Saiba mais**Mais informações poderão ser acessadas nos *links*:   
[Logística - Linha Protheus - TMS - Principais parâmetros CT-e](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024942253-MP-SIGTATMS-Principais-par%C3%A2metros-CT-e)  
[Logística - Linha Protheus - TMS - Como realizar Cancelamento CT-e](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026160512-MP-TMS-Como-realizar-Cancelamento-CT-e)
