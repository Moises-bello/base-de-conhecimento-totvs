---
article_id: 360044394153
category: NFe - Nota Fiscal Eletrônica
content_hash: 0c86313981880937bff1789105f4438d4da22c63dd9ecd0dd2879165573c46d4
fetched_at: '2026-06-28T22:40:03.192464+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  351 Rejeição :
  Valor do ICMS da Operação no CST=51 difere do produto BC e Alíquota'
type: support-article
updated_at: '2025-07-25T18:56:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044394153-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-351-Rejei%C3%A7%C3%A3o-Valor-do-ICMS-da-Opera%C3%A7%C3%A3o-no-CST-51-difere-do-produto-BC-e-Al%C3%ADquota
---

**Dúvida**Como corrigir 351 - Rejeição : Valor do ICMS da Operação no CST=51 difere do produto BC e Alíquota?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* É necessário verificar se foi configurado corretamente no sistema a **nota de diferimento:**

* **No Protheus há 7 tipos de configuração de ICMS diferido conforme o link abaixo:**

*[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=654111155)*

Se utilizada opção:

* Exemplo de XML **Tipo 1**  **parcialmente** diferido:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24154882325655)

* **Diferimento com FECP**

**![Diferimento_parcial_1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/24154882334743)**

* Exemplo de XML **Tipo 1**  **100 por cento** diferido:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24154882342039)

![20201201_121133.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24154914580887)

* Os campos **D2\_PICM e CD2\_ALIQ** devem estar preenchidos e ter o mesmo conteúdo.

* Os campos **FT\_VOPDIF e FT\_ICMSDIF** devem estar preenchidos e ter o mesmo conteúdo.

* O campo **CD2\_BC** deve estar preenchido.

* **Diferimento com FECP:**

![diferimento_1_100_porcento.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/24154914587927)

Se utilizada opção:

* Exemplo de XML **Tipo 3 100 por cento**  diferido:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24154882360855)

* Os campos **D2\_PICM e CD2\_ALIQ** devem estar preenchidos e ter o mesmo conteúdo.

* Os campos **FT\_VOPDIF e FT\_ICMSDIF** devem estar preenchidos e ter o mesmo conteúdo.

* O campo **CD2\_BC** deve estar preenchido.

* **Diferimento com FECP**

![op__o_3_diferido_100.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/24154914599959)

* **Tipo 4**ao utilizar gera rejeição **610:**

***Importante: O tipo 4 foi criado antes da NFe, logo ao utilizar essa opção, ao transmitir a nota fiscal, pode acontecer erros, pois a soma dos itens não será igual ao total da NFe, uma vez que o ICMS diferido é somado apenas ao total da nota fiscal.***

* Exemplo de XML **Tipo 5 esse tipo não é utilizado o CST 51 e sim CST10 uma configuração especifica para UF de PR:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24154914605591)

* **Diferimento com FECP**

![diferimento_5_com_ST.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/24154914614679)

* Exemplo de XML **Tipo 6****100 por cento**  diferido:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24154882391959)**

* **Diferimento com FECP**

**![diferimento_6_100.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/24154882401687)**

* **Parâmetro:**

Para gerar as TAGS do grupo do diferimento o parâmetro **MV\_ART186= .F.**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24154882406039)**

**Ao diferir 100 por cento do ICMS**pode ser gerado **de duas formas o XML destacando o grupo completo ou não.**

O que determina como será gerado o XML é o parâmetro **MV\_ART186** **1º Forma  
  
Para gerar as TAGS do grupo do diferimento o parâmetro MV\_ART186= .F.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24154882406039)  
  
Para gerar como a forma 2:  
  
MV\_ART186 = .T.**Para as UFs que validam a **rejeição 929 pode ser utilizado apenas 1º Forma**

Quando for nota para UF do RJ para atender a resolução 13 a opção do diferimento que deve ser utilizada é a 7 conforme o link abaixo:

[MP - FIS - Configuração do calculo para o ICMS DIFERIDO Resolução SEFAZ 13/2019 RJ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026830373)

* Para gerar diferimento com FECP conforme a **nota técnica 2020.005,** realizar as atualizações do link abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714)

* Configurar conforme **o link abaixo:**

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como gravar os campos CD2\_VFCPDI e CD2\_VFCPEF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408539014935)

* **Exemplo do XML** :

![VFCPEFET.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/24154914641303)

* **Importante:**

O Danfe é um espelho do XML se gerado como a **1º Forma**é destacado**alíquota, base e valor do ICMS**a**2º Forma não é destacado alíquota, base e valor do ICMS.**

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060133073)**
