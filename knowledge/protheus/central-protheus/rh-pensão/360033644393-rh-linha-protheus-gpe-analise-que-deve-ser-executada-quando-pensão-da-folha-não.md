---
article_id: 360033644393
category: RH - Pensão
content_hash: 4fc3d609eec49e6f807c576ec323ed864b0be587f07c67be5ceb85f9fa0685bc
fetched_at: '2026-06-28T22:43:35.119004+00:00'
product: protheus
section_id: 360004995674
source: central-protheus
title: RH - Linha Protheus - GPE - Analise que deve ser executada quando pensão da
  folha não é calculada
type: support-article
updated_at: '2025-04-16T13:27:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033644393-RH-Linha-Protheus-GPE-Analise-que-deve-ser-executada-quando-pens%C3%A3o-da-folha-n%C3%A3o-%C3%A9-calculada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24900139759255) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Pensão da folha não é calculada. Qual análise que deve ser executada?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**Verifique os seguintes pontos:  
  
**1.** As verbas de pensão cadastradas para o beneficiário **não podem** conter identificador de cálculo verifique o cadastro das verbas em **Atualizações > Definições de Cálculo > Verbas (GPEA040)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24900139763991)  
 **2.** Analise se não há verbas de desconto de férias que estão com incidência para este cálculo (RV\_REFFER) em **Atualizações > Definições de Cálculos > Verbas (GPEA040)**. Por exemplo, IR de Férias, INSS de Férias, etc;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24900146979095)  
 **3.** Verifique se há sequências customizadas no roteiro FER ou FOL para o cálculo da pensão em **Atualizações > Definições de cálculo > Roteiros de Cálculo (GPEA160)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24900146985111)  
 **4.** Consulte se houve pagamento de verbas de folha com incidência para pensão ao executar o cálculo da folha na rotina de verbas em **Atualizações > Definições de Cálculos > Verbas (GPEA040)**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31454518303767)

**5.** As verbas de pensão devem ser configuradas com NÃO para pensão em **Atualizações > Definições de Cálculos > Verbas (GPEA040)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24900146987159)

**6.** Caso utilize o Campos de Verbas para Base de Cálculo, no cadastro do beneficiário, verifique se as verbas com **SIM** para Pensão estão devidamente cadastradas em **Atualizações > Funcionários > Beneficiários (GPEA280)**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24900146988183)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24900146989847)

**Saiba mais:**

[RH - Pensão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004995674-RH-Pens%C3%A3o)
