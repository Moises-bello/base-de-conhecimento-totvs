---
article_id: 360047362693
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: fc0362d1fc97753697b11674c0d14a3cc178085b1e79b51bfe0768b218bbf5b2
fetched_at: '2026-06-28T22:42:08.830951+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DIME SC - Quadro
  47 gerado indevidamente
type: support-article
updated_at: '2022-08-17T19:24:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047362693-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DIME-SC-Quadro-47-gerado-indevidamente
---

**Ocorrência** **Quadro 47** da **DIME SC** sendo gerado quando não há operação de entrada de produção primária oriunda de extratores, produtores agropecuários e pescadores.

**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
  
**Causa**   
Esse incidente ocorre, pois, na tabela **SA2 - Fornecedores,** o campo **Tp.Contr.Soc (A2\_TIPORUR)** está preenchido.  
  
**Solução**Para solucionar a ocorrência realize o seguinte procedimento:  
1. Acesse o **Módulo 02- Compras,** clique em **Cadastros** e depois em **Fornecedores**;  
2. Na aba fiscal, localize o campo **Tp.Contr.Soc (A2\_TIPORUR**) e deixe o campo sem preenchimento;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067215534/mceclip0.png)

3. Gere novamente o arquivo txt e verifique que dessa forma o registro não será gerado.
