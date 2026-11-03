---
article_id: 16343860895767
category: eSocial - Gerar XML/ Integração Evento
content_hash: 20b51157201458e727ae10e1773a32de4cf7ca086c04f7741b5fb91b72cd6e24
fetched_at: '2026-06-28T22:47:13.153466+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - S-2299 - Como retificar a data de demissão quando
  há um processo judicial retroagindo a data de demissão?
type: support-article
updated_at: '2026-04-17T18:11:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16343860895767-RH-RM-FOP-eSocial-S-2299-Como-retificar-a-data-de-demiss%C3%A3o-quando-h%C3%A1-um-processo-judicial-retroagindo-a-data-de-demiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16343784085655) Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida**  
Como proceder no sistema TOTVS Folha de Pagamento para informar ao eSocial uma alteração retroativa na data de demissão de um evento S-2299 já enviado ao governo, devido a uma decisão judicial que modificou a data de demissão?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - À partir das versões 12.1.2209.243, 12.1.2302.167 e 12.1.2306.111.

**Solução**  
De acordo com as informações presentes no Manual de Orientação do eSocial (MOS), versão S-1.1 do leiaute, deverá utilizar a tag <indRemun> para indicar que o evento S-2299 corresponde a um desligamento reconhecido judicialmente, ocorrido antes das competências em que já foram informadas remunerações no eSocial. Com essa abordagem, torna-se dispensável excluir as remunerações referentes a competências posteriores.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16342756184599)

Para isto, realize os seguintes passos:

1. Acesse a Rescisão do trabalhador e selecione a opção **Indicativo Remuneração Após o Desligamento** e  preencha as informações necessárias.  
1.1. O campo **Data Fim Quarentena** será desabilitado quando o campo **Indicativo Remuneração Após o Desligamento** **estiver preenchido com o valor 2**. Informando o valor 2 o campo **Data Desligamento Judicial** será habilitado.  
1.2. O campo **Data Desligamento Judicial** deve ser preenchido com uma data de desligamento determinada pelo juiz.  
  
2. Após preencher a **Data Desligamento Judicial**, será gerado um gatilho na fila de eventos com o status de **Retificação**.

**Exemplo**  
Funcionário foi desligado em 15/01/2023, recebeu as verbas rescisórias em janeiro/2023 e o juiz determinou que a demissão deveria ter ocorrido em 25/12/2022, o usuário deve preencher o campo Data Desligamento Judicial com a data de 25/12/2022 (determinada pela justiça). Ao preenchê-la, o sistema gerará um gatilho de retificação do evento S-2299, contendo as seguintes informações:

* O campo <dtDeslig> preenchido com a data informada no novo campo Data Desligamento Judicial (25/12/2022).
* O campo <indRemun> preenchido com o indicativo de situação de remuneração após o desligamento igual a 2.
* O campo <dtFimRemun> preenchido com a data informada no campo Data de Desligamento da rescisão (15/01/2023).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16343715290263)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16343695467543)

**Saiba mais**  
Para mais informações sobre as validações, acesse:

* [S-2299 - Como retificar a data de demissão quando há um processo judicial retroagindo a data de demissão?](https://tdn.totvs.com/pages/viewpage.action?pageId=773888128)
