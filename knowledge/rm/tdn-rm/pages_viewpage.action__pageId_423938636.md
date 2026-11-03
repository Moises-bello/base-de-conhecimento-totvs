---
content_hash: 75215043899b77303dd6f405bc45fea14b79d809feac08a246909db641a99f05
fetched_at: '2026-06-29T00:09:28.048166+00:00'
page_id: '423938636'
product: rm
source: tdn-rm
title: Amarração Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938636
version: 5
---

Nesta tela encontra-se o cadastro geral de Filtros de Amarração de Lançamentos. Estes filtros servirão para consistir a criação de lançamentos em seu sistema. Você poderá definir que tipo de lançamento será permitido e os que não serão permitidos no sistema.

**Atenção**

Esta opção funciona em conjunto com o Parâmetro 'Usa regra de inclusão de Lançamentos'.

**Exemplo**

Alguns exemplos de situações que poderão ser criadas:

* Funcionário A, pode realizar lançamentos somente nas Filiais 1 e 2.
* Todos os lançamentos realizados na Filial 3 deverão ter informado um dos Centros de Custo 1 a 6.
* Não será permitido realizar lançamentos utilizando o Histórico Padrão '00001' quando a conta de Débito for do Grupo 1 (Ativo).

Para criar os exemplos acima veja os procedimentos.

1) Informe o Nome do funcionário A no campo Funcionário. Ative o filtro "Selecionar Filial/Departamento" e selecione as Filiais 1 e 2. Marque os campos "Permite Lançamentos" e "Regra Ativa" Toda vez que este usuário criar lançamentos, e for desta filial, o sistema barrará a inclusão destes.

2) Ative o filtro "Selecionar Filial/Departamento", e selecione Filial 3. Em seguida ative o filtro Centro de Custo e marque os Centros de Custo 1, 2, 3, 4, 5 e 6. Marque também os campos "Permite Lançamentos" e "Regra Ativa" Toda vez que um lançamento for criado para a filial 3 e nenhum destes Centros de Custo forem informados, o sistema não permitirá salvar o lançamento.

3) Ative o filtro Histórico e selecione o histórico '00001', em seguida clique sobre a pasta "Filtros de Contas", ativar o filtro "Contas Contábeis / Débito", e selecione a conta 1. Marque o campo "Regra Ativa" e deixe o campo "Permite Lançamentos" desmarcado. Este filtro barrará todo lançamento que tiver uma conta de débito pertencente ao grupo 1 (por exemplo 1.1.1.1.001) e o Histórico '00001'.

**Atenção**

Cuidado para não criar um filtro contradizendo outro, para não correr o risco dos filtros barrarem todos os seus lançamentos. Certifique-se também, antes de criar seus filtros, de que não exista nenhuma fórmula usada como "Regra de Lançamentos" e que esteja "Ativa", contradizendo algum filtro criado, pois neste caso o sistema irá fazer a leitura dos dois e ambos irão prevalecer.

**Exemplo**

Fórmula 01 - Barra os lançamentos na filial 02 para o Usuário Mestre.

Amarração de Lançamentos 01 - Permite que o usuário mestre cadastre lançamentos apenas na filial 2.

Este exemplo fará com que o usuário mestre não consiga cadastrar lançamentos em nenhuma filial.

Para alterar, excluir ou incluir uma Amarração de Lançamento utilize os seguintes ícones: *Barra de Ferramentas*

***Observação***

A utilização de múltiplas Amarrações pode onerar a performance de inclusão/alteração de Lançamentos.
