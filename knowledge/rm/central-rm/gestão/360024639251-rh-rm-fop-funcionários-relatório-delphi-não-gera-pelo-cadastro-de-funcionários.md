---
article_id: 360024639251
category: Gestão
content_hash: 35f24c10ae5265bf2dc04be89e25de634736df615e7c46aab35cd59ac651cd74
fetched_at: '2026-06-28T22:46:48.339495+00:00'
product: rm
section_id: 1500000861162
source: central-rm
title: 'RH - RM - FOP - Funcionários: Relatório delphi não gera pelo cadastro de funcionários'
type: support-article
updated_at: '2025-03-13T11:27:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024639251-RH-RM-FOP-Funcion%C3%A1rios-Relat%C3%B3rio-delphi-n%C3%A3o-gera-pelo-cadastro-de-funcion%C3%A1rios
---

**Ocorrência**Ao tentar gerar um relatório na visão do funcionário o relatório não sai da tela inicial e fica gerando por tempo indeterminado, conforme imagem abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022904891/mceclip0.png)  
 **Ambiente**RM - Totvs Folha de Pagamento - Todas as versões  
  
**Causa**O erro acontece devido a falta de parametrizações no relatório que está sendo gerado.  
  
**Solução**Para que o relatório Delphi sejam gerados corretamente na MDI a flag **Executa em JobServer** deve sempre estar marcada.  
  
Passos para configurar o relatório:  
  
01. Acesse **Gestão | Gerador de Relatórios | Visão Delphi**;  
02. Selecione o relatório que será gerado e clicar em **Editar;**03. Marcar a flag **Executa em JobServer;**04. Clicar em **Ok** e tentar gerar o relatório novamente pela visão dos funcionários.
