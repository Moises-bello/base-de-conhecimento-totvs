---
article_id: 5750313588759
category: Manutenção de Ativos (SIGAMNT)
content_hash: dcebd3b7044430faba9c62546ada73f9e3842d4c35d09abffc2b21fdeb6c5e8a
fetched_at: '2026-06-28T22:42:33.201493+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Funcionamento do controle da garantia de
  insumos
type: support-article
updated_at: '2022-04-29T18:01:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5750313588759-Manufatura-Linha-Protheus-MNT-Funcionamento-do-controle-da-garantia-de-insumos
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como funciona o controle da garantia de insumos?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**O **SIGAMNT - Manutenção de Ativos** permite o controle da garantia dos insumos utilizados nas **O.S. - Ordens de Serviço**. Dessa forma, o usuário pode monitorar a garantia das peças de reposição, mão de obra e terceiros utilizados na manutenção de seus ativos.  
  
O controle de garantia é alimentado no momento da informação da realização dos insumos de uma **O.S.** Ao indicar que um insumo possui controle de garantia, através do campo **TL\_GARANTI -** **Tem Garantia** igual a **S - Sim**, é apresentada uma tela onde é possível informar suas características, como localização e tipo podendo ser por tempo ou contador.  
  
A utilização de garantia também pode ser indicada no cadastro de um **Bem**, na aba de **Peças de Reposição**, ou no cadastro de uma **Manutenção**, na informação de seus **Insumos**.  
  
Quando existe integração com o módulo **SIGAEST - Estoque e Custos**, é possível realizar insumos através de um **Documento de Entrada - MATA103**. Neste caso, para utilizar a garantia no insumo descrito no documento, basta preencher o campo **D1\_GARANTI -** **Tem Garantia** igual a **S**, que a mesma tela para informação das características da garantia do **SIGAMNT** será apresentada. É importante que o código da **O.S.** seja preenchido nos campos **D1\_OP** - **Ord. Produção** e **D1\_ORDEM** - **Ordem Serviço** para o correto vínculo entre a **Ordem** e o **Insumo**.  
  
Ao informar que o consumo de um insumo está dentro do prazo de garantia, o**SIGAMNT** alerta o operador sobre a ocorrência.  
  
Adicionalmente, o usuário poderá controlar os insumos em garantia, através do relatório disponível para este fim. A opção encontra-se em **Relatórios/Outros/Prod. Em Garantia** - **MNTR720**.
