---
article_id: 360020707251
category: RH - Desoneração
content_hash: 99de1ecbee4ba7b1e6db91611527be2d4cca1f762311804b5f7346372d4ba820
fetched_at: '2026-06-28T22:43:42.237870+00:00'
product: protheus
section_id: 360003109152
source: central-protheus
title: RH - Linha Protheus - GPE - Quais as formas de configurar a alíquota na Tabela
  S033
type: support-article
updated_at: '2025-08-06T20:21:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020707251-RH-Linha-Protheus-GPE-Quais-as-formas-de-configurar-a-al%C3%ADquota-na-Tabela-S033
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33987116598167) Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**Quais as formas de configurar a alíquota na Tabela S033?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão Pessoal - A partir da versão 12.  
  
**Solução**A alíquota da Tabela S033 pode ser informada de duas formas:   
- **Manualmente**, pela rotina **Manutenção Tabelas**, pelo caminho >**Atualizações** >**Definições de Cálculo** >**Manutenção Tabelas**, na **coluna Alíquota**, essa parametrização deve ser realizada **antes** da execução da rotina de **Desoneração da Folha**:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013959841)

- **Automaticamente** na geração da rotina Desoneração folha, onde ao executar a rotina de Desoneração, a pergunta **Verificar Integração**? deve ficar com **2-Faturamento**, **3-Financeiro** ou **4-Ambos**. Dessa forma, o Sistema buscará a informação na tabela **CG1** do módulo **SIGAFIS**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013682902)

**OBSERVAÇÃO:** Caso tenha dúvida no procedimento de atualização da Tabela CG1, favor entrar em contato com o suporte **SIGAFIS**.

**Saiba mais:**  
[RH - Linha Protheus - GPE - Como preencher cada campo da Tabela S033](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052976634)

[RH - Desoneração](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109152-RH-Desonera%C3%A7%C3%A3o)
