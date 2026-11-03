---
article_id: 360051801933
category: RH - Calculo Autonomo/Prolabore
content_hash: 09f1e67d668e32132e37554164f85df206ea20004eb6241b6dab4e9803aca76b
fetched_at: '2026-06-28T22:43:15.255944+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Alteração para que o INSS de funcionários com múltiplos
  vínculos em empresas diferentes. Criado identificador de cálculo é o 1847 (Base
  INSS Autônomo Outras Empresas)
type: support-article
updated_at: '2024-08-15T22:01:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051801933-RH-Linha-Protheus-GPE-Altera%C3%A7%C3%A3o-para-que-o-INSS-de-funcion%C3%A1rios-com-m%C3%BAltiplos-v%C3%ADnculos-em-empresas-diferentes-Criado-identificador-de-c%C3%A1lculo-%C3%A9-o-1847-Base-INSS-Aut%C3%B4nomo-Outras-Empresas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25675256887191)**Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Alteração para que o INSS de funcionários com múltiplos vínculos em empresas diferentes. Criado identificador de cálculo é o 1847 (Base INSS Autônomo Outras Empresas)   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Causa**Alteração para que o INSS de funcionários com múltiplos vínculos em empresas diferentes seja calculado de acordo com as novas definições do governo.  
  
**Solução**

Devido a necessidade de separar o INSS apurado para **autônomos** do INSS apurado para **celetistas**, foi criado um novo identificador de cálculo para que a Base da parte autônoma seja declarada de forma explicita.

O novo identificador de cálculo é o **1847 (Base INSS Autônomo Outras Empresas)**  e a verba deve ter as mesmas incidências da verba com ID.: 0288 (Base INSS Outras Empresas).

A verba 0288 deve continuar sendo incluída com o total da base de INSS de outras empresas, bem como a verba 0289 com o total do INSS descontado em outras empresas.

A verba 1847 deve ser lançada com o **total da base de INSS de outras empresas** onde o funcionário possua vínculo de autônomo.

Exemplo 1: Se o funcionário possuir apenas um vínculo em outra empresa, como autônomo, e com rendimento de R$2000,00, o lançamento deve ser o seguinte

Verba 0288 = 2000,00

Verba 1847 = 2000,00

Exemplo 2: Se o funcionário possuir dois vínculos em outras empresas, com rendimento de R$2000,00 no vínculo CLT e R$3000,00 em um vínculo autônomo, o lançamento deve ser feito da seguinte forma:

Verba 0288 = 5000,00

Verba 1847 = 3000,00  
  
***Importante***  
Se a referência da verba 1847 não for informada, será assumido o percentual padrão de 11% nos cálculos internos, se o INSS da outra fonte pagadora for apurado sobre 20%, este valor deve ser informado na referência da verba 1847  
  
**Saiba Mais**

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
