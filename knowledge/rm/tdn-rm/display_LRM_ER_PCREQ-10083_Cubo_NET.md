---
content_hash: 8dab35eac81f85a2c2e36a7fa1fcdb306e176920b41ed2a4b49fda406d8a72a9
fetched_at: '2026-06-29T00:08:08.398819+00:00'
page_id: '238033127'
product: rm
source: tdn-rm
title: ER_PCREQ-10083_Cubo_NET
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10083_Cubo_NET
version: 115
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Framework | **Módulo** | Inteligência de Negócios |
| **Segmento Executor** |  | | |
| **Projeto1** | FRW\_002 | **IRM1** | PCREQ-10027 |
| **Requisito1** | PCREQ-10083 | **Subtarefa1** | PDR\_FRW\_FRW002-202 |
| **Chamado2** |  | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### Objetivo

 

*Executar um estudo com prova de conceito de ferramentas de análise para substituição ou adequação do controle de Pivot utilizado atualmente pelo Cubo.NET.*

*Foram identificadas situações em que o consumo de memória é excessivo, causando uma degradação da performance no Pivot da DevExpress.*

### Definição da Regra de Negócio

* *Criar uma tabela física no banco de dados com os dados da consulta cedida pelo cliente com 2.3 milhões de registros*
* *Estudar o controle Pivot da DevExpress e identificar alternativas para contornar o problema de perfomance*
  + *Vericar as propriedades de comportamento do controle para identificar as opções mais performáticas*
  + *Estudar a opção de ServerMode do controle de Pivot*
  + *Estudar a opção de OLAP do controle de Pivot*
* *Estudar controles de Pivot de outros fornecedores como alternativa ao uso do DevExpress*
  + *Telerik*
  + *Infragistics*
  + *RadarSoft*
  + *ComponentOne*

### Comparativo de Performance entre os controles

| Fornecedor | Uso de Memória (GB) | Tempo de Inicialização (Segundos) |
| --- | --- | --- |
| DevExpress 14.1 | 6,1 | 4,4 |
| DevExpress 15.2 | 6,1 | 4,0 |
| RadarSoft | 4,1 | 73,5 |
| ComponentOne | 4,8 | 6,2 |
| Telerik | > 10 | < 1,0 |
| Infragistics | ND | ND |

Observações:

Devido a complexidade para utilização do Pivot da Infragistics, o mesmo foi abortado para não impactar nas horas do estudo.

Apesar do cubo da RadarSoft ser o mais demorado para inicialização, aparentemente todos os cálculos de dimensões feitas pelo mesmo são efetuadas na inicialização. Desta forma este controle foi o que obteve a melhor performance na utilização pelo usuário final, enquanto todas as outras opções vão tendo a performance degradada na medida que a navegação é feita.

Todos os controles com exceção do RadarSoft apresentam baixa performance ao trabalhar com este conjunto de dados.

### Considerações finais

Fizemos o contato com o suporte da DevExpress a respeito desta baixa performance do componente. Mesmo após seguirmos as orientações dadas por eles, não obtivemos uma melhora considerável. Criamos um protótipo simulando a nossa situação e enviamos para eles.

Considerando este cenário, a alternativa mais eficiente seria utilizar o ServerMode com uma tabela física no banco. Para isto teremos que fazer mais estudos quando a que tipo de banco utilizar pois o mesmo deve ser acessado pela aplicação cliente. 

Uma proposta seria utilizar um engine de banco de dados local como SQL Compact ou SQLite, é preciso avaliar a performance destas soluções juntamente com a possibilidade de utiliza-las com o Entity Framework ou LINQ for SQL, pois o ServerMode obrigatoriamente precisa de usar uma dessas tecnologias.

Foi avaliada a utilização do Microsoft Analysis Services, mas a mesma depende de um componente de terceiros para visualização e utilizando o DevExpress não obtivemos uma melhora de performance considerável.

Apesar do componente RadarSoft ter tido uma performance mais eficiente, a sua utilização irá ter um grande impacto na experiência de uso, pois visualmente ele é bem inferior, além de trabalhar com um conjunto de dados que deve ser previamente configurado pelo usuário, coisa que não é necessária nas outras alternativas.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
