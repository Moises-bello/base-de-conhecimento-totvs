---
article_id: 360027375872
category: Gestão de Distribuição (SIGAOMS)
content_hash: b4d5cde31f0467a1096b2e031940a0b334398f23a3cecfa16c680177429a9c97
fetched_at: '2026-06-28T22:45:49.916636+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Montagem de carga compartilhada com pedidos
  de múltiplas filiais
type: support-article
updated_at: '2023-10-10T13:15:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027375872-Log%C3%ADstica-Linha-Protheus-OMS-Montagem-de-carga-compartilhada-com-pedidos-de-m%C3%BAltiplas-filiais
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17144280065815)** Tempo aproximado para leitura: **00:01:30 min****Dúvida**Como configurar o Sistema na **Montagem de Carga - OMSA200** compartilhada com pedidos de múltiplas filiais?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Para configurar o Sistema nesta condição é preciso:

* Criar o campo **DAI\_FILPV - Filial do Pedido de Venda**, de forma manual no dicionário de dados, por meio do **Módulo Configurador - SIGACFG**.   
  Este campo deve possuir o mesmo tamanho do campo **filial** nas demais tabelas do Sistema;

![daifilpv.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/17144258790935)

* O ambiente deve possuir **duas** ou **mais Filiais**, as quais identificaremos como **X e Y**;
* O parâmetro **MV\_APDLOPE** deve estar como .T.;
* O parâmetro **MV\_APDLFOP** deve estar com o código da **Filial X - corresponde a Filial que é considerada o Operador Logístico**;
* O parâmetro **MV\_INTDL** deve estar igual a S;
* Todos os parâmetros mencionados acima devem ser independentes de Filial.

A **Montagem de Carga - OMSA200** é compartilhada com pedidos de múltiplas filiais, uma das filiais da empresa trabalha como uma **espécie de Operador Logístico e fica responsável pela expedição e carregamento dos produtos que serão destinados aos seus clientes.**Na visualização da carga é possível consultar as filiais dos pedidos:

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000625641)**

**Importante**

* Cada Filial gera seu próprio número de Nota Fiscal.
* Ao realizar o **Faturamento por Carga - MATA460B**, independente da filial, ao faturar todos os pedidos da carga **são faturados em suas respectivas filiais**, ou seja, será Faturada toda a Carga.

**Saiba mais**Mais informações poderão ser acessadas no *link*:   
[Logística - Linha Protheus - Códigos Clientes e Códigos Operadores Logísticos - DLGA270](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6744161821335-Log%C3%ADstica-Linha-Protheus-OMS-Associa%C3%A7%C3%A3o-dos-C%C3%B3digos-de-Clientes-e-C%C3%B3digos-Operadores-Log%C3%ADsticos-DLGA270)
