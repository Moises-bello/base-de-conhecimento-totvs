---
article_id: 360025656472
category: Gestão de Transportes (TMS)
content_hash: 4c548104c4d1662c215df54f76c190279355406b3c96382ae84b111eff6bc3d5
fetched_at: '2026-06-28T22:45:27.295531+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Cadastro de produto de cálculo
type: support-article
updated_at: '2024-05-02T14:24:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025656472-Log%C3%ADstica-Linha-Protheus-TMS-Cadastro-de-produto-de-c%C3%A1lculo
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23157324257815)****Tempo aproximado para leitura: **00:03:30 min****Dúvida**Como cadastrar o **produto de cálculo**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**Segue abaixo o conceito do uso do **produto de cálculo** na geração de **documento de frete** e procedimentos para configuração do mesmo:

* O que é o **produto de cálculo** no **TMS**?  
  No módulo **TMS** além dos produtos que informamos na entrada do documento do cliente, produtos que serão transportados, temos também um produto que chamamos de **produto de cálculo**.
* Para que serve esse **produto de cálculo** no **TMS**?  
  Devido aos diversos tipos de operação que temos na prestação de serviço de transporte que podem ser de diferentes modais com execução municipal, intermunicipal, interestadual e consequentemente com regras e cobrança de impostos - **ICMS**, **ISS**, **Substituição Tributária**, **ICMS de Pauta,** entre outros, o **produto de cálculo** tornou-se uma representatividade do que podemos considerar como a **mercadoria da transportadora**, ou seja, o serviço prestado por ela e portanto sobre ele podemos definir algumas informações.

Esta configuração é necessária para que as informações fiscais sejam geradas nas tabelas:

* **SF3 - Livros Fiscais;**
* **SFT - Livro Fiscal por Item de NF;**
* **SD2 - Itens de Venda da NF.**

Um exemplo prático sobre a diferenciação entre a prestação de serviço dentro do município, entre municípios - intermunicipal, ou entre estados - interestadual, é a tributação.  
  
Dependendo da localização de onde foi iniciada e finalizada a prestação, distinguem-se os tributos que incidem sobre esse frete:  
  
**Exemplo:**  
Prestação intramunicipal - **ISS**, entre outros entre outros tributos  
Prestação intermunicipal - **ICMS**, entre outros tributos  
Prestação interestadual - **ICMS**, entre outros tributos  
  
Considerando que o **TMS** conta com os parâmetros abaixo para considerar a origem e destino da prestação, campos como de **alíquota de ICMS** - **B1\_PICM**, se não preenchidos, o cálculo será baseado nos parâmetros e **TES**.  
  
Para o campo de **ISS** - **B1\_ALIQISS**, se não informado percentual de alíquota, o cálculo será baseado na tabela de **Grupo de Regiões -** **DUY\_ALQISS** ou no parâmetro **MV\_ALIQISS** caso este campo também não seja preenchido.

* **MV\_ALIQICM** - Define as alíquotas de **ICMS** a serem utilizadas;
* **MV\_NORTE** - Tabelas de estados pertencentes ao norte/nordeste que trabalham com operações interestaduais aplicando alíquota do **ICMS** em 7%;
* **MV\_FRETEST** - Define alíquotas internas de **ICMS** de cada estado a serem utilizadas nas notas de Conhecimento de frete;
* **MV\_ICMPAD** - Define a alíquota de ICMS aplicada em operações dentro do estado onde a empresa está localizada.
* **MV\_ESTICM** - Alíquota de **ICMS** de cada estado. Informar a sigla e em seguida a alíquota, para cálculo de ICMS complementar;
* **MV\_ESTADO** - Sigla do estado da empresa usuária do Sistema, para efeito de cálculo de **ICMS** - 7, 12 ou 18%.

Com esse cadastro pronto faremos posteriormente sua associação ao cadastro de **Regra por Cliente**.  
  
**O produto gravado nos itens da tabela SD2 - Itens de Venda da NF será este produto de cálculo.**  
  
**Glossário****ICMS** - Imposto sobre Circulação de Mercadorias e Serviços **ISS** - Impostos Sobre Serviço **TES** - Tipos de Entrada e Saída **TMS** - Gestão de Transporte
