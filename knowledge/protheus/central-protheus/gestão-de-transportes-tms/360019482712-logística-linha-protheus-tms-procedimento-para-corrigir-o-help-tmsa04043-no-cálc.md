---
article_id: 360019482712
category: Gestão de Transportes (TMS)
content_hash: 54bb80a8aac61f06711b1938957b8130a432b406c3c75abd781b6bc617347d16
fetched_at: '2026-06-28T22:45:32.468100+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Procedimento para corrigir o help TMSA04043
  no cálculo do frete
type: support-article
updated_at: '2025-06-18T18:28:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019482712-Log%C3%ADstica-Linha-Protheus-TMS-Procedimento-para-corrigir-o-help-TMSA04043-no-c%C3%A1lculo-do-frete
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32903533472279)***Tempo aproximado para leitura: **00:05:12 min  
  
Ocorrência**Ocorre o *help* **TMSA04043 - Regra ou TES não encontrado para Tipo Documento/Tipo Frete/Componente/Cliente ou Fornecedor/Região Destino** no cálculo do frete.  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Causa**  
Falta de parametrização ou parametrização inconsistente.  
  
**Solução**O *help***TMSA04043** pode ser apresentado nas seguintes situações:

1. Cotação de frete;
2. Visualização de frete na digitação de documentos do cliente;
3. Cálculo de frete.

É apresentado quando não está sendo localizado uma regra de tributação para o movimento em questão.  
  
A mensagem pode apresentar variações envolvendo **UF - Unidade de Federação** - **estado**, **componentes**, **segmentos**, entre outros.

**![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360028487951)**

Pela imagem conseguimos identificar as informações que o Sistema está utilizando para consulta dos cadastros. Nesse exemplo, está sendo informado que a **Regra** ou o **TES - Tipos de Entrada e Saída** não foi localizada para:

* Tipo de documento = 8
* Tipo de frete = 2
* Componente = 03
* Cliente ou Fornecedor = 000112-15
* Região Destino = J04201

Ou seja, na imagem é apresentada primeiramente uma sequência de cadastros e após as informações que está buscando nestes cadastros.  
  
Para identificar o motivo pelo qual o *help* está apresentando e onde corrigir, é necessário fazer as seguintes validações:  
 **Atualizações/ Documentos e regras/ Regras por Cliente - TMSA600:**Nessa rotina verificar se existe uma regra de tributação para o cliente devedor do frete, neste caso verificar no campo **Dev. Frete - Devedor do Frete** do documento de entrada quem é o devedor do frete, caso não tenha uma regra para o cliente em questão, utilizar a regra genérica, conforme parâmetro **MV\_CLIGEN - Código do Cliente/Loja**. Fazer as seguintes validações nesta rotina:

* No cadastro de regra por cliente somente é obrigatório o preenchimento dos campos **Cliente** e **Loja**, **Docto**. **Transp**. **- Documento de Transporte** e **Regra** **Trib. - Regra de Tributação**. Os demais campos conforme necessidade da empresa;
* Deve ter uma **Regra por cliente** para o tipo de documento que está sendo emitido. O tipo de documento pode ser verificado na mensagem apresentada em tela ou na rotina **Entrada de Documentos** **de** **Clientes - Atualizações - Recebimento -**no campo **Docto. Transp**;
* Verificar se o campo **Cod. Prod**. **- Código do Produto**está preenchido. Caso esteja, é necessário que na rotina **Entrada de Documentos** **de** **Clientes** tenha na linha da nota fiscal o produto em questão ou ter uma regra que contemple o mesmo;
* Verificar como está configurado o campo **Tipo da NFC - Tipo da Nota fiscal do Cliente**. O campo **Tipo Nf Cli.**na rotina **Entrada de Documentos** **de** **Clientes** deve ser igual ao da regra ou ter uma regra que contemple o mesmo;
* Verificar o campo **Tipo****Cliente**. Caso esteja preenchido, o cliente devedor do frete deve ter no seu cadastro de clientes o campo **Tipo** com a mesma informação ou ter uma regra que contemple o mesmo;
* Verificar o campo **Seq. Inscrica. - Sequência de Inscrição.** Caso esteja preenchido, no documento de entrada deverá verificar se o campo **Seq. Ins.** está preenchido;
* Após validar essas informações no cadastro **Regra por Cliente**, verificar como está preenchido o campo **Regra Trib**. Com essa informação acessar a rotina **Regras Tributação** - **Atualizações** - **Doctos e Regras -** e localizar a regra de tributação em questão.

**Atualizações/****Documentos e regras/** **Regras de Tributação - TMSA410:**

* No *grid* Itens da**Regra de Tributação** verificar se existe uma regra para a **TES** desejada. Esse campo é obrigatório para que a mensagem não seja apresentada. Com essa informação verificar se a **TES** que está sendo utilizada não está bloqueada para uso. Essa informação pode ser verificada na rotina **Tipos de Entrada e Saída - Atualizações - Cadastros**;
* Caso seja criada uma regra de tributação informando somente a **TES**, significa que a mesma é genérica, ou seja, será acatada para todos os componentes, estados e segmentos;
* Caso a campo **Componente** esteja preenchido, deverá verificar se os componentes da tabela de frete utilizada estão iguais ao da regra de tributação;
* Caso os campos **UF Origem**, **UF Devedor** e **UF Destino** estiverem preenchidos, deverá ser verificado como está preenchido o campo **Sel. Origem - Seleção de Origem** na rotina **Entrada de Documentos de Clientes**, para que seja verificado em qual cadastro deve ser baseado para verificação da **UF**;
  1. Acessar o documento na rotina **Entrada de Documentos de Clientes** e verificar as **UFs** dos **remetente, destinatário e devedor** do documento;
  2. Acessar o cadastro de clientes e verificar qual a **UF** e **Região de destino** do **remetente** e  **destinatário**. A região de destino de cada cadastro deve estar coerente com a **UF** do mesmo, por exemplo, se a **UF** for **SP - São Paulo**, a região de destino deve ser de uma cidade da **UF** em questão;
* Caso o campo **DUG\_SATIV - Segmento** esteja preenchido, o mesmo deve ser igual ao do devedor do frete, verificando o segmento do devedor do frete no cadastro de clientes campo **Segmento 1**, na aba **Vendas.** Se não deseja controlar a regra de tributação por segmento de cliente, recomenda-se deixar o campo **DUG\_SATIV - Segmento** em branco;
* Caso o campo **DUG\_CONSIG - Consig.** esteja configurado como **Sim**, deverá ser preenchido no entrada de documentos o campo **Consignatario**. Recomenda-se utilizar o campo **DUG\_CONSIG - Consig.**como **3 - Ambos**, para que a regra seja utilizada independente se há consignatário ou não no documento.
