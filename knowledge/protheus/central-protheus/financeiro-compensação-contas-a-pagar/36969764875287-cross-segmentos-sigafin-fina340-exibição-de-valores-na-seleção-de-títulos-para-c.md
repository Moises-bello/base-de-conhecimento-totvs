---
article_id: 36969764875287
category: Financeiro - Compensação Contas a Pagar
content_hash: f112cec767364b7cdb24c56a82080966fdd50d1c58b9d39b78075d751c8e485f
fetched_at: '2026-06-28T22:37:33.667510+00:00'
product: protheus
section_id: 35057559197335
source: central-protheus
title: Cross Segmentos – SIGAFIN – FINA340 - Exibição de valores na seleção de títulos
  para compensação (PA sem impostos x NF com impostos na baixa)
type: support-article
updated_at: '2025-12-12T12:55:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36969764875287-Cross-Segmentos-SIGAFIN-FINA340-Exibi%C3%A7%C3%A3o-de-valores-na-sele%C3%A7%C3%A3o-de-t%C3%ADtulos-para-compensa%C3%A7%C3%A3o-PA-sem-impostos-x-NF-com-impostos-na-baixa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36969781086231) Tempo aproximado para leitura: **00:05min**  
  
**Dúvida**  
FINA340 - Exibição de valores na seleção de títulos para compensação (PA sem impostos x NF com impostos na baixa)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Financeiro - Todas as versões]  
  
**Cenário**

* Existe um título do tipo **NF**, no valor de **R$ 10.000,00**, configurado para **gerar imposto de R$ 150,00 somente no momento da baixa**.
* Existe também um título do tipo **PA**, no valor de **R$ 10.000,00**, configurado para **não gerar impostos**.

**Solução:**

Ao selecionar o título do tipo **NF** e clicar em **Compensar**, a rotina **FINA340** exibirá o valor de **R$ 10.000,00** na tela de marcação.  
Isso ocorre porque **o imposto de R$ 150,00 ainda não foi calculado**, já que a NF está parametrizada para gerar a retenção somente **na baixa**.

Portanto, a tela apresentará:

* **Valor apresentado para compensação:** R$ 10.000,00  
  *(o valor bruto da NF)*

No entanto, ao **finalizar a compensação**, o Protheus executa o cálculo da retenção e aplica:

* **Valor líquido da NF:** R$ 10.000,00 – R$ 150,00 = **R$ 9.850,00**
* **Valor efetivamente compensado:** **R$ 9.850,00**
* **Imposto gerado na baixa:** **R$ 150,00**

Assim, mesmo que a tela exiba o valor de **R$ 10.000,00**, a compensação final utiliza o **valor líquido de R$ 9.850,00**, conforme regra do módulo Financeiro.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/36969764857623)](https://centraldeatendimento.totvs.com/hc/article_attachments/36969764857623)[![](https://centraldeatendimento.totvs.com/hc/article_attachments/36969781087895)](https://centraldeatendimento.totvs.com/hc/article_attachments/36969781087895)[![](https://centraldeatendimento.totvs.com/hc/article_attachments/36969781089687)](https://centraldeatendimento.totvs.com/hc/article_attachments/36969781089687)

**Saiba mais:**

[FINA340 - Parâmetros na Compensação PA X NF quando há retenção na baixa nos impostos PCC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026180471-MP-SIGAFIN-FINA340-Par%C3%A2metros-na-Compensa%C3%A7%C3%A3o-PA-X-NF-quando-h%C3%A1-reten%C3%A7%C3%A3o-na-baixa-nos-impostos-PCC)

[Compensação contas a pagar - FINA340 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=504794483)
