---
content_hash: a4a680d4d64a47ed300accf25299df444cc51725b2f1983992556f41025bcdd9
fetched_at: '2026-06-29T00:11:18.104531+00:00'
page_id: '683206078'
product: rm
source: tdn-rm
title: Integração Lote Contábil Multicoligada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=683206078
version: 2
---

Através deste processo será possível fazer a Integração dos lançamentos do lote ao lote oficial da contabilidade de todas coligadas acessadas pelo usuário, Lote Zero. Para isto, selecione primeiro o(s) lote(s) desejado(s) e em seguida acione o processo Integração de Lotes Multicoligada.

Neste novo processo, não e utilizados filtros, fica restrito apenas o período de lançamentos dos lotes selecionados que é definido durante o processo.

**Observação**

**1°)** Após a integração os Lotes não são excluídos pelo sistema. Para que eles sejam excluídos automaticamente após a integração dos seus lançamentos é preciso marcar a opção "Excluir Lote(S) após o mesmo ser integrado", disponível dentro da tela do processo de integração de lotes, entretanto, os Lotes somente serão excluídos se:

* Não estiverem vinculados a nenhuma referência, parametrização ou cadastro.
* Todos os seus Lançamentos forem integrados, ou seja, não existir mais nenhum lançamento no Lote.

É importante lembrar que os Lotes que possuírem parametrização fixa em módulos externos ao da contabilidade, como no TOTVS Gestão Financeira, Gestão Patrimonial etc., em nenhuma hipótese serão excluídos pelo sistema após a sua integração.

**2°)** A execução do processo de Integração dos Lotes pode ser agendada para um determinado horário. Este recurso pode ser muito útil uma vez que com o agendamento a execução pode ser programada para um horário estratégico, onde não exista grande utilização do aplicativo, como à noite, por exemplo, otimizando desta forma a sua utilização. Para isto, o processo de integração deve ser parametrizado normalmente, mudando apenas a informação da data e hora para execução do processo conforme desejar. O agendamento, porém, só estará disponível quando o *JobServer* estiver configurado para executar em modo 3 Camadas.

**3°)** Antes da Integração de Lotes, algumas validações nos lançamentos serão realizadas a fim de manter a integridade dos dados, por exemplo:

* Se houver diferenças entre os valores de débito e crédito os lançamentos não serão integrados.
* Se o Parâmetro do Sistema 'Verifica Duplicidade de Lote na Integração' estiver marcado, antes de realizar a integração de um lote, o sistema verifica primeiro se já foi integrado anteriormente algum lote que utilizasse este mesmo código e, caso já exista alguma ocorrência de lotes com este mesmo código nos lançamentos integrados, será emitida uma mensagem advertindo-o sobre a integração anterior, permitindo que você opte por continuar ou não a integração.
* Se o parâmetro do sistema 'Aplicar regras de validação de lançamentos na Integração de Lotes' estiver marcado, o sistema fará a validação das regras de inclusão de lançamentos presentes nas Fórmulas e Amarrações de Lançamentos ativas e só fará a integração de lotes se os lançamentos estiverem satisfazendo a estas fórmulas e amarrações ativas.

**4°)** Após a execução do processo, o valor da capa do lote será recalculado. Se todos os lançamentos do lote tiverem sido integrados, o valor da capa do lote ficará zerado. Se os lançamentos tiverem sido integrados parcialmente, o valor da capa do lote será da mesma forma recalculado, sendo diminuído do valor referente aos lançamentos parcialmente integrados.

**5°)** O processo de Integração de Lotes ao lote oficial da contabilidade, Lote Zero, será necessário tanto para os lotes criados no próprio Totvs Gestão Contábil, como para lotes originados de outros aplicativos.

**6°)** Este processo é irreversível, não podendo, portanto, ser desfeita a integração dos lançamentos do(s) lote(s) recém integrado(s) ao lote oficial da contabilidade, Lote Zero.
