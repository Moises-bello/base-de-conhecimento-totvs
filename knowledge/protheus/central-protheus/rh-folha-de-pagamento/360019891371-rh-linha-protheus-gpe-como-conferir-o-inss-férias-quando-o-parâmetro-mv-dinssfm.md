---
article_id: 360019891371
category: RH - Folha de Pagamento
content_hash: 2b26da6c992233db26e9ea38ab2ac8936f5b0d15ffc50278660a45e5fd7c3236
fetched_at: '2026-06-28T22:44:13.264277+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir o INSS férias, quando o parâmetro
  MV_DINSSFM esta com R e o funcionário teve férias partidas
type: support-article
updated_at: '2025-09-15T14:53:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019891371-RH-Linha-Protheus-GPE-Como-conferir-o-INSS-f%C3%A9rias-quando-o-par%C3%A2metro-MV-DINSSFM-esta-com-R-e-o-funcion%C3%A1rio-teve-f%C3%A9rias-partidas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26235893951383) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como conferir o INSS férias, quando o parâmetro MV\_DINSSFM esta com R e o funcionário teve férias partidas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12  
  
**Solução**O parâmetro **MV\_DINSSFM****= R**, significa que o INSS de férias será rateado entre os dois meses de férias do empregado, quando houver férias partidas.  
![](http://tdn.totvs.com/download/attachments/284349894/image2017-7-4%2010%3A44%3A13.png?version=1&modificationDate=1499175855000&api=v2)  
  
Exemplo de **Cálculo das Férias**:  
  
**1. Cálculo INSS Primeiro mês:**  
Base INSS Férias Mês / Base INSS Total (soma dos dois períodos das férias) \* Desconto Total que seria de INSS pela tabela progressiva

**3.364,84** (**Verba 129** 2.523,63 + **Verba 134** 841,21) / **5.047,27** (**Verba 129** 2.523,63 + **Verba 134** 841,21 + **Verba 130** 1.261,82 + **Verba 135** 420,61) \* **565,55** (5.047,27 \* tabela progressiva) **Verba (418) INSS Férias = 377,03**  
  
**2. Cálculo INSS Segundo mês:**

Base INSS Férias Mês Seguinte / Base INSS Total (soma dos dois períodos das férias) \* Desconto Total que seria de INSS pela tabela progressiva

**1.682,43** (**Verba 130** 1.261,82 + **Verba 135** 420,61) / **5.047,27** (**Verba 129** 2.523,63 + **Verba 134** 841,21 + **Verba 130** 1.261,82 + **Verba 135** 420,61) \* **565,55** (5.047,27 \* tabela progressiva) **Verba (501) INSS Férias Mês Seguinte = 188,52**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099980613)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097705714)**

**FOLHA PRIMEIRO MÊS:**Na folha do primeiro mês, é apenas demonstrado as verbas de INSS para os dois meses (INSS FÉRIAS (418) e INSS FERIAS MES SEG (501). Entretanto, somente é considerado para montar a base de INSS do mês o INSS de Férias do primeiro mês:  
  
- Verba 706 (BASE INSS SAL LIMIT) **=**Verba 129 FERIAS + Verba 134 1/3 FERIAS + Verba 112 SALARIO MENSALISTA  
**2.523,63 + 841,21 + 5.047,27 = 8.412,11 \*\*** porém o teto limite é **6.101,06**, desta forma 8.412,11 - 6.101,06 = **2.311,05** será apresentada no na verba 704 (BASE INSS ACIMA LIMIT) - Teto INSS Sal Limit \* tabela progressiva do INSS  
**Verba 703 =  6.101,06 \* tabela progressiva do INSS =  713,08**- Verba 417 INSS = Desconto Total que seria de INSS pela tabela progressiva - Verba (418) INSS FÉRIAS   
**713,08 - 377,03 = 336,05**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100007773)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100007913)

**FOLHA SEGUNDO MÊS:**Na folha do segundo mês, é apenas demonstrada a verba de INSS de Férias do mês seguinte, que como agora é o mês atual gerou na verba 418 INSS FERIAS.   
  
-Verba 706 (BASE INSS SAL LIMIT) **=**Verba 129 FERIAS + Verba 134 1/3 FERIAS + Verba 112 SALARIO MENSALISTA  
**1.261,82 + 420,61 + 6.309,08 = 7.991,51 \*\*** porém o teto limite é **6.101,06**, desta forma 7.991,51 - 6.101,06 = **1.890,45** será apresentada no na verba 704 (BASE INSS ACIMA LIMIT)   
  
- Teto INSS Sal Limit \* tabela progressiva do INSS  
**Verba 703 =  6.101,06 \* tabela progressiva do INSS =  713,08**  
  
- Verba 417 INSS = Desconto Total que seria de INSS pela tabela progressiva - Verba (418) INSS FÉRIAS   
**713,08 - 188,52 = 524,56****![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100009353)**

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)  
[Como conferir o INSS férias, quando o parâmetro MV\_DINSSFM esta com R e o funcionário teve férias partidas](http://tdn.totvs.com/pages/viewpage.action?pageId=284349894)

[RH - Linha Protheus - GPE - Conceito do cálculo de folha com Férias partidas utilizando o parâmetro MV\_DINSSFM= S](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017956652-RH-Linha-Protheus-GPE-Conceito-do-c%C3%A1lculo-de-folha-com-F%C3%A9rias-partidas-utilizando-o-par%C3%A2metro-MV-DINSSFM-S?source=search)

[RH - Linha Protheus - GPE - Configuração do parâmetro MV\_DINSSFM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016451652-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-do-par%C3%A2metro-MV-DINSSFM?source=search)

[RH - Linha Protheus - GPE - Funcionamento do mnemônico P\_LIMTET - Cálculos do INSS das férias e/ou folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050724593-RH-Linha-Protheus-GPE-Funcionamento-do-mnem%C3%B4nico-P-LIMTET-C%C3%A1lculos-do-INSS-das-f%C3%A9rias-e-ou-folha?source=search)

[RH - Linha Protheus - GPE - Como conferir INSS salário e INSS férias em cálculo de folha de pagamento com o parâmetro MV\_DINSSFM = N](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008686801-RH-Linha-Protheus-GPE-Como-conferir-INSS-sal%C3%A1rio-e-INSS-f%C3%A9rias-em-c%C3%A1lculo-de-folha-de-pagamento-com-o-par%C3%A2metro-MV-DINSSFM-N?source=search)

[RH - Linha Protheus - GPE - Como é tratada a verba de dedução INSS base IR férias (Id 0168) na folha do mês seguinte quando tem férias partidas com o parâmetro MV\_DINSSFM = N](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052699634-RH-Linha-Protheus-GPE-Como-%C3%A9-tratada-a-verba-de-dedu%C3%A7%C3%A3o-INSS-base-IR-f%C3%A9rias-Id-0168-na-folha-do-m%C3%AAs-seguinte-quando-tem-f%C3%A9rias-partidas-com-o-par%C3%A2metro-MV-DINSSFM-N?source=search)
