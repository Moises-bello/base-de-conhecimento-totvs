---
content_hash: 870af6c823af56a1d66077149fc701e33923d8dc673be275ec880b3fb03d883c
fetched_at: '2026-06-29T00:08:51.092522+00:00'
page_id: '336404337'
product: rm
source: tdn-rm
title: Integração TOTVS Gestão Fiscal X TAF por webservice
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=336404337
version: 32
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Fiscal |
| **Segmento Executor** | Serviços | | |
| **Projeto1** | Integração RM X TAF | **IRM1** |  |
| **Requisito1** | FISCAL01-3559 | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.20 | **Réplica: 12.1.18, 12.1.19** |  |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>* | | |

Objetivo

Documentar as implementações do cadastro de controle das integrações das informações do RM para o TAF para a geração da REINF

**Definição da Regra de Negócio**

* As informações serão geradas através do Gerador de Saídas em layout específico para este fim.
* Os registros são gravados em tabela interna para posterior envio ao TAF (DINTEGRACAOTAF).
* A visualização dos registros será feita através de cadastro desenvolvido.
  + O cadastro permite a visualização dos registros em lista na qual poderão ser selecionados um ou mais registros para a  execução do processo de integração com o TAF
  + O cadastro permite a abertura dos registros somente para a visualização. Não será permitida a edição ou inclusão de registros com exceção dos registros com Status " - Incluído" ou " - Registro integrado com erro"
* Os registros desta visão possuem um anexo onde é armazenado o log da integração, semelhante ao existente na visão de Notas Fiscais Eletrônicas.
* Os registros terão seus status controlados de acordo com os processos executados.  
   Eles poderão assumir os seguintes valores:
  + Incluído: Status inicial do registro quando ele é gravado na tabela "DINTEGRACAOTAF"  e que ainda não foi integrado com o TAF.
  + "Registro Enviado para o TAF" ou "Enviado Integração Banco x Banco":  O status deverá ser apresentado quando o registro  for enviado para a integração TAF via processos "Integração TAF - WebService - Envio" ou "Integração TAF - Banco x Banco".
  + Registro com erro na integração. O status é apresentado quando o registro integrado com o TAF apresentar erros de estrutura ou de validação realizado pelo TAF.
  + Registro integrado com sucesso com o TAF. O status é apresentado quando o registro for integrado com sucesso pelo TAF.
  + Registro integrado via banco de dados. O status é apresentado quando o registro for integrado com sucesso pelo TAF a partir da tabela TAFST1.
* **(**Melhoria -**Implementação futura)** Cada registro deverá indicar sua origem conforme relação a ser criada com base nos registros do layout TAF conforme exemplo abaixo:   
  + Registro TAF T001 - Complemento do Cadastro de Estabelecimentos  => Cadastro de Filiais no RM.
  + Registro TAF T013 - Cadastro de Documentos Fiscais => Lançamentos de Entrada/Saída no RM.
* **(Melhoria - Implementação futura)** Deverá ser feito o controle dos registros do RM que já foram integrados para que no processo possa-se escolher integrar todos os registros, somente os não integrados ou somente os já integrados.
* **(**Melhoria - Implementação futura**)** Para que não sejam gerados problemas de performance a tabela que armazena os registros da integração será incluída no processo de Liberação de Período.
* O envio das informações da REINF para a receita e controle de seus recibos será feito somente pelo TAF não sendo retornadas para o TOTVS Gestão Fiscal.
* O TOTVS Gestão Fiscal fará somente o controle das informações integradas com o TAF para a geração da REINF.

**Descrição do processo**

**Processo "Geração de Registros - TAF Fiscal"**

Este processo seleciona os lançamentos de acordo com os parâmetros passados para o Layout do Gerador de Saída e grava os dados selecionados na tabela DINTEGRACAOTAF.

Primeiro deve-se importar para o sistema o Layout atualizado(na tela de Gerador de Saídas, disponibilizado no diretório de instalação do sistema. Vide exemplo: C:\TOTVS\CORPORERM\ObjetosGerenciais\Layout - TAF.TOTVSGEN)  para integração com o TAF. Ao executar o processo informe os parâmetros para seleção e demais informações solicitadas pelo layout.

**DICA!!!** Marque o campo "**Gravar preferências do Usuário**" para agilizar novas (re)gerações.

**Especificação das tabelas criadas para auxiliar o processo**

Nome da Tabela: DINTEGRACAOTAF

Uma vez que os dados desta tabela são a ligação entre as informações do TOTVS Gestão Fiscal e o TAF não será permitida a exclusão dos mesmo. **(**Melhoria - Implementação futura**)** Para solucionar um possível problema com performance deverá ser criada uma tabela espelho desta (DINTEGRACAOTAFHIST) para que os registros desta tabela sejam transferidos via processo de Liberação de Período.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **CAMPO** | **TIPO** | **TAMANHO** | **PRECISÃO** | **SCALE** | **PERMITE NULO** | **DESCRIÇÃO** |
| CODCOLIGADA | int | - |  |  | não | Código da Coligada |
| IDINTEGRACAOTAF | int | - |  |  | não | ID de Integração RM x TAF |
| TAFFIL | varchar | 40 |  |  | sim | Empresa e Filial de integração |
| TAFCODMSG | varchar | 1 |  |  | não | Tipo da mensagem de integração |
| TAFSEQ | varchar | 3 |  |  | sim | Sequencial da mensagem de integração |
| TAFTPREG | varchar | 10 |  |  | sim | Tipo do Registro a ser integrado |
| TAFKEY | varchar | 100 |  |  | sim | Chave do Registro a ser integrado |
| TAFMSG | text | 16 |  |  | sim | Mensagem de integração |
| TAFSTATUS | varchar | 1 |  |  | sim | Status do Registro |
| TICKETCODE | varchar | 50 |  |  | sim | Código do Lote do Registro |

**Tabela de log da integração**

Nome da Tabela: DINTEGRACAOTAFLOG

Nesta tabela serão gravados os registros referentes às tentativas de integração do registro RM com o TAF.

|  |  |  |  |
| --- | --- | --- | --- |
| **CAMPO** | **TIPO** | **TAMANHO** | **DESCRIÇÃO** |
| CODCOLIGADA | int | - | Código da Coligada |
| IDLOG | int | - | Id do Log da Integração RM x TAF |
| DATALOG | datetime |  | Data do Log da Integração RM x TAF |
| CODIGOERRO | int | - | Código do erro na Integração RM x TAF |
| MENSAGEM | memo | 256 | Log da Integração RM x TAF |
| IDINTEGRACAOTAF | int | - | Sequencial do registro da DINTEGRACAOTAF |

****(**Melhoria - Implementação futura**)**Observação: Esta tabela também deverá ser incluída no processo de Liberação de Período. Os registros serão gravados por este processo na tabela DINTEGRACAOTAFLOGHIST. Esta implementação será entregue em liberações futuras.**

**Parametrização**

Para atender ao processo de integração das informações da REINF com o TAF é necessário o preenchimento dos parâmetros para integração de acordo com o seu ambiente TAF.

**Localização**: Processo 03.05 - Integração | 03.05.05 - TAF

**Servidor:** Onde o TAF está instalado (de onde o webservice da REINF é distribuído)

**Porta:** Pota na qual o webservice da REINF escuta

**Usuário:**  O mesmo utilizado para  login no TAF

**Senha:** A mesma utilizada para login no TAF

          É **obrigatório** a informação de todos os parâmetros para que os registros sejam integrados com o TAF via WebService.

**Tela**

**obs.:** Caso na Base de Dados não seja encontrado o Script com os Parâmetros da Integração com o TAF, será visualizada uma mensagem informando a inconsistência.

**O Cadastro**

Acesse o menu Obrigações Fiscais | TAF, o sub-menu "**Integração RM X TAF**".

O Log de integração é acessado através do Menu Anexos | **Log da Integração do Registro**.

 Os registros não poderão ser editados ou excluídos, apenas visualizados conforme imagem abaixo.

**(**Melhoria - Implementação futura**)**Marcar os lançamentos selecionados no processo como já exportados. Para isto deverá ser utilizado o campo DLAF.STATUSEXPORTFAZ.

**Integração TAF - WebService - Envio**

* Este processo chama o método POST do web service do TAF.
* Se não houver nenhum registro selecionado na visão serão selecionados todos os registros com status  - Incluído
* Se houver registros selecionados somente estes serão integrados.
* Após o envio o status do registro deverá ser alterado de acordo com o resultado da chamada do serviço.

****Integração TAF - WebService - Consulta****

* Este processo chama o método GET do web service do TAF.
* Se não houver nenhum registro selecionado na visão serão selecionados todos os registros com status  "Registro Enviado para o TAF" ou "Enviado Integração Banco x Banco"
* Se houver registros selecionados somente estes serão consultados.
* Os registros consultados terão seu status alterado de acordo com o resultado da consulta.
* Deverá ser verificada a necessidade de alterar o status dos Lançamentos Fiscais associados aos registros do TAF. **(**Melhoria - Implementação futura**)**

******Integração TAF - WebService - Excluir**** **(**Melhoria - Implementação futura**)****

* Este processo deve chamar o método DELETE do web service do TAF.
* Este processo deve exigir a seleção de pelo menos um registro para ser executado para garantir que um clique indevido no menu apague todos os registros listados na visão.
* Os registros processados com sucesso devem ser deletados da tabela de integração.

********Integração TAF - Banco x Banco********

* Este Processo deve ser utilizado no caso de impossibilidade de uso do web service do TAF para integração dos registros.
* Este processo consiste na gravação dos registros que estão na tabela de integração com o status " - Incluído" na tabela TAFST1. Os registros processados deverão:
* + Permanecer gravados na tabela de integração e ter seu status alterados para Integrados via Banco de Dados
  + Ser gravados na tabela TAFST1 para posterior integração com o TAF.
  + Posteriormente ser consultados através do processo Integração TAF - WebService - Consulta

******(**Melhoria - Implementação futura**)******

* Implementar a opção de integração ao TAF de um Lançamento Fiscal específico ou um intervalo. Este filtro poderá ser feito por data ou número do documento. Este processo poderá ser chamado pelo processos na visão de Lançamentos Fiscais de Entrada/Saída e também pela visão do novo cadastro criado para a integração com o TAF.
* Integração on line de Lançamentos Fiscais. Ao salvar um registro de Lançamento Fiscal  gravar os registros correspondentes no layout de integração TAF. Verificar no layout de integração quais são os registros relacionados ao Lançamento Fiscal, como itens, CliFor, observação, etc.

**O web service de integração com o TAF**

* + Para mais informações a respeito acesse: <http://tdn.totvs.com.br/pages/viewpage.action?pageId=270904682>
  + Para a integração dos registros deve-se chamar o método POST do webservice : O objetivo do método é enviar informações que devem ser gravadas na tabela transacional do TAF  ( TAFST2 ), permitindo que os dados sejam submetidos aos processos de integração.
  + Para consultar o status da integração deve-se chamar o método GET do webservice: O método GET retorna os status dos registros integrados de acordo com os parâmetros (atributos) enviados na URL.
  + Para deletar um registro ou conjunto de registros deve-se chamar o método DELETE: O método DELETE permite excluir toda a cadeia de integração de um TICKETCODE; Um ticket submetido a exclusão tem seus TAFKEYS avaliados, rastreados e excluídos, desde a sua inclusão na TAFST2 e TAFXERP até o cadastro no TAF caso já tenha ocorrido o Processamento.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
