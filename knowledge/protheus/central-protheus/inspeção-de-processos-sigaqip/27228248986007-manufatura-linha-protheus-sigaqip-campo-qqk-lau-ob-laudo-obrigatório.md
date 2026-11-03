---
article_id: 27228248986007
category: Inspeção de Processos (SIGAQIP)
content_hash: f6b6f9a60722adb421b2aa2b8e4bd487ed8ffeee5b8088cb5c321cc392be69b5
fetched_at: '2026-06-28T22:42:25.711451+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Campo QQK_LAU_OB - Laudo Obrigatório
type: support-article
updated_at: '2024-10-21T19:55:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27228248986007-Manufatura-Linha-Protheus-SIGAQIP-Campo-QQK-LAU-OB-Laudo-Obrigat%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27228248955927) Tempo aproximado para leitura: **00:00:35 min** **Dúvida**Qual a funcionalidade do campo **QQK\_LAU\_OB - Laudo Obrigatório**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Todas as versões  
  
**Solução**O campo **QQK\_LAU\_OB** é exibido na rotina **QIPA010 - Especificação de Produto** e tem a função de habilitar ou não a obrigatoriedade de **Laudo de Laboratório** quando a inspeção é executada na rotina **QIPA215 - Resultados.** Este campo é de uso do módulo **SIGAQIP - Inspeção de Processos** e seu conteúdo é refletido no campo **G2\_LAU\_OBR - Laudo Obrigatório**, entretanto o campo **G2\_LAU\_OBR** não é visível na rotina **PCPA124 - Processo Produtivo** por restrição definida ao nível de fonte.
