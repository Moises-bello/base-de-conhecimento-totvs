---
article_id: 40954214000791
category: Rental by ItUp Business
content_hash: 1253a099e8c8a8b23eaeb87ec07c817955e950250e544c16ee169f80e01187b1
fetched_at: '2026-06-28T22:36:20.710245+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Visão Geral e Parâmetros
  do Faturamento Automático
type: support-article
updated_at: '2026-06-05T11:52:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40954214000791-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Vis%C3%A3o-Geral-e-Par%C3%A2metros-do-Faturamento-Autom%C3%A1tico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40954213988375) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como acessar o processo de Faturamento Automático e quais são as opções e regras de tipo de faturamento disponíveis?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões  
  
**Solução**  
Após o envio do equipamento, é possível realizar o faturamento da locação de forma automática, conforme as regras configuradas no projeto e nos parâmetros.

O acesso ao Faturamento Automático pode ser feito por dois caminhos:

* **Manutenção de Projeto:** Através da opção Outras Ações > Faturamento Automático, disponível na tela de Manutenção de Projeto.
* **Menu do Sistema:** Atualizações > Comercial > Faturamento Automático.

No filtro da rotina, é possível delimitar a geração utilizando parâmetros de Datas, Cliente, Loja, Equipamento, Projeto, Produto e Obra. O principal parâmetro a ser observado é o **Tipo do Faturamento**, que define a regra de tratamento conforme o cenário selecionado:

1. **Locação:** Utilizado para cenários de Locação, Cobrança Única e Outros, bem como para Custo Extra quando o parâmetro "Junto = Sim". O faturamento do custo extra ocorre integrado ao principal.
2. **Custo Extra (Junto = Não):** Exclusivo para custo extra. O faturamento é realizado de forma separada da locação, gerando documentos distintos.
3. **Locação e Custo Extra:** Permite o faturamento conjunto, respeitando as regras de cada cenário.
4. **Pro rata Quantitativa (Devolução Parcial):** Aplicado em cenários de Devolução Parcial, considerando a quantidade efetivamente utilizada. Deve ser selecionada isoladamente.
5. **Locação, Custo Extra e Pro rata Quantitativa:** Trata os três tipos conjuntamente em um único processamento, quando aplicável.
6. **Somente Locação:** Fatura apenas os itens de locação, desconsiderando Custo Extra ou Pro rata, indicado para cobrar apenas valores fixos.

**Importante:** Na tela de parâmetros, a opção de "Seleção" como "SIM" deve ser utilizada apenas quando as opções "LOCAÇÃO" ou "CUSTO EXTRA" forem selecionadas separadamente. Quando "NÃO", todos os itens do projeto serão enviados para o Pedido de Venda.
