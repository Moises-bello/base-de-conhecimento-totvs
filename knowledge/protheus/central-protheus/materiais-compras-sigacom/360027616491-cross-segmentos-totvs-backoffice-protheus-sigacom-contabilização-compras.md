---
article_id: 360027616491
category: Materiais - Compras (SIGACOM)
content_hash: dcc8afb1492f3d1a6123f4dcd759bf4c93156b10c94be7a6154072162e75b5b7
fetched_at: '2026-06-28T22:41:08.753576+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Contabilização Compras
type: support-article
updated_at: '2026-06-03T18:02:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027616491-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Contabiliza%C3%A7%C3%A3o-Compras
---

**Dúvida**  
Contabilização Compras - Quais Lançamentos Padrões e como funciona ?  
  
**Ambiente**  
Protheus – Compras – A partir da versão 12  
  
**Solução**

**No módulo do compras, a contabilização pode ocorrer de duas formas :**

* **On-line ( MATA103 - documento de entrada )** – Os lançamentos são gerados automaticamente a medida que os processos são executados no Protheus.
* **Off-line ( CTBANFE - contabilização off line )** – Todas as contabilizações que seriam executadas pelos processos são efetuadas no momento em que o usuário solicita a contabilização, por meio da opção Contabilização Off-Line, menu Miscelânea dos módulos do Protheus.

|  |  |  |  |
| --- | --- | --- | --- |
| **Lançamentos padrão no documento de entrada** | | | |
| ONLINE | OFFLINE | CÓDIGO | Descrição |
|  |  |  |  |
| X | X | 640 | Entrada de NF Devolução/Beneficiamento ( Cliente ) - Itens |
| X | X | 641 | Entrada de NF Devolução/Beneficiamento ( Cliente ) - Itens do Rateio |
| X | X | 642 | Entrada de NF Devol.Vendas - Total (SF1) |
| X | X | 650 | Entrada de NF Normal ( Fornecedor ) - Itens |
| X | X | 651 | Contabilização do rateio dos itens do documento de entrada para Fornecedor - Estão disponíveis as tabelas de Tipo de Entrada e saída, produto, rateio de itens, item do documento de entrada e Fornecedor conforme o tipo do documento. Este lançamento não impede a execução do lançamento 650. |
|  |  |  |  |
| X |  | 655 | Contabilização do exclusão dos itens do documento de entrada - Estão disponíveis as tabelas de Tipo de Entrada e saída, produto, documento de entrada e Cliente ou Fornecedor conforme o tipo do documento. |
| X |  | 656 | Contabilização da exclusão do rateio dos itens do documento de entrada - Estão disponíveis as tabelas de Tipo de Entrada e saída, produto, documento de entrada, rateio de itens, item do documento de entrada e Cliente ou Fornecedor conforme o tipo do documento. Este lançamento não impede a execução do lançamento 651. |
| X | X | 660 | Contabilização do documento de entrada pelos totais - Disponível tabela Fornecedor . |
| X |  | 665 | Contabilização da exclusão do documento de entrada - Disponível a tabelas de Cliente ou Fornecedor conforme o tipo do documento. |
| X | X | 950 | Contabilização dos itens do documento de entrada especifico para documentos de provenientes do módulo de importação - Estão disponíveis as tabelas de Tipo de Entrada e saída e Cliente ou Fornecedor conforme o tipo do documento. Este lançamento é executado junto com o lançamento 650. |
| X |  | 955 | Contabilização da exclusão dos itens do documento de entrada especifico para documentos de provenientes do módulo de importação - Estão disponíveis as tabelas de Tipo de Entrada e saída e Cliente ou Fornecedor conforme o tipo do documento. Este lançamento é executado junto com o lançamento 655. |
| X | X | 65C | Contabilização do rateio por multi naturezas financeiras ( tabela SEV ) |
| X |  | 65D | Contabilização da exclusão do rateio por multi naturezas financeiras ( tabela SEV ) |

Para mais detalhes sobre Lançamentos Padrões [**clique aqui**](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba080_lanc_padronizados.htm)

Caso tenha dúvidas em qual tabela utilizar para seus Lançamentos Padrão de Compras acesse a Documentação [Tabelas de utilização para os Lançamentos Padrão de Compras](https://tdn.totvs.com/pages/releaseview.action?pageId=390416061)

**Demais processos que podem ser contabilizados no compras :**

**->** Baixa automática do PA com o título gerado pelo documento de entrada quando o pedido de compras que for vinculado à nota, possua titulo PA vinculado. LP´s do financeiro mas executados pela rotina de documento de entrada ( MATA103 )

|  |  |  |  |
| --- | --- | --- | --- |
| ONLINE | OFFLINE | CÓDIGO | Descrição |
| X |  | 597 | Baixa por compensação contas a pagar |
| X |  | 589 | Cancelamento da baixa por compensação. Somente ocorrerá e será executado pelo documento de entrada quando a nota que efetuou a compensação automática for excluída. |

Conheça mais sobre :

[**título PA no Pedido de compras**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015664151)

**->** Pedidos de compras e Eliminação de resíduos

|  |  |  |  |
| --- | --- | --- | --- |
| ONLINE | OFFLINE | CÓDIGO | Descrição |
| X | X | 652 | Pedido de Compras - Inclusão de Pedidos Itens |
| X |  | 657 | Pedido de Compras - Exclusão de Pedidos Itens |
| X |  | 658 | Pedido de Compras - Eliminação de Resíduos - Itens |
| X | X | 659 | Pedido de Compras - Rateio do Pedido de Compra |
| X |  | 65A | Pedido de Compras - Exclusão/Estorno do Rateio do Pedido de Compra |
| X | X | 65B | Pedido de Compras por Edital |

**Configurações necessárias :**

Para utilizar o processo de contabilização deve existir os cadastros básicos de **calendário contábil**, **moeda** e amarração destes em **Moeda x Calendário**.

- Calendário Contábil (**CTBA010**):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061553833)

- Moeda Contábil (CTBA140):

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061553933)

- Moeda x Calendário Contábil (**CTBA200**):

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060614094)

**Exemplo de uma configuração simples do LP 650 na rotina CTBA080 ( cadastro de lançamento padrão )**

***Obs:***

Ao acessar o cadastro de Lançamento Padrão, se aprecer a tela abaixo em modo processo:

![Processo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7448193632919)

Por meio do F12 altere a pergunta : Visão pro Processo = Não:

![visao.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7448488640791)

- Dentro da rotina cadastrando o Lançamento Padrão **LP 650**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027069491)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027084252)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027096831)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027096871)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027096951)

# **Contabilização ONLINE - MATA103 - Documento de Entrada**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027097331)

Se o pergunte estiver habilitado para mostrar a tela de Contabilização será apresentada a tela a seguir após a confirmação do Documento de Entrada **(MATA103)**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027086872)

- A informação do lote de contabilidade pode ser consultada a partir da **tabela 09**.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060614314)

***Observação:** Se o pergunte constar para não mostrar o lançamento contábil, caso o sistema identifique alguma divergência será aberta a tela acima de contabilização.*

Após gravar a contabilização o sistema gera registro na tabela CTK e CT2.

* CTK - Arquivo de Contra-Prova
* CT2 - Lançamentos Contábeis

- Na rotina *Lançamento Contábil (**CTBA102**) > Outras Ações > Rastrear* é possível consultar sobre qual documento se trata a contabilização:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061556773)

Através dessa opção o sistema busca informações de campos das tabelas CT2, CTK, CV3 e SE5.

# **Contabilização OFFLINE - CTBANFE**

Verificar a parametrização conforme a necessidade da Contabilização:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027351972)

Consultar o log de execução:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027356151)

 Detalhes do log:![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027356651)

# 

# Agendamento da rotina CTBANFE via schedule

Como efetuar o agendamento da rotina **CTBANFE** - Rotina de contabilização off-line das notas fiscais de entrada via schedule.

A rotina **CTBANFE** está preparada para ser executada via Schedule.  
Basta seguir os mesmos procedimentos para agendamento das demais rotinas do sistema, os quais estão descritos no seguinte link:  
[Schedule - Como agendar a execução de rotinas](http://tdn.totvs.com/pages/viewpage.action?pageId=271167961)  
  
Ao informar a rotina **CTBANFE** no campo "Rotina" em Schedule > Agendamentos > Cadastro, será aberta a tela de parâmetros da rotina (caso não seja aberta, clique no botão "Parâmetros").  
Os parâmetros são os mesmos que são apresentados ao acessar a rotina **CTBANFE** via menu no módulo de Compras em *Miscelânea / Ajuste / Lc.ctb.doc.entrada*.  
Adicionalmente, na configuração via Schedule a tela de parâmetros apresenta a aba "Fórmulas". Nesta aba podem ser definidas fórmulas, que devem ser cadastradas, para que sejam retornados os valores dos parâmetros conforme desejado.  
Caso deseje utilizar fórmulas, deixe os parâmetros da aba "Parâmetro" em branco e utilize apenas as fórmulas.  
A rotina será executada conforme configurado no Schedule para efetuar a contabilização das notas fiscais de entrada

**Parâmetros**

* Parâmetros envolvidos na contabilização:
  + **MV\_PRELAN-** Indica se o Lançamento Contábil será  automaticamente lançado ou passará por Pré-Lançamento. Conteúdos: **S**=Sempre, **N**=Nunca, **D**=Doc Inconsistente . Para mais detalhes clique no link a seguir: <http://tdn.totvs.com/pages/releaseview.action?pageId=284348618>
  + **MV\_OPTNFE-**Indica se os lançamentos contábeis da rotina off-line esta preparada para utilizar query's. Somente documentos de entrada. Para mais detalhes clique no link a seguir: <http://tdn.totvs.com/pages/releaseview.action?pageId=181960817>
  + **MV\_SEGOFI-** Utilizado para definir a configuração da numeração sequencial contábil, conhecida como diário contábil ou correlativo contábil.  Para mais detalhes clique no link a seguir: <https://tdn.totvs.com/pages/releaseview.action?pageId=6068412>
  + **MV\_CNFETHR** - Quantidade de Threads para melhora de performance na contabilização na CTBANFE. <https://tdn.totvs.com/display/PROT/TSZPEZ_DT_PERFORMANCE_CONTABILIZACAO_OFFLINE_DOCUMENTO_ENTRADA>

**Observações Técnicas:**

* Quando é realizada a contabilização, o registro fica com o campo **F1\_DTLANC** preenchido com a data da contabilização. Importante: Caso ocorra a exclusão das informações referentes a contabilização de forma manual, ainda assim o campo **F1\_DTLANC** continuará preenchido, pois se há alguma informação incorreta é necessário corrigir a informação e não excluir a linha da contabilização.

* Melhoria de performance na contabilização off line : <https://tdn.totvs.com/pages/releaseview.action?pageId=181960817>

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/34644092874519-Cross-Segmentos-Totvs-Backoffice-Linha-Protheus-Compras-Como-melhorar-a-performance-da-contabiliza%C3%A7%C3%A3o-no-compras>

* Caso possua mais de uma sequência cadastrada para o mesmo lançamento padrão e esteja ativo, se o registro cair na regra do LP, mesmo se o pergunte estiver configurado para **não** mostrar a tela, será apresentada a rotina para conferência da contabilização.

* No processo de exclusão do documento de entrada mesmo que a configuração esteja para não contabilizar, a rotina por conceito contabiliza, pois a exclusão é irreversível e existe a necessidade de contabilização para abater o valor já contabilizado.

* O sistema considera a informação da entidade contábil da linha do item, ou seja, se tiver entidade contábil diferente do LP o sistema continua considerando a informação do item do documento, pois controla por árvore de decisão.

* Tanto na contabilização on line (**MATA103**) e na off line (**CTBANFE**) a data verificada pelo sistema padrão é a **data de classificação, campo** F1\_DTDIGIT do documento de entrada. Este é um conceito padrão do sistema.No caso da rotina **CTBANFE** há disponível um ponto de entrada ([**CTBNFEDT**](https://tdn.totvs.com/pages/viewpage.action?pageId=6085677)) para efetuar a verificação de outro campo de data na contabilização caso o cliente deseje.No caso da rotina **MATA103** **não há** ponto de entrada criado, no momento, específico para a necessidade de alteração da data a ser considerada, permanecendo assim o conceito padrão.

* Se houver exclusão do Documento de Entrada e o usuário deletar a linha do item o sistema irá gerar registro apenas na tabela **CTK** e não irá excluir o registro da tabela **CT2**. Nessa situação deve verificar na rotina **CTBA101** junto ao seu contábil para verificar possibilidade sobre exclusão ou estorno.

* Relatório relacionado ao processo **CTBR400.**
* Para contabilizar as notas de Despesa de Importação **(MATA119)** e de Conhecimento de Frete **(MATA116)** são utilizados pelo sistema padrão os mesmos LP´s do documento de entrada, visto que essas rotinas também geram informações nas tabelas SD1 e SF1 ( documento de entrada ), ou seja, LP 650 ( para contabilização dos itens da nota ) e LP 660 ( para contabilizar dos totais ). E, na exclusão também, o 655, ou o 665, respectivamente.

* Para Contabilizar **IBS, CBS e IS**, Favor seguir as orientações do artigo abaixo:

  [Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como Contabilizar IBS, CBS e IS?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36639180648983-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-Contabilizar-IBS-CBS-e-IS)

  **Obs:** Para utilizar essa funcionalidade é necessário que o pacote [Expedição Continua - Backoffice Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=587835160) de 06/12/2025 para frente esteja aplicado, senão, corre-se o risco de não gerar o lançamento de contabilização no módulo contábil.

* **Contabilizar alterações no pedido de compras.**

           Para que o sistema contabilize corretamente as alterações de valores efetuadas no pedido de compras, é               necessário ter o LP 657 configurado também. Veja abaixo documento sobre o processo :

[Contabilizar alterações de valores no pedido de compras](https://tdn.totvs.com.br/pages/releaseview.action?pageId=1071999134)

* **Pontos de Entrada disponíveis na CTBANFE**

  **CTBVALOK** - Validação dos lançamentos contábeis    <https://tdn.totvs.com/pages/releaseview.action?pageId=6085286>

  **CTBNFEDT** -  Escolhe a data para contabilização.          <https://tdn.totvs.com/pages/viewpage.action?pageId=6085677>

  **CTBNFE** - Alteração da query de otimização de execução da rotina   <https://tdn.totvs.com/pages/viewpage.action?pageId=6087539>

  **CTNFEORD** - Ordenar a os lançamentos padrões          <https://tdn.totvs.com/pages/viewpage.action?pageId=236590744>

  **CTNFEFIL** - Permite validar se documento será ou não validado durante contabilização   <https://tdn.totvs.com/pages/viewpage.action?pageId=704924442>

  **CTBNFEFIM** - Executa customização                            <https://tdn.totvs.com/pages/releaseview.action?pageId=6085674>

**Importante**

O Suporte Técnico não realiza a validação ou configuração de **lançamentos padrão,** pois isso envolve informações específicas sobre os processos e necessidades do negócio. Ressaltamos que a configuração de LPs é de responsabilidade do **cliente ou dos analistas de implantação**, uma vez que o sistema permite **ajustes e personalizações** conforme as demandas específicas.

Caso você não tenha familiaridade com o **cadastro de LP**, recomendamos que entre em contato com seu Executivo de Soluções de Negócio (ESN) para solicitar a visita de um analista in loco, que poderá avaliar e orientar sobre o seu ambiente de forma mais detalhada.

***Saiba Mais:***

* [**Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como Contabilizar IBS, CBS e IS?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36639180648983-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-Contabilizar-IBS-CBS-e-IS)
* [**Erro\_na\_função\_DETPROVA**](https://tdn.totvs.com/pages/releaseview.action?pageId=243648206)
* [**LP´s para rateio por multi naturezas financeiras**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009301082-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-Lan%C3%A7amentos-Padr%C3%B5es-para-Contabiliza%C3%A7%C3%A3o-do-Rateio-de-Centro-de-Custo-com-M%C3%BAltiplas-Naturezas)
* [**Parâmetros envolvidos no processo de contabilização**](https://tdn.totvs.com/display/public/PROT/SIGACTB+-+Diversos+--+24238)
* [**Saldo tipo 9 na contabilização MV\_PRELAN**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006689172-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA105-Tipo-de-saldo-9-Pr%C3%A9-Lan%C3%A7amento)
* [**HELPs na Contabilização**](https://tdn.totvs.com/pages/releaseview.action?pageId=438288185)
* [**Compartilhamento de Tabelas**](https://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB)
* [**Duplicidade na contabilização**](https://tdn.totvs.com/pages/releaseview.action?pageId=356815352)
* [**Processo Contábil**](https://tdn.totvs.com/pages/viewpage.action?pageId=390416061)
* [**Lançamento\_Padrão\_Do\_Módulo\_Compras\_Rotinas\_MATA103**](http://tdn.totvs.com.br/pages/releaseview.action?pageId=235586200)
* [**Tabelas de utilização para os Lançamentos Padrão de Compras**](https://tdn.totvs.com/pages/releaseview.action?pageId=390416061)
* [**Agendamento da rotina CTBANFE via schedule**](http://tdn.totvs.com.br/display/public/PROT/PCOM07002+-+Agendamento+da+rotina+CTBANFE+via+schedule)
* [**Contabilização no compras utilizando campos do configurador de tributos, tabela F2D**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23337764870295-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Contabiliza%C3%A7%C3%A3o-Compras-utilizando-campos-da-tabela-F2D-do-novo-configurador-de-tributos)
* [**Configurador de tributos**](https://tdn.totvs.com/display/PROT/CFGTRIB+-+Configurador+de+Tributos#CFGTRIBConfiguradordeTributos-CadastrodeRegrasdeC%C3%B3digodePresta%C3%A7%C3%A3odeServi%C3%A7o)
* [**Contabilização dos impostos CBS e IBS**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35707320972439-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Reforma-tribut%C3%A1ria)
* [**Contabilização com base na Sigla do Imposto**](https://tdn.totvs.com/pages/releaseview.action?pageId=977835583)
* [**PÁGINA CENTRALIZADORA COMPRAS**](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [**Artigos Materiais - Compras (SIGACOM)**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
