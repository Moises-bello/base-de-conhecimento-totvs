---
article_id: 360025465672
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 0bfc26d3bc00faf1f05bef686d3a256f393c8165115b719e3a32ddae86b1028e
fetched_at: '2026-06-28T22:37:19.741175+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT  - Por que o Fornecedor,
  Cliente e Data de Vencimento não são mostrados no Browse na Nova Medição ?
type: support-article
updated_at: '2026-04-07T18:51:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025465672-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Por-que-o-Fornecedor-Cliente-e-Data-de-Vencimento-n%C3%A3o-s%C3%A3o-mostrados-no-Browse-na-Nova-Medi%C3%A7%C3%A3o
---

**Dúvida**  
Por que o Fornecedor ou Cliente não é carregado para o Browse na Nova Medição ?  
  
**Ambiente**  
Microsiga Protheus – Gestão de Contratos – A partir da versão 12  
  
**Solução**

Uma informação inicial, é que por padrão no Browse da rotina **CNTA121** são listadas informações apenas da tabela **CND**, de Cabeçalho da Medição.

A rotina **Nova Medição** (**CNTA121**), possibilita a inclusão de uma única medição para diversas planilhas.

Quando seleciona uma competência para medição, a aba planilhas apresenta todas as planilhas do contrato elegíveis para medição, sendo possível a seleção de uma ou mais planilhas.

Para cada planilha será gerado pedido ou título separado, como medições individuais, mas ainda atrelado a mesma medição. Por este motivo o fornecedor/cliente é gravado somente na aba planilha.

Caso haja a situação em que se vê o código de fornecedor/cliente no browse da rotina, normalmente esta acontece quando é visualizado no browse, uma medição que foi incluída pela rotina de Medição **CNTA120** (rotina de medição já descontinuada).

Na rotina Nova Medição (CNTA121) as informações de **Fornecedor/Cliente** bem como **Data de** **Vencimento e outras**,  ficam preenchidas na tabela **CXN**, sendo na tabela **CND** os campos referente ao Fornecedor/cliente **(CND\_FORNEC e CND\_CLIENT)** ficam em branco, como no Browse.

A rotina CNTA121 se utiliza de tabelas acessórias para gravação de informações que antes eram gravadas apenas na tabela CND. Estas tabelas podem ser conhecidas no artigo: [Ciclo de Vida - CNTA120](https://tdn.totvs.com/x/suVeI)

**Obs.1:**

Na rotina **CNTA121**, é possível também visualizar no Browse as medições realizadas pela rotina **CNTA120 (Medição)**, cujo Fornecedor/Cliente ficam visíveis no Browser para consulta. Mas o contrário não ocorre, as medições realizadas pela rotina **CNTA121 (Nova Medição)**, não ficam disponíveis para consulta na rotina **CNTA120 (Medição)**.

**Obs.2:**

No Browse da rotina **CNTA121** são apresentadas apenas campos da tabela CND (e não da tabela CXN) sendo que caso se deseje apresentar no browse informações de outras tabela diferentes da CND do cadastro da medição, deve-se avaliar a possibilidade através de customização/campos customizados.

**Obs.3:**

Assim como os campos acima reportados que não são mais gravados na tabela CND da medição, também não é mais gravado nesta tabela o campo ***CND\_PEDIDO***, que agora é gravado em tabela acessória da rotina.

Para verificação das tabelas utilizadas na rotina de Medição (CNTA121), orientamos verificar o artigo abaixo:

[Ciclo de Vida - CNTA120](https://tdn.totvs.com/pages/releaseview.action?pageId=543090098)

**Obs.4:**

Caso se deseje a visualizaçao de informações no Browse da rotina de Medição (CNTA121) que hoje não estão disponíveis na tabela CND, a possibilidade é através de customização da rotina com a criação de campos customizados e o desenvolvimento de customização para gravação de informações desejadas nestes campos, não sendo recomendado o uso dos campos padrões já existentes para gravação de informação via customização.

*Nota:*

*O Suporte Protheus não auxilia no desenvolvimento de customizações. É recomendado que realize junto a um desenvolvedor.*

***Saiba Mais:***

[Ciclo de Vida - CNTA120](https://tdn.totvs.com/pages/releaseview.action?pageId=543090098)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Rotina Nova Medição CNTA121](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037700393)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotinas de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
