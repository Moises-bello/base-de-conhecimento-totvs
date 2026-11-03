---
article_id: 360021542851
category: Escrita Fiscal - Impostos - ISS
content_hash: 1e6ac21a64ac92febda32e3a08fc60e7da1398434554d7ab2556726350626e53
fetched_at: '2026-06-28T22:39:35.096405+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Bitributação ISS
  (FISA090)'
type: support-article
updated_at: '2021-06-17T12:14:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021542851--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Bitributa%C3%A7%C3%A3o-ISS-FISA090
---

**Dúvida**Como realizar parametrização da BI-TRIBUTAÇÃO de ISS (FISA090)?  
  
**Ambiente**Protheus - Pedido de Venda - A partir da versão 12.1.23  
  
**Solução**Funcionalidade trata do cálculo e recolhimento do ISS para o município do tomador do serviço em duplicidade com o ISS calculado no documento fiscal normalmente para recolhimento no município do prestador ou do serviço prestado, conforme local onde o ISS é devido seguindo a Lei Complementar 116/2003.

Essa bitributação ocorre em municípios que exigem um cadastramento de estabelecimentos prestadores de serviço de outros municípios, quando o prestador tem dificuldade de comprovar o local do estabelecimento. Ao não conseguir realizar o cadastro, o município em questão exige a retenção pelo tomador e recolhimento do ISS como se o prestador estivesse localizado em seu município.

Podemos separar a funcionalidade na ótica do tomador e do Prestador.

Necessidades na ótica do tomador:

* Realizar o cálculo do ISS ao entrar com o documento com a alíquota do próprio município não importando as configurações atuais do ISS
* Realizar o abatimento do ISS bitributado do título principal descontando esse ISS do valor a pagar ao seu fornecedor
* Gerar um título a recolher de ISS bitributado para o seu município.

Nesse formado é possível visualizar na nota fiscal os dois ISS, porém caso o tomador não tenha o entendimento, pode continuar tratando o ISS bitributado apenas como ISS no documento, porém ele apenas será registrar e visualizar no documento o ISS calculado e recolhido em seu município. Neste caso não é necessário utilizar os procedimentos descritos neste documento, basta configurar o cálculo do ISS normalmente com sua alíquota interna e realizar a retenção.

Necessidades na ótica do prestador que não conseguiu comprovar seu local de estabelecimento:

* Realizar o cálculo do ISS do seu município normalmente no documento fiscal, pois é o que será registrado de fato em sua prefeitura e considerado na apuração mensal
* Realizar o cálculo do ISS bitributado utilizando a alíquota do município do seu cliente
* Abater o valor do ISS bitributado do título a receber, pois seu cliente irá realizar a retenção e recolhimento.

**Para configura seu sistema, seguir passo a passo as documentações abaixo:**

Segue documentação : <http://tdn.totvs.com/pages/viewpage.action?pageId=431664696>

Acessar no menu do Módulo **Livros Fiscais (SIGAFIS)** o cadastro de **Bitributação do ISS (** **FISA090)** e configurar conforme cada caso abaixo:

 

Para recolher em seu município o ISS de prestadores de outros municípios em duplicidade com o ISS que já está no documento:

Preencher o Tipo de Configuração (Entrada/Saída), a identificação do seu município (no caso das entradas é onde será gerado o recolhimento), o prestador estabelecido em outro município e o código do ISS.

![](https://tdn.totvs.com/download/attachments/431664696/image2018-10-30_16-4-24.png?version=1&modificationDate=1540930995650&api=v2)

 

Dessa forma o sistema já identifica que quando tomar serviço deste fornecedor, seu município irá exigir o recolhimento, mesmo que o ISS tenha sido recolhido no município do prestador. Para que o cálculo seja possível ainda é necessário configurar a alíquota de ISS, e para isso basta acessar o cadastro de **Alíquotas do ISS (FISA052)**, também no módulo de **Livros Fiscais (SIGAFIS)**, conforme abaixo:

 

![](https://tdn.totvs.com/download/attachments/431664696/image2018-10-30_16-9-51.png?version=1&modificationDate=1540930995620&api=v2)

 

Neste cadastro foi informado também o fornecedor para o qual o título de recolhimento do ISS será gerado, além é claro da alíquota do ISS.

Observação: O cadastro em questão não trata apenas da Bitributação, na verdade abrange todo o ISS. Para mais informações sobre a configuração das alíquotas e utilização para o cálculo do ISS clique [aqui](https://tdn.totvs.com/x/oYNpCw).

 

 

Após este procedimento o cálculo é realizado no documento fiscal:

![](https://tdn.totvs.com/download/attachments/431664696/image2018-10-30_22-27-33.png?version=1&modificationDate=1540952853747&api=v2)

![](https://tdn.totvs.com/download/attachments/431664696/image2018-10-30_16-15-9.png?version=1&modificationDate=1540930995553&api=v2)

![](https://tdn.totvs.com/download/attachments/431664696/image2018-10-30_16-15-34.png?version=1&modificationDate=1540930995527&api=v2)

![](https://tdn.totvs.com/download/attachments/431664696/image2018-10-30_16-16-11.png?version=1&modificationDate=1540930995490&api=v2)

 

É possível perceber que o valor do ISS bitributado não não segue a configuração do ISS normal quanto sua retenção, pois entende-se que ele só é necessário quanto o município do tomador exige sua retenção, independentemente do que outro município possa ter recebido de ISS sobre o serviço.

 

Ao baixar o título devemos observar que o valor do ISS devido foi abatido do principal, e que um título a pagar ao município também foi gerado:

![](https://tdn.totvs.com/download/attachments/431664696/image2018-10-30_22-38-50.png?version=1&modificationDate=1540953530303&api=v2)![](https://tdn.totvs.com/download/attachments/431664696/image2018-10-30_22-39-13.png?version=1&modificationDate=1540953553193&api=v2)

Para cenários onde ao prestar o serviço, não possui o cadastro no município do tomador, e sofrerá a retenção mesmo sendo necessário calcular o ISS do próprio município:

 

No cadastro de **Bitributação do ISS (FISA090)** deve ser criada uma regra de cálculo para as saídas com o município para o qual é necessário realizar o cálculo informando o código do ISS. Neste exemplo um valor de ISS será calculado para o município de Madre de Deus/BA quando gerarmos um documento de saída para um cliente desse município, independentemente do ISS calculado no mesmo item para recolher em seu próprio município.

 

![](https://tdn.totvs.com/download/attachments/431664696/image2018-10-31_8-12-3.png?version=1&modificationDate=1540987924073&api=v2)

 

Vale lembrar que a alíquota de ISS para o serviço em questão no município acima cadastrado deve ser preenchida no cadastro de **Alíquotas do ISS (FISA052)** já existente no módulo **Livros Fiscais (SIGAFIS)**:

![](https://tdn.totvs.com/download/attachments/431664696/image2018-10-31_8-19-21.png?version=1&modificationDate=1540988361973&api=v2)

Observação: O cadastro em questão não trata apenas da Bitributação, na verdade abrange todo o ISS, e por isso é necessário informar inclusive qual o fornecedor para o recolhimento do ISS, pois caso em algum cenário seja necessário pagar ISS a este município o fornecedor já estará configurado. Para mais informações sobre a configuração das alíquotas e utilização para o cálculo do ISS clique [aqui](https://tdn.totvs.com/x/oYNpCw).

Para entendermos as regras da BiTributação nas notas fiscais de saída, segue abaixo alguns cases de exemplo:

Para produtos configurados com a regra de produto **LES:**

* Exemplo 1:
  + Tomador da cidade de Guarulhos;
  + Prestador da cidade de São Paulo;
  + Os campos C5\_ESTPRES (Estado Prestador) e C5\_MUNPRES (Município do Prestador) = EM BRANCO;

**Para estes casos o sistema não deverá calcular a BiTributação. Deve calcular o ISS com a alíquota do tomador;**

* Exemplo 2:
  + Tomador da cidade de Guarulhos;
  + Prestador da cidade de São Paulo;
  + Os campos C5\_ESTPRES (Estado Prestador) = "SP" e C5\_MUNPRES (Município do Prestador) = "18800" (Guarulhos);

**Para estes casos o sistema não deverá calcular a BiTributação. Deve calcular o ISS com a alíquota do tomador;**

* Exemplo 3:
  + Tomador da cidade de Guarulhos;
  + Prestador da cidade de São Paulo;
  + Os campos C5\_ESTPRES (Estado Prestador) = "SP" e C5\_MUNPRES (Município do Prestador) = "50308" (São Paulo);

**Na planilha financeira deve ser calculado ISS considerando alíquota do Prestador informada no FISA052 (Alíquota de ISS) e ISS Bitributado considerando alíquota do município do Tomador informado no FISA052 (Alíquota de ISS).Dessa forma, não haverá bitributação de ISS se o local de prestação de serviço for o município do tomador e sempre haverá bitributação se o local de prestação for o município do prestador.**

Para produtos configurados com a regra de produto **EP:**

Para os produtos configurados com o campo Exe. Servico (B1\_MEPLES) = EP, deve considerar que a prestação do serviço sempre ocorrerá no Município do Prestador, dessa forma, se o cliente está em município diferente e este está cadastrado no FISA090 (Cadastro de BiTributação) sempre será calculado ISS com alíquota do Prestador e ISS Bitributado com alíquota do Tomador.

Abaixo como o cálculo é demonstrado na planilha financeira do pedido e como a nota fiscal será gerada quando o cliente está localizado, conforme o exemplo, em Madre de Deus/BA:

![](https://tdn.totvs.com/download/attachments/431664696/image2018-10-31_8-32-3.png?version=1&modificationDate=1540989129037&api=v2)

![](https://tdn.totvs.com/download/attachments/431664696/image2018-10-31_8-33-33.png?version=1&modificationDate=1540989219267&api=v2)

![](https://tdn.totvs.com/download/attachments/431664696/image2018-10-31_8-34-5.png?version=1&modificationDate=1540989252820&api=v2)

Na **Apuração de ISS (MATA954)** apenas o ISS do seu município será considerado, neste exemplo o valor de R$ 30,00 será somado ao valor a recolher de ISS em sua apuração para recolher em seu município, já o valor de R$ 50,00 será recolhido pelo seu cliente, o tomador do serviço, no município de Madre de Deus/BA. Ao baixar o título a receber relativo a essa nota fiscal é possível perceber que foi gerado um abatimento com o ISS bitributado que será recolhido no município do seu cliente via retenção.

![](https://tdn.totvs.com/download/attachments/431664696/image2018-10-31_8-37-7.png?version=1&modificationDate=1540989429403&api=v2)
