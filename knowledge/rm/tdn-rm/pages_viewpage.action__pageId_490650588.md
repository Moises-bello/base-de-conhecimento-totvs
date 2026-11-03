---
content_hash: e7f9193dd5ba7e5cd628baf69f707ae604b6fbb029140c35b0f48cf8ba13d84d
fetched_at: '2026-06-29T00:10:21.203833+00:00'
page_id: '490650588'
product: rm
source: tdn-rm
title: Parâmetros de Processos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490650588
version: 91
---

#f5f5f5#363636noneParâmetros de Processos

## **Conteúdo**

4. 4.1.   
   4.2.   
   4.3.   
   4.4.   
   4.5.   
   4.6.   
   4.7.

## **01. Visão GeralVisaoGeral**

O Cadastro de Parâmetro de Processos deve ser utilizado para parametrizar processos pré-determinados do TOTVS Gestão Fiscal, são eles:

* Apuração de determinados Tributos;
* Geração de registros de algumas Rotinas Acessórias;
* Cálculos de processos existentes no TOTVS Gestão Fiscal.

## **02. CadastroCadastro**

O Cadastro está disponível em:

BackOffice | Gestão Fiscal | Cadastros | Específicos - Parâmetros de Processos

Menu Parâmetros de Processos

## **03. Campos CadastroCamposCadastro**

O Cadastro é constituído dos seguintes campos:

* Processo
* Grupo do Processo
* Descrição
* Data Inicial
* Data Final
* Código da Filial (Na Inclusão será considerado a filial do contexto)

Tela Parâmetro de Processos

## **04. ProcessosProcessos**

Processos4.1. Apuração

### **4.1.** ApuraçãoApuracao

Ao selecionar essa opção , será disponibilizado o *Grupo do Processo **CPRB - Contribuição Previdenciária sobre a Receita Bruta***

No anexo   é possível informar o tipo de documento que compõe a apuração da CPRB Regime de Caixa.

O cadastro possui os seguintes campos:

* Origem → Modelo de Documento
* Tipo de Documento
* Descrição do Documento
* Código da Conta Contábil.

Não deve ser permitido inclusão de documentos duplicados para um mesmo Filtro de Operação.

Documentação do Processo: <https://tdn.totvs.com/display/public/LRM/CPRB+Regime+de+Caixa#1-1>

Informações

Parâmetro utilizado por empresas sujeitas ao pagamento da Contribuição Previdenciária sobre a Receita Bruta (CPRB), instituída pela [Medida Provisória nº 540, de 2011](http://www.planalto.gov.br/ccivil_03/_Ato2011-2014/2011/Mpv/540.htm), posteriormente convertida na [Lei nº 12.546, de 2011](http://www.planalto.gov.br/ccivil_03/_Ato2011-2014/2011/Lei/L12546.htm) e alterações. A CPRB incide sobre o valor da receita bruta, em substituição à contribuição previdenciária patronal incidente sobre a folha de pagamento dos segurados empregados e contribuintes individuais 19.

4.2. EFD Contribuições

### **4.2.** EFD ContribuiçõesEFDContribuicoes

Ao selecionar essa opção , será disponibilizado os ***G****rupos do Processo**:*

*F100  
F120  
F130  
F500*

**Parâmetros do Patrimônio**

Esta aba somente será exibida caso os grupos de processo forem iguais a F120 ou F130. O cadastro é dotado das seguintes listas:

* Método de Apropriação de Crédito
* Grupo do Patrimônio
* Utilização do Patrimônio
* Número de parcelas a serem apropriadas (Somente para o grupo de processo F130)
* Num. de parcelas p/ periodicidade "Outras": (Somente se o Número de parcelas a serem apropriadas for igual a "Outra periodicidade definida em lei")

**Anexo Filtro de Tributos**

###### **Filtro de Operações**

Para cada tipo de documento, deve-se informar o Tributo. O mesmo é vinculado nos grupos de processo F100, F500 no anexo do, já os grupos de processo referentes ao F120 e F130 são vinculados ao cadastro dos **Parâmetros de Processo** em si.

O Cadastro possui os seguintes campos:

* Código do Tributo
* CST
* Natureza da Receita

Parâmetros:

* Código da Coligada
* Id. do Filtro de Tributo
* Código do Tributo
* Id. Filtro Tipo Operações (Caso o grupo de processo exigir tipo de operação)
* CST
* Natureza Receita

Não deve ser permitido inclusão de tributos duplicados para um mesmo Filtro de Operação.

###### **Filtro de Operações Contábeis**

O cadastro de parâmetro de processo possui o anexo **[Filtro de Operações Contábeis](https://tdn.totvs.com/pages/viewpage.action?pageId=772823527)** para configuração do F100 com origem contábil.

4.3. FECP - Fundo de Combate à Pobreza

### **4.3.** FECP - Fundo de Combate à PobrezaFECP

Ao selecionar essa opção , será disponibilizado o *Grupo do Processo **Produtos não considerados no cálculo do FECP***

Será apresentado a opção para informar o produto que não serão considerados no cálculo do FECP.

Não deve ser permitido cadastrar produtos duplicados para um mesmo subgrupo.

4.4. FCI - Ficha de Conteúdo de Importação

### **4.4.** FCI - Ficha de Conteúdo de ImportaçãoFCI

Ao selecionar essa opção , será disponibilizado o *Grupo do Processo **Seleção de Produtos para geração da FCI***

Será apresentado a opção para informar o produto que serão considerados no processo FCI.

Não deve ser permitido cadastrar produtos duplicados para um mesmo subgrupo.

4.5. EFD-Reinf

### **4.5. EFD-ReinfEFDReinf**

Ao selecionar essa opção, é disponibilizado o Grupo do Processo "**EFD-REINF Parâmetros".**

Esta parametrização será utilizada para geração dos Eventos R-4010, R-4020 e R-4080 da Rotina EFD-REINF

O Cadastro possui os seguintes campos:

**Centralizado**: Quando estiver habilitado, todos os Lançamentos\Movimentações realizados a uma determinada Pessoa Física\Jurídica, serão gerados em um único arquivo XML a ser transmitido para a EFD-REINF.

Quando desabilitado, todos os Lançamentos\Movimentações realizados a uma determinada Pessoa Física\Jurídica, serão agrupados em um arquivo XML para cada Filial a ser transmitido para a EFD-REINF.

**Classificação de Países**: Deve ser informada qual Classificação de Países será utilizada. A informação dessa opção define qual o Código de País que será gerado no XML.

**Valor dos Rendimentos Financeiros**: **“Valor Original** ou **Valor do Serviço”** - Selecionar qual o valor deve ser considerado ao gerar os Rendimentos de Lançamentos Financeiros.

**Anexo Filtro de Filiais**

Será apresentado a opção para informar as Filiais que serão geradas nos Eventos R-4010, R-4020 e R-4080 da Rotina EFD-REINF.

Saiba mais:

**Anexo Filtro de Eventos**

Será apresentado a opção para informar os Tributos e Natureza de Rendimentos que serão geradas nos Eventos R-4010, R-4020 e R-4080 da Rotina EFD-REINF.

Saiba mais:

*[EFD REINF - Eventos Periódicos](https://tdn.totvs.com/pages/viewpage.action?pageId=506387451)*

4.6. CIAP - Cálculo do CIAP

### **4.6. CIAP - Cálculo do CIAPCIAP**

Ao selecionar essa opção, é disponibilizado o Grupo do Processo **"Naturezas que serão consideradas no Cálculo de saídas do CIAP".**

Esta parametrização será utilizada para geração do relatório de Cálculo de Saídas do CIAP.

**É disponibilizado o processo de Inclusão de Naturezas**:

O processo possui os seguintes campos, tanto para Saídas Totais, quanto para Saídas Tributadas:

**Naturezas Iniciais e Finais**: Intervalo de Naturezas que serão adicionadas para o Cálculo.

**Considerar como Tributado**: Deve ser informado qual valor será utilizado nas Naturezas, para o Cálculo do CIAP.

Saiba mais: [Inclusão de Naturezas em Lote](https://tdn.totvs.com/pages/viewpage.action?pageId=864346772)

**Anexo Filtro de Natureza**

Será apresentado a opção para informar as Naturezas que serão geradas do relatório de Cálculo de Saídas do CIAP.

Saiba mais: [Filtro por Naturezas](https://tdn.totvs.com/display/LRM/Filtro+por+Natureza)

4.7. EFD - ICMS/IPI**4.7. EFD - ICMS/IPIEFDICMSIPI**

Ao selecionar essa opção, é disponibilizado o Grupo do Processo **"Naturezas que serão consideradas no Cálculo do Registro 1400 - anual".**

Esta parametrização será utilizada para geração do relatório 1400 anual da EFD.

**Anexo Filtro de Natureza**

Será apresentado a opção para informar as Naturezas que serão consideradas no Cálculo do Registro 1400 anual da EFD.

Saiba mais: [Filtro por Naturezas](https://tdn.totvs.com/display/LRM/Filtro+por+Natureza)

## **05. Habilitar novo Cadastro de Parâmetros de  Processos na nova MDINovoCadastro**

Para habilitar o uso das rotinas migradas referentes ao cadastro de processo utilizando a nova MDI acesse *BackOffice | Gestão Fiscal | Ambiente |Configuração -  Parâmetros | TOTVS Gestão Fiscal*e siga o passo a passo a seguir:

2true1Passo 1

Procure por *Parâmetros Gerais | Parâmetro*s e avance

Imagem2Passo 2

Marque a opção "*Novo Cadastro de Parâmetros de Processos*" e avance

Imagem3Passo 3

As seguintes mensagens serão exibidas:

Novo Cadastro de Parâmetros de Processos (Versão Beta)

Versão Beta - Ao Habilitar este Parâmetro, pode ocorrer instabilidade em alguns Processos do Sistema

Imagem

## **06. Outras informaçõesOutrasInformacoes**

Informações

Descrição sobre o que é , citado no documento.

---
