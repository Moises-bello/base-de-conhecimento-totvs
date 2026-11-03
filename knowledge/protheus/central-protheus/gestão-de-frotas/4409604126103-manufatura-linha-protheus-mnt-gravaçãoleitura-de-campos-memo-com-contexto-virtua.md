---
article_id: 4409604126103
category: Gestão de Frotas
content_hash: a9f1123846749fd734a193ceb107d347f2ef7106e632a0d0856dddbe2ed73ac1
fetched_at: '2026-06-28T22:42:39.424659+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Gravação/leitura de campos Memo com contexto
  virtual para Real
type: support-article
updated_at: '2021-10-01T14:29:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409604126103-Manufatura-Linha-Protheus-MNT-Grava%C3%A7%C3%A3o-leitura-de-campos-Memo-com-contexto-virtual-para-Real
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:15 min** **Dúvida**Como realizar a gravação e a busca de valores de campos **Memo** com o contexto **Real** nas rotinas de **Importação de Abastecimento**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas – Versão 12  
  
**Solução**Foi realizada a alteração do contexto **Virtual** para **Real**, nos campos **Memo** a seguir:

* **TQQ\_OBSERV - Observações**
* **TR6\_OBSERV - Observações**
* **TUI\_OBSERV - Observações**

Anteriormente a gravação dos campos era feita com ao auxilio da função **MSMM**, conforme exemplo a seguir:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409603993239/mceclip0.png)

Porém com os campos no contexto real, não é mais necessário a utilização da função **MSMM**, basta passar o valor direto para o campo.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409604021655/mceclip1.png)

Assim também como a busca de valores, não há mais necessidade da utilização da função **MSMM**, sendo necessário realizar apenas a busca direta pelo campo.  
A alteração realizada impacta de forma direta nas tabelas a seguir:

* **TQQ - Abastecimentos Rejeitados**
* **TR6 - Abastecimentos Importados**
* **TUI - Transferência de Combustível**

**Importante**Antes de realizar as alterações, verifique se os campos citados estão no contexto **Real**, pois caso contrário não será possível realizar a gravação direta.
