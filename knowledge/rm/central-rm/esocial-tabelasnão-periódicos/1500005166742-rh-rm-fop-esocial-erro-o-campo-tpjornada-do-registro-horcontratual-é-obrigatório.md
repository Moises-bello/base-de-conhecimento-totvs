---
article_id: 1500005166742
category: eSocial - Tabelas/Não Periódicos
content_hash: 3cabe9d7564eb6a458d8cb6dc34f7f4da61024b399ce631ef97238ac8123f201
fetched_at: '2026-06-28T22:47:10.450528+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Erro O campo 'tpJornada' do registro 'horContratual'
  é obrigatório e não está preenchido
type: support-article
updated_at: '2025-07-02T17:42:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005166742-RH-RM-FOP-eSocial-Erro-O-campo-tpJornada-do-registro-horContratual-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24454108822295) Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**Ao realizar a geração do XML dos eventos **S-2200**, **S-2206** ou a validação da base de dados do **S-2200**, é apresentada a mensagem de erro **O campo 'tpJornada' do registro 'horContratual' é obrigatório e não está preenchido**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial  - A partir do patch 12.1.29  
  
**Causa**O erro é apresentado quando o campo **Tipo de jornada eSocial** no cadastro do horário vinculado ao funcionário em questão não está preenchido.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse **Folha de Pagamento | Administração de Pessoal | Horários | Histórico de Horários**;  
1.1. Para o evento **S-2200** edite o horário vigente no mês de admissão do funcionário, acesse a aba **eSocial**,preencha o campo de **Tipo de jornada e-Social** e salve o cadastro;  
1.2. Para o evento **S-2206** edite o horário que consta no histórico cujo a vigência for correspondente à data de alteração registrada no evento **S-2206**. Acesse a aba **eSocial**,preencha o campo de **Tipo de jornada e-Social** e salve o cadastro.

![oi.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007073001)

2. Refaça a geração do XML ou a validação da base de dados.
