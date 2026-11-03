---
article_id: 360035400534
category: NFe - Nota Fiscal Eletrônica
content_hash: d393406ec744f9e810162317cdf6781339381bf12706ba1a9eb3f0c9a13d0669
fetched_at: '2026-06-28T22:40:00.234242+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  324 Rejeição
  : CNPJ do destinatário já autorizado para download'
type: support-article
updated_at: '2021-08-10T19:01:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035400534--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-324-Rejei%C3%A7%C3%A3o-CNPJ-do-destinat%C3%A1rio-j%C3%A1-autorizado-para-download
---

**Dúvida**

Como solucionar a 324 Rejeição : CNPJ do destinatário já autorizado para download  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A finalidade da TAG **autXML** é para saber quais CNPJs e CPFs estão autorizados a consultar a nota completa no **site da Sefaz:**

*[Clique Aqui](https://tdn.totvs.com/display/public/PROT/TTXZLW_DT_NFe_Parametro_MV_AUTXML_Cpf_Cnpj_Tag_AutXml)*

1. No **Configurador (SIGACFG)**, acesse **Ambientes/Cadastros/Parâmetros (CFGX017)**. Configure o(s) parâmetro(s) a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360017463732/mceclip1.png)

## 

Informe através do parâmetro **MV\_AUTXML até 10 CPF e/ou CNPJ** do Escritório de Contabilidade e/ou Órgão/pessoa autorizada a receber o xml da NF-e.

Utilizar apenas ponto e vírgula **" ; "** como separador do conteúdo. Não utilizar pontos, virgulas, hifens ou outros caracteres.

* **Exemplo**

**Cont. Por.:**78974147000170;05233768000129;95555504500;

* **Conforme o Manual da Sefaz:**

[Manual de Orientação do Contribuinte - versão 6.00](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=URCYvjVMIzI=)  
  
  
Página 183  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/BgylH1zCIbAW2eYjCTrmbB9xh/?name=inline600401751.png)​  
  
  
O CNPJ deve **ter 14 dígitos** e o **CPF 11**

* **Importante:**

Se houver apenas um CPF e/ou CNPJ é necessário que seja utilizado o separador da mesma forma  

Ex: **Cont. Por.:**78974147000170;

*Se **considerar a solução inviável** para a sua necessidade há****uma melhoria*** para gerar a TAG **autXML** para atender **Ajuste Sinief 16/2018.**

Foi criado o parâmetro **MV\_CMPCNPJ** para mencionar os campos customizados do documento de entrada (SF1) e saída SC5/SF2 para informar os CNPJ/CPF para compor a tag autXML.

* Para implementar há o **boletim no link abaixo:**

[Como utilizar o MV\_CMPCNPJ para mencionar os CNPJ/CPF para compor a tag autXML.](https://tdn.totvs.com/pages/viewpage.action?pageId=563442301)

O fonte do **NFESEFAZ**, deve estar com data igual ou superior

* ***Saiba mais:***

**A partir de 07/07/2020,** a consulta completa da **Nota Fiscal Eletrônica** só poderá ser realizada no Portal Nacional pelas partes envolvidas na operação, ou seja, **emitente, destinatário, transportador e terceiros informados na tag autXML.** A consulta no Portal Nacional apenas pelos participantes da operação já estava prevista no [Ajuste Sinief 16/2018](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2018/AJ0016_18) e não são aplicáveis às pessoas físicas e jurídicas que não possuam Inscrição Estadual.

Fonte: [RFB – Portal Documentos Eletrônicos](http://www.nfe.fazenda.gov.br/portal/informe.aspx?ehCTG=false&Informe=9ydmiExbDZM=)
