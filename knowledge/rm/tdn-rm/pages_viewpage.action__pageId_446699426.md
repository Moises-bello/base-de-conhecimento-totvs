---
content_hash: bdd40e774525cb4872ef979d092fd1afde19922ac1babdb8318444e61417aa2f
fetched_at: '2026-06-29T00:09:55.079745+00:00'
page_id: '446699426'
product: rm
source: tdn-rm
title: ER Nota Técnica 2018.004 Cancelamento por substituição da NFC-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=446699426
version: 9
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão Fiscal |
| **Segmento Executor** | Serviços | | |
| **Requisito/Story/Issue** |  | **Subtarefa** |  |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

### Objetivo

 Atender a  Nota Técnica 2018.004 - Evento de cancelamento por substituição da NFC-e

## Definição da Regra de Negócio

A Nota Técnica 2018.004 publicou a implantação do evento de Cancelamento por substituição para a NFC-e. Este evento é semelhante ao evento de cancelamento normal, mas com um prazo de cancelamento maior desde que obedecidas algumas regras. A substituição deverá ser utilizadas para os casos em que, por motivo qualquer, a empresa venha a emitir duas notas para a mesma operação sendo a primeira com o tipo da emissão normal e a segunda emitida em contingência (Regra definida na própria N.T.). O evento de cancelamento normal não teve nenhuma mudança.

## Cronograma

Este evento entra em vigor no ambiente de homologação a partir de  e em produção a partir de .

## Legislação

Este documento foi elaborado com base na [Nota Técnica 2018.004 v1.00](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=) disponível no portal da NF-e.

## Cadastro

No cadastro do evento da NFC-e deverá ser adicionado um campo para gravar o IDMOV da nota referenciada através do evento de Cancelamento por Substituição. Esta nota deverá ficar visível na tela da NFC-e e do Evento de Substituição apresentando o número do movimento relacionado.

Criar o campo IDMOVREF na tabela TNFEESTADUALEVENT (Foreign Key com TMOV)

## Processo

Tela de execução do processo

1. Deverá ser adicionado uma nova opção de evento para NFC-e através do processo de "Envio de Eventos" da tela de NFC-e/NF-e, conforme abaixo.
   * Descrição: Cancelamento por Substituição de NFC-e
   * Código: 110112
2. Ao selecionar este tipo de eventodeverá ser habilitado um campo para indicar qual a NFC-e substituiu a atual sendo que só pode ser selecionada uma NFC-e autorizada.
3. Ao selecionar a NFC-e substituta deverá ser verificado se o movimento pode ser cancelado e emitir um aviso ao cliente questionando se ele deseja continuar (comportamento igual ao cancelamento normal).
4. Deverá ser habilitado um campo de texto livre para o usuário preencher o motivo do cancelamento com tamanho minimo 5 e máximo 60 (verificar o comportamento do cancelamento normal).

Envio de Eventos

O processo deverá montar um xml para  evento conforme o layout publicado na própria NT (2.1 Leiaute Mensagem de Entrada) e enviá-lo ao TSS/TOTVS Colaboração.

1. **Envio com sucesso:** se o Evento for enviado com sucesso a NFC-e deverá ficar com o status de Cancelamento Pendente e o Evento como pendente.
   1. O campo TNFEESTADUALEVENT.IDMOVREF deverá ser gravado com o IDMOV da nota referenciada.
   2. O status da NFC-e deverá ser alterado para Cancelamento Pendente.
   3. O evento deverá ser salvo com o status Pendente
2. **Envio inconsistente**
   1. Caso o evento fique como inconsistente o mesmo **não** poderá gravar a foreignkey no campo TNFEESTADUALEVENT.IDMOVREF
   2. O status da NF-e deverá ser mantido como autorizada.
   3. E o evento deverá ser salvo como inconsistente.
3. **Regras**

   1. O evento de Cancelamento por Substituição só poderá ser executado para notas Autorizadas.
   2. O evento de Cancelamento por Substituição só poderá ser executado para NFC-e (modelo 65).

Após a execução do processo o histórico deverá gravar qual foi o idmov e numeromov da nota referenciada mesmo que o envio apresente falhas e fique inconsistente.

Consulta de Eventos

Ao executar o processo de Consulta de Eventos o TSS será consultado e retornará uma mensagem Soap ao ERP. 

1. **Evento Autorizado:**Se o TSS retornar o campo STATUS como 6 ou o campo STATEVEN estiver com o valor **155 - Cancelamento autorizado fora do prazo**ou **135 Recebido pelo Sistema de Registro de Eventos, com vinculação do evento na NF-e.**
   1. Se o Evento for autorizado com sucesso o mesmo deverá ficar com status autorizado, a nota deverá ficar com o status Cancelada e o movimento deverá ser cancelado automaticamente.
   2. Caso não seja possível cancelar o movimento o evento deverá ser mantido como pendente, a nota como cancelamento pendente e um log deve ser apresentado ao usuário informado que o movimento não pôde ser cancelado (mesmo comportamento do cancelamento normal).
2. **Evento em processamento:**Caso o TSS retorne o status do evento como 1, 2 ou 4 o mesmo deverá ser mantido como pendente e uma mensagem deve ser apresentada ao usuário informando que o processo o evento está em processamento (verificar o comportamento dos atuis eventos)
3. **Evento Rejeitado**: Se o TSS retornar o campo STATUS como 5 ou 3 o evento deverá ser rejeitado e neste caso.
   1. O status do evento deverá ser alterado para Rejeitado.
   2. O status da NFC-e deverá ser alterado para Autorizado.
   3. o campo IDMOVREF deve ser apagado.
4. **Nenhum dos casos anteriores**: Neste caso nada deverá ser alterado (nota e evento) e uma mensagem deve ser apresentada ao usuário informando que não foi possível interpretar o retorno do evento, caso o problema persista o mesmo deverá entrar em contato com o suporte técnico da TOTVS.

O processo de consulta de evento através do Monitor de Arquivos do TOTVS Colaboração deverá manter o mesmo comportamento da consulta do TSS, porém neste processo não existe o campo STATUS e neste caso deverá ser analisado o processo já existente para verificar como a identificação está sendo realizada. Caso não seja possível identificar a regra no fonte deveremos implementar apenas duas regras obedecendo o mesmo comportamento do TSS:

1. **Evento Autorizado:**Se o campo cStat estiver com o valor**155 - Cancelamento autorizado fora do prazo**ou **135 Recebido pelo Sistema de Registro de Eventos, com vinculação do evento na NF-e.**
2. ****Evento Rejeitado**:**Verificar os códigos de rejeição constantes na NT.

Em todas as execuções da consulta o histórico deve ser gravado.

## Possíveis erros

* **Rejeição: Tipo de Emissão inválido no Cancelamento por Substituição:** Por regra a SEFAZ aceita que uma NFC-e do tipo normal seja substituida por outra NFC-e emitida em contingência e qualquer operação fora deste cenário será rejeitada.
* **Rejeição: Prazo de cancelamento superior ao previsto na Legislação**: Inicialmente o prazo para substituição de uma NFC-e é de 7 dias a partir da data da autorização, mas este regra pode variar conforme a necessidade de cada UF.
* Rejeição: NF-e Substituta Denegada ou Cancelada: A substituição poderá ser executada somente para NFC-e Autorizadas.
* **Rejeição: Data de emissão da NF-e Substituta maior que 2 horas da data de emissão da NF-e a ser cancelada:** Apesar do evento de Substituição poder ser transmitido até 7 dias após a autorização da NFC-e a SEFAZ irá validar se a nota substituta (a NFC-e que foi emitida em contingência) foi emitida a mais de 2h em relação a autorização da nota substituta.
* **Rejeição: Valor total da NF-e Substituta difere do valor da NF-e a ser cancelada:**O evento será autorizada somente se os valores das duas NFC-e forem iguais.
* **Rejeição: Valor total do ICMS da NF-e Substituta difere do valor da NF-e a ser cancelada:**O evento será autorizada somente se os valores de ICMS das duas NFC-e forem iguais.
* **Rejeição: Identificação do destinatário da NF-e Substituta difere da identificação do destinatário da NF-e a ser cancelada:**O evento será autorizada somente se os dados do cliente forem os mesmos nas duas notas.
* **Rejeição: Quantidade de itens da NF-e Substituta difere da quantidade de itens da NF-e a ser cancelada:**O evento será autorizada somente se as duas notas tiverem os mesmos itens
* **Rejeição: Item da NF-e Substituta difere do mesmo item da NF-e a ser cancelada:**O evento será autorizada somente se as duas notas tiverem os mesmos itens na mesma ordem.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
