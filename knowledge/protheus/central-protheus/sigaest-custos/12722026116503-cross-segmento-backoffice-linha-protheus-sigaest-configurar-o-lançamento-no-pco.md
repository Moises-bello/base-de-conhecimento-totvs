---
article_id: 12722026116503
category: SIGAEST - CUSTOS
content_hash: a632ebb322973422173ffeb7abe0a1d363f8ac52958f44ef31e1a95917497a49
fetched_at: '2026-06-28T22:39:00.834645+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configurar o lançamento
  no PCO movimento de estorno
type: support-article
updated_at: '2025-03-12T12:23:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12722026116503-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configurar-o-lan%C3%A7amento-no-PCO-movimento-de-estorno
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28793763516311) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**

No módulo Estoque e Custos, ao efetuar o processo de estorno de uma movimentação interna, o lançamento no PCO não é estornado.  
**Ambiente**

Microsiga Protheus – Estoque e Custos – A partir da versão 12.1.33  
  
**Causa**

Há casos em que o estorno/exclusão do movimento não tem a mesma chave de inclusão, como por exemplo o processo 000151, onde a opção ***Estornar ?***(AKB\_ESTORN) na configuração de Lançamentos por Processo(**PCOA030**), mesmo marcada como "SIM", não terá efeito.  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. No módulo **SIGAPCO**, acessar a rotina **PCOA030**;

2. Cadastrar o lançamento **000151**;

3. Sugerimos que nesse caso para cada item, sejam criados duas sequencias, cada uma com ***Tipo*** (AKC\_TIPO) diferente, tratando a inclusão do movimento e um outro o estorno;

**Lançamento para Movimento de Devolução e de Estorno de Requisição:**

![credito.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12723557099799)

**Lançamento para Movimento de Requisição e de Estorno de Devolução:**

![debito.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12723534861719)

4. Realizar o estorno da movimentação interna, seja ela de requisição ou devolução;

5. Com isso o lançamento original será mantido no PCO e gerado um novo lançamento de estorno (Débito e Crédito).

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os Códigos dos Lançamentos Padronizados do Estoque?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020801392-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-C%C3%B3digos-dos-Lan%C3%A7amentos-Padronizados-do-Estoque-)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como Contabilizar as Movimentações no Estoque Custos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405082704791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-Contabilizar-as-Movimenta%C3%A7%C3%B5es-no-Estoque-Custos)*
