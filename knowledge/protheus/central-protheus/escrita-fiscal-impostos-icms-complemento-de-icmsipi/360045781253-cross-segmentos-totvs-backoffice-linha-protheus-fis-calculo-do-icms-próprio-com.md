---
article_id: 360045781253
category: Escrita Fiscal - Impostos - ICMS - Complemento de ICMS/IPI
content_hash: f104681bf4d2690c472aef569475bb5559c94b22035419fe34050c90d24a2b4c
fetched_at: '2026-06-28T22:39:21.294936+00:00'
product: protheus
section_id: 1500001538701
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Calculo do ICMS Próprio
  com B.C do ICMS complementar zerada
type: support-article
updated_at: '2021-07-13T18:39:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045781253-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Calculo-do-ICMS-Pr%C3%B3prio-com-B-C-do-ICMS-complementar-zerada
---

**Dúvida**  
Como configurar o sistema para que o valor do ICMS Próprio seja calculado com redução de base de calculo e o valor do ICMS Complementar seja apresentado com valor de base de cálculo zerada efetuando o calculo sem considerar a redução da base.   
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Acessar o cadastro de TES - (MATA080)Na Aba Impostos configure os campos abaixo:   
  
Utilizando redução de base de cálculo do ICMS:   
  
Cadastro de TES  
  
Aba Impostos:   
  
Calcula ICMS = Sim   
% Red do ICMS = Definido pelo cliente  
L. Fisc. ICMS = Outros   
Calc Dif ICM = Sim   
Mat. Consumo = Sim   
Sit Trib ICM = 90 Outras   
Cons. Red Cmp = Não   
Calc Difal = Sim   
  
Configurar o parâmetro MV\_BICMCMP = .F.   
  
"Informa se a base do ICMS complementar deve ser reduzida como o ICMS normal"                           
  
Abaixo calculo apresentado no documento de entrada utilizando as configurações acima e considerando o exemplo enviado na solução de consulta utilizando redução de base de calculo do ICMS:   
  
![](https://totvssuporte.zendesk.com/attachments/token/eFCOzJUSTwx7ixuRRNfM8Hn0s/?name=inline-715051830.png)
