---
article_id: 4408762432919
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: f25f093a344e5d7d9b3a33c391fcba1c7dec6db7e5f014bb06d5b65121228dc3
fetched_at: '2026-06-28T22:42:45.729856+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Preenchimento do campo Parc/Total no
  apontamento de produção
type: support-article
updated_at: '2022-12-15T11:31:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408762432919-Manufatura-Linha-Protheus-SIGAPCP-Preenchimento-do-campo-Parc-Total-no-apontamento-de-produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:20 min** **Dúvida**Quando o Sistema sugere o conteúdo do campo **Parc/Total** no apontamento de produção?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Ao realizar um apontamento de produção o campo **Parc/Total** é preenchido automaticamente conforme o saldo da **OP - Ordem de Produção** e a quantidade apontada, ao sair dos campos **Ordem de Produção**, **Quantidade Produzida** ou **Quantidade Perda** e o cursor der entrada em outro campo qualquer em tela.  
Para isso será necessário também que seja preenchido o valor desses campos, ou se já tiverem valor, que este valor seja apagado e preenchido novamente.  
O campo **Parc/Total** não tem seu conteúdo atualizado se o usuário preencher o campo **Ordem de Produção**, **Quantidade Produzida** ou **Quantidade Perda** e clicar diretamente em confirmar, sem que o cursor esteja em outro campo, ou se o usuário entrar e sair de um desses campos sem alterar o seu valor. Além disso, ele não não tem seu valor alterado ao clicar em confirmar, sendo gravado o valor que está em tela.  
  
**Saiba mais**  
Para preencher novamente **Parc/Total** ao clicar em **Confirmar**, pode-se implementar o código para o preenchimento do campo através do ponto de entrada: [MT680VAL - Inclusão das Produções](https://tdn.totvs.com/pages/releaseview.action?pageId=6089410)
