---
article_id: 360033190014
category: NFe - Nota Fiscal Eletrônica
content_hash: 1042039614c5839acc69f87271096163e197a095d1321521898acada2bae3129
fetched_at: '2026-06-28T22:40:05.501816+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 929 Rejeição :
  Informado CST de diferimento sem as informações de diferimento'
type: support-article
updated_at: '2025-07-28T19:04:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033190014-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-929-Rejei%C3%A7%C3%A3o-Informado-CST-de-diferimento-sem-as-informa%C3%A7%C3%B5es-de-diferimento
---

**Dúvida**Como solucionar a rejeição abaixo ?

929 Rejeição : Informado CST de diferimento sem as informações de diferimento  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Ao transmitir nota com **Diferimento** a **critério da UF** será verificado se foram geradas todas as TAGS do grupo do **ICMS51.**

**modBC (id: N13), pRedBC (id: N14), vBC (id: N15), pICMS (id: N16), vICMSOp (id: N16a), pDif (id: N16b), vICMSDif (id: N16c), vICMS (id: N17)**

* Por isso, é necessário verificar se foi configurado corretamente no sistema a nota de diferimento:

* **No Protheus há 7 tipos de configuração de ICMS diferido conforme o link abaixo:**

*[Clique Aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=654111155)*

Se utilizada opção:

* Exemplo de XML **Tipo 1**  **parcialmente** diferido:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042531134)

* **Diferimento com FECP**

**![Diferimento_parcial_1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408801664791)**

* Exemplo de XML **Tipo 1**  **100 por cento** diferido:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043702934)

![20201201_121133.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360098806434)

* Os campos **D2\_PICM e CD2\_ALIQ** devem estar preenchidos e ter o mesmo conteúdo.

* Os campos **FT\_VOPDIF e FT\_ICMSDIF** devem estar preenchidos e ter o mesmo conteúdo.

* O campo **CD2\_BC** deve estar preenchido.

* **Diferimento com FECP:**

![diferimento_1_100_porcento.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408801601303)

Se utilizada opção:

* Exemplo de XML **Tipo 3 100 por cento**  diferido:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043376553)

* Os campos **D2\_PICM e CD2\_ALIQ** devem estar preenchidos e ter o mesmo conteúdo.

* Os campos **FT\_VOPDIF e FT\_ICMSDIF** devem estar preenchidos e ter o mesmo conteúdo.

* O campo **CD2\_BC** deve estar preenchido.

* **Diferimento com FECP**

![op__o_3_diferido_100.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408793785111)

* **Tipo 4**ao utilizar gera rejeição **610:**

***Importante: O tipo 4 foi criado antes da NFe, logo ao utilizar essa opção, ao transmitir a nota fiscal, pode acontecer erros, pois a soma dos itens não será igual ao total da NFe, uma vez que o ICMS diferido é somado apenas ao total da nota fiscal.***

* Exemplo de XML **Tipo 5 esse tipo não é utilizado o CST 51 e sim CST10 uma configuração especifica para UF de PR:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042531794)

* **Diferimento com FECP**

![diferimento_5_com_ST.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408793633175)

* Exemplo de XML **Tipo 6****100 por cento**  diferido:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043385773)**

* **Diferimento com FECP**

**![diferimento_6_100.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408793945879)**

* **Parâmetro:**

Para gerar as TAGS do grupo do diferimento o parâmetro MV\_ART186= .F.

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042541894)**

**Ao diferir 100 por cento do ICMS**pode ser gerado **de duas formas o XML destacando o grupo completo ou não.**

O que determina como será gerado o XML é o parâmetro **MV\_ART186**

**1º Forma  
  
Para gerar as TAGS do grupo do diferimento o parâmetro MV\_ART186= .F.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360042541894)  
  
  
Para gerar como a forma 2:  
  
MV\_ART186 = .T.**Para as UFs que validam a **rejeição 929 pode ser utilizado apenas 1º Forma**

* **Importante:**

O Danfe é um espelho do XML se gerado como a **1º Forma**é destacado**alíquota, base e valor do ICMS**a**2º Forma não é destacado alíquota, base e valor do ICMS.**

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042529934)**

**Saiba mais:**

Quando for nota para UF do RJ para atender a resolução 13 a opção do diferimento que deve ser utilizada é a 7 conforme o link abaixo:

[MP - FIS - Configuração do calculo para o ICMS DIFERIDO Resolução SEFAZ 13/2019 RJ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026830373)

* Para gerar diferimento com FECP conforme a **nota técnica 2020.005,** realizar as atualizações do link abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714)

* Configurar conforme **o link abaixo:**

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como gravar os campos CD2\_VFCPDI e CD2\_VFCPEF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408539014935)

* **Exemplo do XML** :

![VFCPEFET.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4409045280151)
