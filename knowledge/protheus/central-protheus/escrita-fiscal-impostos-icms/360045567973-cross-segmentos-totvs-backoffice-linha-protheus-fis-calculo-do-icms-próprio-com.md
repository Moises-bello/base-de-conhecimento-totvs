---
article_id: 360045567973
category: Escrita Fiscal - Impostos - ICMS
content_hash: 275e501b2cc2f186c008b73978dd71c18b20ffb74670e00bfb4a2e6be7837c11
fetched_at: '2026-06-28T22:39:24.355415+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Calculo do ICMS Próprio
  Com Valor e Base de Cálculo Zerados
type: support-article
updated_at: '2021-07-28T17:08:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045567973-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Calculo-do-ICMS-Pr%C3%B3prio-Com-Valor-e-Base-de-C%C3%A1lculo-Zerados
---

**Dúvida**Como configurar o sistema para que o valor do ICMS Próprio seja apresentado com valor e base de cálculo zerados.

A solicitação de configuração acima, foi apresentada por conta do trecho abaixo:

***"Na aquisição de bens para o ativo permanente ou de material de uso e consumo, caso o Estado de origem tenha concedido benefício fiscal sobre a operação sem anuência do CONFAZ, benefício esse que altere a sua base de cálculo, para efeito de apuração do ICMS diferencial de alíquota, deverá a consulente observar as restrições previstas pelo Decreto nº 4.540/2004.******Neste caso, o percentual do diferencial de alíquota deverá ser aplicado sobre o valor total da operação, sem considerar o benefício concedido.***  
***A título de exemplo, considerando-se que o referido bem tenha sido adquirido no Estado de São Paulo no valor de R$ 1.000,00, e que sobre a operação tenha sido concedido redução de base de cálculo de 40% sem anuência do CONFAZ, nesta hipótese, deverá ser recolhido o ICMS diferencial de alíquota no valor de R$ 100,00, ou seja, 10% (17% - 7%) sobre o valor de R$ 1.000,00, portanto, sem computar o benefício fiscal, vez que esse não fora aprovado pelo CONFAZ.”***  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Acessar o cadastro de TES - (MATA080)  
  
Na Aba Impostos configure os campos abaixo:   
  
Calcula ICMS = Não   
% Red do ICMS = Definido pelo cliente  
L. Fisc. ICMS = Outros   
Calc Dif ICM = Sim   
Mat. Consumo = Sim   
Sit Trib ICM = 90 Outras   
Cons. Red Cmp = Não   
Calc Difal = Sim   
Configurar o parâmetro MV\_BICMCMP = .F.   
  
Abaixo calculo apresentado no documento de entrada utilizando as configurações acima:   
  
![](https://totvssuporte.zendesk.com/attachments/token/eBdIzZkYZ0tJgWmjU6hOUOfko/?name=inline462843949.png)
