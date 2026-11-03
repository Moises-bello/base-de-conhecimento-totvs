---
article_id: 36340712152855
category: NFCOM - Nota Fiscal Fatura de Serviço de Comunicação Eletrônica
content_hash: 0605428d898783cc3324845f1a56f55122ee21d6dd60988127906146be937137
fetched_at: '2026-06-28T22:39:55.165667+00:00'
product: protheus
section_id: 33828030194199
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - indIEDest
  x IE
type: support-article
updated_at: '2025-11-14T17:13:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36340712152855-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-indIEDest-x-IE
---

**Dúvida**  
Como é a regra para montagem das tags **indIEDest x IE** no XML?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**  
Conforme layout da Sefaz, há três opções para a tag **indIEDest:**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/36340712132887)**

Para isso, à nível de montagem de XML, seguem as condições conforme Cadastro do Cliente (SA1):  
  
Opção 1 - Campos: A1\_INSCR = preenchido e A1\_CONTRIB=1  
**<indIEDest>1</indIEDest>**  
**<IE>123456</IE> (exemplo apenas)**  
  
Opção 2 - Campos: A1\_INSCR=ISENTO = preenchido e A1\_CONTRIB=2  
**<indIEDest>2</indIEDest>**  
**<IE>ISENTO</IE>**  
  
Opção 3 - Campos: A1\_INSCR=VAZIO  
**<indIEDest>9</indIEDest>**  
  
**IMPORTANTE**  
Segundo a Sefaz, para as UF's de Destinatário: AM, BA, CE, GO, MG, MS, MT, PE, RN, SE e SP, **não é permitido o envio do literal ISENTO na IE**, ou seja, o campo A1\_INSCR precisará estar em branco, caso contrário ocorrerá a [rejeição 432:](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36290703148311-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Rejei%C3%A7%C3%A3o-432-UF-do-Destinat%C3%A1rio-n%C3%A3o-aceita-ISENTO-com-Inscri%C3%A7%C3%A3o-Estadual)  
- <https://dfe-portal.svrs.rs.gov.br/Nfcom/ConsultaRegrasValidacao>
