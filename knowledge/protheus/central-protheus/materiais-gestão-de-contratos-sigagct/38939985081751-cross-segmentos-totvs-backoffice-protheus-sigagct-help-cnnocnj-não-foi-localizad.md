---
article_id: 38939985081751
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 79901efbebd7ba7125816547779df4fe527d1562f36b878bdc9e27dd3866667e
fetched_at: '2026-06-28T22:37:22.984216+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help: CNNOCNJ – Não
  foi localizado cadastro de Documentos x Situação para o tipo de contrato XXX ao
  alterar a situação do Contrato'
type: support-article
updated_at: '2026-03-10T18:13:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38939985081751-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CNNOCNJ-N%C3%A3o-foi-localizado-cadastro-de-Documentos-x-Situa%C3%A7%C3%A3o-para-o-tipo-de-contrato-XXX-ao-alterar-a-situa%C3%A7%C3%A3o-do-Contrato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38939985051287) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
  
Help: **CNNOCNJ** – Não foi localizado cadastro de Documentos x Situação para o tipo de contrato XXX ao alterar a situação do Contrato

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38939985053719)

**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Causa:**

O help ocorre , pois o campo **Ctr. Dt Doc (CN1\_CTRDOC)** está preenchido com **= 1 - Sim** no Cadastro de **Tipos de Contrato**(CNTA021)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38940030371095)

**Solução**  
  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Será necessário acessar a rotina **Documentos x situações**(CNTA210) e  cadastrar o Tipo de contrato na situação Vigente ou nas demais situações que necessita.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38940030371991)  
**Obs:** Para cadastrar o Tipo Doc conforme imagem acima acesse Cadastros>Tipos>Documentos(CNTA060)

2. Caso não tenha necessidade de utilizar o Controle de Documentos no contrato ajuste o campo **Ctr. Dt Doc (CN1\_CTRDOC) = 2 - Não** no Cadastro de **Tipos de Contrato**(CNTA021)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38939985063959)

**Saiba Mais :**

[**Artigos Materiais - Gestão de Contratos - (SIGAGCT)**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
