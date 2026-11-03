---
content_hash: d87378f5b1da4ef126821cf80973c57dde20c324b9b44b8360f9b43073cb2d50
fetched_at: '2026-06-29T00:09:28.080303+00:00'
page_id: '423938653'
product: rm
source: tdn-rm
title: Agrupamento de Lançamentos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938653
version: 15
---

***Atenção!***

Esta funcionalidade só está disponível para as bases já migradas para o Novo Modelo do BackOffice.  
   
O processo de Agrupamento de Lançamentos tem como objetivo agrupar várias partidas comuns existentes nos *Lançamentos* de um mesmo lote ou então agrupar somente *Partidas* comuns de um mesmo lançamento contábil em uma única partida, reduzindo assim o volume de lançamentos da contabilidade e conseqüentemente dos livros contábeis.

É possível selecionar as partidas/lançamentos existentes dentro do lote a serem consideradas para o processo utilizando-se um Filtro por datas, para isto deve-se informar uma data inicial e data final, restringindo assim as partidas/lançamentos a serem consideradas para o agrupamento. Se nenhuma faixa de datas for informada, todas as partidas/lançamentos existentes no lote serão automaticamente consideradas para o processo de agrupamento.

Conforme as opções disponíveis, esse processo permite realizar o agrupamento de **Lançamentos** contábeis ou **Partidas** idênticas, de acordo com as formas de agrupamento selecionada:

* Agrupar débitos com créditos em uma única partida
* Agrupar partidas a débito
* Agrupar partidas a crédito.

Se desejar que o processo de agrupamento seja aplicado a determinada Filial, basta marcar a opção *Ativar Filtro* e selecionar as Filiais desejadas. Caso a opção não seja marcada, o processo será aplicado para todas as filiais existentes nos lançamentos/partidas.  
Você pode utilizar também os *Filtros* Genéricos. Neste caso você deverá criá-los podendo utilizar um leque amplo de opções para seleção dos lançamentos/partidas para o processo de agrupamento ou selecionar um filtro já existente.

É possível também utilizar *Filtros para Seleção de Contas Contábeis*. Caso sejam utilizados, o processo será aplicado somente para lançamentos/partidas que tenham as contas contábeis informadas no filtro para o débito e/ou para o crédito.

Os dados informados nos vários filtros disponíveis no processo de agrupamento serão sempre acumulativos, por isto preste bastante atenção nos dados informados. Talvez fique mais simples e claro utilizar um único filtro genérico para todas as seleções desejadas.

Você pode ainda informar um novo 'Documento' e um novo 'Complemento' para as partidas que serão agrupadas, no entanto, as partidas originais, ao serem consultadas, mostrarão o 'Documento' e o 'Complemento' originais.

Além disso, é possível também:

* Agrupar mesmo se complementos de histórico forem diferentes
* Agrupar mesmo se o campo "Contrapartida" for diferente (este campo será limpo após o agrupamento)

**Regras para o agrupamento:**

O agrupamento de lançamentos ou partidas será permitido apenas quando todos os seguintes campos forem idênticos:

* Data
* Filial
* Conta contábil
* Departamento
* Centro de custo
* Histórico
* Complemento
* Contrapartida
* Participante
* Dimensão de Cliente/Fornecedor

**Atenção!**

**1**- Este processo só poderá ser realizado para lançamentos que ainda estejam em lote (lote N) sendo possível executá-lo somente em um único lote por vez e, no lote selecionado, não poderá haver diferenças entre débitos e créditos.

**2**- No momento da execução do Agrupamento de Lançamentos, além das regras inerentes a este processo, o sistema fará também a leitura do parâmetro do sistema '**Aplicar regra de validação de lançamentos no Agrupamento de Lançamentos**' que está disponível nos Parâmetros do TOTVS Gestão Contábil, nas opções referentes à Lançamentos Contábeis. Se este parâmetro estiver marcado o sistema fará também a validação das regras de inclusão de lançamentos (amarrações e fórmulas) e só fará o agrupamento dos lançamentos que estiverem satisfazendo às amarrações e fórmulas existentes. Com este parâmetro desmarcado, as amarrações e fórmulas existentes não serão validadas pelo processo de Agrupamento de Lançamentos. Vale ressaltar que, dependendo do volume de informações da base de dados, executar o processo de Agrupamento de Lançamentos com este parâmetro habilitado, pode comprometer a performance deste processo.

**Observação:**

O Agrupamento de Lançamentos hoje está habilitado para todos os módulos migrados para a plataforma .Net, restrito somente ao módulo TOTVS Folha de Pagamento, pois este possui um módulo próprio de rastreabilidade não permitindo o agrupamento pelo TOTVS Gestão Contábil.

Mais Informações

* Agrupar Lançamentos
* Agrupar Partidas
* Regras e exemplos de Agrupamentos
* [Parametrização para o Fracionamento de Jobs para o processo de Agrupamento de Lançamentos Contábeis](https://tdn.totvs.com/pages/viewpage.action?pageId=960999980)
