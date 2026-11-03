---
article_id: 360027728452
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: e7b8c09a70b6af950a30e902b55bdde94efd898a760adc1a341ddefb3ce59580
fetched_at: '2026-06-28T22:42:42.234746+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Empenhando no armazém padrão, mesmo
  configurado para considerar outro armazém
type: support-article
updated_at: '2022-11-28T13:03:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027728452-Manufatura-Linha-Protheus-SIGAPCP-Empenhando-no-armaz%C3%A9m-padr%C3%A3o-mesmo-configurado-para-considerar-outro-armaz%C3%A9m
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:00:50 min**

**Dúvida**Por que está empenhando no armazém padrão, mesmo configurado para considerar outro armazém nos parâmetros do **F12** do **MATA650 - Ordens de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução** Na abertura de uma ordem de produção, se na pergunta **Cons. Só Armazém Padrão?** do **F12** do **MATA650** estiver preenchido com **Sim**, as perguntas **Considera do Armazém?** e **Até o Armazém?** não serão consideradas. Se na pergunta **Cons. Só Armazém Padrão?** estiver como **Não**, as outras perguntas citadas acima refere-se apenas ao cálculo do saldo disponível e não para empenho, que é gerado **sempre** no almoxarifado padrão. Apenas para produtos com **rastro** e/ou **localização**, e pergunta **Sugere** **Lote/Localiz a Empenhar** estiver igual a **Sim**, o Sistema empenha outro armazém que não seja o padrão.
