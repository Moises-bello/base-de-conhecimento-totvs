---
article_id: 4410252227735
category: Metrologia (SIGAQMT)
content_hash: 1fdfcf814d5612b576ea6ae8763096f4671fcb92199f6e51d53108fe9b27da13
fetched_at: '2026-06-28T22:42:24.761119+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - Alterar responsável no cadastro do
  instrumento
type: support-article
updated_at: '2021-10-07T16:40:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410252227735-Manufatura-Linha-Protheus-SIGAQMT-Alterar-respons%C3%A1vel-no-cadastro-do-instrumento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura**: 00:00:50 min****Dúvida**Na rotina de **Cadastro de Instrumentos - QMTA010**, ao realizar a alteração de um cadastro, o campo **Responsável -****QM2\_RESP** não permiti edição. Como alterar o **responsável**?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Solução**O **Sistema** valida se a **Família de Instrumento** cadastrada na rotina **QMTA030 - Cadastro de Famílias de Instrumentos** possui controle de movimentação pela rotina **QMTA010 - Cadastro de Instrumentos**. Esse controle é definido através do campo **Cont. Movim. - QM1\_LOCAL** e se possuir o conteúdo igual a **S - Sim**, a edição do responsável não é permitida, caso o conteúdo esteja igual a **N-Não** a alteração do campo **Responsável - QM2\_RESP** será permitida no cadastro do instrumento.
