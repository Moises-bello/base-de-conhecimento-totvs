---
article_id: 21191189147159
category: Inspeção de Entradas (SIGAQIE)
content_hash: c4df991b2e85eff8d2695fc69a4757d7fa8629d15126c679a544194d23686171
fetched_at: '2026-06-28T22:42:26.990311+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Habilitar evento de notificação de
  entrada aguardando tratamento
type: support-article
updated_at: '2024-02-07T20:53:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21191189147159-Manufatura-Linha-Protheus-SIGAQIE-Habilitar-evento-de-notifica%C3%A7%C3%A3o-de-entrada-aguardando-tratamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21191251364759) Tempo aproximado para leitura: **00:00:50 min****Dúvida**No módulo **SIGAQIE - Inspeção de Entradas** como habilitar evento de **notificação de entrada aguardando tratamento**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**Para habilitar a notificação de entrada de qualidade aguardando tratamento no módulo **SIGAQIE - Inspeção de Entradas**, realize os seguintes passos:  
1. No **SIGACFG - Configurador** em **Usuário > Senhas > Usuários**, o campo de **E-mail - USR\_EMAIL** necessita estar preenchido com *e-mail* válido;  
2. Acesse **Smartclient** e a rotina **CFG040 - Inscrição de Leitura Event Viewer** em **Miscelânea;**3. Nesta rotina preencha o campo **Canal** com a informação **002 - Ambientes**, o campo **Categoria** com **001 - Módulos**, o campo **ID do Evento** com evento **006 - Controle de Qualidade aguardando tratamento** e o campo **E-mail** com **S - Sim;**  
4. Ao confirmar a entrada da nota na rotina **MATA103 - Documento de Entrada**, havendo integração com o **SIGAQIE**, será disparada a notificação para o e-mail cadastrado.
