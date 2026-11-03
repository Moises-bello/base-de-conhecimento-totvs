---
article_id: 360058224233
category: eSocial - Tabelas/Não Periódicos
content_hash: b047be2279bc1e5771b7d0951dd9308c753b92a3c086f021375b2dde631ea64f
fetched_at: '2026-06-28T22:47:10.178242+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial  -  Erro ao gerar S-2200/S-2300: Validação do campo
  ''dtAdm'': Se {cadIni} = [S], deve ser anterior à data de início da obrigatoriedade'
type: support-article
updated_at: '2024-12-30T15:28:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058224233-RH-RM-FOP-eSocial-Erro-ao-gerar-S-2200-S-2300-Valida%C3%A7%C3%A3o-do-campo-dtAdm-Se-cadIni-S-deve-ser-anterior-%C3%A0-data-de-in%C3%ADcio-da-obrigatoriedade
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24456595384855) Tempo aproximado para leitura: 00:02:10 min  
  
Ocorrência**Ao gerar o evento **S-2200/S-2300** ocorre a mensagem **Erro na Validação do campo 'dtAdm': Se {cadIni} = [S], deve ser anterior à data de início da obrigatoriedade do empregador no eSocial**.

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Para solucionar o incidente realize os passos abaixo:  
**1**. Acesse **Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais 1/6** e verifique a data de obrigatoriedade para os eventos não periódicos;  
**2**. Acesse **Folha de Pagamento | eSocial | Fila de Eventos** localize o evento com erro e identifique o tipo de operação e a data de admissão gerada na tag **dtAdm** conforme exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097957233)

**2.1.** Caso a data de admissão seja anterior à data de obrigatoriedade identificada no passo 1 o correto será enviar um evento com o tipo de operação sendo **Carga Inicial**;  
**2.2.** Caso a data de admissão seja posterior à data de obrigatoriedade identificada no passo 1 o correto será enviar um evento com o tipo de operação sendo **Inclusão**.  
  
**Saiba mais**Para mais informações acesse:  
      • [S-2200 – Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=452719244)
