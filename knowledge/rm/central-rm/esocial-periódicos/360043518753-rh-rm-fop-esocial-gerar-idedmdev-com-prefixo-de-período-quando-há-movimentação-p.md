---
article_id: 360043518753
category: esocial - Periódicos
content_hash: 4236dea520c8c2e61ac29ad112cebd7c5d87bbb49938eef2a674c848e94db9cc
fetched_at: '2026-06-28T22:47:09.413085+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Gerar ideDmDev com prefixo de período quando há movimentação
  para autônomos do Totvs Gestão Financeira com categorias diferentes e mesmo CPF
type: support-article
updated_at: '2023-06-14T10:59:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043518753-RH-RM-FOP-eSocial-Gerar-ideDmDev-com-prefixo-de-per%C3%ADodo-quando-h%C3%A1-movimenta%C3%A7%C3%A3o-para-aut%C3%B4nomos-do-Totvs-Gest%C3%A3o-Financeira-com-categorias-diferentes-e-mesmo-CPF
---

**Dúvida**Como gerar a tag **ideDmDev** com prefixo período quando há movimentação para autônomos do **Totvs Gestão Financeira** com categorias diferentes e mesmo CPF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Quando existe cadastro de autônomos que tem múltiplos vínculos cadastrados e possuem lançamentos no mesmo período de pagamento, a tag **ideDmDev** é gerada em duplicidade. Desta forma foi criado o campo prefixo período para diferenciar o período de pagamento a ser enviado para cada autônomo. Para correta geração siga os passos abaixo:

1. Acesse **Folha de Pagamento | Administração de Pessoal | Cliente e Fornecedor | Anexos | eSocial**;  
2. Insira no campo **Prefixo Período** para o **cliente/fornecedor** este campo poderá ser preenchido com letras ou números;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058070894/mceclip0.png)

3. Feito o lançamento financeiro basta gerar o xml  em **Folha de Pagamento | eSocial | Gerar XML**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058071114/mceclip1.png)

3.1. Conforme cadastro no passo 2 o **Prefixo Período** "A" a tag **idDmDev** irá gerar o prefixo inserido no cadastro + o número 1 que é o período padrão de geração dos lançamentos financeiros;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058071214/mceclip2.png)

**Importante**Para correta geração do XML, caso o autônomo possua 3 ou mais cadastros com lançamentos financeiros somente um deles poderá ficar sem Prefixo de Período preenchido  
  
**Saiba** **mais**Para maiores detalhes sobre o processo acesse [Como](https://tdn.totvs.com/pages/releaseview.action?pageId=532649418#1-1) [gerar a tag ideDmDev com prefixo período quando há movimentação para autônomos do Totvs Gestão Financeira com categorias diferentes e mesmo CPF?](https://tdn.totvs.com/pages/releaseview.action?pageId=532649418#1-1)
