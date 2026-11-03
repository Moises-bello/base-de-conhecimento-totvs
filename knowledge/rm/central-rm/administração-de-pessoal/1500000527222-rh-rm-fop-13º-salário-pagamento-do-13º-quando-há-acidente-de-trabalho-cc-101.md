---
article_id: 1500000527222
category: Administração de Pessoal
content_hash: e37e5dee63cdf2112674989ea083d269b8b89d056c5505c099cb65a6eeb8cd9b
fetched_at: '2026-06-28T22:47:02.214176+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: 'RH - RM - FOP - 13º Salário: Pagamento do 13º quando há acidente de trabalho
  (CC 101)'
type: support-article
updated_at: '2021-06-15T18:15:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000527222-RH-RM-FOP-13%C2%BA-Sal%C3%A1rio-Pagamento-do-13%C2%BA-quando-h%C3%A1-acidente-de-trabalho-CC-101
---

**Dúvida**

Ao empregado afastado por acidente de trabalho por mais de 15 dias é devido o pagamento de 13º por parte da empresa?  
  
**Ambiente**

RM - Totvs Folha de Pagamento - Todas as versões  
  
**Solução**

A partir do 16º dia de afastamento a responsabilidade pelos pagamentos ao empregado é da Previdência Social, inclusive o 13º Salário. Sendo assim, será o mesmo comportamento do afastamento por Previdência. Porém, a grande diferença, é que quando o funcionário é afastado por acidente de trabalho, a Empresa continua sendo responsável pelo recolhimento do FGTS do 13º, assim como deverá ser feito via RM.

Após efetuar o evento da 1ª e 2ª parcela ao funcionário, deverá lançar no envelope o evento de código de cálculo 101- 13º Pago pela Previdência. Esse deve ser do tipo de desconto e estornar INSS 13º, e ainda deverá ser informado qual o valor pago pela Previdência.

[Código de Cálculo 101 - 13º Pago pela Previdência](https://tdn.totvs.com/pages/releaseview.action?pageId=452718489)

Desconto tipo valor. Neste código de cálculo, o usuário deverá informar o valor pago de 13º salário aos funcionários afastados por acidente de trabalho. O valor informado neste código de cálculo será deduzido da base de calculo do 13º salário para o cálculo do INSS. Portanto, este evento deverá **Estornar Cálculo INSS 13 º Salário,** pois se não irá descontar duas vezes do funcionário.

O evento de desconto não deverá estornar FGTS 13º , pois dessa forma, ao gerar a SEFIP, será levado a base de FGTS para recolhimento.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000580521/mceclip2.png)  
  
**Atenção:**

* O evento com este código de cálculo deve ser lançado no movimento antes do lançamento do 13º salário.
* Caso a Previdência tenha pago a menor o 13º, será responsabilidade da empresa em pagar a Diferença e o Recolhimento do FGTS 13º será do valor total pago pela empresa.
