---
content_hash: eda2949b735bd3a82872fea7bc0cf58ac3e1d478ca55445037f21e8b72e4c710
fetched_at: '2026-06-29T00:12:02.231437+00:00'
page_id: '899198287'
product: rm
source: tdn-rm
title: Integração TOTVS Gestão Hospitalar x Backoffice Datasul
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=899198287
version: 11
---

## **01. VISÃO GERAL**

Este documento tem por objetivo reunir todas as informações relevantes sobre a Integração do TOTVS Gestão Hospitalar (RM Saúde) x BackOffice Datasul disponível a partir da 12.1.XX.

## **02. SISTEMAS ENVOLVIDOS**

## **03. INTEGRAÇÃO**

## **04. IPAAS**

## **05. ESCOPO**

## **06. PRÉ-REQUISITOS**

## **07. INTEGRAÇÃO PROTHEUS**

Esse documento não visa a descrição dos procedimentos de instalação do Protheus padrão e suas configurações. Neste documento serão apresentadas informações referentes ao EAI da Linha Protheus, que é o responsável pela comunicação com o TOTVS Gestão Hospitalar.

Cadastrar/Configurar Adapter para Integração no Protheus

Entre no configurador (SIGACFG), em Ambiente/Schedule/Adapter EAI, e preencha-o da seguinte forma:

| Msg Única | Rotina | Mensagem | Envia | Recebe | Método | Operação | Canal | Versão | Alias |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sim | AGRA045 | WAREHOUSE | Sim | Não | Síncrono | Todas | EAI | 1.000 | NNR |
| Sim | MATA020 | CUSTOMERVENDOR | Sim | Sim | Síncrono | Todas | EAI | 2.002 |  |
| Sim | MATA030 | CUSTOMERVENDOR | Sim | Sim | Síncrono | Todas | EAI | 2.002 |  |
| Sim | CTBA140 | CURRENCY | Sim | Não | Síncrono | Todas | EAI | 2.000 | CTO |
| Sim | MATA360 | PAYMENTCONDITION | Sim | Não | Síncrono | Todas | EAI | 2.000 | SE4 |
| Sim | MATA070 | BANK | Sim | Não | Síncrono | Todas | EAI | 2.000 | SA6 |
| Sim | CTBA030 | COSTCENTER | Sim | Não | Síncrono | Todas | EAI | 2.000 | CTT |
| Sim | MATA010 | ITEM | Sim/Não | Não/Sim | Síncrono | Todas | EAI | 2.001 | SB1 |
| Sim | QIEA030 | UNITOFMEASURE | Sim | Não | Síncrono | Todos | EAI | 2.000 | SAH |
| ~~Sim~~ | ~~MATA035~~ | ~~FAMILY~~ | ~~Sim/Não~~ | ~~Não/Sim~~ | ~~Síncrono~~ | ~~Todas~~ | ~~EAI~~ | ~~2.000~~ | ~~SBM~~ |
| Sim | MATA035 | STOCKGROUP | Sim | Não | Síncrono | Todas | EAI | 1.000 | SBM |
| Sim | FINA040 | ACCOUNTRECEIVABLEDOCUMENT | Não | Sim | Síncrono | Todas | EAI | 3.000 |  |
| Sim | FINA050 | ACCOUNTPAYABLEDOCUMENT | Não | Sim | Síncrono | Todas | EAI | 2.000 |  |
| Sim | FINA070 | ACCOUNTRECEIVABLEDOCUMENTDISCHARGE | Não | Sim | Síncrono | Atualização | EAI | 2.000 |  |
| Sim | FINA070 | REVERSALOFACCOUNTRECEIVABLEDOCUMENTDISCHARGE | Não | Sim | Síncrono | Exclusão | EAI | 2.000 |  |
| Sim | MATA103B | INVOICE (Doc de entrada) | Sim | Não | Síncrono | Todas | EAI | 3.001 |  |
| Sim | MATA521 | INVOICE (Exclusão de doc de saída) | Sim | Não | Síncrono | Todas | EAI | 3.009 |  |
| Sim | MATA461 | INVOICE (Doc de Saída) | Sim | Não | Síncrono | Todas | EAI | 3.009 |  |
| Sim | MATA225 | STOCKLEVEL | Não | Sim | Síncrono | Todas | EAI | 1.000 |  |
| Sim | MATA241 | STOCKTURNOVER | Sim | Sim | Síncrono | Todas | EAI | 1.003 |  |
| Sim | MATA261 | TRANSFERWAREHOUSE | Sim | Sim | Síncrono | Todas | EAI | 1.001 |  |
| Sim | MATA340 | INVENTORY | Sim | Não | Síncrono | Todas | EAI | 1.000 |  |
| Sim | MATA410 | ORDER | Não | Sim | Síncrono | Todas | EAI | 3.002 |  |
| Sim | FINA010 | FINANCIALNATURE | Sim | Não | Síncrono | Todas | EAI | 2.000 | SED |

O conteúdo da coluna Alias só deve ser preenchida se o cadastro for compartilhado no Protheus. No caso de cadastro compartilhado, é necessário que o adapter Family seja configurado para enviar do Protheus e não receber. Neste caso, a fórmula visual do grupo de estoque deve ser desabilitada.

## 

## **08. INTEGRACAO RM**

## Transações/Entidades/Mensagens únicas

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Método** | **ID** | | | **Descrição** | | **Origem** | **Destino** |
| **Cadastros** | | 01 | Local de estoque | | Protheus | | RM |
| 02 | Cliente-Fornecedor | | Protheus | | RM |
| 03 | Grupo de Estoque | | RM | | Protheus |
| 04 | Moeda | | Protheus | | RM |
| 05 | Condição de pagamento | | Protheus | | RM |
| 06 | Banco | | Protheus | | RM |
| 07 | Centro de Custo | | Protheus | | RM |
| 08 | Produto | | RM | | Protheus |
| 09 | Unidade de Medida | | Protheus | | RM |
| 10 | Coligada\*  \* Integrado manualmente, incluindo na tabela de de/para em ambos os sistemas | |  | |  |
| 11 | Filial\*  \* Integrado manualmente, incluindo na tabela de de/para em ambos os sistemas | |  | |  |
| 12 | Prestadores | | RM | | Protheus |
| 13 | Convênios | | RM | | Protheus |
| **Processos** | | 14 | Título a receber | | RM | | Protheus |
| 15 | Título a pagar | | RM | | Protheus |
| 16 | Baixa de títulos | | RM | | Protheus |
| 17 | Cancelamento de baixa | | RM | | Protheus |
| 18 | Nota fiscal de entrada | | Protheus | | RM |
| 19 | Saldo | | RM | | Protheus |
| 20 | Movimentação de estoque | | RM/ Protheus | | Protheus/ RM |
| 21 | Transferências | | RM/ Protheus | | Protheus/ RM |
| 22 | Inventário | | Protheus | | RM |
| 23 | Pedido de venda | | RM | | Protheus |

## Fluxo das Informações

O fluxo básico desta integração está em definir a origem da informação, enviar para o EAI da linha do produto e este se comunica com o EAI da outra linha. Ambos os produtos possuirão as mesmas informações, porém podem possuir códigos diferentes. Cada sistema possui uma tabela de de-para onde são armazenados os códigos de origem e os códigos de destino e a entidade correspondente. Com isso, cada sistema envia o seu código e o outro sistema faz a troca assim que receber a mensagem. Abaixo serão detalhados cada entidade envolvida nesta integração.

## Cadastros

Os cadastros são a base da integração entre os sistemas. Foi definido o sistema de origem para cada cadastro, portanto qualquer alteração nesta origem pode impactar na integração padrão. A alteração de sistema de origem impacta na configuração da mensagem utilizada em ambos os sistemas e pode envolver algum tipo de desenvolvimento, seja uma fórmula visual, um complemento na mensagem na parte de envio ou recebimento da mensagem, no caso da linha RM.

## Empresa / Filial

É o primeiro cadastro que deve ser realizado nesta integração. No RM esta entidade é um cadastro comum. Mas no Protheus a Empresa é definida no Arquivo Sigamat.emp que fica no System do ambiente do Protheus e não faz parte de uma tabela de banco de dados. Este é o arquivo que permite à empresa utilizar o sistema. Isto faz parte da implantação do Protheus padrão.

Este cadastro deverá ser feito manualmente no Protheus e no RM, e depois configurar o “de/para” de integração correspondente (RM e Protheus possuem interfaces específicas para este fim). Neste caso, não será utilizada nenhuma mensagem para o sincronismo deste cadastro.

O cadastro de filial também deve ser feito manualmente na tabela de “de-para” de integração.

|  |  |  |  |
| --- | --- | --- | --- |
| De-para RM (Empresa) | | De-Para Protheus (Empresa)/(FILIAL) | |
| Tabela RM | GCOLIGADA | **Referência** | RM |
| Chave Primária RM | CODCOLIGADA | **Company** | <Valor da Empresa RM> |
| Valor Chave Primária RM | <Valor CODCOLIGADA> | **Branch** | <Valor da Coligada RM> |
| Sistema Integrado | PROTHEUS | **Emp. Protheus** | <Empresa do Protheus> |
| Valor Chave Integração | < Valor recebido pelo InternalId > | **Fil.Protheus** | <Filial do Protheus> |

---

# **DOCUMENTO BASE DA INTEGRAÇÃO RM SAÚDE X PROTHEUS**

Importante

A integração do RM com o Protheus é realizada somente através do EAI 1.0. A versão EAI 2.0 ainda não é suportada no TOTVS Gestão Hospitalar.

Para ativar a integração é necessário a execução de Scripts na base RM. Esses Scripts estão em constante atualização/correção, com isso, a cada nova implantação solicitar os scripts mais atuais para suporte do RM Saúde, nunca reaproveitar scripts de outras implantações.

## **01. VISÃO GERAL**

Este documento tem por objetivo reunir todas as informações relevantes sobre a Integração do TOTVS Gestão Hospitalar (RM Saúde) x BackOffice Protheus disponível a partir da 12.1.6.

## **02. SISTEMAS ENVOLVIDOS**

**Sistema Envolvidos**

Descrição dos sistemas envolvidos no contexto de negócio (e que serão envolvidos na integração).

* CorporeRM através dos seguintes módulos:

+ **RM Saúde (TOTVS Gestão Hospitalar)**: realiza a gestão hospitalar da empresa, desde o registro do paciente, passando pela assistência, gerando o faturamento, baseado nos diversos padrões do mercado como TISS, SUS, ABRAMGE, IPASGO, IPERGS, IPSEMG e etc.
+ **Estoque (RM Nucleus):** utilizado para o cadastro de produtos, locais de estoque, unidades de medida, condições de pagamento. Trata-se do intermediador da integração, uma vez que a integração entre o Hospitalar e ele já é nativa.

* Microsiga Protheus através dos seguintes módulos:

+ **Compras (SIGACOM):** Oferece à equipe de compras de uma empresa, condições de acompanhar e controlar as carteiras de compras, cotações, pedidos de compras e o recebimento de materiais, permitindo a reposição dos estoques em tempo hábil e apresentando informações indispensáveis a uma boa negociação com seus fornecedores.
+ **Faturamento (SIGAFAT):** Pode ser definido como a receita bruta decorrente da venda de mercadorias, de mercadorias e serviços e de serviços de qualquer natureza.
+ **Estoque e Custos (SIGAEST**): Controle de materiais movimentados e armazenados da empresa, além do custo incorrido sobre este material.

## **03. INTEGRAÇÃO**

A integração entre os sistemas foi motivada pelo uso prévio do Protheus pela instituição ou pela escolha do uso de BackOffice da linha Microsiga e do Hospitalar da linha RM. O TOTVS Gestão Hospitalar já é integrado nativamente com o BackOffice RM e com este cenário surgiu a necessidade de integração com o BackOffice Protheus.

O **TOTVS Gestão Hospitalar** é responsável pela gestão de saúde e o Protheus pela gestão de estoque, financeira e contábil.

Esta integração visa unir os dois sistemas para minimizar o trabalho de cadastrar as entidades comuns em ambos os sistemas e permitir que cada um trate exclusivamente do seu negócio.

* Premissas.
  + Esta solução deve primar pela simplicidade e facilidade de uso, facilidade de manutenção e facilidade de atualização.
  + Deve respeitar os sistemas operacionais utilizados pelas soluções *software* das marcas: WINDOWS.
  + Utilizar o Protheus versão 11.7 (e patchs específicos para esta integração) e o RM versão 11.82 (último patch disponível). Observação: Ambos utilizam o modelo de licenciamento TOTVS padrão (Licence Server).
  + Bancos de dados homologados: SQL Server 2005 ou 2008 e Oracle 10g ou 11g.
  + Se o cliente já possui base de dados implantada do RM ou do Protheus será responsabilidade da equipe de implantação efetuar a carga inicial e/ou sincronismo dos cadastros. A integração irá efetuar o sincronismo automático de novos registros ou alterações posteriores à ativação da integração.
  + Por padrão, todos os cadastros mantidos pelo Backoffice Protheus deverão ser desabilitados (manualmente) no controle de segurança do RM. Exceções serão destacadas ao longo do documento.
* Arquitetura (Tecnologia).
  + Integração de processos síncronos através de WebServices (EAI).

Comunicação direta do EAI RM x EAI Protheus, via WebServices. Mensagens Assíncronas e Síncronas.

Utilização do Monitor da Fila de Integração para gravar todas as mensagens enviadas/recebidas para efeito de registro e, no caso de mensagem assíncrona, permitindo reprocessar.

## **04. MODELO DE MENSAGEM ÚNICA TOTVS (TOTVSMESSAGE)**

Durante o processo de consolidação de marcas, iniciado pela TOTVS, várias empresas diferentes foram adquiridas e com elas vários produtos passaram a compor o portfólio de ofertas disponível aos clientes. Esta expansão de ofertas permitiu que clientes de uma marca, antes limitados pelas opções com aquela “etiqueta”, pudessem agora compor o seu ambiente de TI utilizando produtos de origens diferentes (Exemplo: BackOffice Protheus + TIN).

Esta mesma iniciativa já era uma prática comum nos clientes, porém todo o custo envolvido na integração entre estes aplicativos era visto pelo cliente como parte da escolha de utilizar-se de produtos de diferentes fornecedores. Uma vez que estes produtos passam a fazer parte de uma mesma oferta, os clientes TOTVS passam a demandar que estes produtos sejam naturalmente integrados. Isto significa que se antes o cliente arcava com o custo e o risco envolvido em uma integração (como corrupção da base de dados, por exemplo), ele agora entende que a TOTVS deve prover soluções já integradas, independente da origem dos produtos oferecidos.

Com o objetivo de padronizar as integrações com os produtos TOTVS, foi definida uma nova diretriz para os projetos de integração: A de que todos os produtos TOTVS devam trabalhar com uma mensagem XML únicos evitando, desta forma, o processo de transformação de mensagens. Neste cenário, teríamos o seguinte quadro:

Neste cenário, qualquer produto TOTVS trabalhará com o mesmo XML para uma mesma entidade, vamos supor que tenhamos um XML correspondente à mensagem de CLIENTES, ela poderá ser enviada para qualquer um dos produtos que suporte o recebimento desta entidade.  
Uma vez que os vários produtos TOTVS terão um "idioma" comum (o XML Único), as integrações entre estes produtos não exigirão mais que as mensagens sejam transformadas de um formato para outro. Com isto, será possível conectar diretamente dois produtos, sem a necessidade do TOTVS ESB, como no diagrama abaixo:

Além de questões referentes ao formato das mensagens, a mensagem única também torna uniforme o tratamento destas mensagens XML pelos aplicativos, principalmente no que diz respeito à capacidade de rastreamento.

## **05. ESCOPO**

A Gestão Hospitalar será feita exclusivamente no TOTVS Gestão Hospitalar (cadastro dos prestadores, convênios, tabelas de preço de MATMED, produto, grupo de estoque, etc.).

O controle de estoques, compras, faturamento, financeiro, contábil e fiscal serão feitos no Protheus (módulos integrados: SIGACOM, SIGAFAT e SIGAEST). Os cadastros básicos, bem como os cadastros de Cliente e Fornecedor, Centro de Custo, Condição de Pagamento, Unidade de Medida, Moeda serão realizados sempre no Protheus e sincronizados para o RM.

## **06. PRÉ-REQUISITOS**

A integração respeita todos os pré-requisitos definidos pelas linhas de produto TOTVS envolvidos. Para mais detalhes sobre configuração de hardware recomendada, sistema operacional, bancos de dados suportados e demais dados, consulte os seguintes documentos no TDN:

* Documento TOTVS Application Server - 29289 da Linha Protheus: <http://tdn.totvs.com.br/display/tec/Application+Server>
* Documento de Portabilidade da Linha RM: <http://tdn.totvs.com/display/rm/Portabilidade>

Os produtos envolvidos utilizam o modelo de licenciamento padrão (License Server). Para pleno funcionamento, as licenças (Hard Lock) devem ser providenciadas junto a TOTVS com antecedência. Vale ressaltar que esta integração está de acordo com as boas práticas recomendadas pelo Comitê de Integração TOTVS e utiliza a arquitetura Mensagem Única e comunicação via WebServices.

### **Versão mínima Protheus**

Utilizar a versão 11.7 (ou superior).

Os WebServices exigem uma licença específica “TOTVS I”.

### **Versão mínima RM**

Utilizar a versão 11.82.36 (específica).

A TOTVS disponibiliza um backup da base de dados RM “vazia” que pode ser utilizada para novos clientes. Para clientes que já possuem versão anterior utilizar o Conversor RM para atualizar o banco de dados para a versão 11.82.

## **07. INTEGRAÇÃO PROTHEUS**

Esse documento não visa a descrição dos procedimentos de instalação do Protheus padrão e suas configurações. Neste documento serão apresentadas informações referentes ao EAI da Linha Protheus, que é o responsável pela comunicação com o TOTVS Gestão Hospitalar.

Cadastrar/Configurar Adapter para Integração no Protheus

Entre no configurador (SIGACFG), em Ambiente/Schedule/Adapter EAI, e preencha-o da seguinte forma:

| Msg Única | Rotina | Mensagem | Envia | Recebe | Método | Operação | Canal | Versão | Alias |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sim | AGRA045 | WAREHOUSE | Sim | Não | Síncrono | Todas | EAI | 1.000 | NNR |
| Sim | MATA020 | CUSTOMERVENDOR | Sim | Sim | Síncrono | Todas | EAI | 2.002 |  |
| Sim | MATA030 | CUSTOMERVENDOR | Sim | Sim | Síncrono | Todas | EAI | 2.002 |  |
| Sim | CTBA140 | CURRENCY | Sim | Não | Síncrono | Todas | EAI | 2.000 | CTO |
| Sim | MATA360 | PAYMENTCONDITION | Sim | Não | Síncrono | Todas | EAI | 2.000 | SE4 |
| Sim | MATA070 | BANK | Sim | Não | Síncrono | Todas | EAI | 2.000 | SA6 |
| Sim | CTBA030 | COSTCENTER | Sim | Não | Síncrono | Todas | EAI | 2.000 | CTT |
| Sim | MATA010 | ITEM | Sim/Não | Não/Sim | Síncrono | Todas | EAI | 2.001 | SB1 |
| Sim | QIEA030 | UNITOFMEASURE | Sim | Não | Síncrono | Todos | EAI | 2.000 | SAH |
| ~~Sim~~ | ~~MATA035~~ | ~~FAMILY~~ | ~~Sim/Não~~ | ~~Não/Sim~~ | ~~Síncrono~~ | ~~Todas~~ | ~~EAI~~ | ~~2.000~~ | ~~SBM~~ |
| Sim | MATA035 | STOCKGROUP | Sim | Não | Síncrono | Todas | EAI | 1.000 | SBM |
| Sim | FINA040 | ACCOUNTRECEIVABLEDOCUMENT | Não | Sim | Síncrono | Todas | EAI | 3.000 |  |
| Sim | FINA050 | ACCOUNTPAYABLEDOCUMENT | Não | Sim | Síncrono | Todas | EAI | 2.000 |  |
| Sim | FINA070 | ACCOUNTRECEIVABLEDOCUMENTDISCHARGE | Não | Sim | Síncrono | Atualização | EAI | 2.000 |  |
| Sim | FINA070 | REVERSALOFACCOUNTRECEIVABLEDOCUMENTDISCHARGE | Não | Sim | Síncrono | Exclusão | EAI | 2.000 |  |
| Sim | MATA103B | INVOICE (Doc de entrada) | Sim | Não | Síncrono | Todas | EAI | 3.001 |  |
| Sim | MATA521 | INVOICE (Exclusão de doc de saída) | Sim | Não | Síncrono | Todas | EAI | 3.009 |  |
| Sim | MATA461 | INVOICE (Doc de Saída) | Sim | Não | Síncrono | Todas | EAI | 3.009 |  |
| Sim | MATA225 | STOCKLEVEL | Não | Sim | Síncrono | Todas | EAI | 1.000 |  |
| Sim | MATA241 | STOCKTURNOVER | Sim | Sim | Síncrono | Todas | EAI | 1.003 |  |
| Sim | MATA261 | TRANSFERWAREHOUSE | Sim | Sim | Síncrono | Todas | EAI | 1.001 |  |
| Sim | MATA340 | INVENTORY | Sim | Não | Síncrono | Todas | EAI | 1.000 |  |
| Sim | MATA410 | ORDER | Não | Sim | Síncrono | Todas | EAI | 3.002 |  |
| Sim | FINA010 | FINANCIALNATURE | Sim | Não | Síncrono | Todas | EAI | 2.000 | SED |

O conteúdo da coluna Alias só deve ser preenchida se o cadastro for compartilhado no Protheus. No caso de cadastro compartilhado, é necessário que o adapter Family seja configurado para enviar do Protheus e não receber. Neste caso, a fórmula visual do grupo de estoque deve ser desabilitada.

### Configurar o EAI para Integração no Protheus

No Protheus, acesse no configurador **SIGACFG / Ambiente / Schedule / Schedule.**

### Cadastrar Agent

1. Clique no sinal de +(Soma) ao lado esquerdo do Globo Verde com o título **Agent,** para abrir as opções Cadastro e Monitor.
2. Clique na opção Cadastro.
3. Após isso clique no Globo Verde com sinal de +(Soma) que está à direita da tela, as informações da tela de detalhes serão preenchidas automaticamente.

### Cadastrar Agendamento

1. Clique no sinal de +(Soma) ao lado esquerdo do Globo Verde com o título Agendamento, para abrir as opções Cadastro e Monitor.
2. Clique na opção **Cadastro**, na tela de detalhes na parte inferior da tela principal.
3. Clique no primeiro ícone de um caderno com sinal de +(soma). Algumas informações aparecerão automaticamente.
4. Complete o preenchimento apenas em **Rotina**, com FWEAI e com Empresa/Filial clicando na Lupa ao lado direito do campo.
5. Será exibida a tela apresentando as empresas cadastradas.
6. Selecione a empresa que fará integração, clique duas vezes no Check-box ao lado esquerdo do Nome da empresa até ficar marcado com um (x).
7. Após isso, clique no botão OK.
8. Clique no botão Recorrência (Duas setas circulares).
9. Na nova janela selecione **Sempre Ativo** nas opções de Padrão de Recorrência para que o job do EAI fique sempre escutando a fila de mensagens únicas.
10. Para finalizar clique no (V) de cor verde Botão Confirmar.

### EAI – Como visualizar os arquivos XML criados pelas rotinas

São apresentadas duas telas sendo a de **Transações** na parte superior e a tela de **Eventos da Tarefa** na parte inferior.

1. Na tela de transações são exibidas as mensagens que foram geradas.
2. Para visualizar o arquivo XML criado pela mensagem, clique na linha da mensagem e em seguida clique na Lupa azul que se encontra na parte superior da tela, será aberto o arquivo XML no browser do Internet Explorer.
3. Ao clicar na linha da Mensagem, na tela de Eventos da Tarefa podem ser exibidas as seguintes informações de acordo com o status da mensagem:
   1. Início de Processamento.
   2. Falhas.
   3. Processo Interrompido.
   4. Fim de Processamento.

 Nota: Para identificar a Cor da Legenda com o tipo de mensagem, clique duas vezes na bolinha colorida que será exibida a tela de legenda com a identificação do tipo com a Cor.

### Limpar Histórico de Mensagens

Opção Limpeza de Tabelas: Caso queira realizar uma limpeza dos históricos das mensagens.

Ao clicar nesta opção, será exibida uma tela denominada **Tabelas,**  uma frase com a descrição “**Selecione a Tabela”** e uma seta preta apontando para baixo do lado direito da frase. Clique nesta seta para abrir as opões: Tarefas ou EAI.

1. Clique em EAI, e marque um tipo de mensagem que deseja limpar do histórico, são elas:  
   * Aguardando Execução.
   * Executando.
   * Finalizada.
   * Falhou.
   * Bloqueado.
2. Para identificar a Cor da Legenda com o tipo de mensagem, clicar duas vezes na bolinha colorida, será exibida a tela de legenda e a  identificação de cores correspondente ao status.
3. Para executar todas as opções, não selecione nenhuma e clique no botão Executar. Será exibida a tela com todas as mensagens para serem excluídas.
4. Para finalizar clique no Ícone de um Caderno com um (x) vermelho que está no lado direito superior da tela. Será exibida uma tela de confirmação com a mensagem **Confirma deleção?**.
5. Clicar no botão Sim para excluir todos históricos ou no botão Não para manter os históricos.

### Configurar Parâmetros da Integração

1. Acesse o configurador (SIGACFG) , em Ambiente/Cadastros/Parâmetros:

* + **MV\_EAIURL2=** Endereço WebService que Receberá os Dados Enviados (Exemplo: <http://ip_do_servidor/TOTVSBusinessConnect/wsEAIService.asmx?wsdl>).
  + **MV\_EAIWS=** Informe o nome do Client WebService do EAI para envio a outro EAI. (WSEAISERVICE).
  + **MV\_EAIUSER=** <Nome de usuário>.
  + **MV\_EAIPASS=** <Senha de usuário>.
  + **MV\_EAIMETH=** Informe o método de envio do EAI para envio a outro EAI. (RECEIVEMESSAGE).

2. No Configurador, acesse **Ambiente/Schedule/Emp fil. Msg Única** e configure o de-para de Coligada e Filial.

## **08. INTEGRACAO RM**

Serão destacadas as informações referentes ao TOTVS Business Connect (TBC) que é a ferramenta EAI da Linha RM, responsável pela comunicação com o BackOffice Protheus.

Para demais esclarecimentos sobre demais produtos da Linha RM, consulte a documentação disponível no endereço:[*tdn.totvs.com*](http://www.tdn.totvs.com/display/public/rm/Home)

### Pré-requisitos

Nesta versão os WebServices de Integração da linha RM devem ser hospedados no Microsoft IIS. Além disto a Biblioteca RM necessita da Microsoft .NET Framework. Assim, os pré-requisitos de instalação para o EAI RM são os seguintes:

* Microsoft .NET Framework 4.0
* Internet Information Services (IIS)

### Instalar os WebServices de Integração (TBC)

Execute o instalador “TOTVS Business Connect – [versão].msi” e patchs disponíveis, se existirem. Este pacote cria uma aplicação no IIS e copia os arquivos necessários para a utilização dos WS. Os WS serão instalados na porta 80 (como é a porta padrão pode ser omitida na url). E o alias de banco de dados padrão será CORPORERM.

O administrador do sistema poderá alterar esta e demais configurações, se necessário, editando o arquivo Web.config que se encontra no diretório de instalação RM na pasta WS\_TBC.

### Instalar a Biblioteca RM

Execute o instalador “BibliotecaRM – [versão].msi” e patchs disponíveis, se houver. Este pacote contém o client “RM.exe” e demais arquivos necessários para funcionamento de todos os módulos da linha RM. A instalação pode ser feita em 3 camadas ou local.

## Configurar a Integração

1. Execute o configurador conforme imagem abaixo para a criação de campos e conjunto de mensagens de integração.
2. Selecione o sistema Integração, em **Ferramentas, opção Configurar**.
   1. Após execução, inative esta integração.
3. Informe o usuário e senha do banco e clique em **Testar Conexão** para habilitar o botão **Avançar.**
4. Selecione a Integração **TOTVS Manutenção de ativos X BackOffice RM**, clique em **Avançar** e depois em **Executar.**
5. Acesse o Menu Integração / Mensagem Única / Integrações. Edite o registro de identificador = 1001 e desmarque o campo **Ativo?**

**Importante**: Execute os scripts somente após ter definido os cadastros de coligada e filial. Após isso, pare o serviço do RM.Host.Service para que as alterações no banco sejam refletidas na aplicação.

1. Execute o script para configurar a integração com o TOTVS Gestão Hospitalar. Este script faz a configuração da integração, incluindo todas as mensagens utilizadas, tipos de movimento, máscaras, etc.
2. Execute o script IntegracaoRMSaude\_Protheus\_01.sql. O script já define algumas máscaras defaults para os códigos de cliente/fornecedor, produto, família de materiais, local de estoque. Defina a máscara para que seja compatível com os códigos no Protheus.
3. No script IntegracaoRMSaude\_Protheus\_02.sql.É necessário informar a coligada que será utilizada no cliente.
4. Inicie o serviço RM.Host.Service

Oracle:  SQL Server:

## Requisitos Básicos da integração

* Máscara do código do cliente/fornecedor deve ser compatível com a máscara no Protheus
* Utilizar CPF Único
* Utilizar CNPJ Único
* Máscara do código do produto deve ser igual ao do Protheus
* Habilitar a TB1 para manutenção de Família de Materiais.
* Máscara do local de estoque deve ser compatível
* Máscara do centro de custo deve ser compatível
* Para a utilização de cadastros compartilhados, deve-se ter a mesma configuração em todas as coligadas dos seguintes itens:
  + Produto global
  + Cliente/fornecedor global

## Parametrizar a integração

1. Acesse RM.exe / Segmento Integrações / Aba Integração / Mensagem Única / Integrações. Esta interface permite incluir ou alterar um pacote de integração.
2. Selecione TOTVS Gestão Hospitalar x BackOffice Protheus (**Identificador = 1011**) e clique em editar para alterar as configurações iniciais.

## Primeira parte – Identificação

1. **Nome Integração:** Este é um campo meramente informativo, recomendamos uma descrição curta, mas clara, para este pacote de integração. Por padrão este nome já vem preenchido como: TOTVS Gestão Hospitalar x BackOffice Protheus.
2. **Nome Reduzido:** Também é um campo apenas informativo, insira um bem curto. Por padrão vem preenchido como: THPROT.
3. **Sistema Integrado:** Informe PROTHEUS. Este é um mnemônico que identifica a aplicação de origem e será enviado no atributo "name" da tag <Product> no XML trafegado.
4. **URL WebService:** Informe o endereço do WebService Protheus para envio de mensagens. Utilize o formato http://\[servidor\]:\[porta\]/EAIService.apw . Para verificar se o WS Protheus está disponível digite o endereço do mesmo no seu navegador (no formato http://\[servidor\]:\[porta\]), na página apresentada procure pelo texto EAISERVICE).
5. **Usuário Autenticação:** Informe o nome do usuário para autenticação pelo WebService Protheus.
6. **Senha Autenticação:** Informe a senha para autenticação pelo WebService Protheus.

## Segunda parte – (Anexo) Mapeamento de Entidades

É possível realizar um mapeamento de cada entidade (cada mensagem única) que faz parte do pacote de integração.   
O script de Configuração irá fazer o mapeamento padrão automaticamente. Alterações só devem ser feitas com critério. Caso seja necessário acrescentar uma entidade à integração que não esteja no pacote padrão, clique em Anexos e escolha "Mapeamento de Entidades". Na tela que é apresentada informe o código ou nome da mensagem. Clique no botão reticências (...) para localizar a mensagem na lista de mensagens pré-cadastradas.

## Terceira parte – (Anexo) Parâmetros

Aqui estão disponíveis os parâmetros utilizados na integração. Este parâmetro já vem preenchidos pelo script de inicialização. Os parâmetros de tipo de movimento não devem ser alterados. Já os parâmetros TIPOSAIDAPEDIDOVENDA, TIPODOCMOVFATURA, TIPODOCFOLHAPAGTO, SERIEDOCMOVFATURA e SERIEDOCFOLHAPAGTO devem ser alterados para os valores de cada cliente.

* TMVTRANSF: tipo de movimento do Nucleus utilizado nas movimentações de transferência
* TMVENTRADANF: tipo de movimento do Nucleus utilizado nas movimentações de entrada de nota fiscal que afeta estoque
* TMVENTRADANFNAOBAIXA**:**tipo de movimento de ENTRADA de nota que NÃO afeta estoque
* TMVENTRADANFCONSIGNADO: tipo de movimento de ENTRADA de CONSIGNADO de nota que afeta estoque
* TMVENTRADANFCONSIGNADONAOBAIXA: tipo de movimento de ENTRADA de CONSIGNADO de nota que NÃO afeta estoque
* TMVDEVOLUCAONF: tipo de movimento de  DEVOLUÇÃO  de nota que afeta estoque
* TMVDEVOLUCAONFNAOBAIXA: tipo de movimento de  DEVOLUÇÃO  de nota que NÃO afeta estoque
* TMVDEVOLUCAONFCONSIGNADO: tipo de movimento de DEVOLUÇÃO de CONSIGNADO de nota que afeta estoque
* TMVDEVOLUCAONFCONSIGNADONBAIXA: tipo de movimento de  DEVOLUÇÃO  de CONSIGNADO de nota que NÃO afeta estoque
* TMVDEVOLUCAOCC: tipo de movimento do Nucleus utilizado nas movimentações de devolução para centro de custo
* TMVDEVOLUCAO: tipo de movimento do Nucleus utilizado nas movimentações de devolução
* TMVBAIXA: tipo de movimento do Nucleus utilizado nas movimentações de baixa de estoque. Requisições para paciente, prescrição
* TMVENTRADAAJUSTE: utilizado para incrementar o saldo no inventário
* TIPOSAIDAPEDIDOVENDA: código do tipo de saída do Protheus para emissão de pedidos de venda
* TIPODOCMOVFATURA: tipo de documento do Protheus utilizado para o envio de título a receber, relacionado ao movimento de fatura
* TIPODOCFOLHAPAGTO: tipo de documento do Protheus utilizado para o envio de título a receber relacionado ao movimento de folha de pagamento
* SERIEDOCMOVFATURA: série utilizada para enviar o título a receber para o Protheus
* SERIEDOCFOLHAPAGTO: série utilizada para enviar o título a pagar para o Protheus
* CODCLASSIFICPAIS: utilizado como código do país

## Configuração de-para de Coligada e Filial

1. Acesse RM.exe / Segmento Integrações / Aba Integração / Mensagem Única / De-Para.
2. Inclua o registro de correspondência entre os códigos das empresas do Protheus com as coligadas do RM conforme imagem.
3. Faça o mesmo procedimento para as filiais. Deve-se atentar como o Protheus envia o valor da tag BranchId no cabeçalho da mensagem, pois o EAI RM irá concatenar as tags CompanyId com a BranchId separadas pelo caracter |
4. Assim no cadastro de filial ficaria 01|01 à CompanyId|BranchId, para o caso de não utilizar o conceito de gestão de grupo de empresas. Para o uso de gestão de grupo de empresas, o cadastro de de-para ficaria: 03|0101, onde 03 seria o grupo de empresa, o primeiro 01 seria o código da empresa e o segundo 01 seria o código da filial, sendo que 0101 é o código completo da filial.
5. Para o caso de utilizar o compartilhamento de cadastros do Protheus, é necessário configurar no cadastro das coligadas, o código do grupo da empresa a que pertencem as coligadas. Este código é utilizado para a réplica dos cadastros dentro do mesmo grupo.

## Fórmulas Visuais

Realize a importação das fórmulas visuais necessárias para a integração de convênios, prestadores, produtos e grupos de estoque.

1. Acesse o RM.exe / Segmento Saúde / Gestão Hospitalar / Gestão / Fórmula Visual.
2. Em Categoria, crie a categoria 'Integração Protheus'.
3. Na página Perfil da Categoria de Fórmula Visual inclua os perfis que terão acesso a está categoria.
4. Inclua o perfil do usuário que fará a importação das fórmulas.
5. Após isso acesse o RM.exe / Segmento Saúde / Gestão Hospitalar / Gestão / Fórmula Visual.
6. Em Fórmula visual execute o processo Importação de Fórmula visual.
7. Clique em Adicionar Objetos.
8. Selecione o arquivo IntegracaoProtheus.TotvsWF**.**
9. Na página Seleção de Coligadas, deixa a Coligada Atual.
10. Para cada fórmula e necessário informar na página Parâmetros a categoria cadastrada anteriormente e marcar a opção Importar Gatilho.

## No RMSaude.exe

1. Acesse o menu Opções/Parâmetros/Parâmetros de integração.
2. Para cada tipo de movimento cadastrado no RM Saúde, informe a TES relacionada do Protheus. Se não for informado nenhum valor, a integração assumirá um valor default definido num parâmetro dentro do Protheus.
3. A filial de integração é necessária para enviar para qual filial o cliente/fornecedor pertence.
4. A quantidade de dias é utilizada para o cálculo de vencimento do pagamento a prestadores.
5. A forma de baixa é necessária para informar o tipo de baixa que será feita durante a integração de recebimento de valores das faturas.

## Definição de Integração em Sistemas da linha RM

1. No RM.exe, acesse Ambiente / Parâmetros / Integrações de Sistemas.
2. Localize o registro abaixo e marque o campo Integrado. Isso fará com que alguns cadastros compartilhados sejam acessíveis no RM Saúde.

## EAI – Fila de Mensagens Únicas

1. Acesse **RM.exe / Segmento Integrações / Aba Integração / Mensagem Única / Fila de mensagens únicas**.
2. Nesta tela serão registradas as informações de envio e recebimento de mensagens XML trafegadas pela integração.
3. Para ver mais detalhes da mensagem trafegada de um duplo clique no registro, para detalhes de execução (erro ou sucesso) selecione o registro e clique em Anexos / Informações de execução de mensagem, neste anexo é possível visualizar a mensagem de resposta.

Dados da mensagem trocada entre o RM e o Protheus:

Detalhes da execução da mensagem. O campo Mensagem transformada corresponde ao xml que foi enviado para o outro EAI e o campo Mensagem de resposta corresponde ao xml que o outro EAI retornou mediante ao xml recebido:

## Controle de Versão

O grupo TOTVS representado por suas marcas irá administrar as demandas de evolução dos layouts e demais ajustes, acordando junto aos solicitantes o prazo de liberação de release.

Todas as evoluções programadas deverão ser discutidas e aprovadas pelas marcas antes do início do desenvolvimento e somente serão desenvolvidas em caso de concordância das marcas e alinhamento com as diretivas definidas pelo Comitê de Integração TOTVS.

## Suporte

O suporte aos recursos da Integração será de responsabilidade de todas as linhas, sendo assim as equipes de suporte dos produtos TOTVS Gestão Hospitalar (RM Saúde) e *Backoffice* Protheus estarão aptas a fazer a primeira análise e, quando necessário, repassar para a equipe mais adequada em cada caso.

Nota: a versão atualizada deste fluxo pode ser consultada no TDN (TOTVS Developer Network), acesse o caminho [http://tdn.totvs.com](http://tdn.totvs.com/), faça o login e acesse Qualidade de Software Corporativa / Metodologia de Desenvolvimento de Produtos TOTVS / Processo de Sustentação / Subprocesso de Suporte Técnico / Fluxo de Integração de Produtos.

## Transações/Entidades/Mensagens únicas

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Método** | **ID** | | | **Descrição** | | **Origem** | **Destino** | **XSD (versões podem variar)** |  |
| **Cadastros** | | 01 | Local de estoque | | Protheus | | RM | Warehouse\_1\_000.xsd | |
| 02 | Cliente-Fornecedor | | Protheus | | RM | CustomerVendor\_2\_002.xsd | |
| 03 | Grupo de Estoque | | RM | | Protheus | Family\_2\_000.xsd | |
| 04 | Moeda | | Protheus | | RM | Currency\_2\_000.xsd | |
| 05 | Condição de pagamento | | Protheus | | RM | PaymentCondition\_2\_000.xsd | |
| 06 | Banco | | Protheus | | RM | Bank\_2\_000.xsd | |
| 07 | Centro de Custo | | Protheus | | RM | CostCenter\_2\_000.xsd | |
| 08 | Produto | | RM | | Protheus | Item\_2\_001.xsd | |
| 09 | Unidade de Medida | | Protheus | | RM | UnitOfMeasure\_2\_000.xsd | |
| 10 | Coligada\*  \* Integrado manualmente, incluindo na tabela de de/para em ambos os sistemas | |  | |  |  | |
| 11 | Filial\*  \* Integrado manualmente, incluindo na tabela de de/para em ambos os sistemas | |  | |  |  | |
| 12 | Prestadores | | RM | | Protheus | CustomerVendor\_2\_002.xsd | |
| 13 | Convênios | | RM | | Protheus | CustomerVendor\_2\_002.xsd | |
| **Processos** | | 14 | Título a receber | | RM | | Protheus | AccountReceivableDocument\_3\_000.xsd | |
| 15 | Título a pagar | | RM | | Protheus | AccountPayableDocument\_2\_000.xsd | |
| 16 | Baixa de títulos | | RM | | Protheus | AccountReceivableDocumentDischarge\_2\_000.xsd | |
| 17 | Cancelamento de baixa | | RM | | Protheus | ReversalOfAccountReceivableDocumentDischarge\_2\_000.xsd | |
| 18 | Nota fiscal de entrada | | Protheus | | RM | Invoice\_3\_001.xsd | |
| 19 | Saldo | | RM | | Protheus | STOCKLEVEL\_1\_000.xsd | |
| 20 | Movimentação de estoque | | RM/ Protheus | | Protheus/ RM | STOCKTURNOVER\_1\_003.xsd | |
| 21 | Transferências | | RM/ Protheus | | Protheus/ RM | TRANSFERWAREHOUSE\_1\_001.xsd | |
| 22 | Inventário | | Protheus | | RM | INVENTORY\_1\_000.xsd | |
| 23 | Pedido de venda | | RM | | Protheus | ORDER\_3\_002.xsd | |

## Fluxo das Informações

O fluxo básico desta integração está em definir a origem da informação, enviar para o EAI da linha do produto e este se comunica com o EAI da outra linha. Ambos os produtos possuirão as mesmas informações, porém podem possuir códigos diferentes. Cada sistema possui uma tabela de de-para onde são armazenados os códigos de origem e os códigos de destino e a entidade correspondente. Com isso, cada sistema envia o seu código e o outro sistema faz a troca assim que receber a mensagem. Abaixo serão detalhados cada entidade envolvida nesta integração.

## Cadastros

Os cadastros são a base da integração entre os sistemas. Foi definido o sistema de origem para cada cadastro, portanto qualquer alteração nesta origem pode impactar na integração padrão. A alteração de sistema de origem impacta na configuração da mensagem utilizada em ambos os sistemas e pode envolver algum tipo de desenvolvimento, seja uma fórmula visual, um complemento na mensagem na parte de envio ou recebimento da mensagem, no caso da linha RM.

## Empresa / Filial

É o primeiro cadastro que deve ser realizado nesta integração. No RM esta entidade é um cadastro comum. Mas no Protheus a Empresa é definida no Arquivo Sigamat.emp que fica no System do ambiente do Protheus e não faz parte de uma tabela de banco de dados. Este é o arquivo que permite à empresa utilizar o sistema. Isto faz parte da implantação do Protheus padrão.

Este cadastro deverá ser feito manualmente no Protheus e no RM, e depois configurar o “de/para” de integração correspondente (RM e Protheus possuem interfaces específicas para este fim). Neste caso, não será utilizada nenhuma mensagem para o sincronismo deste cadastro.

O cadastro de filial também deve ser feito manualmente na tabela de “de-para” de integração.

|  |  |  |  |
| --- | --- | --- | --- |
| De-para RM (Empresa) | | De-Para Protheus (Empresa)/(FILIAL) | |
| Tabela RM | GCOLIGADA | **Referência** | RM |
| Chave Primária RM | CODCOLIGADA | **Company** | <Valor da Empresa RM> |
| Valor Chave Primária RM | <Valor CODCOLIGADA> | **Branch** | <Valor da Coligada RM> |
| Sistema Integrado | PROTHEUS | **Emp. Protheus** | <Empresa do Protheus> |
| Valor Chave Integração | < Valor recebido pelo InternalId > | **Fil.Protheus** | <Filial do Protheus> |

**Banco**

O cadastro de bancos, agências e conta caixa devem ser cadastrados somente no BackOffice Protheus através do módulo SIGAFIN. Esta informação é utilizada somente na integração financeira quando se deve informar a conta caixa no processo de baixa.

**Identificador da Mensagem: BANK**

Versão: 2.000

Módulo RM: BackOffice – Gestão Contábil

Módulo Protheus: SIGAFIN

Tipo de Envio: Síncrono.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **PROTHEUS** | | **RM** | |
| Tabela | Campo | Tabela | Campo |
| **Code** | SA6010 | A6\_CODE | GBANCO | NUMBANCO |
| **Name** | SA6010 | A6\_NOME | GBANCO | NOME |
| **ShortName** | SA6010 | A6\_NREDUZ | GBANCO | NOMEREDUZIDO |
| **Febraban** | SA6010 | A6\_NUMBCO | GBANCO | NUMEROOFICIAL |
| **Code** | SA6010 | A6\_CODE | GAGENCIA | NUMBANCO |
| **Agency/Number** | SA6010 | A6\_AGENCIA | GAGENCIA | NUMAGENCIA |
| **Address/Number** |  |  | GAGENCIA | NUMERO |
| **Address/Complement** | SA6010 | A6\_END | GAGENCIA | COMPLEMENTO |
| **Address/City/Description** | SA6010 | A6\_MUN | GAGENCIA | CIDADE |
| **Address/State/Code** | SA6010 | A6\_EST | GAGENCIA | ESTADO |
| **Address/District** | SA6010 | A6\_BAIRRO | GAGENCIA | BAIRRO |
| **Address/ZIPCode** | SA6010 | A6\_CEP | GAGENCIA | CEP |
| **ContactInformation/ CommunicationInformation/PhoneNumber** | SA6010 | A6\_TEL | GAGENCIA | TELEFONE |
| **Account/Number** |  |  | FCONTA | NROCONTA |
| **CompanyId** |  |  | FCONTA | CODCOLIGADA |
| **CompanyId** |  |  | FCXA | CODCOLIGADA |
| **Account/Number** |  |  | FCXA | CODCXA |
| **-** |  | concat('Conta Caixa - ',Number) | FCXA | DESCRICAO |
| **CompanyId** |  |  | FCXA | CODCOLPROP |
| **CompanyId** |  |  | FCXA | CODCOLCONTA |

Protheus:

RM:

 

**Centro de Custo**

Os Centros de Custos devem ser cadastrados somente no BackOffice Protheus através do SIGACTB (Atualizações / Entidades / Custos) e serão sincronizados automaticamente para o RM.

**Identificador da Mensagem: COSTCENTER**

Versão: 2.000

Módulo RM: BackOffice – Gestão de Estoque, Compras e Faturamento /Cadastros / Centro de Custo

Módulo Protheus: SIGACTB

Tipo de Envio: Síncrono.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **PROTHEUS** | | **RM** | |
| Tabela | Campo | Tabela | Campo |
| **CompanyId** | CTT |  | GCCUSTO | CODCOLIGADA |
| **CompanyInternalId** | CTT | Empresa | - | - |
| **BranchId** | CTT | CTT\_FILIAL | - | - |
| **Code** | CTT | CTT\_CUSTO | GCCUSTO | CODCCUSTO |
| **InternalId** | CTT | Empresa/CTT\_FILIAL/CTT\_CUSTO |  | IDINTEGRACAO |
| **RegisterSituation** | CTT | CTT\_BLOQ | GCCUSTO | ATIVO |
| **Name** | CTT | CTT\_DESC01 | GCCUSTO | NOME |
| **ShortCode** | CTT | CTT\_RES | GCCUSTO | CODREDUZIDO |
| **SPED** |  | - | GCCUSTO | ENVIASPED |
| **Class** | CTT | CTT\_CLASSE | GCCUSTO | PERMITELANCAMENTO |

Notas:

**RM**: Deve-se definir a máscara do código do centro de custo. O código no Protheus é um campo livre, podendo assim enviar um valor que o RM não possa aceitar, o RM faz a validação do código do Protheus de acordo com a máscara e retorna um erro quando existir.

A tag <SPED> da mensagem única é do tipo boolean (true/false) que será gravado no campo “SPED” do RM os valores “T” para true e “F” para false.

A tag <RegisterSituation> da mensagem única é um Enumerado (Active/Inactive) que será gravado no campo “ATIVO” os valores “T” para Active e “F” para Inactive.

A tag <Class> será gravada no campo “PERMITELANCAMENTO”. Quando o valor da tag for 1 (Sintético) será gravado 0, se o valor da tag for 2 (Analítico) será gravado 1.

**Importante**:

Após cadastrar os centros de custos, acessar o RMSaude.exe / Opções / Parâmetros / Funções Automáticas, cadastrar a função Importação de Centro de Custo, definir um período, salvar e em seguida clicar no botão Executa.

## Moeda

As Moedas devem ser cadastrados somente no BackOffice Protheus através do **SIGACTB (Atualizações / Cadastros / Moedas Contábeis)** e serão sincronizados automaticamente para o RM.

Não é permitido alterar o símbolo de uma moeda já cadastrada.

**Identificador da Mensagem: CURRENCY**

Versão: 2.000

Módulo RM: BackOffice – Gestão de Estoque, Compras e Faturamento /Cadastros / Financeiro / Moedas e Índices

Módulo Protheus: SIGACTB

Tipo de Envio: Síncrono.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **PROTHEUS** | | **RM** | |
| Tabela | Campo | Tabela | Campo |
| **Code** | CTO | CTO\_MOEDA | - | - |
| **InternalId** | CTO | Empresa/ CTO\_FILIAL/ CTO\_MOEDA | HCINTEGRACAOID | IDINTEGRACAO |
| **Description** | CTO | CTO\_DESC | GMOEDA | DESCRICAO |
| **Symbol** | CTO | CTO\_SIMB | GMOEDA | SIMBOLO |
| **DecimalPlaces** | CTO | CTO\_DECIM | GMOEDA | NUMCASASDECIMAIS |

Notas:

RM: O símbolo da moeda é a chave primária. Desta forma, ao cadastrar no Protheus uma moeda com um símbolo que já exista no RM ele será vinculado ao registro cadastrado anteriormente caso seja de empresas diferentes, ou seja, teremos dois registros no de/para do RM apontando para um único registro de moeda. Exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Empresa | Moeda | Descrição | Símbolo | Casas Decimais |
| **01** | 01 | Moeda 01 | € | 2 |
| **02** | 01 | Moeda 02 | € | 2 |
| **03** | 01 | Moeda 03 | € | 2 |

O de/para no RM ficará:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Tabela RM | Chave RM | Valor Chave RM | Sistema Integrado | Chave Integração |
| **GMOEDA** | SIMBOLO | € | Protheus | 01/ /01 |
| **GMOEDA** | SIMBOLO | € | Protheus | 02/ /01 |
| **GMOEDA** | SIMBOLO | € | Protheus | 03/ /01 |

Caso o usuário tente cadastrar uma nova moeda com o mesmo símbolo para a empresa que já tenha este símbolo integrado o RM retornará uma mensagem de erro. Exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Empresa | Moeda | Descrição | Símbolo | Casas Decimais |
| **01** | 02 | Moeda 02 | € | 2 |

Neste caso será retornado uma mensagem de erro pois a empresa 01 já possui a moeda 01 com o símbolo € cadastrado. Este tratamento será feito no RM via eventos.

Se alterado no PROTHEUS dados de uma moeda, cuja exista mais de um de-para no RM, as demais moedas do RM sofrerão a alteração, porém no PROTHEUS as demais moedas nada sofrerão. Exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Empresa | Moeda | Descrição | Símbolo | Casas Decimais |
| **02** | 01 | Moeda 01 alterada | € | 4 |

Para a alteração acima serão alterados o cadastro da moeda 01 da empresa 02 do Protheus e na moeda € do RM porém, as moedas 01 da empresa 01 e 03 do Protheus não serão alteradas.

Protheus:

RM:

## Cliente/Fornecedor

Os Fornecedores devem ser cadastrados somente no BackOffice Protheus através do SIGAFIN (Atualizações / Cadastros / Fornecedor).

O sincronismo de Cliente e Fornecedor será de forma automática para o RM utilizando a mesma estrutura de mensagem. O que os difere é a Tag <EntityType>.

Esta mesma mensagem é utilizada para o cadastro de convênios, prestadores e responsáveis financeiros. Porém estes cadastros são realizados no TOTVS Gestão Hospitalar.

**Identificador da Mensagem: CUSTOMERVENDOR**

Versão: 2.002

Módulo RM: BackOffice – Gestão de Estoque, Compras e Faturamento /Cadastros / Financeiro / Clientes/Fornecedores

Módulo Protheus: SIGAFAT e SIGAFIN

Tipo de Envio: Síncrono

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **PROTHEUS - Cliente** | | **PROTHEUS - Fornecedor** | | **RM** | |
| Tabela | Campo | Tabela | Campo | Tabela | Campo |
| CompanyId | SA1 | Empresa | SA2 | Empresa | FCFO | CODCOLIGADA |
| BranchId | SA1 | A1\_FILIAL | SA2 | A2\_FILIAL | - | - |
| CompanyInternalId | SA1 | Empresa/A1\_FILIAL | SA2 | Empresa/ A2\_FILIAL | - | - |
| Code | SA1 | A1\_COD | SA2 | A2\_COD | FCFO | CODCFO |
| InternalId | SA1 | Empresa/A1\_FILIAL /A1\_COD | SA2 | Empresa/ A2\_FILIAL/A2\_COD | HCINTEGRACAOID |  |
| ShortName | SA1 | A1\_NREDUZ | SA2 | A2\_NREDUZ | FCFO | NOMEFANTASIA |
| Name | SA1 | A1\_NOME | SA2 | A2\_NOME | FCFO | NOME |
| Type | SA1 | Customer | SA2 | Vendor | FCFO | PAGREC |
| EntityType | SA1 | A1\_TIPO | SA2 | A2\_TIPO | FCFO | PESSOAFISOUJUR |
| RegisterDate | SA1 | RegisterDate |  |  |  |  |
| RegisterSituation | SA1 | A1\_MSBLQL | SA2 | A2\_MSBLQL | FCFO | ATIVO |
| GovernmentalInformation.Id Name=CNPJ | SA1 | A1\_CGC | SA2 | A2\_CGC | FCFO | CGCCFO |
| Address.Address | SA1 | A2\_END | SA2 | A2\_END | FCFO | RUA |
| Address.Number | SA1 | A2\_END | SA2 | A2\_END | FCFO | NUMERO |
| Address.Complement | SA1 | A1\_COMPLEM | SA2 | A2\_COMPLEM | FCFO | COMPLEMENTO |
| Address.City.CityCode | SA1 | A1\_EST+A1\_COD\_MUN | SA2 | A2\_COD\_MUN | FCFO | CODMUNICIPIO |
| Address.City.CityDescription | SA1 | A1\_MUN | SA2 | A2\_MUN | FCFO | CIDADE |
| Address.District | SA1 | A1\_BAIRRO | SA2 | A2\_BAIRRO | FCFO | BAIRRO |
| Address.State.StateCode | SA1 | A1\_EST | SA2 | A2\_EST | FCFO | CODETD |
| Address.State.StateDescription | SA1 | X5DESCRI | SA2 | X5DESCRI | FCFO | DESCETD |
| Address.Country.CountryCode | SA1 | A1\_PAIS | SA2 | A2\_PAIS | FCFO | CODPAIS |
| Address.Country.CountryDescription | SA1 |  | SA2 |  | FCFO | PAIS |
| Address.ZIPCode | SA1 | A1\_CEP | SA2 | A2\_CEP | FCFO | CEP |
| Address.POBox | SA1 | A1\_CX\_POST | SA2 | A2\_CX\_POST | FCFO | CAIXAPOSTAL |
| ListOfCommunicationInformation.CommunicationInformation.PhoneNumber | SA1 | A1\_TEL | SA2 | A2\_TEL | FCFO | TELEFONE |
| ListOfCommunicationInformation.CommunicationInformation.FaxNumber | SA1 | A1\_FAX | SA2 | A2\_FAX | FCFO | FAX |
| ListOfCommunicationInformation.CommunicationInformation.Email | SA1 | A1\_EMAIL | SA2 | A2\_EMAIL | FCFO | EMAIL |

Notas:

* A máscara em ambos os sistemas deve ser igual.
* Ao cadastrar um prestador é gerado um fornecedor no RM e sincronizado com o Protheus . O mesmo é gerado um fornecedor no Protheus.
* Ao cadastrar um convênio é gerado um cliente no RM e sincronizado com o Protheus .  O mesmo é gerado um cliente no Protheus.
* Ao cadastrar um responsável financeiro, é criado um cliente no RM e depois gerado um cliente no Protheus. Neste caso, o sincronismo só ocorre no pedido de nota fiscal.

Protheus:

## Grupo de Estoque

Este cadastro no RM é tratado como uma tabela de classificação, TTB1 e sincronizado do RM para o Protheus.

**Identificador da Mensagem: FAMILY**

Versão: 2.000

Módulo RM: BackOffice – Gestão de Estoque, Compras e Faturamento/Cadastros/Tabelas de classificação

Módulo Protheus: SIGAEST

Tipo de Envio: Síncrono

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **PROTHEUS** | | **RM** | |
| Tabela | Campo | Tabela | Campo |
| **CompanyId** | SBM010 | Empresa | - | CODCOLIGADA |
| **Code** | SBM010 | BM\_GRUPO | TTB1 | CODTB1FAT |
| **InternalId** | SBM010 | Empresa/ BM\_GRUPO | HCINTEGRACAOID | CODCOLIGADA/ CODTB1FAT |
| **Description** | SBM010 | BM\_DESC | TTB1 | DESCRICAO |
| **WarehouseCode** |  | - | TTB1 | - |
| **UnitOfMeasureCode** |  | - | TTB1 | - |
| **FamilyClassificationCode** |  | - | TTB1 | - |

Notas:

Para utilizar esta mensagem é necessário parametrizar o Gestão de Estoques do RM para utilizar a tabela de classificação 1 TTB1. Isso já é feito pelo script de implantação. É necessário utilizar a fórmula visual ***Integração Grupo de produto*** para fazer o sincronismo deste cadastro com o Protheus.

Deve-se definir a máscara deste cadastro para ser compatível com o cadastro no Protheus.

RM:

Protheus:

## Produto/Serviço

Os Produtos e Serviços devem ser cadastrados no RM e sincronizados automaticamente para o Protheus; ou configurados para ter origem no Protheus e sincronizados com o RM. Isso depende da configuração do Adapter no Protheus.

**Identificador da Mensagem: ITEM**

Versão: 2.001

Módulo RM: BackOffice – Gestão de Estoque, Compras e Faturamento /Cadastros / Produtos

Módulo Protheus: SIGAEST

Tipo de Envio: Síncrono.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **PROTHEUS** | | **RM** | |
| Tabela | Campo | Tabela | Campo |
| CompanyId | SB1 | Empresa | TPRODUTO | CODCOLPRD |
| TPRODUTODEF | CODCOLIGADA |
| BranchId | SB1 | B1\_FILIAL | - | - |
| CompanyInternalId | SB1 | Empresa/B1\_FILIAL | - | - |
| Code | SB1 | B1\_COD | TPRODUTO | CODIGOPRD |
| InternalId | SB1 | Empresa/B1\_FILIAL/ B1\_COD | HCINTEGRACAOID | IDINTEGRACAO |
| Name | SB1 | B1\_DESC | TPRODUTO | DESCRICAO |
| ShortName | SB1 | B1\_DESC | TPRODUTO | NOMEFANTASIA |
| Active | SB1 | B1\_ATIVO | TPRODUTO | INATIVO |
| UnitOfMeasureInternalId | SB1 | Empresa/SAH\_FILIAL/B1\_UM | TPRODUTODEF | CODUNDCONTROLE |
| CODUNDCOMPRA |
| CODUNDVENDA |
| DeployDate | - | - | TPRODUTO | DTCADASTRAMENTO |
| NetWeight | SB1 | B1\_PESO | TPRODUTO | PESOLIQUIDO |
| GrossWeight | SB1 | B1\_PESBRU | TPRODUTO | PESOBRUTO |
| Origin | SB1 | B1\_ORIGEM | TPRODUTO | REFERENCIACP |
| Values.CostPrice | SB1 | BZ\_UPRC ou B1\_UPRC | TPRODUTODEF | PRECO1 |
| Values.SalesPrice | SB1 | B1\_PRV1 | TPRODUTODEF | PRECO2 |
| Values.AverageCostPrice | SB2 | B2\_CM1 | TPRODUTODEF | CUSTOMEDIO |
| Values.StandardCostPrice | SB1 | BZ\_CUSTD ou B1\_CUSTD | TPRODUTODEF | CUSTOUNITARIO |
| Values.BaseDate | SB1 | BZ\_UCALSTD ou B1\_UCALSTD | TPRODUTODEF | DATABASEPRECO1 |
| ProductType | SB1 | B1\_TIPO | TPRODUTO | TIPO |
| SecondUnitOfMeasureInternalId | SB1 | Empresa/AH\_FILIAL/B1\_SEGUM | HCUNDCONV | CODUNDSEG |
| MultiplicationFactorValue | SB1 | B1\_CONV | HCUNDCONV | FATOR |

Notas:

São aceitos dois tipos de produtos <ProductType>, Produto acabado (10) e Mão de Obra (07) que serão gravados o valor “P” para Mercadoria e “S” para Mão de Obra.

As configurações inicias da integração irá alterar a máscara do Código do Produto para “QQQQQQQQQQQQQQQ” que permite 15 caracteres de qualquer tipo.

A primeira unidade de medida do Protheus será gravada em todas unidades de medida (Controle, Compra e Venda) do Produto no RM.

Produto Global: Ao receber a mensagem única como produto global, o RM irá verificar via Eventos se nos parâmetros de produto está configurado para utilizar Produto Global, se estiver, será ignorado o código da coligada (CompanyId) enviado pelo Protheus e será gravado com o código 0 (zero). As configurações de Produto Global no Protheus e no RM ficarão a cargo do implantador.

Protheus:

RM:

 

## Condição de pagamento

As Condições de Pagamentos devem ser cadastradas somente no BackOffice Protheus através do SIGACOM (Atualizações / Cadastros / Cond. de Pagamento) e serão sincronizados automaticamente para o RM.

**Identificador da Mensagem: PAYMENTCONDITION**

Versão: 2.000

Módulo RM: BackOffice – Gestão de Estoque, Compras e Faturamento/Cadastros/Tabelas auxiliares / Condições de pagamento

Módulo Protheus: SIGACOM

Tipo de Envio: Síncrono

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **PROTHEUS** | | **RM** | |
| Tabela | Campo | Tabela | Campo |
| CompanyId | SE4 | Empresa | TCPG | CODCOLIGADA |
| BranchId | SE4 | E4\_FILIAL | - | - |
| CompanyInternalId | SE4 | Empresa/E4\_FILIAL | - | - |
| Code | SE4 | E4\_CODIGO | TCPG | CODCPG |
| InternalId | SE4 | Empresa/E4\_FILIAL /E4\_CODIGO | HCINTEGRACAOID | IDINTEGRACAO |
| Description | SE4 | E4\_DESCRI | TCPG | NOME |
| DayFirstDue | SE4 | Ver Tópico 6.1.7.2 | TCPG | PRAZO1 |
| QuantityPlots | SE4 |  | TCPG | QUANTASVEZES1 |
| RangePlots | SE4 |  | TCPG | PERIODOEMDIAS1 |
| WeekDayFixed | SE4 |  | TCPG | DIASVENCSEMANA |
| DaysCondition | - | - | TCPG | TIPO1 |

Protheus:

RM

 

## Unidade de medida

As Unidades de Medidas devem ser cadastradas somente no BackOffice Protheus através do SIGAQIE (Atualizações / Cadastros / Unidades Medida) e serão sincronizados automaticamente para o RM.

**Identificador da Mensagem: UNITOFMEASURE**

Versão: 2.000

Módulo RM: BackOffice – Gestão de Estoque, Compras e Faturamento /Cadastros / Tabelas auxiliares / Unidade

Módulo Protheus: SIGAQIE

Tipo de Envio: Síncrono

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **PROTHEUS** | | **RM** | |
| Tabela | Campo | Tabela | Campo |
| Code | SAH | AH\_UNIMED | TUND | CODUND |
| InternalId | SAH | Empresa/AH\_FILIAL/ AH\_UNIMED | HCINTEGRACAOID | IDINTEGRACAO |
| Description | SAH | AH\_DESCPO | TUND | DESCRICAO |
|  |  |  | TUND | CODUNDBASE |
|  |  |  | TUND | FATORCONVERSAO |

Notas:

No Protheus a unidade de medida é um cadastro por empresa e no RM o cadastro de unidade de medida é um cadastro compartilhado, para solucionar esse caso as unidades de medida com mesmo símbolo no Protheus irão apontar para uma mesma unidade de medida do RM

No RM deve ser informada uma Unidade Base, porém não temos esta informação no Protheus, desta forma, este campo será preenchido com o valor do campo <Code>.

O campo “FATORCONVERSAO” receberá sempre o valor 1, pois a Unidade Base será sempre o mesmo código da Unidade Principal.

## Local de Estoque

Os Locais de Estoque devem ser cadastrados somente no BackOffice Protheus no SIGACOM (Atualizações / Cadastros / Locais de Estoque) e sincronizados automaticamente para o RM através de mensagem única.

**Identificador da Mensagem: WAREHOUSE**

Versão: 1.000

Módulo RM: BackOffice – Gestão de Estoque, Compras e Faturamento /Cadastros / Local de Estoque

Módulo Protheus: SIGACOM

Tipo de Envio: Síncrono

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **PROTHEUS** | | **RM** | |
| Tabela | Campo | Tabela | Campo |
| CompanyId | NNR | Empresa | TLOC | CODCOLIGADA |
| BranchId | NNR | NNR\_FILIAL | - | - |
| CompanyInternalId | NNR | Empresa/NNR\_FILIAL | TLOC | CODFILIAL |
| Code | NNR | NNR\_CODIGO | TLOC | CODLOC |
| InternalId | NNR | Empresa/NNR\_FILIAL/NNR\_CODIGO | TLOC | CODCOLIGADA/CODFILIAL/CODLOC |
| Description | NNR | NNR\_DESCRI | TLOC | NOME |
| Active |  |  | TLOC | INATIVO (0 – ATIVO, 1 – INATIVO) |

## Processos

Os processos poderão ser gerados através de dois Tipos de Fluxo:

* RM / Protheus: O RM irá consumir um WebService do EAI Protheus para envio da(s) mensagem(s) e o Protheus irá retornar uma mensagem com o status do processamento, após a resposta do Protheus, o RM atualizará o registro no Monitor da Fila de Integração.
* Protheus / RM: O Protheus irá consumir um WebService do EAI RM para envio da(s) mensagem(s) e o RM irá retornar uma mensagem com o status do processamento.

A seguir serão descritos os processos do TOTVS Gestão Hospitalar integrados diretamente com o BackOffice Protheus.

## Título a pagar

Tipo de Fluxo: RM e Protheus

Mensagem: ACCOUNTPAYABLEDOCUMENT

Versão: 2.000

O título a pagar se refere aos repasses que o hospital deve pagar ao médico. Após serem liberados para pagamento, o usuário deverá clicar no botão ***Gerar título a pagar no Protheus*** para que o processo seja disparado. O processo de geração do movimento no Nucleus foi mantido. Após a inclusão do movimento é enviado para o Protheus a mensagem ACCOUNTPAYABLEDOCUMENT com os dados do prestador, valor a ser pago, data de emissão, vencimento. A série do documento gerado será o parâmetro **SERIEDOCFOLHAPAGTO** e o tipo de documento será o conteúdo do parâmetro **TIPODOCFOLHAPAGTO**. Caso seja necessário cancelar a folha, basta clicar no botão **Retornar para correção** que o título será excluído do Protheus.

## Título a receber

Tipo de Fluxo: RM è Protheus

Mensagem: ACCOUNTRECEIVABLEDOCUMENT

Versão: 3.000

O título a receber é gerado para as faturas de convênios. Além do título a receber é gerando em conjunto o pedido de venda. Este processo é executando no menu Faturamento -> Geração de Movimento de fatura.

A série do documento gerado será o parâmetro **SERIEDOCMOVFATURA** e o tipo de documento será o conteúdo do parâmetro **TIPODOCMOVFATURA**. Caso seja necessário cancelar o movimento de fatura, basta clicar no botão **Exclui Movimento de Fatura** que o título será excluído do Protheus.

## Baixa de títulos

Tipo de Fluxo: RM è Protheus

Mensagem: ACCOUNTRECEIVABLEDOCUMENTDISCHARGE

Versão: 2.000

A baixa de títulos é realizada nas faturas dos convênios. Após gerado o movimento de fatura e consequentemente gerado no Protheus o título a receber, basta acessar o menu *Tesouraria/Controle de Recebimentos,* página inferior *Fatura,* subpágina *Fatura.* Informe a competência, o convênio e a unidade de faturamento e clique no botão *Pesquisar*. Selecione a fatura desejada, clique na subpágina *Recebimentos* e inclua o valor recebido. Neste momento é solicitada a conta-caixa deste recebimento e a baixa será efetuada no Protheus.

**Cancelamento de Baixa de títulos**

Tipo de Fluxo: RM è Protheus

Mensagem: REVERSALOFACCOUNTRECEIVABLEDOCUMENTDISCHARGE

Versão: 2.000

O cancelamento de baixa de títulos deve ser realizado quando o valor informado está incorreto ou algum outro motivo que leve a exclusão do recebimento. Feito isso, a baixa associada será excluída no Protheus.

## Inventário

Tipo de Fluxo: Protheus è RM

Mensagem: INVENTORY

Versão: 1.000

O inventário é realizado no Protheus e sincronizado com o RM apenas para manter o histórico de movimentações dos produtos, assim como a geração dos códigos de barras para os diversos lotes.

## Nota fical de entrada

Tipo de Fluxo: Protheus è RM

Mensagem: INVOICE

Versão: 3.001

A nota fiscal de entrada de produtos é realizada no Protheus e sincronizada com o RM.

No RM é gerado um movimento com o código do fornecedor da nota, data de emissão e seus itens com a quantidade, preço unitário, validade e lote. Ao receber a nota fiscal de entrada, a integração criará os novos lotes recebidos com suas respectivas validades e incluirá nas tabelas do Nucleus. Estes dados são importantes para que o TOTVS Gestão Hospitalar consiga atualizar os preços dos itens e gerar os códigos de barras dos itens.

## Pedido de venda

Tipo de Fluxo: RM è Protheus

Mensagem: ORDER

Versão: 3.002

O pedido de venda se refere à fatura gerada para os convênios e ao pedido de emissão de nota fiscal para o paciente.

Após encerrada a conta do paciente e esta possuir gastos particulares, o usuário acessará o TOTVS Gestão Hospitalar, menu Tesouraria /Controle de Solicitação p/ Emissão de Nota Fiscal / Recibos. Clicar no botão *Gerar Solicitação de emissão de documento*, informar o paciente, selecionar o tipo de gasto, selecionar o responsável financeiro e clica no botão *Processar*. Após isso, clicar no botão *Gera Pedido de emissão de documento para o Protheus*. Neste momento é exibido o movimento associado a este processo e deve-se informar a condição de pagamento deste pedido de venda.

Para a fatura, acesse o menu Faturamento /Geração de Movimento de fatura. Clicar no botão *Gera Movimento de fatura e informar a condição de pagamento para este pedido. No caso da fatura são utilizadas duas mensagens, a Order para o pedido de venda e a ACCOUNTRECEIVABLEDOCUMENT para o título a receber.*

## Saldo em estoque

Tipo de Fluxo: RM è Protheus

Mensagem: STOCKLEVEL

Versão: 1.000

Esta mensagem é utilizada para se consultar o saldo no BackOffice Protheus. São enviados o produto e o local de estoque e retornam o saldo por lote e validade que serão exibidos na tela de movimentação de estoque e impressão de etiquetas de códigos de barras.

## 1.1.8.    Movimentação de estoque

Tipo de Fluxo: RM è Protheus e Protheus è RM

Mensagem: STOCKTURNOVER

Versão: 1.003

Esta mensagem é utilizada em toda movimentação que envolve mudança de saldo no estoque. Tanto as movimentações do lado do RM quanto do lado do Protheus refletirão em ambos os sistemas. No lado do RM seria apenas como histórico, já no Protheus ocorre a alteração no saldo e suas respectivas alterações financeiras e fiscais. Esta mensagem envolve requisição para paciente, devolução de paciente, requisição para centro de custo, devolução de centro de custo, folha de sala, requisição para o CME

**Devolução**

## Transferência

Tipo de Fluxo: RM è Protheus e Protheus è RM

Mensagem: TRANSFERWAREHOUSE

Versão: 1.001

Esta mensagem é utilizada para refletir as transferências de produtos entre locais de estoque.

**Restrições:**

No RM, um movimento de transferência, os itens só podem ser transferidos entre dois locais de estoque, ou seja, os locais são definidos no movimento. Já no Protheus, é possível definir para cada item o local de origem e o de destino. Com isso, com a integração ativa, no Protheus deve-se realizar as transferências apenas com os mesmos locais de estoque para todos os itens.

**Checklist de suporte da aplicação**

**Instalação/Configuração**

Protheus:

* Verificar no AppServer.INI está configurado ambiente correto, Filial, ou se a chamada do Scheduler foi configurado.
* Verificar no Adapter se a Rotina está cadastrada e se constam todas as informações corretas como: Nome correto do XSD, se Envia está como SIM, se o Serviço está como EAI.
* Verificar se no Scheduler foi cadastrado o Agent e se o Ambiente está o mesmo do AppServer.INI e o Agendamento se na Rotina está FWEAI,  e a Filial a que você está Logado .
* Verifique os Parâmetros, MV\_EAIMETH, MV\_EAIWS , MV\_EAIURL2, MV\_EAIUSER, MV\_EAIPASS
* Verifique o Firewall (desabilite-o).

RM:

* Verificar em RM.exe / Segmento Integrações / Aba Integração / Mensagem Única / Integrações se a integração ID = 1011 está com Status = ‘Ativo’.
* Verificar se existe as fórmulas visuais ativas.

**Checklist de Verificações:**

Relacione itens de verificações para que o atendente possa:

* Identificar o funcionamento da integração

Protheus:

Para verificar se a integração está funcionando, entre no Scheduler e em EAI, clique na última linha de histórico de Transações, clique nele e clique na Lupa da mesma tela, abrirá no Browser um arquivo XML com todas as informações que você cadastrou na Tela, verifique se aparece a Data a Hora e Inicio de Processamento e Fim de Processamento, sem nenhuma mensagem de Erro no meio destas informações.

RM:

* Verificar se na fila de mensagem única existem registros.
* Verificar no menu de Integrações se a integração ID=1011 está com status = ‘Ativo’.
* Verificar se foram importadas as Fórmulas Visuais para esta integração.
* Identificar a ocorrências de problemas

Protheus:

* Procure no histórico se tem alguma linha com mensagem de Erro.

RM:

* Verificar se na fila de mensagem única existem registros com Status de Execução = “Error”.

* Coletar evidências do mau funcionamento relatado pelo cliente

Protheus:

* Tivemos o problema do Firewall estar bloqueando a entrega da mensagem, tivemos que desligar para funcionar.
* O Servidor de Entrega da Mensagem tem Usuário e Senha que devem ser logados para receber a Mensagem: para isto cadastre nos parâmetros já informados na Instalação, MV\_EAIUSER e MV\_EAIPASS  e preencher com os dados do Login e Senha.
* Host do Destinatário ter caído.
* Confirmar Endereço IP e Porta do Destinatário e verificar se está correto no parâmetro MV\_EAIURL2.

RM:

* O web.config (tags DBAlias e Port) do WebSerivce deve possuir o mesmo nome do Alias e a mesma Porta usadas na aplicação RM.exe.
* Realizar possíveis ajustes na integração quanto à configuração ou negócio

Protheus:

* Verifique se os Parâmetros estão configurados corretamente com o endereço de IP e Porta do Server Destino que receberá a Mensagem ou a Configuração do Adapter ou seu Appserver.INI
* Outras Informações.

divs
