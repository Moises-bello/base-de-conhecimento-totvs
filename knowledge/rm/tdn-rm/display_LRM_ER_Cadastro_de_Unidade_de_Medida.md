---
content_hash: 3848f5a5281acedb70713437e7a99e51cd39848106db2eb0a62a100614494aa0
fetched_at: '2026-06-29T00:06:01.820954+00:00'
page_id: '198940550'
product: rm
source: tdn-rm
title: ER_Cadastro_de_Unidade_de_Medida
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Cadastro_de_Unidade_de_Medida
version: 8
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Gestão de Estoque, Compras e Faturamento | **Módulo** | Cadastros |
| **Segmento Executor** |  | | |
| **Projeto1** | R\_C&P\_MOV006 | **IRM1** | PCREQ-4508 |
| **Requisito1** | PCREQ-6393 | **Subtarefa1** | PDR\_CP\_MOV006-891 |
| **Chamado2** | N/A | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | N/A | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

  Migração do Cadastro de Unidade para o ambiente Fluig utilizando o TOTVS HTML Framework.

## Definição da Regra de Negócio

**TOTVS HTML *Framework***

 

O TOTVS | HTML *Framework* foi concebido para tratar apenas a camada de interface das aplicações, confiando que os produtos por trás da interface irão conceder a infraestrutura e a implementação mínima dos serviços para utilização do *framework*. 

Ela tem como objetivo:

* Fornecer uma Infraestrutura de componentes visuais e de serviços (de interface) HTML5;
* Prover uma IDE de desenvolvimento HTML5, baseada no TDS ([TOTVS Developer Studio](http://ds.totvs.com/));
* Disponibilizar um Template de CRUD responsivo com respectivo acelerador no TDS, baseado em Serviços providos pelos produtos;
* Estruturar um ambiente de desenvolvimento compatível com o Fluig e que possa ser utilizados por todos os produtos TOTVS.

A arquitetura pode ser resumida de acordo com a imagem a baixo:

Mais informações sobre o TOTVS HTML Framework: [tec:TOTVS](http://tdn.totvs.com/pages/createpage.action?spaceKey=LRM&title=HTML+Framework&linkCreation=true&fromPageId=196053421) 

### Fluig

No mundo dos negócios, onde as empresas precisam ter controle sobre suas operações e, ao mesmo tempo, agilidade para atender aos diversos processos que acontecem simultaneamente, a forma de interação mudou. A comunicação e os procedimentos são determinados, mas não rígidos, e a única constância é justamente a mudança e tudo precisa estar em nossas mãos. 

Entendendo a mudança no comportamento dos indivíduos no ambiente corporativo e as demandas tecnológicas, a TOTVS criou a plataforma fluig com o objetivo de centralizar em uma única tela todos os processos, documentos e sistemas com um único login em uma interface de comunicação colaborativa. 

Em resumo Fluig é uma plataforma de produtividade e colaboração que unifica a gestão de processos, documentos e identidades. 

Mais informações sobre o Fluig nos links:  

* <http://tdn.totvs.com/display/public/fluig/Sobre+o+Fluig>
* <http://www.fluig.com/>

#### Cadastro de Unidades

Nesta opção, cadastram-se as unidades de medida que serão utilizadas pelo sistema. As unidades aqui cadastradas poderão ser utilizadas nos produtos, nas cotações e movimentos.

```
Observações:
```

* O Fator de Conversão, é o valor, em relação a unidade base, pelo qual deverá ser multiplicada a quantidade do produto nesta unidade. Será respeitada uma consistência que verificará se o fator de conversão, após ser truncado, será diferente de zero. Caso o fator de conversão seja diferente de zero, será gravado normalmente, caso contrário, uma mensagem será exibida para o usuário informando que o fator de conversão está errado e deverá ser alterado.
* As quantidades serão apresentadas, de acordo com o número de casas decimais informada na unidade, no campo Nº Casas Decimais.
* O tamanho do Código Reduzido está limitado a 2 caracteres e será utilizado para a integração com parceiros de automação comercial, devido à restrição existente nas impressoras fiscais, que limitam o tamanho do código da unidade de medida.

No **TOTVS Gestão de Estoque, Compras e Faturamento** o **Cadastro de Unidades** está localizado no seguinte caminho: **BackOffice | Gestão de Estoque, Compras e Faturamento | Cadastros | Mais... | Tabelas Auxiliares | Unidade**

#### Migração

Para o Cadastro de Unidades do **TOTVS Gestão de Estoque, Compras e Faturamento** serão desenvolvidas telas web utilizando o TOTVS HTML Framework.

Uma vez que as telas Web forem desenvolvidas, estas serão inserida na plataforma Fluig e/ou Portal RM para que o usuário possa ter um acesso mais ágil e prático do cadastro.

#### Campos e Regras

O Cadastro de Unidade de Medida possui os seguintes campos e suas respectivas regras.

* Código: Código da unidade de medida. Campo obrigatório.
* Descrição: Descrição da unidade de medida. Campo obrigatório.
* Cód. Unidade Base: Utilizado para a conversão. Não poderá ser alterado caso esteja vinculado a um produto com saldo. Valor padrão: UN.
* Fator de Conversão: Utilizado, juntamente com o cód. de unidade base para realizar a conversão. Não poderá ser alterado caso esteja vinculado a um produto com saldo. Deve ser positivo. Valor padrão: 1.
* Código Reduzido: Sigla que identifica, de forma resumida, o código da unidade. Tamanho máximo de 2 caracteres.
* Nº Casas Decimais: Utilizado ao exibir/imprimir as quantidades. Necessário ter um valor maior que zero e não pode conter mais que 4 caracteres. Valor padrão: 0.

##### Tabelas Utilizadas

* TUND

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
