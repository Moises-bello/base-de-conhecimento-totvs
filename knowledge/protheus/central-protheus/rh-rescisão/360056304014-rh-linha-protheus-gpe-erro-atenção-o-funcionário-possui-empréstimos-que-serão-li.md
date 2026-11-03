---
article_id: 360056304014
category: RH - Rescisão
content_hash: c3bb3dbb348595fe86d24a89631ca836496feb23c5316d06354d1561e68f4af6
fetched_at: '2026-06-28T22:43:51.039454+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE -  Erro: Atenção o funcionário possui empréstimo(s)
  que serão liquidados parcialmente ou NÃO serão liquidados pois o saldo devedor dos
  mesmos ultrapassa de 30% sobre o liquido da Rescisão. Verifique os Lançamentos Futuros'
type: support-article
updated_at: '2024-09-23T19:24:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056304014-RH-Linha-Protheus-GPE-Erro-Aten%C3%A7%C3%A3o-o-funcion%C3%A1rio-possui-empr%C3%A9stimo-s-que-ser%C3%A3o-liquidados-parcialmente-ou-N%C3%83O-ser%C3%A3o-liquidados-pois-o-saldo-devedor-dos-mesmos-ultrapassa-de-30-sobre-o-liquido-da-Rescis%C3%A3o-Verifique-os-Lan%C3%A7amentos-Futuros
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26570604987543)***Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Por que o sistema apresenta o erro "Atenção o funcionário possui empréstimo(s) que serão liquidados parcialmente ou NÃO serão liquidados pois o saldo devedor dos mesmos ultrapassa de 30% sobre o liquido da Rescisão. Verifique os Lançamentos Futuros" ao calcular rescisão complementar?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097863873)**

O erro é apresentado porque o empréstimo foi liquidado em calculo de folha de pagamento, porém a verba de desconto consignado não possui o campo RV\_EMPCONS.

Para resolução é necessário habilitar o campo RV\_EMPCONS via Configurador e preencher o campo no acumulado.  
  
**Campo Cadastro Verba:**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097864773)**

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
