---
article_id: 36242064183319
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: cf19aee7bffed618305931bc1ad84ae69396ccaf6bc8964ca21179a376e2cb79
fetched_at: '2026-06-28T22:39:15.784059+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar o
  cálculo do CBS/IBS Regular cClasstrib 200022?
type: support-article
updated_at: '2026-04-10T20:18:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36242064183319-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-c%C3%A1lculo-do-CBS-IBS-Regular-cClasstrib-200022
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36242064063895) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como configurar o cálculo do CBS/IBS Regular cClasstrib 200022?  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - FIS - a partir da release 12.1.2310  
  
**Solução**  
**A configuração apresentada abaixo é um exemplo, que poderá servir como base para a criação do cenário específico da sua empresa.**

**Recomenda-se validar junto à sua equipe Fiscal ou Contábil a memória de cálculo que deverá ser aplicada às suas operações.**

Inicialmente deve ser verificado o cClassTrib que será utilizado nesta operação, pois poderá ter variações na configuração da Regra de Alíquota. Segue o link com maiores informações:

[Classificação Tributária](https://dfe-portal.svrs.rs.gov.br/Cff/ClassificacaoTributaria)

O cClassTrib 200022 e 2000024 utilizado é um exemplo de IBS e CBS Regular, porém pode ser utilizado outro código que se enquadra do IBS/CBS Regular.

Exemplo: 200022

Para o calculo correto do IBS e CBS Regular, deve possuir os seguintes tributos:

* IBS Municipal
* IBS Estadual
* CBS Federal
* IBS Municipal Regular
* IBS Estadual Regular
* CBS Regular

Segue abaixo a configuração:

## Tributos

CBSREG - CBS FEDERAL REGULAR

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36242064068887)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36242064070679)

IBSERG - IBS ESTADUAL REGULAR

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36242049112855)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36242064076439)

IBSMRG - IBS MUNICIPAL REGULAR

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36605311205783)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36242064082711)

CBSFED - CBS FEDERAL

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36493516720663)

IBSEST - IBS ESTADUAL

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36493516721303)

IBSMUN - IBS MUNICIPAL

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36493516723095)

## Perfil de Produto

Criar um Perfil de produto e incluir TODOS no campo Cód. Produto.

Todos os produtos serão considerados nesse perfil.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36242064087959)

## Perfil de Operação

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36886569721879)

## Perfil de Participante

Criar um Perfil de Participante e incluir TODOS os Fornecedores e Cliente.

No campo Participante digite a palavra TODOS e no campo Loja ZZ ou quantidade caracteres que possua em seu ambiente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36242049137815)

## Perfil de Origem/Destino

Utilizar o Perfil 000002 - Todas as UFS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36242064101527)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36242049141911)

### **Regra de Base de Cálculo para todos os impostos**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36886562744087)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36886562745879)

### **Regra de Aliquota -  para todos os impostos**

**Na Regra de Alíquota utilizar a opção 04 - Alíquota Informada Manualmente no campo Valor Origem.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36886562746647)

### **Regra de Escrituração -  para todos os impostos**

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importar a tabela cClassTrib-IBS/CBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34662420522391-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-importar-a-tabela-cClassTrib-IBS-CBS-no-Configurador-de-Tributos)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36886569728023)

## Regra de Cálculo - Documentos Fiscais

IBSEST, IBSMUN, CBSFES, CBSREG, IBSERG e IBSMRG  - TODOS IGUAIS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36886562759575)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36886562761111)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36886569732119)

## Calculo apresentado no Pedido de venda - Venda a AM

Venda Hibrida pelo TES

Valor da mercadoria= 1000,00

Base de calculo do ICMS = 1000,00- 16,50-76,00 = 907,50\*7% = 63,53

Base de calculo do PIS/Cofins = 1000,00

1000,00\*1,65% = 16,50

1000,00\*7,6% = 76,00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36886569733399)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36886562765719)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36886569736343)

### Como é gravado na CJ3:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36886569737879)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36886562778647)

Para a transmissão precisa da configuração do parametro

* Por padrão MV\_CSTGXML vem com os seguintes CST: **000/200/210/220/510/550/830**
* Caso deseja gerar o grupo de IBS/CBS para outro CST que não esteja na lista, basta informar um CST ao final da lista separando-os cada CST por uma barra "/". Por exemplo, o CST 222, ficando o parâmetro assim: 000/200/210/220/510/550/830**/222**

  [Documentação do parâmetro MV\_CSTGXML](https://tdn.totvs.com/pages/viewpage.action?pageId=1011566715)

Atualizações do TSS de acordo com o kcs

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária – Nota Técnica 2025.002 v.1.10, v1.20 e V1.30. IBS - CBS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10-v1-20-e-V1-30-IBS-CBS)

Transmissão

<ICMS>

<ICMS40>

<orig>**0**</orig>

<CST>**40**</CST>

<vICMSDeson>**63.53**</vICMSDeson>

<motDesICMS>**7**</motDesICMS>

<indDeduzDeson>**1**</indDeduzDeson>

</ICMS40>

</ICMS>

<PIS>

<PISNT>

<CST>**06**</CST>

</PISNT>

</PIS>

<COFINS>

<COFINSNT>

<CST>**06**</CST>

</COFINSNT>

</COFINS>

<IBSCBS>

<CST>**200**</CST>

<cClassTrib>**200022**</cClassTrib>

<gIBSCBS>

<vBC>**0**</vBC>

<gIBSUF>

<pIBSUF>**0**</pIBSUF>

<gDevTrib>

<vDevTrib>**0**</vDevTrib>

</gDevTrib>

<gRed>

<pRedAliq>**100.0000**</pRedAliq>

<pAliqEfet>**0**</pAliqEfet>

</gRed>

<vIBSUF>**0**</vIBSUF>

</gIBSUF>

<gIBSMun>

<pIBSMun>**0**</pIBSMun>

<gDevTrib>

<vDevTrib>**0**</vDevTrib>

</gDevTrib>

<gRed>

<pRedAliq>**100.0000**</pRedAliq>

<pAliqEfet>**0**</pAliqEfet>

</gRed>

<vIBSMun>**0**</vIBSMun>

</gIBSMun>

<vIBS>**0**</vIBS>

<gCBS>

<pCBS>**0**</pCBS>

<gDevTrib>

<vDevTrib>**0**</vDevTrib>

</gDevTrib>

<gRed>

<pRedAliq>**100.0000**</pRedAliq>

<pAliqEfet>**0**</pAliqEfet>

</gRed>

<vCBS>**0**</vCBS>

</gCBS>

<gTribRegular>

<CSTReg>**200**</CSTReg>

<cClassTribReg>**200022**</cClassTribReg>

<pAliqEfetRegIBSUF>**0**</pAliqEfetRegIBSUF>

<vTribRegIBSUF>**0**</vTribRegIBSUF>

<pAliqEfetRegIBSMun>**0**</pAliqEfetRegIBSMun>

<vTribRegIBSMun>**0**</vTribRegIBSMun>

<pAliqEfetRegCBS>**0**</pAliqEfetRegCBS>

<vTribRegCBS>**0**</vTribRegCBS>

</gTribRegular>

</gIBSCBS>

</IBSCBS>

</imposto>

<infAdProd>**Valor do ICMS abatido: R$ 63.53 ( 7% sobre R$ 1000.00 ).**</infAdProd>

<vItem>**843.97**</vItem>

</det>

<total>

Documentações relacionadas:  
[Escrita Fiscal - Reforma Tributaria - CBS e IBS](https://centraldeatendimento.totvs.com/hc/pt-br/sections/33305945453079-Escrita-Fiscal-Reforma-Tributaria-CBS-e-IBS)
