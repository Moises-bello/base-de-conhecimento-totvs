---
article_id: 360025949692
category: Inspeção de Processos (SIGAQIP)
content_hash: d9ddebd1b16f0c2a9acfef05bd8666bdcc3b4bd1493caa8c47f7f9cee761f4aa
fetched_at: '2026-06-28T22:42:25.932603+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Regras de compartilhamento de tabelas
type: support-article
updated_at: '2025-06-06T19:00:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025949692-Manufatura-Linha-Protheus-SIGAQIP-Regras-de-compartilhamento-de-tabelas
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32644699511063)***Tempo aproximado para leitura: **00:00:40 min****Dúvida**Quais são as regras de compartilhamento de tabelas no módulo **SIGAQIP - Inspeção de Processos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Solução**As tabelas abaixo devem seguir o mesmo compartilhamento da tabela **SG2 - Operações**.   
Por exemplo: Quando a tabela **SG2** está em modo **compartilhado**, todas as tabelas devem também estar em modo **compartilhado**:

|  |  |
| --- | --- |
| Tabela | Descrição |
| QP6 | Histórico de Produtos |
| QP7 | Ensaios Mensuráveis dos Produtos |
| QP8 | Ensaios Textos dos Produtos |
| QP9 | Não-Conformidades dos Produtos |
| QQK | Especificações das Operações |
| SG2 | Operações – módulos de Materiais |
