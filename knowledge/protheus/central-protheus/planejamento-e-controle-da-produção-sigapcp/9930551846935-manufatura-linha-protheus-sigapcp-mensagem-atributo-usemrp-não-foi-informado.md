---
article_id: 9930551846935
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: a363a11c216eecdb7900de8cf8b4a004cdd6f62c9e544f84739ecaaf2ec38260
fetched_at: '2026-06-28T22:42:44.429005+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem Atributo usemrp não foi informado
type: support-article
updated_at: '2022-11-01T14:14:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9930551846935-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-Atributo-usemrp-n%C3%A3o-foi-informado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:50 min****Ocorrência**No módulo **SIGAPCP - Planejamento e Controle da Produção**, ao executar a rotina **PCPA140 - Sincronizador do MRP** ocorre a mensagem **Atributo usemrp não foi informado**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Este incidente ocorre quando o local de estoque indicado na mensagem não está parametrizado para ser utilizado no **MRP - Manufacturing Resource Planning**.  
  
**Solução**Para solucionar essa ocorrência, acesse a rotina **AGRA045 - Locais de Estoque** e verifique se o campo **Entra MRP** possui alguma informação**.**Caso esteja em branco, deverá ser informado **1-Sim** ou **2-Não** para que a mensagem não seja exibida.  
Esta validação deve ser realizada para todos os locais de estoque.
