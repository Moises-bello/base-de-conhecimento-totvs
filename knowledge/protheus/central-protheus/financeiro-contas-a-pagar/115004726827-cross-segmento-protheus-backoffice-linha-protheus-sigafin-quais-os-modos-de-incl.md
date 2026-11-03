---
article_id: 115004726827
category: Financeiro - Contas a Pagar
content_hash: bcf8f65407510dc9e773163fc9a117b2869afd285d966fcc17592a56972cfd95
fetched_at: '2026-06-28T22:38:08.421298+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento Protheus - Backoffice Linha Protheus - SIGAFIN  - Quais os modos
  de inclusão de PA
type: support-article
updated_at: '2026-03-05T14:07:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004726827-Cross-Segmento-Protheus-Backoffice-Linha-Protheus-SIGAFIN-Quais-os-modos-de-inclus%C3%A3o-de-PA
---

**Dúvida**

No Contas a Pagar quais os modos de inclusão do PA?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da versão 12

**Solução**

Na inclusão do PA, os parâmetros F12 oferecem três opções de como gerar o pagamento antecipado PA: '

• O PA é pago em dinheiro, a movimentação bancária será gerada e registrada na SE5 com o campo E5\_TIPODOC configurado como PA.

**Cheque P/ Adiantamento =** Não e **Gera Mov. Banc. S/ Cheque =** Sim

**![Gravar_2024_07_10_11_29_45_941.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24789560064919)**

• O **PA** é pago com cheque, a movimentação bancária será gerada e registrada na SE5 com o campo E5\_TIPODOC configurado como BA, após a liberação do cheque será gerado movimento do tipo CH.

**Cheque P/ Adiantamento =**Sim e **Gera Mov. Banc. S/ Cheque =** Não

**![Gravar_2024_07_10_11_45_56_25.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24789560072215)**

• O **PA** é pago por CNAB, não é gerado movimentação bancária, somente após o retorno do cnab ou baixa automática, com o campo E5\_TIPODOC configurado como PA.

**Cheque P/ Adiantamento** = Não e **Gera Mov. Banc. S/ Cheque =** Não

**![Gravar_2024_07_10_11_54_47_466.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24789560078359)**

**Importante**

Caso o banco esteja configurado no parâmetro ***MV\_CARTEIR***, será considerado um banco interno da empresa e, portanto, não estará habilitado para emissão de cheques ou para não gerar movimento, ou seja, configurando os parâmetros **"Cheque p/ Adiantamento = Não" e "Gera Mov. Banc. s/ Cheque = Não"**, a movimentação bancária será gerada normalmente na tabela **SE5**.

**Saiba mais**

[Modos de inclusão PA](https://tdn.totvs.com/display/public/PROT/FIN0012_CPAG_modos_de_inclusao_de_PA)

[MV\_CARTEIR e MV\_CXFIN](https://tdn.totvs.com/pages/releaseview.action?pageId=172300136)

[Tipo de movimento da E5\_TIPODOC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022538171-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Descri%C3%A7%C3%B5es-dos-tipos-de-movimenta%C3%A7%C3%B5es-do-campo-E5-TIPODOC)
