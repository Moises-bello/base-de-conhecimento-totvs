---
article_id: 360007132632
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: ee99119f706c3e5814315cda7ddb9b9d3221137a25933ca5485e6c8486b21179
fetched_at: '2026-06-28T22:40:44.463502+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus  - SIGACTB - Habilitar procedures
  dinâmica na geração da ECD
type: support-article
updated_at: '2022-07-07T15:16:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007132632-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Habilitar-procedures-din%C3%A2mica-na-gera%C3%A7%C3%A3o-da-ECD
---

**Dúvida**

O que fazer quando houver lentidão na geração do arquivo da ECD para empresas com grandes movimentações?

* CTBS001
* PARÂMETRO MV\_CTBSPRC

**Ambiente**

Protheus – Contabilidade – A partir da versão 11.80

**Solução**

Melhoria de performance da escrituração contábil (ECD) - Sped Contábil.

Na escrituração da ECD com utilização da procedure dinâmica habilitada pelo parâmetro MV\_CTBSPRC ocorre a gravação das tabelas auxiliares CS's diretamente no banco de dados, por este motivo não existe a interação da aplicação no Monitor (envio de instruções). O tempo de processamento ocorrerá de acordo com a quantidade de dados a serem processados, levando em consideração uma empresa com grande movimentação anual o processo realmente poderá exceder algumas horas.

Criação do parâmetro MV\_CTBSPRC (SIGACFG)

Ambiente -> Cadastros -> Parâmetros

Nome da Variavel: MV\_CTBSPRC

Tipo: Lógico

Conteúdo: .T.

![](http://tdn.totvs.com/download/attachments/271676420/image2017-2-21%2010%3A20%3A21.png?version=1&modificationDate=1487683684000&api=v2)

![](http://tdn.totvs.com/download/attachments/271676420/image2017-2-21%2010%3A27%3A26.png?version=1&modificationDate=1487683684000&api=v2)

Veja Também :

[DT\_PERFORMANCE\_GERACAO\_ARQUIVO\_TEXTO](http://tdn.totvs.com/display/public/PROT/TUUIVS_DT_PERFORMANCE_GERACAO_ARQUIVO_TEXTO)

<http://tdn.totvs.com/display/public/PROT/ECD0002_MV_CTBSPRC_PERFORMANCE_ECD>

[Campo CT8\_DESC e CT2\_HIST](https://tdn.totvs.com/pages/releaseview.action?pageId=235586425)

[Como melhorar a performance para geração do arquivo TXT para a ECD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028659532-SIGACTB-ECD-Como-melhorar-a-performance-para-gera%C3%A7%C3%A3o-do-arquivo-TXT-para-a-ECD?source=search)
