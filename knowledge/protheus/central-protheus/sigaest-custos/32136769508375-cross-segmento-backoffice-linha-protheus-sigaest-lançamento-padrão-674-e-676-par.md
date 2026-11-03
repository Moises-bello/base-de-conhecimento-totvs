---
article_id: 32136769508375
category: SIGAEST - CUSTOS
content_hash: 87ec57a3216f8702bdf6e25815453ecadf87110f0b34de57d3b193ae70ebf659
fetched_at: '2026-06-28T22:39:02.000138+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Lançamento Padrão
  674 e 676 particularidades importantes
type: support-article
updated_at: '2025-05-16T11:25:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32136769508375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Lan%C3%A7amento-Padr%C3%A3o-674-e-676-particularidades-importantes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32136746988567) Tempo aproximado para leitura: **00:02:45 min**

**Dúvida**

Quais as particularidades dos Lançamentos Padrões 674 e 676, **visto que esses Lançamentos Padrões são contabilizados de forma ON-LINE** porém, utilizando o parâmetro MV\_CUSMED igual a M (Mensal)? O que deve ser considerado para utilização desses Lançamentos Padrões?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Solução**

Os Lançamentos Padrões 674 e 676 são utilizados por empresas que preferem efetuar os **Ajustes de inventário,** **após o processamento do CUSTO MÉDIO** **e antes do Fechamento**, com a funcionalidade da pergunta do processamento de Inventário **"Atualiza Saldo do Fechamento"** igual a **"Sim"** (print abaixo) que atualiza a **CT2 com o Custo já apurado** pelo processamento do Custo Médio e também atualiza os **campos B2\_QFIM, B2\_VFIM1 e B2\_CMFIM1**. Dessa forma não há necessidade de recalcular o CUSTO MÉDIO para em seguida efetuar o Fechamento do período.

Para cenários diferentes desse modelo relatado acima, precisa utilizar o **Lançamento Padrão 666 para Requisição de Saldos** e **Lançamento Padrão 668 para Devoluções de Saldos**.  
  
Dúvida em como contabilizar estoque, veja [***nesse link***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405082704791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-Contabilizar-as-Movimenta%C3%A7%C3%B5es-no-Estoque-Custos) exemplo de configuração.   
  
Também veja [***nesse link***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020801392-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-C%C3%B3digos-dos-Lan%C3%A7amentos-Padronizados-do-Estoque) os Lançamentos Padrões de Estoque.

![mata340 .jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/32139694987543)

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre CUSTOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[SIGAEST - Quais os Códigos dos Lançamentos Padronizados do Estoque?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020801392-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-C%C3%B3digos-dos-Lan%C3%A7amentos-Padronizados-do-Estoque)

[SIGAEST - Como Contabilizar as Movimentações no Estoque Custos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405082704791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-Contabilizar-as-Movimenta%C3%A7%C3%B5es-no-Estoque-Custos)
