---
article_id: 360035902494
category: Comércio Exterior - Easy Import Control - Licença de Import
content_hash: 26b5d0acc02e71c3465d576caae1f4c35ae0d967a13aeaec31034ae0ff0bb3ad
fetched_at: '2026-06-28T22:39:42.729726+00:00'
product: protheus
section_id: 1500001549682
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - REJEIÇÃO 334
type: support-article
updated_at: '2022-06-02T12:20:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035902494-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-REJEI%C3%87%C3%83O-334
---

**Dúvida**Como corrigir a Rejeição 334?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – Todas versões  
  
**Solução**Deve ser informado o ato concessório na PLI para os itens anuentes.  
O sistema trata a PLI (Pedido da Licença de Importação) da seguinte forma:  
- O item deve ser anuente, podendo ser alterada a anuência no Purchase Order;  
- A PLI é obrigatório antes de se montar o embarque, pode ser complementada a informação do número da LI após o embarque na fase de Manutenção LI.

Como cadastrar um Pedido de Licença de Importação (PLI):  
1. Selecione o menu Atualizações\ Licença de Import\ Manutenção PLI.  
2. Clique na opção Incluir e preencha as informações da "PLI, o número de "PLI" é de controle do operador, podendo ser utilizado o número de pedido, deve ser informado o número do "Ato concessório" na capa da PLI - campo: W4\_ATO\_CON.  
3. Clique sobre o botão PO de Referência e selecione o pedido, em ações relacionadas.  
4. Clique sobre o botão Ok para confirmar. O sistema apresentará a tela para seleção de itens.  
5. Ao marcar o item com um duplo clique ou através do botão Marca/Desmarca Todos, o sistema apresentará a tela para definição dos dados do item, necessário informar pelo liquido unitário e peso bruto unitário.  
6. Confira os dados e clique sobre o botão Confirmar.  
7. Clique sobre o botão Confirmar para gravar.

Lembrando que para os itens anuentes (Drawback) é obrigatório ter PLI, após o preenchimento da PLI será possível prosseguir com o em Embarque, e realizar posteriormente a manutenção da LI, informando o número de LI. Com campo W4\_ATO\_CON ao gerar a pré-nota, o campo WN\_AC será gravado com o número do ato concessório.
