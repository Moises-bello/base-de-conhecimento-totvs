---
article_id: 4403610689559
category: RH - Períodos de Apontamento
content_hash: 4f892c1caf77bf28181575af4022cd9cc2ea02c5eb75d7950538131df5e11b6b
fetched_at: '2026-06-28T22:44:45.103236+00:00'
product: protheus
section_id: 32419304439959
source: central-protheus
title: RH - Linha Protheus - PON - Como consultar marcações de um período em aberto
type: support-article
updated_at: '2025-10-13T17:57:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403610689559-RH-Linha-Protheus-PON-Como-consultar-marca%C3%A7%C3%B5es-de-um-per%C3%ADodo-em-aberto
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35601442278807) Tempo aproximado para leitura: 00:02:00 min**Dúvida**Como verificar as marcações de um período que consta ainda em aberto?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**É importante primeiramente ressaltar que o ponto eletrônico (SIGAPON) **valida a data base do sistema** junto com os parâmetros **MV\_PAPONTA** e **MV\_PONMNES** para o **reconhecimento** e **montagem do calendário** de período aberto. Exemplo, para períodos retroativos em aberto:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31453597211543)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31453600605079)  
  
Após processar a rotina de **Leitura/Apontamento (PONM010)** para que as marcações do arquivo TXT em caso de relógios físicos ou através de integrações de outros sistemas para que sejam lidas e gravadas nas tabelas responsáveis marcações (SP8), apontamentos (SPC), pré leitura (RFE) e cabeçalho da pré leitura (RFB). O usuário tem duas rotinas onde pode fazer a **consulta** e **manutenção** desses dados, que são:  
**1 - Integrados (PONA280)**: a rotina pode ser localizada em **Atualizações > Lançamentos > Integrados.**  
Nesta rotina, nós temos a visualização completa do período de apontamento, porém, as marcações/apontamentos são vistos de forma individual clicando sobre cada dia. Além disso, nessa rotina é possível fazer uma **troca de evento** através do campo **Código Inf**. ou **lançar** um **Abono de Horas** através do campo **Mot. Abono**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31453600605847)  
  
**2 - Marcações (PONA040)**: a rotina pode ser localizada em **Atualizações - Lançamentos - Marcações**.  
Nesta rotina, nós temos a visualização **geral** do **período de apontamento**. Para verificar os **apontamentos**, é necessário clicar em **Outras Ações - Reaponta ou F9**, será aberta uma **caixa** com os **apontamentos** de cada dia:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31453600606999)

**Saiba Mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[Funcionalidade da tabela RFB e como controlar a leitura para que o NSR não ocasione erros no processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016068372)  
[Como funciona a Leitura e Apontamento das marcações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004052211-RH-Linha-Protheus-PON-Como-funciona-a-Leitura-e-Apontamento-das-marca%C3%A7%C3%B5es)
