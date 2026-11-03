---
article_id: 360051662253
category: Gestão de Transportes (TMS)
content_hash: 14d6d752570ac0ce00cf6ca55944abf792c58807de834f6e90f1b4b1c6188667
fetched_at: '2026-06-28T22:45:29.506609+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Percurso de Viagem
type: support-article
updated_at: '2021-12-22T12:42:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051662253-Log%C3%ADstica-Linha-Protheus-TMS-Percurso-de-Viagem
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:30 min****Dúvida**Como funciona o Percurso de Viagem no **SIGATMS** ?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Ao confirmar a viagem o sistema apresentará uma tela de percurso de viagem, esta tela será apresentada em algumas situações:

* Caso o parâmetro **Apres. Percurso Vge. aberta** do **F12** da viagem esteja igual a **1-Sim**;
* Caso os estados do percurso da viagem não respeitem os estados definidos na aba **Percursos** **MDF-e** - **Tabela DIQ**do cadastro de **Rota - OMSA100**;
* Caso ocorram alterações com a viagem em trânsito.

O objetivo desta tela é permitir a visualização e algumas manipulações dos estados de passagem da viagem, para efeito da geração do **MDF-e**, podendo desta forma realizar as seguintes ações na tela:

* Adicionar novos estados de passagem entre os estados já trazidos automaticamente;
* Realizar a reordenação de estados utilizando o campo **Seq. Passagem - DL1\_SEQUEN**, para definir o trajeto que o veículo realmente realizará nesta viagem;
* Realizar a movimentação do documento entre as passagens de mesmo destino. **Este caso deve ser utilizado, caso o veículo passe mais de uma vez dentro do estado e o documento será entregue nas passagens posteriores**.

O carregamento desta tela segue as seguintes regras:

* **Enquanto a viagem esteja em aberto:**
  + O estado de origem usado na definição dos pontos do percurso será selecionado à partir do campo **Cd.Ori. MDF-e** - **DA8\_CDOMDF**, que define a região de origem da viagem no cadastro da rota, caso o mesmo esteja em branco, o sistema utilizará o **Estado de entrega**- **M0\_ESTENT** do cadastro da empresa;
  + Caso a rota selecionada na viagem possua um percurso de **MDF-e** já definido, o sistema usará estes estados como base para geração do percurso. Caso não exista percurso, o sistema usará os estados de destino do documento para geração;
  + Os documentos serão adicionados dentro de cada um dos seus respectivos estados de destino.
* **Caso a viagem esteja em trânsito e seja necessário a inclusão de um documento não previsto:**
  + Os documentos não previstos entrarão sempre em um ponto que possui destino o estado da filial da viagem, mesmo que o destino da entrega seja outro estado, neste caso, quando o documento chegar na filial será gerado um novo **Movimento de viagem - Tabela DUD** para que o mesmo possa concluir seu processo de entrega;
  + O estado de origem do ponto do percurso será referente ao código da região de origem do documento, por isso é importante na digitação da nota selecionar a região de origem como remetente no campo **Selec. Origem** - **DTC\_SELORI** igual a  **2- Cliente Remetente** ou **3- Local Coleta**.

Caso a viagem esteja **em trânsito** e ocorra a inclusão de documentos não previstos, o sistema realizará a inclusão das operações de chegada e saída de cliente, caso as mesmas não existam, logo após a gravação do percurso. Além de gerar as operações, a chegada no cliente será apontada automaticamente. Caso as operações já existam, o sistema não realizará o apontamento de chegada.  
  
**Glossário  
MDF-e -** Manifesto Eletrônico de documentos fiscais **SIGATMS -**Gestão de Transportes
