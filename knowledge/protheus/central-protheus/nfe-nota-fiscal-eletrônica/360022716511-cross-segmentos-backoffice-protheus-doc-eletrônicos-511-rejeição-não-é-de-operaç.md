---
article_id: 360022716511
category: NFe - Nota Fiscal Eletrônica
content_hash: aeaff4a01d9c1a8d2608e3df42d46ac1715d0e085d9d80e52a0fe1b10e406354
fetched_at: '2026-06-28T22:40:05.080282+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 511 Rejeição :
  Não é de Operação com Exterior e Código País destinatário difere de 1058 (Brasil)'
type: support-article
updated_at: '2025-08-12T00:07:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022716511-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-511-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-de-Opera%C3%A7%C3%A3o-com-Exterior-e-C%C3%B3digo-Pa%C3%ADs-destinat%C3%A1rio-difere-de-1058-Brasil
---

**Dúvida**

Como solucionar a 511 Rejeição : Não é de Operação com Exterior e Código País destinatário difere de 1058 (Brasil) ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para nota de saída ***(ou que utiliza cadastro de cliente):***

Se operação é uma venda interna para **estrangeiro** ao utilizar o ***CFOP iniciado por 5 é necessário que seja para consumidor final e tenha o documento do estrangeiro informado.***

***1. Verifique no cadastro de*** TES o campo ***Cod. Fiscal  "F4\_CF"***está com um ***CFOP iniciado por 5.***

***![F4_CF__2_.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414185134103)***

2- Se estiver ***preenchido com um CFOP*** iniciado por 5  no cadastro de cliente  preencher o campo Tipo ***A1\_TIPO = F (Consumidor final).***

![A1_TIPO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414185434519)

3- Preencher o documento do estrangeiro no cadastro de ***cliente no campo RG/Ced. Estr.  "A1\_PFISICA" = 5 a 20 caracteres.***

![documento_estrangeiro.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414185547159)

4 - Preencher no campo Estado ***"A1\_EST" = EX e  preencher o campo diferente de brasil  Pais "A1\_PAIS"***

![A1_EST__A1_PAIS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414199821975)

5- Deixar o campo ***CNPJ/CPF "A1\_CGC = em branco" e o campo Fisica/Jurid "A1\_PESSOA" = J- Jurídica***

![A1_CGC.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414186062231)

6 - Após isso, exclua a **nota e gere novamente.**

**Se nota de entrada ou que utilize fornecedor,** *preencher os mesmos campos no cadastro do fornecedor tabela SA2.*

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414186141463)**
