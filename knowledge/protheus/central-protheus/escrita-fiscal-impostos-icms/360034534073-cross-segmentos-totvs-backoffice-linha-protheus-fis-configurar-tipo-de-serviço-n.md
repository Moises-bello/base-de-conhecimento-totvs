---
article_id: 360034534073
category: Escrita Fiscal - Impostos - ICMS
content_hash: ddb29b022f8da35383ffc685bc5ecaca0937973b9e4d8468ea56aa2f2a8f1106
fetched_at: '2026-06-28T22:39:25.633851+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Configurar tipo de
  serviço nota espécie CTE-OS enviar para Reinf
type: support-article
updated_at: '2022-02-15T20:01:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034534073-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configurar-tipo-de-servi%C3%A7o-nota-esp%C3%A9cie-CTE-OS-enviar-para-Reinf
---

**Dúvida**Como cadastrar o tipo de serviço para o reinf, nota com a espécie CTE-OS?  
  
 **Ambiente**Microsiga Protheus – Fiscal – A partir da versão 12  
  
**Solução**

Foi criado o campo Tipo serviço **(F2Q\_TPSERV)** no cadastro de Complemento Fiscal do produto que deverá ser preenchido quando existir documentos fiscais espécie **CTE-OS** tributados com INSS e ICMS. 

1. Essa alteração está condicionada  aos seguintes processos:

2. Para que seja habilitado a seção complementos fiscal do produto rotina (**FISA180**), será necessário a inclusão da informação da tabela "**F2Q**" no parâmetro **MV\_CADPROD** Exemplo: |SA5|SBZ|SB5|DH5|SGI|**F2Q**";

**MV\_CADPROD** - Determina os cadastros complementares que serão apresentados no cadastro de produto  

SA5 - Produto X Fornecedor   
SBZ - Indicadores  
SB5 - Complemento de Produto  
DH5 - Complemento de Produto DCL  
SGI - Produtos Alternativos  
F2Q - Complemento Fiscal de Produto

3. Precisa estar com o fonte FISA180.PRW com data igual ou superior a 12/07/2018, pacote abaixo.

<https://suporte.totvs.com/portal/p/10098/download?e=698444>

4. Cadastrar na rotina Complemento Fiscal do Produto (FISA180), o produto e o tipo de serviço conforme exemplo abaixo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044739233/mceclip0.png)
