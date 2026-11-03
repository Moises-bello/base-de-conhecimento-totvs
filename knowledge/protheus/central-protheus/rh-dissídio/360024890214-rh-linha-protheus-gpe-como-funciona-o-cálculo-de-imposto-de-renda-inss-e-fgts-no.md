---
article_id: 360024890214
category: RH - Dissídio
content_hash: 630c28160a1468321049493f11cfcaf1fe79ffabc8dad628b80f38f68c62fd7e
fetched_at: '2026-06-28T22:43:43.540340+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona o cálculo de Imposto de Renda, INSS
  e FGTS no dissidio retroativo
type: support-article
updated_at: '2025-08-20T13:02:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024890214-RH-Linha-Protheus-GPE-Como-funciona-o-c%C3%A1lculo-de-Imposto-de-Renda-INSS-e-FGTS-no-dissidio-retroativo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34314692174103) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como funciona o cálculo de Imposto de Renda, INSS e FGTS no dissidio retroativo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**No cálculo do dissidio retroativo o sistema **recalcula valores** de INSS e FGTS, assim como suas bases e os percentuais da empresa, de terceiros e acidente do trabalho.   
  
Portanto as verbas de Base de FGTS, Base INSS, Depósito do FGTS e Desconto do INSS **devem ser configuradas** para que seja possível ao sistema apurar as diferenças relativas à previdência e ao FGTS. Se estas verbas não forem configuradas, não sairão no dissídio retroativo e consequentemente, não serão tratadas as diferenças, pois isto somente ocorre na rotina GPEM690.  
  
Desta forma nas **verbas em que serão apuradas as diferenças** de dissídio (ID 0341, 0342 e demais diferenças criadas) **não pode haver incidência para FGTS e INSS**. Esta verificação é muito importante para que não haja dupla tributação sobre os valores apurados como diferença.  
  
A tributação de **Imposto de Renda** é feita por data de pagamento, **diferente** do FGTS e INSS, que trabalham por competência. Portanto, as verbas que compõem o cálculo do IR deverão possuir incidências para o IRRF, e, tratando-se das verbas de pagamento das diferenças dos valores de férias, no cadastro da verba, deverá ficar com “Sim” no campo “Ref. Férias”, e as verbas de pagamento das diferenças de 13º salário deverão ficar com “Sim” no campo “Ref.13º”. O pagamento é feito na própria verba do IRRF na folha de pagamento (id 0066).  
  
**Saiba Mais**  
O link a seguir direciona para o manual de dissidio, onde é possível verificar a configuração das verbas para cálculo correto do dissidio retroativo: [MANUAL GPE - Dissídio Retroativo](http://tdn.totvs.com/pages/viewpage.action?pageId=220889925)
