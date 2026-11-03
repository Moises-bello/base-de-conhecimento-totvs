---
article_id: 360034530613
category: NFe - Nota Fiscal Eletrônica
content_hash: ccaade413d63d4c77da331a2c08580208e0946ceabae01c1eac034729538e323
fetched_at: '2026-06-28T22:40:01.598679+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 931 Rejeição:
  Informado código de benefício fiscal incompatível com CST e UF'
type: support-article
updated_at: '2023-10-30T17:12:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034530613--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-931-Rejei%C3%A7%C3%A3o-Informado-c%C3%B3digo-de-benef%C3%ADcio-fiscal-incompat%C3%ADvel-com-CST-e-UF
---

**Dúvida**Como solucionar a rejeição abaixo:

931 Rejeição: Informado código de benefício fiscal incompatível com CST e UF ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

No site da Sefaz nacional é possível consultar a lista de **código de beneficio** que podem ser utilizados por **CST.**

* **Acessar o site**

[**https://www.nfe.fazenda.gov.br/portal/principal.aspx**](https://www.nfe.fazenda.gov.br/portal/principal.aspx)

Aba documentos -> Diversos, pesquisar ***CBENEF***

Se necessário gerar o literal ***SEM CBENEF*****,**acessar o módulo **Configurador (SIGACFG)**, em seguida em ***Ambiente /** **Cadastros / Parâmetros*** clicar em ***editar******, exemplo MV\_CODCST* *PR=90;41;RS=10,90;GO;SC;***

![20220321_113222.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4907277711127)

[Clique Aqui](https://tdn.totvs.com/display/public/PROT/Preencher+a+tag+cBenef+no+XML+da+NF-e)

3. Se houver dúvidas para alterar no Protheus o ***código de benefício fiscal*** [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033521654)

4. Se estiver ***correto, altere*** no TES o campo **Sit. trib. ICMS** **(F4\_SITTRIB) e vincule o CST correto ao ***código de benefício fiscal conforme lista da UF.*****

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078727553)
