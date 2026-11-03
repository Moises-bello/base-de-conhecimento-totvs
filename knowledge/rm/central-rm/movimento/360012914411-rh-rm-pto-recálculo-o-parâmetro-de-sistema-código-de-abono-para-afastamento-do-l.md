---
article_id: 360012914411
category: Movimento
content_hash: 128af559304af45a40346adaf533fb123d12177f0b87a2dbe6edd510f628a67c
fetched_at: '2026-06-28T22:46:36.086284+00:00'
product: rm
section_id: 1500000861602
source: central-rm
title: 'RH - RM - PTO - Recálculo: "O parâmetro de sistema ''código de abono para
  afastamento do Labore'' não está configurado corretamente"'
type: support-article
updated_at: '2025-02-19T00:58:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012914411-RH-RM-PTO-Rec%C3%A1lculo-O-par%C3%A2metro-de-sistema-c%C3%B3digo-de-abono-para-afastamento-do-Labore-n%C3%A3o-est%C3%A1-configurado-corretamente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16981006119447) Tempo aproximado para leitura: 00:01:00 min**

**Ocorrência**No módulo **Automação de Ponto**, ao realizar o **recálculo** do espelho do funcionário, é apresentado o erro "O parâmetro de sistema 'código de abono para afastamento do Labore' não está configurado corretamente".  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto  – A partir da versão 11.80  
  
**Causa**   
Esse incidente ocorre devido a falta de cadastro do abono nas parametrizações iniciais do sistema.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse o módulo de **Automação de Ponto**, guia **Configurações** e selecione a opção **Parametrizador**. Dentro da janela, selecione a opção **Iniciais** e avance o processo.  
     
   ![2018-08-09_14_09_10-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008865912)
2. Após isso, insira o código do abono que será utilizada no afastamento, dentro do campo **Abono utilizado para Atestados do Labore**.  
   ![2018-08-09_14_08_55-Assistente_de_Implanta__o_de_Processos__Ponto___Iniciais_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008865892)
