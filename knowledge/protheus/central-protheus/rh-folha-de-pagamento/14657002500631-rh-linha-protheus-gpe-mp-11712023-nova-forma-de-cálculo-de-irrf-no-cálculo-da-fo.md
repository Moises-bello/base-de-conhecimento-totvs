---
article_id: 14657002500631
category: RH - Folha de Pagamento
content_hash: 04351e4395fcfe775b7c1cb3a7f6ed0700cdd9bc02ba200a4fb285f42ebdb507
fetched_at: '2026-06-28T22:44:11.886536+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE -  MP-1.171/2023 - Nova forma de cálculo de IRRF
  no cálculo da folha
type: support-article
updated_at: '2025-05-12T13:03:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14657002500631-RH-Linha-Protheus-GPE-MP-1-171-2023-Nova-forma-de-c%C3%A1lculo-de-IRRF-no-c%C3%A1lculo-da-folha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15272745211799) Tempo aproximado para leitura: **00:02:30 min****Dúvida**Nova forma de cálculo de IRRF no cálculo da folha - MP-1.171/2023.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.1.33.  
  
**Solução**Efetuado a alteração no cálculo do IRRF conforme MP 1.171/2023 no roteiro da Folha, para verificar o desconto simplificado mensal (correspondente a 25% (vinte e cinco por cento) do valor máximo da faixa com alíquota zero da tabela progressiva mensal).

O sistema efetuará o cálculo do IRRF tanto no modelo de tributação completo quanto no modelo de tributação simplificado e irá gerar o desconto de IR de acordo com o modelo de tributação que for mais vantajoso ao empregado, isto é, o que tiver menor valor.

**Necessário que o ambiente já esteja configurado para a nova forma de cálculo.**

O passo a passo para configuração está disponível no link abaixo:

[RH - Linha Protheus - GPE - MP-1.171/2023 - Como configurar a nova forma de cálculo de IR no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14626756121367)

Alguns cenários de cálculo da Folha de Pagamento:

* **Cenário 1:**

Neste Exemplo 1 do cálculo da folha, o Empregado tem um salário de R$ 2.640,00 e possuí um dependente de IR cadastrado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14657272132503)

Não gerou desconto do IR, devido ao cálculo no modelo de tributação simplificado ser mais vantajoso:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14657382124695)

**Conferência modelo simplificado:** R$ 2.640,00 - R$ 528,00 [dedução simplificada] = R$ 2.112,00, que é o limite da faixa de isenção.

**Conferência modelo completo descartado:** R$ 2.640,00 - R$ 219,85 [INSS] - 189,59 [dependente] = R$ 2.230,56 \* 7,5% - R$ 158,40 [dedução faixa 1]= R$ 8,89.

**Observação:**  
Nessa situação, como tenho os IDs 1913 ao 1924 cadastrados, o sistema gerou o valor de R$ 2.420,15 na verba vinculada ao ID 1913, e o valor de R$ 8,89 na verba de ID 1914.  
Além disso, também gerou o valor de R$ 528,00 referente a dedução simplificada na verba  
vinculada ao ID 1921.

* **Cenário 2:**

Neste Exemplo 2 do cálculo da folha, o Empregado tem um salário de R$ 5.000,00 e não possuí dependentes de IR:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14657408454039)

Calculou o desconto de IR no valor de R$ 354,47, apurado no modelo simplificado, pois foi mais vantajoso:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14657466335639)

**Conferência modelo simplificado:** R$ 5.000,00 - R$ 528,00 [dedução simplificada] = R$ 4.472,00 \* 22,5% = R$ 1.006,20 - R$ 651,73 [dedução faixa 3] = R$ 354,47.

**Conferência modelo completo descartado:** R$ 5.000,00 - R$ 525,90 [INSS] = R$ 4.474,10 \* 22,5% = R$ 1.006,67 - R$ 651,73 [dedução faixa 3] = R$ 354,94.

**Observação:**  
Nessa situação, o sistema gerou o valor de R$ 4.474,10 na verba vinculada ao ID 1913 e o valor de R$ 354,94 na verba vinculada ao ID 1914.  
Além disso, também gerou o valor de R$ 528,00 referente a dedução simplificada na verba  
vinculada ao ID 1921.

* **Cenário 3:**

Neste Exemplo 3 do cálculo da folha, o Empregado tem um salário de R$ 10.000,00 e possuí 02 dependentes de IR:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14657528722071)

Calculou o desconto de IR no valor de R$ 1.519,60, apurado no modelo completo, pois foi mais vantajoso:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14657483243031)

**Conferência modelo simplificado descartado:** R$ 10.000,00 - R$ 528,00 [dedução simplificada] = R$ 9.854,80 \* 27,5% = R$ 2.604,80 - R$ 884,96 [dedução faixa 4] = R$ 1.719,84.

**Conferência modelo completo:** R$ 10.000,00 - R$ 876,95 [INSS] - R$ 379,18 [dependente] = R$ 8.743,87 \* 27,5% = R$ 2.404,56 - R$ 884,96 [dedução faixa 4] = R$ 1.519,60.

**Observação:**  
Nessa situação, o sistema gerou o valor de R$ 10.000,00 na verba vinculada ao ID 1913 e o valor de R$ 1.719,84 na verba vinculada ao ID 1914.  
Além disso, também gerou o valor de R$ 528,00 referente a dedução simplificada na verba  
vinculada ao ID 1921.

**Saber Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[https://](https://tdn.totvs.com/pages/releaseview.action?pageId=756458638)[Documentação Técnica](https://tdn.totvs.com/pages/releaseview.action?pageId=756458638)

[https://](https://suporte.totvs.com/portal/p/10098/download)[Link para download do pacote](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA)

[RH - Linha Protheus - GPE - MP-1.171/2023 - Como configurar a nova forma de cálculo de IR no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14626756121367)

[Espaço Fiscal - Totvs](https://www.totvs.com/blog/fiscal-clientes/novo-calculo-de-imposto-de-renda/)

[DOU - MEDIDA PROVISÓRIA nº 1.171, de 30 de ABRIL de 2023](https://www.in.gov.br/en/web/dou/-/medida-provisoria-n-1.171-de-30-de-abril-de-2023-480184173)

[FAQ da Consultoria de Segmentos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=758481181)
