---
article_id: 360050835113
category: Escrita Fiscal - Impostos - IPI
content_hash: 35083c6bc4d9eb6927b28592360490bf0aac7713d72c40b4b93559d3b5e268b6
fetched_at: '2026-06-28T22:39:29.021765+00:00'
product: protheus
section_id: 1500001538641
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Qual a configuração
  de IPI DE PAUTA ?
type: support-article
updated_at: '2021-07-28T13:44:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050835113-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Qual-a-configura%C3%A7%C3%A3o-de-IPI-DE-PAUTA
---

**Dúvida** Qual a configuração de IPI DE PAUTA ?

**Importante**

O IPI de pauta é um método definido pelo governo para o calculo de IPI de alguns produtos identificados pela nomenclatura comum do Mercosul ( NCM ). Este método de calculo atribui o valor do IPI pela embalagem em que o produto é comercializado, como exemplo podemos destacar: refrigerantes, água mineral, chocolates, etc...

**Obs.****Alíquota do IPI (5%) IPI de pauta  não é demostrada na planilha financeira**

**Ambiente**

Protheus - Livros Fiscais - A partir da versão 11.80

**Solução:**

Para o calculo do IPI de pauta é necessário preencher o valor do IPI no cadastro de produto  IPI de pauta ( B1\_VLR\_IPI ) ou a Exceção Fiscal quando houver mais de um valor por operação. Abaixo transcrevemos a formula de calculo do IPI de Pauta:

**Quantidade comercializada \* Valor do IPI de Pauta \* Parâmetro MV\_IPIPFAT**

**Observação**: Quando o parâmetro MV\_IPIPFAT não for definido, será assumido 1 para efeito de calculo.

**Exemplo de configuração**

**Parâmetro >** MV\_IPIPFAT = B1\_PESO

**Cadastro do Produto :**

**Aba Cadastrais  >**Peso Liquido = 1,0000

**Aba Imposto** > Campos Aliq. IPI = 5%

Campo IPI de Pauta R$ 3,75

**TES**

**Aba Imposto >** Campo IPI Bruto = L Liquido

**Evidencia após as configurações :**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077238153/mceclip4.png)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077238313/mceclip5.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076101574/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077237633/mceclip3.png)

Boletim tecnico

[https://tdn.totvs.com/pages/releaseview.action?pageId=6070582,](https://tdn.totvs.com/pages/releaseview.action?pageId=6070582)
