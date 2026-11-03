---
article_id: 360019535652
category: NFe - Nota Fiscal Eletrônica
content_hash: c657ed2afc473b13c633d7dc38b5b712eb6a077441355ee34ad392c27cb4d4ba
fetched_at: '2026-06-28T22:40:07.115779+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Qual situação tributária
  (CST) de ICMS que destaca o valor do imposto no XML e DANFE
type: support-article
updated_at: '2025-06-18T14:45:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019535652-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Qual-situa%C3%A7%C3%A3o-tribut%C3%A1ria-CST-de-ICMS-que-destaca-o-valor-do-imposto-no-XML-e-DANFE
---

**Dúvida**Qual situação tributária (CST) de ICMS que destaca o valor do imposto no XML e DANFE ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**Exemplo de **NÃO** destaque de **ICMS**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015384532)

* Conforme está no Manual de Orientação do contribuinte da SEFAZ, **versão 6.00, página 196.**

[Manual de Orientação do Contribuinte - versão 6.00](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=URCYvjVMIzI=)  
  
Os CST **40, 41 e 50** não possuem tags de valor do ICMS, consequentemente, o valor não irá para o DANFE, que é um espelho do XML.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015435791)  
  
1 - Para haver o destaque o ICMS deve ser calculado e além disso, no TES o campo **Sit. trib. ICMS** **(F4\_SITTRIB)** **00, 20, 51, 70, ou 90:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32896640519703)

Se utilizado o CST 51, configurar a nota conforme abaixo:

* É necessário verificar se foi configurado corretamente no sistema a **nota de diferimento:**
* **No Protheus há 7 tipos de configuração de ICMS diferido conforme o link abaixo:**

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=654111155)

**Para gerar as TAGS do grupo do diferimento o parâmetro MV\_ART186= .F.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32896633766295)**

2- Após isso, exclua a nota e gere novamente  se for utilizar o mesmo pedido digite novamente a TES para que seja alterada a situação tributária no item do produto.  
  
***Saiba Mais***Caso seja nota de devolução, além da situação tributária é necessário que o parâmetro esteja configurado conforme abaixo:  
  
**MV\_ICMDEVO = .T.*****Conforme o link abaixo:***

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Destaque de ICMS normal ou ICMS-ST na Devolução da nota](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020986011)

3- Se houver  **ICMS-ST**  só será destacado se utilizar a **situação tributária do ICMS 10, 30, 70 ou 90** Altere a situação tributária no TES no campo  **Sit. trib. ICMS** **(F4\_SITTRIB)**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32896640519703)

* **Importante:**

Caso tenha **ICMS próprio** e o **ICMS-ST o CST 30 "destaca apenas o ICMS - ST."**

4- Preencha o  campo **Agrega solid = Sim (F4\_INCSOL)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32896633767575)**

5- Após isso, exclua a nota e gere novamente  se for utilizar o mesmo pedido digite novamente a TES para que seja alterada a situação tributária no item do produto.  
  
***Saiba Mais***Caso seja nota de devolução, além da situação tributária é necessário que o parâmetro esteja configurado conforme abaixo:

***MV\_ICSTDEV = .T.******Conforme o link abaixo:***

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Destaque de ICMS normal ou ICMS-ST na Devolução da nota](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020986011)

* **Importante:**

Caso seja emitente do **Simples Nacional.**

6- Configurar o parâmetro **MV\_IMPSIMP=.T.**

![MV_IMPSIMP.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360098078593)

7- Para haver o destaque o ICMS deve ser calculado e além disso, no TES o campo  **F4\_CSOSN "Campo Cod. Sit. SN" deve estar como 101 ou 900.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32896640528791)

8- Para destacar no Danfe os campos na SF3 **(SF3->F3\_BASEICM e SF3->F3\_VALICM)** devem estar preenchidos. Para isso no **TES** deixar L. fiscal ICMS = **Tributado**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32896633771415)**

* **Saiba mais:**Caso seja diferimento realizar a configuração do link abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 929 Rejeição: Informado CST de diferimento sem as informações de diferimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033190014)

* Se os parâmetros estiverem ***corretos, CST e imposto tributado na CD2:***

 Verificar se os tamanhos dos campos estão ***corretos na SX3*** e em sua base de dados.  
  
Verificar o tamanho dos campos dentro do banco de dados utilizando o comando ***SP\_HELP (nome da tabela).***  
  
F2\_SERIE e CD2\_SERIE  
F2\_DOC  e CD2\_DOC  
F2\_CLIENTE  com CD2\_CODFOR e CD2\_CODCLI  
D2\_COD  e CD2\_CODPRO 

[Link de todos os artigos de NFe](https://centraldeatendimento.totvs.com/hc/pt-br/sections/207068528-NFe-Nota-Fiscal-Eletr%C3%B4nica)
