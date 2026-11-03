---
content_hash: c70a2eff087206c1c214e32e19564bfe5c56a104b677ce806e1fc7a720f5cf64
fetched_at: '2026-06-29T00:05:45.034592+00:00'
page_id: '1002495035'
product: rm
source: tdn-rm
title: Serviço de seleção de Regras Tributárias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1002495035
version: 2
---

## **Conteúdo**

**3Conteúdo**

## **1. O que é**

O **Serviço de seleção da Regra Tributária** é um recurso do **TOTVS Gestão Fiscal** que auxilia no preenchimento automático do campo *"Regra Tributária"* no Cadastro do Movimento, utilizando informações previamente registradas no sistema.

Esse preenchimento segue uma regra definida, com base em dados de entrada específicos, conforme o fluxo descrito abaixo. O objetivo é aplicar, automática, a Regra Tributária que será incidir sobre a operação.

## **2. Regras**

As regras de seleção das regras tributárias possuem os seguintes grupos: Tipo de operação, Participante (cliente e empresa/filial), Localidade (estado e cidade/município) e produto (produto e classificação fiscal de bens e serviços) e são preenchidas conforme descrito na documentação de Cadastro de Regras tributárias: Regras de seleção e Detalhes da Regra Tributária (<https://tdn.totvs.com/pages/releaseview.action?pageId=939252927>).

  

Este serviço é consumido na tela de edição do item de movimento através do acionamento da lista de seleção de **Regras tributárias** (lookup). Ao acioná-lo, abrir a lista para a seleção de um registro, o Nucleus reunirá uma série de informações, encapsulará em um conjunto de dados (similar ao que é realizado para a Natureza de operação no movimento/item do movimento) e este serviço será consumido recebendo tais informações.

O serviço fará uma avaliação dos valores cadastrados para as regras de seleção das regras tributárias contrapondo-os com os dados enviados pelo registro de origem, em nosso exemplo o movimento/item de movimento, pontuará cada regra tributária, selecionará aquelas de maior pontuação e as retornará ao chamador (no caso a lista de seleção de **Regras tributárias** do item de movimento). O chamador processará tais registros formatando-os para apresentá-los na lista de seleção de regras tributárias de maneira a apresentá-las ao usuário para seleção de um dos registros (caso retorne apenas um registro então já o selecionará no controle de regra tributária do item de movimento).

O serviço, basicamente, filtra e retorna uma lista de regras tributárias considerando os valores do registro original (por exemplo movimento) comparando-os com os itens dos grupos das regras de seleção das regras tributárias ((Tipo de operação, Participante, Localidade, Produto -  ver documentação logo acima), atribui pontos a tais regras tributárias e retorna as que mais pontuarem. Caso no consumo deste serviço seja informada a natureza de operação (CFOP) e esta tenha uma regra tributária associada então tal regra será retornada, caso contrário (natureza não informada e/ou não existe regra associada à natureza) o serviço funcionará conforme descrito.

 

As regras tributárias para avaliação/pontuação serão recuperadas observando as regras tributárias ativas e o período de vigência relativo à data de lançamento (fiscal) do movimento.  
As demais informações do movimento necessárias para avaliação junto as regras de seleção são: o cliente e filial do movimento, estado e cidade/município informados no "Local de operação" do movimento, o produto do item de movimento e a "Classificação fiscal de bens e serviços" vinculado ao produto do item de movimento e o tipo de operação.

   

A avaliação compete de verificar se os valores do registro original, por exemplo o movimento, estão entre os itens dos grupos informados nas regras de seleção. Caso estejam, recebem um peso/ponto, caso contrário não pontuam e tal regra tributária é descartada da seleção. Com exceção a regra de "Tipo de operação" é necessário que o registro original se enquadre em todas os grupos das regras de seleção para pontuar, caso contrário tal regra tributária é descartada.

Ao final da avaliação/pontuação de todas as regras tributárias o serviço identifica a maior pontuação e retorna todas as regras tributárias que atingiram tal pontuação (as que empataram com a maior pontuação) ou uma lista vazia caso não identifique nenhuma compatibilidade.

Para conhecer os "pesos" aplicados a cada Regra de seleção, visita a documentação do .
