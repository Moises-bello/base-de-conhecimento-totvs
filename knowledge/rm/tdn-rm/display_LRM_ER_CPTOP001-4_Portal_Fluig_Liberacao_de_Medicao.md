---
content_hash: 2238765890efa2b91c2b7764ee7aea545d3eb1cddc4fb996a6edd78b6b49ad68
fetched_at: '2026-06-29T00:08:10.119305+00:00'
page_id: '240301590'
product: rm
source: tdn-rm
title: ER_CPTOP001-4_Portal_Fluig_Liberacao_de_Medicao
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_CPTOP001-4_Portal_Fluig_Liberacao_de_Medicao
version: 23
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Contratos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | CPTOP001 | **IRM1** | CPTOP001-3 |
| **Requisito1** | CPTOP001-4 | **Subtarefa1** | CPTOP001-55 |
| **Chamado2** | Não se aplica. | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | |  |  | | --- | --- | | **Pré-requisitos para melhor entendimento da especificação** | | | **Entidade** | **Link para o Wikihelp** | | Projetos | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Projetos.aspx> | | Contratos | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Contrato.aspx> | | Períodos de Contrato | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.PeriodosContrato.aspx> | | Liberação de Período de Contrato | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.LiberarPeriodo.aspx> | | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Migração da funcionalidade de Liberação de Período de Contrato para o ambiente Web utilizando o TOTVS HTML Framework.

## Definição da Regra de Negócio

### **TOTVS HTML Framework**

O TOTVS | HTML *Framework* foi concebido para tratar apenas a camada de interface das aplicações, confiando que os produtos por trás da interface irão conceder a infraestrutura e a implementação mínima dos serviços para utilização do *Framework*. 

 Ela tem como objetivo:  

* + - Fornecer uma Infraestrutura de componentes visuais e de serviços (de interface) HTML5;
    - Prover uma IDE de desenvolvimento HTML5, baseada no TDS ([TOTVS Developer Studio](http://ds.totvs.com/));
    - Disponibilizar um Template de CRUD responsivo com respectivo acelerador no TDS, baseado em Serviços providos pelos produtos;
    - Estruturar um ambiente de desenvolvimento compatível com o Fluig e que possa ser utilizados por todos os produtos TOTVS.

A arquitetura pode ser resumida de acordo com a imagem a baixo: 

 

Mais informações sobre o TOTVS HTML Framework: [tec:TOTVS](http://tdn.totvs.com.br/pages/createpage.action?spaceKey=LRM&title=HTML+Framework&linkCreation=true&fromPageId=196053421)

### Fluig

No mundo dos negócios, onde as empresas precisam ter controle sobre suas operações e, ao mesmo tempo, agilidade para atender aos diversos processos que acontecem simultaneamente, a forma de interação mudou. A comunicação e os procedimentos são determinados, mas não rígidos, e a única constância é justamente a mudança e tudo precisa estar em nossas mãos. 

Entendendo a mudança no comportamento dos indivíduos no ambiente corporativo e as demandas tecnológicas, a TOTVS criou a plataforma fluig com o objetivo de centralizar em uma única tela todos os processos, documentos e sistemas com um único login em uma interface de comunicação colaborativa. 

Em resumo Fluig é uma plataforma de produtividade e colaboração que unifica a gestão de processos, documentos e identidades. 

 

Mais informações sobre o Fluig nos links:  

* + <http://tdn.totvs.com/display/public/fluig/Sobre+o+Fluig>
  + <http://www.fluig.com/>

### Liberação de Período de Contrato

É a liberação do período de contrato que pode ser para pagamento, suprimento ou somente sinalizar o fim do período. 

#### Pré-Requisitos para realizar Liberação de Período de Contrato no TOTVS HTML

* + Ter um contrato criado.
  + Ter itens ou objetos associados.
  + Ter Períodos gerados para o contrato.
  + Ter Períodos medidos

### Detalhes da Liberação de Período de Contrato

Para a funcionalidade de Liberação de Período de Contrato do TOTVS Obras e Projetos existem páginas Web utilizando o TOTVS HTML Framework.

Uma vez que as páginas Web forem desenvolvidas, estas serão inseridas na plataforma Fluig para que o usuário possa ter um acesso mais ágil e prático da funcionalidade.

O acesso à Liberação de Períodos se dá através das páginas de "Medição de Item de Contrato" e "Consumir Objetos do Contrato" e está disponível em cada período do contrato nas seguintes opções ():

* + - Liberar para Suprimento/Faturamento (esta funcionalidade está detalhada em um outro documento);
    - Liberar para o TOTVS Obras e Projetos;
    - Liberar para o Financeiro.

A página de Liberação de Período de Contrato contém três abas distintas:

* + - TOTVS Obras e Projetos ():
      * **Valor da Medição:**
        + **% reajuste:** Percentual que pode ser informado para reajustar a medição do período na liberação;
        + **Com reajuste:**Valor da liberação aplicado o percentual de reajuste;
        + **Sem reajuste:**Valor se o reajuste aplicado;
        + **Valor Retido/Deduzido no Período:**Valor total da retenções e deduções no período. Este campo estará habilitado somente se não existirem deduções ou retenções, e no caso de existir os valores e percentuais devem estar zerados;
        + **Valor Retido no Item:**Valor da retenção informada na medição do período;
        + **Valor Retido Total:**Valor da soma da retenção informada na medição do período e da retenção informada na liberação do período;
        + **Total da Liberação:** Valor total da medição adicionando o reajuste e subtraindo a retenção.
      * **Reajustes:** Uma tabela com um cadastro de reajuste informado no cadastro do contrato;
      * **Deduções:** Utilizado para informar os tipos e valores de deduções do período. Existe, também, a opção para informar os produtos faturados à dedução onde a dedução deverá ser associada ();
      * **Retenções:** Utilizado para informar os tipos e valores de retenções do período;
      * **Campos Complementares:**Possui os campos complementares cadastrados no Menu Cad. Gerais | Campos Complementares | Detalhamento Medição. (Não disponível nesta versão);
      * **Observação:**Observação da liberação.
    - Integração Financeiro (): Esta aba somente estará disponível se o projeto estiver integrado com o Financeiro RM e não integrado com o Financeiro Protheus
      * **Identificação**;
        + **Código Cliente/Fornecedor:** Permite informar o Cliente ou Fornecedor em questão, o cliente/fornecedor do contrato é automaticamente exibido.
        + **Tipo Contábil:** Permite informar qual o tipo contábil do Lançamento que será gerado no Financeiro.
        + **Tipo Documento:** Permite informar qual o tipo de documento do Lançamento que será gerado no Financeiro.
        + **Conta Caixa:** Permite informar qual a conta caixa do Lançamento que será gerado no Financeiro.
        + **Tipo de Lançamento:** Permite informar o tipo do Lançamento que será gerado no Financeiro (Rateio de Centro de Custo e Rateio de Departamento).
        + **Gerar Lançamento no Financeiro com Rateio de Centro de Custo;**
        + **Gerar Lançamento no Financeiro com Rateio de Departamento;**
      * **Campos Opcionais de Valores:**Permite informar os valores dos Campos Opcionais de Valores parametrizados no Financeiro;
      * **Datas Opcionais:** Permite informar as datas parametrizadas no Financeiro;
      * **Tabelas Opcionais:** Permite informar as tabelas opcionais parametrizadas no Financeiro;
      * **Campos Opcionais Alfa:** Permite informar os campos opcionais Alfas parametrizados no Financeiro.
    - Suprimento/Faturamento: esta funcionalidade está detalhada em um outro documento.

Além das abas citadas, a página de liberação contém a Data de Liberação, a opção de apenas Salvar as informações sem liberar o período, nesse caso apenas as informações da aba "TOTVS Obras e Projetos" serão salvas e a opção de liberar o período com todas as opções selecionadas. Se o período já estiver liberado a mensagem "O período selecionado já se encontra liberado." será exibida na parte superior da página e apenas a opção de Voltar estará disponível.

### Cancelar Liberação do Período

A funcionalidade de Cancelar Liberação do Período também está disponível nas páginas de "Medição de Item de Contrato" e "Consumir Objetos do Contrato" juntamente com as opções de liberação. Ao selecionar essa opção uma pergunta será exibida, questionando se realmente o cancelamento é necessário, onde ao confirmar, a liberação do período será cancelada.

**Importante:**

 

* **A opção de campos complementares existente no processo de Liberar Período da MDI, não será implementado nesta versão, pois depende de uma rotina a ser desenvolvida no TOTVS HTML Framework para criação dos mesmos.**

## Protótipo de Tela

### **Protótipo 01**

**Opções de Liberação de Período**

**Protótipo 02**

**Aba TOTVS Obras e Projetos**

### **Protótipo 03**

**Aba Integração Financeiro**

**Protótipo 07**

**Produtos Faturados à Dedução**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
