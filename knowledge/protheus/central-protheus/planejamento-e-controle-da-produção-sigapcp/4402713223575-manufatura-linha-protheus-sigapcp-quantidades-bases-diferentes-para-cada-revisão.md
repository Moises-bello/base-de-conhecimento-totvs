---
article_id: 4402713223575
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 1d4550385d6bb2e0f2d81906c484375a3aec533d7ce3f9098ea02b5ce1e4cf51
fetched_at: '2026-06-28T22:42:45.821280+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Quantidades bases diferentes para cada
  revisão de estrutura
type: support-article
updated_at: '2025-01-17T19:42:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402713223575-Manufatura-Linha-Protheus-SIGAPCP-Quantidades-bases-diferentes-para-cada-revis%C3%A3o-de-estrutura
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29317447789207)***Tempo aproximado para leitura: **00:01:21 min**  
**Dúvida**É possível ter quantidades bases diferentes para revisões de estruturas diferentes no **MATA200 - Cadastro de Estruturas** ou **PCPA200 - Manutenção de Estruturas**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Não é possível ter uma quantidade base diferente para cada revisão da estrutura. A informação da quantidade base fica registrada no campo **B1\_QB - Quantidade Base da Estrutura** da tabela **SB1 - Descrição Genérica de Produto** ou no campo **BZ\_QB - Quantidade Base da Estrutura** da tabela **SBZ - Indicadores de Produtos**, de acordo com o parâmetro **MV\_ARQPROD - O parâmetro configura se os de indicadores de produtos serão considerados pela tabela SB1 ou se serão considerados pela da tabela SBZ.**Para alterar a quantidade base que será utilizada no cálculo dos empenhos ao gerar os empenhos pela rotina **MATA650 - Ordem de Produção**, pode-se utilizar o ponto de entrada **MQTBASEST.****Saiba mais**A documentação sobre o ponto de entrada **MQTBASEST** encontra-se disponível no *link*: [MQTBASEST - Altera quantidade base da estrutura](https://tdn.totvs.com/display/PROT/MQTBASEST+-+Altera+quantidade+base+da+estrutura)
