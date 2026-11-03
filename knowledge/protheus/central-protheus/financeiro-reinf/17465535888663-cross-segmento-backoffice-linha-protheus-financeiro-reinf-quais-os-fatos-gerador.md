---
article_id: 17465535888663
category: Financeiro - Reinf
content_hash: bcfedd26d18f5afe368bfa65640f2b934444ebaecdc60ed2e9f41e5a1f268a92
fetched_at: '2026-06-28T22:37:51.665836+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - Financeiro REINF - Quais os fatos
  geradores serão considerados no extrator financeiro
type: support-article
updated_at: '2026-02-10T19:41:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17465535888663-Cross-Segmento-Backoffice-Linha-Protheus-Financeiro-REINF-Quais-os-fatos-geradores-ser%C3%A3o-considerados-no-extrator-financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17465508505623) Tempo aproximado para leitura: **00:05 min**

**Dúvida**

Quais os fatos geradores serão considerados no extrator financeiro?

**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - Financeiro REINF - Todas as versões.

**Solução**  
 **1- IRRF gerado na inclusão do título a pagar (A2\_CALCIRF=1)**

* Caso os parâmetros [*MV\_VCTIRPF = C*](https://tdn.totvs.com/pages/viewpage.action?pageId=531009057) e [*MV\_VENCIRF = C*](https://tdn.totvs.com/pages/viewpage.action?pageId=531009057), o fato gerador será a data de entrada/contabilização do documento (*FT\_ENTRADA*), caso contrário será considerada a data de emissão (FT\_EMISSAO*)*;
* Se o título a pagar não tiver vínculo com um Documento de Entrada, os campos considerados serão E2\_EMIS1 (fato gerador contabilização) ou **E2\_EMISSAO** (fato gerador emissão);
  + Para o **título a pagar avulso** (sem vínculo com nota fiscal) será considerada a pergunta "**Seleção de títulos a pagar**" do ***Wizard*** **do Extrator Fiscal** (aba **Financeiro**), onde:
    - A opção "**1-Data da contabilização**" considera a data do campo **E2\_EMIS1**;
    - A opção "**2-Data da emissão**" considera a data do campo **E2\_EMISSAO**;
  + Para o **título a pagar de um Documento de Entrada** e que a **TES** gerou **livro fiscal** (**SF3**/**SFT**), será considerada a data do campo **FT\_EMISSAO**;

Quando o [**MV\_RATIRRF**](https://tdn.totvs.com/pages/viewpage.action?pageId=531009057)estiver configurado com.**T.** (**rateia o IR entre as parcelas da nota**) e o **A2\_CALCIRF=1** (**emissão**), os valores de **IRRF** **de todas as parcelas** serão enviadas ao **TAF** somados e vinculados à nota fiscal, e não aos títulos de cada parcela;

**2 - IRRF gerado na baixa do título a pagar (A2\_CALCIRF=2)**

* Será considerada a data do pagamento do título principal (exemplo: título do **tipo NF**, **DP**, **BOL**, etc.), através do campo **FK2\_DATA**;

**3 - PIS, CONFINS E CSLL**

* Independente da configuração do parâmetro **MV\_BX10925**, que permite que os **TX's** desses impostos possam ser gerados na emissão ou na baixa, o **Extrator Fiscal** irá considerar como fato gerador do **PIS**, **COFINS** e **CSLL** o pagamento do título principal (exemplo: **título do tipo NF**, **DP**, **BOL**, etc.), através do campo **FK2\_DATA**;
  + Quando o parâmetro **MV\_BX10925=2** (gera **TX's** na inclusão do **título a pagar**), o **Extrator Fiscal** irá verificar se o título principal está baixado para enviar os tributos ao **TAF**. Se a baixa tiver sido **parcial,** serão enviados os valores dos tributos proporcionais ao valor baixado;

**4 - INSS**

* Para o **título a pagar ou receber avulso** (sem vínculo com nota fiscal) será considerada a pergunta "**Seleção de títulos" do*****Wizard*** **do Extrator Fiscal** (aba **Financeiro**), onde:
  + A opção "**1-Data da contabilização**";
  + A opção "**2-Data da emissão**";
  + Para o **título a pagar de um Documento de Entrada** e que a **TES** gerou **livro fiscal** (**SF3**/**SFT**), será considerada a data do campo **FT\_EMISSAO**

**Saiba Mais**  
[FAQ - 0016 - Quais os fatos geradores serão considerados no extrator financeiro?](https://tdn.totvs.com/pages/releaseview.action?pageId=737543501)
