---
content_hash: 7275b44edcb2c9fea5d77b2e279fd9cd94873aa705295b55836bebeeb74a75ce
fetched_at: '2026-06-29T00:09:27.244603+00:00'
page_id: '423938460'
product: rm
source: tdn-rm
title: Integração de Lotes - Lote Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938460
version: 7
---

***Atenção!***

Esta funcionalidade só está disponível para as bases já migradas para o Novo Modelo do BackOffice.

O Totvs Gestão Contábil trabalha com dois tipos de lotes de lançamentos: um chamado Lote Zero e outro Lote N. O **Lote Zero** é o lote oficial da contabilidade e de onde o sistema retira todas as informações necessárias para elaboração e emissão de relatórios, controle e consulta de saldos, apuração de resultados, rotinas legais, enfim, é do lote zero onde o sistema retira todas as informações necessárias para o controle da escrituração contábil. **Lote N** são lotes de lançamentos que tem por finalidade facilitar o controle sobre lançamentos que ainda não fazem parte dos dados oficiais da contabilidade.

Se a empresa trabalhar de forma integrada com outros aplicativos, os lançamentos gerados por estes aplicativos serão trazidos para o Totvs Gestão Contábil através de lotes de lançamentos. Depois de conferidos e ajustados se preciso, eles deverão ser integrados ao lote principal da contabilidade para passarem, assim, a fazer parte dos dados oficiais da contabilidade.

Através deste processo será possível fazer a Integração dos lançamentos do lote ao lote oficial da contabilidade, Lote Zero. Para isto, selecione primeiro o(s) lote(s) desejado(s) e em seguida acione o processo Integração de Lotes. O(s) lote(s) selecionado(s) já estará relacionado no processo sendo possível neste momento adicionar novos lotes ou excluir lotes relacionados. Podem-se utilizar também Filtros a fim de selecionar apenas determinados lançamentos a serem integrados, mas atenção, o sistema não permite a integração parcial de um lançamento. Quando a opção "Filtro Genérico" for utilizada, o sistema irá aplicar as condições definidas no filtro indicado para selecionar os lançamentos a serem integrados. Se for encontrada pelo menos uma partida de um lançamento que satisfaça às condições, este lançamento com todas as partidas que o compõem será integrado, mesmo que as partidas restantes deste lançamento não satisfaçam plenamente às condições aplicadas no filtro.

**Exemplo**

Vamos supor que em um lote exista, entre outros, um lançamento com 10 partidas. Foi indicado um filtro genérico cuja condição é "Conta Crédito = 1.1.1.1.004". Uma destas 10 partidas contém a conta a crédito = 1.1.1.1.004. Na integração deste lote todas as partidas deste lançamento serão integradas, mesmo que somente uma tenha satisfeito à condição, pois como já foi dito, o sistema não integra parcialmente um lançamento.

**Observação**

**1°)** Após a integração os Lotes não são excluídos pelo sistema. Para que eles sejam excluídos automaticamente após a integração dos seus lançamentos é preciso marcar a opção "Excluir Lote(S) após o mesmo ser integrado", disponível dentro da tela do processo de integração de lotes, entretanto, os Lotes somente serão excluídos se:

* Não estiverem vinculados a nenhuma referência, parametrização ou cadastro.
* Todos os seus Lançamentos forem integrados, ou seja, não existir mais nenhum lançamento no Lote.

É importante lembrar que os Lotes que possuírem parametrização fixa em módulos externos ao da contabilidade, como no TOTVS Gestão Financeira, Gestão Patrimonial etc., em nenhuma hipótese serão excluídos pelo sistema após a sua integração.

**2°)** A execução do processo de Integração dos Lotes pode ser agendada para um determinado horário. Este recurso pode ser muito útil uma vez que com o agendamento a execução pode ser programada para um horário estratégico, onde não exista grande utilização do aplicativo, como à noite, por exemplo, otimizando desta forma a sua utilização. Para isto, o processo de integração deve ser parametrizado normalmente, mudando apenas a informação da data e hora para execução do processo conforme desejar. O agendamento, porém, só estará disponível quando o *JobServer* estiver configurado para executar em modo 3 Camadas.

**3°)** Antes da Integração de Lotes, algumas validações nos lançamentos serão realizadas a fim de manter a integridade dos dados, por exemplo:

* Se houver diferenças entre os valores de débito e crédito os lançamentos não serão integrados.
* Se o Parâmetro do Sistema 'Verifica Duplicidade de Lote na Integração' estiver marcado, antes de realizar a integração de um lote, o sistema verifica primeiro se já foi integrado anteriormente algum lote que utilizasse este mesmo código e, caso já exista alguma ocorrência de lotes com este mesmo código nos lançamentos integrados, será emitida uma mensagem advertindo-o sobre a integração anterior, permitindo que você opte por continuar ou não a integração.
* Se o parâmetro do sistema 'Aplicar regras de validação de lançamentos na Integração de Lotes' estiver marcado, o sistema fará a validação das regras de inclusão de lançamentos presentes nas Fórmulas e Amarrações de Lançamentos ativas e só fará a integração de lotes se os lançamentos estiverem satisfazendo a estas fórmulas e amarrações ativas.

**4°)** Após a execução do processo, o valor da capa do lote será recalculado. Se todos os lançamentos do lote tiverem sido integrados, o valor da capa do lote ficará zerado. Se os lançamentos tiverem sido integrados parcialmente, o valor da capa do lote será da mesma forma recalculado, sendo diminuído do valor referente aos lançamentos parcialmente integrados.

**5°)** O processo de Integração de Lotes ao lote oficial da contabilidade, Lote Zero, será necessário tanto para os lotes criados no próprio Totvs Gestão Contábil, como para lotes originados de outros aplicativos.

**6°)** Este processo é irreversível, não podendo, portanto, ser desfeita a integração dos lançamentos do(s) lote(s) recém integrado(s) ao lote oficial da contabilidade, Lote Zero.

Fluxo de Aprovação

Caso o Fluxo de aprovação de lotes/lançamentos esteja habilitado - parâmetro "**Utilizar Fluxo de Aprovação**" estiver marcado (mais detalhes em [Fluxo de aprovação de lançamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=838210925)) - a integração dos lotes originários do Contábil somente será executada para aqueles cujo Status de Aprovação esteja como "**Aprovado**".

Para a execução do processo se for selecionado algum lote com Status de aprovação diferente de "Aprovado" então será apresentada uma mensagem informando que tais lotes serão desconsiderados no processamento e apenas os demais, que atenderem esta condição, serão processados.

Ao final do processo, caso os Lançamentos sejam integrados, o status do Lote retornará para "**Em edição**" e o campo Usuário Solicitante será apagado.

Os lotes originários dos demais módulos que não sejam o Contábil não são influenciados, impactados ou restringidos pelas funcionalidades e/ou processos do Fluxo de aprovação de lançamentos.
