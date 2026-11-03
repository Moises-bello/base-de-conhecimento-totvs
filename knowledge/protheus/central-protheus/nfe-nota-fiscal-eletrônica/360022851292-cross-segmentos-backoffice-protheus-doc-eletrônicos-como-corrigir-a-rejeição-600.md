---
article_id: 360022851292
category: NFe - Nota Fiscal Eletrônica
content_hash: 4eccb61ec1ae2a1ac3fb08a99a4ff5daaf57b913e055dc5ae01e7fe68f581e7a
fetched_at: '2026-06-28T22:40:05.659070+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como corrigir a
  rejeição 600: CSOSN incompatível na operação com Não Contribuinte?'
type: support-article
updated_at: '2025-09-30T13:41:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022851292-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-corrigir-a-rejei%C3%A7%C3%A3o-600-CSOSN-incompat%C3%ADvel-na-opera%C3%A7%C3%A3o-com-N%C3%A3o-Contribuinte
---

**Dúvida**Como resolver a Rejeição 600: CSOSN incompatível na operação com Não Contribuinte?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

**Causa**

Operação com Não Contribuinte (indIEDest=9) e CSOSN difere da relação abaixo:  
- 102-Tributação SN sem permissão de crédito;  
- 103-Tributação SN, com isenção para faixa de receita bruta;  
- 300-Imune;  
- 400-Não tributada pelo Simples Nacional;  
- 500-ICMS cobrado anteriormente por substituição tributária ou por antecipação;

**Solução**

Se a operação for para não contribuinte **<indIEDest>9****</indIEDest>** só poderá ser utilizado os **CSOSN** **102, 103, 300, 400 ou 500.**

1- Sendo assim, se realmente for uma operação de **não contribuinte** alterar o conteúdo do campo no TES **F4\_CSOSN "Campo Cod. Sit. SN" para 102, 103, 300, 400 ou 500.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061024513)

2- Após isso, **exclua a nota** e gere novamente.

3- Se **não for operação para não contribuinte altere o cadastro de cliente ou fornecedor** (caso faça nota de saída do tipo B - utiliza fornecedor):  

4- Para contribuinte preencher no cadastro de cliente a inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

5- Preencher o campo Destaca IE **"A1\_IECONT"**  em branco

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

6- Preencher o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33722150948375)

7- Para cadastro de cliente Isento deixe em branco ou Preencha com literal Isento no campo de inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

8- Preencher o campo Destaca IE **"A1\_IECONT"**  em branco

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

9- Preencher o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33722150948375)

10- Para nota de saída do tipo B, utiliza fornecedor para cadastro de Isento deixe em branco ou Preencha com literal Isento no campo de inscrição estadual no campo  Ins. Estad. **"A2\_INSCR"**

11- Para nota de saída do tipo B, utiliza fornecedor preencher a inscrição no campo **A2\_INSCR, e preencher o campo A2\_CONTRIB = 1**

12- Após isso, exclua a nota e gere novamente.

* **Saiba mais:**

**A Sefaz não valida a rejeição caso utilize uma das exceções abaixo:**

Operação com Não Contribuinte (indIEDest=9) e  
CSOSN difere da relação abaixo:  
- 102-Tributação SN sem permissão de crédito;  
- 103-Tributação SN, com isenção para faixa de receita bruta;  
- 300-Imune;  
- 400-Não tributada pelo Simples Nacional;  
- 500-ICMS cobrado anteriormente por substituição tributária ou por antecipação;

Exceção 1: A regra de validação acima não se aplica para NF-e de entrada (tpNF=0-Entrada).  
Exceção 2: A regra de validação acima não se aplica nas operações com CFOP de conserto ou reparo (CFOP 5915, 5916, 6915 e 6916) ou de remessa para demonstração dentro do Estado (CFOP 5912 e 5913).  
Exceção 3: A regra de validação não se aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/07/2016. (NT 2015.003)

Exceção 4: A critério da UF, a regra de validação acima não se aplica para o MEI (CRT=4) nas operações de Remessa com os CFOP 5904 e 6904 e CSOSN=900.  
Exceção 5: A regra de validação acima não se aplica para o MEI (CRT=4) nas operações de Remessa com os CFOP 5551 ou 6551, e CSOSN=900.
