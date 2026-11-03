---
article_id: 360046798213
category: NFe - Nota Fiscal Eletrônica
content_hash: b9e79ef4aed38eee5bd2b31554ab0549e1678c34a1413ea9726c65970cdd35a4
fetched_at: '2026-06-28T22:40:01.539836+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 771 Rejeição:
  Informado idEstrangeiro em operação interestadual'
type: support-article
updated_at: '2021-10-11T14:45:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046798213--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-771-Rejei%C3%A7%C3%A3o-Informado-idEstrangeiro-em-opera%C3%A7%C3%A3o-interestadual
---

**Dúvida**Como solucionar a rejeição abaixo:

771 Rejeição: Informado idEstrangeiro em operação interestadual ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- Se gerada a nota com **CFOP iniciado por 6** de operação interestadual **não pode** ser gerada a T**AG idEstrangeiro.**

2- Verifique se o campo foi preenchido no cadastro de cliente A1\_PFISICA **"RG/Ced.Estr."**  ou fornecedor A2\_PFISICA **"RG/Ced.Estr." se tiver conteúdo retire.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065750374/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065750534/mceclip2.png)

3- Caso o **CFOP** seja operação interna verificar se o parâmetro no configurar **MV\_ESTADO** está configurado corretamente com a UF de emissão de nota da empresa.

4- Caso seja venda de um destinatário EX do exterior com CFOP de operação interestadual a única exceção é  para combustível ou lubrificante, sendo assim será necessário alterar no TES no campo **F4\_CF "Cod. Fiscal" para** o CFOP**6.667**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066797813/mceclip3.png)**

5- Configure a nota para que seja levado os dados de **combustível e lubrificante** conforme o link abaixo:

[MP - NFE - Rejeição 660 CFOP de Combustível e não informado grupo de combustível da NF-e](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020837511)

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066794093/mceclip0.png)**
