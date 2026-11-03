---
article_id: 360045767373
category: esocial - Processos
content_hash: 6f9d61808f0dd437c904d889965ce73b5350d80fcdc0bd2edfae5f86234d6493
fetched_at: '2026-06-28T22:47:08.317286+00:00'
product: rm
section_id: 1500000834441
source: central-rm
title: RH - RM - FOP - eSocial - Carga inicial de funcionários demitidos
type: support-article
updated_at: '2024-06-27T18:53:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045767373-RH-RM-FOP-eSocial-Carga-inicial-de-funcion%C3%A1rios-demitidos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24483318488983) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**  
Como gerar no sistema o processo de Carga Inicial Funcionários Demitidos?  
  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. No módulo Folha de Pagamento acesse **eSocial | Outros processos | Carga Inicial Funcionários Demitidos** e preencha os campos abaixo, será possível filtrar por **Período da Rescisão** e/ou **Período do último movimento.**

![teste.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062871334)

2. Em seguida, localize os gatilhos gerados na Fila de Eventos, gere o XML e integre com o TAF para transmitir ao eSocial.

Neste processo, serão gerados os gatilhos dos eventos não periódicos [S-2200 – Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=452719244)  e [S-2300 – Trabalhador Sem Vínculo de Emprego/Estatutário - Início](https://tdn.totvs.com/pages/viewpage.action?pageId=364908534)  para a [Fila de Eventos](https://tdn.totvs.com/display/LRM/Fila+de+Eventos) dos funcionários demitidos anterior a data de obrigatoriedade do eSocial.   
  
**Importante**  
Na seleção de Funcionários por default, somente será consistida a situação **D - Demitidos**, os demais dados de seleção (Tipo de Funcionário, Código de Recebimento, Fórmulas e Filtros) poderão ser realizados da maneira desejada.

Quando há rescisão complementar e a data de último movimento for alterada, o processo poderá ser filtrado para considerar o limite entre **Período da Rescisão** e **Período do último movimento**. Para que ocorra desta forma deve-se selecionar os dois períodos.  
  
**Saiba mais**  
Para maiores informações, acesse:  
     • [Carga Inicial Funcionários Demitidos](https://tdn.totvs.com/pages/releaseview.action?pageId=452719755)
