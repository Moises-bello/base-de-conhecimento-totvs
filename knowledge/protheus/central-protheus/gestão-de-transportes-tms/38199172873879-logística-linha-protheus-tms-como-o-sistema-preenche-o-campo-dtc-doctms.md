---
article_id: 38199172873879
category: Gestão de Transportes (TMS)
content_hash: 0846558a0bda9904bfe9a74ecb5c41784f7af8efe28abdb23d63cf84425744f5
fetched_at: '2026-06-28T22:45:27.477873+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Como o Sistema preenche o campo DTC_DOCTMS
type: support-article
updated_at: '2026-02-06T15:04:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38199172873879-Log%C3%ADstica-Linha-Protheus-TMS-Como-o-Sistema-preenche-o-campo-DTC-DOCTMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38199172860055) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como o Sistema preenche o campo **DTC\_DOCTMS - Documento de Transporte** na  inclusão de documentos na rotina **Entrada de Documentos - TMSA050**?   
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Solução**  
No cadastro do serviço de negociação é especificado o tipo de documento de transporte no campo **DC5\_DOCTMS - Documento de Transporte.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38199172860567)

Ao incluir um novo documento na rotina **Entrada de Documentos - TMSA050**, ao preencher os dados da operação e definir o devedor do frete, o Sistema seleciona o contrato do cliente e permite selecionar a negociação e o serviço. Ao selecionar o serviço no campo **DTC\_SERVIC - Serviço**, o Sistema preenche o campo **DTC\_DOCTMS** conforme o serviço de negociação selecionado para o documento.  
  
Importante ressaltar que a lista de serviços pode variar conforme as regiões de origem e cálculo do documento:

* Se a região de origem e cálculo são diferentes, o Sistema entende que não trata-se de uma operação intramunicipal e exclui os serviços com o campo **DC5\_DOCTMS = 5 - Nota Fiscal.**

Exemplo:  
Meu contrato de cliente possui o serviço **ENT - Entrega** com o campo **DC5\_DOCTMS = 2** e o serviço **NFS - Nota Fiscal de Serviço** com o campo **DC5\_DOCTMS = 5**.  
Se a região de origem e região de cálculo são o município de **São Paulo - Q50308**, o Sistema listará ambos os serviços.  
Se a região de origem for **Joinville - O09102** e a região de cálculo **São Paulo - Q50308**, o Sistema irá listar somente o serviço **ENT - Entrega** com o campo **DC5\_DOCTMS = 2**, pois não se trata de uma operação intramunicipal.
