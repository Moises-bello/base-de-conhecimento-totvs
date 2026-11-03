---
content_hash: 961604fa6b4bd93ef89c22101f4d7fa81754591fc1aa20012af9897f363f3f7e
fetched_at: '2026-06-29T00:09:24.821581+00:00'
page_id: '423938031'
product: rm
source: tdn-rm
title: Transferência de Controle 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938031
version: 4
---

Novidade: Foi implementado para a versão 12.1.12 e as subsequentes o parâmetro "Permitir a transferência de controle posterior ao período de cálculo atual". Tal parâmetro passa a permitir transferência de controle fora do período de cálculo atual, desde que seja em uma data superior ao período de cálculo atual.

**Observação:** Em nenhuma hipótese será permitido realizar a contabilização para o tipo de transferência citado acima e há também a impossibilidade de realizar a transferência para **FILIAL** fora do período de cálculo atual.

Este processo é responsável por transferir o(s) patrimônio(s) entre , , centros de custo, localizações e responsáveis. A transferência poderá ser realizada utilizando um ou mais patrimônios, sendo que para a segunda opção deve-se atentar a questões como a data de aquisição e se estão todos ativos.

**A transferência de controle não será realizada nas seguintes situações:**

* Em patrimônio(s) considerado(s) Título(s);
* Em patrimônio(s) inativo(s) e baixado(s) totalmente. Para isto a baixa total deverá ser realizada com o parâmetro "Desativar Patrimônio após sofrer baixa total" marcado;
* Em patrimônio(s) inativo(s);
* Em data anterior a da última transferência realizada para o(s) mesmo(s) patrimônio(s), ou seja, deve-se conferir se o patrimônio já possui uma transferência e se a data é posterior a informada no processo a ser realizado;
* Os dados de destino (filial, departamento, centro de custo, localização e responsável) devem estar ativos.

Outra situação a ser considerada durante o processo de transferência é em relação aos dados de origem e destino. Os dados de destino devem ser diferentes dos dados de origem, ou seja, os dados (filial, departamento, centro de custo, localização e responsável) atuais do patrimônio devem ser diferentes dos informados durante a transferência de controle.

**Parametrização**

O responsável a ser utilizado no processo de transferência de controle está diretamente relacionado com o parâmetro "Usar funcionários do RM Labore como responsáveis", ou seja, caso este parâmetro esteja marcado o sistema irá considerar os funcionários do TOTVS Folha de Pagamento (RM Labore). Se o parâmetro citado anteriormente não estiver marcado será considerado os responsáveis cadastrados no próprio sistema patrimonial.

Como o Totvs Gestão Patrimonial permite vincular uma localização a um responsável, caso o parâmetro "Vincular Localização com Responsável" esteja marcado o processo de transferência de controle verificará se existe alguma localização vinculada a um responsável. Se existir este vinculo o sistema associará responsável da localização à mesma de forma a não prejudicar a vinculação definida pelo usuário.

**Procedimentos para realizar a transferência de controle**

Existem duas maneiras de executar o processo de transferência de controle, a partir do menu Operações Patrimoniais/Transferência de controle e pela tela de visão de patrimônios cadastrados na opção processos. Ao utilizar a transferência a partir do menu Operações Patrimoniais deve-se informar o patrimônio a ser transferido. Lembre-se que na opção acima podem der informados mais de um patrimônio.

Após selecionar o(s) patrimônio(s) deve-se informar os dados de destino que são Filial, Departamento, Centro de Custo, Local e Responsável ou Funcionário (dependendo da parametrização). Neste momento deve-se ter atenção para as regras de exceções impostas pelo sistema como não utilizar títulos ou patrimônios inativos.

O próximo passo é informar a data da transferência (obrigatório), o número do documento e um texto de observação. A data da transferência deverá estar de acordo com regra definida pelo sistema citada no item "A transferência de controle não será realizada nas seguintes situações" deste help.

Transferir patrimônios agregados: Ao marcar esta opção todos os patrimônios que possuem outros patrimônios agregados a eles serão transferidos. Nesta situação, para o(s) patrimônio(s) agregado(s) serão aplicadas as mesmas regras de exceção como patrimônio inativo ou totalmente baixado.

**Observação**

Para utilizar o processo de transferência a partir da visão de patrimônios cadastrados deve selecionar o(s) patrimônio(s) desejado(s) e escolher a opção "Transferência de Controle" em "Processos". A diferença entre esta forma de chamar o processo com a que acessa o menu Operações Patrimoniais é que nesta opção não aparecerá a tela onde se pode informar o(s) patrimônio(s), visto que os mesmos já foram selecionados na visão de patrimônios cadastrados.

**Transferências de controle realizadas**

Após realizar a transferência de controle com sucesso pode-se conferir seu resultado por destino a partir da tela de cadastro de patrimônio. Para isto é necessário editar o patrimônio transferido e acessar a aba de históricos de controle. Esta aba apresentará o histórico por Filial, Centro de custo, Departamento, Responsável e Localização. Entre as informações que serão exibidas neste tela pode-se citar os usuários de criação e alteração, as datas de criação e alteração, a data de entrega do patrimônio naquela opção (exemplo: entrada na filial) e a data de saída do patrimônio naquela opção (exemplo: saída da filial). Outro caminho existente na visão de cadastro de patrimônios para acessar as informações das transferências realizadas é em Anexos, históricos de Filial, Centro de custo, Departamento, Responsável ou Localização.

**Serviço referente ao envio de e-mail**

A cada transferência de controle realizada pode-se enviar um e-mail para o responsável atual e o novo responsável do patrimônio. Caso queira utilizar esta funcionalidade deve-se marcar a opção "Enviar e-mail de patrimônios sob responsabilidade" nos parâmetros do sistema. Observação: Este recurso é válido somente quando o responsável está definido como um funcionário do RM Labore. Para isto o parâmetro "Usar funcionários do RM Labore como responsáveis" deve estar marcado e o campo que armazena o e-mail do funcionário devidamente preenchido.

Veja também

* Consulta de Transferências de Controle
* Contabilização da Transferência de Controle
