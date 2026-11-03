---
article_id: 15936047108375
category: NFe - Nota Fiscal Eletrônica
content_hash: 84d9acee683412c393212ffbd047656b2f4187fc58ed220e1822df2e3006d51e
fetched_at: '2026-06-28T22:40:05.052950+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 482: Código do
  Município do Destinatário diverge do cadastrado na UF'
type: support-article
updated_at: '2025-06-16T17:03:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15936047108375-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-482-C%C3%B3digo-do-Munic%C3%ADpio-do-Destinat%C3%A1rio-diverge-do-cadastrado-na-UF
---

**Dúvida**Como corrigir a 482: Código do Município do Destinatário diverge do cadastrado na UF ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

1 - Ao gerar rejeição referente ao ***cMUN do destinatário*** verifique se o seu XML gerou conforme o exemplo abaixo:

![cmun.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15936085808407)

![sao](https://centraldeatendimento.totvs.com/hc/article_attachments/15936447573271)

2- Conforme o XML acima  o **município  composto por 07 dígitos** que é obrigatória, deve estar conforme o IBGE através do link:

<http://www.ibge.gov.br/home/geociencias/areaterritorial/area.shtm>

 3- É necessário ajustar a informação no cadastro do cliente e o campo deve ser composto por 07 dígitos. Se for **cadastro de cliente** preencher **A1\_EST "Estado"**e**A1\_COD\_MUN "Cod. Municipio":**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15936069734423)

Se cadastro **de fornecedor preencher****A2\_EST "Estado" e A2\_COD\_MUN "Cod. Municipio":**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15936056219287)

4- Após isso, exclua a nota e gere novamente;

* **Saiba mais:**Verificação se a IE do destinatário existe na UF de destino (operação interestadual), se o contribuinte está habilitado e se o CNPJ informado está vinculado com a IE informada, para qualquer um dos ambientes de autorização (SEFAZ Autorizadora ou SEFAZ Virtual); É possível verificar o município do cadastro na Sefaz.
* **Cadastro Centralizado de Contribuinte (CCC):**

<https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc>

![ccc.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15936408676503)

* ***Validação da Sefaz:***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15935941789591)
