---
article_id: 360018436411
category: NFe - Nota Fiscal Eletrônica
content_hash: 8eac17815af2af131019f09dc97429c01f381e5095827f4454dd7da70b37f516
fetched_at: '2026-06-28T22:40:01.434985+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 508 Rejeição CST
  incompatível na operação com Não Contribuinte'
type: support-article
updated_at: '2021-09-09T14:52:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018436411--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-508-Rejei%C3%A7%C3%A3o-CST-incompat%C3%ADvel-na-opera%C3%A7%C3%A3o-com-N%C3%A3o-Contribuinte
---

**Dúvida**Como solucionar a rejeição:

508 Rejeição: CST incompatível na operação com Não Contribuinte ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A rejeição **508** ocorre, pois o destinatário  foi gerado como **não contribuinte** e foi utilizando um **CST do ICMS não valido** para essa operação.

1-Verifique se realmente a nota deve gerar o destinatário como **não contribuinte**

**<indIEDest>9</indIEDest>**

Verifique se o destinatário se enquadra como **1, 2 ou 9** conforme abaixo:

**1=**Contribuinte ICMS (informar a IE do destinatário);  
**2=**Contribuinte isento de Inscrição no cadastro de Contribuintes do ICMS;  
**9=**Não Contribuinte, que pode ou não possuir Inscrição Estadual no Cadastro de Contribuintes do ICMS;

* Essa consulta é possível ser realizada pelo CNPJ ou IE pelo site da Sefaz conforme o link abaixo:

  **Cadastro Centralizado de Contribuinte (CCC):**

  **<https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc>**

 2- Caso o  destinatário seja **Contribuinte ou Isento** altere o cadastro de cliente conforme abaixo:

**indIEDest = 1 ( Contribuinte)**

A1\_INSCR = preenchido  
A1\_CONTRIB =SIM  
A1\_IENCONT = Em branco

**indIEDest = 2** **(Isento)**

A1\_INSCR = Em branco ou ISENTO  
A1\_CONTRIB (ABA FISCAIS) = SIM (é contribuinte só não tem Inscrição)  
A1\_IENCONT (ABA OUTROS) = Em branco

3- Se o destinatário se enquadrar como 9 **(Não contribuinte)**  será necessário se adequar a situação tributária da nota correta no campo do TES **Sit. trib. ICM** **F4\_SITTRIB = 00, 20, 40, 41 e 60** ou **utilizar alguma das  validações que constam nas exceções** dessa NT conforme o print abaixo.

* Validação da Sefaz **conforme a NT 2020.005\_v\_1.20**

![508_rejei__o_parte_1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408155179287/508_rejei__o_parte_1.JPG)

![508_rejei__o_parte_2.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408151936791/508_rejei__o_parte_2.JPG)

* **Importante:**

 Caso esteja utilizando algumas das exceções e mesmo assim a rejeição persistir entre em contato com a Sefaz para saber o motivo de não aceitar a exceção que consta na NT.

Na **nota Técnica 2020.005,** foi acrescenta a **exceção 9 para notas de energia elétrica,** se houver dúvidas de como emitir notas de energia elétrica temos a documentação do link abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.003](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051143213)
