---
content_hash: e8ada5c531277104e24a3b9c5c3abae2d424fa13cfe92346d233c9aba445f9c3
fetched_at: '2026-06-29T00:10:52.293751+00:00'
page_id: '571782427'
product: rm
source: tdn-rm
title: Movimentações do BackOffice e Apropriações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=571782427
version: 8
---

Nesta consulta é possível verificar todas as movimentações de Pagamento, Entrega, Apropriação e Devolução, retornadas pelo processo de importar apropriações.

Sendo possível a execução do processo de importação a partir desta mesma visão. Para mais detalhes sobre a utilização deste processo disponíveis em: [Apropriações e Movimentações do Backoffice no TCOP - Totvs Construção Obras e Projetos](https://tdn.totvs.com/pages/viewpage.action?pageId=518472242)

Durante a execução do processo, vão ser validados os valores se houver alguma transferência de apropriação, caso exista Transferência e o saldo do movimento no BackOffice seja insuficiente, ao final do processo será exibido o Log semelhante a imagem abaixo com todas as transferências inconsistentes (para saber sobre o processo de "Transferência de Apropriações" clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=697260353)).

No Log esta descrito:

**Tarefa:** descrição e código da tarefa apropriada.

**Data Apropriação:** data em que foi feita a apropriação

**Quantidade:** quantidade que existia antes da execução do processo.

**Quantidade Atual:** nova quantidade que foi alterada no BackOffice e importada para o projeto.

Importante ressaltar que para visualização das apropriações e movimentações é necessário a liberação de permissão no sistema.

Acessando o perfil de usuário .

Importante!

Caso a importação de movimento traga lançamentos com valores zerados, será necessário revisar a configuração do tipo de movimento, pois deverão estar com o mesmo tipo de rateio de centro de custo informado, tanto no movimento de origem quanto no final.

Saiba como parametrizar os tipos de movimento de entrega e devolução nos parâmetros do projeto, .
