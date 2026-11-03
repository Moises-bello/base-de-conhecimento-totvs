---
article_id: 35827873184535
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 6c625d118cab7bb2e66860c9c7cae87f8cdd486d3befcc9ace6c19d1c6cdc993
fetched_at: '2026-06-28T22:38:33.061836+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Qual a funcionalidade da
  rotina Contas de Vendedores (FATA520)?
type: support-article
updated_at: '2025-10-24T12:25:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35827873184535-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Qual-a-funcionalidade-da-rotina-Contas-de-Vendedores-FATA520
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35827873175575) Tempo aproximado para leitura: **00:01:30 min**  
  
  
**Dúvida**  
Qual a funcionalidade da rotina Contas de Vendedores (FATA520)?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**  
  
Esta rotina permite a associação dos suspects, prospects e clientes aos respectivos vendedores, controlando a quantidade deles. Também é possível controlar quantas oportunidades e propostas.

O controle de contas é totalmente transparente, não necessitando de qualquer manutenção por parte dos operadores.

Sempre que um suspect for incluído e associado a um representante, este suspect passa a contar como um dos suspects associados ao representante.

A partir da qualificação do suspect pode ser gerada uma oportunidade para um determinado representante. Na geração da oportunidade, o suspect é convertido para prospect.   
  
Caso o suspect estivesse associado ao representante, seu registro será alterado, caso contrário, será incluído o código do novo prospect na conta do representante, assim como o código da oportunidade gerada.

Para todos os clientes com oportunidade de vendas em aberto será incluído um registro daquele cliente na conta do representante associado à oportunidade. Assim que a oportunidade for finalizada, independente do motivo da finalização, o cliente sai da conta do representante.  
  
  
***Importante:***

O botão "Reprocessa" tem por objetivo recriar o cadastro de Vendedores x Entidades.  
A rotina irá excluir todos os vínculos da tabela **ADL - Controle de Conta do Vendedor** e criá-los novamente conforme amarração entre o vendedor, cliente, prospects e suspects.  
O reprocessamento é executado apenas quando as [Estruturas de Vendas (FATA070 - SIGAFAT)](https://tdn.totvs.com/pages/viewpage.action?pageId=359468427) estiverem configuradas.

**Saiba mais:**

[**Contas de Vendedores (FATA520 - SIGAFAT)**](https://tdn.totvs.com/pages/releaseview.action?pageId=359468945)
