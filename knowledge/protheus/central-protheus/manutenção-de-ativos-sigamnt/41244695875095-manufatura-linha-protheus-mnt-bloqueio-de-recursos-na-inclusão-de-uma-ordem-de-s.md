---
article_id: 41244695875095
category: Manutenção de Ativos (SIGAMNT)
content_hash: 889211a86caa45f7e59625b69e58b86b6cd079091d988a7646991b2fa93d6e11
fetched_at: '2026-06-28T22:42:32.815093+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Bloqueio de recursos na inclusão de uma
  Ordem de serviço de manutenção
type: support-article
updated_at: '2026-06-17T11:56:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41244695875095-Manufatura-Linha-Protheus-MNT-Bloqueio-de-recursos-na-inclus%C3%A3o-de-uma-Ordem-de-servi%C3%A7o-de-manuten%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41244702222743) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como funciona o bloqueio de recursos na inclusão de uma **Ordem de Serviço de Manutenção**?   
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**  
Na inclusão de uma **O.S. - Ordem de serviço** preventiva quando o campo **Parada Bem - TF\_PARADA** da **Manutenção - MNTA120** está igual a **S - Sim**:

1. Quando o bem não tem relacionamento com recurso do **SIGAPCP - Planejamento e controle da produção**, ou seja, o campo **Recur/Ferram - T9\_RECFERR** do **Cadastro de bem - MNTA080** está vazio, o bloqueio ocorre na rotina **Bloqueio Bem - MNTA150**, na tabela **ST3**. Esse bloqueio é apenas informativo.
2. Quando o bem tem relacionamento com recurso do **SIGAPCP**, ou seja, campo T9\_RECFERR está preenchido, o bloqueio ocorre na rotina **Bloqueio de recursos - MATA660**, na tabela **SH9**. Esse bloqueio serve para a rotina do **Carga Máquina**, conforme descrito no artigo do *link* [Manufatura - Linha Protheus - SIGAPCP - Apontamento com o recurso bloqueado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9531347527831-Manufatura-Linha-Protheus-SIGAPCP-Apontamento-com-o-recurso-bloqueado)
