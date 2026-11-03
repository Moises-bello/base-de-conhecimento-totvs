---
article_id: 19551316517015
category: SIGAACD - Automação e Coleta de Dados
content_hash: 663c00efb12e05f39709d7c2fbf2b17188b0e668d89a9112726cff12a2fb1a0a
fetched_at: '2026-06-28T22:39:12.730866+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Existem outros Operadores
  em Andamento, a quantidade informada finaliza o saldo da Operação. '
type: support-article
updated_at: '2023-12-04T18:03:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19551316517015-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Existem-outros-Operadores-em-Andamento-a-quantidade-informada-finaliza-o-saldo-da-Opera%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19551370609303) Tempo aproximado para leitura: **00:02:00 min****Dúvida**O que fazer quando ocorrer a mensagem "Existem outros Operadores em Andamento, a quantidade informada finaliza o saldo da Operação" na rotina ACDV025?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -Estoque/Custos - Todas as versões.  
  
**Solução**Quando ocorrer a mensagem do Print abaixo na rotina ACDV025 é necessário verificar o seguinte ponto:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19551316493591)

* Acessar a rotina Transações da Produção(ACDA070) e configurar uma das operações dessa forma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19551338158103)

Dessa forma no momento de apontar é necessário selecionar o outro operador para apontar em conjunto a determinada operação, selecionando a tecla Enter e depois a tecla ESC para confirmar a operação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19551370622359)

Ao selecionar o operador é necessário finalizar a operação com sucesso.

**Pontos de Atenção:**

* Verificar os parâmetros [MV\_GANHOPR](https://tdn.totvs.com/display/public/PROT/MV_GANHOPR) e o [MV\_PERCPRM](https://tdn.totvs.com/pages/releaseview.action?pageId=389549440)
* Temos também o ponto de entrada [ACD023VQ](https://tdn.totvs.com/pages/releaseview.action?pageId=6091029)

**Saiba Mais:**  
*[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*

*[ACDV025 - Produção PCP Mod II - Processo de ganho de produção](https://tdn.totvs.com/pages/releaseview.action?pageId=527001583)*
