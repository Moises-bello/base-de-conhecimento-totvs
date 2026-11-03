---
article_id: 4402644962967
category: MDFe - Manifesto de Carga
content_hash: 4db6f890b42b7698f89b762048dde37f147a16ed3747be515147c47437265c9b
fetched_at: '2026-06-28T22:40:08.210308+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE -  Manifesto
  de Carga Nota técnica 2021.002
type: support-article
updated_at: '2025-06-17T18:59:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402644962967-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Manifesto-de-Carga-Nota-t%C3%A9cnica-2021-002
---

**Dúvida**Quais são as atualizações e procedimentos necessários para configuração da NT 2021.002 ?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**  
![MDFe_2021.002.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4402644946711)

Esta Nota Técnica promove ajustes no leiaute do MDF-e do **modal rodoviário adequando o grupo de**  
**informações do vale pedágio** em acordo com a definição da Agência Nacional de Transportes  
Terrestres (ANTT).

Define a **inclusão da chave do PIX** como forma alternativa de recebimento do frete no modal rodoviário  
e no evento de pagamento do frete.

Também promove uma nota explicativa sobre a **regra de validação da duplicidade de chaves de acesso**  
**visando padronizar o entendimento em todos os DF-e.**

E por fim, **o novo padrão de placas do Mercosul** não traz mais no registro do licenciamento a informação da UF de emplacamento do veículo, tornando facultativo o preenchimento desse campo.

* Para acessar a documentação da **solicitação acesse o link:**

*<https://tdn.totvs.com/pages/releaseview.action?pageId=617358319>*

*<https://tdn.totvs.com/pages/releaseview.action?pageId=625151417>*

* **Protheus** realizar atualização do link abaixo, aplicar a **Patch, compile o MDFESEFAZ e DAMDFE:**

RDMAKE: <https://suporte.totvs.com/portal/p/10098/download#detail/1152113>

Protheus 12.1.2310: <https://suporte.totvs.com/portal/p/10098/download?e=1124963>

Protheus 12.1.2410 <https://suporte.totvs.com/portal/p/10098/download?e=1171486>

Atualizar também os**Schemas** (<https://suporte.totvs.com/portal/p/10098/download#detail/761857>) compatível para ambos release.

* **Importante:**

#### As alterações, **nesta Nota técnica** liberadas pelo desenvolvimento:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402638444567)

## **01. Visão Geral**

O projeto MDF-e Integrado tem como objetivo a disponibilização, pelas Secretarias de Fazenda, de uma infraestrutura digital de documentos, legislações e processos voltados para a simplificação da emissão de documentos fiscais eletrônicos de transporte e integração, dentro de um ecossistema digital, que permite às Empresas Transportadoras de Cargas (ETC), Transportadores Autônomos de Cargas (TAC), ANTT, Administradores de Meios de Pagamentos e as próprias Secretarias de Fazenda, o aperfeiçoamento dos seus processos e compartilhamento de informações entre todos estes atores, a partir de um único documento e infraestrutura já consolidada e em uso por todos os envolvidos.

Esta nova NT é obrigatória para modal rodoviário e quando o Tipo Emitente for igual a **Prestador de Serviço de Transporte** (tpEmit=1) ou transportador que emitirá **CT-e globalizado** (tpEmit=3), não sendo obrigatório para **emitentes com frota própria** (tpEmit=2). Caso seja um emitente com frota própria e possuir um **TAC agregado** será possível emitir as informações de pagamento no sistema.

O evento que deverá permitir informar o pagamento do TAC-Agregado ou equiparado a TAC a ocorrer no final do período conforme a relação de viagens realizadas (Exige MDF-e).

## **02. Rotina de Transmissão de evento de Pagamento de Operação de Transporte**

Realizar a transmissão e autorização de uma MDF-e com veículo configurado como TAC Agregado, para isso, basta acessar o módulo **Faturamento (SIGAFAT) / Atualizações / Cadastros / Veículos (OMSA060)**.

Preencher o campo **Frota (DA3\_FROVEI)** com tipo **3 - Agregado** para salvar-lo como TAC agregado.

![](https://tdn.totvs.com/download/attachments/545634768/image2020-3-31_9-48-31.png?version=1&modificationDate=1586291475173&api=v2)

Com MDF-e ja transmitido e autorizado, acessar a rotina de MDF-e (Módulo Faturamento (SIGAFAT) / Atualizações / Nf-e e Nfs-e / MDF-e (SPEDMDFE), após informar os filtros da tela, clicar no botão **Outras Ações / Gerenciar MDFe**.

![](https://tdn.totvs.com/download/attachments/545634768/image2020-3-30_15-10-9.png?version=1&modificationDate=1586291474007&api=v2)

![](https://tdn.totvs.com/download/attachments/545634768/image2020-4-8_8-58-56.png?version=1&modificationDate=1586347136570&api=v2)

Selecionar o MDF-e e clicar no botão **Outras Ações / Eventos**.

![](https://tdn.totvs.com/download/attachments/545634768/image2020-4-8_9-0-21.png?version=1&modificationDate=1586347221150&api=v2)

Na tela de **Monitor de Eventos MDF-e**, selecionar o evento **3- Pagamento Oper. Transporte**.

![](https://tdn.totvs.com/download/attachments/545634768/image2020-4-8_9-3-18.png?version=1&modificationDate=1586347398043&api=v2)

Será apresentada mesma tela de preenchimento das informações de pagamentos presente na rotina de inclusão de MDF-e. Preencher-la de acordo com os dados referente ao(s) pagamento(s) realizado(s) de maneira tardia para este MDF-e, exemplo com dados fictícios:

Informar os campos:

* **Qtd Viagens:** Com a quantidade de viagens deste MDF-e
* **Nr Viagem:** Com o numero da viagem deste MDF-e

No grid **Informações de Pagamento**, serão informados os seguintes dados:

* Nome do Responsável pelo Pagamento;
* CPF ou CNPJ ou Id Estrangeiro do Responsável pelo Pagamento;
* Valor Total do Contrato;
* Forma de pagamento (Á vista ou À Prazo);
* CNPJ da IPEF ou Código do Banco e Código da Agencia.

![](https://tdn.totvs.com/download/attachments/545634768/image2020-4-8_9-24-41.png?version=1&modificationDate=1586348681347&api=v2)

**Importante**: Caso seja preenchido o **CNPJ da IPEF** não será necessário o preenchimento dos campos de **Código do Banco** e **Código da Agência**. Este dois últimos deverão ser preenchidos caso o **CNPJ da IPEF** não for informado.

Para cada linha adicionada no grid de Informações de pagamento serão atualizados e adicionados novos grupos (grid) de **Componentes do Pagamento** e **Parcelas do Pagamento**.

No grid **Componentes do Pagamento**, serão informados os seguintes dados:

* **Tipo do Componente** (1- Vale Pedágio; 2 - Impostos, taxas e contribuições; 3 - Despesas (bancárias, meios de pagamento, outras) / 99 - Outros);
* **Valor do Componente**;
* **Descrição do Componente** (necessário somente quando informado tipo de componente 99 - Outros).

![](https://tdn.totvs.com/download/attachments/545634768/image2020-4-8_9-28-4.png?version=1&modificationDate=1586348884137&api=v2)

No grid **Parcelas do Pagamento**, serão informados os seguintes dados:

* **Número da Parcela;**
* **Valor da Parcela**;
* **Vencimento da Parcela.**

![](https://tdn.totvs.com/download/attachments/545634768/image2020-4-8_9-28-25.png?version=1&modificationDate=1586348905313&api=v2)

**Importante**: Este grid (**Parcelas do Pagamento**) será preenchido somente quando for informado a forma de pagamento **À Prazo** no grid de **Informações de Pagamentos**.

Em seguida, clicar no botão **Transmitir**.

![](https://tdn.totvs.com/download/attachments/545634768/image2020-4-8_9-32-45.png?version=1&modificationDate=1586349165847&api=v2)

Logo após salvar o documento e realizar a transmissão do mesmo, para isso clicar em **Outras ações / Gerenciar MDF-e**.

![](https://tdn.totvs.com/download/attachments/545634768/image2020-4-8_9-34-15.png?version=1&modificationDate=1586349255303&api=v2)

Para atualizar o status do evento, basta clicar no botão **Refresh**.

![](https://tdn.totvs.com/download/attachments/545634768/image2020-4-8_9-34-38.png?version=1&modificationDate=1586349278483&api=v2)

**Operação opcional**: Clicar no botão **Schema** para visualizar o XML do documento com as novas *tags* referentes as informações de pagamentos.

![](https://tdn.totvs.com/download/attachments/545634768/image2020-4-8_9-36-4.png?version=1&modificationDate=1586349364213&api=v2)

Abaixo trecho do XML de evento transmitido:

![](https://tdn.totvs.com/download/attachments/545634768/image2020-4-8_9-38-24.png?version=1&modificationDate=1586349504933&api=v2)

![](https://tdn.totvs.com/download/attachments/545634768/image2020-4-8_9-38-40.png?version=1&modificationDate=1586349520727&api=v2)

**Operação opcional**: Clicar no botão **Mensagem** para detalhar alguns campos a mais referente ao envio do evento.

![](https://tdn.totvs.com/download/attachments/545634768/image2020-4-8_9-35-22.png?version=1&modificationDate=1586349322853&api=v2)

![](https://tdn.totvs.com/download/attachments/545634768/image2020-4-8_9-35-34.png?version=1&modificationDate=1586349334327&api=v2)

Pronto! Foram vinculados ao MDF-e os dados referentes ao pagamento.

## **03. Alterações da Nota Técnica 2021.001**

Foi publicada a Nota Técnica 2021.001 que trata da Adequação do Vale Pedágio e Ajustes nas RVs, com o objetivo de definir a inclusão da chave do PIX como forma alternativa de recebimento do evento de pagamento do frete.

Conforme imagem abaixo, o campo Chave PIX foi inserido na tela do Evento de Pagamento e possui um limite de até 60 caracteres.

Vale salientar que só deverá ser informado o PIX se os campos CNPJ IPEF e Cod. Banco e Cod. Agencia estiverem vazios, caso contrário será levado para o xml respeitando a seguinte prioridade: CNPJ IPEF depois Cod. Banco e Cod. Agencia e por último a Chave PIX.

![](https://tdn.totvs.com/download/attachments/545634768/pix%200.png?version=1&modificationDate=1619126667403&api=v2)

## **04. Alterações da Nota Técnica 2021.002**

Foi publicada a Nota Técnica 2021.002 que trata da Adequação do grupo Pagamento e Ajustes nas RVs, com o objetivo de promover ajustes no leiaute do MDF-e do modal rodoviário e do evento de pagamento

da operação, adequando o grupo de informações do pagamento a prazo do frete e suas respectivas regras de validação, com o objetivo de melhorar a qualidade das informações a serem utilizadas para o lastro de

recebíveis de transportes, a serem operacionalizados por instituições do segmento financeiro e Escrituradores de Duplicatas Escriturais, a partir da Plataforma de Consultas para Antecipações de Recebíveis dos Estados

(PLAC dos Estados).

O campo Valor Adiantamento deve ser preenchido apenas se a Forma de Pagamento for "1-Pagamento à Prazo" .

No Quadro de Parcelas, o Valor Parcela e Vencimento da Parcela passaram a ser obrigatórios no envio do arquivo xml à Sefaz, caso a Forma de Pagamento também seja "1-Pagamento à Prazo" .

![](https://tdn.totvs.com/download/attachments/545634768/vadiant%200.png?version=1&modificationDate=1621023665320&api=v2)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403789364375)

## **01. VISÃO GERAL**

O projeto MDF-e Integrado tem como objetivo a disponibilização, pelas Secretarias de Fazenda, de uma infraestrutura digital de documentos, legislações e processos voltados para a simplificação da emissão de documentos fiscais eletrônicos de transporte e integração, dentro de um ecossistema digital, que permite às Empresas Transportadoras de Cargas (ETC), Transportadores Autônomos de Cargas (TAC), ANTT, Administradores de Meios de Pagamentos e as próprias Secretarias de Fazenda, o aperfeiçoamento dos seus processos e compartilhamento de informações entre todos estes atores, a partir de um único documento e infraestrutura já consolidada e em uso por todos os envolvidos.

Esta Nota Técnica promove ajustes no leiaute do MDF-e do modal rodoviário e do evento de pagamento da operação, adequando o grupo de informações do pagamento a prazo do frete e suas  respectivas regras de validação, com o objetivo de melhorar a qualidade das informações a serem utilizadas para o lastro de recebíveis de transportes, a serem operacionalizados por instituições do segmento financeiro e Escrituradores de Duplicatas Escriturais, a partir da Plataforma de Consultas para Antecipações de Recebíveis dos Estados (PLAC dos Estados).

Esta nova NT é obrigatória para modal rodoviário e quando o Tipo Emitente for igual a **Prestador de Serviço de Transporte** (tpEmit=1) ou transportador que emitirá **CT-e globalizado** (tpEmit=3) ou Transportador Próprio que informou o Tipo de Transportador (tpEmi=2 com tag tpTransp informada), informar:  **Responsável pela Geração do CIOT ou o Responsável pelo pagamento do Vale-pedágio**.

## **02.****Tipos de Transportadores (ETC, TAC ou CTC)**

Neste capitulo iremos abordar uma breve explicação de como configurar os tipos de transportadores: ETC, TAC e CTC contemplados para a rotina de MDF-e (SPEDMDFE) presente no módulo Faturamento (SIGAFAT) do sistema ERP Protheus.

Apenas como definição rápida, os três tipos são:

**ETC** - Empresa de Transporte de Cargas: toda empresa que disponha de veículos que são empregados no transporte de mercadorias e bens (próprios ou cargas de terceiros);

**TAC** - Transportador Autônomo de Cargas: obrigatório para todo e qualquer tipo de autônomo, desde operadores de pequenos caminhões que operam em cidades, até caminhoneiros que dirigem grandes distâncias. Prestando seus serviços para pequenas, médias e grandes transportadora

**CTC**- Cooperativa de Transporte de Cargas: inclui as cooperativas e uniões de condutores que operam no mercado de transporte de mercadorias.

Abaixo é exemplificado como cadastrar cada tipo de transportadora no sistema:

**ETC - Empresa de Transporte de Cargas**

Os campos que diferem para o sistema o tipo de transportadora, neste caso para um ETC, são:

**Frota (DA3\_FROVEI)**: 2 Terceiro ou 3 - Agregado

**Proprietário (DA3\_CODFOR)**: Fornecedor do tipo pessoa física - **Tipo (A2\_TIPO)**: J - Jurídico

![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-20_0-6-46.png?version=1&modificationDate=1624158407177&api=v2)

**Proprietário do veiculo (Fornecedores - SA2) como pessoa jurídica: Tipo (A2\_TIPO)**: J - Jurídico

![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-20_0-9-33.png?version=1&modificationDate=1624158574100&api=v2)

**TAC - Transportador Autônomo de Cargas (Independente e Agregado)**

Os campos que diferem para o sistema o tipo de transportadora, neste caso para um TAC, são:

**Frota (DA3\_FROVEI)**: Caso informado **2 - Terceiro**, neste caso o sistema entenderá como um **TAC Independente**. Caso informado **3 - Agregado**, o sistema entenderá como **TAC Agregado**

**Proprietário (DA3\_CODFOR)**: Fornecedor do tipo pessoa física - **Tipo (A2\_TIPO)**: F - Físico

![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-19_23-45-57.png?version=1&modificationDate=1624158163993&api=v2)

**Proprietário do veiculo (Fornecedores - SA2) como pessoa física: Tipo (A2\_TIPO)**: F - Físico

![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-19_23-49-33.png?version=1&modificationDate=1624158163947&api=v2)

**CTC- Cooperativa de Transporte de Cargas**

Os campos que diferem para o sistema o tipo de transportadora, neste caso para um CTC, são:

**Frota (DA3\_FROVEI)**: 2 - Terceiro ou 3 - Agregado

**Proprietário (DA3\_CODFOR)**: Fornecedor do tipo pessoa física - **Tipo (A2\_TIPO)**: X - Outros

![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-19_23-45-57.png?version=1&modificationDate=1624158163993&api=v2)

**Proprietário do veiculo (Fornecedores - SA2) como pessoa jurídica: Tipo (A2\_TIPO)**: X - Outros

![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-20_0-11-32.png?version=1&modificationDate=1624158692837&api=v2)

## **03. Vale-Pedágio**

Neste capitulo iremos mostrar como é realizado o preenchimento dos campos de Vale Pedágio na rotina de MDF-e (SPEDMDFE) do módulo Faturamento do sistema ERP Protheus.

No módulo Faturamento (SIGAFAT), acessar "Atualizações / NF-e e NFS-e / MDF-e (SPEDMDFE). Informar os filtros e em seguida clicar na operação desejada.

Na aba **Vale-Pedágio** informar os seguintes campos:

* **CNPJ Empresa Fornecedora do Vale-Pedágio:** Informar o CNPJ da empresa fornecedora do vale-pedágio homologada na ANTT.
* **CNPJ/CPF Responsável Pagamento:** Informar o CNPJ ou o CPF do responsável pelo pagamento do vale-pedágio.
* **Número Comprovante de Compra:**Informar o número de ordem do comprovante de compra do Vale-Pedágio fornecido para cada veículo ou combinação veicular, por viagem.
* **Valor do Vale-Pedágio:**Informar o valor do vale-pedágio.
* **Tipo do Vale-Pedágio:**Informar o tipo do vale-pedágio (01 - TAG, 02 - Cupom ou 03 - Cartão).

![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-20_17-8-51.png?version=1&modificationDate=1624219731487&api=v2)

![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-20_17-26-14.png?version=1&modificationDate=1624220774187&api=v2)

Estas informações não são obrigatórias de preenchimento dependendo de sua configuração ou obrigações junto a ANTT. Caso seja necessário, poderão ser informados 1 ou mais vale-pedágios para o MDF-e.

Após informar os campos basta clicar em **Salvar** para gravar as informações do vale-pedágio no MDF-e.

A categoria de combinação Veicular (TAG: **categCombVeic** do XML), é preenchida automaticamente pelo sistema com base na quantidade de eixos informado presente no cadastro do veículo, onde será respeitada a seguinte tabela:

| Numero de Eixos do veículo | Conteúdo da TAG **categCombVeic**do XML |
| --- | --- |
| 2 | 02 |
| 3 | 04 |
| 4 | 06 |
| 5 | 07 |
| 6 | 08 |
| 7 | 10 |
| 8 | 11 |
| 9 | 12 |
| 10 | 13 |
| Maior que 10 | 14 |

Os vale-pedágios são apresentados em DAMDFE após autorização.

![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-21_12-32-17.png?version=1&modificationDate=1624289537543&api=v2)

## **04.****Produto Predominante**

Neste capitulo iremos mostrar como é realizado o preenchimento dos campos de **Produto Predominante** na rotina de MDF-e (SPEDMDFE) do módulo Faturamento do sistema ERP Protheus.

No módulo Faturamento (SIGAFAT), acessar "Atualizações / NF-e e NFS-e / MDF-e (SPEDMDFE). Informar os filtros e em seguida clicar na operação desejada.

Existem dois mecanismos para preenchimento das informações do produto predominante, são eles:

A primeira maneira de preencher os dados do produto predominante é através do campo **Produto** presente na aba **Produto Predominante**. Ao informar o produto serão preenchidos automaticamente os campos **Descrição do produto**, **Código NCM**, **Cód. de Barras (GTIN)**. Os campos **Tipo de Carga**, **CEP Carregamento**, **CEP Descarregamento** não serão preenchidos automaticamente, sendo esses necessário preenchimento manual.

![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-20_17-39-39.png?version=1&modificationDate=1624221580100&api=v2)

A segunda maneira de preenchimento dos dados do produto é através da rotina **Outras Ações / Produto Predominante**, que irá apresentar uma tela de seleção com os 10 produtos com maior quantidade (somatório das quantidades) de todos os produtos dos documentos selecionados na aba **Documentos.** 

**![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-20_17-36-21.png?version=1&modificationDate=1624221381410&api=v2)**

Para escolha dos produtos é realizada o agrupamento dos produtos de todos os documentos selecionados no MDF-e ,em seguida somados os seus valores totais (D1\_TOTAL/D2\_TOTAL) e são apresentados os 10 primeiros que resultam em maior valor para seleção. Caso não seja exibido o item desejado, o mesmo poderá ser informado manualmente como no procedimento anterior.

**![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-21_12-34-24.png?version=1&modificationDate=1624289664963&api=v2)**

**![](https://tdn.totvs.com/download/attachments/625151508/image2021-6-21_12-36-38.png?version=1&modificationDate=1624289798417&api=v2)**

**Critério para exibição dos produtos predominantes com base legal:**

Visando esclarecer a correta identificação do produto predominante no MDF-e em operações de Transporte Rodoviário de Carga Lotação, assim entendida à que corresponda a uma única NF-e ou CT-e, com cargas distintas, o emitente deverá atender o disposto no §2° do art. 4° da [**RESOLUÇÃO ANTT Nº 5.867, DE 14 DE JANEIRO DE 2020**](https://www.in.gov.br/en/web/dou/-/resolucao-n-5.867-de-14-de-janeiro-de-2020-238315084), expedida pela Agência Nacional de Transportes Terrestres – ANTT, nos seguintes dizeres:

*“§2° Para o caso de operações de Transporte Rodoviário de Carga Lotação em que sejam transportadas cargas distintas, sujeitas à classificação em mais de um tipo de carga estabelecida no Anexo II desta Resolução, deverá ser considerada aquela que resulte em maior valor”.*

Abaixo serão detalhados os campos presentes na aba **Produto Predominante**:

* **Produto:** Campos apenas para auxiliar (facilitador) na busca do produto exibindo o cadastro de produto para seleção. **Este campo não é gravado e nem enviado a SEFAZ.**
* **Descrição do produto:** Informar a descrição do produto (caso seja utilizado um dos facilitadores, o campo de origem é a Descrição do Produto - B1\_DESC).
* **Tipo de Carga:** Informar o tipo da carga conforme Resolução ANTT nº. 5.849/2019. 01-Granel sólido; 02-Granel líquido; 03-Frigorificada; 04-Conteinerizada; 05-Carga Geral; 06-Neogranel; 07-Perigosa (granel sólido); 08-Perigosa (granel líquido); 09-Perigosa (carga frigorificada); 10-Perigosa (conteinerizada); 11-Perigosa (carga geral).
* **Código NCM:**Código NCM do produto (caso seja utilizado um dos facilitadores, o campo de origem é a NCM do Produto - B1\_POSIPI).
* **Cód. de barras (GTIN):** Informar o GTIN (Global Trade Item Number) do produto, antigo código EAN ou código de barras (caso seja utilizado um dos facilitadores, o campo de origem é o código de barras do Produto - B1\_CODBAR).
* **CEP de Carregamento:**CEP onde foi carregado o MDF-e. Este campo refere-se a informação da **carga lotação** e deve ser informado somente quando MDF-e for de carga lotação.
* **CEP de Descarregamento:**CEP onde foi descarregado o MDF-e. Este campo refere-se a informação da **carga lotação** e deve ser informado somente quando MDF-e for de carga lotação.

Caso seja selecionado apenas um documento fiscal, obrigatoriamente devem ser informados os campos **CEP de Carregamento** e **CEP de Descarregamento**.

As informações de **produto predominante não são impressas no DAMDFE** padrão do sistema, podendo este ser customizado conforme necessidade do cliente através do RDMake padrão DAMDFE.PRW disponível no portal de downloads da TOTVS.

## **05. TABELAS UTILIZADAS**

* CC0 - Manifesto Documentos Fiscais

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402645191831)**
