---
article_id: 6790971349143
category: RH - Pensão
content_hash: ef61586ef1c866372a84132c16ac70e88418fb13bd435736d5f0dc62939847f7
fetched_at: '2026-06-28T22:43:35.164163+00:00'
product: protheus
section_id: 360004995674
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar o cálculo da pensão na folha
  de pagamento quando há desconto de pensão no adiantamento
type: support-article
updated_at: '2025-04-16T13:25:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6790971349143-RH-Linha-Protheus-GPE-Como-parametrizar-o-c%C3%A1lculo-da-pens%C3%A3o-na-folha-de-pagamento-quando-h%C3%A1-desconto-de-pens%C3%A3o-no-adiantamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24899539531927) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como parametrizar o cálculo da pensão na folha de pagamento quando há desconto de pensão no adiantamento?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Para que o desconto da pensão na folha de pagamento fique correto quando também há desconto de pensão no adiantamento, a **verba de ID 0007- Desconto Adiantamento** deve ficar com **SIM** para pensão na aba Incidências, então entre na rotina de Verbas pelo caminho **Atualizações >Definições de Cálculo >Verbas (GPEA040)** e faça o ajuste conforme abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6790906877591)  
  
E para os funcionários que recebem adiantamento e tem desconto de pensão somente na folha de pagamento, deverá ser informada todas as verbas que fazem base para a pensão no cadastro de beneficiários, excluindo a verba de desconto de adiantamento, assim o cálculo ficará correto.

Entre na rotina de Beneficiários pelo caminho **Atualizações >Funcionários >Beneficiários (GPEA280)**, e no campo **Verb. Bs. Calc** informe **todas as verbas** que fazem base para a pensão do funcionário:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6790967735831)

**Saiba mais:**

[RH - Pensão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004995674-RH-Pens%C3%A3o)
