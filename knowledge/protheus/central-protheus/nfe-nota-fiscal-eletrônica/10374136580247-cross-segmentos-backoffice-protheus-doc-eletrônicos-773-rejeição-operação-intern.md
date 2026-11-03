---
article_id: 10374136580247
category: NFe - Nota Fiscal Eletrônica
content_hash: bbea85bf70c9d698c9fa938d98982d5e848af58bfa8a8cf3f1e8dfb7f40317de
fetched_at: '2026-06-28T22:40:05.285540+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 773 Rejeição: Operação
  Interna e UF de destino difere da UF do emitente'
type: support-article
updated_at: '2025-06-30T19:31:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10374136580247-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-773-Rejei%C3%A7%C3%A3o-Opera%C3%A7%C3%A3o-Interna-e-UF-de-destino-difere-da-UF-do-emitente
---

**Dúvida**Como solucionar a 773 Rejeição: Operação Interna e UF de destino difere da UF do emitente ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se operação Interna no Estado ***(tag:idDest = 1)*** e operação não é com Consumidor final: – UF de destino difere da UF do emitente

1- Preencher para consumidor final o campo no pedido de vendas **Tipo cliente:**

**C5\_TIPOCLI" = F**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33157524245143)

**(se nota de devolução com cliente ou utiliza cadastro de cliente)** informar no cadastro de cliente A1\_TIPO = F (consumidor final).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33157524246935)

Ou

2. Preencher o CFOP no TES da nota no campo **Cod. Fiscal "F4\_CF" de operação interestadual iniciado por 2 ou 6.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33157547713815)

***Exceção:*** Se a tag UFCons (id:LA06) foi informada com a mesma UF do emitente não se aplica esta regra (NT 2013/005)

Para habilitar a opção de complemento de combustível nos Livros Fiscais, você deverá:  
  
1. Incluir um grupo de produto (**Combustíveis**);

2. Alterar o cadastro do produto e vincular o grupo no campo **B1\_GRUPO;**

3. Informar o grupo no parâmetro **MV\_COMBUS;**

4. Após gerar a nota, acessar: **Livros Fiscais > Atualizações > Movimentos > NF-e Manual de Entrada / Saída > Complementos;**

**Na versão 4.00 da NF-e será necessário informar os quatro campos abaixo:  
  
· CD6\_CODANP**

**· CD6\_DESANP**

**. CD6\_UFCONS**

**. CDD\_IFCOMP**

Existe a possibilidade do preenchimento automático dos campos da CD6 para isso usar o ponto de entrada MATUCOMP.

Existe a possibilidade do campo CDD\_IFCOMP ser preenchido automaticamente. Para isso é necessário ativar o parâmetro MV\_ATUCOMP e usar o ponto de entrada MATUCOMP, abaixo documentação:   
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=642645988>

Ocorre a rejeição 660, pois é **obrigatória** a informação do grupo de combustível para os CFOPs constantes no **Anexo XI.02** - CFOP de Combustível e Lubrificantes (**NT 2012/003**)

Para preencher os Complementos de Combustíveis, entrar em **Livros Fiscais -> Movimentos-> NF Manual de saída->Ações Relacionadas->Complemento->Complementos de Combustível** e depois preencher os seguintes campos:

Complemento de combustível, para o **XML** a SEFAZ obriga somente 3 tags, **<cProdANP>** (**Código de produto da ANP**), **<UFCons>** (**Sigla da UF de consumo**) e ***<descANP> (Descrição do produto conforme ANP).***
