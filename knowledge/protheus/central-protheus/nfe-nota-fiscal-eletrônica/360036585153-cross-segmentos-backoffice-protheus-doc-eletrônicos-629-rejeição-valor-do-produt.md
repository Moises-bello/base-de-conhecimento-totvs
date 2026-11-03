---
article_id: 360036585153
category: NFe - Nota Fiscal Eletrônica
content_hash: fac1b8b708698727eec86a7b214f7ef6be7d452c1259af2399fcf887dfdbea0f
fetched_at: '2026-06-28T22:40:01.521314+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 629 Rejeição : Valor
  do Produto difere do produto Valor Unitário de Comercialização e Quantidade Comercial
  (nota de complemento)'
type: support-article
updated_at: '2023-10-25T19:49:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036585153--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-629-Rejei%C3%A7%C3%A3o-Valor-do-Produto-difere-do-produto-Valor-Unit%C3%A1rio-de-Comercializa%C3%A7%C3%A3o-e-Quantidade-Comercial-nota-de-complemento
---

**Dúvida**

Como corrigir a Rejeição 629: Valor do Produto difere do produto Valor Unitário de Comercialização e Quantidade Comercial (nota de complemento) ?  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A rejeição ocorre, pois a Sefaz faz a validação da **quantidade vezes a valor unitário** para chegar no valor do **produto.**

Devido não haver em algumas notas complementares**quantidade  a Sefaz retorna a rejeição, sendo assim:**

* Verifique se o XML gerou como o **exemplo abaixo:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071911993)**

**Finnfe:**

**1-** Normal  
**2-** Complementar  
**3-** Ajuste  
**4-** Devolução

1- Se gerou como FINNFE = 1 provavelmente a Nota Fiscal de origem não foi referenciada corretamente. Se esta for referenciada manualmente, preencha os campos **NF . Ori , Serie Ori** e **Item Ori**.

O preenchimento automático pelo gatilho **F4 (Nota de saída)** ou **F7 (Nota entrada)** alimenta automaticamente os campos.

2- Verificar se a nota foi **referenciada ao documento**de origem corretamente:

D2\_ITEMORI, D2\_SERIORI, D2\_NFORI **(nota de saída)**

![referecia_nt_saida.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18561634262167)

D1\_ITEMORI, D1\_SERIORI, D1\_NFORI **(nota de entrada)**

**![referecia_nt_entrada.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18561634272791)**

**Importante:**

Lembrando que a nota só é **referenciada no XML** caso exista no sistema.

Se for preenchido automaticamente pelo gatilho **F4 (Nota de saída) ou F7 (Nota entrada)** os campos são alimentados automaticamente.

Se a mesma for referenciada manualmente deve se preencher os campos **NF . Ori , Serie Ori e Item Ori** . 

É **impossível referenciar uma nota que não está no sistema**, pois este busca os dados da nota fiscal de origem nas tabelas para referenciar no XML.

Verifique se há a possibilidade de inclusão da nota fiscal de origem com a chave correta: **Entrada (F1\_CHVNFE), saída (F2\_CHVNFE)**.

Em caso de dúvidas na inclusão de nota de saída, abra um chamado no suporte Faturamento. **Se for nota de entrada, no suporte de Materiais.**

Se a nota não tiver que gerar movimentação (estoque, financeiro, etc.), gere-a pela rotina **NF MANUAL SAIDA/ENTRADA no módulo de Livros Fiscais.**

**3- Se não exclua a** nota referencie corretamente, ****após isso exclua a nota e gere novamente.****
