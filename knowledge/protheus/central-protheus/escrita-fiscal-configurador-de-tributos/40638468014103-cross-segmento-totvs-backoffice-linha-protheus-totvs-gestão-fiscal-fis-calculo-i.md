---
article_id: 40638468014103
category: Escrita Fiscal - Configurador de Tributos
content_hash: 896d00717fe7d37076269d86d0f37201d042b60a35cecbf876d2bde68b37bba4
fetched_at: '2026-06-28T22:39:17.582195+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  FIS - Calculo ICMS ST Pauta ou MVA (Configurador de Tributos)?
type: support-article
updated_at: '2026-05-25T18:01:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40638468014103-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-FIS-Calculo-ICMS-ST-Pauta-ou-MVA-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40638467997207) Tempo aproximado para leitura:  10:00 **min**  
  
**Dúvida**  
Calculo ICMS ST Pauta ou MVA (Configurador de Tributos)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Essa documentação tem o objetivo de demonstrar uma operação de saída, onde é necessário comparar as bases de MVA e Pauta para definir qual será o valor utilizado como base de cálculo do ICMS ST

Nesse cenário, o valor de Pauta é de R$ 14,03. Quando o valor da mercadoria, multiplicado pelo percentual de MVA ( 45,52 )  for menos que o valor de Pauta (ou seja, até 14,02), o sistema deve considerar os 14,03 como base de cálculo do ICMS ST.

Agora, se o calculo for maior igual ou maior que o valor de Pauta, o sistema deve considerar o valor da mercadoria x percentual de MVA, para cálculo do ICMS ST.

Valor da Pauta = 14,03

MVA = 45,52%

ncm = 2202.9900

MV\_ESTADO = SP

Cliente = SP

Cadastro de Produtos 000070

Unidade = UN

NCM = 2202.9000

![]()![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723853468951)

Dados da configuração no Fisa170

Id Tributos

ICMS

ICMSST

Cadastro de Regra de NCM

ICMS ST - MVA

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723853474967)![]()

ICMS ST - PAUTA

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40638467998359)

ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723865972503)![]()

#### **ICMS**

Regra de Base de Calculo - ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723865974679)![]()

Regra de Alíquota

Formula = manual

I:ALIQ\_NCM

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723865976087)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723853486487)![]()

Regra de escrituração = CST10

Incidência = tributado

Total da NF = sem ação

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723865980951)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723865983255)![]()![]()

Regra de Calculo Documentos Fiscais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723853492887)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723865987479)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723853495959)![]()![]()![]()

Origem x destino 000002 = todas as UFS

Participantes = TODOS os clientes

Operação = 5401/6401

Produto = 000070

#### **PAUTA**

Regra de Base de calculo

Formula manual

 O:QUANTIDADE \* I:PAUTA

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723853497751)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723853498391)![]()

![]()

Não tem regra de base de calculo, pois entra como base auxiliar no calculo do ICMS ST

#### **ICMS ST**

Regra de base de calculo ICMS ST

Formula = manual

O:VAL\_MERCADORIA \* I:MVA

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723865995287)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723865997975)![]()![]()

Regra de Alíquota

Formula = manual

 I:INDICE\_AUXILIAR\_MVA

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723866000023)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723853505559)![]()![]()

Regra de escrituração

Incidência = tributado

CST = 10

total da NF = 6

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723853506327)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723866006679)![]()![]()

Regra de Calculo Documentos fiscais - com o uso da base de calculo auxiliar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723866008343)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723853514647)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723866011031)

Perfis os mesmos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723853519895)![]()![]()![]()

Deduzir o icms do valor do ICMS ST

![]()

IBS/CBS

cClasstrib = 000001

<https://tdn.totvs.com/pages/releaseview.action?pageId=1025239075>

1a) Pedido de Vendas valor inferior a pauta

Valor da mercadoria = 9,88

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723853523479)![]()

Transmissão

CMS>

<ICMS10>

<orig>**0**</orig>

<CST>**10**</CST>

<modBC>**3**</modBC>

<vBC>**9.88**</vBC>

<pICMS>**7.0000**</pICMS>

<vICMS>**0.69**</vICMS>

<modBCST>**5**</modBCST>

<vBCST>**14.38**</vBCST>

<pICMSST>**17.0000**</pICMSST>

<vICMSST>**1.75**</vICMSST>

</ICMS10>

2a) Pedido de Vendas valor da mercadoria maior que o valor da Pauta

Valor da mercadoria = 15,00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723866016535)![]()

ICMS10>

<orig>**0**</orig>

<CST>**10**</CST>

<modBC>**3**</modBC>

<vBC>**15.00**</vBC>

<pICMS>**18.0000**</pICMS>

<vICMS>**2.70**</vICMS>

<modBCST>**5**</modBCST>

<vBCST>**21.83**</vBCST>

<pICMSST>**18.0000**</pICMSST>

<vICMSST>**1.23**</vICMSST>

</ICMS10>

</ICMS>

Todos os impostos calculados pelo Fisa170, são gravados na CJ3/F2D/CD2

Boletim

<https://tdn.totvs.com/pages/releaseview.action?pageId=976153553>
