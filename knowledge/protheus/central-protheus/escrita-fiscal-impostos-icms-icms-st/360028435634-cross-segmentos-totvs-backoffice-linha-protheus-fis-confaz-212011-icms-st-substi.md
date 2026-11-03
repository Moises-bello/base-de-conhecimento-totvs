---
article_id: 360028435634
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: ecb44559cf6a6fb2d3ca74aa53615b103a4d836bf2650113c665e3fb2267901f
fetched_at: '2026-06-28T22:39:20.306260+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Confaz 21/2011
  ICMS-ST Substituição Tributária'
type: support-article
updated_at: '2021-07-13T17:25:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028435634--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Confaz-21-2011-ICMS-ST-Substitui%C3%A7%C3%A3o-Tribut%C3%A1ria
---

**Dúvida**Por quê o sistema está calculando ICMS-ST sem ter MVA cadastrado?  
  
 **Ambiente**Microsiga Protheus – Fiscal – A partir da versão 11.80  
  
**Solução** **Configuração ICMS-ST sem ter MVA cadastrado:**

O sistema realiza o cálculo do **ICMS-ST** sem ter **MVA** cadastrado para algumas **UFS** destinadas para operações enquadradas na Confaz 21/2011.

**TES**

Venda Pres. (**F4\_VENPRES**) **=**1=Sim; 2=Não

Campo utilizado para indicar se a Venda é Presencial ou não. Tratamento para Confaz 21/2011

Marg. Solid.(**F4\_MKPSOL**) **=**1=Nunca; 2= Configuração; 3=Sempre

Indica se o cliente é contribuinte ou não do **ICMS** em seu estado. Caso este campo esteja configurado como 2=Não, mesmo que o cliente possua Inscrição Estadual, ele será tratado como não contribuinte do **ICMS** pelo sistema, utilizando essa configuração para determinar a alíquota do **ICMS** durante o faturamento.

**CLIENTE**

Tipo do Cliente(**A1\_TIPO**) **=** F=Cons. Final; L=Produtor Rural; R=Revendedor;   S=Solidário; X=Exportação    

Tipo de Cliente: Opções Brasil (L,F,R,S,X):

F - Cons. Final; L - Produtor Rural; R - Revendedor; S - ICMS Solidário sem IPI na base; X - Exportação.

Contribuinte (**A1\_CONTRIB**) = 1=Sim; 2=Não

Indica se o cliente é contribuinte ou não do ICMS em seu estado. Caso este campo esteja configurado como 2-Não, mesmo que o cliente possua Inscrição Estadual, ele será tratado como não   contribuinte do **ICMS** pelo sistema, utilizando essa configuração para  determinar a alíquota do **ICMS** durante o faturamento.

**PARÂMETRO**

**MV\_UFPST21 =**AC/AL/AP/BA/CE/DF/ES/GO/MA/MT/PA/PB/PE/PI/SE/RN/RO/RR

Indique as UF’s destinatárias para as operações enquadradas na Confaz 21/2011.

**IMPORTANTE**

Para que o cálculo seja feito corretamente, o cliente deve ser do tipo Consumidor Final.

**Procedimento para Utilização**

1. Cadastrar um **Produto (MATA010)**.

2. Cadastrar um **TES (MATA080)** que possua os campos:

**F4\_VENPRES** igual a 2 **= Não**

**F4\_MKPSOL** igual a 1 **= Nunca**

3. A UF de destino deve estar contida no parâmetro criado pelo compatibilizador: **MV\_UFPST21**.

4. O cliente deve ser do tipo **Consumidor Final**.

Para mais informações sobre o tratamento Confaz 21/2011 ICMS-ST acessar:

<http://tdn.totvs.com/pages/releaseview.action?pageId=238029857>
