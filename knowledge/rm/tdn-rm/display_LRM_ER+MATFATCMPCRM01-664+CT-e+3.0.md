---
content_hash: 17f3630dfb670b9d519516696c3219e984e94b47a13101f8b30581339107b316
fetched_at: '2026-06-29T00:08:43.975985+00:00'
page_id: '307835429'
product: rm
source: tdn-rm
title: ER MATFATCMPCRM01-664 CT-e 3.0
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+MATFATCMPCRM01-664+CT-e+3.0
version: 114
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### 

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Movimento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | MATFATCMPCRM01 | **IRM/EPIC1** | MATFATCMPCRM01-664 |
| **Requisito/Story/Issue1** | MATFATCMPCRM01-296 | **Subtarefa1** | NA |
| **Chamado/Ticket2** | NA | | |
| **País** | Brasil | | |
| **Outros** | NA | | |

## 

## Objetivo

De acordo com o Ato COTEPE/ICMS 20, de 1 de setembro de 2016, até 4 de dezembro de 2017 é permitida a utilização do MOC – CT-e, na versão 2.00a para o cumprimento das obrigações previstas no Ajuste SINIEF 09/07. Dessa forma, a partir de 5 de dezembro de 2017 passa a vigorar o MOC – CT-e na versão 3.00.

Para atendimento da legislação, serão necessárias algumas alterações no leiaute da versão 2.00, que serão descritas abaixo.

## 

## Definição da Regra de Negócio

Parâmetros - Integrações | Fiscal

* Em **Dados Fiscais | Parâmetros por Filial | Ambiente CT-e**, no GroupBox **Versões de Layout Utilizados**, transformar o TextBox **CT-e** em um ComboBox, com o valor "3.00" e retirar os demais TextBox.

Parâmetros - Tipo de Movimento

* Retirar consistência de obrigatoriedade de marcar o parâmetro **Editar Dados da Placa do Veículo** ao salvar os parâmetros de Tipo de Movimento, pois no CT-e 3.00 as informações de veículo não serão enviadas.

Tela de Edição do Movimento

* Em **Transporte | Transportadora**, ocultar o CheckBox **Lotação** (TMOVTRANSP.LOTACAO).
* Em **CTRC | Outros Dados**, ocultar o TextBox **CIOT**.
* Em **CTRC | Remetente e Destinatário**, no GroupBox **Tipo** (TMOVTRANSP.TIPOREMETENTE) dentro do GroupBox **Remetente**, incluir um RadioButton para seleção da opção "Diversos", semelhante a opção existente no GroupBox **Tipo** (TMOVTRANSP.TIPODESTINATARIO) dentro do GroupBox **Destinatário**.
* Em **CTRC | Remetente e Destinatário**, criar um campo texto com tamanho até 256 caracteres com o nome **Observações** que deverá ser exibido quando o **Tipo do Remetente** (TMOVTRANSP.TIPOREMETENTE) ou do **Destinatário** (TMOVTRANSP.TIPODESTINATARIO) for "Diversos". Deve ser criada uma consistência para garantir que o campo seja preenchido com no mínimo 15 caracteres.
* Na tela **Documentos de Transportes Anteriores**:

1. O ComboBox **Tipo de Documento** (TCTEDOC.TIPODOCORIGINARIO) deverá conter apenas os seguintes valores:  
   07-ATRE;  
   08-DTA (Despacho de Transito Aduaneiro);  
   09-Conhecimento Aéreo Internacional;  
   10 – Conhecimento - Carta de Porte Internacional;  
   11 – Conhecimento Avulso;  
   12-TIF (Transporte Internacional Ferroviário);  
   13-BL (Bill of Lading).
2. O campo **Número Nota** (TCTEDOC.NUMERODOCFISCAL) deve permitir até 30 caracteres.

* Em **CT-e**, ocultar as telas **Seguro de Carga**, **Motorista** e **Carga Perigosa - ONU**.

Envio

1. Leiaute Genérico

* Os campos de data passam a ter tamanho 21, pois foram alterados para o formato UTC completo, com informação de TimeZone. Exemplo: no formato UTC para os campos de Data-Hora, "TZD" pode ser -02:00 (Fernando de Noronha), -03:00 (Brasília) ou -04:00 (Manaus), no horário de verão serão -01:00, -02:00 e -03:00. Exemplo: "2010-08-19T13:00:15-03:00".

Grupo de Informações "infCTe":

* A tag "versao" deve ser preenchida com o valor "3.00".

Grupo de Informações "ide":

* A tag "forPag" foi excluída.
* A tag "procEmi" deverá ser preenchida "0", que representa a opção "emissão de CT-e com aplicativo do contribuinte".
* A tag "refCTE" foi excluída.
* Foi incluída a tag "indGlobalizado", tamanho 1. Deve ser preenchida com 1 quando **Tipo Remetente** (TMOVTRANSP.TIPOREMETENTE) ou **Tipo Destinatário** (TMOVTRANSP.TIPODESTINATARIO) for igual a “Diversos”. Nas demais situações a tag não deve ser informada.
* A tag "xMunEnv" passa a ter tamanho entre 2 e 60.
* A tag "xMunIni" passa a ter tamanho entre 2 e 60.
* A tag "xMunFim" passa a ter tamanho entre 2 e 60.
* Foi incluída a tag "indIEToma", obrigatória, numérica, tamanho 1. Deve ser preenchida com:  
  1 – Contribuinte ICMS;  
  2 – Contribuinte isento de inscrição;  
  9 – Não Contribuinte.  
  Essa informação é referente ao tomador indicado na tag "toma3" ou "toma4" e deverá ser buscada do cadastro (DFILIAL.CONTRIBUINTE ou FCFO.CONTRIBUINTE) do tomador que foi informado no movimento.

Grupo de Informações "toma4":

* A tag "IE" passa a ter tamanho fixo de 14.
* A tag "xNome" passa a ter tamanho entre 2 e 60.
* A tag "xFant" passa a ter tamanho entre 2 e 60.

Grupo de Informações "enderToma":

* A tag "xLgr" passa a ter tamanho entre 2 e 255.
* A tag "xBairro" passa a ter tamanho entre 2 e 60.
* A tag "xMun" passa a ter tamanho entre 2 e 60.
* A tag "xPais" passa a ter tamanho entre 2 e 60.
* A tag "dhCont" passa a ter tamanho 21.

Grupo de Informações "emit":

* A tag "IE" passa a ter tamanho fixo de 14.
* A tag "xNome" passa a ter tamanho entre 2 e 60.
* A tag "xFant" passa a ter tamanho entre 2 e 60.

Grupo de Informações "enderEmit":

* A tag "xLgr" passa a ter tamanho entre 2 e 60.
* A tag "xBairro" passa a ter tamanho entre 2 e 60.
* A tag "xMun" passa a ter tamanho entre 2 e 60.

Grupo de Informações "rem":

* Quando o **Tipo Remetente** (TMOVTRANSP.TIPOREMETENTE) for igual a "Diversos", a tag "CNPJ" deve ser preenchida com o CNPJ do emitente do CT-e (GFILIAL.CGC).
* A tag "IE" passa a ser opcional e a ter tamanho fixo de 14.
* A tag "xNome" passa a ter tamanho entre 2 e 60.
* Quando o **Tipo Remetente** (TMOVTRANSP.TIPOREMETENTE) for igual a "Diversos", a tag "xNome" deve ser preenchida com "DIVERSOS".
* A tag "xFant" passa a ter tamanho entre 2 e 60.

Grupo de Informações "enderReme":

* A tag "xLgr" passa a ter tamanho entre 2 e 255.
* A tag "xBairro" passa a ter tamanho entre 2 e 60.
* A tag "xMun" passa a ter tamanho entre 2 e 60.
* A tag "xPais" passa a ter tamanho entre 2 e 60.
* O grupo de informações "locColeta" e todas as suas tags foi excluído.

Grupo de Informações "exped":

* A tag "IE" passa a ser opcional e a ter tamanho fixo de 14.
* A tag "xNome" passa a ter tamanho entre 2 e 60.

Grupo de Informações "enderExped":

* A tag "xLgr" passa a ter tamanho entre 2 e 255.
* A tag "xBairro" passa a ter tamanho entre 2 e 60.
* A tag "xMun" passa a ter tamanho entre 2 e 60.
* A tag "xPais" passa a ter tamanho entre 2 e 60.

Grupo de Informações "receb":

* A tag "IE" passa a ser opcional e a ter tamanho fixo de 14.
* A tag "xNome" passa a ter tamanho entre 2 e 60.

Grupo de Informações "enderReceb":

* A tag "xLgr" passa a ter tamanho entre 2 e 255.
* A tag "xBairro" passa a ter tamanho entre 2 e 60.
* A tag "xMun" passa a ter tamanho entre 2 e 60.
* A tag "xPais" passa a ter tamanho entre 2 e 60.

Grupo de Informações "dest":

* Quando o **Tipo****Destinatário** (TMOVTRANSP.TIPODESTINATARIO) for igual a "Diversos", a tag "CNPJ" deve ser preenchida com o CNPJ do emitente do CT-e (GFILIAL.CGC).
* A tag "IE" passa a ter tamanho fixo de 14.
* A tag "xNome" passa a ter tamanho entre 2 e 60.
* Quando o **Tipo Destinatário**(TMOVTRANSP.TIPODESTINATARIO) for igual a "Diversos", a tag "xNome" deve ser preenchida com "DIVERSOS".

Grupo de Informações "enderDest":

* A tag "xLgr" passa a ter tamanho entre 2 e 255.
* A tag "xBairro" passa a ter tamanho entre 2 e 60.
* A tag "xMun" passa a ter tamanho entre 2 e 60.
* A tag "xPais" passa a ter tamanho entre 2 e 60.
* O grupo de informações "locEnt" e todas as suas tags foi excluído.

Grupo de Informações "ICMSSN":

* Foi incluída a tag "CST", obrigatória, numérica, tamanho 2. Deve ser preenchida com valor 90.

Grupo de Informações "emiDocAnt":

* A tag "IE" passa a ter tamanho fixo de 14.

Grupo de Informações "idDocAntPap":

* A tag "nDoc" passa a ter tamanho entre 1 e 30.

Grupo de Informações "idDocAntEle":

* A tag "chave" passa a se chamar "chCTe".
* O grupo de informações "seg" e todas as suas tags foi excluído.
* O grupo de informações "peri" e todas as suas tags foi excluído.

Grupo de Informações "infCteSub":

* Foi incluída a tag "refCteAnu", obrigatória, númerica, tamanho 44. Deve ser preenchida com a chave de acesso do CT-e de Anulação.
* O grupo de informações "tomaNaoICMS" e todas as suas tags foi excluído.

Grupo de Informações "infGlobalizado":

* Esse grupo de informações deve ser criado sempre que o **Tipo Remetente** (TMOVTRANSP.TIPOREMETENTE) ou o **Tipo Destinatário** (TMOVTRANSP.TIPODESTINATARIO) do movimento for igual a “Diversos”. Caso contrário não precisa ser criado.
* Contem a tag "xObs", obrigatória, caracter, tamanho entre 15 e 256. Deve ser preenchida com as informações contidas no campo texto **Observações** que será criado em **CTRC | Remetente e Destinatário**.

Grupo de Informações "infServVinc":

* Esse grupo de informações deve ser criado sempre que o CT-e for vinculado a CT-e multimodal. Caso contrário não precisa ser criado.
* Contem o grupo de informações "infCTeMultimodal", obrigatório. Deve ser incluído um para cada multimodal.
* Contem a tag "chCTeMultimodal", obrigatória, numérica, tamanho 44. Deve ser preenchida com a chave de acesso do CT-e Multimodal.

2. Leiaute Rodoviário

Grupo de Informações "rodo"

* A tag "dPrev" foi excluída.
* A tag "lota" foi excluída.
* A tag "CIOT" foi excluída.
* O grupo de Informações "valePed" e todas suas tags foi excluído.
* O grupo de Informações "veic" e todas suas tags foi excluído.
* O grupo de Informações "lacRodo" e todas suas tags foi excluído.
* O grupo de Informações "moto" e todas suas tags foi excluído.

Consistências

1. Retiradas

* Se Tipo do CT-e (TMOVTRANSP.TIPOCTE) = 0 (Normal) ou 3 (Substituição) e Indicador de Lotação (TMOVTRANSP.LOTACAO) = 1: Verificar se o grupo de informações do veiculo (veic) foi informado (TCOMPONENTECARGA com registro para o CT-e a ser enviado) para modal de transporte (TTMVEXT.MODAL) Rodoviário.
* Se Tipo do CT-e (TMOVTRANSP.TIPOCTE) = 0 (Normal) ou 3 (Substituição), se modal (TTMVEXT.MODAL) = Rodoviário e RNTRC (TVEICULO.RNTC) for diferente de “ISENTO”: Verificar se o grupo de informações do seguro da carga (seg) foi informado (TCTESEGURO informado para o CT-e a ser enviado).

2. Incluídas

* Se indicador de tomador for igual a Contribuinte (indIEToma = 1): Rejeitar se o tomador indicado (toma3 ou toma4) não possuir informação da IE (DFILIAL.CONTRIBUINTE ou FCFO.CONTRIBUINTE) ou se estiver informado “ISENTO”.
* Se indicador de tomador for igual a Isento de Inscrição (indIEToma=2): Rejeitar se o tomador indicado (toma3 ou toma4) não possuir informação de IE (DFILIAL.CONTRIBUINTE ou FCFO.CONTRIBUINTE) ou se estiver informada diferente do literal “ISENTO".
* Se indicador de tomador for igual a Não Contribuinte (indIEToma=9): Rejeitar se o tomador indicado (toma3 ou toma4) possuir a tag IE (DFILIAL.CONTRIBUINTE ou FCFO.CONTRIBUINTE) informada.
* Se Tipo do CT-e (TMOVTRANSP.TIPOCTE) = 0 (Normal) ou 3 (Substituição) e Tipo de Serviço (TMOVTRANSP.TIPOSERVICOCTE) for igual a Redespacho / Redespacho Intermediário / Subcontratação: O grupo de Documentos Anteriores (docAnt) deve ser informado (TCTEEMISSOR com registro para o CT-e a ser enviado).
* Se estiver informado o grupo de documentos anteriores (TCTEEMISSOR com registro para o CT-e a ser enviado): Rejeitar se o CT-e estiver com tipo de serviço (TMOVTRANSP.TIPOSERVICOCTE) Normal (tpServ=0).
* Se informado indicador de CT-e Globalizado (indGlobalizado) (TMOVTRANSP.TIPOREMETENTE ou TMOVTRANSP.TIPODESTINATARIO igual a “Diversos”): UF de início (TMOVTRANSP.CODETDCOLETA) deve ser igual a UF de fim (TMOVTRANSP.CODETDENTREGA) da prestação.
* Se informado indicador de CT-e Globalizado (indGlobalizado) (TMOVTRANSP.TIPOREMETENTE ou TMOVTRANSP.TIPODESTINATARIO igual a “Diversos”): Tomador do CT-e (TMOVTRANSP.TOMADORTIPO) deve ser Remetente ou Destinatário.

DACTE

Não existe mais o DACTE Modal Rodoviário (Carga Lotação) e Modal Rodoviário (Carga Fracionada). No DACTE Modal Rodoviário foram realizadas algumas alterações:

Identificação do Emitente

* Incluído o campo CNPJ do emitente.
* Incluído o campo IE do emitente.

Data e Hora de Emissão

* Apresentar campo no formato HH.MM.SS.

CT-e Globalizado

* O quadro Forma de Pagamento foi retirado e foi incluído o quadro CT-e Globalizado.
* Deve apresentar o campo Indicador do CT-e Globalizado, indGlobalizado, em ide.
* Deve apresentar o campo Informações do CT-e Globalizado, xObs, em infGlobalizado.

CFOP - Natureza de Operação

* Neste quadro deve ser apresentado os campos CFOP e Natureza da Operação, no formato CFOP - natOp.

Valor Total da Carga

* Este quadro foi incluído e deve apresentar o campo Valor Total da Carga, vCarga, em infCarga.

Seguradora

* Este quadro foi retirado.

Informações Relativas ao Imposto

* O campo Substituição Tributária foi substituído pelo campo Classificação Tributária do Serviço, CST. Em ICMS.
* O campos ICMS ST foi retirado.

Documentos Originários

* Foi retirado o campo Observações.

Previsão do Fluxo da Carga

* Este quadro contem informações referentes ao modal aéreo.

Observações Gerais

* Este quadro foi incluído e deve apresentar o campo Observações Gerais, xObs de compl

Informações Específicas do Modal Rodoviário

* Foi excluído o campo CIOT.
* Foi excluído o campo Lotação.
* Foi excluído o campo Data Prevista de Entrega.

Informações Específicas do Modal Rodoviário - Lotação

* Este quadro foi excluído.

Abaixo o leiaute novo do DACTE:

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [ACAA040 – Parâmetros] | [Alteração] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA050 – Negociação Financeira] | [Envolvida] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA060 – Cadastro de Pedidos] | [Criação] | [Atualizações -> Acadêmico-> Cadastros] | - |

**Tabelas Utilizadas**

* TCTE - Conhecimento de Transporte Eletrônico
* TMOV - Movimentos
* TCTEDOC - Dados dos Documentos Anteriores CTe
* TMOVTRANSP - Dados de Transporte

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
