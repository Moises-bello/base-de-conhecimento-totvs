---
article_id: 37067347073559
category: eSocial - Gerar XML/ Integração Evento
content_hash: 4014923cde32cdf7496be7e2db407e1d30a491a46c1e23a5eb2a60bbe79707bd
fetched_at: '2026-06-28T22:47:12.267177+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro código 304: Nao existe um Contrato de Trabalho
  para o CPF: XXXXXXXXXXX ou este encontra-se encerrado na data do evento.. Erro código
  2: O campo nao pode ser preenchido: Indicador de Preenchimento de Cota.'
type: support-article
updated_at: '2026-03-17T22:06:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37067347073559-RH-RM-FOP-eSocial-Erro-c%C3%B3digo-304-Nao-existe-um-Contrato-de-Trabalho-para-o-CPF-XXXXXXXXXXX-ou-este-encontra-se-encerrado-na-data-do-evento-Erro-c%C3%B3digo-2-O-campo-nao-pode-ser-preenchido-Indicador-de-Preenchimento-de-Cota
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37067329032087) Tempo aproximado para leitura:**00:01:30 min**  
  
  
**Ocorrência**  
Ao integrar o evento **S-2205**, é apresentado o **erro código 304**: Não existe um Contrato de Trabalho para o CPF: XXXXXXXXXXX ou este encontra-se encerrado na data do evento.. Erro código 2: O campo não pode ser preenchido: Indicador de Preenchimento de Cota. Localização: /eSocial/evtAltCadastral/alteracao/dadosTrabalhador/infoDeficiencia/infoCota.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**  
Esse incidente ocorre porque o evento **S****-2205** está sendo enviado com o campo **Indicador de Preenchimento de Cota (infoCota)** preenchido, porém **não existe vínculo ativo** para o CPF informado na data do evento. O eSocial valida esse campo apenas quando há **Contrato de Trabalho vigente**, previamente informado por meio dos eventos **S-2200 (Cadastramento Inicial)** ou **S-2300 (Trabalhador Sem Vínculo)**.  
Caso o contrato esteja encerrado ou não exista, o preenchimento do campo **infoCota** não é permitido.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Verifique se o trabalhador possui **Contrato de Trabalho ativo** na data informada no evento, conferindo os eventos **S-2200 ou S-2300** enviados ao eSocial.
2. Caso o contrato esteja **encerrado**, **não será possível** o envio do evento de **Alteração Cadastral (S-2205)** com data **posterior ao desligamento** do trabalhador.
3. Se o contrato deveria estar ativo, valide se os eventos de admissão (**S-2200**) ou vínculo (**S-2300**) foram enviados corretamente e aceitos pelo eSocial.
4. Após os ajustes, gere novamente o evento **S-2205 – Alteração Cadastral** e realize um novo envio ao eSocial.

**Saiba mais**

[RH - RM - FOP - eSocial - Erro 303 na integração com o Governo: Não foi localizado o contrato de trabalho do trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9783033300119-RH-RM-FOP-eSocial-Erro-303-na-integra%C3%A7%C3%A3o-com-o-Governo-N%C3%A3o-foi-localizado-o-contrato-de-trabalho-do-trabalhador)
