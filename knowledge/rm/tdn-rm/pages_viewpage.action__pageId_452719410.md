---
content_hash: 6e8d1345356a85ef786f83c15b5be12ea49e475696e040feec13daddc15966de
fetched_at: '2026-06-29T00:10:07.352864+00:00'
page_id: '452719410'
product: rm
source: tdn-rm
title: Gerenciamento de Benefícios no RM Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719410
version: 2
---

**Gerenciamento de Benefícios no RM Portal**

Pelo portal é possível consultar os benefícios disponíveis, automáticos, solicitados, em uso, com recusa em andamento e recusados. Aqueles benefícios que não pertencem a nenhum dos status mencionados não serão exibidos no portal.

**Disponíveis**: São aqueles benefícios que estão apenas vinculados ao beneficiário e não são automáticos.

**Automáticos**: São aqueles benefícios que estão apenas vinculados como automático direta ou indiretamente ao beneficiário

**Solicitados**: São aqueles benefícios que tem requisições de solicitação de adesão ou modificação em andamento ou aprovadas.

**Em uso**: São os benefícios que já tem requisições de solicitação ou modificação concluídas e cuja data de solicitação seja maior ou igual a data de inicio da vigência e menor ou igual a data fim da vigência.

**Recusa em andamento**: São os benefícios que tem requisições de recusa em andamento ou aprovadas.

**Recusados**: São os benefícios que já tem requisições de recusa concluídas.

**Situações em que um benefício não poderá ser solicitado:**

- O benefício não pode ser automático para o beneficiário.

- O benefício não pode estar SOLICITADO ou RECUSA EM ANDAMENTO.

- O benefício não pode estar fora da vigência.

- Caso o benefício pertença a um grupo de EXCLUSIVIDADE, a quantidade total de benefícios pertencentes ao mesmo grupo adquiridos pelo beneficiário deve ser menor que a cota do grupo. A quantidade de benefícios adquiridos é igual à quantidade de benefícios EM USO do beneficiário.

- Caso o benefício pertença a um grupo de Dependência, o benefício de referencia precisa estar em uso pelo beneficiário para que a aquisição dos benefícios vinculados ao grupo possa ser efetuada.

- O benefício deve estar vinculado diretamente ao beneficiário, salvo no caso do beneficiário ser um funcionário, situação na qual poderá estar vinculado à função, cargo ou seção de lotação (inclusive às seções hierarquicamente superiores).

- Se o benefício pertencer a mais de um grupo deverá atender às regras de validação de pelo menos um dos grupos. Ou seja, se um determinado beneficio atende a uma regra de um grupo de benefícios o mesmo não será exibido no portal, pois existe um grupo que em que a regra bloqueia a aquisição do benefício.

- Caso o sistema esteja configurado para utilizar controle de pontuação (RHU000600), o total de pontos disponíveis para o funcionário deve ser superior à soma da pontuação requerida pelo benefício para cada beneficiário.

- Deve existir um tipo de requisição vinculado ao benefício.

**Observação**

Os procedimentos de solicitação ou de recusa de benefício através do Portal somente serão realizados mediante processo de efetivação de requisição. Um benefício somente será considerado como adquirido para o beneficiário no momento em que a requisição for efetivada(concluída) no RMVitae (Gerencia de RH/ Requisições/ Efetivar Benefícios).

**Página de Visão dos benefícios:**

Esta interface é acessível a partir do portal pela  página de visualização dos dados do funcionário / Recursos Humanos / Solicitar Benefício.

Exibirá os benefícios das seguintes situações: automático, disponível, solicitado, em uso, recusa em andamento e recusado.

O status exibido na tela de visão pode diferenciar do status exibido na tela de consulta do benefício quando:

- O benefício for extensivo aos dependentes e para cada um deles o status for diferente na tela de consulta. Para isso o sistema irá considerar na tela de visão a seguinte regra de precedência para exibição do status: Em Uso

-> Recusa em Andamento ->  Solicitado -> Recusado -> Disponível Sendo o status em uso considerado o mais forte e disponível o mais fraco.

**Exemplo**

O Benefício "Plano de Saúde" está como em uso para o funcionário e para os seus 3 dependentes um está como recusado, outro disponível e outro como recusa em andamento. Nesse caso na tela de visão o benefício será exibido como em uso, pois é o status com maior precedência dentre os outros. O beneficio for solicitado pelo portal e efetivado no RMVitae pelo assistente de lançamento na tela de visão o benefício será exibido como EM USO e na tela de consulta será exibido como SOLICITADO.

**Página de Consulta do Benefício:**

Esta interface é acessível através da Página de Visão dos Benefícios quando o usuário logado clicar duas vezes em cima de um dos benefícios listados na visão. Serão exibidos os benefícios do usuário logado e seus dependentes juntamente com seus respectivos status individuais.

**Página de Solicitação:**

Esta interface é acessível através da Página de Consulta do Benefício quando o usuário logado selecionar o beneficiário e clicar no botão "solicitar adesão/modificação". Neste momento é possível informar dados nos campos complementares e também imprimir os relatórios gerenciais vinculados a requisição de solicitação. Basta clicar no link "imprimir" disponível ao lado de cada beneficiário. Este relatório precisa estar previamente configurado (com passagem de parâmetros de coligada, chapa do funcionário e código do dependente).

**Página de Recusa:**

Esta interface é acessível através da Página de Consulta do Benefício quando o usuário logado clicar no botão "recusar adesão".

Neste momento é possível informar dados nos campos complementares e também imprimir os relatórios gerenciais vinculados a requisição de recusa. Basta clicar no link "imprimir" disponível ao lado de cada beneficiário. Este relatório precisa estar previamente configurado (com passagem de parâmetros de coligada, chapa do funcionário e código do dependente).
