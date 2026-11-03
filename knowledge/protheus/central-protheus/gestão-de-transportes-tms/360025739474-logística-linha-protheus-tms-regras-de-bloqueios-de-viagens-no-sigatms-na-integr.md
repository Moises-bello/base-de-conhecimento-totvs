---
article_id: 360025739474
category: Gestão de Transportes (TMS)
content_hash: 5df2fd5d9847d5f442b77206ed6aa457f48c3e20df15c1b5504216eadc2ed48d
fetched_at: '2026-06-28T22:45:32.533165+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Regras de bloqueios de viagens no SIGATMS
  na integração com o SIGAMNT
type: support-article
updated_at: '2024-05-24T19:53:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025739474-Log%C3%ADstica-Linha-Protheus-TMS-Regras-de-bloqueios-de-viagens-no-SIGATMS-na-integra%C3%A7%C3%A3o-com-o-SIGAMNT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23724625911831)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como ocorrem os **bloqueios de viagem** no **SIGATMS - Gestão de Transportes** quando há a integração com o **SIGAMNT - Manutenção de Ativos**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**Quando o **TMS** esta integrado ao **MNT**, os bloqueios de viagens podem ocorrer em dois momentos:

1. Na inclusão do veiculo na tela de Complemento da Viagem, campo **DTR\_CODVEI** - Ao informar o veículo no Complemento da Viagem, se este veiculo estiver vinculado ao módulo **Manutenção de ativos,** campo **DA3\_CODBEM**, se neste momento existir uma **Ordem de Serviço** na tabela **STJ** com campo **TJ\_SITUACA** = 'P' (Pendente) e o campo **TE\_CARACTE** = 'C' (Corretiva), então, o **TMS** bloqueará o uso deste veiculo.  
   Caso deseje adicionar novas validações, temos o ponto de entrada [**TMS240VLD**](https://tdn.totvs.com/pages/releaseview.action?pageId=738233746) que valida campos preenchidos no complemento de viagem.
2. Ao salvar a inclusão da viagem - No momento em que confirmamos a inclusão da viagem, o Sistema verifica a qual **Bem**, tabela **ST9**, os veículos **Cavalos e Reboques** estão relacionados.  
     
   Após isso, é verificado o **Tipo de Acompanhamento**, campo **TF\_TIPACOM**, que o **Bem** está definido no seu cadastro de **Manutenção** - tabela **STF**, onde poderá ser **T - Tempo** ou **C - Contador.**  
   Sendo **T - Tempo**, o Sistema calcula a **Data Real da Próxima Manutenção** e caso esteja dentro da **Data de Inicio Planejamento** - campo**DTR\_DATINI** e **Data de Fim Planejamento**, campo **DTR\_DATFIM,** então, a viagem será bloqueada.  
     
   Sendo **C - Contador**, o Sistema verifica o contador **hodômetro** real do **Bem** pelo campo **TP\_ACUMCON** da tabela **STP**. Neste caso ele utiliza o maior **hodômetro**encontrado. Na sequência é verificado o contador máximo do **hodômetro** permitido somando os campos **Contador Ultima Manuten.**- campo **TF\_CONMANU** com o **Incremento Entre Manut.** - campo **TF\_INENMAN** do **Cadastro da Manutenção.**Caso o **hodômetro** real do Bem seja maior ou igual ao **hodômetro** máximo permitido, então, a **Viagem** será bloqueada.  
     
   Para que essas validações ocorram, o **TMS** deve estar configurado com os cadastros de distâncias, **[TMSA711](https://tdn.totvs.com/pages/releaseview.action?pageId=485434153)** ou [**TMSA710**](https://tdn.totvs.com/pages/releaseview.action?pageId=464949425) para obtenção do KM conforme a rota informada na viagem. De acordo com este KM, o **TMS** poderá realizar o bloqueio de viagem citado neste item 2.

Temos apenas estas duas formas de bloqueios de viagens, caso o usuário deseje efetuar bloqueio no fechamento da viagem, temos o ponto de entrada [**TM310TOK**](https://tdn.totvs.com/pages/releaseview.action?pageId=834246087).  
  
Tabelas envolvidas no processo:  
  
**DTR** - Veículos da Viagem  
**DA3** - Veículos  
**ST9** - Bem  
**STC** - Estrutura  
**STF** - Manutenção  
**STP** - Ordens Serviço Acompanhamento  
  
**Importante**  
As tabelas **ST9**, **STC**, **STF** e **STP** pertencem ao módulo **Manutenção de Ativos** e caso tenham alguma dúvida quanto às mesmas orientamos abertura de **ticket** diretamente para esta equipe.
