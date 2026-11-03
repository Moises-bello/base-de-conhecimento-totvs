---
article_id: 360058957914
category: RH - Rescisão
content_hash: 68f7f26f2496e4945f645c80ee56ae9447b98a6efee92fd7ba053c20edd3cfb7
fetched_at: '2026-06-28T22:43:49.806851+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - O que deve ser feito quando o aviso prévio é interrompido
  por motivo de novo emprego do funcionário
type: support-article
updated_at: '2025-07-28T19:21:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058957914-RH-Linha-Protheus-GPE-O-que-deve-ser-feito-quando-o-aviso-pr%C3%A9vio-%C3%A9-interrompido-por-motivo-de-novo-emprego-do-funcion%C3%A1rio
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33774467878679)***Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**O que deve ser feito quando o aviso prévio é interrompido por motivo de novo emprego do funcionário?**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**No cálculo da rescisão de contrato deve ser realizada as seguintes configurações:  
  
**1.** Selecione um tipo de rescisão onde o aviso seja trabalhado, visto que o empregado trabalhou parte dos dias. Para isso, na **Tabela S043** da rotina **Manutenção de Tabelas**, pelo caminho >**Atualizações** >**Definições de Cálculo** >**Manutenção Tabelas** a coluna **Aviso Prévio** deve estar com **T**:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012470882)  
  
**2.** Preencha o campo **Data Aviso**, o Sistema incluirá de forma automática 30 dias no campo de **Aviso Prévio**. Após esse preenchimento automático, **altere** a quantidade de dias do **campo Aviso Prévio** de acordo com os dias que o funcionário já trabalhou:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012819941)  
  
**3.** Com o campo **Aviso Prévio** alterado, o Sistema preenche o campo **Aviso Cump.** com a mesma quantidade do campo Aviso Prévio, o Sistema vai calcular na rescisão somente os dias de aviso que foram cumpridos e caso tenha dias de saldo de salário, também:  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012820041)  
  
**IMPORTANTE**: Ressaltamos que essa alteração nos dias de aviso prévio é sugerida pelo suporte apenas quando o aviso é interrompido por um motivo legal - funcionário que começou um novo emprego. Essa alteração também se faz necessária para que o sistema não utilize o restante do aviso prévio ou projete a data de demissão, gerando férias e 13º sobre aviso incorretamente.   
  
**Embasamento**:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=362467660>  
<https://tdn.totvs.com/pages/releaseview.action?pageId=351031543>

**Saiba mais**Para adquirir mais conhecimento acesse o(s) *link*(s) abaixo:  
[RH - Linha Protheus - GPE - Como calcular verba de Aviso Trabalhado na Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019724912-MP-GPE-Como-calcular-verba-de-Aviso-Trabalhado-na-Rescis%C3%A3o)  
[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
