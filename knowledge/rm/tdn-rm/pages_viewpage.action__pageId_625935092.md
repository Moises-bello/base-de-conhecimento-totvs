---
content_hash: 58fb4454aca39e443309d31ca73e9333fd7f464910b83071a179fe73cf00c94a
fetched_at: '2026-06-29T00:11:04.269654+00:00'
page_id: '625935092'
product: rm
source: tdn-rm
title: Portal de Imóveis - Backend - Globais - Situação da Proposta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=625935092
version: 12
---

Portal de Imóveis cria um workflow de situações de propostas para gerenciar o status de cada etapa pelas quais as propostas podem ser submetidas. Este processo se inicia criando as etapas através do menu backend> Globais > Situações das propostas.

Ao abrir a situação, verá que o Portal de Imóveis já traz algumas situações padrões permitindo alteração e ou criação de novas situações.

*OBS: Sugerimos que não excluam as opções existentes, caso necessário promovam as alterações necessárias. As situações **VENDIDAS** e **PROPOSTA** **CANCELADA** não devem ser alteradas pois elas possuem ações definidas internamente no Portal de Imóveis.*

Importante!

Quando a *Situação da Proposta* no PI, for **9 - Proposta Cancelada**, o campo *Alterar a Situação da Subunidade,* no TCG, deve ser parametrizado para Disponível para Venda.

Assim, ao avançar uma proposta para esta etapa, o PI irá alterar a situação da venda no TCGI de Em Proposta, para Cancelada e a situação da subunidade desta proposta será alterada de *Em Proposta* para *Disponível para Venda* e poderá ser associada a outra proposta ou à outra venda, normalmente.

#FF9000Workflow de movimentação de proposta

Ao editar, ou incluir uma situação de proposta  encontramos os seguintes campos:

* **Titulo**: nome da situação da proposta
* **Alterar situação da unidade para**: este parâmetro mostra um combo com todas as situações de unidades cadastradas no menu SITUACAO DAS UNIDADES. Estas situações podem ter nomes diferentes das situações de unidades cadastradas no RM, mas a finalidade é termos uma ligação entre as unidades presentes no Portal de Imóveis e no RM, mas trataremos disto no menu SITUACAO DE UNIDADES. Quando selecionada que a proposta em edição deve mudar a situação da unidade ao avançar a proposta a unidade será alterada para o que for definido neste campo.

* **Cor de fundo e cor da letra**: define a cor da situação de proposta selecionada. Como no exemplo abaixo

* **Alertar movimento da situação por****e-mail**: ao cadastrar e-mails neste campo, estes receberão uma mensagem quando a proposta chegar nesta situação.

* **Permite edição**: permite editar uma proposta que estiver na situação com esta opção marcada.
* **Permite imprimir contrato**: as propostas com esta opção aparecerão no menu da proposta a opção de impressão de contrato, conforme imagem abaixo
* **Permite forçar a proposta:** Quando marcado, aparecerá no menu de propostas a opção AUTORIZAR PROPOSTAS REPROVADAS. Esta opção será eliminada em versões futuras, pois esta opção só faz sentido para a situação de propostas REPROVADAS. A opção de AUTORIZAR PROPOSTAS REPROVADAS também somente aparece quando o grupo do usuário que está acessando o Portal de Imóveis tem marcado a opção de mesmo nome conforme imagem

* **Visível na página de propostas**: as situações com esta opção vão aparecer somente no menu propostas
* **Visível na página de contratos**: as situações com esta opção vão aparecer somente no menu contratos
* **Permite editar comissão**: se marcado, aparecerá no menu da proposta a opção comissão, que abrirá a tela de cadastro e ou edição de comissão.

* **Permite altera a situação**: se marcado aparecerá no menu da proposta a opção AVANÇAR A ETAPA DA PROPOSTA. As opções possíveis para onde a proposta deverá avançar, deverão ser selecionadas na mesma tela de cadastro de situação de propostas (mapeamento de situações) conforme imagem. As opções que aparecerão no AVANÇAR ETAPA DA PROPOSTA são as opções marcadas nesta tela.
* **Permite edição da comissão somente se for o corretor da reserva ativa**: mesmo que esteja marcada a opção de editar comissão, somente será permitido se a proposta a ter sua comissão editada possua uma reserva ativa, com uma corretor associado a mesma.
* **Permite incluir excluir documentos da proposta**: aparecerá no menu da proposta a opção DOCUMENTOS DA PROPOSTA, mas é importante saber que para que esta opção apareça, também é necessário que o empreendimento possua quais documentos devem ser cadastrados por proposta. Esta parametrização está em backend> empreendimentos > documentos da proposta.

* **Verificar se a comissão foi lançada**: quando marcado, somente permitirá avançar desta situação para a próxima, quando a comissão do corretor estiver cadastrada.
* **Ignorar validação de documentos:** quando marcado irá desconsiterar qualquer validação de documentos para esta situação utilizada na proposta.
* **Validar documentos obrigatórios estão aprovados**: quando marcado, somente permitirá avançar desta situação para a próxima, se todos os documentos da proposta definidos como obrigatórios estão aprovados.
* **Considerar como proposta ativa**: determina que esta situação é uma situação de proposta ativa. Isto é importante pois o Portal de Imóveis permite somente uma proposta ATIVA por vez por unidade. Portanto se tenho uma proposta ativa, exemplo VENDIDA  o Portal de Imóveis não fará outra proposta para esta mesma unidade, mesmo que por algum erro a unidade esteja disponível. Por padrão todas as situações que não possuem movimentação devem ser consideradas INATIVAS, exemplo: PROPOSTA CANCELADA e CONTRATO ANULADO.

  

* **Derrubar filas de reservas das unidades**: o Portal de Imóveis trabalha com filas de reservas de unidades. Portanto, podemos ter vários corretores com reservas enfileiradas na mesma unidade e estas reservas ficarão ativas até a proposta ativa alcançar a situação de proposta que tem esta opção marcada. Neste momento o Portal de Imóveis irá eliminar todas as reservas que estavam em fila e não haverá mais contagem de tempo a partir deste momento. Esta opção deve ser usada em uma situação de proposta que reflita um processo de negociação em estágio avançado, cuja possibilidade de cancelamento é baixa.
* **Derrubar reserva ativa**: deve ser marcado quando se desejar derrubar somente a reserva que está ativa no momento, esta opção é utilizada na situação de PROPOSTA CANCELADA, onde devemos eliminar a reserva da proposta que está sendo cancelada e se houver fila a próxima deve assumir a reserva. Atenção: Quando este parâmetro estiver habilitado, ao alterar a situação da proposta, a reserva ativa será derrubada. No entanto, se houver fila, não ocorrerá a atualização automática e não haverá contagem de tempo, pois o sistema não consegue determinar o status atual da proposta. Para evitar esse cenário de travamento da fila, sugerimos a utilização da opção "Derrubar filas de reservas das unidades", quando este parâmetro estiver marcado para situação da proposta.
* **Horas para adicionar a reserva da proposta**: por padrão o Portal de Imóveis define valores (globais ou por empreendimento) para as etapas de RESERVA e PROPOSTA, portanto quando estamos avançando as etapas definidas pelas situações de propostas, podemos acrescentar horas para serem SOMADAS ao tempo já determinado para uma etapa. Exemplo:

  Está definido que ao fazer uma proposta esta terá duração de 6 horas. Uma das etapas seguintes a proposta é o CONTRATO EM ANALISE e nesta situação cadastramos que serão acrescentadas 4 horas ao tempo que já estava em vigor quando a proposta avançou da etapa anterior, portanto se na etapa anterior faltavam 2 horas para acabar o tempo definido, ao avançar será somado a este tempo 4 horas da situação CONTRATO EM ANÁLISE ficando agora um tempo total de análise de 6 horas.

* **Permite excluir**: permite excluir a proposta. Com o uso da nova comissão, ao realizar esta ação o sistema irá excluir tanto a proposta, quanto a venda existente no TCGI.
* **Visível no menu corretor e comissão**: demonstra esta proposta no menu corretor > comissão. Este menu é utilizado quando a empresa deseja que o corretor conheça o status das comissões lançadas para ele.
* **Exigir justificativa ao avançar**: quando marcado, somente irá avançar a etapa da proposta se uma justificativa for escrita no espaço destinado a isto
* **Excluir venda no** **BackOffice****:** permite desfazer a efetivação ou a preparação da venda que foi criada no TCGI. Ao marcar esta opção, será exibido no menu da proposta a opção "*Desfazer venda no backoffice"* e caso a venda associada a esta proposta esteja em situação "*Em preparação"* ou "*Efetivada"*, o sistema irá voltar esta venda para a situação de "*P**roposta"*.

* **Parametrização da Situação da Proposta com CRM:** Caso o parâmetro *criar interesse no instante que cria a proposta* estiver definido como SIM o Portal de Imóveis fará a criação ou a atualização o interesse. Obs.: *A parametrização apenas atualiza o interesse se e somente se o interesse for criado automaticamente quando a proposta for criada*
* **Mapeamento de situações para avançar a etapa da proposta:** Aqui você pode configurar o mapeamento de situação(ões), informando quais às outras situações podem ser mapeadas baseado nesta situação que você está cadastrando ou alterando.
* **Mapeamento de Documentos Obrigatórios:**Faça o mapeamento de quais documento(s) são necessários passarem por um procedimento de validação ao avançar situação da proposta. Para que seja feito o procedimento de validação é necessário que o parâmetro: ***Validar documentos obrigatórios estão aprovados*** esteja habilitando.**habilitado.**
