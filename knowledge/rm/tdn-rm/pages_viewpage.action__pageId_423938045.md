---
content_hash: 171db47037903fe98d585eca26739810e5d6ec238410d33a1e272c280fb0ffb9
fetched_at: '2026-06-29T00:09:25.169780+00:00'
page_id: '423938045'
product: rm
source: tdn-rm
title: Apontamento via Código de Barras por Atividade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938045
version: 2
---

Ao fazer a leitura do código de barras para apontamento de atividade será disponibilizada a tela de apontamento de atividade, onde poderão ser inseridos todos os dados de apontamento.  
É disponibilizado no sistema  um relatório padrão de etiquetas de código de barras, caso seja de interesse, pode-se personalizar relatórios específicos conforme o layout abaixo: 

**Layout Código de Barras por Atividade**  
  
 ID!OP-0002/11!001.01!BASE!0  
  
 Onde:  
**ID**: Identificador padrão de início de código de barras  
**!:** Separador padrão  
**OP-0002/11**: Código da Ordem de Produção  
**001.01**: Código da Estrutura a ser apontada  
**BASE:** Modelo da Estrutura  
**0:** Identificador da atividade   
  
***Observação*:**  Os campos Ordem de Produção, Código da Estrutura, Modelo da Estrutura e Identificador da Atividade podem ser verificados via consulta SQL na tabela KAPTOCODBARRAETIQUETAS, que é preenchida ao realizar o processo de geração de etiquetas.  
  
**Apontamento de recursos da atividade via Código de Barras:**No apontamento via Código de Barras por Atividade também é possível informar através da leitura de códigos de barras todos os recursos utilizados na atividade da ordem de produção. Esses recursos com seus layouts são:

* **Material Apontado (Material Consumido, Perda de Material e Subproduto Gerado)**

*****Atenção!*****O layout para material consumido, perda de material e subproduto gerado é o mesmo, o que define para onde que o produto está sendo apontado é a aba que está em foco no momento da leitura do código de barras.  
  
 Layout:  
 MA!1032!  
Onde:  
**MA:** Identificador padrão de Material apontado  
**!:** Separador padrão  
**1032:** Identificador do Produto  
  
 No Material Consumido e Perda de Material também é possível informar o lote e/ou número de série juntamente com o produto que está sendo apontado, conforme os layouts abaixo:

* **Material Controlado por Lote**

MA!1044!!125!  
Onde:  
**MA:** Identificador padrão de Material apontado  
**!:** Separador padrão  
**1044:** Identificador do Produto  
**125:** Identificador do Lote apontado

* **Material Controlado por Número de Série**

MA!1045!!!0001  
Onde:  
**MA:** Identificador padrão de Material apontado  
**!:** Separador padrão  
**1045:** Identificador do Produto  
**0001:** Número de Série apontado

* **Material Controlado por Lote e Número de Série:**

MA!1046!!126!0001  
Onde:  
**MA:** Identificador padrão de Material apontado  
**!:** Separador padrão  
**1046:** Identificador do Produto  
**126:** Identificador do Lote apontado  
**0001:** Número de Série apontado

**Apontando Lote e Número de Série separadamente:**

Também é possível apontar lote e número de série dos produtos separadamente, ou seja, após já ter inserido o produto pode-se informar o lote e/ou número de série daquele produto através da leitura do código de barras.

* **Lote apontado**

ML!1044!!125  
Onde:  
**ML:** Identificador padrão de Lote apontado  
**!:** Separador padrão  
**1044:** Identificador do Produto  
**125:** Identificador do Lote apontado

* **Número de Série apontado**

MS!1045!!!0001  
Onde:  
**MS:** Identificador padrão de Número de Série apontado  
**!:** Separador padrão  
**1045:** Identificador do Produto  
**0001:** Número de Série apontado

* **Número de Série apontado (com lote)**

MS!1046!!126!0001  
Onde:  
**MS:** Identificador padrão de Lote e Número de Série apontados  
**!:** Separador padrão  
**1046:** Identificador do Produto  
**126:** Identificador do Lote apontado  
**0001:** Número de Série apontado

* **Material Controlado por Grade Antiga:**Caso o material apontado tenha controle de grade antiga, o sequencial do item de grade deverá sempre ser informado após o Identificador do Produto. Layout  para apontamento de material com grade antiga :

MA!1043!3!  
Onde:  
**MA:** Identificador padrão de Material Apontado  
**!:** Separador padrão  
**1043:** Identificador do Produto  
**3:** Sequencial do Item de Grade

* **Mão de Obra Alocada:**Para informar mão de obra alocada na atividade através da leitura de código de barras, o layout do mesmo deve ser conforme abaixo:

MO!FA-001  
Onde:  
**MO:** Identificador padrão de Mão de Obra  
**!:** Separador padrão  
**FA-001:** Código da Mão de Obra

* **Equipamento Alocado:**Para informar equipamento alocado na atividade através da leitura de código de barras, o layout do mesmo deve ser conforme abaixo:

EQ!CEQP-001  
Onde:  
**EQ:** Identificador padrão de Equipamento  
**!:** Separador padrão  
**CEQP-001:** Código do Equipamento

* **Índice de Registro de Produção:**Para informar índice de Registro de Produção na atividade através da leitura de código de barras, o layout do mesmo deve ser conforme abaixo:

RP!002  
Onde:  
**RP:** Identificador padrão de Índice de Registro de Produção  
**!:** Separador padrão  
**002:** Código do Índice de Registro de Produção

* **Registro de Qualidade:**Para informar Registro de Qualidade na atividade através da leitura de código de barras, o layout do mesmo deve ser conforme abaixo:

RQ!002!ATV-01!MO-002  
Onde:  
**RQ:** Identificador padrão de Índice de Registro de Qualidade  
**!:** Separador padrão  
**002:** Código do Motivo de Registro de Não Conformidade  
**ATV-01:** Código da atividade corretiva  
**MO-002:** Código da Mão de Obra responsável

* **Parada de Atividade (Sem Agente de Parada):**Para informar parada de atividade(sem agente) através da leitura de código de barras, o layout do mesmo deve ser conforme abaixo:

PA!QUE-01!  
Onde:  
**PA:** Identificador padrão Parada de Atividade  
**!:** Separador padrão  
**QUE-01:** Código da Razão de Parada

* **Parada de Atividade (Com  Agente de Parada):**Para informar parada de atividade(com agente) através da leitura de código de barras, o layout do mesmo deve ser conforme abaixo:

PA!QUE-01!FA-002  
Onde:  
**PA:** Identificador padrão Parada de Atividade  
**!:** Separador padrão  
**QUE-01:** Código da Razão de Parada  
**FA-002:** Código do Agente de parada  
**Dica:**É possível navegar entre as abas na tela de apontamento utilizando atalhos do teclado, os mesmos são:

|  |  |
| --- | --- |
| **Aba** | **Atalho** |
| Cabeçalho | ALT + D |
| Material Consumido | ALT + M |
| Perda Material | ALT + P |
| Subproduto Gerado | ALT + S |
| Trabalho Efetivo | ALT + T |
| Registro de Produção | ALT + Q |
| Parada de Atividade | ALT + I |
| Apontamentos (Habilitada na Correção) | ALT + A |

Informações Adicionais

* # [Como Fazer – Apontamento via código de barras por atividade](http://tdn.totvs.com/pages/viewpage.action?pageId=42043440)
* # [Como Fazer - Apontamento de materiais via código de barras](http://tdn.totvs.com/pages/viewpage.action?pageId=42043437)
* # [Como Fazer – Apontamento de índices de registro de produção e qualidade via código de barras](http://tdn.totvs.com/pages/viewpage.action?pageId=42043439)
