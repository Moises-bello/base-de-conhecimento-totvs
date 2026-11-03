---
article_id: 15309469010199
category: RH - Férias
content_hash: 89f2c16f819c4df62ac0b598c6690920008c373830f29b7e63272f5a22e609f8
fetched_at: '2026-06-28T22:43:59.250914+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Valor da verba Base de IR de férias com Id de cálculo
  0016 apresenta valores diferentes para funcionários que possuem desconto de IR dos
  que não tem
type: support-article
updated_at: '2025-05-20T18:05:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15309469010199-RH-Linha-Protheus-GPE-Valor-da-verba-Base-de-IR-de-f%C3%A9rias-com-Id-de-c%C3%A1lculo-0016-apresenta-valores-diferentes-para-funcion%C3%A1rios-que-possuem-desconto-de-IR-dos-que-n%C3%A3o-tem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15309492903831) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Valor da verba de Base de I. R. de Férias, que possui Id de cálculo 0016 apresenta valores diferentes para funcionários que possuem desconto de I. R. dos que não tem  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.33  
  
**Causa**Esta diferença ocorre por conta das **Implementações** do novo cálculo de **Imposto de Renda Simplificado.**   
  
**Solução**No momento do cálculo das férias o Sistema fará a verificação de qual dos modelos de cálculo será **mais benéfico** ao funcionário.

Quando o cálculo do IR utiliza o modelo **simplificado,** o INSS **não** é utilizado no cálculo, sendo considerada **apenas** a **dedução simplificada,** então o INSS não é abatido da base de IR.   
Quando o cálculo do IR é **completo,** o **INSS é abatido** da base de IR pois ele é utilizado no cálculo.

**Saiba Mais**[Espaço Fiscal - Totvs](https://www.totvs.com/blog/fiscal-clientes/novo-calculo-de-imposto-de-renda/)  
[DOU - MEDIDA PROVISÓRIA nº 1.171, de 30 de ABRIL de 2023](https://www.in.gov.br/en/web/dou/-/medida-provisoria-n-1.171-de-30-de-abril-de-2023-480184173)  
[FAQ da Consultoria de Segmentos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=758481181)  
[RH - Linha Protheus - GPE - MP-1.171/2023 - Nova forma de cálculo de IRRF no cálculo da folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14657002500631)  
[RH - Linha Protheus - GPE - Por que para alguns funcionários é abatido o INSS da base de IR e para outros não após alteração do cálculo de IR simplificado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14951685379991-RH-Linha-Protheus-GPE-Por-que-para-alguns-funcion%C3%A1rios-%C3%A9-abatido-o-INSS-da-base-de-IR-e-para-outros-n%C3%A3o-ap%C3%B3s-altera%C3%A7%C3%A3o-do-c%C3%A1lculo-de-IR-simplificado?source=search)  
[RH - Linha Protheus - GPE - MP-1.171/2023 - Como configurar a nova forma de cálculo de IR no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14626756121367)
