---
article_id: 6350680624919
category: Escrita Fiscal - Impostos - ICMS
content_hash: 2d80eb98e6784b25fe32b4a19382b7d1cc39eaea22c4c1eb1f3778ad82727175
fetched_at: '2026-06-28T22:39:24.085098+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  MP FIS Quais as configurações do campo F4_APLIRED ( Red Carg TRB )?
type: support-article
updated_at: '2022-05-26T17:33:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6350680624919-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-MP-FIS-Quais-as-configura%C3%A7%C3%B5es-do-campo-F4-APLIRED-Red-Carg-TRB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**MP FIS Quais as configurações do campo F4\_APLIRED ( Red Carg TRB )?  
  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Solução**

O campo Red. Carg TRB (F4\_APLIRED) na TES é utilizado para um cálculo diferenciado de ICMS ST, podendo atender à legislação de diversos Estados, afetando diretamente o cálculo de ICMS próprio apenas na dedução do ICMS ST.  
  
![](https://totvssuporte.zendesk.com/attachments/token/XYyHNtb646ArWpLqiu7bTY5x1/?name=inline-492704806.png)​  
  
 Vide Help do campo: Reduz o valor do ICMS na mesma proporção da redução da carga tributária do ICMS/ST, somente para abater do valor   do ICMS-ST calculado.  
 Este campo possui 4 opções, conforme exemplificações abaixo para cada uma delas:  
  
**![](https://totvssuporte.zendesk.com/attachments/token/KiHgtZjwU07eOqsqt7aAglDkz/?name=inline1344594900.png)​**  
  
**1-Sim: Aplica redução de B.C. e a mesma alíquota da ST no ICMS a abater do ICMS/ST.**  
  
Por exemplo:  
Valor do produto: R$ 1.000,00  
Origem: SP Destino: MG  
Base do ICMS próprio: 1.000,00 x 12% = R$ 120,00  
Base do ICMS ST: 1.000 + 50%(MVA) = 1.500,00  
Aplica-se Redução de 20% na base ST: 1.500,00 – 300,00 = R$ 1.200,00  
Valor do ICMS ST:  
1.200,00 \* 18% = 216,00 (18% alíquota interna destinatário)  
216,00 – (bc do próprio: 1.000,00 x aliq ST 18% = 180,00 e aplica a redução de 20% (36,00): 144,00)  
216,00 – 144,00  
Valor do ST: R$ 72,00  
**Conclusão:**  
Note que no momento de deduzir o ICMS próprio do ST, ele sofre a redução e utiliza a alíquota do ST. Já o cálculo do ICMS próprio destacado na nota não é alterado.  
  
**2-Não: Não irá afetar o cálculo**  
Nada será afetado no cálculo.  
  
**3-Prop.Aliq: Aplica redução de B.C. e a mesma redução de alíquota ICMS Próprio a abater do ICMS/ST**  
Por exemplo:  
Valor do produto: R$ 1.000,00  
Origem: SP Destino: MG  
Base do ICMS próprio: 1.000,00 x 12% = R$ 120,00  
Base do ICMS ST: 1.000 + 50%(MVA) = 1.500,00  
Aplica-se Redução de 20% na base ST: 1.500,00 – 300,00 = R$ 1.200,00  
Valor do ICMS ST:  
1.200,00 \* 18% = 216,00 (18% alíquota interna destinatário)  
216,00 – (ICMS próprio: R$ 120,00 aplica a redução de 20% do ICMS ST (24,00) = R$ 96,00)  
216,00 – 96,00  
Valor do ST: R$ 120,00  
**Conclusão**:  
Note que no momento de deduzir o ICMS próprio do ST, ele sofre a redução do ST. Já o cálculo do ICMS próprio destacado na nota não é alterado.  
  
**4-Aliq.ST: Utiliza a alíquota do ICMS/STpara calcular o valor do ICMS Próprio a abater do ICMS/ST**  
Por exemplo:  
Valor do produto: R$ 1.000,00  
Origem: SP Destino: MG  
Base do ICMS próprio: 1.000,00 x 12% = R$ 120,00  
Base do ICMS ST: 1.000 + 50%(MVA) = 1.500,00  
Aplica-se Redução de 20% na base ST: 1.500,00 – 300,00 = R$ 1.200,00  
Valor do ICMS ST:  
1.200,00 \* 18% = 216,00 (18% alíquota interna destinatário)  
216,00 – (bc do próprio: 1.000,00 x aliq ST 18% = 180,00)  
216,00 – 180,00  
Valor do ST: R$ 36,00  
  
**Conclusão**:  
Note que no momento de deduzir o ICMS próprio do ST, ele utiliza a alíquota do ST. Já o cálculo do ICMS próprio destacado na nota não é alterado.
