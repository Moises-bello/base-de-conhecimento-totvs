---
article_id: 360025600891
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 0f55370c1b8a889b83bf0db3a23df9911437e2cfe14e27881729256424dc17ff
fetched_at: '2026-06-28T22:40:44.501808+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB -  ECD  -  CAMPO NOTA
  EXPLICATIVA DESABILITADO J800/J8001
type: support-article
updated_at: '2022-07-18T18:30:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025600891-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-CAMPO-NOTA-EXPLICATIVA-DESABILITADO-J800-J8001
---

**Dúvida**

Como habilitar o campo de nota explicativa ou do termo de substituição (J800/J8001) para trocar/limpar o conteúdo do campo?

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024330411/mceclip0.png)**  
**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus  - Contabilidade Gerencial - A partir da versão P11.8

**Solução**  
  
Como paliativa:

* Gere uma nova revisão com o layout de 2017 LAYOUT 6 (layout anterior),
* Apague o conteúdo dos campos J800/ J801, e finalize a exportação.
* Ao gerar o layout 7 (atual) os campos estarão sem conteúdo preenchido.

Isso aconteceu porque a wizard da ECD grava na memoria os dados da ultima revisão.

Por enquanto, só assim conseguiremos apagar esse conteúdo que não utilizaremos na revisão atual.

O desenvolvimento já esta atuando nesta correção, issue **DSERCTR1-19653.**
