---
article_id: 360021564091
category: Materiais - Compras (SIGACOM)
content_hash: 864c064a6bb9eb5a5af7931b01379428db85ad3fb6874626eba662e096de98a8
fetched_at: '2026-06-28T22:41:07.463014+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao tentar excluir uma
  NF na rotina Documento de Entrada é apresentado o Help A103CAGREG
type: support-article
updated_at: '2022-07-05T18:21:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021564091-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-tentar-excluir-uma-NF-na-rotina-Documento-de-Entrada-%C3%A9-apresentado-o-Help-A103CAGREG
---

**Dúvida**

Ao tentar excluir uma NF na rotina Documento de Entrada é apresentado o Help **A103CAGREG**  
  
**Ambiente**

Protheus – Compras – A partir da versão 11.80

**Causa**

Esse incidente ocorre quando o documento a ser excluído está vinculado a uma nota de complemento/frete ou despesa de importação.  
  
**Solução**

Para consultar as Notas Ficais filtre através dos campos Docto. Orig. **(D1\_NFORI)** e Série Orig. **(D1\_SERIORI)** na consulta genérica (*Consulta > Cadastros > Genéricas*) da **SD1 (Itens das NF de Entrada)**.

Para excluir as notas fiscais vinculadas a ela é necessário voltar na rotina de Conhecimento de Frete (**MATA116**) e excluir os CTE's encontrados na consulta genérica.

Caso os campos mencionados estejam em branco pesquise na tabela **SF8 (Amarração NF Orig x NF Imp/Fre)** através do campo **F8\_NFORIG**. A nota fiscal que encontra-se vinculada a nota de compra estará informada no campo **F8\_NFDIFRE**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045306534/mceclip1.png)

* Em seguida, verifique como está preenchido o campo **F8\_TIPO**.
  + Caso esteja preenchido com **F** está relacionada a uma nota de **FRETE** que deve ser consultadaatravés da rotina ***Nt. Conhec. Frete (MATA116)**.*
  + Caso esteja preenchido com **D** está relacionada a uma nota de **DESPESA** que deve ser consultadaatravés da rotina ***Despesa de Importação (MATA119)***.

Há também o relatório **Nota Fiscal de Origem x Nota Fiscal de Frete (MATR015)**que possibilita verificar os registros da tabela SF8.

*Compras > Relatórios > Documentos de Entrada > Nota Fiscal de Origem x Nota Fiscal de Frete:*

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046164653/mceclip4.png)

**Exemplo:**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045308774/mceclip5.png)
