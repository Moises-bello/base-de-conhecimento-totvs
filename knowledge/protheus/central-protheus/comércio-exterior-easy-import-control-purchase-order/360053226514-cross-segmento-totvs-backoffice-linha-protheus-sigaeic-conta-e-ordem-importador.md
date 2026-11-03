---
article_id: 360053226514
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: b384e7881d88274ac03a7b242b995fbb2bdaeffb3106afbb23e5782ecbb864ae
fetched_at: '2026-06-28T22:39:41.130060+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Conta e Ordem
  Importador
type: support-article
updated_at: '2021-09-10T12:00:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053226514-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Conta-e-Ordem-Importador
---

**Dúvida**Como incluir o processo de conta e ordem por Importador?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**

Pré-Requisitos:

* Necessário habilitar os parâmetros com os seguintes conteúdos MV\_PCOIMPO = .T., MV\_PCOFOB = F, MV\_EIC\_PCO = T e MV\_EASY = S.
* Possuir um Solicitação de Importação cadastrada.

**Sequência 001:**

1. No Easy Import Control (SIGAEIC) acesse Atualizações/ Purchase Order/ Manutenção (EICPO400).
2. Clique em Incluir.
3. Preencha os campos obrigatórios. Na pasta Cadastrais informe a opção SIM no campo Import. C.O.? (W2\_IMPCO) e clique em Confirmar.
4. Na tela de Seleção de SI, informe a unidade requisitante e a SI cadastrada anteriormente. Clique em Confirmar.
5. Na tela de Seleção de Itens, selecione o item e clique em Confirmar.
6. Clique em Confirmar novamente.
7. Será apresentada a mensagem Confirma a gravação?, clique em SIM.
8. Será apresentada a mensagem informando que foi gerado o pedido no SIGACOM. Clique em OK.

**Sequência 002:**

1. No Compras (SIGACOM) acesse Atualizações/ Pedidos/ Pedido de Compras (MATA121).
2. Ao entrar na rotina será possível visualizar o pedido gerado.

**Sequência 003:**

1. No Easy Import Control (SIGAEIC) acesse Atualizações/ Desembaraço/ Manutenção (EICDI502).
2. Clique em Incluir, preencha os campos obrigatórios.
3. Na pasta Cadastrais veja que o campo Import. C.O.? (W6\_IMPCO) está preenchido.
4. Na pasta Outros, preencha os campos Tipo Consig.(W6\_PRO\_IMP) e CNPJ Consig.(W6\_CGC\_OUT).
5. Clique em Ações Relacionadas e clique em Itens. Dê um duplo clique no item e marque o mesmo.
6. Clique em Ações Relacionadas, em Invoice e em Incluir. Preencha os campos obrigatórios e vincule o item. Clique em Confirmar.
7. Clique em Ações Relacionadas, em seguida em Adições, clique em Ações Relacionadas novamente e em Gera. Clique em Confirmar.
8. Ao clicar em Confirmar na tela de Conferência Final será apresentada a mensagem: Confirma a Gravação?, clique em SIM.

**Sequência 004:**

1. No Easy Import Control (SIGAEIC) acesse Atualizações / Desembaraço / Pré-Nota/ Geração PV (EICCO100). Selecione o processo no qual os valores não foram gravados e clique em Pré-Nota.
2. Serão exibidos os valores correspondentes às despesas e os itens que compõem o processo.
3. Clique em Des/Marca Todas Despesas, estes irão marcar respectivamente todas as despesas do processo.
4. Clique em Grava Valores, ao apresentar a mensagem Confirma Gravação do valores? Clique em SIM.
5. O sistema irá perguntar se deseja sair da rotina, clique em Não. Retorne para a tela de Pré-Nota com Geração de PV e clique em Gerar PV.
6. Na tela de Geração de Pedido de Venda, preencha os campos Tipo do Pedido de Venda e Condição de Pagamento e clique em Confirmar.
7. Será apresentada a mensagem Confirma Gravação dos valores e geração de PV?, clique em SIM.
8. Será apresentada a mensagem: Pedido de Venda gerado com sucesso, código: 000013. Clique em Ok.
9. O status do registro passa a ser vermelho, isto é, os valores estão gravados e pedido de venda gerado.

**Sequência 005:**

1. No Easy Import Control (SIGAEIC) acesse Atualizações / Desembaraço / Pré-Nota/ Geração PV (EICCO100).
2. Selecione o processo no qual os valores foram gravados, clique em Ações Relacionadas e em seguida clique Impressao val.
3. Clique em *Preview*.
4. Será apresentado o relatório.
5. Para imprimir, clique em Imprimir. Caso contrário, clique em Sair.

**Sequência 006:**

1. No Faturamento (SIGAFAT) acesse Atualizações / Pedidos/ Pedidos de Venda (MATA410).
2. Será possível visualizar o pedido de venda gerado.

Conforme boletim: <https://tdn.totvs.com/pages/releaseview.action?pageId=6806811>
