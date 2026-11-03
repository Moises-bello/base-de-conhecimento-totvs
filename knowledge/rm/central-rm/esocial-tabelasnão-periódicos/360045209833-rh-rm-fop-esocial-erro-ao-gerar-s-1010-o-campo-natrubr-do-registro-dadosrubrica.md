---
article_id: 360045209833
category: eSocial - Tabelas/Não Periódicos
content_hash: 994d2c719c5964a19fa037c773e9743800a4693a93bdb63665629d51c753d0cd
fetched_at: '2026-06-28T22:47:10.559039+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP- eSocial - Erro ao gerar S-1010: O campo ''natRubr'' do registro
  ''dadosRubrica'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2024-06-21T13:44:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045209833-RH-RM-FOP-eSocial-Erro-ao-gerar-S-1010-O-campo-natRubr-do-registro-dadosRubrica-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24226801185431)** Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Ao realizar a geração do XML do evento **S-1010** é apresentada a mensagem de erro: **O campo 'natRubr' do registro 'dadosRubrica' é obrigatório e não está preenchido.****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro é apresentado quando o campo **Natureza da rubrica eSocial** no cadastro do evento da folha de pagamento não está preenchido.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse **Folha de Pagamento | Administração de Pessoal | Eventos** e localize o evento correspondente;  
2. Edite o evento e preencha o campo **Natureza da Rubrica (e-Social)**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061283654)

3. Realize a geração do XML novamente.  
  
**Importante**  
Para preenchimento da natureza da rubrica eSocial consulte a **Tabela 03** do Layout do eSocial.
