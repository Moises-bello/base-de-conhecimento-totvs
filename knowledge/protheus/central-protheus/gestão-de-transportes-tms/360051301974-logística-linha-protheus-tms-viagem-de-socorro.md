---
article_id: 360051301974
category: Gestão de Transportes (TMS)
content_hash: b366bd3c1c27faf82eb249fe97e6c5fa892f6b38dadf2ab283406ddb85f88708
fetched_at: '2026-06-28T22:45:33.487580+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Viagem de Socorro
type: support-article
updated_at: '2025-05-28T11:06:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051301974-Log%C3%ADstica-Linha-Protheus-TMS-Viagem-de-Socorro
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29388498892055)***Tempo aproximado para leitura: **00:03:00 min**  
**Dúvida**Como funciona a **Viagem de Socorro** no **TOTVS Logística TMS**?  
  
**Ambiente**

TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões **Solução**A **Viagem de Socorro**é utilizada para registrar o **trânsito de veículos sem carga**, para situações imprevistas, veículos quebrados ou para efetuar o transbordo de carga em ocasiões esporádicas.  
  
Por isso, o Sistema permite que a viagem seja gerada sem relacionar documentos, assim como a **Viagem Vazia.** Além disso, o Sistema também permite que a viagem possua um veículo da **Categoria - DUT\_CATVEI** igual à **2 - Cavalo**, sem exigir um veículo da **Categoria - DUT\_CATVEI** igual à**3** **- Carreta**, considerando que este veículo irá assumir a carga da viagem a ser socorrida.  
  
Viagens que pode utilizar esse processo:

* **Viagem de Coleta:** É um serviço regular de transporte entre um terminal de frete e as instalações do consignatário, ou seja, é o processo para efetuar a retirada das mercadorias no endereço determinado pelo cliente solicitante.
* **Viagem de Transporte:** É utilizada para efetuar a transferência de cargas entre as transportadoras que possuem filiais.
* **Viagem de Entrega:** É o processo utilizado para efetuar a distribuição das mercadorias na região destino.

Para utilizar a **Viagem de Socorro**, é necessário que:

* Acesse a rotina no menu **Atualizações/Viagens/Rodoviário Entrega/Viagens (modelo 2) - TMSA144** e inclua uma viagem selecionando o tipo da viagem como **Socorro.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081623693)**

* Informe a rota a ser utilizada e acesse a opção **Outras Ações/Comp. Via.** para informar o veículo, podendo informar um veículo, podendo ser da **categoria Cavalo**, sem a obrigatoriedade de informar um veículo da **categoria Carreta,** que irá efetuar o socorro e o motorista e salve a viagem.
* Na viagem normal que necessita do socorro, é necessário que ela esteja com a operação de **Saída de Viagem** apontada, com *status* **Em Trânsito,** e, na **Viagem de Socorro**, ela deve permanecer com seu *status* **Em Aberto**.
* Aponte um **Registro de Ocorrência** para a viagem a ser socorrida do tipo **08 - Transferência de Viagem - DT2\_TIPOCO**. Caso não possua uma ocorrência desse tipo, pode cadastrá-la na rotina no menu **Atualizações/ocorrências/Tabela de Ocorrências - TMSA020.** Segue exemplo do cadastro dessa ocorrência.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080568294)

* Ao apontar o **Registro de Ocorrência**, é necessário informar cada documento a ser transferido de viagem e informar a **Viagem de Socorro** gerada que irá transportar esses documentos nos campos **Fil. Vge. Trf. - DUA\_FILVTR** e **Num. Vge. Trf. - DUA\_NUMVTR**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087651913)

* Com o parâmetro **MV\_TMSCVIA -** igual à **3 - Pergunta,**o Sistema pergunta se deseja cancelar ou encerrar essa viagem.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087651993)

* Após a conclusão do apontamento da ocorrência, a viagem original estará com o *status* escolhido na pergunta anterior e o documento estará na viagem de socorro.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087656073)

* Considerando o manifesto da viagem, nesse momento deve ser transmitido o encerramento da viagem original.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087655973)

* Após isso, o processo poderá prosseguir normalmente por meio da **Viagem de Socorro**, efetuando o **carregamento** dos documentos, **fechamento da viagem**, geração de um **novo manifesto,** apontamento das **operações** de transporte e **registros de ocorrência** para encerrar a **Viagem de Socorro** e seu manifesto.

**Importante**O parâmetro **MV\_TMSCVIA** só terá ação se todas os documentos da viagem original tenham sido encerrados, cancelados e/ou transferidos para a viagem de socorro. Se transferir apenas 1 documento para a viagem de socorro e deixar outro documento não encerrado na viagem original, esta não será encerrada ou cancelada, pois o Sistema entende que ainda há uma tarefa a ser executada nessa viagem.
