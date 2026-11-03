---
content_hash: 598f60c43bacdf9faac91c1a471d46c0f5c5344138eaa877b8ddf7c830b66d44
fetched_at: '2026-06-29T00:09:34.624372+00:00'
page_id: '425459208'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Processo de Ordem de Serviço de Pneus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459208
version: 3
---

**Backoffice RM x Protheus SigaMNT - Processo de Ordem de Serviço de Pneus**

---

O processo de Ordem de Serviço(OS) de Pneus tem por objetivo controlar os pneus que estão saindo da empresa para reforma (reparo e consertos).

O registro dos pneus que serão consertados e/ou reformados é realizado através da rotina de O.S. em Lote, onde deve-se registrar quais os pneus serão enviados para um determinado fornecedor, para um determinado serviço.  Somente pneus com status "Aguardando Reforma" poderão ser incluídos.

Para cada pneu incluído no lote será criado uma Ordem de Serviço no BackOffice com suas respectivas movimentações Solicitação de Armazém ou Solicitação de Compra. O tipo de solicitação que será gerada irá considerar a parametrização do SigaMNT Gestão de Frotas.

Quando o BackOffice processar a Solicitação de Armazém ou a Solicitação de Compra, será reportado um insumo de terceiro para o SigaMNT.  O insumo é reportado através da mensagem StockTurnOver.

Na rotina de O.S. em Lote é possível também fazer o recebimento dos pneus que voltaram da reforma. Para os pneus recebidos o SigaMNT irá enviar mensagem de atualização de status da OS de cada pneu recebido com seus respectivos itens reportados. Os pneus que compõe o lote e não foram recebidos terão suas OS's canceladas e as suas respectivas SA's ou SC's excluidas, ficando o SigaMNT responsável por enviar estas mensagens ao BackOffice.

Fica a cargo das regras de negócio do SigaMNT Gestão de Frotas a definição das solicitações (armazém ou compra) necessárias em cada O.S. de Pneu, que assim enviará  as respectivas mensagens para a criação dos movimentos no BackOffice.

**Processo de geração de OS de Pneus**

**1º)** Gerar a OS no SigaMNT para os pneus que estejam aguardando reforma/conserto. Para cada pneu é gerada uma OS e para cada OS é gerada uma SA ou SC para realização de serviço de terceiros  
 ***OBS:*** *Para detalhes de como uma OS de Pneus no Protheus SigaMNT favor consultar a documentação do mesmo.*

**2º)** Verificar no BackOffice os movimentos gerados (OS, SA e SC). Para isso é necessário acessar o tipo de movimento parametrizado para gerar OS, SA e SC.   
 Os movimentos de OS são criados através da mensagem "MaintenanceOrder" e os movimentos de SA e SC através da mensagem "Request", sendo que o campo type diferenciará qual movimento será criado. Campo type=000 gerará movimento de SA (Solicitação de Armazém) e campo type=001 gerará movimentos SC (Solicitação de Compra).

**3º)** A SA ou SC é recebida pelo BackOffice.

**4º)** Se o parâmetro MV\_NGOSNFE estiver ativo no SigaMNT, o Backoffice deve realizar então uma aplicação direta na OS aberta, relacionando a SA/SC gerada. Nesse momento o MNT será atualizado com o número da nota fiscal na ordem de serviço, o que indica a realização do serviço.

**5º)** Após receber a SA ou SC será disparada uma mensagem para o SigaMNT para realizar o insumo de terceiro na OS. A SA ou SC fica como recebida. A SA ou SC deverá ser recebido no BackOffice através de um movimento de baixa.

**6º)** Em seguida é possível realizar o recebimento da OS em lote no SigaMNT. Todas as ordens de serviço que forem realizadas (recebidas) serão terminadas e as não realizadas serão canceladas.

**Importante:**

Movimentos que integrem ordem de serviço de pneu devem possuir os seguintes parâmetros no backoffice (Aba Manutenção no cadastro de tipo de movimento):

* Integrado com SigaMNT – Ativo

---

Para mais informações sobre o processo de Ordem de Serviço de Pneus , acesse os boletins técnicos

**Recursos Adicionais**

TDN - Boletim Técnico : [Processo de Ordem de Serviço de Pneus](http://tdn.totvs.com/download/attachments/76251261/PROTHEUS_BT_ORDEM+DE+SERVI%c3%87O+DE+PNEUS_BR_CON000158.pdf?version=1&modificationDate=1380054070000)
