---
article_id: 360024704233
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: bcb5e8953908c044d7c9ab0575bfcf3c294623af17e3dff802c301fbc5a23416
fetched_at: '2026-06-28T22:42:44.649316+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - O que é necessário para a execução
  da rotina de Carga Máquina '
type: support-article
updated_at: '2025-02-21T20:32:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024704233-Manufatura-Linha-Protheus-SIGAPCP-O-que-%C3%A9-necess%C3%A1rio-para-a-execu%C3%A7%C3%A3o-da-rotina-de-Carga-M%C3%A1quina
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:20 min**  
**Dúvida**Quais cadastros são necessários para que a rotina **MATA690 - Carga Máquina** possa ser executada?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Para a execução do **Carga Máquina** é necessário:   
 1. **MATA010 -****Cadastro de produto**;  
 2. **MATA200 - Cadastro de estruturas** - Opcional, pois mesmo sem estrutura é possível rodar a carga máquina para o produto;  
 3. **MATA780 - Cadastro de Calendários** - O calendário é importante para definir os horários de disponibilidade semanal de um recurso, de um centro de custo ou de toda a fábrica, o objetivo principal é a alocação da carga máquina. É possível incluir exceções aos calendários através da rotina **MATA640 - Exceções aos Calendários.**  
4. **MATA610 - Cadastro de Recurso** - Recursos é qualquer elemento físico, homens, máquinas, etc, que são responsáveis pelo exercício das operações de transformação do produto.   
5. **MATA632 - Cadastro do Roteiro de Operações**- É o elemento do roteiro, da ficha de processo, de cada produto. São através das operações que o Sistema consegue alocar a necessidade de produção, os recursos, máquinas ou operadores do Sistema, em um calendário previsto.  
6. **MATA650 - Ordens de Produção -**Inclusão da Ordens de Produção;  
7. **MATA690 - Carga Máquina -** O carga máquina tem a principal função de alocar ordens de produção existentes nas devidas máquinas, recursos disponível, baseadas no cadastro de operações dos produtos e no calendário de cada uma delas. A partir do momento que uma máquina está alocada para produzir uma determinada **OP - Ordem de produção**, o padrão do Sistema assume que a mesma não poderá ser utilizada para outras operações de outras **Ops**.  
8. **Analisando a alocação** - Após a execução é apresentado gráfico de alocação no modelo de *Gantt*. As barras cinza são os tempos definidos no calendário. As barras coloridas referem-se às **Ops** alocadas. Cada subdivisão da barra colorida é uma operação alocada. Ao clicar sob uma das divisões, na parte inferior é apresentado os dados relativos à alocação da operação.  
  
**Importante** O **Carga Máquina** não leva em consideração o saldo em estoque dos componentes, para alocar as operações.
