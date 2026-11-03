---
article_id: 8678496412055
category: Fiscal Arquivos Magnéticos - Ressarcimentos
content_hash: 053cfc0cd6b1e193683f6bcd7455844f0cab29a16ae1ed1f8b7eafb1ae64159b
fetched_at: '2026-06-28T22:42:12.596672+00:00'
product: protheus
section_id: 1500001546642
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FISR190- CAT42 - Relatório CAT42
  Composição campos 21 e 27.
type: support-article
updated_at: '2022-09-06T18:14:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8678496412055-Cross-Segmento-Backoffice-Linha-Protheus-FISR190-CAT42-Relat%C3%B3rio-CAT42-Composi%C3%A7%C3%A3o-campos-21-e-27
---

**Dúvida**

Como é composto os **campos 21 e 27 do relatório FISR190**.   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**

Mais informações sobre a estrutura do relatório **FISR190*,***referente a composição dos **campos 21 e 27.**  
  
**1.** Segundo o Manual do Sistema de **Apuração do Ressarcimento** ou **Complemento do ICMS Retido por Substituição Tributária ou Antecipado**, temos:

"**Coluna 12** - Valor total do **imposto suportado pelo contribuinte substituído (Entrada)** - O valor total do imposto **suportado pelo contribuinte substituído**, abrangendo o incidente na operação própria do substituto e o retido, ou o cobrado na operação interestadual anterior e o antecipado pelo destinatário paulista, nas operações de entrada."  
  
Entendemos que, para a composição dessa coluna, em aquisições nas quais o remetente da mercadoria é um **substituído tributário**, não podemos usar o valor que seria o **ICMS próprio do substituído** (obtido mediante aplicação da **alíquota interna** sobre a **base de cálculo** que seria atribuída à operação própria desse **remetente substituído**, conforme **artigo 271 do RICMS**), visto que o texto descritivo da **coluna 12** é claro, quando cita apenas o incidente na **operação própria do substituto**.  
  
Sabemos que em aquisições com **CST 060**, o valor apresentado em **Informações Complementares** (e usado pela **rotina de apuração** para a **composição da coluna 12**) é apenas o do **imposto recolhido anteriormente por Substituição Tributária**, e não o da **operação própria do substituto**. Em resumo, em **aquisições de substituído, não possuímos o valor do ICMS próprio do substituto**.  
  
**2.** A rotina de **apuração do ressarcimento** leva em consideração o **ICMS próprio** em **aquisições de** **substituído**, mas apenas para a **composição das colunas 21 e 27.** Segundo o **Manual do Sistema de Apuração do Ressarcimento** ou **Complemento do ICMS Retido por Substituição Tributária ou Antecipado**, temos:

"**Coluna 21 - Valor de Confronto** - **ICMS** Efetivo da Entrada nas Demais Hipóteses  
O valor do **ICMS da operação própria**, do **sujeito passivo por substituição** do qual a mercadoria tenha sido recebida diretamente ou o cobrado na **operação interestadual** anterior, em caso de **antecipação**, ou ainda o **valor do ICMS** que seria atribuído à **operação própria do contribuinte substituído** do qual a mercadoria tenha sido recebida, caso estivesse submetida ao **regime comum de tributação**; observar, quando aplicável, **o artigo 271 do RICMS*."***  
  
"**Coluna 27 - Apuração** – **Valor do ICMS Crédito da Operação Própria** (artigo 271)  
**Valor do Crédito de ICMS da Operação Própria** (artigo 271) obtido na **coluna 21** quando o **Código Enquadramento Legal for igual a 4**."  
  
Portanto, em resumo, **para a composição da coluna 21** (e consequentemente da coluna 27), nos baseamos no **disposto no artigo 271 do RICMS-SP**, conforme disposições do Manual da Portaria CAT 42/2018. No entanto, entendemos que para a **coluna 12**, não podemos nos basear nesse artigo, pois ele não é citado nessa coluna. Percebe-se que ali deve haver um **ICMS próprio**, mas o do substituto.  
Seguindo orientações do o **Manual do Sistema de Apuração do Ressarcimento** ou **Complemento do ICMS Retido por Substituição Tributária ou Antecipado**, entendemos ser possível presumir o valor de **composição da coluna 12**, mesmo em aquisições com **CST 060**. O manual observa o seguinte:  
  
O **ICMS** suportado pelo **contribuinte substituído**, abrangendo o incidente na **operação própria do substituto e o retido**, ou o **cobrado na operação interestadual** anterior e o pago por **antecipação** pelo **destinatário paulista**, é a soma dessas duas parcelas, ou seja, a soma do cobrado na operação própria do substituto com o **retido por substituição tributária**, ou a soma do cobrado na **operação interestadual** anterior com o pago por **antecipação pelo destinatário paulista**. Visto ainda de outra forma, o **ICMS suportado** é o valor resultante da multiplicação da base de cálculo da sujeição passiva por **substituição** pela alíquota interna aplicável à saída ao **consumidor final**. Assim, exemplificando, se uma determinada mercadoria é vendida pelo fabricante a R$ 100,00 e a margem de **valor agregado (MVA) ou Índice de Valor Adicionado Setorial (IVA-ST)** é de 50%, sendo a alíquota interna da mesma 18%, a base de cálculo da retenção será R$ 150,00 e o **ICMS suportado pelo contribuinte substituído** será de R$ 27,00 (sendo o incidente na operação própria do fabricante substituto R$ 18,00 e o ICMS retido R$ 9,00).  
  
Considerando todas as informações passadas acima entendemos que em aquisições com **CST 060**, no **Protheus**, a legislação nos permite compor a **coluna 12**, utilizando, para isso, a **base de cálculo da sujeição passiva por substituição**, informada no campo **D1\_BASNDES/ FT\_BASNDES**, **multiplicado pela alíquota interna do produto**.

Atualmente, nessa situação, **usa-se apenas o valor do imposto recolhido anteriormente**, informado em **D1\_ICMNDES/FT\_ICMNDES**.
