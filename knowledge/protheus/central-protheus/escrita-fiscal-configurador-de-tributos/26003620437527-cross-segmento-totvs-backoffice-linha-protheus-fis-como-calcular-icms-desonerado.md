---
article_id: 26003620437527
category: Escrita Fiscal - Configurador de Tributos
content_hash: 1c2bdc68ad5068a938e3bc5ae68935c0f68089acb274f38d94aa43ba5ae74e49
fetched_at: '2026-06-28T22:39:17.119306+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como calcular ICMS
  Desonerado com base dupla no FISA170?
type: support-article
updated_at: '2026-02-11T19:22:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26003620437527-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-ICMS-Desonerado-com-base-dupla-no-FISA170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26003620416151) Tempo aproximado para leitura: 08:00**min** **Dúvida**

Como calcular **ICMS Desonerado** com base dupla no **FISA170**?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

**ICMS Desonerado**

*Art. 4º  Na hipótese de operação ou prestação com **redução de base de cálculo, o campo "Valor do ICMS desonerado" deve ser preenchido com o resultado da seguinte fórmula:***

*vICMSDeson = Preço\_NF \* (1 - (AlíqN \* (1 - pRedBC))) / (1 - AlíqN) - Preço NF*

*(...)*

[*https://appasp.economia.go.gov.br/legislacao/arquivos/Secretario/IN/IN\_1563\_2023.htm*](https://appasp.economia.go.gov.br/legislacao/arquivos/Secretario/IN/IN_1563_2023.htm)

Valor da mercadoria = 1000,00

redução de base = 40%

600,00/0,88 = 681,82

681,82\*12% = 81,82

CFOP = 5106

CST = 20

MV\_ESTADO = GO

Cliente = GO

Perfil de Produto:

![](https://totvssuporte.zendesk.com/attachments/token/DgnFnA4FWyA9cnpg0sZIBBkHf/?name=image.png)

Perfil Tributário de Operação selecione 000050 padrão do sistema:

![](https://totvssuporte.zendesk.com/attachments/token/NriW5lJzhSWGKDhPeMki1wo72/?name=image.png)

Perfil de Participante:

![](https://totvssuporte.zendesk.com/attachments/token/xPwQyXk06oCodcZG1Mg267F3c/?name=image.png)

Perfil Origem X destino:

![](https://totvssuporte.zendesk.com/attachments/token/66Ey9zziQ6kB73zrk1Irlpr2C/?name=image.png)

Regra de Alíquota:

![](https://totvssuporte.zendesk.com/attachments/token/J44M7CiBuphyeg4KPRpG7WSDK/?name=image.png)

Regra de Base de calculo:

![](https://totvssuporte.zendesk.com/attachments/token/rW0jgkb2zolj0a15aldzLDxLm/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/6imOnqZ73SpNtTjG8Skd7DFJr/?name=image.png)

Regra de Escrituração:

![](https://totvssuporte.zendesk.com/attachments/token/LU1jTArwT2lIQgOzzRh7UU0oN/?name=image.png)

Regra de Calculo - Documentos Fiscais:

![](https://totvssuporte.zendesk.com/attachments/token/zD288md6dvciet5nIz6cSWA0e/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/UmANvZguHZh4Bg1uCMs9CvXBy/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/OYOHBVvxkRqGakrOEAevqHGvl/?name=image.png)

TES:

![](https://totvssuporte.zendesk.com/attachments/token/vM0MZ9HaKX8K4kX1KqsWnac35/?name=image.png)

Sit trib icm = 20

Mot.Desone = 9

Lançamento do pedido de Venda:

![](https://totvssuporte.zendesk.com/attachments/token/z36FCG27Qfn5klMrJULxFhj5t/?name=image.png)

Nota fiscal Faturada:

![](https://totvssuporte.zendesk.com/attachments/token/1FuqjT04KwOFx32S0hG6FUqta/?name=image.png)

Documentação complementar:

<https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+12.1.22.10>
