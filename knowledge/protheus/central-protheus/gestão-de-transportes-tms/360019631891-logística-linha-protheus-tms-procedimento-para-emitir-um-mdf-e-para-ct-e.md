---
article_id: 360019631891
category: Gestão de Transportes (TMS)
content_hash: 276ace85062cf328cf30d0abe412170fde2877760563b9da2def7948028716fb
fetched_at: '2026-06-28T22:45:32.482584+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Procedimento para emitir um MDF-e para CT-e
type: support-article
updated_at: '2022-11-17T18:49:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019631891-Log%C3%ADstica-Linha-Protheus-TMS-Procedimento-para-emitir-um-MDF-e-para-CT-e
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:05:48 min  
  
Dúvida**Como gerar um **MDF-e - Manifesto Eletrônico de Documentos Fiscais** para **CT-e - Conhecimento de Transporte Eletrônico**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O **Projeto MDF-e** tem como objetivo a implantação de um modelo nacional de documento fiscal eletrônico que venha substituir a sistemática atual de emissão do documento em papel, com validade jurídica garantida pela assinatura digital do emitente, simplificar as obrigações acessórias dos contribuintes e permitir, ao mesmo tempo, o acompanhamento em tempo real das operações comerciais pelo **Fisco**.  
  
O **MDF-e** deve ser emitido a partir de viagens do tipo **Entrega** e **Transporte**, não é possível em viagem do tipo **Coleta**.  
  
Ao enviar um **MDF-e** para a **SEFAZ - Secretaria de Estado da Fazenda** e esse for autorizado, deve-se concluir seu processo, efetuando o encerramento ou cancelamento, pois a **SEFAZ** pode rejeitar os próximos envios.  
  
**Para gerar o MDF-e:**

* Gerar os **CT-es**;
* Carregá-los na viagem - **Entrega/Transporte**;
* Nas rotinas **TMSA144B - Viagem Mod. 2 - Transporte Rodoviário**, ou, **TMSA144D** - **Manifestação de Viagem Modelo 2**, posicione na viagem - **Necessário estar com o *status* em aberto ou fechada,** que consta os documentos carregados e selecione a opção **Outras ações / Manutenção / Manifesto / Manifestar**;
* Tipo de manifesto **Eletrônico**;
* Após realizar esse processo, irá apresentar uma tela contendo algumas informações apenas para confirmação;
* Em **Outras ações / Manutenção / Manifesto / MDF-e**;
* Ao apresentar os perguntes, preencha-os de acordo com os dados da viagem que deseja enviar o **MDF-e**, e no pergunte **Transmissão** = **Envio MDF-e** e transmita-o para a **SEFAZ**.
* Neste processo são enviados os dados por meio do **XML - *Extensible Markup Language***:
  + **Transportadora**;
  + **Veículo**;
  + **Motorista**;
  + **Proprietário do veículo**;
  + **NF-e - Nota fiscal eletrônica**, que estão sendo transportadas;

**CT-e**.

**Para visualizar o MDF-e**

* Posicione na **viagem** que consta os documentos carregados e selecione a opção **Outras ações / Manutenção / Manifesto / Visualizar/Excluir.**

**Cancelamento do MDF-e**

* O cancelamento só pode ser realizado dentro do prazo de 24 horas após a aprovação do **MDF-e**. Caso tenha passado o prazo para o cancelamento o **MDF-e** deve ser encerrado. Para efetuar o cancelamento do **MDF-e**, realize o seguinte processo:
  + Posicione na **viagem** que consta os documentos carregados e selecione a opção **Outras ações / Manutenção / Manifesto / Visualizar/Excluir**;
  + Após a exclusão selecione a opção **Outras ações / Manutenção / Manifesto / MDF-e**;
  + Ao apresentar os perguntes, preencha-os de acordo com os dados da viagem que deseja cancelar o **MDF-e** e no pergunte **Transmissão** = **Cancelamento** e transmita-o para a **SEFAZ**.

Para exclusão do **MDF-e** é importante se atentar, pois **a SEFAZ permite a exclusão em até 24 horas após a autorização do envio do MDF-e**, após isso, não autorizará o cancelamento.  
  
**Encerramento do MDF-e**

* O encerramento deve ser realizado pela filial que iniciou a operação após a conclusão do processo físico. Para efetuar o encerramento do **MDF-e**, efetue o seguinte processo:
  + Posicionando na **viagem** com os devidos apontamentos, ocorrências e com o *status* de **Encerrada,**selecione a opção **Outras ações / Manutenção / Manifesto / MDF-e**;
  + Ao apresentar os perguntes, preencha-os de acordo com os dados da viagem que deseja encerrar o **MDF-e** e no pergunte **Transmissão** = **Encerramento** e transmita-o para a **SEFAZ**.

**Transferência entre filiais**  
Exemplificando a geração do **MDF-e** em um processo de **Transferência entre Filiais** utilizando-se do modal **Rodoviário: Filial A > Filial B > Filial C > Filial D.**

* Sendo todas as **Filiais** dentro da mesma **UF - Unidade da Federação**, será gerado um único **MDF-e** e seu encerramento ocorrerá na última filial, **Filial D**, desde que nesse processo ocorra apenas descarregamento de carga nas filiais de trânsito;
* Sendo todas as **Filiais** dentro de uma mesma **UF,** porém, se houver o carregamento de carga em alguma das filiais, o **MDF-e** deverá ser encerrado na filial em questão e gerado um novo **MDF-e** para a carga total que seguirá adiante;
* Em um processo de **Transferência entre Filiais** o **MDF-e** é gerado por **UF** de **destino da carga** e não por **UF** de **descarga**.

**Rejeições**As rejeições mais comuns são causadas por falhas de cadastros, por exemplo:

* Falta de **RNTRC - Registro Nacional de Transportadores Rodoviários de Cargas**no cadastro do **Proprietário do Veículo**;
* Falta de **CPF - Cadastro de Pessoa Física** no cadastro de **Motorista**;
* Falta de **Informação** no cadastro do **Veículo**;
* Veículo sendo utilizado em um **MDF-e** com o mesmo trajeto;
* **MDF-e** em aberto a mais de um mês;
* Erro no roteiro enviado pelo cadastro de rota.

**Viagem**Veja onde se encaixam os processos descritos acima em uma viagem:

* Incluir uma **viagem**;
* **Gerar manifesto do tipo eletrônico;**
* **Transmitir MDF-e;**
* Fechar **viagem**;
* Apontar **operações**;
* Apontar **ocorrência**;
* Encerrar **viagem**;
* **Transmitir encerramento do MDF-e**

**Saiba mais**No artigo abaixo, foram disponibilizadas informações importantes sobre **MDF-e:**[Logística - Linha Protheus - TMS - Informações e parametrizações sobre MDF-e](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025373131)  
O **MDF-e** recebeu melhorias na **versão 12.1.23 do Protheus**, como a **Automação do MDF-e.** Leia a documentação a seguir para saber mais:  
[DT Automação do Manifesto - MDF-e Automático](http://tdn.totvs.com/pages/releaseview.action?pageId=460685349)  
[DT Automação do Manifesto - Cenários MDF-e Automático](http://tdn.totvs.com/pages/releaseview.action?pageId=461918037)
