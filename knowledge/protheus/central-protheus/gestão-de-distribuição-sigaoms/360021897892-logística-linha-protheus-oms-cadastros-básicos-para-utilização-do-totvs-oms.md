---
article_id: 360021897892
category: Gestão de Distribuição (SIGAOMS)
content_hash: 80f0d7dac1c156e04910ab5cb71a7707ed674800b559830ba8383bbd6e6108c0
fetched_at: '2026-06-28T22:45:49.565119+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Cadastros Básicos para utilização do TOTVS
  OMS
type: support-article
updated_at: '2024-03-21T12:14:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021897892-Log%C3%ADstica-Linha-Protheus-OMS-Cadastros-B%C3%A1sicos-para-utiliza%C3%A7%C3%A3o-do-TOTVS-OMS
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura:**00:05:18 min  
  
Dúvida**Quais são os **Cadastros Básicos** para utilização do **TOTVS OMS**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Os cadastros básicos para utilização do **TOTVS OMS****- Order Management System** são:  
  
**Cadastros:**Clientes - **MATA030 - SA1**  
Fornecedores - **MATA020 - SA2**  
Produtos - **MATA010 - SB1**  
Complemento de Produtos - **MATA180 - SB5**   
Transportadoras - **MATA050 - SA4**  
**TES Tipos de Entrada e Saída** - **MATA080 - SF4**  
Condição de Pagamento - **MATA360 - SE4**  
  
No **cadastro de Produtos**, vincular o **Tipo da Carga** ao produto no campo **Tipo Carga - B1\_TIPCAR**.  
  
No **cadastro de TES Tipos de Entrada e Saída**, preencher os campos:   
**Gera Duplicata - F4\_DUPLIC**, preencher com **sim** para geração do titulo no financeiro, após a emissão de uma **Nota Fiscal de Saída**.  
**TES. Devol - F4\_TESDV**, preencher o código da **TES** de entrada que será utilizada para os casos de Devolução na rotina **Retorno de Cargas - OMSA320**.  
  
**Logística:**  
Grupo de Veículos - **OMSA110 - DAC**  
Tipos de Veículos - **TMSA530 - DUT**  
Veículos - **OMSA060 - DA3**  
Motoristas - **OMSA040 - DA4**  
Ajudantes - **OMSA050 - DAU**  
Modelos de Carga - **OMSA180 - DBO**  
  
O **cadastro de Grupos de Veículos** permite criar um registro para agrupamento da frota de acordo com determinadas características. Exemplo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103464073/mceclip2.png)

O **cadastro de Tipos de Veículos**, permite registrar todos os **Tipos de Veículos** utilizados pelo distribuidor.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101309734/mceclip3.png)

O **Cadastro Veículos** é utilizado para registrar as características dos veículos que serão utilizadas na geração das cargas, tais como **Capacidade e Volume**, e onde informa-se a **placa**, que posteriormente é gravada nas notas fiscais de saída. Além disso, é por meio deste cadastro que realiza-se a **associação do veículo a um Tipo ou um Grupo de Veículos.**  
  
Os **cadastro de Motoristas  e Ajudantes**, são utilizadas para registrar as informações dos Motoristas e dos Ajudantes. No cadastro de Motoristas é possível indicar o **código de Fornecedor do motorista**, para que possam ser **gerados os débitos contra ele no momento do acerto financeiro da carga**.  
No caso dos Ajudantes, é possível realizar a **associação de um ou mais ajudantes à carga**, no momento de sua geração, porém a informação é apenas de **caráter informativo**.  
  
O **cadastro de Modelos de Carga** disponibiliza um recurso extra para filtragem dos pedidos e produtos que serão alocados em uma carga. Neste sentido, é possível que sejam montadas **cargas exclusivas para produtos secos, produtos químicos ou perecíveis,** permitindo assim o direcionamento delas a veículos especiais de acordo com o modelo de carga selecionado.  
O **Modelo de Carga deve estar vinculado a um Tipo de Carga**, correspondente a um registro da **tabela DU**, do arquivo de **Tabelas Genéricas - SX5.**  
Para que o filtro seja efetivo no momento da montagem das cargas, é necessário vincular um **Modelo de Carga** ao cadastro de cada um dos **Produtos** a serem distribuídos, informado no campo **B1\_TIPCAR**.  
  
**Roteirização**Consiste em configurar a logística de entregas, possuindo as seguintes características:

* Cadastramento de frota de veículos para entrega;
* Determinar a localização dos clientes;
* Estabelecer datas e horários de recebimento.

Zonas - **OMSA070 - DA5**Setores por Zona - **OMSA080 - DA6**Pontos por Setor - **OMSA090 - DA7**Rota - **OMSA100 - DA8**Calendário - **OMSA350 - DAA - DAB**  
  
O **cadastro de Zonas** nada mais é do que um local, uma região ou uma área delimitada, que engloba um conjunto de clientes. Este cadastro tem como objetivo armazenar todas as zonas atendidas pelo distribuidor, sendo um cadastro base para composição das rotas, montagem das cargas e, consequentemente, das sequências de entrega. Exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103368673/mceclip0.png)

O **cadastro de Setores** **por Zona** caracterizam-se por subdivisões existentes dentro de uma mesma Zona. Por exemplo, tendo a cidade de São Paulo como uma determinada Zona, poderíamos dividi-la nos seguintes setores:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002367421/mceclip1.png)

O **cadastro de Pontos por Setor** são referências existentes dentro de um dado Setor e permitem que seja definida a sequência de entrega da Rota, que pode ser por Cliente ou por Faixa de CEP. Exemplo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101206234/mceclip2.png)

O **cadastro de Rotas** permite elaborar as rotas de entrega previstas pelo distribuidor, ordenando as Zonas e Setores na ordem desejada. Exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002456661/mceclip0.png)

O **cadastro de Calendário**, é utilizado devido  algumas particularidades nas operações de clientes e transportadores, existem casos nos quais as entregas só podem ser realizadas em um determinado período do mês ou da semana. Para tratar esse tipo de situações existe o cadastro de Calendários, que define janelas de entrega para a **Rota**, **Zona** ou **Setor**. Exemplo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103463853/mceclip1.png)
