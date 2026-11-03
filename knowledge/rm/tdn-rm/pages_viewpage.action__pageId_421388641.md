---
content_hash: 3cf8f7c753a1d50b37838816a5d4a9ce842d911203e2e767c67e0da49fe7cd02
fetched_at: '2026-06-29T00:09:17.764872+00:00'
page_id: '421388641'
product: rm
source: tdn-rm
title: Boletim Técnico - Controle de Alçada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388641
version: 5
---

Os passos a seguir servirão de guia para a utilização do Controle de Alçada, cujo objetivo é o controle de permissão concedida a um grupo de usuários para acessar/executar um cadastro ou processo. Para esse requisito o controle é sobre o cadastro de Template de acordo e dos processos sobre o acordo. O Template disponível para realizar o Acordo dependerá do valor líquido dos lançamentos de origem sendo compreendido no Valor da Faixa do Template.

No caso de integração com o Totvs Educacional, as regras de negócio do mesmo é que irá definir quais lançamentos podem sofrer o Acordo utilizando o Template adequado.

**Controle de alçada e seleção de Template**

O controle será realizado através do Perfil de Usuário que o mesmo possui as permissões, os Templates devem ser vinculados a este. Para iniciar a utilização certifique-se que o perfil associado ao usuário possui permissão para (Incluir|Editar|Aprovar e Excluir). Para alterar as permissões do usuário acesse o cadastro de [perfis](http://tdn.totvs.com/x/bbAQG)nos serviços globais.  
No Totvs Gestão Financeira ao solicitar a geração do Acordo , serão exibidos os Templates permitidos ao usuário para selecionar o desejado. Caso exista somente um único Template que atenda as regras do mesmo será automaticamente selecionado.

**Aceite na Geração do Acordo**

Ao executar o processo de geração da rotina a negociação poderá ser impressa através do botão de "Imprimir Negociação" na etapa onde são visualizadas as parcelas. Caso no Template de Acordo a opção "Gerar aceite do documento de acordo" esteja marcada, será apresentado relatório com informações do Serviço Financeiro que está sendo contratado para que o mesmo possa realizar o "aceite" ou não da transação. Somente com o aceite das condições apresentadas será possível concluir o processo de geração do Acordo.

**Aprovação do Acordo**

Existem duas formas de aprovação do Acordo que são parametrizadas no Template: a "Simples", executava via processo na visão de Acordos pelo usuário que tenha permissões no menu, e a aprovação via Work Flow que gera, de acordo com os parâmetros definidos no Template, um atendimento para o Módulo CRM. O processo será controlado por um campo de Status, e também serão armazenados o usuário e data da aprovação.

**Efetivação do Acordo**

A efetivação do acordo será realizada conforme parametrização da opção "Efetivação do Acordo" no Template com as opções : Ao Criar | Ao Aprovar | Ao pagar primeira. O status estará conforme cada operação.

Em aberto

Acordo criado, mas ainda não passou pelo processo de aprovação/efetivação.

Reprovado

Se Template faz controle de aprovação indica que o acordo não foi aprovado.

Não Efetivado

Indica que o acordo foi não está efetivado, ocorre após o mesmo ser cancelado.

Efetivado

Indica que o acordo foi efetivado.

Ao efetivar um Acordo a cobrança será realizada nas parcelas geradas do mesmo. Alterações no lançamento de origem do Acordo somente poderão ocorrer caso o mesmo esteja com status de efetivado ou cancelado. No caso de Acordo reprovado os lançamentos não serão gerados ficando apenas como consulta na guia de lançamentos não efetivados.

**Geração dos Lançamentos Financeiros do Acordo**

Os Lançamentos Financeiros do Acordo serão gerados conforme a opção de Efetivação parametrizada no Template.

Até que a efetivação ocorra existem somente registros de lançamentos não efetivados que poderão ser visualizados no anexo "Lançamentos não efetivados" do cadastro.

* Se habilitada a opção Efetivação do acordo do Template como "Ao Criar" os lançamentos serão gerados automaticamente na criação do acordo.
* Se "Ao aprovar", ocorrerá após a execução do processo de aprovação, que pode ser Simples ou Via Work Flow.
* Com a opção de "Após pagamento 1ª parcela" somente o lançamento da primeira parcela é criado junto com o Acordo, para as demais parcelas, ocorre na baixa ou emissão de cheque desse lançamento.

Os valores defaults para os campos Filial, Centro de Custo, Departamento, Tipo de documento, Conta Caixa e Tabelas Opcionais (1 a 5) nos lançamentos criados pelo Acordo serão carregados dos Lançamentos de origem caso tenham o mesmo valor em todos. Se não carregados, virão dos defaults do template.

**Integração com o Totvs Educacional**

Na integração do Educacional somente será permitido a criação de novos Acordos para o mesmo Cliente/Fornecedor (Responsável Financeiro) caso não existam Acordos ainda não efetivados.

Será possível realizar Negociação Online de lançamentos deste produto, através de parametrização no template de Acordo com a opção *"Disponível Web"*

**Cancelamento do Acordo**

O processo de cancelamento do Acordo poderá ser realizado de duas formas: "Varredura de lançamentos" e "Cancelamento visão do Acordo".

* Varredura de lançamentos será utilizada quando a primeira parcela do Acordo já estiver vencida em um número de dias maior que o prazo que será definido na execução, sendo assim o sistema varrerá os Lançamentos Financeiros identificando o Acordo e cancelando o mesmo.
* Cancelamento pela visão de Acordo no menu Processos.

Em ambos os casos a regra para cancelamento será a mesma: lançamentos gerados pelo acordo não podem estar baixados nem cancelados. O cancelamento do acordo irá disparar um processo para que o módulo que fez o acordo faça suas validações e também execute as regras de cancelamento em suas entidades (caso exista alguma)

**Adicionais**

O sistema irá respeitar as informações do perfil , após realizar  Logout – Login da aplicação. As alterações passarão a valer ao iniciar o sistema.
