---
article_id: 360018741711
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: f5b7a9ba0239cfe491a7f41aa88047419c13fd7412432d0f131ca6ad1efd794c
fetched_at: '2026-06-28T22:40:48.806020+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF Registro J001 esta
  sendo gerado Igual a "1"
type: support-article
updated_at: '2023-06-28T13:08:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018741711-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Registro-J001-esta-sendo-gerado-Igual-a-1
---

**Dúvida**

* Registro J001 esta sendo gerado Igual a "1",com isso não gera nenhum dados no arquivo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014196771)  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Causa**

* Manual da receita descreve :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014195872)

**Solução**

* É necessário que a C1O e CH5 tenham o mesmo compartilhamento da tabela CT1, CVN e CVD.
* Caso seja exclusivo, o campo C1O\_FILIAL será preenchido pelo sistema com a filial
* Verifique todos os pontos abaixo :
* [MP - SIGACTB - ECF – O que avaliar quando J050 e J051 não é gerado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search)
* [MP - SIGACTB - ECF - J051 não esta sendo gerado no arquivo TXT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005033352-MP-SIGACTB-ECF-J051-n%C3%A3o-esta-sendo-gerado-no-arquivo-TXT?source=search)
* Através da Issue [DSERTAF2-4873](http://tdn.totvs.com/pages/viewpage.action?pageId=381029136) foi tratada a situação caso as tabelas sejam  compartilhadas.
* Verifique no Validador ECD/ECF o compartilhamento das tabelas e também se não gera mensagem nas contas analíticas referente a amarração com a conta referencial, vídeo do validador ECF: <https://www.youtube.com/watch?v=WdgThLwJ9yM>
