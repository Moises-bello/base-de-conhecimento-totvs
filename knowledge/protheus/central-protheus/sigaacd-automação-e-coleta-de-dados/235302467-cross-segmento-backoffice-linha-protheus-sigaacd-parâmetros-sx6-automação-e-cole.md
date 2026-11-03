---
article_id: 235302467
category: SIGAACD - Automação e Coleta de Dados
content_hash: 9ff563c0eaa7f0b37cb31b84339bfd88e659657381d7df6b11aa7dffc5d4a410
fetched_at: '2026-06-28T22:39:13.706577+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Parâmetros (SX6) -
  Automação e Coleta de Dados.
type: support-article
updated_at: '2026-03-23T22:27:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235302467-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Par%C3%A2metros-SX6-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados
---

O módulo Automação e Coleta de Dados (ACD) do TOTVS Protheus possui diversos parâmetros que controlam processos como CQ, endereçamento, estoque, expedição, produção, recebimento e inventário. Cada parâmetro define comportamentos específicos, como validação de endereços, tipos de movimentação, impressão de etiquetas, controle de conferência, ajustes automáticos e sincronização com o aplicativo Meu Coletor de Dados.

**Dúvida**

Quais são os parâmetros que envolvem o Meu Coletor (ACD)?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**

Segue abaixo os principais parâmetros do módulo **Automação e Coleta de Dados**:

| Processo | Parâmetro | Tipo | Descrição |
| --- | --- | --- | --- |
| **CQ** | **MV\_CBENDCQ** | C | Valida os "endereços" de inspeção para C.Q. separados por ";", caso este parâmetro esteja em branco o sistema não faz tal validação.  Exemplo: 98INSPECAO; |
| **CQ** | **MV\_CBPE003** | L | Acerto do CB0 no estorno do CQ via Protheus. |
| **CQ** | **MV\_CBPE010** | L | Valida estorno de CQ via Protheus. |
| **CQ** | **MV\_CBPE020** | L | Faz o estorno automatico do C.Q (Caso exista prod. no C.Q),Somente Protheus. |
| **ENDEREÇAMENTO** | **MV\_ENDPROC** | C | Endereço padrão para o  endereçamento automático no armazém de processos (MV\_PROC). |
| **ENDEREÇAMENTO** | **MV\_CBPE016** | L | Faz Acerto do CB0 no estorno da Distribuição. |
| **ESTOQUE** | **MV\_TMCBRP** | C | Tipo de movimentação para Requisição de Processo. |
| **ESTOQUE** | **MV\_TMCBDP** | C | Tipo de movimentação para Devolução de Processo. |
| **ESTOQUE** | **MV\_CBARMPD** | C | Armazém padrão utilizando no envio e retorno de Processo quando não é utilizando código interno. |
| **EXPEDIÇÃO** | **MV\_ACDSERI** | C | O parâmetro informa a série da nota fiscal de saída que será gerada. Utilizada na distribuição de volumes. Exemplo: UNI |
| **EXPEDIÇÃO** | **MV\_CBIXBNF** | C | Nome do ponto de entrada para emissão de nota fiscal de saída para expedição RF. Exemplo: "NFEXAMP" |
| **EXPEDIÇÃO** | **MV\_CFENDIG** | C | No processo de expedição RF, quando o parâmetro está ativado, 1-Sim, a cada conferência de produtos diferentes é exigido que se faça a conferência do endereço, mesmo se o endereço do produto em questão seja o mesmo do produto que foi conferido anteriormente. Já quando o parâmetro está desativado, 0-Não, esta conferência de endereço é requisitada uma única vez caso o endereço seja o mesmo. 0-Não 1-Sim |
| **EXPEDIÇÃO** | **MV\_CONFEND** | C | Este parâmetro habilitado, 1-Sim, exige que o endereço seja conferido na expedição. Caso contrário, será exigida somente a leitura das etiquetas dos produtos. 1-Sim 0-Não |
| **EXPEDIÇÃO** | **MV\_IACD01** | C | O parâmetro deverá conter o Código do Local  de impressão utilizado no programa de expedição. Este código se refere à tabela CB5 do módulo ACD. |
| **EXPEDIÇÃO** | **MV\_REMIEMB** | C | Parâmetro que informa se a etiqueta do produto será reimpressa  no processo de embalagem do módulo ACD. 0-Não 1-Sim |
| **EXPEDIÇÃO** | **MV\_OSEP2UN** | C | Na Ordem de Separação o programa utiliza a 2 U.M. caso a quantidade a separar seja menor que a 2 U.M o sistema utilizará a 1 U.M. 0-Não utiliza   1-Utiliza |
| **EXPEDIÇÃO** | **MV\_CBEXCNF** | C | O parâmetro define se a nota fiscal será excluída pelo Protheus ou pelo coletor rádio freqüência. Após a exclusão, a Ordem de Separação poderá ser selecionada novamente para ser feito o estorno das embalagens e/ou etiquetas lidas. 1 – Protheus; 2 – RF (Rádio Frequência) |
| **EXPEDIÇÃO** | **MV\_DIVERPV** | C | Referenciado a um código cadastrado na tabela de divergências (tabela CB4) ,utilizado na Ordem de Separação. Quando estiver fazendo a separação dos itens e não deseja que o item seja separado, deverá apontar a divergência contida no parâmetro para que a Ordem de Separação não solicite mais o item e o mesmo seja estornado do Pedido de Vendas. Isto não impede posteriormente liberar o item deste pedido e gerar uma nova Ordem de Separação. Operação válida quando não se deseja fazer o estorno da Ordem de Separação pois a mesma já se encontra em andamento. |
| **EXPEDIÇÃO** | **MV\_CBVLDOS** | C | Permite o embarque simultâneo de Ordens de Separação diferentes  1-Sim  2-Não |
| **EXPEDIÇÃO** | **MV\_CBRQEST** | L | Considera a Estrutura do Produto x Saldo na geracao da Ordem de Separacao |
| **EXPEDIÇÃO** | **MV\_CBVLDTR** | C | Valida a Transportadora na rotina de Embarque  1-Sim  2-Não |
| **EXPEDIÇÃO** | **MV\_CBPE001** | L | Habilita o Ponto de entrada Template SF2520E Acerto do CB0 na Exclusão da NF de devolução via Protheus Somente se a etiqueta estiver com NF de Devolução gravada |
| **EXPEDIÇÃO** | **MV\_CBPE005** | L | Faz Filtro do PV na Geração da Nota - Mata460 |
| **EXPEDIÇÃO** | **MV\_CBPE006** | L | Atualiza CB7 (Cabeçalho da Ordem de Separação) com o Numero da Nota e Serie, quando Nota Gerada Pelo Protheus. |
| **EXPEDIÇÃO** | **MV\_CBPE007** | L | Gravação do código da Ordem de Separação para cada Item da Nota (SD2->D2\_ORDSEP). |
| **EXPEDIÇÃO** | **MV\_CBPE008** | L | Estorno das informações da nota na Ordem de Separação. |
| **EXPEDIÇÃO** | **MV\_CBPE013** | L | Faz validação do estorno da liberação dos PV's. |
| **EXPEDIÇÃO** | **MV\_CBPE021** | L | Validacao da exclusao da Nota Fiscal de Saida (MATA520/MATA521). |
| **EXPEDIÇÃO** | **MV\_CBOSPRC** | L | Permite ou nao gerar Ordens de Separacoes parciais |
| **EXPEDIÇÃO** | **MV\_CBPE022** | L | Grava o numero da ordem de separação no campo C9\_ORDSEP no exato momento da geraçãoo do registro. |
| **EXPEDIÇÃO** | **MV\_CFEMBS** | C | Permite a conferência da Nota Fiscal de Saida atraves do Monitor de Embarque Simples do Protheus (1=Nao;2=Sim) |
| **EXPEDIÇÃO** | **MV\_CBPE023** | L | Bloqueia a alteração dos Pedidos de Vendas quando uma Ordem de Separação for Gerada. |
| **GENÉRICO** | **MV\_ACDCB0** | C | Neste parâmetro devem ser informados os tipos de etiquetas que irão utilizar o código interno (CB0) para controle de codificação. Tipos usados: '01' - produto '02' - localização/Endereço '04' - usuário '05' - volume saída '06' - transportadora '07' - volume entrada Ex.: Para se utilizar um controle de codificação para produtos e localização/endereço, o parâmetro deverá ser preenchido da seguinte forma: 01\*02 |
| **GENÉRICO** | **MV\_CB0ALFA** | C | Quando o parâmetro está como 1-Sim, os códigos internos são gerados em seqüenciais que consideram caracteres alfanuméricos para sua composição. Ex.: A000000000 Caso esteja com 0-Não a composição se dá somente a partir de caracteres numéricos. Ex.: 0000000001 0-Não 1-Sim |
| **GENÉRICO** | **MV\_CHKQEMB** | C | Confere quantidade de produto granel na embalagem RF para código interno. 1-Sim 0-Não |
| **GENÉRICO** | **MV\_ATVCONS** | C | Ativa/Desativa a consulta VT100 (CTRL+C) (1-Sim,2-Nao) |
| **GENÉRICO** | **MV\_CODCB0** | C | Código Seqüencial de identificação do código de barras, este código é gerado na Impressão das etiquetas que utilizam o Código interno (CB0) . |
| **GENÉRICO** | **MV\_EANP2** | L | Permite utilizar a segunda parte da etiqueta. |
| **GENÉRICO** | **MV\_INTACD** | C | Identifica se usa a integração ACD com os outros módulos. 0-Não 1-Sim |
| **GENÉRICO/PE** | [**MV\_LOGACD**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/39243178305687-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-gerar-um-Log-de-auditoria-para-o-ACD) | C | Contém a configuração do Log do ACD, sendo asterisco\* para que haja o controle de todos os logs ou a indicação por log desejado. Tipos de Log disponíveis: ''01' – endereçamento '02' – transferência '03' – baixa de cq '04' – inventário '05' – conferência '06' – requisição '07' – divisão etiqueta '08' – preparação endereçamento '‘09' – expedição '10' - devolução Ex.: O usuário deseja controlar somente o log sobre os endereçamentos e os inventários realizados. Então ele irá preencher com : 01,04 \* Todos ou 01,02,03,04... |
| **GENÉRICO** | **MV\_CBNEWID** | C | Novo id utilizando a função soma1() dentro da função cbproxcod(), usado na geração do id da etiqueta. 0-Não – utiliza uma codificação com maior numero de combinações porem não é possível obter a informação indexada conforme a criação do código. 1-Sim – possibilita ter a informação indexada conforme a sua criacao |
| **GENÉRICO** | **MV\_CBAJUQE** | L | Permite ao usuário ajustar a Quantidade por Embalagem na rotina de impressão de etiquetas produtos. .T.  – Habilita o ajuste da QTD por Embalagem .F. – Desabilita o ajuste da QTD por Embalagem. |
| **INVENTÁRIO** | **MV\_ALTENDI** | C | O parâmetro permite ou não fazer o ajuste das etiquetas dos produtos com os armazéns e endereços lidos na medida em que é feito o inventário. Exemplo: No momento está sendo inventariado o armazém 01, endereço A01 e o produto em questão foi estocado errado e a leitura de sua etiqueta aponta para o armazém 01, endereço B01. Caso o parâmetro esteja configurado para 1-Sim, a etiqueta do produto será corrigida para o endereço correto, caso contrario será informado que o produto lido será invalido. 0-Não 1-Sim. |
| **INVENTÁRIO** | **MV\_CBINVMD** | C | Define o Modelo do Inventário: 1-Contagem Batida 2-Saldo em estoque |
| **INVENTÁRIO** | **MV\_CODINV** | C | Código Seqüencial do Mestre de  inventario, este código é gerado automaticamente no momento em que um novo Mestre de Inventário é cadastrado. |
| **INVENTÁRIO** | **MV\_USUINV** | C | Código interno serializado por contagem de inventario de uso interno do sistema, portanto não mexer. |
| **INVENTÁRIO** | **MV\_VLDTINV** | C | Bloqueio o inventário por data. 0-Não, o sistema ira bloquear o produto ou endereço no momento que iniciar a contagem física e será desbloqueado automaticamente a ser feito o acerto de inventario e o parâmetro MV\_INVAUT deverá estar obrigatoriamente com 1-sim  1-SIM, o sistema ira bloquear o produto ou endereço no momento que iniciar a contagem física o  mesmo será desbloqueado somente com a virada do dia. |
| **INVENTÁRIO** | **MV\_VQTDINV** | C | Permite a digitação da quantidade na rotina de inventário quando utilizado o código interno (CBO). 0-Não 1-Sim |
| **INVENTÁRIO** | **MV\_CBCLABC** |  | Ativa o controle de classificacao ABC para analise de mestre de invetario |
| **INVENTÁRIO** | **MV\_INVAUT** | C | Define se o acerto do inventário será Automático ou será realizado pelo Gestor do Inventário (manual): 0=Não acerta 1=Acerto pelo coletor 2=Acerto pelo MONITOR 3=Ambos |
| **INVENTÁRIO** | **MV\_CBFCQTD** |  | Forca o foco na quantidade inventariada toda vez que estiver inventariando um produto. 1-Ativado;2-Desativado |
| **INVENTÁRIO** | **MV\_CBPE012** | L | Valida lançamento do inventário do ACD. |
| **PRODUÇÃO** | **MV\_CBREQD3** | C | Tipo do movimento para requisição da ordem de separação para produção RF. Este tipo de movimento deve estar devidamente cadastrado na tabela  de "Tipo Movimentação" – SF5. Exemplo: "501" |
| **PRODUÇÃO** | **MV\_IACD04** | C | O parâmetro deverá conter o Código do local de impressão utilizado no programa de Identificação de produto na produção (Apontamento da Produção). Este código se refere à tabela CB5 do módulo ACD. |
| **PRODUÇÃO** | **MV\_IMPIPOP** | C | Indica se  imprime  etiqueta de identificação do produto na produção.  0  - Não Imprime 1  - Imprime na produção, ou seja, no apontamento da Produção. |
| **PRODUÇÃO** | **MV\_NLOGACD** | C | Neste parâmetro é informado o código do evento que não será registrado no log. Exemplo: O usuário não quer registrar as requisições pois o volume delas é muito grande, logo o parâmetro deverá ser preenchido da seguinte forma: 06 |
| **PRODUÇÃO** | **MV\_IMETREQ** | C | Verifica se deve imprimir etiquetas na requisição. 0-Não 1-Sim |
| **PRODUÇÃO** | **MV\_MULTOPS** | C | Verifica se a requisição aceita múltiplas OPS. 0-Não 1-Sim |
| **PRODUÇÃO** | **MV\_VLDREQ** | C | Verifica se valida a quantidade a ser produzida com a quantidade  Requisitada para a OP. 1 - Valida na primeira operação; 2 - Valida na última operação. |
| **PRODUÇÃO** | **MV\_VLDEVAI** | C | Trata devolução com OP para produtos de apropriação indireta;  1 - Aceita quantidade maior do que a requisitada; 2 - Não aceita quantidade maior do que a requisitada;  3 - Permite escolha do usuário. |
| **PRODUÇÃO** | **MV\_SOLOPEA** | C | Solicita  operador no apontamento de producao ACD (1-Sim, 2-Nao) |
| **PRODUÇÃO** | **MV\_SGQTDOP** | C | Sugere como valor inicial do get o saldo da OP a ser apontado para a  Operação - rotinas de Produção PCP MOD1 e MOD2 do ACD 0-Não 1-Sim |
| **PRODUÇÃO** | **MV\_SGQTDRE** | C | Sugere como valor inicial do get o saldo da etiqueta lida – rotina de requisição / devolução (ACDV040) |
| **PRODUÇÃO** | **MV\_CBCALPR** | L | Calculo do total de horas na Prod.Mod2 via RF/ ACD .T. Usar calendario (Padrão) ou .F. usar calculo padrão da rotina da Produção Mod.2 (MATA681). |
| **PRODUÇÃO** | **MV\_CBCFSD4** | C | Confere se o produto a ser requisitado pertence ao empenho da Ordem de Produção. 1-Sim  2-Não |
| **PRODUÇÃO** | **MV\_CBCFSG1** | C | Confere se o produto a ser requisitado pertence a estrutura do PI ou PA a ser produzido. 1-Sim  2-Não |
| **PRODUÇÃO** | **MV\_CBFIMIN** | C | Informa se deve finalizar o início da operação que está sendo apontada no ato do apontamento da mesma independente de ter atingido o saldo. 1=Sim  2=Não (Default = 2) |
| **PRODUÇÃO** | **MV\_CBEMPRQ** | L | Considera o Saldo da tabela SBF com empenho na rotina de requisição do ACD .T. – Considera o Empenho .F. – Não Considera |
| **PRODUÇÃO** | **MV\_INFQEIN** | C | Indica se deve ser informada a quantidade ao iniciar uma operação nas rotinas de produção PCP MOD1 e PCP MOD2. 1=Sim 2=Não |
| **PRODUÇÃO** | **MV\_CBATUD4** | C | Indica se deve ser feito o empenho dos lotes ao iniciar a operação 01 de uma OP na rotina de Produção PCP MOD1 e PCP MOD2. 1=Sim 2=Não |
| **PRODUÇÃO** | **MV\_CBVQEOP** | C | Valida a quantidade iniciada com o saldo disponível da operação para o apontamento da produção e/ou apontamento de perda na rotina de produção PCP MOD1 e PCP MOD2. 1=Sim 2=Não |
| **PRODUÇÃO** | **MV\_REQAUT** | C | Conversão do empenho, realiza as requisições do estoque, quando: A=Automática, D=Digitada (manual). |
| **PRODUÇÃO** | **MV\_CBVLAPI** | C | Indica se deve validar a quantidade a ser apontada com a quantidade informada no inicio da operação. Rotina PCP MOD1 e PCP MOD2. 1=Sim 2=Não |
| **PRODUÇÃO** | **MV\_CBPE004** | L | Validação do Encerramento da OP - Mata250 |
| **PRODUÇÃO** | **MV\_CBPE011** | L | Valida o estorno do apontamento da produção - Mata680 |
| **PRODUÇÃO** | **MV\_CBPE014** | L | Faz validacao da exclusao PCP MOD 1 e MOD 2. |
| **PRODUÇÃO** | **MV\_CBPE015** | L | Faz validação da exclusão de Horas Improdutivas. |
| **PRODUÇÃO** | **MV\_CBPE017** | L | Faz Validação da exclusão da OP - Mata650. |
| **PRODUÇÃO** | **MV\_CBCALEN** | C | Parametro onde e informado o calendario padrao que deve ser utilizado |
| **PRODUÇÃO** | **MV\_CBPE018** | L | Habilita a impressão da etiqueta do produto(PA) no apontamento da produção e faz a baixa da requisicao do D4\_EMPROC. |
| **RECEBIMENTO** | **MV\_CONFFIS** | C | O parâmetro habilitado, S= Ativado, ativa no sistema a conferência física no recebimento de mercadorias. Podendo o usuário acompanhar o processo do recebimento em tempo real através de uma pasta que se encontra na visualização da Pré-Nota. Também não permite a classificação da Nota Fiscal antes da conferência da nota. S= Ativado ; N= Desativado |
| **RECEBIMENTO** | **MV\_IACD02** | C | O parâmetro deverá conter o Código do Local  de impressão utilizado no Pedido de Compra e/ou no Recebimento de Materiais para impressão das etiquetas de identificação dos produtos. Este código se refere à tabela CB5 do módulo ACD. |
| **RECEBIMENTO** | **MV\_IACD03** | C | O parâmetro deverá conter o Código do local de impressão utilizado no programa de Identificação de produto. Este código se refere à tabela CB5 do módulo ACD. |
| **RECEBIMENTO** | **MV\_IMPIP** | C | Informa como será impressa a etiqueta de identificação de Produto: 1 – No Pedido compras 2 – No Recebimento 3 – Não Imprime 4 – Na NFE (Nota Fiscal de Entrada) |
| **RECEBIMENTO** | **MV\_REGVOL** | C | Informa se o  volume de entrada deve ser registrado na rotina de recebimento, através da leitura da etiqueta de volume. 0 -  Não Registra , neste momento será solicitado a quantidade de volumes e o sistema ira imprimir as etiquetas de volume. 1 -  Registra, neste momento será solicita a leitura de uma etiqueta temporária para que seja habilitada na tabela CB0 |
| **RECEBIMENTO** | **MV\_SELVAR** | C | Permite ao usuário poder escolher a opção para digitar uma quantidade variável.  1 – Ativado: Exibe a opção para alterar a quantidade; 2 – Desativado: Não exibe a opção para alterar a quantidade. |
| **RECEBIMENTO** | **MV\_CBCQEND** | C | Endereço padrão para endereçamento automático dos produtos enviados para CQ através da rotina de recebimento Mod2.    OBS: Deve-se definir o código do armazém de CQ concatenado com o endereço de CQ. Exemplo: 98ENDCQ |
| **RECEBIMENTO** | **MV\_CBPAJIM** | C | Permite o ajuste dos impostos antes da geração da Nota Fiscal de Entrada através da rotina de recebimento Mod2 1-Sim; 2-Não |
| **RECEBIMENTO** | **MV\_CBVLPAJ** | N | Valor Maximo permitido no ajuste dos impostos antes da geração da Nota Fiscal de Entrada pela rotina de recebimento Mod2 |
| **RECEBIMENTO** | **MV\_CBPESO** | C | Verifica se deve informar o peso do produto no ato do recebimento através da rotina de receb. Mod2 1-Sim  2-Não |
| **RECEBIMENTO** | **MV\_CBSA5** | L | Permite a pesquisa do cód.barras na rotina de recebimento do ACD através da amarração Produto x Fornecedor (SA5). .T.  – Habilita a pesquisa .F. – Desabilita a pesquisa |
| **RECEBIMENTO** | **MV\_CBV2UM** | L | Permite a validação da 2.a Unidade de Medida na rotina de recebimento do ACD. .T.  – Permite a validação .F. – Não permite a validação |
| **RECEBIMENTO** | **MV\_CBPE002** | L | Atualiza CB0 na Exclusão da Pré-nota. |
| **RECEBIMENTO** | **MV\_CBPE009** | L | Realiza o endereçamento automático para o CQ na classificação da Nota. |
| **RECEBIMENTO** | **MV\_CBPE019** | L | Faz ajuste do CB0 apos a exclusão da Nota - Somente Protheus. |
| **RECEBIMENTO** | **MV\_TPCONFF** | C | Indica se a conferencia fisica sera realizada na  Pre-Nota ou na Nota Fiscal de Entrada. O valor    default (padrao) desse parametro sera Pre-Nota. |
| **RECEBIMENTO** | **MV\_IMPAUT** | C | Imprime etiqueta no Pedido de Compras / Aut. de Entrega quando se utiliza rotina automática 0- Nunca imprime, 1-Pergunta, 2- Sempre imprime |
| **RECEBIMENTO** | **MV\_CLACFDV** | C | Informe .T. para permitir classificar uma nota que  esteja com divergência na conferencia física ACD |
| **INVENTÁRIO** | **MV\_ANAINV** | C | Permite a analise do inventario pelo Coletor  (1-Sim,2-Nao) |
| **APLICATIVO** | [**MV\_MCDTPPR**](https://tdn.totvs.com/pages/releaseview.action?pageId=546686576) | C | Define quais os tipos de produto serão sincronizados no app Meu Coletor de Dados. As informações devem ser separadas por vírgula e sem espaços. |
| **APLICATIVO** | [**MV\_MCDPRSL**](https://tdn.totvs.com/pages/releaseview.action?pageId=546686576) | L | Define se somente produtos presentes na tabela SB2 (independente de ter saldo) serão sincronizados no App Meu Coletor de Dados |
