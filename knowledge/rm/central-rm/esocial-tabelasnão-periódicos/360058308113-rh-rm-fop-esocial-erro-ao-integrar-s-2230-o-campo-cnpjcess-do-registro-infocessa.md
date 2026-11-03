---
article_id: 360058308113
category: eSocial - Tabelas/Não Periódicos
content_hash: 44a8acf69bc2df752cd204d67224671277c255e0359c824cc2a2cbbb3a757541
fetched_at: '2026-06-28T22:47:10.576516+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP- eSocial- Erro ao integrar S-2230: O campo ''cnpjCess'' do registro
  ''infoCessao'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2025-07-02T20:53:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058308113-RH-RM-FOP-eSocial-Erro-ao-integrar-S-2230-O-campo-cnpjCess-do-registro-infoCessao-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**Ao gerar evento S-2230 é apresentada seguinte mensagem de erro: **O campo 'cnpjCess' do registro 'infoCessao' é obrigatório e não está preenchido**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Essa mensagem de erro é apresentado no caso de afastamento por cessão ou requisição do trabalhador, não tendo cadastrado com o CNPJ do órgão/entidade no campo do eSocial.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** Acesse o cadastro do funcionário, na aba **Históricos | Histórico de Afastamento | eSocial** e preencha os campos **Ônus da Cessão** e **CNPJ do órgão para onde o trabalhador foi cedido;**

![](https://tdn.totvs.com/download/attachments/351019497/image2018-4-3_10-37-21.png?version=1&modificationDate=1522764137000&api=v2)

**2.** Ao gerar o XML na fila de eventos, o sistema irá gerar o grupo **infoCessao** no evento S-2230.

![](https://tdn.totvs.com/download/attachments/351019497/image2018-4-3_10-39-41.png?version=1&modificationDate=1522764137000&api=v2)

**Saiba mais**  
Para mais informações acesse:   
      • [Mapeamento S-2230](https://tdn.totvs.com/display/public/LRM/Evento+S-2230)
