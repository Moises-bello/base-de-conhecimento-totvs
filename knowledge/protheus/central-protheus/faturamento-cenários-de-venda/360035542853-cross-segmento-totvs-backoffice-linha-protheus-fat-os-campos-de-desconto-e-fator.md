---
article_id: 360035542853
category: Faturamento - Cenários de Venda
content_hash: 28a74188d529422fef4e2450f03846aecee8b1ba7c96d85d5745d4327ef7377a
fetched_at: '2026-06-28T22:38:33.908883+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - FAT - Os campos de Desconto
  e Fator não são preenchidos na Tabela de Preço '
type: support-article
updated_at: '2024-01-12T12:15:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035542853-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FAT-Os-campos-de-Desconto-e-Fator-n%C3%A3o-s%C3%A3o-preenchidos-na-Tabela-de-Pre%C3%A7o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20520911075479)** Tempo aproximado para leitura: **00:01:00 min**

**Duvida**

Ao preencher os campos de **Desconto - DA1\_VLRDES** e **Fator - DA1\_PERDES** eles não são gravados na tabela de preço, como habilitar?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento -  A partir da versão 11.80.  
  
**Solução**Para preencher os campos **Desconto - DA1\_VLRDES** e **Fator - DA1\_PERDES**na tabela de preço, é necessário que preencha no cadastro do Produto selecionado o campo **"Preco Venda - B1\_PRV1".**

Após preencher os campos Valor de Desconto e Fator gravam a informação digitada na tabela de preço.

![tabela_de_pre_o.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360045551234)

**Observações:**

Na inclusão da Tabela de Preços o sistema disponibiliza o preço base preenchido, sendo que os campos **Preço de Venda**e **Valor do Desconto**sempre tomarão como referência o preço base do produto.

No entanto, caso não tenha sido cadastrado, pode ser informado diretamente o valor total no campo **Preço de Venda.**

**Saiba mais:****[FAT0269\_Precificação no módulo Faturamento](https://tdn.totvs.com/pages/viewpage.action?pageId=393364250)**
