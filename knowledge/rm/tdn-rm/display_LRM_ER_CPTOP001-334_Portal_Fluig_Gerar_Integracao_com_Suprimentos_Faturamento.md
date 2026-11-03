---
content_hash: 620d108fd45b978011fffb9f0c3a9290e2e9a06a8225894ecf31feeae64d18b9
fetched_at: '2026-06-29T00:08:16.171555+00:00'
page_id: '244928006'
product: rm
source: tdn-rm
title: ER_CPTOP001-334_Portal_Fluig_Gerar_Integracao_com_Suprimentos_Faturamento
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_CPTOP001-334_Portal_Fluig_Gerar_Integracao_com_Suprimentos_Faturamento
version: 119
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Contratos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | CPTOP001 | **IRM1** | CPTOP001-333 |
| **Requisito1** | CPTOP001-334 | **Subtarefa1** | CPTOP001-388 |
| **Chamado2** | Não se aplica. | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | |  |  | | --- | --- | | **Pré-requisitos para melhor entendimento da especificação** | | | **Entidade** | **Link para o Wikihelp** | | Projetos | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Projetos.aspx> | | Contratos | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Contrato.aspx> | | Períodos de Contrato | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.PeriodosContrato.aspx> | | Gerar Integração com Suprimento / Faturamento | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.GerarIntegracaoSuprimFatur.aspx> | | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Migração da funcionalidade de Gerar Integração com Suprimentos/Faturamento de Contrato para o ambiente Web utilizando o TOTVS HTML Framework.

## SuprimentoDefinição da Regra de Negócio

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

### Gerar Integração com Suprimento/Faturamento

É a liberação do período de contrato que integra com o sistema de Suprimento/Faturamento gerando para o BackOffice (Protheus, TOTVS Gestão de Estoque, Compras e Faturamento, entre outros) um movimento com o tipo, o produto, condição de pagamento, filial, local de estoque e centro de custo selecionados ou de acordo com os valores definidos no cadastro do contrato.

#### Pré-Requisitos para realizar Liberação de Período de Contrato no TOTVS HTML

* + Ter um contrato criado.
  + Ter itens ou objetos associados.
  + Ter Períodos gerados para o contrato.
  + Ter Períodos medidos

### Detalhes do processo de Gerar Integração com Suprimento/Faturamento

Para a funcionalidade de Gerar Integração com Suprimento/Faturamento do TOTVS Obras e Projetos existem páginas Web utilizando o TOTVS HTML Framework.

Uma vez que as páginas Web forem desenvolvidas, estas serão inseridas na plataforma Fluig para que o usuário possa ter um acesso mais ágil e prático da funcionalidade.

O acesso ao processo se dá através das páginas de "Medição de Item de Contrato" e "Consumir Objetos do Contrato" e está disponível em cada período do contrato nas opção Liberar para Suprimento/Faturamento ():

A página de Gerar Integração com Suprimento/Faturamento contém a seguinte aba:

* + - Resumo da Liberação (): Aba também presente na Liberação de Período para o Financeiro
      * **Valor da Medição:**
        + **% reajuste:** Percentual que pode ser informado para reajustar a medição do período na liberação;
        + **Com reajuste:**Valor da liberação aplicado o percentual de reajuste;
        + **Sem reajuste:**Valor se o reajuste aplicado;
        + **Valor Retido/Deduzido no Período:**Valor total da retenções e deduções no período. Este campo estará habilitado somente se não existirem deduções ou retenções, e no caso de existir os valores e percentuais devem estar zerados;
        + **Valor Retido no Item:**Valor da retenção informada na medição do período;
        + **Valor Retido Total:**Valor da soma da retenção informada na medição do período e da retenção informada na liberação do período;
        + **Total da Liberação:** Valor total da medição adicionando o reajuste e subtraindo a retenção.
      * **Reajustes:** Uma tabela com um cadastro de reajuste informado no cadastro do contrato;
      * **Deduções:** Utilizado para informar os tipos e valores de deduções do período. Existe, também, a opção para informar os produtos faturados à dedução onde a dedução deverá ser associada;
      * **Retenções:** Utilizado para informar os tipos e valores de retenções do período;
      * **Campos Complementares:**Possui os campos complementares cadastrados no Menu Cad. Gerais | Campos Complementares | Detalhamento Medição. (Não disponível nesta versão);
      * **Observação:**Observação da liberação.
      * **Suprimento/Faturamento** (): Painel que contêm as informações necessárias para a integração com o sistema de Suprimento/Faturamento
      * + **Movimento**: Informações que serão atribuídas ao movimento gerado no Suprimento/Faturamento
          - **Tipo de Movimento a ser gerado:** O valor default pode ser definido no cadastro do contrato;
          - **Local de estoque:** O valor default pode ser definido no cadastro do contrato;
          - **Estado:** Utiliza como valor default o estado do projeto;
          - **Município:** Utiliza como valor default o município do projeto;
          - **Condição de Pagamento:** O valor default pode ser definido no cadastro do contrato;
          - **Filial:**O valor default pode ser definido no cadastro do contrato, porém é utilizado somente se não estiver integrado com o Protheus, caso integrado, verifica se o parâmetro "Permite alterar filial do contrato" está marcado, não estando, a filial utilizada será a do projeto;
          - **Centro de Custo:** Utiliza como valor default o centro de custo do projeto;
          - **Produto:**O valor default pode ser definido no cadastro do contrato;
          - **Produtos Associados:** Essa opção somente será exibida se o contrato for do tipo "Insumo" ou "Extra Histograma" e se o parâmetro de projeto "Considerar produtos associados no faturamento de contratos de insumo" estiver marcado;
          - **Observação;**
        + **Tabelas Opcionais**: Devem estar parametrizadas no Suprimento/Faturamento para utilização
          - **Tabela Opcional 1;**
          - **Tabela Opcional 2;**
          - **Tabela Opcional 3;**
          - **Tabela Opcional 4;**
          - **Tabela Opcional 5;**
        + **Valores Extras**: Devem estar parametrizados no Suprimento/Faturamento para utilização
          - **Valor Extra 1:**
            * **Percentual;**
            * **Valor.**
          - **Valor Extra 2:**
            * **Percentual;**
            * **Valor.**

Além das informações citadas, a página contém a Data de Liberação, que somente estará disponível se o parâmetro geral "Permitir data retroativa no faturamento de contratos" estiver marcado. Contém a opção de apenas Salvar as informações sem liberar o período, nesse caso apenas as informações da aba "Resumo da Liberação" sem considerar as informações de Suprimento/Faturamento serão salvas. Por fim, contém e a opção de Liberar Integração Suprimento/Faturamento com todas as opções selecionadas. Se o período já estiver liberado a página não abrirá e a mensagem "O período selecionado já se encontra liberado." será exibida.

## Protótipo de Tela

### **Protótipo 01**

**Opções de Liberação de Período**

**Protótipo 02**

**Aba Resumo da Liberação com **Integração Suprimento/Faturamento****

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
