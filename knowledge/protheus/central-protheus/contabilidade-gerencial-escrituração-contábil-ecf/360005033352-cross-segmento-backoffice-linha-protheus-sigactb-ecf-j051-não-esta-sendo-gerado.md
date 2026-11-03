---
article_id: 360005033352
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 25da1aaf08badf11456a6bd885141f1d53b8f9ed1d7de796d35303694ff9d005
fetched_at: '2026-06-28T22:40:47.371048+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - J051 não esta
  sendo gerado no arquivo TXT
type: support-article
updated_at: '2022-07-28T19:42:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005033352-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-J051-n%C3%A3o-esta-sendo-gerado-no-arquivo-TXT
---

**Ambiente** Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Ocorrência**

TAF não está gera J051 no arquivo TXT

Analise realizada conforme link abaixo

<http://tdn.totvs.com/pages/viewpage.action?pageId=284465420>

* Na TAFST1 e TAFST2 foi criado o registro T010 e T010AA
* Integração com o TAF não apresentou nenhum erro ou advertência
* Através da rotina TAFA060 o sistema gerou o registro do J051

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360006651052/image.png)**

* Ao gerar a Revisão o J051  não é gerado

**Causa**

* Tamanho dos campo  CAE\_CTA e CAG\_CTA

**Solução**

* DSERCTR1-12290 - **Liberada** através do link abaixo
* <http://tdn.totvs.com/pages/releaseview.action?pageId=485425635>

**Paliativo orientado antes da liberação da Pacth**

**1 - Backup das Tabelas CAE e CAG  
2 -  Alteração dos campos: CAE\_CTA de 6 para 36 E CAG\_CTA de 6 para 36.  
3 - Drop da Tabelas  
4 - Feito o Processo de Zap nas Tabeas TAFST1,TAFST2,TAFXERP, TAFECF\_01  
5 - Feito o Processo de Exportação dos Dados do ECF pelo Modulo 34  
6 - Geração do novo Arquivo.  
7 - Registro J051 Gerado com Sucesso.**

**Observação : Após liberação da pacote**

**Caso ocorrência persista verifique a documentação abaixo**

* **Execute UPDDISTR**
* **Verifique se o tamanho campos estão : CAE\_CTA de 36 E CAG\_CTA de 36.**
* **Drop da Tabelas**
* **Efetue o Processo de Zap nas Tabeas TAFST1,TAFST2,TAFXERP, TAFECF\_01**
* **Efetue  o Processo de Exportação dos Dados do ECF pelo Modulo 34**
* **Através da rotina TAFA060 se as contas foram geradas**
* **Geração do novo Arquivo.**
* **Registro J051 Gerado com Sucesso.**

[MP - SIGACTB - ECF – O que avaliar quando J050 e J051 não é gerado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search)
