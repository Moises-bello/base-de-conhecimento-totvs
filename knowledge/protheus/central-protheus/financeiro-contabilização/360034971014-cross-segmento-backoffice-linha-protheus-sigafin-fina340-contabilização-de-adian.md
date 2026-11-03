---
article_id: 360034971014
category: Financeiro - Contabilização
content_hash: 39b652349f764e8ced139c1f5221ea307f73c46c15fb524808f89c07b88965b2
fetched_at: '2026-06-28T22:38:05.275083+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA340 - Contabilização
  de adiantamento a fornecedor
type: support-article
updated_at: '2023-05-31T14:09:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034971014-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA340-Contabiliza%C3%A7%C3%A3o-de-adiantamento-a-fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00min****Dúvida**Como contabilizar o adiantamento a fornecedor?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – A partir da versão 12  
  
**Solução**Considerado apenas uma regra contábil de mercado, o sistema contabiliza apenas da seguinte forma abaixo:   
  
Por **Pagamento Adiantado** (Inclusão do Adiantamento)

```
Lançamento Padrão 513  
Débito - Adiantamento a Fornecedores (Ativo) - Tabela SED  
Crédito - Caixa ou Banco (Ativo) - Tabela  SA6
```

Por **Recebimento da mercadoria** – (Emissão do tipo: NF) utilize o Lançamento Padrão 510 ou Lançamento Padrão 650:  
**Para entrada da nota Fiscal**

```
Lançamento Padrão 650  
Débito- Estoque/Imobilizado (Ativo) Tabela SB1  
Crédito - Fornecedores (Passivo) -Tabela  SA2
```

OU   
**Para inclusão manual do tipo: NF no Financeiro**

```
Lançamento Padrão 510  
Débito- Materiais Diversos (Ativo) Tabela SED  
Crédito - Fornecedores (Passivo) -Tabela  SA2
```

Por **Compensação**/**baixa das contas de fornecedores** feita pela rotina **FINA340:**

```
Lançamento Padrão 597  
Débito - Fornecedores (Passivo) - Tabela SA2  
Crédito - Adiantamento a Fornecedores (Ativo) - Tabela SED
```

**Importante**Caso seja necessário contabilizar de outras formas, será necessário criar novas sequências dos lançamento padrão.  
  
**Saiba mais**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Lançamentos Padrão no Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6367404603031)  
[FIN0007\_LPAD\_Lançamento\_padrão\_financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=235585410)
