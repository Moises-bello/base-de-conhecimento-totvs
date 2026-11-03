---
article_id: 5311267180055
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 1d8621e6520bc7ee82c2065f718478bdab4527d30048972ea2d2d245127792d4
fetched_at: '2026-06-28T22:42:10.351856+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar o
  E-CREDAC - Sistema Eletrônico de Gerenciamento de Crédito Acumulado de ICMS?
type: support-article
updated_at: '2024-04-08T19:19:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5311267180055-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-E-CREDAC-Sistema-Eletr%C3%B4nico-de-Gerenciamento-de-Cr%C3%A9dito-Acumulado-de-ICMS
---

**Dúvida**  
Como configurar o ambiente para geração do **E-CREDAC - Sistema Eletrônico de Gerenciamento de Crédito Acumulado de ICMS?**  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**

**Solução**

A **SEFAZ-SP** instituiu duas formas de solicitar a apropriação dos **Créditos Acumulados de ICMS**:  
   
- **Portaria CAT207** que determina a apropriação de forma **Simplificada**.  
   
- **Portaria CAT83** que é forma completa da apropriação do crédito. A solicitação de ressarcimento neste molde é mais complexa, sendo necessário um maior controle dos processos de compra (**tabela SD1**), venda (**tabela SD2**) e se existirem de produção (**tabela SD3**).  
   
O sistema atende as duas formas e cabe ao fiscal da empresa definir qual se adequa melhor ao seu cenário e operações da empresa.  
   
Abaixo, seguem *links* com as documentações:  
   
**CAT207 - Apuração Simplificada do Crédito Acumulado do ICMS - Portaria CAT207/2009 - SP**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=631856241>

**Relatório FISR026 - CAT207**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=625453930>

==  
  
**CAT83 -  Portaria CAT83/09 - eCred - Crédito Acumulado**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=640694285>  
   
Recomendamos que antes da implantação da rotina, utilize uma base teste para seguir os exemplos que temos nos *links*.  
 Assim será mais fácil abstrair a forma de como o sistema apura seus créditos acumulados e adequar as suas operações em base de produção.
