---
article_id: 22193004178199
category: Inspeção de Processos (SIGAQIP)
content_hash: 41a6f5c063435dd99d791bc89748720ad6b98567b7b99bb2542718b15f02d0e9
fetched_at: '2026-06-28T22:42:25.751465+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Habilitar evento de notificação de
  controle de qualidade aguardando tratamento
type: support-article
updated_at: '2024-03-20T12:28:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22193004178199-Manufatura-Linha-Protheus-SIGAQIP-Habilitar-evento-de-notifica%C3%A7%C3%A3o-de-controle-de-qualidade-aguardando-tratamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22192959708567) Tempo aproximado para leitura: **00:00:50 min****Dúvida**No módulo **SIGAQIP - Inspeção de Processos** como habilitar evento de **notificação de controle de qualidade aguardando tratamento**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIP) - Versão 12  
  
**Solução**Para habilitar a notificação de controle de qualidade aguardando tratamento no módulo **SIGAQIP**, realize os seguintes passos:  
1. Habilitar integração com **SIGAEST - Estoque:** [Manufatura - Linha Protheus - SIGAQIP - Habilitar integração com SIGAEST](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15791811821591-Manufatura-Linha-Protheus-SIGAQIP-Habilitar-integra%C3%A7%C3%A3o-com-SIGAEST);  
2. No **SIGACFG - Configurador** em **Usuário > Senhas > Usuários**, o campo de **E-mail - USR\_EMAIL** necessita estar preenchido com *e-mail* válido;  
3. Acesse **Smartclient** e a rotina **CFG040 - Inscrição de Leitura Event Viewer** em **Miscelânea;**4. Nesta rotina preencha o campo **Canal** com a informação **002 - Ambientes**, o campo **Categoria** com **001 - Módulos**, o campo **ID do Evento** com evento **006 - Controle de Qualidade aguardando tratamento** e o campo **E-mail** com **S - Sim;**5. Ao confirmar o apontamento na rotina **MATA250- Produção Simples**, **MATA680 - Produção PCP MOD1** e/ou **MATA681 - Produção PCP MOD 2**, será disparada a notificação para o e-mail cadastrado.
