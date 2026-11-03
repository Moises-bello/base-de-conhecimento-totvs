---
article_id: 8824276205847
category: NFe - Nota Fiscal Eletrônica
content_hash: 01f3c5811185d427e24265e021cc391ed81e9e282d7c0d4cb08a8b4f6b5608bd
fetched_at: '2026-06-28T22:40:05.275510+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 732 Rejeição :
  CFOP de operação interestadual e idDest diferente de 2'
type: support-article
updated_at: '2025-07-09T12:11:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8824276205847-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-732-Rejei%C3%A7%C3%A3o-CFOP-de-opera%C3%A7%C3%A3o-interestadual-e-idDest-diferente-de-2
---

**Dúvida**Como corrigir 732 Rejeição: CFOP de operação interestadual e idDest diferente de 2  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Se gerada a nota com **CFOP iniciado por 6** de operação interestadual **não pode** ser gerada a **TAG idDest precisa ser 2.**

2. Verificar se todos os itens os ***CFOPS iniciam por 6*** e se a operação é fora da UF, se algum o ***CFOP estiver iniciado por 5 alterar no TES*** alterar o CFOP pelo TES da nota no campo **Cod. Fiscal "F4\_CF", para um CFOP de operação interna**iniciado por **2 ou 6;**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347472153495)

3. Após isso, exclua a **nota e gere novamente.**

Ou

4. Se venda para cliente do exterior todos os CFOPS devem ser de operação interna iniciados por 1 ou 5 alterar o CFOP pelo TES da nota no campo **Cod. Fiscal "F4\_CF", para um CFOP de operação interna**iniciado por **1 ou 5;**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347472153495)

5. Preencher o campo no cadastro de cliente ***A1\_PFISICA* "RG/Ced.Estr."**  ou fornecedor A2\_PFISICA **"RG/Ced.Estr." se tiver conteúdo retire.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347457522199)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347457523095)

6. Preencher para consumidor final o campo no pedido de vendas **Tipo cliente** **C5\_TIPOCLI" = F**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347472159255)

7. Caso o **CFOP** seja operação interna verificar se o parâmetro no configurar **MV\_ESTADO** está configurado corretamente com a UF de emissão de nota da empresa.

8. Caso seja venda de um destinatário EX do exterior com CFOP de operação interestadual a única exceção é  para combustível ou lubrificante, sendo assim será necessário alterar no TES no campo **F4\_CF "Cod. Fiscal" para** o CFOP**6.667**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347472160279)**

9. Configure a nota para que seja levado os dados de **combustível e lubrificante** conforme o link abaixo:

[MP - NFE - Rejeição 660 CFOP de Combustível e não informado grupo de combustível da NF-e](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020837511)

* ***Validação da Sefaz:***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8824365769367)
