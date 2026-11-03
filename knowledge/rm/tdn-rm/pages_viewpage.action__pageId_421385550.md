---
content_hash: 39c9eeb19923af69a1c105bff3792897d16c3cd772bfc049256e799ce5733cda
fetched_at: '2026-06-29T00:09:16.766206+00:00'
page_id: '421385550'
product: rm
source: tdn-rm
title: Recursos da Composição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385550
version: 3
---

A tela de recursos da composição nos permite visualizar os insumos ou composições auxiliares associados. Para executar este processo utilizamos o grid 'Recursos da composição', na visão de Composições, acionada pela opção Anexos -> Recursos da Composição, ou na edição da Composição, aba Identificação, em ambos o processo para associação é o mesmo.

No grid de recursos da composição é possível alterar a quantidade e o preço unitário do insumo, se o valor for diferente do atual, um novo preço é cadastrado para o recurso (insumo) e caso o preço, com a descrição "Preço em (Data atual)", já exista cadastrado, o valor será alterado. Se o valor do preço for alterado, uma mensagem será apresentada, informando que um novo preço será inserido, e essa mensagem pode ser desabilitada na própria caixa da mensagem. Para criar um novo preço a partir desse recurso, é necessário que a edição do insumo esteja habilitada para o usuário corrente.

Ao clicar no lookup de insumo serão listados todos os insumos cadastrados no Projeto e que contenham grupo DNIT definido. Também serão listados os insumos cadastrados no projeto Global.  Ao informar o insumo ficará habilitado o check "Recurso Ativo", que por default aparece habilitado, porém este pode ser desabilitado, sendo a apresentação deste recurso diferente dos recursos ativos, ficando na cor cinza. A frente do lookup existe uma opção que possibilita o cadastro de um novo insumo.  
Ao clicar no lookup de composição auxiliar serão listadas todas as composições cadastradas no projeto e que possam ser composição auxiliar. Também serão listadas todas as composições auxiliares do projeto global.  Ao informar a composição auxiliar ficará habilitado o check "Recurso Ativo", que por default aparece habilitado, porém este pode ser desabilitada, sendo a apresentação deste recurso diferente dos recursos ativos, ficando na cor cinza. A frente do lookup existe uma opção que possibilita o cadastro de uma nova composição.

Os campos Quantidade, Equipe e Fórmula são campos que podem ser definidos pelo usuário, onde a quantidade e a equipe são apresentados com valor default 1 e o campo fórmula se refere à fórmula para cálculo da quantidade de  recursos da composição, quando deseja-se definir a quantidade através de fórmulas.  
Na inclusão de recursos da composição existe uma aba referente a fórmulas do recurso, onde é possível construir fórmulas para realizar cálculos com base no recurso associado, saiba mais em  .   
Os campos Unidade: Fator K, Unidade: Produção por Hora, Grupo DNIT, Transporte, Equipamento, Preço Unitário, Preço Parcial, são definidos após salvar o recurso associado, eles são preenchidos com as informações que já constam no recurso.  
Em Transporte, é exibido informações da Distância Média de Transporte (DMT), onde os campos **DMT(Terra - LN)** = Leito Natural, **DMT(Revestido - RP)** = Revestimento Primário e **DMT(Pav - P)** = Rodovia Pavimentada.

**Observação:**  
Não é possível uma composição de tipo equipamento, ter como recurso uma composição que também seja do tipo equipamento.
