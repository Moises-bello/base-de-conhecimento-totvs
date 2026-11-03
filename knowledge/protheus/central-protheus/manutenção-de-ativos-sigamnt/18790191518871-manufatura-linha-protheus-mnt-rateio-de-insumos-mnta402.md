---
article_id: 18790191518871
category: Manutenção de Ativos (SIGAMNT)
content_hash: b97296743f8fc2fb647b96679896ff7757c59a9e18d16a328e6e2259d4aa8572
fetched_at: '2026-06-28T22:42:34.377989+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Rateio de Insumos - MNTA402
type: support-article
updated_at: '2023-11-06T15:08:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18790191518871-Manufatura-Linha-Protheus-MNT-Rateio-de-Insumos-MNTA402
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18790170276119) Tempo aproximado para leitura: **00:01:50 min** **Dúvida**Qual é o objetivo da rotina **Rateio de Insumos - MNTA402**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**No ambiente **Manutenção de Ativos**, por meio das opções **Atualizações / Retorno Ordem de Serviço - O.S / Rateio de Insumos**, é possível visualizar esta rotina.  
A rotina tem por objetivo possibilitar rateio de horas reportadas de insumos do tipo **Ferramenta**, **Mão-de-obra** e **Terceiro** para diversas ordens de serviços que podem ser selecionadas pelo usuário.  
Os insumos serão divididos de acordo com a formula: **Tempo / Quantidade de O.S.** Assim cada insumo será dividido entre as ordens selecionadas, não podendo ter quantidade inferior a 1 minuto por **O.S**. - **Ordem de Serviço**Procedimento para rateio de **O.S.**:

1. No módulo **Manutenção de Ativos - SIGAMNT**, opções **Atualizações / Controle de Oficina / Bens / Bens - MNTA080**, inclua um bem.
2. Em **Atualizações / Controle de Oficina / Manutenção / Manutenção - MNTA120**, inclua uma manutenção para o bem.
3. Em **Atualizações / Controle de Oficina / Ordem de Serviço - MNTA420**, inclua duas **O.S.'s**: uma **Corretiva** e a outra **Manual**, para o bem incluído no passo 1, com situação **L - Liberada**.
4. Em**Atualizações / Controle de Oficina / Retorno / Simplificado**, clique na opção **Rateio** e verifique que as **O.S's** incluídas no passo 3, estão no *browse*.
5. Selecione as **Ordens de Serviço** e informe um insumo, que pode ser **Mão-de-obra**, **Ferramenta** ou **Terceiro**. Confirme a tela.
6. Repita o procedimento anterior, clicando na opção **Finalizar**.
7. Verifique que ao exibir a janela para informar dados sobre a **O.S**, o campo **Irregularidade**será obrigatório apenas para a **O.S Corretiva**.
