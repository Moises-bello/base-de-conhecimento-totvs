---
article_id: 37673439117335
category: Financeiro - Baixas a Pagar
content_hash: 2687714ee650b9407ef74a1433aa03a88db57bea6c6b30e4865c2b09424c1ea4
fetched_at: '2026-06-28T22:37:24.851551+00:00'
product: protheus
section_id: 38295862957335
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA080 - TXA baixado porém com
  saldo em aberto
type: support-article
updated_at: '2026-03-04T16:47:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37673439117335-Cross-Segmento-Backoffice-Linha-Protheus-FINA080-TXA-baixado-por%C3%A9m-com-saldo-em-aberto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37673439106967) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
O imposto de adiantamento consta como baixado; entretanto, o saldo do título permanece em aberto. Como proceder para realizar a baixa integral e zerar o saldo?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FNA080 - Todas as versões.   
  
**Solução**

O sistema dispõe do parâmetro **MV\_BXTXA**, cuja finalidade é controlar o comportamento da baixa dos títulos do tipo **TXA** gerados pelo **PA** com incidência de impostos.

Essa diferenciação de comportamento é necessária para viabilizar a **compensação posterior** entre os títulos de adiantamento de imposto (**TXA**) e os títulos de imposto do tipo **TX**, originados a partir de documentos **NF** ou **DP**.

O parâmetro **MV\_BXTXA** é responsável por definir como será realizada a baixa dos adiantamentos de impostos, conforme as opções abaixo:

* **Opção 1 – Permitir a baixa**  
  Permite a baixa do título de imposto, realizando a quitação integral e zerando o saldo do título TXA.
* **Opção 2 – Não zerar o saldo**  
  A baixa do título é executada, porém, o saldo não é zerado. O título permanecerá com saldo em aberto até que ocorra a compensação entre o título **TXA** e o respectivo título **TX** gerado pelo documento do tipo **NF**.

Na prática, quando o título apresenta a legenda **“Adiantamento de imposto baixado com saldo”**, isso indica que a baixa foi realizada, porém, o saldo permanece em aberto aguardando a compensação com o título de imposto correspondente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37673439107479)

A baixa do movimento foi realizada com sucesso; entretanto, o saldo do título permanece em aberto.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37673477451287)

Nessa situação, o saldo somente será quitado após a compensação entre o título **TXA** e o respectivo título **TX** gerado a partir de uma **NF**.

Alternativamente, é possível ajustar o parâmetro **MV\_BXTXA** para a opção **1**, o que permitirá que o saldo do título seja baixado integralmente no momento da baixa, sem a necessidade de compensação posterior.

**Saiba mais**

[MV\_BXTXA](https://tdn.totvs.com/display/public/PROT/MV_BXTXA)
