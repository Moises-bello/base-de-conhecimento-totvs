---
article_id: 360004476711
category: RH - Férias
content_hash: cfc5b278f0621be7551fbd23d4dd3dbbacfc471ced12a843e28575576149ed0e
fetched_at: '2026-06-28T22:43:59.259181+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Verbas de férias não estão sendo integradas na
  folha de Pagamento
type: support-article
updated_at: '2025-06-02T14:59:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004476711-RH-Linha-Protheus-GPE-Verbas-de-f%C3%A9rias-n%C3%A3o-est%C3%A3o-sendo-integradas-na-folha-de-Pagamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26492303688471)Tempo aproximado para leitura: 00:02:00 min  
  
Ocorrência**As verbas do Roteiro FER não estão sendo integradas no Roteiro FOL, mesmo executando a Rotina GPEM019 - Integração.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Esse incidente pode ocorrer, pela inconsistência nas parametrizações das verbas do Roteiro de Férias  
  
**Solução**Acesse **Atualizações / Definições de Cálculos / Verbas** e revise o conteúdo dos seguintes campos:

**1. Verbas Mês Seguinte (RV\_COMDSEG):** As verbas de mês seguinte devem estar informadas com o código das verbas de férias no mês, por exemplo:  
  
-A verba com **Identificador de Cálculo** **0073 - Férias Mês Seguinte** deve estar preenchida com o código da verba de Identificador **0072 - Férias Mês**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32526517743383)  
  
-A verba com **Identificador de Cálculo** ***0078 - 1/3 Férias Mês Seguinte*** deve estar preenchida com o código da verba de Identificador ***0077 - 1/3 Férias Mês***.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32526490812695)  
  
 **2. Ref. Férias (RV\_REFFER):** As verbas referente a férias devem estar com o conteúdo igual a **S - Sim**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32526490815127)

**3. INSS (RV\_INSS) e INSS Férias (RV\_INSSFER):** Verificar o conteúdo destes dois campos para as verbas de férias, **caso possua incidência de INSS.**   
  
-Verbas referente ao mês como Férias Mês e 1/3 Férias Mês devem estar com **INSS = Sim** e **INSS Férias = Sim  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32526517754647)**

-Verbas referente ao mês seguinte como **Férias Mês Seguinte e 1/3 Férias Mês Seguinte,** deve estar com **INSS = Não** e **INSS Férias = Sim**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32526490819479)

**Observação:**  
Se verificou que utilizou alguma configuração incorreta após o cálculo da folha, alterar essas configurações após o cálculo das férias e da integração **não terá efeito**. Esse procedimento deve ser feito antes de qualquer outro processo; portanto, será necessário **refazer todo o cálculo.**

**Saiba Mais**[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)  
[RH - Linha Protheus - GPE - Como configurar verbas de férias mês seguinte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027941171-RH-Linha-Protheus-GPE-Como-configurar-verbas-de-f%C3%A9rias-m%C3%AAs-seguinte)  
[Verbas de Férias não estão sendo integradas na Folha de Pagamento](http://tdn.totvs.com/pages/viewpage.action?pageId=361440968)
