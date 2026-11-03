---
article_id: 5379083836695
category: RH - Calculo Autonomo/Prolabore
content_hash: a4cec93123809e7889ff595b60b8b720cb03c98882d908f725b6cda96133300d
fetched_at: '2026-06-28T22:43:15.187270+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Lançamento de verba de outras empresas para autônomo
type: support-article
updated_at: '2025-08-08T11:34:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5379083836695-RH-Linha-Protheus-GPE-Lan%C3%A7amento-de-verba-de-outras-empresas-para-aut%C3%B4nomo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24997051038231) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Lançamento de verba de outras empresas para Autônomo  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**

Alteração para que o INSS de funcionários com múltiplos vínculos em empresas diferentes seja calculado de acordo com as novas definições do governo.

Devido a necessidade de separar o INSS apurado para autônomos do INSS apurado para celetistas, foi criado um novo identificador de cálculo para que a Base da parte autônoma seja declarada de forma explicita.

O novo identificador de cálculo é o **1847 (Base INSS Autônomo Outras Empresas)**  e a verba deve ter as mesmas incidências da verba com **ID: 0288 (Base INSS Outras Empresas)**. Para cadastrar a verba acesse **Atualizações > Definições de Cálculos > Verbas (GPEA040).**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31945686429719)

A verba 0288 deve continuar sendo incluída com o total da base de INSS de outras empresas, bem como a verba 0289 com o total do INSS descontado em outras empresas.

A verba 1847 deve ser lançada com o total da base de INSS de outras empresas onde o funcionário possua vínculo de autônomo.  
  
**Exemplo 1:** Se o funcionário possuir apenas um vínculo em outra empresa, como autônomo, e com rendimento de R$2000,00, o lançamento deve ser o seguinte

Verba 0288 = 2000,00

Verba 1847 = 2000,00

**Exemplo 2:** Se o funcionário possuir dois vínculos em outras empresas, com rendimento de R$2000,00 no vínculo CLT e R$3000,00 em um vínculo autônomo, o lançamento deve ser feito da seguinte forma:

Verba 0288 = 5000,00

Verba 1847 = 3000,00

**Importante**

Se a referência da verba 1847 não for informada, será assumido o percentual padrão de 11% nos cálculos internos, se o INSS da outra fonte pagadora for apurado sobre 20%, este valor deve ser informado na referência da verba 1847 - [https://tdn.totvs.com/pages/releaseview.action?pageId=555268152.](https://tdn.totvs.com/pages/releaseview.action?pageId=555268152)

**Saiba mais:**

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
