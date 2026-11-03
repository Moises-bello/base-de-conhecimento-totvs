---
article_id: 11534575101847
category: PCO - Visões
content_hash: 4ecf662b618b0e79eea0ba3d8b432afa5bce61f65dc9e416fa050425720fdbf5
fetched_at: '2026-06-28T22:37:08.830925+00:00'
product: protheus
section_id: 1500001550982
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAPCO - PCOA170 - Configurações
  da Visão Gerencial para o módulo PCO
type: support-article
updated_at: '2023-01-09T13:05:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11534575101847-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAPCO-PCOA170-Configura%C3%A7%C3%B5es-da-Vis%C3%A3o-Gerencial-para-o-m%C3%B3dulo-PCO
---

**Dúvida**Como configurar a Visão Gerencial para o módulo PCO

**Ambiente**Cross Segmento - Backoffice Linha Protheus -Planejamento e Controle Orçamentário.

#### **Solução:**

Esta rotina define as planilhas e os filtros exibidos nas consultas de visão gerencial e o tipo de operação (soma ou subtração) a ser aplicado aos valores orçados.

**Importante**

Uma configuração sempre deve ser referenciada a uma parametrização.

Neste processo pode ser realizado o cadastramento e criação das contas orçamentárias gerenciais e o conteúdo de cada conta será definido.

A estrutura de contas orçamentárias gerenciais pode conter contas analíticas ou sintéticas, assim como um plano de contas padrão.

Ao definir uma conta gerencial analítica, esta será a conta responsável pela totalização de outras contas, centros de custos ou para as parametrizações que foram determinadas na parametrização da configuração.

O cadastramento de uma configuração é muito similar à inclusão de uma planilha orçamentária, porém as contas que serão cadastradas na visão gerencial são contas que não existem no plano de contas e são pertinentes apenas a esta visão gerencial.

Ao criar uma nova configuração, uma tela com um modelo de árvore é exibido para inclusão e manutenção das contas orçamentárias gerenciais da visão. Utilize a opção **Estrutura** para cadastrar as contas orçamentárias e sua devida hierarquia sintética/analítica.

Também é possível realizar bloqueios por usuário limitando algumas opções da rotina de visão gerencial no PCO, mais detalhes em ->[Visão gerencial (PCOA210\_3 - SIGAPCO)](https://tdn.totvs.com/pages/viewpage.action?pageId=312175376).

#### **EXEMPLO DE UTILIZAÇÃO**

Criação de visões departamentais, consolidando as contas pertencentes a um determinado centro de custo ou consolidar várias planilhas em uma única visão.

Somente são executadas consultas com configuração padrão (incluídas automaticamente pelo Sistema), cujo filtro refere-se à planilhas com o mesmo tipo e período informado.

Ao entrar na rotina é apresentado a tela com as seguintes opções:

**Incluir / Alterar / Visualizar / Outras Ações**

![](https://tdn.totvs.com/download/attachments/667355455/image2022-2-15_17-35-36.png?version=1&modificationDate=1644957337307&api=v2)

Para Incluir uma configuração, clique em **Incluir** e informe os dados de acordo conforme orientação dos helps de campo, confira os campos e clique em **Salvar**.

**Observação:**Após o preenchimento do campo ***Configuração,***e confirmação da inclusão, este campo não poderá mais ser alterado.

![](https://tdn.totvs.com/download/attachments/667355455/image2022-2-15_17-45-26.png?version=1&modificationDate=1644957926847&api=v2)

**Campos a serem preenchidos:**

**Código:** Código da visão gerencial orçamentária.

**Descrição:** Descrição da visão gerencial orçamentária.

**Nível Max.:** Quantidade de níveis que serão abertos inicialmente na visualização da planilha orçamentária.

**Configuração:** Código da configuração que será utilizado para definição dos filtros da visão gerencial orçamentária. (Acessar a rotina[PCOA160](https://tdn.totvs.com/pages/viewpage.action?pageId=312175426))

**Memo:** Observações da visão gerencial.

Será aberta a tela para cadastro dos níveis da visão gerencial, posicione na segunda linha, vá em **outras ações >> Estrut. >> Incluir C.O.G**

![](https://tdn.totvs.com/download/attachments/667355455/image2022-2-15_18-7-19.png?version=1&modificationDate=1644959240697&api=v2)

Irá abrir a tela para cadastro das contas da visão gerencial, onde as sintéticas ficarão um nível acima das contas analíticas.

Na aba **Conta Orc. Gerencial**

**C.Orc.Ger. :**Preencher com o código da conta orçamentária que será representada na visão gerencial.

**Descrição:** Descrição da conta

![](https://tdn.totvs.com/download/attachments/667355455/image2022-2-15_18-25-49.png?version=1&modificationDate=1644960351840&api=v2)

Na aba **Características C.O.G:**

**Classe:** Indicador se conta será analítica ou sintética.

**Cond.Normal:**Determina se conta orçamentária será credora ou devedora.

**Ordem:** Indica a ordem das contas orçamentarias gerenciais utilizadas nas visões gerenciais.

**Carac.Impr.:** Indica qual o identificador de impressão para relatórios de visão gerencial.

![](https://tdn.totvs.com/download/attachments/667355455/image2022-2-16_10-27-22.png?version=1&modificationDate=1645018043693&api=v2)

Na aba **Outros**tem somente o campo nível que já vem preenchido e não é permitido a alteração.

Após clicar em **Salvar**, será possível editar o grid que filtrará os itens.

Basta posicionar na conta criada e clicar em **Editar**.

Observação: Os campos de cadastro já vem preenchido com um range aberto, ou seja, de branco a 'ZZZZZ'.

**Principais campos:**

**Operação:** Indica se item orçamentário será somado ou subtraído na execução da visão gerencial orçamentária.

**Função:**Poderá ser utilizado para manipular o valor do item orçamentário (variável nValor) por formula ou função de usuário na execução da visão gerencial orçamentaria. [Exemplo.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018804431-MP-SIGAPCO-O-campo-AKP-FORMUL-utilizado-no-cadastro-de-vis%C3%B5es-gerenciais-or%C3%A7ament%C3%A1rias-pode-ser-usado-com-RDMAKES-ou-com-f%C3%B3rmulas-simples-)

**Apl.Filt.:**Indica se aplica o filtro para tabela Classificadores Receita/Despesa.

**Planilha Orct.:** Busca o código da Planilha orçamentária na tabela AK1

**Versão:**Versão da planilha que foi selecionada no campo **Planilha Orct.**

![](https://tdn.totvs.com/download/attachments/667355455/image2022-2-16_10-51-58.png?version=1&modificationDate=1645019519003&api=v2)

Seguindo os mesmos passos acima para configuração de conta da visão, tanto para analíticas quanto para as sintéticas.

Importante !!

**Obs:** E diferentemente da [Visão gerencial (CTBA161)](https://tdn.totvs.com/pages/viewpage.action?pageId=6068435)do módulo Contabilidade Gerencial (SIGACTB), onde é possível fazer a exportação e importação de um arquivo .cve, a visão gerencial do módulo Planejamento e Controle Orçamentário (SIGAPCO) deve ser criada e configurada manualmente.

#### **UTILIZANDO UMA VISÃO**

Importante

É preciso ter um cubo previamente configurado.

**A. Cadastrar um parametrização:**

Em **Atualizações >> Visões >> Parâmetros (PCOA160):**

**Observação:**Ao digitar o código do cubo, vá em outras ações e clique em***Cpo/Cubo***para trazer as configurações do Cubo.

![](https://tdn.totvs.com/download/attachments/667355455/image2022-2-16_17-2-49.png?version=1&modificationDate=1645041770300&api=v2)

**B. Fazer a configuração de uma visão**

Em**Atualizações >> Visões >> Configurações (PCOA170):**

**Selecione a parametrização cadastrada anteriormente.**

**![](https://tdn.totvs.com/download/attachments/667355455/image2022-2-16_17-20-58.png?version=1&modificationDate=1645042861680&api=v2)**

Incluir as contas sintéticas e analíticas conforme sua preferência, nesse exemplo tem três sintéticas e duas analíticas.

Foram previamente cadastradas as contas orçamentárias em**Atualizações >> Cadastros >> Contas Orçamentárias (PCOA010):**

![](https://tdn.totvs.com/download/attachments/667355455/image2022-2-16_17-45-48.png?version=1&modificationDate=1645044351013&api=v2)

Incluindo a conta sintética da visão gerencial orçamentaria, em**Atualizações >> Visões >> Configurações (PCOA170):**:

![](https://tdn.totvs.com/download/attachments/667355455/image2022-2-17_14-25-23.png?version=1&modificationDate=1645118724333&api=v2)

Logo em seguida, posicionando na conta sintética incluo a conta analítica:

**Observação:** Essa conta analítica será a conta filha da conta sintética acima.

Estão destacadas os códigos das contas que será o range dessa conta na visão gerencial orçamentária.

![](https://tdn.totvs.com/download/attachments/667355455/image2022-2-17_14-28-36.png?version=1&modificationDate=1645118917560&api=v2)

Seguindo os passos anteriores, segue a visão gerencial orçamentária completa.

![](https://tdn.totvs.com/download/attachments/667355455/image2022-2-17_14-32-29.png?version=1&modificationDate=1645119150677&api=v2)

**C. Utilizando uma consulta conforme a visão gerencial orçamentária cadastrada**

Ter lançamentos com saldos orçados e realizados cadastrados no período para melhor visualização da consulta.

Nesse exemplo foram lançados, conferir em**Atualizações >> Movimentos >> Lançamentos (PCOA050):**

![](https://tdn.totvs.com/download/attachments/667355455/image2022-2-17_10-50-51.png?version=1&modificationDate=1645105853937&api=v2)

Usando a rotina de consultas de saldos por período, em**Consultas >> Visões >> Saldos por Período (PCOC360)**

**![](https://tdn.totvs.com/download/attachments/667355455/image2022-2-16_17-56-30.png?version=1&modificationDate=1645044991400&api=v2)**

**Preencha os parâmetros conforme período desejado:**

**![](https://tdn.totvs.com/download/attachments/667355455/image2022-2-16_17-58-35.png?version=1&modificationDate=1645045118707&api=v2)**

**![](https://tdn.totvs.com/download/attachments/667355455/image2022-2-16_17-59-13.png?version=1&modificationDate=1645045157403&api=v2)**

**![](https://tdn.totvs.com/download/attachments/667355455/image2022-2-16_18-0-27.png?version=1&modificationDate=1645045230400&api=v2)**

Após confirmar, será aberto a consulta:

Os destaques na figura, é para o nome da visão, as contas cadastradas na configuração e o valor do saldo no período, conforme lançamentos usado nesse exemplo.

![](https://tdn.totvs.com/download/attachments/667355455/image2022-2-17_14-35-16.png?version=1&modificationDate=1645119317517&api=v2)

## 

#### **CAMPOS e PARÂMETROS**

**Principais Ajustes de Campos e Parâmetros**

**AKN - Visão Gerencial Orçamentária**

| Campo | Descrição |
| --- | --- |

| AKN\_FILIAL | Filial do Sistema |
| AKN\_CODIGO | Código da Planilha Orçamentária |
| AKN\_DESCRI | Descricão da Visão Gerencial Orçamentária |
| AKN\_NMAX | Nível Máximo |
| AKN\_CONFIG | Configuração |
| AKN\_MEMO | Memo |

**AKO - Conta Gerencial Orçamentária**

| Campo | Descrição |
| --- | --- |

| AKO\_FILIAL | Filial do Sistema |
| AKO\_NIVEL | Nível |
| AKO\_CODIGO | Código da Visão Gerencial |
| AKO\_CO | Conta Orçamentária Gerencial |
| AKO\_COPAI | Conta Gerencial Superior |
| AKO\_DESCRI | Descrição |
| AKO\_CLASSE | Classe |
| AKO\_CONNOR | Condição Normal |
| AKO\_ORDEM | Ordem |
| AKO\_IDTIMP | Característica Impressão |

**AKP - Filtro Conta Gerencial Orçamentária**

| Campo | Descrição |
| --- | --- |
| Campo | Descrição |
| --- | --- |

| AKP\_FILIAL | Filial do Sistema |
| AKP\_CODIGO | Código da Visão Gerencial |
| AKP\_ITEM | Item |
| AKP\_CO | Conta Orçamentária Gerencial |
| AKP\_CONFIG | Configuração |
| AKP\_ITECFG | Item Configuração |
| AKP\_TIPO | Tipo |
| AKP\_VALINI | Valor Padrão Inicial |
| AKP\_VALFIM | Valor Padrão Final |
| AKP\_OPERAC | Operação |
| AKP\_FORMUL | Função |
| AKP\_FILTCL | Aplica Filtro |

## 

#### **TABELAS UTILIZADAS**

* AKN → Visão Gerencial Orçamentária
* AKO → Conta Gerencial Orçamentária
* AKP → Filtro Conta Gerencial Orçamentária

**Saiba mais:**

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Principais parâmetros do módulo PCO - Principais parâmetros do módulo PCO - Planejamento e Controle Orçamentário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017496452-MP-SIGACOM-Principais-par%C3%A2metros-do-m%C3%B3dulo-PCO-?source=search)

[Controladoria - PCO - Protheus 12](https://tdn.totvs.com/display/public/PROT/Controladoria+-+PCO+-+Protheus+12)

[Cross Segmento - Backoffice Linha Protheus - SIGAPCO - CheckList para utilização do modulo Planejamento de Custos Orçamentários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038998854-MP-SIGAPCO-CheckList-para-utiliza%C3%A7%C3%A3o-do-modulo-Planejamento-de-Custos-Or%C3%A7ament%C3%A1rios)

[Importação dados para planilha orçamentária via arquivo xml](https://tdn.totvs.com/pages/releaseview.action?pageId=439706297)
