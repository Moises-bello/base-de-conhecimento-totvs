---
article_id: 360025514652
category: Gestão de Transportes (TMS)
content_hash: 3c33991a98713c6c1d2a0d498ea797e196607a67a793703577c4e4a814ff0871
fetched_at: '2026-06-28T22:45:29.325590+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Inclusão do Condutor no MDF-e
type: support-article
updated_at: '2023-08-28T11:43:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025514652-Log%C3%ADstica-Linha-Protheus-TMS-Inclus%C3%A3o-do-Condutor-no-MDF-e
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17081275779351)***Tempo aproximado para leitura: **00:02:18 min****Dúvida**Como incluir um segundo condutor no **MDF-e - Manifesto de Carga eletrônica**, já autorizado pela **SEFAZ - Secretaria de Estado da Fazenda**?  
  
**Ambiente**

TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**Por meio desta implementação é possível efetuar a **Inclusão de Condutor em uma Viagem de Entrega ou Transporte**, com *status* **Em Trânsito** e transmiti-la a **SEFAZ**.  
  
Esta melhoria foi desenvolvida para atender o **Ajuste Sinief - Sistema Nacional de Informações Econômicas e Fiscais 20/2014** cláusula 14, que trata da **inclusão de condutor em um MDF-e com *status* Não Encerrado.**O envio do **MDF-e** deve obrigatoriamente, estar com *status* **Autorizado o uso do MDF-e**na **SEFAZ**, e seu encerramento ainda não transmitido com *status* **Em Aberto**.  
  
Somente será permitida a Inclusão de um novo condutor, quando a viagem estiver com *status* **Em Trânsito**.  
  
**Procedimento para Utilização:**

* Em **SIGATMS - Gestão de Transportes**, acesse **Atualizações/Viagens.** Opte pela opção **Rodoviário Entrega** ou**Rodoviário Transporte** e em seguida**Viagem mod.2 - TMSA144;**
* Selecione uma viagem com *status* **Em trânsito;**
* Em **Ações Relacionadas**, selecione as opções **Manutenção/ Inclusão Condutor**. A tela com os veículos na viagem é apresentada;
* Em **Complemento de Viagem - TMSA240**, selecione um veículo;
* Clique em **Ações Relacionadas/Mot. Viag** e inclua um motorista;
* Salve as alterações em **Confirmar**. Somente é permitida a inclusão de 1 único condutor por veículo. Alterações não são permitidas;
* Selecione uma viagem;
* Para realizar a transmissão, clique em **Ações Relacionadas/Manutenção Manifesto/MDF-e - TMSAE73**;
* Na tela de **Parâmetros**, preencha os parâmetros para o filtro;
* No campo **Transmissão**, selecione a opção **Inclusão** **de** **Cond**.;  
  Selecione o manifesto à ser transmitido e clique em **Transmitir**;  
  Aguarde o retorno da **SEFAZ**. Caso a transmissão e autorização ocorram de forma correta, o retorno do evento deve ser: **135 – Evento Registrado e Vinculado ao MDF-e**.

**Importante**Por meio da rotina **TMSA240**, em **Ações Relacionadas/ Mot. Viag,** também é possível consultar o *status* da transmissão, no campo **Status da MDF-e,**onde consta a informação como **Transmitido** ou **Em Aberto**.
