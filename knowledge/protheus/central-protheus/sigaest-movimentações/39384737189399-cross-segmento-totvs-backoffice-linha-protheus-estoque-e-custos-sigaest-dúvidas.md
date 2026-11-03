---
article_id: 39384737189399
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 894ab733f4996cb5dfc776fdc35c8bf153a057c7b52813698de08c20b8761633
fetched_at: '2026-06-28T22:38:58.466887+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque e Custos (SIGAEST)
  - Dúvidas sobre o Campo (B2_TIPO) Tipo de Armazém
type: support-article
updated_at: '2026-03-30T12:21:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39384737189399-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Estoque-e-Custos-SIGAEST-D%C3%BAvidas-sobre-o-Campo-B2-TIPO-Tipo-de-Armaz%C3%A9m
---

O campo Tipo de Armazém (B2\_TIPO) no sistema TOTVS Protheus classifica os armazéns em três tipos: Padrão, Próprio e Terceiros, garantindo que saldos de naturezas distintas não se misturem. Transferências entre armazéns de tipos diferentes são bloqueadas para preservar a integridade fiscal e física do estoque, evitando inconsistências e problemas em obrigações fiscais como o Bloco K. A escolha do tipo depende da maturidade dos processos do cliente.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39384737186839) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Qual é a funcionalidade do campo Tipo de Armazém (B2\_TIPO), como ocorrem suas validações no sistema e por que não é possível realizar transferências entre armazéns de tipos diferentes?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
A funcionalidade do campo Tipo de Armazém (B2\_TIPO), implementado na rotina de Saldos em Estoque (MATA225), é definir e separar a natureza dos saldos armazenados pela empresa. Ele atua como uma trava de integridade para garantir que saldos de naturezas distintas não sejam misturados indevidamente.

**Existem três opções configuráveis para este campo****:**

* 1 = Padrão: Permite qualquer tipo de movimentação.
* 2 = Próprio: Permite qualquer movimentação, exceto saldo de poder de terceiros.
* 3 = Terceiros: Permite somente movimentações de poder de terceiros, que devem ser realizadas via documentos de entrada/saída com a TES configurada para esse fim.

**O módulo de Estoque (SIGAEST) possui validações ativas para o Tipo de Armazém****:**

* A rotina de Saldos (MATA225) permite a classificação do armazém.
* Nas Movimentações Internas (MATA240/MATA241), o sistema bloqueia a inclusão de movimentos internos para armazéns do tipo 3 = Terceiros.
* Os armazéns de Terceiros só aceitam movimentações via documentos fiscais.
* Em Documentos de Entrada/Saída, os armazéns do tipo 2 = Próprio bloqueiam notas fiscais que tentem movimentar poder de terceiros.

O sistema impede a transferência de saldos quando o tipo do armazém de destino é diferente do tipo do armazém de origem, apresentando o help BLOQLOC5. Essa trava existe para preservar a integridade fiscal e física do saldo. Se fosse permitida a transferência de um saldo de um armazém Próprio para um de Terceiros, ocorreria uma inconsistência grave, mascarando um saldo pertencente à empresa em um local destinado apenas a itens que não são de sua propriedade. Essa restrição evita furos de estoque e problemas em obrigações fiscais, como o Bloco K, onde distinguir posse de propriedade é fundamental.

**A orientação sobre qual tipo de armazém utilizar depende da maturidade dos processos do cliente****:**

* O tipo "Padrão" é indicado para clientes que não precisam segregar fisicamente o estoque de terceiros do estoque próprio e que desejam manter o comportamento legado do sistema.
* Os tipos "Próprio/Terceiros" são indicados para clientes com processos rigorosos de auditoria e armazéns físicos distintos para mercadorias de terceiros, como regimes de comodato ou conserto.
* Ao optar pela segregação (Próprio/Terceiros), a operação se torna mais rígida, exigindo documentos fiscais específicos para alimentar os armazéns de terceiros e impedindo que ajustes manuais simples sejam feitos via rotina de movimentos internos.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[Documentação referente a duvidas sobre o Campo (B2\_TIPO) Tipo de Armazém - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=1051247382)
