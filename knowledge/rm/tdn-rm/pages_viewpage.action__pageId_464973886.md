---
content_hash: 404484d9bf60a79d3aa77fdf176041123ca92d4ef27d4d15e90928b582c5e4e1
fetched_at: '2026-06-29T00:10:15.755791+00:00'
page_id: '464973886'
product: rm
source: tdn-rm
title: Copiar Ordem de Serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=464973886
version: 1
---

A cópia da Ordem de Serviço permite ao usuário gerar uma Ordem de Serviço a partir de uma ordem já existente.   
Para realizar a cópia da ordem de serviço o usuário deverá acessar a tela de visão da ordem de serviço, selecionar a Ordem de Serviço que deseja fazer a cópia e clicar no botão "Copiar OS", uma nova OS será gerada com o número sequencial do número da Ordem de Serviço.   
Para ter acesso a esta funcionalidade o usuário deverá ter permissão.   
Para conceder permissão ao usuário basta acessar o Menu Cadastros | Segurança | Perfis e dar permissão ao usuário na tag "Copiar Ordem de Serviço".  
***Atenção!*** Como a Ordem de Serviço esta utilizando a interface do movimento, o sistema fará, para cópia da ordem, as mesmas validações de campo que ele faz quando se esta gerando um movimento. Se existir na OS pai algum campo obrigatorio que não esteja preenchido o sistema emitirá uma mensagem ao usuário e não fará a cópia da nova ordem até que o usuário preencha todos os campos obrigatórios da Ordem de Serviço.

**Acessórios da Ordem de Serviço**

A tela acessórios da ordem de serviço exibe todos os acessórios da ordem de serviço. Esses acessórios são os acessórios referentes ao objeto de manutenção da ordem de serviço.   
Para exibir a tela de acessórios o usuário terá que clicar no botão "Acessórios" que se encontra na tela de visão da ordem de serviço ou na tela de edição da ordem de serviço.  
Ao editar os acessórios do objeto de manutenção o usuário terá que executar o processo "Atualizar acessórios" que fica no menu Processos para que o tela de acessórios seja atualizada com as modificações realizadas.

**Alterar Indicador da Ordem de Serviço**

A funcionalidade alterar indicador de uso na Ordem de Serviço permite que o usuário vincule ou desvincule um indicador de uso a uma ordem de serviço.  
Essa funcionalidade esta disponível na aba indicador de uso da edição da ordem de serviço e para acessá-la o usuário deverá clicar em qualquer área da aba "Indicadores de Uso"com o botão direito do mouse onde aparecerá duas opções:   
Vincular indicador de uso: A opção "Vincular Indicador de uso" associa um indicador de uso a ordem de serviço.  
e Desvincular indicador de uso: A opção "Desvincular indicador de uso" torna o indicador de uso não mais associado a O.S, ele será excluído da aba "Indicadores de uso".  
A vinculação e desvinculação são feitas numa tela onde são listados os indicadores de uso que podem ser selecionados pelo usuário.   
No menu Parâmetro do RM Officina, na aba ordem de serviço foi adicionado um novo parâmetro "Não buscar indicador de uso na O.S. automaticamente".   
Ao marcar esse parâmetro, ao abrir uma nova OS o indicador de uso do objeto não vai ser preenchido automaticamente e o usuário terá de faze-lo de forma manual, já desmarcando o parâmetro, toda vez que for aberta uma OS o sistema preencherá o campo indicador de uso automaticamente, porem se o usuário optar por alterar o indicador de uso pode faze-lo com a funcionalidade "Vincular Indicador de Uso".  
***Observação***: Se o parâmetro "Campo Indicador de Uso na OS é obrigatório" estiver marcado, não será possível desvincular um indicador de uso pois ao marcar o parâmetro fica obrigatório existir um indicador de uso na Ordem de Serviço.
