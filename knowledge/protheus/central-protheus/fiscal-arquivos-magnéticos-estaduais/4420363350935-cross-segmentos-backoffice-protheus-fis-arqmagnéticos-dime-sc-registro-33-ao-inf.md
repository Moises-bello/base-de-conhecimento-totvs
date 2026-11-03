---
article_id: 4420363350935
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 06c0c219d5c2bf52a13008622f23d01c4261046d507006a11381b11a2d238663
fetched_at: '2026-06-28T22:42:10.744487+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DIME SC -  "Registro
  33 - Ao informar receita "XXXX" deve ser informado o item 14199."
type: support-article
updated_at: '2022-08-17T19:40:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420363350935-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DIME-SC-Registro-33-Ao-informar-receita-XXXX-deve-ser-informado-o-item-14199
---

**Dúvida**

 Ao validar o arquivo da DIME SC é apresentado o erro abaixo:

**Exemplo com o código de receita 2496**

"Registro 33 - Ao informar receita 2496 deve ser informado o item 14199."

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420345550999/mceclip0.png)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12  
  
**Solução**

O erro ocorre devido no quadro '12' foi informado o código da Receita 2496 - ICMS - Resultante da Utilização de Crédito Presumido, dessa forma será necessário digitar o valor no Quadro 14 item 14199 - Imposto a Recolher Utilização do Crédito Presumido.

Verificar o preenchimento na Wizard do Registro Tipo 35 - Quadro 14

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420345671319/mceclip1.png)

* **Item 199 - (=) Imposto a Recolher pela Utilização do Crédito Presumido**

Este item é calculado automaticamente pelo sistema

**Exemplo:**

* **Item 050 - (=) Débito Apurado pela Apropriação Extemporânea do Crédito Presumido**

Valor informado manualmente:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420363154839/mceclip3.png)

**Item 199 - (=) Imposto a Recolher pela Utilização do Crédito Presumido**

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420363416599/mceclip10.png)

**No arquivo TXT**

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420363280407/mceclip8.png)

**Informações adicionais :**

**DIME - Declaração de ICMS e do Movimento Econômico do Estado de Santa Catarina**

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=655881026#SCDIME-Declara%C3%A7%C3%A3odeICMSedoMovimentoEcon%C3%B4micodoEstadodeSantaCatarina-RegistroTipo46(Cr%C3%A9ditosporregimeseautoriza%C3%A7%C3%B5esespeciais),relativoaoCr%C3%A9ditoinformadonoDCIP>
