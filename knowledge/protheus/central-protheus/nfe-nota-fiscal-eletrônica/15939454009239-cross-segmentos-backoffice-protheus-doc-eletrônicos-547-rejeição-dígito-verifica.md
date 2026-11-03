---
article_id: 15939454009239
category: NFe - Nota Fiscal Eletrônica
content_hash: 4815af99e48deb308fde67e458a6670879f7b26cd84dd89608e0d20ab1df6ac7
fetched_at: '2026-06-28T22:40:01.490655+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 547 Rejeição:
  Dígito Verificador da Chave de Acesso da NF-e Referenciada inválido'
type: support-article
updated_at: '2023-07-13T12:52:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15939454009239--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-547-Rejei%C3%A7%C3%A3o-D%C3%ADgito-Verificador-da-Chave-de-Acesso-da-NF-e-Referenciada-inv%C3%A1lido
---

**Dúvida**Como corrigir a rejeição 547 Rejeição: Dígito Verificador da Chave de Acesso da NF-e Referenciada inválido ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Acessar a  **rotina de transmissão SPEDNFE;**

![nfesefaz.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15939445267095)

2. Clique em **Outras ações -> Monitor -> faixa ->** Digite o número e série da nota;

**![monitor_faixa.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15939459656471)**

3. Clique no **botão Schema; Copie e Cole o conteúdo completo do XML.**

![545_rej_monitor.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15939473890327)

4. Verifique ***a TAG refNFe, , conforme o XML de exemplo:***

***![](https://centraldeatendimento.totvs.com/hc/article_attachments/15939402060055)***

5. Para saber a chave com dígito errado, **consulte o link abaixo:**

***<https://www.nfe.fazenda.gov.br/portal/principal.aspx>***

6. Neste link, **Clique em Serviços ->  Consultar NF-e:**

**![consultar](https://centraldeatendimento.totvs.com/hc/article_attachments/15939485034007)**

**Ou na rotina SPEDNFE:**

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410653946135-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Consultar-NFe-pela-Chave>

7. A nota original para que traga de forma correta no XML a **chave** deverá estar gravada de forma correta nas tabelas ***SF3, SFT, SF1 ou SF2 nos campos* F3\_CHVNFE, FT\_CHVNFE, F1\_CHVNFE ou F2\_CHVNFE.**

**![CHAVES.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15939459665815)**

8. Se a nota for formulário próprio = Sim e tenha sido transmitida pela empresa, na rotina de transmissão de nota ir em ***Outra ações -> Monitor -> faixa ou Monitor -> Consulta NF*** para que seja preenchida a chave nas tabelas corretamente.

![Monitor_-_faixa_-_consulta_NF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15939453975575)

9. Se a nota de origem for de entrada com ***formulário próprio = Não*** verifique se a chave no campo ***F1\_CHVNFE foi digitada*** de forma correta validando a chave no portal da Sefaz no ambiente Nacional ou de Origem.

![F1_CHVNFE.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15939445283223)

10. Refaça a nota e transmita novamente.

* ***Saiba mais:***

***Chave de nota de exportação.***

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 340 Rejeição : Não informado o grupo de exportação indireta no item](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020130711)

* **Validação da Sefaz:**

**![547](https://centraldeatendimento.totvs.com/hc/article_attachments/15939459670423)**
