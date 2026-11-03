---
article_id: 360025660032
category: Manutenção de Ativos (SIGAMNT)
content_hash: 884453b526ceaf494a0767d36d553df84bef5d654d8fa7e1a163810ea0220768
fetched_at: '2026-06-28T22:42:33.040320+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Configuração de Parâmetros
type: support-article
updated_at: '2024-03-20T14:11:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025660032-Manufatura-Linha-Protheus-MNT-Configura%C3%A7%C3%A3o-de-Par%C3%A2metros
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22209049567895)***Tempo aproximado para leitura: **00:13:40 min****Dúvida**Quais os principais parâmetros do módulo de **Manutenção de Ativos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Um parâmetro é uma variável que atua como elemento chave na execução de determinado processamento. De acordo com o seu conteúdo é possível obter diferentes resultados. Para configurar um parâmetro utilize o ambiente **Configurador**.  
  
Todas as variáveis são iniciadas pelo prefixo **MV\_**, e agem sobre diversas operações no Sistema.  
  
Os principais parâmetros pelo ambiente **Manutenção de Ativos** são:

|  |  |  |
| --- | --- | --- |
| **Parâmetros** | **Descrição** | **Conteúdo** |
| **MV\_ESTHOME** | Indica o momento que o estoque será debitado.  **S** - **Abastecimento;** **C** - **Conciliação;** **N** - **Não baixa estoque**. |  |
| **MV\_ESTNEG** | Indica se o Sistema permite que os saldos em estoque dos produtos fique negativo, através de movimentações. | **S** **N** |
| **MV\_INTTMS** | Identifica se o módulo do **Gestão de Frotas - SIGATMS** está integrado aos outros módulos. | **F** |
| **MV\_LOCALIZ** | Indica se os produtos poderão usar controle de localização física ou não.  **S** **- Sim**;  **N** **- Não**. | **N** |
| **MV\_MCONTAB** | Módulo **Contábil** utilizado pelo **Advanced   CTB** = **SIGACTB** - **Contabilidade Gerencial** - tabela **CTT** **- Centro de custo**.  **CON = SIGACON - Contabilidade** – tabela **SI3** - **Centro de custo**. | **CTB** |
| **MV\_MNTOSCO** | Permite mais de uma **OS - Ordem de serviço** **Corretiva** ou **Manual** aberta para a mesma data sem que a anterior esteja finalizada.   **S** **- Sim**;  **N** **- Não**. | **S** |
| **MV\_MNTUSA** | Determina integração do **MNT - Manutenção de Ativos** com **PCP - Planejamento e controle da produção/Compras/Estoque**. Somente para versão inferior a 5.08 ou específicos - programas. | **SSS** |
| **MV\_NG1SERA** | Código do serviço relacionado com a tabela **ST4 - Serviços de Manutenção**que será cadastrado na **OS** quando for gerada. | **CORRE01** |
| **MV\_NGALERT** | Número de dias a ser considerado, a partir da data atual do Sistema, para disparar *Workflow* de alerta para os usuários cadastrados na tabela **TPT - Grp Contas E-mail x Funcion**. | **365** |
| **MV\_NGALMUL** | Lista todas as **Árvores Lógicas** da empresa quando a tabela **TAF - Nivel Organizacional** está exclusiva.  **0 -** **Filial Corrente**;  **1 -** **Todas as Filiais**. | **0** |
| **MV\_NGAUTON** | Indica se consiste autonomia do veículo.  **1** - **Não consiste**;  **2** - **Consiste sempre**; **3** - **Consiste apenas em rotinas de abastecimento**. | **2** |
| **MV\_NGCLICK** | Disponibiliza o uso do botão direito do mouse no **SIGAMNT**. | **S** |
| **MV\_NGCMAQP** | Indica se o Sistema deve consistir retorno de produção em máquina parada.   **S** **- Sim**;  **N** **- Não**. | **S** |
| **MV\_NGCOFIX** | Percentual utilizado para calcular o contador fixo da manutenção. O percentual pode ser de 0 a 100. | **50** |
| **MV\_NGCOPOS** | Indica se deve ser disparada a tela para permitir fazer cópias da ordem de serviço corretiva incluída no **MNTA420 - OS Corretiva**. Informar   **1 - Não dispara**; **2 - Dispara a tela**. | **1** |
| **MV\_NGCOQPR** | Caso o parâmetro esteja configurado com **S**, no momento do reporte de insumo, o Sistema verifica se a quantidade de peças de reposição informada no **Cadastro do Bem** está de acordo com a quantidade informada no Reporte. Não será permitida a inclusão de quantidades superiores ao que foi registrado no **Cadastro do Bem**, nesta situação o Sistema exibirá uma mensagem de alerta.  Caso o parâmetro esteja configurado com **N**, no momento do reporte de insumo, o Sistema não verifica se quantidade de peças de reposição informada no **Cadastro do Bem** está de acordo com a quantidade informada no **Reporte**. | **N** |
| **MV\_NGCORAB** | Indica se o Sistema deve verificar e alertar se tem corretiva aberta para o mesmo **Bem** e mesmo **Serviço**, no momento da inclusão de uma **Ordem de serviço corretiva**. | **N** |
| **MV\_NGCORPR** | Permite gerar empenho e solicitação de serviço para ordem de serviço:   Corretivas  **S** **- Sim**;  **N - Não**. | **N** |
| **MV\_NGDPST9** | Indica se poderá duplicar código do bem e *tag* entre filiais e empresas.   Para  **0** **- Não verifica**;  **1** **- Por empresa**;  **2** **- Por filial**;  **3 - Filial e empresa**. | **0** |
| **MV\_NGEPICC** | Indica se é permitido excluir o **EPI - Equipamento de proteção individual** que está entregue a um funcionário, sendo que o **EPI** está vinculado ao **Centro de Custo** ou a **Função**.   **S** **- Sim**;  **N** **- Não**. | **1** |
| **MV\_NGETAEX** | Bloqueia ou não, a finalização da **Ordem de Serviço** com etapas não respondidas e/ou sem informar o executante. | **2** |
| **MV\_NGGERSA** | Indica se gera **Solicitação ao Armazém**, em vez de gerar **Solicitação de Compra**.  **S** **- Sim**;  **N** **- Não**; **P - Produtos apenas**. | **N** |
| **MV\_NGHISES** | Quando o parâmetro estiver configurado em **N**, mesmo que o ambiente **Manutenção de Ativos** esteja integrado com o ambiente **Estoque**, não efetuará a baixa no estoque, quando o serviço da ordem estiver igual a **HISTOR - Histórico**, habilitará também o campo de custo para informar os valores do insumo no retorno da ordem de serviço.  Quando o parâmetro estiver configurado em **S**, deverá baixar do estoque os insumos também das ordens de serviço de **Histórico**. | **N** |
| **MV\_NGINFOS** | Indica se na transferência de bens é obrigatório informar a ordem de serviço.   Para **S** **- Sim**;  **N** **- Não**. | **1** |
| **MV\_NGIOSAU** | Indica se o Sistema permite imprimir **OS - Ordem de serviço** geradas automaticamente por contador.   Informar  **S** **- Sim**;  **N** **- Não**. | **S** |
| **MV\_NGLOCPA** | Indica o almoxarifado padrão para gerar os produtos utilizados pelo **SIGAMNT** -  **Manutenção/Terceiros.** | **01** |
| **MV\_NGMNTAT** | Integração **Manutenção - MNT** com **Ativo - ATF**. Informar **\" \"ou\"N\". Não Integra**;   **1** - **Alterações no ATF replicarão no MNT**;  **2** **- MNT p/AT**F; **3 - MNT p/ATF e ATF p/MNT**. | **N** |
| **MV\_NGMNTBG** | Indica qual o serviço específico de abertura das **Ordens de Serviço** do **BANDAG**. |  |
| **MV\_NGMNTCM** | Integração **Manutenção - MNT** com **Compras COM**.   Informar **S** **- Sim**;  **N** **- Não**. | **N** |
| **MV\_NGMNTCP** | Indica se a geração da solicitação de compras e pelo processo do compras - **S**; Ou pelo processo da programação e **controle de produção - PCP** - **N**. | **N** |
| **MV\_NGMNTES** | Integração **Manutenção - MNT** com **Estoque - EST**.   Informar **S** **- Sim**;  **N** **- Não**. | **N** |
| **MV\_NGMNTFI** | Integração **Manutenção - MNT** com **Financeiro - FIN**.  Informar **S** **- Sim**;  **N** **- Não**. | **S** |
| **MV\_NGMNTMS** | Integração do **Manutenção de Ativos - MNT** com **Gestão de Transporte - TMS**.   Informar **S - Sim**;  **N - Não**. | **S** |
| **MV\_NGMNTNO** | Permite vincular ou não a **Ordem de Serviço** automaticamente aos pedidos informados.  Sendo:  **S - Sim;  N - Não.** | **1**  **2** |
| **MV\_NGMNTPC** | Integração **Manutenção - MNT** com **Planejamento controle da produção - PCP**.   Informar **S** **- Sim**;  **N - Não**. | **N** |
| **MV\_NGMNTQN** | Integração **Manutenção - MNT** com **Não-Conformidade - QNC**.   Informar **S** **- Sim**;  **N** **- Não**. | **N** |
| **MV\_NGMNTRH** | Informar **S** **- Sim**;  **N** **- Não**. | **N** |
| **MV\_NGMNTSC** | Indica se o modo de aglutinar os itens das solicitação de compra dos produtos.   Informar **1** **- Normal**;  **2** **- Por OP**;  **3** **- Por necessidade**. | **1** |
| **MV\_NGMOTAB** | Indica quais tipos de motoristas podem realizar abastecimentos.  **1 - Próprio**; **2** **- Terceiro**; **3** **- Agregado**. |  |
| **MV\_NGMOTGE** | Indica o **CPF - Cadastro de pessoa física** do motorista. Será utilizado para abastecimentos que não contém motoristas predefinidos. |  |
| **MV\_NGMULOS** | Permite gerar múltiplas **OSs** a partir do retorno da solicitação de serviço. | **N** |
| **MV\_NGNOVOS** | Questionará quando gerar nova **OS**?  **1** - Gerar apenas quando não existir **OS** aberta - **mesmo bem + serviço + sequência**;  **2** - Gera mesmo se existir **OS** aberta. | **2** |
| **MV\_NGOCINS** | Indica causa para movimentação posicional após inspeção |  |
| **MV\_NGOSAES** | Caso o parâmetro esteja configurado para **S**, ele verificará as ordens dos bens filhos da estrutura de bens e gerará a ordem de serviço automática para os bens filhos, sem consultar o usuário.  Caso o parâmetro esteja configurado para **C**, ele consultará o usuário por meio de uma mensagem de alerta perguntando se deverão ser geradas as ordens de serviço para os bens filhos.  Caso o parâmetro esteja configurado para **N**, ele não gerará as ordens de serviço para os bens filhos e também não consultará o usuário. | **N** |
| **MV\_NGOSAUT** | Indica se deve gerar **OS** automaticamente sempre que uma **OS** por tempo for finalizada. | **N** |
| **MV\_NGOSNFE** | Informa se as **Ordens de Serviço** em lote dependem de um documento de entrada e para que possam ser realizadas por meio da rotina de **OS** **Lote**, quando integrada ao módulo de **Estoque/Custos** ou **Compras**  Se o parâmetro estiver configurado com a opção **Sim** é necessário vincular a **OS** a um documento de entrada para que ela possa ser recebida como realizada, e no recebimento serão apresentados os dados de **Nota Fiscal**, **Série Nf** e **Vl. Serviço do documento**.   Se o parâmetro estiver configurado como **Não**, os campos de **Nota Fiscal** e **Serie Nf** serão abertos para que sejam preenchidos manualmente ou sejam deixados em branco, para efetuar o recebimento como realizado e informar os campos **Desenho** e **Vl. Serviço**. | **1** |
| **MV\_NGOSPRO** | Indica se o Sistema deve alertar se já existe uma **OS** para o mesmo bem/serviço/sequência com data próximo - x dias, a que está sendo aberta. | **30** |
| **MV\_NGPGDIA** | Indica se a Programação de **OS** deve ser diária.   Informar **S** **- Sim**;  **N** **- Não**. |  |
| **MV\_NGPGEVE** | Indica se a Programação pode ser cadastrada por evento. | **N** |
| **MV\_NGPRAUT** | Indica o percentual aceitável de variação de autonomia. Este percentual pode variar de 0 a 100. |  |
| **MV\_NGPREVE** | Indica se será mostrada a informação de que há ordem de serviço preventiva atrasada e em qual momento o alerta deve ser mostrado. As opções disponíveis são:  **1** - Abertura de **OS** **Corretiva**, determina que a mensagem de alerta apenas será exibida na inclusão de uma **OS Corretiva - MNTA420**.  **2** - Abertura de **SS - Solicitação de serviço**, determina que a mensagem de alerta apenas será exibida na abertura de **Solicitação de Serviço - MNTA280**.  **3 -** **OS** **Corretiva** ou **SS**, a mensagem será apresentada tanto na abertura de **OS** **Corretiva** como para **Solicitação de Serviço.**  **4** - Não exibir, determina que não deve ser apresentada mensagem alertando para ordem preventiva atrasada. | **1** |
| **MV\_NGPRSB2** | Indica se busca o preço médio na tabela **SB2 - Item custo** quando integrado ao estoque.   Informar: **S** **- Sim**;  **N** **- Não**. |  |
| **MV\_NGPRVDI** | Percentual  de tolerância que deverá  ser aceita quando do cálculo da nova variação dia. | **10** |
| **MV\_NGRECAL** | Permite o recálculo de custo de insumo on-line.   Informar: **S** **- Sim**;  **N** **- Não**. | **N** |
| **MV\_NGREPRE** | Indica se deve mostrar insumos x quantidades ainda não reportadas conforme os insumos previstos na finalização de **OS** no retorno. | **N** |
| **MV\_NGREPRO** | Reprograma ordens de serviço preventiva, caso a data fim real da **OS** finalizada seja maior que inicio previsto da **OS** existente, para o mesmo **Bem/Serviço/Seqüência**.  Informar: **S** **- Sim**;  **N** **- Não**. | **N** |
| **MV\_NGRESIN** | *E-mails* dos responsáveis por **Sinistro**. |  |
| **MV\_NGRESMU** | *E-mails* dos responsáveis por multas. |  |
| **MV\_NGRETOS** | Determina se há retorno de **OS** de produção. Para   **0** - **Não retorno**; **1** - **Retorno via SD3**. | **0** |
| **MV\_NGRHMKP** | Identifica o percentual de *MARKUP* a ser aplicado ao salário do funcionário de 0,00 a 999,99%. | **0** |
| **MV\_NGSALHO** | Condiciona a alteração dos campos **Código, Nome, C.Custo, Turno** na tabela **ST1 - Funcionário**. | **N** |
| **MV\_NGSERVE** | Identifica o caminho do servidor para acessar os arquivos necessários para montar gráficos. | **\\SYSTEM\** |
| **MV\_NGSSWRK** | Indica se no modulo de **Solicitação de Serviço** será utilizado envio de mensagens por *Workflow* online pelos solicitantes.   Informar: **S** **- Sim**;  **N** **- Não**. | **N** |
| **MV\_NGSTLPH** | Indica o código do *status* do veículo que está liberado para o processo de penhora. Este código será  atualizado automaticamente no cadastro de bens no momento em que for liberado da penhora |  |
| **MV\_NGSTPHR** | Indica o código do *status* do veículo que está no processo de penhora. Este código será  atualizado automaticamente no cadastro de bens no momento em que o veículo for cadastrado como penhorado. |  |
| **MV\_NGTARGE** | Quando habilitado, permite a utilização da rotina **Tarefas genéricas**. |  |
| **MV\_NGTNDFL** | Identifica se no retorno de **OS** corretiva será obrigatório a digitação da irregularidade.   Informar: **S** **- Sim**;  **N** **- Não**. | **S** |
| **MV\_NGTOLVL** | Indica o percentual de tolerância para fechamento de **Nota Fiscal**. |  |
| **MV\_NGUNIDT** | Identifica o tipo de unidade da quantidade quando for informado um insumo que utiliza tipo de unidade e hora   Informar: **D** **-** **Decimal**;  **S** - **Sexagesimal**. |  |
| **MV\_NGVEROS** | Se o conteúdo do parâmetro estiver preenchido com **V** – consultará uma única vez o usuário sobre a existência de ordens de serviço abertas, solicitando sua confirmação.   Caso selecione **Sim** será gerada a ordem de serviço automática mesmo que possua ordem de serviço aberta para o mesmo bem, serviço e seqüência.   Caso selecione **Não**, não será gerada a ordem de serviço para as manutenções que já possuírem ordem de serviço aberta.  Caso o conteúdo do parâmetro esteja preenchida com **S** - **Sim** consultará o usuário a cada manutenção sobre a existência de ordens de serviços abertas, solicitando sua confirmação.  Caso o conteúdo do parâmetro esteja preenchida com **N** - **Não** consultará o usuário e gerará ordem de serviço automática mesmo com ordens de serviço em aberto. |  |
| **MV\_NGWFHT** | Indica o **IP** e a **Porta** para a comunicação **HTTP** do *workflow*. | **HTTP://127.0.0.1:8080** |
| **MV\_NGWFLG** | Indica se gera **log** específico do processamento do *workflow*.   Informar: **0** - **Desabilita**;  **1** **- Habilita**. | **1** |
| **MV\_PRODAUT** | Gera lançamentos automáticos de **Produto** das **Ordens de produções** vinculadas a **OP** **Pai** - **Produto Acabado**.   Informar **T** - **Gera**;  **F** - **Não gera**. | **F** |
| **MV\_PRODMNT** | Item de estoque para ordem de produção do **SIGAMNT**. | **MANUTENÇÃO** |
| **MV\_PRODTER** | Item de estoque que indica Terceiros no **SIGAMNT** | **TERCEIROS** |
| **MV\_RASTRO** | Determina a utilização ou não da rastreabilidade dos lotes de produção.   Informar: **S** **- Sim**;  **N** **- Não**. |  |
| **MV\_RELT** | Diretório especificado para impressão de relatório | **\SPOOL\** |
| **MV\_ULMES** | Data do último fechamento do estoque. | **19970101** |
| **MV\_VARDIA** | Número de ocorrência na variação dia. | **10** |
| **MV\_WFDIR** | Diretório de trabalho do *Workflow* | **\workflow** |
| **MV\_NGABAVL** | Valida o relacionamento do veículo com esquema padrão, estrutura padrão, manutenção padrão e manutenção.  **1** **- Valida**;  **2** **- Não Valida**. | **2;2;2;2** |
