---
article_id: 36257157328023
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 285107ed5bd88b6af7bd71aaf01da4e9446742e2f8cba374aa68d74f8ad88fb5
fetched_at: '2026-06-28T22:37:22.916354+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help CNT300DCPC ao
  realizar uma Revisão de Contrato
type: support-article
updated_at: '2025-11-11T16:47:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36257157328023-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CNT300DCPC-ao-realizar-uma-Revis%C3%A3o-de-Contrato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36257157316119) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Ao realizar uma revisão de contrato com Cronograma Financeiro e reduzir parcelas através do Parâmetro de Revisão de Decréscimo ocorre o Help CNT300DCPC ao clicar na opção de "Atualizar Cronograma Financeiro/Fisico".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36257157317399)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões]

**Solução**  
O help CNT300DCPC, esta relacionado a no processo de revisão estar se tentando reduzir um número de parcelas maior ou igual ao numero de parcelas existente no Cronograma Financeiro em questão.

Por padrão do módulo, não é permitido no processo de revisão, se excluir todas as parcelas do Cronograma Financeiro para inclusão de outro Cronograma, mas somente se consegue reduzir (Decréscimo) um numero de parcelas menor que a quantidade de parcelas existentes, e caso necessário posteriormente incluir (Acréscimo) novas parcelas nessa ou em outra revisão, conforme a necessidade.

Dessa forma para que não ocorra a mensagem de help CNT300DCPC deve-se utilizar no parâmetro de revisão para decréscimo de parcelas, um número menor do que o número de parcelas existentes no Cronograma Financeiro em questão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36257157318039)

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Documentação Gestão de Contratos do TDN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441027145623)

[Guia de Referencia - Gestão de Contratos - Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=224127467)

[FAQs - Gestão de Contratos](https://tdn.totvs.com/x/O_tgDQ)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
