---
content_hash: 2867dc7f78be35efed5afd65a1fba0fa2f1d83a73595fdf6da0df562fffc8e18
fetched_at: '2026-06-29T00:09:30.897873+00:00'
page_id: '425458555'
product: rm
source: tdn-rm
title: Geração Campanha a partir de Clientes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458555
version: 1
---

**Geração Campanha a partir de Clientes**   
O serviço de gerar campanha de relacionamento possibilita a criação de uma nova campanha de marketing a partir de uma seleção de clientes. Os clientes podem ser do tipo Cliente, Prospect, Aluno, Pessoa, Professor.  
A execução com sucesso do serviço terá impacto diretamente na campanha de marketing, com a criação de um novo registro contendo os clientes selecionados como clientes da campanha. A nova campanha irá refletir as informações fornecidas e será criada com o status "pausada".  
O serviço pode ser acionado a partir da "Lista de Clientes", da tela de visão de "Atendimento", do cadastro de prospect/suspect, e do serviço "Informações de Clientes".  
Para solicitar o serviço através da "Lista de Clientes", deve-se acessar o menu "Grupo de Clientes" ou "Campanha de Marketing". Pelo menos um registro deve ser selecionado para que seja possível a execução do serviço. Na tela de visão é seleciona-se os clientes para os quais se deseja gerar uma nova campanha. Em seguida um *winzard* é apresentado contendo um grid onde é possível visualizar quais foram os clientes selecionados (clientes repetidos não serão mostrados), a coligada do cliente, o código do cliente, o nome do cliente e o tipo do cliente.   
Também são disponibilizados para preenchimento os campos 'Título' (campo obrigatório; deve conter o título da nova campanha), 'Objetivo' (objetivos da campanha), 'Atendente' (campo obrigatório; qual atendente está criando a campanha), 'Data Inicial' (data de início da campanha), 'Data Final' (data fim da campanha), 'Observação' (descrição mais exata dos objetivos da campanha). A execução do serviço só terá prosseguimento após os campos obrigatórios terem sido preenchidos. Caso contrário, uma mensagem será retornada e a execução do serviço será cancelada.   
Caso a solicitação do serviço seja através da tela de visão de "Atendimentos", antes da execução do mesmo será realizada uma verificação da tela de visão à procura de colunas específicas (COLIGADACLIENTE, CODCFO, NOMECLIENTE, TIPO). A verificação é necessária, pois, caso se utilize uma tela de visão de atendimento personalizada, a mesma pode não possuir as colunas mínimas para que o serviço seja chamado. Caso isso ocorra, uma mensagem irá informar a necessidade de colunas.   
O serviço é executado a partir da seleção de atendimentos, onde cada atendimento deverá ter um cliente de algum tipo. Apenas os clientes de cada atendimento são mostrados no *grid* do processo (clientes repetidos não serão mostrados). Ao final da execução, uma nova campanha será criada.   
Solicitando o serviço a partir do cadastro de prospect/suspect, o processo irá apenas filtrar os registros que sejam ou do tipo prospect ou do tipo suspect. Os que estiverem inativos ou tiverem o campo em branco (nulo) serão desconsiderados para a execução. Ao final, uma nova campanha terá sido criada.  
O serviço também pode ser solicitado a partir da opção "Informações de Clientes". Para os diferentes tipos de clientes existentes na visão, será gerada uma campanha de marketing, sendo que os clientes repetidos não serão mostrados no *grid*.
