---
article_id: 360053742193
category: NFe - Nota Fiscal Eletrônica
content_hash: 9011c9fa41d0cc2f26a1e51f92745a915b0e956d1373498efe021eff128a8586
fetched_at: '2026-06-28T22:40:07.219828+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Impressão DANFE Etiqueta
type: support-article
updated_at: '2024-09-06T17:40:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053742193-Cross-Segmentos-Backoffice-Protheus-Impress%C3%A3o-DANFE-Etiqueta
---

**Dúvida**Como realizar a impressão do Danfe Etiqueta?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe

Cross Segmentos - TSS

**Solução**

Foi publicada pela a NT 2020.004 DANFE Simplificado - Etiqueta, pois com o avanço do comércio eletrônico, surgiu a necessidade de simplificar o processo de impressão do Documento Auxiliar da Nota Fiscal Eletrônica.

A impressão do DANFE Simplificado – Etiqueta, possível de ser utilizado pelos contribuintes nas operações de venda a varejo para consumidor final em comércio eletrônico, venda por telemarketing ou processos semelhantes, ocorrerá seguindo os padrões técnicos estabelecidos na Nota Técnica, atendendo ao disposto no §5º-A da cláusula nona do Ajuste SINIEF 07/05.

Para a criação da consulta padrão (SXB) devemos acessar o módulo **Configurador (SIGACFG)**, em **Base de dados / Dicionário / Bases de Dados**. Clicar na opção **Consultas Padrão** e logo em seguida no botão **Incluir**.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-25_21-2-55.png?version=1&modificationDate=1624665775537&api=v2)

Informar os seguintes campos e clicar em **Avançar**.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-25_21-3-48.png?version=1&modificationDate=1624665828597&api=v2)

Selecionar a tabela **CB5** e clicar em **Avançar**.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-25_21-4-4.png?version=1&modificationDate=1624665845003&api=v2)

Clicar no botão **Adicionar Índice**.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-25_21-4-34.png?version=1&modificationDate=1624665875090&api=v2)

Selecionar o primeiro índice e clicar em **Confirmar**.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-25_21-5-38.png?version=1&modificationDate=1624665938947&api=v2)

Clicar no botão **Incluir** campos na colunas.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-25_21-5-58.png?version=1&modificationDate=1624665958447&api=v2)

Selecionar o campo **CB5\_CODIGO** clicando no botão conforme imagem abaixo.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-25_21-6-40.png?version=1&modificationDate=1624666001117&api=v2)

Clicar em **Confirmar** para gravar o campo.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-25_21-7-42.png?version=1&modificationDate=1624666062640&api=v2)

Realizar procedimento de inclusão de campos na coluna (procedimento anteriores) para os demais campos:

**CB5\_DESCRI**

**CB5\_MODELO**

Em seguida clicar em **Avançar**.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-25_21-10-20.png?version=1&modificationDate=1624666220980&api=v2)

Clicar no botão **Incluir**.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-25_21-10-53.png?version=1&modificationDate=1624666253830&api=v2)

Clicar no botão para seleção do campo **CB5->CB5\_CODIGO** e clicar no botão **OK**.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-25_21-11-26.png?version=1&modificationDate=1624666286350&api=v2)

Clicar em **Finalizar** para finalizar a inclusão da consulta padrão.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-25_21-13-30.png?version=1&modificationDate=1624666410563&api=v2)

**PERGUNTAS (SX1)**

Para a criação da consulta padrão (SXB) devemos acessar o módulo **Configurador (SIGACFG)**, em **Base de dados / Dicionário / Bases de Dados**. Clicar na opção **Perguntas**e logo em seguida no botão **Incluir**.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-25_21-18-52.png?version=1&modificationDate=1624666732797&api=v2)

Informas os seguintes dados:

Grupo: **NFDANFETIQ**

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-25_21-19-31.png?version=1&modificationDate=1624666772043&api=v2)

E os seguintes dados. Em seguida clicar em **Confirmar** para realizar a inclusão do pergunte (SX1) **NFDANFETIQ**.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-25_21-20-8.png?version=1&modificationDate=1624666808560&api=v2)

**VISÃO GERAL**

No Protheus, ao acessar a rotina Nf-e Sefaz, clicando em Outras Ações > DANFE foram incluídas duas opções no botão "Imp. Padrão" e "Imp. Etiqueta", conforme pode-se ver na imagem abaixo.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-22_15-58-30.png?version=1&modificationDate=1624388310673&api=v2)

O botão "Imp. Padrão" (Impressão Padrão) possui a mesma ação que ao clicar no "DANFE" antes da atualização, ou seja, irá abrir a tela de configuração da impressão.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-22_16-12-58.png?version=1&modificationDate=1624389179040&api=v2)

A nova funcionalidade ficará a cargo do botão "Imp. Etiqueta" (Impressão Etiqueta), que ao ser clicado abrirá um filtro para selecionar as notas desejadas.

* De Nota Fiscal
* Até Nota Fiscal
* Série
* De Data
* Até Data
* Tipo da Operação
* Tipo de Impressora
* Impressora

Número da nota fiscal inicial que deseja realizar a impressão.

**Obs.: As notas devem estar autorizadas, para isso recomendamos que após a emissão realize o monitoramento.**

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-23_22-15-50.png?version=1&modificationDate=1624497350690&api=v2)       ![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-23_22-16-20.png?version=1&modificationDate=1624497380263&api=v2)

**I****MPRESSÃO EM ETIQUETA**

A partir do release 12.1.33 do Protheus essa implementação estará no RPO padrão, mas caso deseje realizar uma customização será possível baixar o fonte DanfeEtiqueta.prw no portal de Downloads e, após as alterações, compilá-lo no RPO.

**CRIAÇÃO DA FILA DE IMPRESSÃO**

Deverá ser criada uma fila de impressão através da inclusão de um registro na tabela genérica J3 (Fila de Impressão) pelo Configurador (SIGACFG).

Acessar SIGACFG → Base de Dados → Dicionário → Bases de Dados → Tabelas Genéricas → Pesquisar a Tabela J3 → Editar → Incluir o Registro

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-23_21-50-37.png?version=1&modificationDate=1624495837643&api=v2)

### 

**CADASTRO DE LOCAL DE IMPRESSÃO**

Para incluir uma impressora Zebra será necessário acessar o módulo SIGACOM → Atualizações → Acd → Local de Impressão e clicar em Incluir.

Tipo: Spool

![](https://tdn.totvs.com/download/attachments/625467172/image2021-7-1_11-46-12.png?version=1&modificationDate=1625150772383&api=v2)

Inserir a fila criada na tabela genérica J3 (Fila de Impressão), consultar tópico 03.b.

Ao tentar imprimir a primeira etiqueta, será criada uma pasta dentro do diretório protheus\_data como o nome informado na criação da fila de impressão, no caso deste exemplo, "danfe etiqueta";

Caminho: .../protheus\_data/impter/zebra/danfe etiqueta

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-25_10-20-3.png?version=1&modificationDate=1624627203120&api=v2)

Nesta pasta ficarão os arquivos gerados pelo Protheus para que possam ser impressos.

Tipo: IP (Internet Protocol)

![](https://tdn.totvs.com/download/attachments/625467172/image2021-7-1_11-48-42.png?version=1&modificationDate=1625150922520&api=v2)

### 

**LAYOUT DA ETIQUETA**

A Nota Técnica 2020.004 que dispõe sobre o DANFE Simplificado relata quais campos devem ser inseridos no documento.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-23_21-42-24.png?version=1&modificationDate=1624495344797&api=v2)

Com base no texto retirando da NT, foi desenvolvido o seguinte layout para o DANFE Simplificado - Etiqueta.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-23_21-40-21.png?version=1&modificationDate=1624495221720&api=v2)

Os campo de Nome/Razao Social tanto do emitente quanto do destinatário suportam até 2 linhas de conteúdo.

Caso deseje incluir mais informações, será possível a customização do rdmake.

Para tal, consultar FAQ **MP - ADVPL - Lista de metodos Classe MSCB (Impressora Térmica)**

**IMPRESSÃO EM A4**

COMPILAÇÃO DO RDMAKE

A partir do release 12.1.33 do Protheus essa implementação estará no RPO padrão, mas caso deseje realizar uma customização será possível baixar o fonte DanfeEtiqueta.prw no portal de Downloads e, após as alterações, compilá-lo no RPO.

### 

**IMPRESSÃO DO LOGO**

Para a impressão do DANFE Simplificado em impressão normal(2), pode ser configurado o logo da impressão conforme documentação a seguir: [NFE0005\_Alteração\_do\_Logotipo\_na\_DANFE\_por\_Parâmetro](https://tdn.totvs.com/pages/viewpage.action?pageId=56132524)

### 

**LAYOUT DA DANFE**

A impressão da DANFE Simplificado em impressora normal(2) é impressa apenas em orientação paisagem e folha tamanho A4, as configurações de borda também são fixas. Nesse modelo é possível imprimir até 6 DANFES na mesma página.

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-24_14-44-43.png?version=1&modificationDate=1624556683897&api=v2)

       Layout de impressão foi definido conforme as instruções da Nota Técnica: 2020.004:

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-24_16-7-31.png?version=1&modificationDate=1624561651777&api=v2)

           DANFE simplificado exemplo:

![](https://tdn.totvs.com/download/attachments/625467172/image2021-6-24_15-47-15.png?version=1&modificationDate=1624560435613&api=v2)

Os campo de Nome/Razao Social tanto do emitente quanto do destinatário suportam até 2 linhas de conteúdo.

Para impressoras Zebra, não há tamanho em pixels definido no fonte.  
O que foi verificado é que o fonte utiliza funções que já eram existentes no sistema pra impressão em Zebras, segue documentação:

[Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Lista de métodos da classe MSCB (Impressora Térmica)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018867572-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Lista-de-m)

Impressão de um Box em impressora ZEBRA LPT1:  
<https://tdn.totvs.com/display/public/mp/MSCBBox+-+Imprime+um+box+--+30803>

<https://tdn.totvs.com/pages/releaseview.action?pageId=505769401>

Verificar também os modelos de impressora utilizada:  
<https://tdn.totvs.com/display/public/mp/MSCBPrinter+-+Configura+Impressora+--+30557>

Adicionalmente, você pode testar a impressão utilizando o site abaixo para simular a visualização com o arquivo gerado:  
<http://labelary.com/viewer.html>

O boletim técnico está disponível no link abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=625467172>
