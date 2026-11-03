---
article_id: 360022206012
category: Financeiro
content_hash: f669053c43edcdd21808ea09fa60f226727455dbef6822dba4be1e64fc953b38
fetched_at: '2026-06-28T22:38:01.123744+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Procedimento para emissão
  de DARF
type: support-article
updated_at: '2021-08-13T23:22:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022206012-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Procedimento-para-emiss%C3%A3o-de-DARF
---

**Dúvida**Procedimento para emissão de DARF e recursos da rotina FINA373.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) –  Financeiro – FINA373 – A partir da versão 12.1.017  
  
**Solução**

**Controle de Darf**Este recurso permite o controle sobre a emissão de Darf (Documento de Arrecadação de Receitas Federais), possibilitando a identificação dos títulos de impostos que compõem a Darf emitida para seu recolhimento.  
O objetivo desta rotina é facilitar a identificação dos títulos que compõe a Darf emitida para seu recolhimento, bem como facilitar a geração das informações para a DCTF (Módulo Fiscal).

Procedimentos:

1. Acesse o Módulo **Financeiro** > **Atualizações** > **Diversos** > **Controle Darf**.    
2. Observe que estão disponíveis as opções:

* **Emitir Darf**
* **Reemitir Darf**
* **Consulta Darf**
* **Cancelar Darf**

**Emitir Darf**Para emitir Darf é necessário possuir registros no **Contas a Paga**r (tabela **SE2**) com retenção de impostos, que possua o campo **GERA DIRF** = Sim, e que tenha o código de retenção do imposto no campo **CD RETENÇÃO** preenchido.

No módulo **Financeiro** acesse **Relatórios** > **Contas a Pagar** > **Emissão de Darf** preencher os campos conforme a necessidade de recolhimento da empresa.

**Importante:**No momento da **emissão da Darf**, será gerado um identificador único por guia, para controle das guias emitidas no Modelo Comum.    
Este controle será gravado nas tabelas **SE2** – **Campo de identificação de guia de Darf** (**E2\_IDDARF**) e **FI9** – **Controle de emissão de guias de Darf** (Registro do controle – todos os campos serão gravados).  
As guias emitidas no Modelo Simples não serão gravadas, pois não tem relacionamento com os títulos a pagar contidos no sistema.

**Remitir Darf**Será utilizada para reimprimir o documento de arrecadação já emitido anteriormente.

Procedimentos:

1. Clique em **Reemitir** no browser.  
2. Observe que o Sistema apresenta a tela para seleção da **guia de identificação da Darf** (IDDARF) que se quer reemitir.  
3. Preencha os campos conforme descrição a seguir:  
**Período de/até** (data de emissão da Darf).  
**Guia de/até** (código de identificação de Darf).   
**Fornecedor de/até.**

**Importante:**Esta opção não efetua **recálculo do valor da Darf**, apenas a reimpressão do documento com os valores pelos quais foi gerada.  
Somente guias (IDDARF) emitidas anteriormente e ativas no cadastro de emissão de Darf poderão ser reemitidas.

**Consulta DARF**Permite consulta à composição (títulos de impostos) de uma Darf, apresentando uma tela com as informações da **guia emitida** (IDDARF).

Procedimentos:  
1. Clique na opção **Consulta** no browser.  
2. O Sistema exibe a tela contendo um campo para digitação da guia (IDDARF) que se quer consultar.  
3. Confirme para visualizar os dados referentes a:   
**Código de retenção do imposto**.   
Dados do **Fornecedor** do título principal (Código do Fornecedor, Loja e Nome Reduzido).   
Valor da Darf.

**Importante:**Informações dos títulos componentes da Darf (registros da tabela **FI9**). Nenhuma alteração será feita quanto aos registros das tabelas **SE2** ou **FI9**.  
O botão na barra de ferramentas permite emitir o **relatório de Darf**, para simples conferência.

**Cancelar DARF**Utilizado para cancelamento de uma Darf já emitida, permitindo que os títulos, antes pertencentes a uma guia, sejam amarrados a outra.

Procedimentos:

1. Clique na opção **Cancelamento** no browser.   
2. Observe que a tela apresentada é idêntica à de consulta.   
3. Informe o **código da guia** (IDDARF) que deseja **cancelar** e **confirmar** o cancelamento.   
4. O Sistema exibirá outra tela solicitando a confirmação do cancelamento da Darf.   
5. Se procede, confirme.

**Importante:** O Sistema efetuará a limpeza do **código de Darf** (IDDARF) no registro de **Contas a Pagar** (**E2\_IDDARF**) e a exclusão do registro do **FI9** referentes à Darf cancelada.  
 Nenhum título de imposto, componente da Darf deste cancelamento, poderá ter sido baixado (**FI9\_STATUS** = “B”).
