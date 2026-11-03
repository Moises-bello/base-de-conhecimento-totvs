---
article_id: 360041173953
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: e1fd1945dbc08702d83e6cb8295cbe960499bb61a56d6c4f43ae0453a4ea4e7a
fetched_at: '2026-06-28T22:37:56.224962+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA300 - Geração do
  bloco B para os segmento J, N e O
type: support-article
updated_at: '2022-07-22T15:39:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041173953-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA300-Gera%C3%A7%C3%A3o-do-bloco-B-para-os-segmento-J-N-e-O
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00min**

**Dúvida**O sistema não está gerando no arquivo SISPAG os dados do segmento B, quando os modelos do borderôs abaixo: 

**Segmento J e J-52**

·         30 - Liquidação de títulos em cobrança no Itaú

·         31 - Pagamento de títulos em outro banco

**Segmento N**

·         16 - Pagamento de Tributos DARF

·         17 - Pagamento de Tributos GPS

·         18 - Pagamento de Tributos DARF SIMPLES

·         21 - Pagamento de Tributos DARJ

·         22 - Pagamento de Tributos GARE ICMS SP

·         25 - Pagamento de Tributos IPVA (SP e MG)

·         27 - Pagamento de Tributos DPVAT

·         29 - GR-PR sem Código de Barras

·         35 - Pagamento de Tributos FGTS - GFIP

**Segmento O**

·         13 - pagamento a concessionárias

·         19 - Pagamento de IPTU

·         28 - GR-PR com Codigo de Barras

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA300 - A partir da versão 12.0

**Solução**  
No padrão do Protheus no **Sispag**, o banco 341 (Itaú) não gera o **segmento B** para os **segmentos J**, **J52**, **N** e **O**, devido ser Opcional.  
  
Porém caso a mesma tenha necessidade recomendamos utilizar o módulo configurador e configurar a opção de **modelo2** no configurador utilizando a rotina **FINA430**.
