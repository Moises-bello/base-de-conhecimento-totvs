---
article_id: 360028659532
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: f3d0d4fdbd9a3c607be0637205fda783485178c85bb02be5e6f09d12dbbef5ad
fetched_at: '2026-06-28T22:40:44.775030+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB / ECD  - Como melhorar
  a performance para geração do arquivo TXT para a ECD
type: support-article
updated_at: '2023-11-13T15:45:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028659532-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-Como-melhorar-a-performance-para-gera%C3%A7%C3%A3o-do-arquivo-TXT-para-a-ECD
---

**Dúvida*****Como melhorar a performance para geração do arquivo TXT para a ECD?***

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
**Solução**

O Ponto de entrada desenvolvido na rotina CTBSTXT com o objetivo de alterar o valor do cache de geração do arquivo texto na rotina de Escrituração Contábil.

O sistema foi alterado para gravar em cache o conteúdo referente ao bloco de inclusão na geração do arquivo texto. A gravação do arquivo é feita a cada 100 registros no arquivo. Esta quantidade pode ser alterada através do ponto de entrada, permitindo assim maior flexibilidade na execução.

|  |  |
| --- | --- |
| **Localização:** | CTBSTXT |
| **Eventos:** | Atualizações/Escrituração Contábil/Central Escrituração |
| **Programa Fonte:** | CTBS001 |
| **Função:** | CTBTXCache |
| **Retorno:** | nRet - Valor do cache definido para geração do arquivo. |
| **Exemplo:** | #Include '[Protheus.ch](http://protheus.ch/)'  User Function CTBTXCache()  // Valor do cache Local nRet := 500  Return nRet |
