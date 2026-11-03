---
article_id: 8134979381399
category: RH - Folha de Pagamento
content_hash: 398095225aaa93f04e7d2310e510ca32bbba0e4ee5120dc180560eb459d50600
fetched_at: '2026-06-28T22:44:16.341722+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Separação ID 1449 - Abono Pago mês anterior
type: support-article
updated_at: '2024-09-12T22:05:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8134979381399-RH-Linha-Protheus-GPE-Separa%C3%A7%C3%A3o-ID-1449-Abono-Pago-m%C3%AAs-anterior
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26337856146455) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Consulta COSIT nº209/2021 - Separação do ID **1449 - Abono Pago mês anterior** para este ID levar somente o Abono Pago Mês anterior e criar um novo ID para o valor de **1/3 de abono Pago mês anterior**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.

#### **Solução:**

Ajuste para efetuar separação do ID **1449** **- Desconto de abono mês anterior** e ID **1890 - 1/3 abono pago no mês anterior.**

Dessa forma, os valores de desconto de abonos e 1/3 abono serão gerados em dois Ids:

- ID de cálculo **1449 - Abonos Pagos mês anterior,** irá conter o desconto dos valores de abono que foram pagos no mês anterior, obtido através das verbas configuradas com o campo **RV\_REFFER** preenchido **S** (Sim) e referentes aos ID´s de cálculo:

**0205 - Abono mês seguinte**

**0207 - Dif. abono mês seguinte**

**0633 - Media horas s/ abono mês seguinte**

**0634 - Media valor s/ abono mês seguinte**

**0635 - Adicional s/ abono mês seguinte**

**1313 - ATS abono mês seguinte**

**1315 - ATS abono mês seguinte s/ verbas**

**1317 - Periculosidade abono mês seguinte**

**1319 - Periculosidade abono mês seguinte s/ verbas**

**1321 - Insalubridade abono mês seguinte**

**1323 - Insalubridade abono mês seguinte s/ verbas**

**1325 - Adicional cargo confiança abono mês seguinte**

**1327 - Adicional transferência abono mês seguinte**

**1409 - Periculosidade s/ medias abono mês seguinte**

**1410 - Insalubridade s/ media abono mês seguinte**

**1418 - Dif. media horas s/ abono mês seguinte**

**1419 - Dif. media valor s/ abono mês seguinte**Exemplo de cadastro para verba de ID 1449:

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8137646693527)**

**Obs: Para facilitar o cadastro, copiar a configuração da verba de ID de cálculo 0164, mas retirar a incidência para tributação (INSS, IR e FGTS).**

- ID de cálculo **1890 - 1/3 Abono pago mês anterior,**Irá conter o desconto dos valores de 1/3 de abono que foi pago no mês anterior, obtido através da verba referente ID´s de cálculo:

**0206 -** **1/3 abono**

**0208 - Dif. 1/3 Abono**

Exemplo de cadastro para verba de ID 1890:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8137744460951)

**Observação:**

Será **obrigatório** efetuar o cadastro da verba do ID **1890** e deixar a incidência para **IR = Sim**, para efetuar o fechamento do período, pois o valor do desconto do abono deverá ser gerado para o próximo período.

**Importante**

Para explicar a diferença do conceito do sistema após a criação do ID 1890, verificar o exemplo abaixo:

Funcionário com salário de R$ 2.400,00, com férias de 20 dias e 10 de abono iniciados em 16/04/2018 e as verbas de provento e desconto abaixo:

| Verba | Descrição | Valor |
| --- | --- | --- |
| 186 (Id 0205) | Abono Pecuniário Mês Seguinte | R$ 800.00 |
| 187 (Id 0206) | 1/3 Sobre Abono Pecuniário Mês Seguinte | R$ 266,67 |

Ao realizar o fechamento do período, o sistema irá transportar as verbas de abono do mês seguinte para o próximo período como verbas abono e 1/3 abono do mês e irá gerar verba de desconto para zerar o líquido dessas verbas.

As verbas de  abono e 1/3 de abono que foram geradas para o próximo período são:

| Verba | Descrição | Valor |
| --- | --- | --- |
| 184 (Id 0074) | Abono Pecuniário Mês | R$ 800,00 |
| 185 (Id 0079) | 1/3 Sobre Abono Pecuniário Mês | R$ 266,67 |

Antes da criação do Id 1890, o sistema iria efetuar a geração do desconto de férias e abono aglutinados na mesma verba:

| Verba | Descrição | Valor |
| --- | --- | --- |
| 434 (Id 1449) | Abonos Pagos Mês Anterior | R$ 1.066.67 |

Após a criação do Id 1449, o sistema irá separar o desconto de férias e o desconto do abono em duas verbas:

| Verba | Descrição | Valor |
| --- | --- | --- |
| 434 (Id 1449) | Abonos Pagos Mês Anterior | R$ 800,00 |
| 435 (Id 1890) | 1/3 Abono Pago Mês Anterior | R$ 266,67 |

A verba de **ID 1890 não é obrigatória** desde que o IR do**ID 206** e **ID 208** sejam  iguais a **Não**, porém caso a incidência para **IR** destas verbas sejam**Sim**, a criação da verba para o **ID 1890 se torna obrigatória** para fechar o período, caso contrário será apresentado log informando a necessidade da criação da verba para que os valores fiquem corretos para o e-social.

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

**<https://tdn.totvs.com/pages/releaseview.action?pageId=353278778>  <https://tdn.totvs.com/pages/releaseview.action?pageId=353278778>**
