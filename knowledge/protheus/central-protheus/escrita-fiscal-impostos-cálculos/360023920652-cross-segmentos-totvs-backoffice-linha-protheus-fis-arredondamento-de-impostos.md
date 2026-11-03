---
article_id: 360023920652
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 70f2f97d906f39d4d5e4c43ebf05b8cb603996288068f022d5e5e084c2b749d8
fetched_at: '2026-06-28T22:39:30.656622+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Arredondamento de
  Impostos
type: support-article
updated_at: '2025-11-07T20:47:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023920652-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Arredondamento-de-Impostos
---

**Dúvida**Como tratar Arredondamento de impostos no Protheus?

**Ambiente**Protheus – Fiscal – Todas as  versões  
  
**Solução**

Para tratar o arredondamento de Impostos na nota fiscal existem o parâmetro **MV\_RND\*\***, onde (\*\*) poderá ser:

**MV\_RNDIPI, MV\_RNDICM, MV\_RNDFUN, MV\_RNDISS, MV\_RNDIRF, MV\_RNDINS, MV\_RNDCOF, MV\_RNDPIS, MV\_RNDCSL, MV\_RNDPS2, MV\_RNDCF2, MV\_RNDPS3** e**MV\_RNDCF3.**

Utilizados em conjunto com o parâmetro **MV\_RNDSOBR**:

1. Sempre que o **RNDSOBR** estiver como Falso, não teremos o tratamento das sobras e consequentemente os valores serão truncados por item.
2. Quando o **RNDSOBR** estiver como Verdadeiro e o RND\*\* também como Verdadeiro, será efetuado o tratamento de arredondamento por item.
3. Quando o **RNDSOBR** estiver como Verdadeiro e o RND\*\* como falso, será efetuado o tratamento de arredondamento no total do imposto (truncando por item e considerando a sobra).
4. É preciso também validar o parâmetro **MV\_RNDPREC** que irá determinar a precisão do arredondamento:

**MV\_RNDPREC**: Indica a precisão de arredondamento dos valores de impostos das Notas Fiscais.

### Abaixo segue exemplos de como o sistema trata o arredondamento dos impostos:

Importante

![](https://tdn.totvs.com/download/attachments/697254959/EX_ARREDONDAMENTO_INSS.png?version=1&modificationDate=1657042233733&api=v2)

Para imposto de ISS existe arredondamentos definidos na norma ABNT NBR 5891/77 e na resolução 886/66 do IBGE para validação do valor de ISS enviado nas notas de serviço. Documento sobre no link abaixo;

[Arredondamento\_de\_ISS\_Padrão\_ABNT](https://tdn.totvs.com/pages/viewpage.action?pageId=446702089)

**MV\_RNDIRRF** enxergado na gravação do título de IRRF, identifica se o valor será arredondado ou truncado.  
**MV\_RNDIRF**enxergado nos cálculos de tributos por item, identifica se o valor será arredondado ou truncado, por item.

Os cálculos do IRRF acontecem em pelo menos dois momentos, na emissão de nota, e na emissão de título.  
Na Emissão de nota, os cálculos fiscais são por item, e ao final há a totalização dos valores no cabeçalho da nota, enquanto na emissão de título, o cálculo acontece sobre o valor total e não por item.

Por conta disso, pode ocorrer diferença de centavos quando os parâmetros de arredondamento de IRRF estão definidos para truncar o valor do tributo.  
O parâmetro **MV\_RNDSOBR** configurado como **.T.** ajusta a maioria das situações, porém, pode ocorrer situações específicas onde ainda haverá a diferença de 0,01 centavo do título para o somatório do tributo nos itens.

Uma alternativa para solucionar esta divergência, é manter o **MV\_RNDIRF = .F.** enquanto **MV\_RNDIRRF = .T.**Isso fará com que os valores sejam idênticos tanto na gravação do tributo por itens quanto na gravação do título. 

 Obs.: antes de efetuar qualquer alteração de configuração em produção, testes devem ser efetuados em base de homologação.

Importante

No caso do tributo IRRF há dois parâmetros de arredondamento no sistema: MV\_RNDIRRF e MV\_RNDIRF

* **SX6 -**Cadastro de Parâmetros**;**

**Link do Desenvolvimento: <https://tdn.totvs.com/display/public/PROT/ARRIMP+-+Arredondamento+de+impostos>**
