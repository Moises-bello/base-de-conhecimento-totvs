---
content_hash: b3300968247ffd6e7dbfbe612b3d321b0ebb23b6f7516d4c2a9bfc141dd85c5c
fetched_at: '2026-06-29T00:06:01.855852+00:00'
page_id: '198941062'
product: rm
source: tdn-rm
title: Fórmula Visual (TOTVS Gestão de Estoque, Compras e Faturamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198941062
version: 26
---

Mais informações sobre documentação da Frame explicando sobre Fórmula Visual, [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=237383316)

Disponibilização de atividades de Fórmula Visual para permitir a elaboração de Fórmulas Visuais que chamem os serviços disponíveis na tela de movimentos. Os serviços disponibilizados neste ciclo são:

**Inclusão de informações no movimento**

Para que a inclusão de informação no movimento ou item do movimento seja realizada é necessário a utilização da atividade de **Salvar Movimento** no final do fluxograma.

Movimento

* Inclusão Rateio Centro de Custo do Movimento
* Inclusão Rateio Departamento do Movimento
* Salvar Movimento

Item do Movimento

* Inclusão Item Movimento - É necessário passar IDMOV como -1

Para utilizar as atividades abaixo é necessário chamar a atividade **Inclusão Item Movimento** primeiro e passar IDMOV como 0.

* Inclusão Item Grade Movimento
* Inclusão Item Lote Movimento
* Inclusão Item Número Série Movimento
* Inclusão Rateio Centro de Custo do Item Movimento
* Inclusão Rateio Departamento do Item Movimento

**Alteração de informações**

Para que a alteração de informação no movimento ou item do movimento seja realizada é necessário a utilização da atividade de **Salvar Alteração Movimento** no final do fluxograma.

Movimento

Para fazer qualquer alteração no movimento é necessário que a primeira atividade no fluxograma seja a de **Alteração Movimento**.

* Alteração movimento
* Alteração Rateio Centro de Custo do Movimento
* Alteração Rateio Departamento do Movimento
* Salvar Alteração Movimento

Item do Movimento

Para fazer qualquer alteração no item do movimento é necessário que a primeira atividade no fluxograma seja a de **Alteração Movimento**, seguida pela de **Alteração Item Movimento**.

* Alteração Item Movimento
* Alteração Item Grade Movimento
* Alteração Item Lote Movimento
* Alteração Item Número Série Movimento
* Alteração Rateio Departamento do Item Movimento
* Alteração Rateio Centro de Custo do Item Movimento

Importante

As atividades de alteração de movimento e item do movimento não permitem alterar registros que possuem relacionamento. Para alterar tais movimentos é necessário usar as atividades **Ler Registro** e **Salvar Registro**, caso contrário as entidades vinculadas ao item do movimento serão perdidas.

**Carregamento de Parâmetros**

Através das atividades abaixo é possível utilizar as informações dos parâmetros nas fórmulas visuais.

* Parâmetros Geral do Movimento
* Parâmetros Movimento por Filial
* Parâmetros Tipo de Movimento

**Contexto**

Em processos que utilizam assinantes (subscriber) é possível consultar ou atribuir alguma informação ao contexto através das atividades abaixo.

* Consulta valor no contexto do movimento (Assinante)
* Atribuir valor no contexto do Assinante/Movimento

**Outras Ações**

* Cancelar Movimento
* Exclusão Movimento

**Inclusão de Fórmulas Visuais**

Acessar TOTVS Gestão de Estoque, Compras e Faturamento | Guia Gestão | Fórmula Visual | Fórmula Visual, as Atividades de Fórmulas Visuais estarão disponíveis na Aba ‘Atividades’.  
O usuário deverá criar as fórmulas visuais de acordo com a necessidade e vincular em processos do tipo de movimento desejado.

**Dicas**

**Criação de Fórmulas Visuais Dinâmicas**

Para executar uma FV de acordo com o registro selecionado ao invés de passar um IDMOV específico, basta fazer a seguinte configuração:

1. Na propriedade IDMOV selecione o botão "..."
2. Clique uma vez sobre Fields[0] habilitando a edição do texto e troque o valor 0 por "IDMOV" (entre aspas)
3. Clique em "+" a esquerda do campo Fields["IDMOV"] para expandir a estrutura e selecione AsInteger
4. Clique em OK

**Criação de Fórmulas Visuais para processamento de vários registros**

Para isso é necessário a utilização das atividades **Para cada Iteração** e **Sequência**.

1. Nas propriedades da atividade **Para cada Iteração** no campo **Lista de Items** selecione Rows dentro de Tables[0] conforme mostrado abaixo.
2. Coloque a atividade **Sequência** dentro da atividade **Para cada Iteração**.
3. A atividade que será executada para cada registro selecionado deverá ser colocada dentro da atividade de **Sequência**. Além disso o valor da sua propriedade IdMov deverá ser editado da seguinte forma:
   1. Clique uma vez sobre Fields[0] que está localizado dentro da rmsForEachActivity para habilitar a edição e substitua o valor 0 por "IDMOV" (entre aspas)
   2. Em seguida selecione AsInteger e clique em OK
