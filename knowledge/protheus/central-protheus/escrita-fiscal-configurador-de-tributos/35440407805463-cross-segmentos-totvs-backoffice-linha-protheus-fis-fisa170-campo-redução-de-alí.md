---
article_id: 35440407805463
category: Escrita Fiscal - Configurador de Tributos
content_hash: 133249afa5e789c7b9644c4a10a98c70239ac277664295c3fdfd2cfce96490d1
fetched_at: '2026-06-28T22:39:17.714560+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 - Campo Redução
  de Alíquota (F28_REDALI)  no Configurador de Tributos
type: support-article
updated_at: '2025-12-09T13:53:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35440407805463-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Campo-Redu%C3%A7%C3%A3o-de-Al%C3%ADquota-F28-REDALI-no-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35440400479383) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Campo Redução de Alíquota  no Configurador de Tributos  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**  
O sistema já possui tratamento referente à redução da alíquota efetiva já está configurado no Configurador de Tributos (CFG), através do novo campo “Redução de Alíquota”.

O campo é uma nova funcionalidade e esta disponível a partir da aplicação da expedição contínua: <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1182881>

O campo Redução de Alíquota permite parametrizar o percentual de redução da alíquota nominal de um imposto, resultando em uma alíquota efetiva menor.

Esse mecanismo é utilizado para aplicar benefícios fiscais, incentivos regionais ou adequações legais, permitindo que a base de cálculo do tributo seja reduzida proporcionalmente ao percentual informado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35440400480407)

Exemplo de aplicação

**Situação:**  
Uma empresa comercializa um produto no valor de R$ 1.000,00, com alíquota original de ICMS = 18%.  
Existe um benefício fiscal que reduz a alíquota em 33,33%.

**Cálculo:**  
Alíquota Efetiva = 18% × (1 - 33,33%)  
Alíquota Efetiva = 18% × 0,6667 = **12%**  
R$ 1.000,00 × 12% = **R$ 120,00**

**Observação:**  
Sem a redução, o valor do ICMS seria **R$ 180,00**.

Help do campo: % Redução de Alíquota - Define o percentual de redução a ser aplicado sobre a alíquota original.

**Exemplo adicional:**  
Em uma operação de **R$ 1.000,00**, com alíquota de **18%**, o valor original do imposto seria **R$ 180,00**.  
Se for aplicada uma **redução de 33,33%**, o cálculo será:  
18% × (1 - 33,33%) = 18% × 0,6667 = **12%**  
Resultado: o valor do imposto a recolher será **R$ 120,00**.

Documentações relacionadas:

[CFGTRIB - Configurador de Tributos](https://tdn.totvs.com/display/PROT/CFGTRIB+-+Configurador+de+Tributos)

[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)

###
