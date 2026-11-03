---
article_id: 360026197711
category: Gestão de Frotas
content_hash: fd776dfd08f7d6e7914d44c5d4fc1c7430c103fe0aafa281a897c95c40d6f048
fetched_at: '2026-06-28T22:42:39.610875+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Utilização do contador por km em pneus
  com o primeiro contador utilizando horímetro
type: support-article
updated_at: '2021-09-01T21:19:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026197711-Manufatura-Linha-Protheus-MNT-Utiliza%C3%A7%C3%A3o-do-contador-por-km-em-pneus-com-o-primeiro-contador-utilizando-hor%C3%ADmetro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:30 min****Dúvida**Como utilizar contador por **KM - Quilômetros** em pneus, quando o veículo tem o primeiro contador utilizando **Horímetro**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Todas as versões  
  
**Solução**Para utilização do contador por **KM** em pneus que o veículo possui o primeiro contador utilizando o **Horímetro**, serão necessários seguir os seguintes passos para configuração:

1. Acesse o **Configurador**.
2. Em **Base de Dados/Dicionário/Base de Dados**, altere os parâmetros a seguir com um serviço para o esquema de rodados.
   * **MV\_NGSEREF -  Código do serviço para Reforma de pneus – Recape = PNEREF**
   * **MV\_NGSECON - Código de serviço para Conserto de Pneus = PNECON**
   * **MV\_NGSERPN - Código de serviço utilizado para movimentação de Pneus = PNEMOV**
   * **MV\_NGRODIZ - Código de serviço utilizado para O.S de Rodízio de Pneus = PNEROD**
   * **MV\_NGSERCA - Código de serviço para Canibalismo = PNECAN**
   * **MV\_NGSINSP -  Código de serviço para inspeção de pneus = PNEINS**
3. Acesse o módulo de **Manutenção de Ativos - SIGAMNT**
4. Em **Atualizações/Controle de Oficina/Bens/Bens**, incluir cinco bens, conforme a relação a seguir.
   * Um bem com categoria **4 - Frota** não integrada ao **TMS - Gestão de Transportes**, possuindo contador próprio e segundo contador
   * Quatro bens com categoria **3 - Pneu**, com o contador controlado pelo pai da estrutura e com o segundo contador.
5. Em **Atualizações/Controle de Oficina/Manutenção/Serviços**, incluir um serviço do tipo **corretivo** com o mesmo conteúdo do parâmetro **MV\_NGSERPN - PNEMOV**.
6. Em **Atualizações/Controle de Pneus/Estrutura/Esquema Mod. 2**, incluir uma estrutura, informando no esquema o mesmo nome da família e tipo modelo previamente cadastrados. Em seguida, selecionar o pneu, informar a mesma família do pneu cadastrado e confirmar.
7. Em **Atualizações/Controle de Oficina/Ordem de Serviço/Corretivo**, incluir uma ordem de serviço corretiva de movimentação de pneu com o serviço **PNEMOV**. Abrir a **O.S. - Ordem de Serviço** em rodados e incluir os pneus na estrutura.
8. Em **Atualizações/Controle de Oficina/Manutenção/Manutenção**, incluir uma manutenção para o bem pai controlada pelo contador **1 - horímetro** e outra para o pneu pelo contador **2 - hodômetro**.

**Importante**O Sistema não difere reporte do **Hodômetro** ou **Horímetro**, para ele o que conta é a quantidade contida no campo. A manutenção tem a opção de ser orientada por primeiro ou segundo contador. A sugestão recomendada é que o pneu possua um segundo contador, assim como o bem pai, sendo o segundo contador um **Hodômetro** o pneu terá o controle correto.
