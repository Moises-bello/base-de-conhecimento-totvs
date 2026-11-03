---
article_id: 37697972721431
category: Financeiro - Comissão
content_hash: f618e0cbc6835eec380ca208561af9d3f1fac3f5cac124b08935d65321d8c7ba
fetched_at: '2026-06-28T22:37:50.675922+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - MATA530 - Help: Existem fornecedores
  sem natureza cadastradas'
type: support-article
updated_at: '2026-01-15T14:45:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37697972721431-Cross-Segmento-Backoffice-Linha-Protheus-MATA530-Help-Existem-fornecedores-sem-natureza-cadastradas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37697972703639) Tempo aproximado para leitura: **00:05 min**  
  
**Ocorrência**  
Quando executado a rotina de atualização de pagamento de comissão é exibido a mensagem "Existem fornecedores sem naturezas cadastradas. Deseja gerar um arquivo com a relação destes fornecedores"?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37697972704151)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210.  
  
**Causa**  
Na atualização do backoffice realizada em 11/12/2025, foi implementado um ajuste no processo de atualização de comissões. A partir dessa alteração, tornou-se obrigatória a vinculação de uma natureza financeira no cadastro do fornecedor para o qual a comissão será gerada.  
  
**Solução**

Para regularizar o processo, é necessário acessar o cadastro de fornecedores, selecionar a **aba Admin/Fin.** e informar no **campo Natureza** a natureza financeira correspondente à geração da comissão.

Após essa configuração, execute novamente a rotina de pagamento de comissões para que os pagamentos sejam devidamente processados.

**Saiba mais sobre a nova mudança**

[Cross Segmento - Backoffice Linha Protheus - FINA440 - Como ajustar o valor da comissão?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36581426178711-Cross-Segmento-Backoffice-Linha-Protheus-FINA440-Como-ajustar-o-valor-da-comiss%C3%A3o)
