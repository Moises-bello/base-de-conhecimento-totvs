---
content_hash: 5db7dad8e0e73d786b479c3a95f665faa5c2245b1a1f48e8d9ec603a60a26c50
fetched_at: '2026-06-29T00:11:16.435932+00:00'
page_id: '668180079'
product: rm
source: tdn-rm
title: Integrar Aquisições Por Contrato (Arrendamento Mercantil)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=668180079
version: 27
---

Este processo tem como objetivo integrar os contratos de imobilizados realizadas pelo módulo Gestão de Estoque, Compras e Faturamento com o Sistema de Gestão Patrimonial, cadastrando os patrimônios e preparando-os para cálculos de depreciação, inventário, etc.

A inserção dos patrimônios tem como base alguns dados do contrato escolhido, como por exemplo: Data de Aquisição é referente a Data do Contrato, Valor do Patrimônio é igual ao Valor Presente do item do contrato, a quantidade do item de contrato será a quantidade do patrimônio no patrimônio integrado/criado.

Após a integração dos bens, se a quantidade de patrimônios integrados for superior a UM MIL o sistema não fará cálculos de depreciação automaticamente. Nesse caso, o usuário terá que disparar os cálculos.

440320

a,b,c,d,eaOpções de seleção (Filtros)

Utilize uma ou mais opções de filtro para seleção dos contratos que deseja integrar com o módulo patrimonial:

* Data do contrato - Os contratos listados com base nesse filtro serão aqueles cujo a Data do Contrato estejam entre a Data Inicial e Data Final. Por padrão é apresentado o período patrimonial em aberto.
* Código do contrato - Nesse campo deve ser informado o código exato do contrato que deseja listar.
* Fornecedor - Serão listados apenas os contratos referentes ao fornecedor escolhido.

         

bSeleção de Contratos

Nesta etapa aparecerão todos os contratos que atendem aos filtros utilizados na etapa anterior. Selecione aqueles que deseja integrar e clique em Avançar.

cTipos de Campos

Nos campos **Descrição do Patrimônio**, selecione uma das opções da lista para preenchimento dos mesmos no Patrimônio que será criado.

Algumas considerações sobre as opções:

* ****Gerar código de patrimônio e numero do patrimônio automaticamente****

  Marcando essa opção o sistema irá gerar o número do patrimônio e o código do patrimônio automaticamente, respeitando sempre o título amarrado ao grupo de patrimônio ou ao produto. O número do patrimônio irá receber o maior valor inteiro da base acrescido de 1, porém se não houver valores inteiros receberá 1. Vale ressaltar que o número do patrimônio é gerado automaticamente considerando os parâmetros de sistema, por exemplo, ele não será 1 se o sistema estiver parametrizado para gerar o número do patrimônio igual ao código do patrimônio.

  Observação: Se esta opção não for marcada a integração ficará pendente para edição no menu Relatórios/Integrações → Integrar Aquisições Pendentes.
* **Gerar o código do patrimônio a partir do título do patrimônio definido no produto**

Com essa opção o sistema usará o título amarrado direto dos cadastros de produto, existente no módulo Gestão de Estoque, Compras e Faturamento, no lugar do título informado em "Cadastros Grupo de patrimônios Contábeis" do módulo Patrimonial.

* **Trazer o rateio de centro de custo do item do contrato para o rateio gerencial do Patrimônio**

Ao marcar essa opção o sistema irá considerar o rateio gerencial no patrimônio, porém, caso o rateio gerencial não esteja configurado no centro de custo origem, esse item não será integrado.

* **Trazer o centro de custo do item do contrato para o patrimônio**

Essa opção passa a ser obrigatória caso o parâmetro do sistema **Tornar Centro de Custo Obrigatório** esteja marcado.

* **Trazer o departamento do item do contrato para o patrimônio**

Essa opção passa a ser obrigatória caso o parâmetro do sistema **Tornar Departamento Obrigatório** esteja marcado.

* **Utilizar Localidade**

A localidade informada será associada ao(s) patrimônio(s) gerado(s) após a execução do processo.

Informar A Localidade passa a ser obrigatório caso o parâmetro do sistema **Tornar Localização Obrigatória** esteja marcado.

Caso parâmetro do sistema **Vincular** **Localização com Responsável**esteja marcado, o Responsável vinculado ao patrimônio será buscado da Localidade e não da tela.

Caso parâmetro do sistema **Vincular Localização com Centro de Custo** esteja marcado, o Centro de Custo vinculado ao patrimônio será buscado da Localidade quando a opção **Trazer o centro de custo do item do contrato para o patrimônio**estiver desmarcado, ou não houver Centro de Custo vinculado ao Item de Contrato.

* **Utilizar Responsável**

O responsável informado será associado ao(s) patrimônio(s) gerado(s) após a execução do processo.

Informar o Responsável passa a ser obrigatório caso o parâmetro do sistema **Tornar Responsável Obrigatório** esteja marcado.

Atenção:  
Ao integrar o Sistema de Gestão Patrimonial com o sistema de Compras/Estoque, o sistema estará validando se o patrimônio está com o título inativo, ou seja, se no sistema de Compras estiver utilizando um Grupo de patrimônios que possui um título inativo no Sistema de Gestão Patrimonial, não será possível concluir a integração.

Esta condição é verdadeira desde que a preferência "Não incluir bens em títulos INATIVOS" esteja habilitada.

Veja Também

* Patrimônios
* Integrar Aquisições Pendentes
