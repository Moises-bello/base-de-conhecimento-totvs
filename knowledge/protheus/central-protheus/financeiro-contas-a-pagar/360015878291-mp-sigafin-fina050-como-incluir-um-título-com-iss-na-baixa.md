---
article_id: 360015878291
category: Financeiro - Contas a Pagar
content_hash: bfc1233c03335ba4249d1ac96e17ff0620ca7f7c740374ded2f9c8688e29970d
fetched_at: '2026-06-28T22:38:09.976335+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP- SIGAFIN - FINA050 - Como incluir um título com ISS na baixa
type: support-article
updated_at: '2021-04-28T15:19:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015878291-MP-SIGAFIN-FINA050-Como-incluir-um-t%C3%ADtulo-com-ISS-na-baixa
---

**Dúvida**Como incluir um título com geração de ISS na baixa ?  
   
 **Ambiente**Microsiga Protheus - Financeiro - FINA050 - A partir da versão 11.80.   
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1. Pelo Modulo **Configurador**> **Ambiente**> **Cadastros**> **Parâmetros**, ajuste o parâmetro **MV\_ALIQISS** = 5% **Exemplo**: (Cidade de São Paulo) - Verifique em sua cidade qual alíquota é utilizada.  
  
 2. No **Configurador > Ambiente > Cadastros > Parâmetros** ajuste o parâmetro **MV\_MRETISS** = 1 - Na **BAIXA** do título principal;

3. No modulo **Financeiro,** acesse **(FINA050)** Contas a Pagar, observe na baixa do arquivo e note que o sistema irá criar um novo lançamento com o valor calculado do **ISS**.
