---
content_hash: 23cb1710b7dc17ab676064fc8acbbe6dc1b6d8e88a1df3d121c5d16f3adf7f7b
fetched_at: '2026-06-29T00:09:27.996018+00:00'
page_id: '423938607'
product: rm
source: tdn-rm
title: Preferências dos Usuários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938607
version: 3
---

As *Preferências* são definições ou parametrizações específicas e exclusivas configuradas para cada usuário, definindo um modo particular de utilização do sistema. Para esta configuração especial o usuário deverá logar no sistema e configurar suas preferências para digitação de lançamentos e orçamentos em série conforme opções disponíveis.

Marque os campos que você deseja fixar na inclusão de lançamentos em série. Os campos que estiverem marcados terão seus dados mantidos a cada inclusão de novo lançamento/partida. Marque todos os campos que você deseja manter preenchidos com os dados da partida anterior para as novas partidas incluídas no lançamento.

Alguns campos dependerão de outros para ficarem habilitados. Os campos "Rateio a Débito" e/ou "Rateio a Crédito" só ficarão disponíveis quando o campo "Valor" estiver marcado, assim como os campos "Conta a Débito" e/ou "Conta a Crédito".

As *Preferências* também podem ser configuradas da mesma forma para a inclusão de novos orçamentos. Se na inclusão de um novo registro você não desejar alterar o conteúdo de nenhum dos campos aqui marcados, mantendo os mesmos dados do registro anterior, marque também a opção **Não posicionar nos campos fixados durante a digitação**. Desta forma a inclusão ficará mais ágil, pois ao pressionar a tecla Tab ou Enter para passar para o próximo campo, o cursor irá se posicionando nos demais campos, saltando estes marcados. O conteúdo destes campos que foram marcados e copiados do registro anterior fica, porém, liberado para digitação ou alteração, basta posicionar nos respectivos campos e alterá-los.

Além da fixação de campos que serão utilizados na inclusão de registros em série, você poderá definir também:

* **Sugerir automaticamente o código reduzido da conta quando utilizar dígito verificador**

Marque esta opção para permitir a sugestão automática do código reduzido e o respectivo dígito verificador das contas contábeis e gerenciais.

Exemplo: Com esta preferência marcada e os parâmetros do sistema "Usa código reduzido" e "Usa dígito verificador" também marcados, na inclusão de uma partida, informando-se, por exemplo, o n.º 5 e acionando a tela TAB no campo da conta contábil  o sistema trará automaticamente a primeira conta encontrada com código reduzido iniciado com 5. Com esta preferência desativada, não trará nada e o usuário deverá informar o código desejado e o seu respectivo dígito verificador.

* **Exibir Campos Complementares na visão de partidas do lançamento**

Com esta opção marcada, os campos complementares de lançamentos ativos, existentes na base de dados, ficarão visíveis na visão de lançamentos.

* **Exibir a tela de manutenção de partidas ao abrir a tela de lançamentos a partir da visão**

Com esta opção Desmarcada, na visão de Lançamentos, ao editar uma partida o sistema abrirá o 'Lançamento' com todas as partidas que o compõe. Com esta opção Marcada, ao editar uma partida o sistema abrirá a própria tela da 'Partida' para edição.

* **Ao salvar a Partida salvar automaticamente o Lançamento Contábil**

Com esta preferência marcada, ao acionar o botão Salvar da tela da Partida, a partida e seu respectivo lançamento serão salvos imediatamente no banco de dados. Com esta preferência desmarcada, somente ao acionar o botão Salvar da tela de visão do Lançamento Contábil é que as informações serão salvas no banco de dados.
