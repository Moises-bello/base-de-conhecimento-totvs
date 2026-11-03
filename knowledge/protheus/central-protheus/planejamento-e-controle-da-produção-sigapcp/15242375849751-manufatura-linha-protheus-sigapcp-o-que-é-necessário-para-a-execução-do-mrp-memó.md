---
article_id: 15242375849751
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: c221ee258baf4da20568958861ae45f5cd7f88ebd5672e5fade097d07e96447b
fetched_at: '2026-06-28T22:42:44.654924+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - O que é necessário para a execução
  do MRP memória
type: support-article
updated_at: '2023-06-13T14:03:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15242375849751-Manufatura-Linha-Protheus-SIGAPCP-O-que-%C3%A9-necess%C3%A1rio-para-a-execu%C3%A7%C3%A3o-do-MRP-mem%C3%B3ria
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15242331556375) Tempo aproximado para leitura: **00:03:35 min  
  
Dúvida**Quais cadastros são necessários para que a rotina **PCPA712- MRP Memória**possa ser executada?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**O novo **MRP - Material Requiriment Planning** foi projetado para ser executado em memória e sem acessar nenhuma tabela no **ERP Protheus** durante seu processamento. Para isso, é preciso realizar alguns procedimentos, antes da execução do programa, que será descrito a seguir:   
  
**1. PCPA139 - Parâmetros de integração do MRP -** Nesse programa é feita a ativação do novo **MRP** e a configuração das *API's*, que fazem a atualização dos dados entre o Sistema e o **MRP**. Para cada *API* disponível, será configurada se a execução será *online* ou via *schedule*.  
  
**2. PCPA141 - Configuração de integração do MRP por *Schedule* -** Para as *API's* que foram configuradas para atualizar via *schedule*, é preciso cadastrar no agendador, via **SIGACFG - Configurador**.  
  
**3. PCPA140 - Sincronização -** Nesse programa é feita a sincronização inicial dos dados entre o Sistema e o **MRP.** Após realizar essa sincronização, o sistema mantém os dados atualizados por meio das *API's*, conforme configurado na etapa 1, para aqueles que tem o campo **Tipo Exec** preenchido com *Online* .   
  
**4. PCPA131 - Calendário MRP -** Nesse programa é cadastrado o calendário do **MRP**. O novo programa utiliza um calendário separado do que já existe no **SIGAPCP**. O **MRP** utiliza os dados cadastrados nesse programa para realizar os cálculos de *leadtime* dos produtos.  
  
**5. PCPA136 - Demandas do MRP -** Nesse programa são centralizadas todas as demandas que o **MRP** pode considerar, sendo possível realizar a importação de pedidos de venda, plano mestre de produção, previsões de vendas, demandas originadas no **SIGAPMS - Gestão de Projetos** e importação via arquivo  de extensão CSV. Também é possível cadastrar demandas manuais, em que não tenha nenhuma origem citada anteriormente.   
É com base nessas demandas que o **MRP** realiza o cálculo das necessidades dos produtos, além da posição de estoque de cada item e das políticas de estoque  
  
**6. PCPA712 - MRP Memória -** Após ter feito as etapas citadas anteriormente, o novo **MRP** pode ser executado.   
  
**7. PCPA144 - Documentos do MRP** ou **Resultados do MRP através da tela PO UI -** O novo **MRP** gera as necessidades de produção e disponibiliza os valores para serem analisados através desses programas. Após a análise, é possível realizar a geração dos documentos.  
  
**Saiba mais**  
Para mais informações sobre as rotinas descritas a acima, acesse:  
[Parâmetros de integração MRP - PCPA139](https://tdn.totvs.com/pages/releaseview.action?pageId=493617705)  
[Configuração de integração do MRP por SCHEDULE - PCPA141](https://tdn.totvs.com/pages/releaseview.action?pageId=506393943)  
[Sincronizador do MRP - PCPA140](https://tdn.totvs.com/display/public/PROT/Sincronizador+do+MRP+-+PCPA140)  
[Calendário MRP - PCPA131](https://tdn.totvs.com/pages/releaseview.action?pageId=420549568)  
[Demandas do MRP - PCPA136](https://tdn.totvs.com/display/public/PROT/Demandas+do+MRP+-+PCPA136)  
[MRP (em Memória) - PCPA712](https://tdn.totvs.com/pages/releaseview.action?pageId=501460101)  
[Geração de Documentos - PCPA144](https://tdn.totvs.com/pages/releaseview.action?pageId=569483982)  
[Resultados do MRP](https://tdn.totvs.com/display/public/PROT/Resultados+do+MRP)
