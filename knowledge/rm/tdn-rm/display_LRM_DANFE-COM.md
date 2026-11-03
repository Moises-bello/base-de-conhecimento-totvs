---
content_hash: 104c4d99ac3d4265de4bfa079b8953e7048f5f8c5c7f1f0b8d30ab2f93ae8241
fetched_at: '2026-06-29T00:12:16.506663+00:00'
page_id: '990764154'
product: rm
source: tdn-rm
title: DANFE-COM
type: documentation
url: https://tdn.totvs.com/display/LRM/DANFE-COM
version: 121
---

**Para **Impressão Múltipla,**deve ser realizado o salvamento em PDF:2Conteúdonone**

# 1. Visão Geral

O Documento Auxiliar da Nota Fiscal de Comunicação Eletrônica (DANFE-COM) é a representação gráfica simplificada da NFCom. Sua finalidade é permitir a conferência das informações básicas do documento fiscal eletrônico, além de servir como instrumento de entrega ao consumidor dos serviços de telecomunicações.

É importante destacar que o DANFE-COM **não substitui a NFCom** e **não possui validade jurídica por si só**, sendo apenas uma representação para consulta e apoio operacional. A validade legal permanece vinculada ao arquivo eletrônico da NFCom (xml), devidamente autorizado pela SEFAZ.

Conforme definido no manual, **no DANFE-COM não devem ser inseridas informações que não constem do respectivo arquivo XML da NFCom, exceto o protocolo de autorização da NFCom**. Essa regra assegura a integridade dos dados, garantindo que as informações impressas estejam em conformidade com o documento fiscal autorizado eletronicamente.

# 2. Configurações iniciais

Para acessar o processo Eventos, no menu *Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom)*, é necessário fornecer a permissão conforme abaixo:

ConfigPermissões Usuários

Para dar permissão de acesso ao menu da NFCom a um usuário, siga os passos abaixo:

* Acesse o perfil vinculado ao usuário desejado do módulo TOTVS Gestão de Estoque, Compras e Faturamento e edite o perfil;
* Vá até a aba **Acesso a Menus**, siga o caminho **[*04] Vendas | [04.02] Documentos Eletrônicos***, selecione **[04.02.01.07] Nota Fiscal de Comunicação Eletrônica (NFCom), [04.02.01.07.05] Imprimir DANFE** e logo após, clique em **Permitir Acesso**.

Segurança - Acesso - Perfis

# 3. SMART VIEW

A impressão do **DANFE-COM** é realizada por meio do [SMART VIEW](https://tdn.totvs.com/display/TREP/SMART+VIEW). Para instalar e configurar o SMART VIEW, consulte o guia oficial disponível em:

smart\_viewTipo relatório DANFE-Com

É necessário executar o RM Atualizador. Ao executá-lo será criado o tipo "**332 - DANFE NFCom**" nos recursos do SMART VIEW, este tipo é necessário para a correta importação do relatório DANFE-Com.

Compartilhamento de Recursos Smart View

Durante o fluxo de uso de um recurso Smart View, é necessário o gerenciamento dos níveis de permissões dos usuários que acessarão os recursos. Na documentação abaixo você encontrará uma explicação detalhada sobre como gerenciar o acesso aos seus recursos.

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/16106157353623-Cross-Segmentos-Backoffice-RM-BI-Compartilhamento-de-recursos-no-Smart-View-Categoria>

Caso o cadastro da categoria não seja feito corretamente ou o perfil do usuário não estiver vinculado à categoria ao tentar visualizar ou salvar o relatório será exibida uma mensagem de erro com o seguinte texto: "Usuário não possui permissões de uso ao recurso".

# 4. Processo Imprimir DANFE-COM

O relatório **DANFE-COM** pode ser obtido diretamente no [TOTVS Compartilhamento](https://tdn.totvs.com/pages/viewpage.action?pageId=348297816), sendo sua impressão realizada pelo processo **Imprimir DANFE (SmartView)**.

TOTVS Compartilhamento

* NUCREL00001 - DANFE-COM - 1.00 - Retrato

O processo poderá ser executado apenas para NFCom com um dos status abaixo:

* **Não** **Transmitido:** Neste caso o DANFE será impresso com a mensagem "NOTA AINDA NÃO AUTORIZADA - SEM VALOR FISCAL". Este tipo de impressão é para permitir a visualização do relatório antes de autorizar a nota;
* **Autorizado:** Com este status o DANFE-COM pode ser impresso na versão oficial para ser enviado ao cliente;
* **Demais status:** O processo apresentará a validação: "**A DANFE só poderá ser emitida se a Nota estiver Autorizada**".

O relatório pode ser gerado conforme opções abaixo

Tipos de impressãoVisualização#002233dashed

No processo **Imprimir DANFE-COM**, o recurso **SmartView** já é carregado com os dados preenchidos.

Temos o tipo de geração "**Visualiza Impressão"**:

Nesta etapa basta clicar em **Enviar,** que veremos a execução do recurso **SmartView** exibindo o DANFE-COM para visualização:

Para o tipo de geração "**Visualizar Impressão**", só é possível realizar a impressão individual.

Impressão#002233dashed

Para imprimir a partir da Visualização basta clicar no ícone de impressão conforme destacado abaixo e selecionar a impressora de destino:

A impressão também pode ser feita após selecionar o Tipo de Geração "**Salvar em PDF**" e mandar o arquivo gerado para impressora.

Salvar em Arquivo PDF#002233dashed

O tipo de geração “**Salvar em PDF**” armazena o arquivo no diretório selecionado, utilizando como nome o **chave de acesso da nota**, seguido da extensão “**.PDF**”.  
Exemplo: 35251099999999000191620050000000261020027989.PDF

#002233dashed

O tipo de geração "**Visualizar Impressão**", também permite exportar o DANFE-COM em formato PDF:

Impressão de múltiplas NFCom

Para **Impressão Múltipla,** deve ser realizado o salvamento em formato PDF:

Após a geração dos arquivos, basta enviá-los para impressão:

# 5. Detalhamento Relatório DANFE-COM

Todas as informações apresentadas no DANFE-COM são extraídas do **arquivo XML da NFCom**. Nenhum dado será considerado a partir de cadastros internos do sistema, evitando divergências entre o arquivo XML e a sua representação impressa.

Impressão Relatório DANFE-COM#002233dashed

### DANFE-COM

400

A seguir, são detalhadas as divisões que compõem o DANFE-COM:

## 5.1 Divisão I - Informações do Cabeçalho: Dados do Emitente

O cabeçalho deverá indicar obrigatoriamente os dados do emitente da NFCom, contendo as seguintes informações:

Dados Emitente#002233dashed

### DANFE-COM - Dados Emitente

#002233dashed

### Campos NFCom

| Nomes | Tipos | Campos Xml |
| --- | --- | --- |
| Razão Social do Emitente | Literal | emit.xNome |
| CNPJ/CPF | Literal | emit.CNPJ.emit.CPF |
| Inscrição Estadual | Literal | emit.IE |
| **Endereço Completo Emitente** | | |
| Logradouro | Literal | enderDest.xLgr |
| Número | Literal | enderDest.nro |
| Complemento | Literal | enderDest.xCpl |
| Bairro | Literal | enderDest.xBairro |
| Nome do Município | Literal | enderDest.xMun |
| CEP | Literal | enderDest.CEP |
| Sigla da UF | Literal | enderDest.UF |
| Telefone | Literal | enderDest.fone |

## 5.2 Divisão II – Informações do Assinante / Destinatário

Local onde deverá ser impressas as informações do destinatário/assinante da NFCom:

Dados Destinatário / Assinante#002233dashed

### DANFE-COM - Assinante / Destinatário

#002233dashed

### Campos NFCom

| Nomes | Tipo | Campos Xml |
| --- | --- | --- |
| Razão Social | Literal | dest.xNome |
| CNPJ / CPF | Literal | dest.CNPJ/dest.CPF |
| Inscrição Estadual | Literal | dest.IE |
| Telefone | Literal | enderDest.fone |
| Código do Cliente | Literal | assinante.iCodAssinante |
| Referência | Data | gFat.CompetFat |
| Vencimento | Data | gFat.dVencFat |
| Total a Pagar | Decimal | total.vNF |
| **Endereço Completo Destinatário / Assinante** | | |
| Logradouro | Literal | enderDest.xLgr |
| Número | Literal | enderDest.nro |
| Complemento | Literal | enderDest.xCpl |
| Bairro | Literal | enderDest.xBairro |
| CEP | Literal | enderDest.CEP |
| Nome do Município | Literal | enderDest.xMun |
| Sigla da UF | Literal | enderDest.UF |

## 5.3 Divisão III – Informações de Identificação da NFCom e do Protocolo de Autorização

Informações de identificação da NFCom:

Identificações da NFCom#002233dashed

### DANFE-COM - Identificação da NFCom

#002233dashed

### Campos NFCom

| Nomes | Tipo | Campos Xml |
| --- | --- | --- |
| Número da NFCom | Literal | ide.nNF |
| Série da NFCom | Literal | ide.serie |
| Data de Emissão | Data | ide.dhEmi |
| Chave de Acesso | Literal | infNFCom - Atributo=Id |
| Protocolo de Autorização | Literal | infProt.nProt |
| Data e Hora da Transmissão | Literal | infProt.dhRecbto |

## 5.4 Divisão IV – Informações dos itens do DANFE-COM

Local onde será apresentado a lista de produtos e serviços:

Informações do Item#002233dashed

### DANFE-COM - Informações do Item

#002233dashed

### Campos NFCom

| Nomes | Tipo | Campos Xml | Observções |
| --- | --- | --- | --- |
| Itens da Fatura | Decimal | prod.xProd | Se o item possuir o indicador de devolução (prod.indDevolucao) deverá ser adicionado na descrição o literal “Devolução” entre parênteses. |
| Unidade | Decimal | prod.uMed |  |
| Quantidade | Decimal | prod.qFaturada |  |
| Preço Unitário | Decimal | prod.vItem |  |
| Valor Total | Decimal | prod.vProd |  |
| PIS/COFINS | Decimal | (PIS.vPIS + COFINS.vCOFINS) |  |
| Base de Cálculo ICMS | Decimal | vBC | A tag vBC estará presente nos ICMS's com CST's 00, 20 e 90 |
| Alíquota | Decimal | (pICMS + pFCP) | A tag pICMS estará presente nos ICMS's com CST's 00, 20 e 90  A tag pFCP estará presente nos ICMS's com CST's 00 e 20 |
| Valor do ICMS | Decimal | (vICMS + vFCP) | A tag vICMS estará presente nos ICMS's com CST's 00, 20 e 90  A tag vFCP estará presente nos ICMS's com CST's 00 e 20 |

## 5.5 Divisão V – Informações dos Tributos

Local destinado à exibição dos valores totais dos tributos que serão impressos no DANFE-COM:

Informações dos Tributos#002233dashed

### DANFE-COM - Informações dos Tributos

#002233dashed

### Campos NFCom

| Nome | Tipo | Campos Xml | Observação |
| --- | --- | --- | --- |
| VALOR TOTAL NNF | Decimal | total.vNF |  |
| TOTAL BASE DE CALCULO | Decimal | imposto.ICMS.vBC |  |
| VALOR ICMS | Decimal | imposto.ICMS.vICMS | Quando for os CTS's - 00 ou 20 utilizará o valor da base de cálculo. |
| VALOR ISENTO | Decimal | prod.vProd | Quando for os CTS's - 40 ou 51 utilizará o valor do produto. |
| VALOR OUTROS | Decimal | imposto.ICMS.vICMS | Quando for o CTS - 90 utilizará o valor da base de cálculo. |
| PIS | Decimal | imposto.PIS.vPIS |  |
| COFINS | Decimal | imposto.COFINS.vCOFINS |  |
| FUST | Decimal | imposto.FUST.vFUST |  |
| FUNTTEL | Decimal | imposto.FUNTTEL.vFUNTTEL |  |
| Valor PISRF | Decimal | imposto.retTrib.vRetPIS | Disponível no Objeto de Negócio, mas não adicionado no relatório. |
| Valor COFINSRF | Decimal | imposto.retTrib.vRetCofins | Disponível no Objeto de Negócio, mas não adicionado no relatório. |
| Valor CSLLRF | Decimal | imposto.retTrib.vRetCSLL | Disponível no Objeto de Negócio, mas não adicionado no relatório. |
| BC IRRF | Decimal | imposto.retTrib.vBCIRRF | Disponível no Objeto de Negócio, mas não adicionado no relatório. |
| Valor IRRF | Decimal | imposto.retTrib.vIRRF | Disponível no Objeto de Negócio, mas não adicionado no relatório. |

## 5.6 Divisão VI – Área de Mensagem Fiscal

Área destinada à impressão de mensagens de interesse fiscal contida no arquivo eletrônico da NFCom:

Mensagem Fiscal#002233dashed

### DANFE-COM - Reservado ao Fisco

No caso de notas não autorizadas, será exibida a seguinte mensagem:

#002233dashed

### Campo NFCom

| Nome | Tipo | Campo Xml |
| --- | --- | --- |
| RESERVADO AO FISCO | Literal | infAdic.infAdFisco |

## 5.7 Divisão VII – Mensagem de Interesse do Contribuinte - QrCode PIX

Área destinada à impressão de mensagens de interesse do contribuinte contidas no arquivo eletrônico da NFCom:

Interesse do Contribuinte#002233dashed

### DANFE-COM - Informações Complementares

### DANFE-COM - QrCode PIX

#002233dashed

### Campo NFCom

| Nome | Tipo | Campo Xml | Observação |
| --- | --- | --- | --- |
| INFORMAÇÕES COMPLEMENTARES | Literal | infAdic.infCpl |  |
| QrCode PIX | Literal | gFat.gPIX.urlQRCodePIX | O QrCode será exibido quando a tag "urlQRCodePIX" do xml estiver preenchida.  O serviço utilizado pelo Nucleus para gerar automaticamente o QRCodePIX, porém é necessário ter o TOTVS Techfin.  **[Grupo de Informações d](https://tdn.totvs.com/pages/viewpage.action?pageId=901956138)[o PIX](https://tdn.totvs.com/pages/viewpage.action?pageId=901957732)** |

## 5.8 Divisão VIII – Código de Barras - Fatura/Pagamento

Código de Barras#002233dashed

### DANFE-COM - Código de Barra

#002233dashed

### Campo NFCom

| Nome | Tipo | Campo Xml | Observação |
| --- | --- | --- | --- |
| CODIGO DE BARRAS - FATURA/PAGAMENTO | Literal | gFat.codBarras | Para os clientes que não possuem o TOTVS Techfin, o campo será preenchido com zeros ou noves.  **[Grupo de Informações de Controle da Fatura](https://tdn.totvs.com/pages/viewpage.action?pageId=901956138)** |
