---
article_id: 15082232520087
category: RH - Provisão
content_hash: 251bcead8e7012ab4ec60f98a4160728be2960afd15b4ed98eec3ac16115898e
fetched_at: '2026-06-28T22:43:56.038084+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Provisão de Férias com dias Férias Indevidas para
  funcionário afastado por Aposentadoria por Invalidez
type: support-article
updated_at: '2025-11-25T13:34:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15082232520087-RH-Linha-Protheus-GPE-Provis%C3%A3o-de-F%C3%A9rias-com-dias-F%C3%A9rias-Indevidas-para-funcion%C3%A1rio-afastado-por-Aposentadoria-por-Invalidez
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21822215754775) Tempo aproximado para leitura: **00:03:30 min**

**Ocorrência**  
Ao processar os cálculos de Provisão de Férias, o sistema apresenta dias de Férias indevidos para funcionários com Aposentadoria por Invalidez.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15081943637655)  
  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todos os Releases.  
  
**Causa**  
Este incidente pode ocorrer devido a criação indevida de **Períodos Aquisitivos** ou configuração do **Tipo de Ausência.**

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
**1.** Verifique se foi aplicado o Pacote de Expedição Contínua - Acumulado de RH:  
  
12.1.2310: <https://suporte.totvs.com/portal/p/10098/download?e=1123885>   
**IMPORTANTE!** Esta atualizacao bloqueia ambientes sem GARANTIA ESTENDIDA.

12.1.2410: <https://suporte.totvs.com/portal/p/10098/download#detail/1170810>   
12.1.2510: <https://suporte.totvs.com/portal/p/10098/download#detail/1221795>

**Observação**: é recomendado fazer uma cópia do RPO e aplicar o pacote inicialmente em ambiente **TESTE.**

**2.** Acesse Atualizações / Lançamentos / Ausências (GPEA240), e verifique o início do **Afastamento por Aposentadoria por Invalidez:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15073700969111)

**3.** Acesse: Atualizações / Definições de Cálculo / Tipos de Ausência (GPEA430), selecione o **Tipo de Ausência** lançado para o funcionário e clique em Visualizar. Confirme se os campos de **Férias** estão configurados como no exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15073796269463)

**4.** Acesse: Atualizações / Funcionários / Controle Dias de Direito (GPEA050), selecione o funcionário e clique em Visualizar, e verifique se há **períodos aquisitivos** criados indevidamente:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15074069646999)

Neste exemplo, veja que o primeiro período aquisitivo está **Ativo**, o segundo período aquisitivo está **Prescrito** devido o afastamento por Acidente de Trabalho, e após o Início do afastamento por Aposentadoria, nenhum período foi criado.   
Caso haja períodos criados indevidamente após o início do afastamento por Aposentadoria por Invalidez, como o afastamento é considerado uma **Suspensão de Contrato**, os mesmos deverão ser excluídos.   
  
  
**5.** Para excluir o Período Aquisitivo, Clique em **+ Manutenção**, selecione o período indevido e aperte a tecla ***Delete***, e em seguida clique em Confirmar:

![Excluir_Periodo_Aquisitivo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15081320056983)

**6.** Acesse: Miscelanea / Provisões / Provisões de Férias / 13º Salário (GPEA070) e **Exclua o Cálculo de Provisão incorreto** para este funcionário.  
Para mais informações sobre como excluir a Provisão, [clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036636774-RH-Linha-Protheus-GPE-Como-Excluir-o-C%C3%A1lculo-Individual-das-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio).

**7.** Calcule novamente as **Provisões**, e confirme se os dias de Férias estão corretos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15081601038231)

**Saiba Mais:**  
[RH-Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
