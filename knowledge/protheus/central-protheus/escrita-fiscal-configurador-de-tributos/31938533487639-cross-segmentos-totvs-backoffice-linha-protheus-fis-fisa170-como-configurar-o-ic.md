---
article_id: 31938533487639
category: Escrita Fiscal - Configurador de Tributos
content_hash: dcd3efc8423edf49f5ef0513ea7e6950522bb2a9bf500961034f5a710d2cc3bb
fetched_at: '2026-06-28T22:39:17.757981+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 - Como configurar
  o ICMS ST com FECP ST no Configurador de Tributos?
type: support-article
updated_at: '2025-11-03T17:52:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31938533487639-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-configurar-o-ICMS-ST-com-FECP-ST-no-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31938533423383) Tempo aproximado para leitura: 00:10**min**  
  
**Dúvida**  
Como configurar o ICMS ST com FECP ST no fisa170?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)   
  
**Solução**

O NCM sujeito a incidencia do calculo do ICMSST deve o ICMS configurado com a CST10, para gerar o XML de forma correta

A figura abaixo mostra o trecho do XML, correspondente ao grupo **Grupo N03 – Grupo Tributação do ICMS = 10**.

![Trecho de um arquivo XML de NF-e - ICMS ST na Nota Eletrônica](https://dhg1h5j42swfq.cloudfront.net/2021/06/05125016/xml.png)

**Exemplo de uma venda interna com cálculo de ICMS ST e FECP ST**

MV\_ESTADO = MG

Cliente = MG

NCM = 33059000 - cest 2002200

Alíquota ICMS = 25%

Alíquota ICMS ST = 25%

FECP ST = 2%

CFOP = 5910 - Remessa em Bonificação

**Configurações Fisa170:**

Cadastro de Regra NCM

ICMS - alíquota = 25%

ICMS ST - alíquota = 25%

FCPST = 2%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938533428119)

ICMS ST - Margem do valor agregado - CEST 2002200 - MVA =34,55 e FECP ST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938548459799)

Perfis

1ª) Perfil de Produtos = 000013

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938548461719)

No sb1 - cadastro de Produtos, precisa ter o NCM e a origem configurados

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938548465559)

 2ª) Perfil de Operação - criei um especifico para atender ao CFOP 5910

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938533434391)

3ª) Perfil de Participante

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938548467351)

4ª) Perfil de origem x destino

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938533436439)

**Regra de Base de cálculo do ICMS**

valor da mercadoria + frete

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938533437591)

**Regra de Base de cálculo do ICMS ST e do FECP ST**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938533438871)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938548475159)

**Regra de Alíquota**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938548476951)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938548479895)

**Regra de Escrituração**

ICMS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938533446935)

ICMS ST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938548482711)

**Regra de Cálculo Documentos Fiscais – ICMS**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938548483095)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938533448855)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938533449367)

**Regra de Cálculo Documento Fiscais - FECP ST**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938548485527)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938548486551)

PERFIS OS MESMOS

 **Regra de Cálculo Documentos Fiscais - ICMS ST**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938548487191)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938533453463)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938548490647)

PERFIS OS MESMOS

Detalhamento da formula de calculo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938533455511)

TES

CFOP = 5910

Documento de saídas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31938548493335)

Documentações

**[CFGTRIB - Configurador de Tributos](https://tdn.totvs.com.br/display/PROT/CFGTRIB+-+Configurador+de+Tributos)**

**[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=676039354)**

**[CFGTRIB - Perguntas e Respostas - Configurador de Tributos](https://tdn.totvs.com.br/display/PROT/CFGTRIB+-+Perguntas+e+Respostas+-+Configurador+de+Tributos)**

**[CFGTRIB - Boas Práticas - Guia de Utilização do Configurador de Tributos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=825324804)**
