---
article_id: 4410784373399
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 7704d8ac8e068fa6d2ea6e92c6f8abc76bbe41bfe9317b0be43c453b659bc805
fetched_at: '2026-06-28T22:38:55.562718+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Help A311NAOEXCLUI
  na exclusão da Solicitação de Transferência '
type: support-article
updated_at: '2021-10-15T13:38:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410784373399-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Help-A311NAOEXCLUI-na-exclus%C3%A3o-da-Solicita%C3%A7%C3%A3o-de-Transfer%C3%AAncia
---

**Dúvida**

O sistema não permite reabrir a solicitação de transferência no momento da exclusão e apresenta o Help A311NAOEXCLUI. Como corrigir ?   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Hoje no sistema não existe uma tratativa para desfazer uma transferência efetivada que foi gerada incorretamente.  
  
O conceito do sistema não permite excluir uma transferência efetivada apresentando o help A311NAOEXCLUI.  
Não existe um método para retornar o saldo de um produto da filial destino para origem desfazendo o processo, bem como não há validações de fonte necessárias como análise de saldo, disponibilidade do produto para retorno, entre outras para que esse retorno fosse efetuado.  
  
O processo de estorno de uma movimentação de transferência entre filiais envolve a manipulação de estoques e livros fiscais em locais distintos, tem por muitas vezes, um processo burocrático atrelado. Por este motivo, o processo de estorno não é estruturado em rotina de automação e deve ser realizado pontualmente através das rotinas de exclusão de documento de entrada (na filial destino) e exclusão de documento de saída (na filial origem).

**Utilize o ponto de entrada M310ESTO para esta execução.**

**[M310ESTO - Ponto de Entrada na Confirmação do Estorno do Relacionamento entre Origem e Destino](https://tdn.totvs.com/pages/releaseview.action?pageId=516225226)**

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
