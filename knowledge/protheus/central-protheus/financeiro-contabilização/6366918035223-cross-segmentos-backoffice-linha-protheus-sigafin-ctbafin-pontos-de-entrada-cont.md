---
article_id: 6366918035223
category: Financeiro - Contabilização
content_hash: 2c3d66758aee128ea06b1e119f0d225afadcad49d252fcb40d7f9bb3ac2c21d0
fetched_at: '2026-06-28T22:38:05.354310+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - Pontos de
  Entrada Contabilização Off-line
type: support-article
updated_at: '2024-07-26T19:38:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6366918035223-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-Pontos-de-Entrada-Contabiliza%C3%A7%C3%A3o-Off-line
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23468455500567) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quais os pontos de entrada da rotina Contabilização Off-line (CTBAFIN)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Segue abaixo a relação dos pontos de entrada da rotina **CTBAFIN**  
**CtbFPos** Permite complementar a **contabilização off-line** do **financeiro** é chamado após a contabilização da filial corrente**.**  
[CtbFPos - Tratamentos específicos na Contabilização de Filial.](https://tdn.totvs.com/x/Cko9I)  
  
**F370E1F** Permite a edição completa da *Query* que consulta na Tabela **SE1** (Títulos a Receber) os registros para a contabilização**.**[F370E1L - Confirma contabilização do titulo SE1](https://tdn.totvs.com/x/8KJc)  
  
**F370E2F** Permite a edição completa da *Query* que consulta na Tabela **SE2** (Títulos a Pagar), possibilitando modificar a filtragem dos registros para a contabilização.[F370E2F - Ponto de Entrada para filtrar registros do SE2 da rotina CTBAFIN](https://tdn.totvs.com/x/p7DkJQ)

**F370E5F** Permite a edição completa da Query que consulta na Tabela **SE5** (**Movimentação Bancária),** possibilitando modificar a filtragem dos registros para a contabilização.[F370E5F - Ponto de Entrada para filtrar registros do SE5 da rotina CTBAFIN](https://tdn.totvs.com/x/FbHkJQ)  
  
**F370EFF** Permite complementar a Query que consulta a Tabela **SEF** (**Cheques**), possibilitando modificar a filtragem dos registros para a contabilização.  
[F370EFF - Ponto de Entrada para filtrar registros do SEF da rotina CTBAFIN](https://tdn.totvs.com/x/ULLkJQ)

**Saiba mais**

[Contabilização Offline - CTBAFIN](https://tdn.totvs.com/pages/releaseview.action?pageId=497932563#Contabiliza%C3%A7%C3%A3oOffline-CTBAFIN-Financeiro-P12-03.PAR%C3%82METROSAPLICADOS)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - Performance na Contabilização do Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000227308-MP-SIGAFIN-CTBAFIN-Performance-na-Contabiliza%C3%A7%C3%A3o-do-Financeiro?source=search)

[Cross Segmento - Backoffice Linha Protheus -SIGAFIN - Como contabilizar o Pagamento Antecipado (PA)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036131394-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Como-contabilizar-o-Pagamento-Antecipado-PA-?source=search)
