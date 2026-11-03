---
article_id: 360024939633
category: Inspeção de Processos (SIGAQIP)
content_hash: e64a22e39a7484b8b6ed418c1404e430463a6f343eb37352f699d13027d99faf
fetched_at: '2026-06-28T22:42:25.870008+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAQIP - Número de unidades Não Conformes excede
  o Número de Unidades Amostrais definidos na especificação do Ensaio:  xx'
type: support-article
updated_at: '2021-10-01T13:11:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024939633-Manufatura-Linha-Protheus-SIGAQIP-N%C3%BAmero-de-unidades-N%C3%A3o-Conformes-excede-o-N%C3%BAmero-de-Unidades-Amostrais-definidos-na-especifica%C3%A7%C3%A3o-do-Ensaio-xx
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:50 min**  
**Ocorrência**No módulo **SIGAQIP - Inspeção de Processos**, ao realizar a inspeção na rotina **QIPA215 - Resultados** ocorre a mensagem **Número de unidades Não Conformes excede o Número de Unidades Amostrais definidos na especificação do Ensaio:  xx**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**A mensagem **Número de unidades Não Conformes excede o Número de Unidades Amostrais definidos na especificação do Ensaio:  xx** indica que o número de unidades **não conformes**, não pode ser maior que o número de **amostras**. O número de amostras é definido na rotina **QIPA020 - Cadastro de Ensaios**.  
  
**Solução**Consulte o ensaio informado na mensagem na rotina **QIPA020** e verifique a quantidade informada no campo **Tam. Amostra**.
