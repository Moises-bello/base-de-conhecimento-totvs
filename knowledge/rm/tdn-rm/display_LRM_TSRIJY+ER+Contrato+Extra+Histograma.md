---
content_hash: caa63a87f5f93d4cb9af30eba07fcffac4e52ab71232d1c844e8e875e1c70d5f
fetched_at: '2026-06-29T00:06:07.878462+00:00'
page_id: '201739527'
product: rm
source: tdn-rm
title: TSRIJY ER Contrato Extra Histograma
type: documentation
url: https://tdn.totvs.com/display/LRM/TSRIJY+ER+Contrato+Extra+Histograma
version: 49
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Totvs Obras e Projetos | **Módulo** | Contratos |
| **Segmento Executor** | Construção e Projetos | | |
| **Chamado** | TSRIJY | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   

## Objetivo

 Possibilitar a criação de contratos onde podem ser consumidos apenas insumos que não façam parte do Histograma do Projeto.

## Definição da Regra de Negócio

O Contrato Extra-Histograma possibilita que sejam criados contratos onde podem ser consumidos apenas insumos que não façam parte do Histograma do Projeto, ou seja, os insumos que não constam na Curva ABC de Insumos do Projeto.

Ao acessar a tela de criação/edição do contrato, além das finalidades já existentes, estará disponível a finalidade "Contrato Extra-Histograma", lembrando que uma vez salvo o contrato, sua finalidade não poderá ser alterada. O Contrato Extra-Histograma é sempre A Pagar e somente os campos relativos ao Número do Contrato, Fornecedor, Data do Contrato e Data de Início e Fim serão obrigatórios em contratos dessa finalidade. 

Na rotina do Contrato Extra-Histograma é utilizado o processo "Associar Objetos ao Contrato" só que, diferente do Contrato de Insumos, neste contrato serão associados insumos locais pertinentes ao projeto corrente, mas que não estejam associados à Curva ABC de Insumos e nem estejam na planilha de tarefas.  

Como este tipo de contrato somente permite insumos que não estejam na Curva ABC é importante que o cálculo do projeto seja executado previamente para que os valores da Curva ABC sejam atualizados. 

Na  "Associação de Objetos ao Contrato" inicialmente será apresentada a tela com o filtro para seleção dos Grupos de Custo locais dos insumos a serem associados, podendo ser selecionados um ou mais grupos. 

Ao Avançar, será exibida uma lista de todos os insumos do projeto que não possuem histograma, filtrada pelos Grupos de Custo selecionados.

O 'Custo Unitário' dos insumos será automaticamente preenchido com o resultado do 'Preço do Insumo x Lei Social do Insumo' enquanto que o 'Valor Unitário' será preenchido com o resultado do 'Custo Unitário x BDI do Projeto'.

Como os insumos disponíveis para contratação não possuem histograma, a sua 'Quantidade Orçada' será sempre 0 (zero).

No momento da associação de objetos, é possível editar a quantidade contratada e o valor unitário contratado dos objetos.

Neste processo, os objetos já associados ao contrato corrente serão exibidos na cor azul.

Caso utilize o controle de status dos contratos, a Associação de Objetos ao Contrato somente poderá ser realizada caso o contrato esteja com o status "Em Negociação".

Através do Anexo ‘Objetos do Contrato’ é possível visualizar todos os objetos que estão associados ao contrato, bem como as quantidades consumidas de cada objeto. Através deste anexo também poderá ser efetuada a exclusão dos objetos do contrato, desde que ainda não tenham sido consumidos.

Para efetuar o consumo dos objetos de um Contrato Extra-Histograma deve-se, através dos períodos gerados, selecionar o período para consumo e utilizar o processo ou o botão "Consumir Objetos do Contrato". Nesta opção será apresentada a lista de objetos vinculados ao contrato selecionado, possibilitando associar um objeto ou vários objetos de uma só vez, sendo que é necessária a confirmação da associação de vários objetos. Selecionados os objetos, aparecerá a opção para identificar em qual tarefa cada objeto será consumido e o consumo efetuado.

Diferente do contrato de insumos onde somente é permitido o consumo em tarefas às quais o objeto está vinculado na planilha de atividades, no Contrato Extra-Histograma o objeto poderá ser consumido em qualquer tarefa, etapa ou obra do projeto.

No processo "Consumir Objetos do Contrato" além da aba dos 'Objetos Associados ao Contrato', onde se faz o consumo dos mesmos, está também disponível a aba 'Objetos Consumidos no Período'. Em ambas as abas é possível visualizar informações como: Quantidade Contratada, Valor Contratado, Quantidade Consumida, Valor Consumido, Percentual Consumido e Saldo do Valor e da Quantidade. Na primeira aba os valores são dispostos levando em consideração todo o contrato e na segunda aba o período em questão.

Os períodos consumidos são marcados pelo símbolo V na cor azul sobre o símbolo do período.

Os Contratos Extra-Histograma não são considerados no saldo do Fluxo de Desembolso.

Os insumos associados e/ou consumidos nos Contratos Extra-Histograma posteriormente poderão ser vinculados a qualquer composição ou tarefa, podendo inclusive ser comprados ou associados em um Contrato de Insumos, sendo que a quantidade já associada ao Contrato Extra-Histograma será considerada e abatida da quantidade planejada, ficando assim disponível para compra ou contratação em um Contrato de Insumos somente a quantidade restante. 

Os demais anexos e processos do Contrato Extra-Histograma são os mesmos do Contrato de Insumos. 

Somente terão permissão para criar e/ou editar os Contratos Extra-Histograma os usuários cujo perfil possua liberação para essa rotina em *"Serviços Globais > Segurança > Perfis > Projetos > Construção e Projetos"* (item 05.01.02.01.67 - Associar Objetos ao Contrato Extra-Histograma do 'Acesso a Menus').

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Criação/Edição dos Contratos | Alteração | Controle > Contratos > Contrato | Conforme especificado nas Regras de Negócio |
| Associação de Objetos ao Contrato | Alteração | Controle > Contratos > Contrato > Processos > Associar Objetos ao Contrato | Conforme especificado nas Regras de Negócio |
| Consumo de Objetos do Contrato | Criação | Controle > Contrato > Contratos > Processos > Consumir Objetos de Contrato | Conforme especificado nas Regras de Negócio |
| Exclusão de Insumos Não Utilizados | Alteração | Orçamento > Insumos > Excluir Insumos Não Utilizados | Conforme especificado nas Regras de Negócio |
| Criação/Edição de Perfis | Alteração | Servços Globais > Segurança > Perfis | Conforme especificado nas Regras de Negócio |

## Protótipos de Tela

**Protótipo 01 - Criação/Edição de Contratos**

Obs.: Não houve modificação nas demais telas do contrato.

****Protótipo 02 - Perfil****

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
