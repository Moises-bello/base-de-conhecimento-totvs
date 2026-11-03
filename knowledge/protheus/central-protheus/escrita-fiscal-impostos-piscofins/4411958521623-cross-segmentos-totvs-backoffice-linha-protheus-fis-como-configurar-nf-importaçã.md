---
article_id: 4411958521623
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 58d9cb767fd83231fb6f1c86ca8072bf485e1c95ebb68e60562b5308a2f9d4cd
fetched_at: '2026-06-28T22:39:36.885706+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar NF
  Importação PIS /COFINS alíquota zero?
type: support-article
updated_at: '2024-07-31T20:31:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411958521623-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-NF-Importa%C3%A7%C3%A3o-PIS-COFINS-al%C3%ADquota-zero
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25318178566423) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**  
MP - FIS - Como configurar NF Importação Com Calculo de ICMS e PIS /COFINS alíquota zero ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - FIS - Todas as versões  
  
**Solução**

Segue exemplo de configuração de TES

Valor da mercadoria = 8.884,69  
II imposto importação = 5.330,81  
Base de calculo = 17.335,97  
18% = 3.120,47  
  
TES  
  
Calcula ICMS = Sim  
L. Fisc ICMS = Tributado  
Agrega Valor = I - ICMS+Mer  
PIS/COFINS = Ambos  
Cred. Pis/Cof = Não calcula  
Sit Trib Pis = 73  
Sit Trib Cof  = 73  
Agr. Pis = P - Pis+Merc  
Agr. Cofins = C - COF+Merc  
PS/CF import = 3 = Ambos  
  
Lançamento do Documento de Entrada/Importação:   
  
![](https://totvssuporte.zendesk.com/attachments/token/DWOeZ4wEM2vE7kzZ958waq7zZ/?name=inline1737042013.png)​
