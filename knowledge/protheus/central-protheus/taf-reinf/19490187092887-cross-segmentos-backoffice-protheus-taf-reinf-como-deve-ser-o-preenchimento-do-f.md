---
article_id: 19490187092887
category: TAF - REINF
content_hash: e1f1e92fe5b09f4e67fe6ae6424a321142b681a280c20211ea961f340207bc49
fetched_at: '2026-06-28T22:41:33.640786+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como deve ser o preenchimento
  do Fornecedor Exterior para a Reinf?
type: support-article
updated_at: '2024-08-07T18:30:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19490187092887-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-deve-ser-o-preenchimento-do-Fornecedor-Exterior-para-a-Reinf
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19490174766487) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Quais campos devem ser preenchidos no cadastro do Participante no TAF, quando se tratar de Fornecedor Estrangeiro, para que os eventos R-4010 ou R-4020 sejam habilitados para apuração?   
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice Linha Protheus - TOTVS Automação Fiscal - Todas as versões  
  
**Solução**

Módulo 84 > Menu atualizações > Cadastros > Fiscais > Participantes

Os campos que são validados pelo painel reinf do Fornecedor Estrangeiro são os seguintes:

**Tipo Pessoa:** 3 - Outros

![fornc1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/19490141859351)

**Id Pais Ex**: preencher com o código do País (caso se tratar de Inglaterra, preencher com **Reino Unido,** não há o país Inglaterra no layout**)**

**Indicat NIF**: preencher conforme operação

**Forma Trib**: preencher conforme operação

**Tp Pessoa EX**: preencher Com: 1 - Pessoa Física ou 2 - Pessoa Jurídica

**Rel Fonte Pg**: preencher conforme operação

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19490129160471)

Os campos correspondentes no Cadastro de Fornecedores, correspondem aos seguintes campos abaixo:  
  
**C1H\_PPES = A2\_TIPO**  
**C1H\_PAISEX = A2\_PAISEX**  
**C1H\_RELFON = A2\_BREEX**  
**C1H\_NIF = A2\_NIFEX**  
**C1H\_IDTRIB = A2\_TRBEX**  
**C1H\_PEEXTE = DKE\_PEEXTE**

**Observação**: Os Fornecedores Estrangeiros só devem ser transmitidos em conjunto com a natureza de rendimento que possuir a informação de Fornecedor Exterior, ou seja, se aquele código aceita um fornecedor estrangeiro pessoa física ou jurídica. Caso não seja respeitada essa informação, poderá ocorrer rejeições na transmissão. Mais informações, consultar o anexo **Tabelas**, do layout da Reinf: <http://sped.rfb.gov.br/arquivo/show/7185>
