---
article_id: 13053142707991
category: RH - Contabilização
content_hash: 3c8f6a6d530343abb450381ea88095d123aa550cf77a8462a1146883502bc55f
fetched_at: '2026-06-28T22:43:45.846416+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar a contabilização de provisão de férias
  rateada
type: support-article
updated_at: '2023-03-13T20:39:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13053142707991-RH-Linha-Protheus-GPE-Como-realizar-a-contabiliza%C3%A7%C3%A3o-de-provis%C3%A3o-de-f%C3%A9rias-rateada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como realizar a contabilização de provisão de férias rateada?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**  
Verifique o passo a passo para contabilização da provisão rateada:   
  
1. Realize a configuração da programação de rateio na folha de pagamento conforme documentação abaixo:  
[RH - Linha Protheus - GPE - Como realizar a programação de rateio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018658931-RH-Linha-Protheus-GPE-Como-realizar-a-programa%C3%A7%C3%A3o-de-rateio)  
  
2. Cadastre as verbas com os identificadores de cálculo de provisão rateada:

**- Identificadores de Cálculo de Provisão de Férias (Rateada):**0960 - Provisão Mês de Férias rateio  
0961 – Provisão Mês 1/3 férias rateio  
0962 – Provisão Adicional de Férias rateio  
0963 – Provisão de INSS Férias rateio  
0964 – Provisão FGTS Férias rateio  
0965 – PIS Provisão Férias Rateio  
  
3. Efetue o cálculo da provisão.   
  
4. Em miscelânea -> Provisões -> Provisão Férias/13º salário visualize o cálculo, as opções de consulta e geração de relatório são:  
-> Provisão rateada   
-> Imprimir mensal de férias

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13053849375127)  
  
5) Para provisão rateada observe que existem verbas que são correspondente às verbas da tabela SRT (provisão) sendo apresentadas na tabela RHT (provisão rateada):

**Exemplo 1:**  
P51(0130) x P50 (0960)  -  A verba na tabela SRT é a verba de ID 0130 e a verba correspondente na tabela RHT é a verba de ID 0960.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13054013405719)

**Exemplo 2:**

P61 (0255) x P60 (0961) -  A verba na tabela SRT é a verba de ID 0255 e a verba correspondente na tabela RHT é a verba de ID 0961.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13054071279383)

**ATENÇÃO:** A tabela RHT será a tabela preponderante para a contabilização. 

6) Conferência da linha do Mês, para férias a Vencer, de acordo com o relatório impresso na opção IMPRIMIR MENSAL DE FÉRIAS:  
![](https://centraldeatendimento.totvs.com/hc/pt-br/article_attachments/13057785160727/bae03fde0660bf392c826dda7f181cfb46d38bcded23ec34757ba9a631f0838e.png)

7) Verifique a contabilização no exemplo abaixo das verbas P50 e P60. Veja que as verbas apresentadas são exatamente as verbas da tabela RHT, devido a configuração do rateio:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13056385415959)

**Saiba Mais**  
[RH - Linha Protheus - GPE - Quais são os identificadores de cálculo, disponíveis para provisão de férias e 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6071282481303-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-os-identificadores-de-c%C3%A1lculo-dispon%C3%ADveis-para-provis%C3%A3o-de-f%C3%A9rias-e-13%C2%BA-sal%C3%A1rio)  
[Página Centralizadora da Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o?page=1#articles)  
[Página Centralizadora da Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
