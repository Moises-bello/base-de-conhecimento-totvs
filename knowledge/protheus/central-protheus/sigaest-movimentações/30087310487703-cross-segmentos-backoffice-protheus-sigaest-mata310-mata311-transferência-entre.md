---
article_id: 30087310487703
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 80c11c52fba14290bd0c280aed604d33e705bc205c7f9e89d95430c224a2b981
fetched_at: '2026-06-28T22:38:58.560539+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross-Segmentos-Backoffice-Protheus-SIGAEST-MATA310-MATA311-Transferência entre
  Filiais-Somar-o-Valor-do-ICMS-no-Item
type: support-article
updated_at: '2025-03-12T12:41:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30087310487703-Cross-Segmentos-Backoffice-Protheus-SIGAEST-MATA310-MATA311-Transfer%C3%AAncia-entre-Filiais-Somar-o-Valor-do-ICMS-no-Item
---

**Dúvida**Como somar o valor do ICMS no Item e Total da nota ?  
  
**Ambiente**Microsiga Protheus- todas as versões.  
  
**Solução**

1° - Está com o pacote abaixo aplicado :   
O pacote pode ser acessado no endereço:  
12.1.2210: [https://r.totvs.io/p/1177670 ;](https://r.totvs.io/p/1177670)  
12.1.2310: [https://r.totvs.io/p/1177668 ;](https://r.totvs.io/p/1177668)  
12.1.2410: <https://r.totvs.io/p/1177671> ;   
12.1.33: [https://r.totvs.io/p/1177669 ;](https://r.totvs.io/p/1177669)

2°- Criar o parâmetro MV\_TRFICMS conforme documentação abaixo:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=894381636>

3º - Para efetuar o cálculo do ICMS realize a configuração através do Configurador de Tributos conforme a documentação abaixo:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=907923942>

4°- Configurar o parâmetro MV\_FILTRF conforme pede no artigo abaixo:  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011717052-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Transfer%C3%AAncia-entre-Filiais-utilizando-o-par%C3%A2metro-MV-FILTRF>

5°- Acessar a rotina de Cadastro de TES e configure os campos:  
F4\_TRANSFIL = 1 - SIM para os TES de entrada e Saída  
  
6° - Acesse o cadastro do cliente e configure o campo A1\_FILTRF

7° - Acesse o cadastro do Fornecedor e configure o campo A2\_FILTRF

8º - Após realizar os procedimentos acima, acessar a rotina transferência entre filiais ( MATA311 ) para emissão da operação, e logo em seguida   
verificar se os valores foram calculados corretamente, ou seja, verificar se soma ICMS no Vlr. Unitário e Vlr. Total, para a NF de Entrada e Saída.
