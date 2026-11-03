---
content_hash: db4ecf162051b635ab6d90d6b4341675dd32a3fc435122607e8e5df8b653ae86
fetched_at: '2026-06-29T00:10:08.795681+00:00'
page_id: '452719581'
product: rm
source: tdn-rm
title: Requisições
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719581
version: 3
---

**Requisições**   
   
Controle de Processos Requisição obrigatória para admissão

Marcando este parâmetro, torna-se obrigatório especificar a requisição de aumento de quadro ou de substituição que será vinculada a processos como: seleção, inclusão de candidato em processo de admissão e admissão.

Caso este campo não seja definido como obrigatório, estes procedimentos poderão ser realizados sem a necessidade de atender a uma requisição.

Requisição obrigatória para alterar cargo e/ou salário

Marcando este parâmetro, torna-se obrigatório a existência de uma requisição aprovada de Alteração de Dados Funcionais para alterações de dados como função e salário no cadastro do funcionário. Os campos "Função", "Faixa/ Nível salarial" e "Salário" ficam travados para edição.

Requisição obrigatória para transferir funcionário

Marcando este parâmetro, torna-se obrigatório a existência de uma requisição aprovada de Transferência para alteração da seção no cadastro do funcionário. Os campos "Filial" e "Seção" ficam travados para edição.

Requisição obrigatória para transferir e alterar dados funcionais

Marcando este parâmetro, torna-se obrigatório a existência de uma requisição aprovada de Transferência com Alteração de Dados Funcionais para alteração dos dados referentes à seção, função, faixa/ nível salarial e salário no cadastro do funcionário. Os campos "Filial", "Seção" "Função", "Faixa/ Nível salarial" e "Salário" ficam travados para edição.

Requisição obrigatória para desligamento

Marcando este parâmetro, torna-se obrigatório a existência de uma requisição aprovada de desligamento para demitir um funcionário.

Permitir alterar dados da requisição vinculada

Marcando este parâmetro, torna-se possível alterar os dados de uma requisição nos processos:

* Vincular candidatos/funcionários à requisição de aumento de quadro ou substituição,
* Efetivar Alteração de Dados Funcionais,
* Efetivar Transferência,
* Efetivar Transferência com Alteração de Dados Funcionais
* Demissão.

Envio automático de e-mail. 

Marcando este parâmetro, será enviado e-mails contendo mensagens padronizadas que informarão os participantes do fluxo e gestores sobre o andamento das requisições.  
   
Bloquear modificações de campos complementares após o primeiro aprovador

Marcando este parâmetro, o segundo e os demais aprovadores das requisições não terão permissão para alterar os campos complementares da requisição. Caso contrário, os campos complementares poderão ser alterados.

Configuração de E-mails E-mail do Gestor de Requisições de Recursos Humanos

Campo para definição do e-mail do Gestor de RH que receberá as notificações sobre o andamento dos processos relativos às requisições.

E-mail do Gestor de Requisições do Departamento Pessoal

Campo para definição do e-mail do Gestor do DP que receberá as notificações sobre o andamento dos processos relativos às requisições.

**Observação:** Somente serão enviadas as mensagens da requisição para os endereços eletrônicos desejados, caso os campos relacionados à configuração de envio de e-mails tenham sido preenchidos nos parâmetros globais.

Motivo de mudança de função para efetivar requisições que tenham alteração de dados funcionais

Este parâmetro deve ser informado para ser utilizado somente na efetivação das requisições de "Alteração de Dados Funcionais" e "Transferência com Alteração de Dados Funcionais" quando não houver alteração de função, o motivo de alteração de função não estiver preenchido e houver alteração de níivel e/ou faixa salarial.

**Observação:** Nas requisições de "Alteração de Dados Funcionais" e "Transferência com Alteração de Dados Funcionais" o usuário pode modificar somente os dados salariais, mantendo a função inalterada. Para o RM Labore a alteração de Nível e/ou Faixa salarial configura-se uma alteração de Função. Se o sistema faz uso de tabelas salariais e o Gestor criar uma requisição alterando o Nível e/ou Faixa Salarial será solicitado somente o motivo de alteração de salário. Porém, no momento da efetivação destas requisições o usuário poderá informar um motivo para alteração de função ou preencher o campo "Motivo de Alteração de Função para requisições com alteração de dados funcionais" para que este motivo seja preenchido automaticamente na efetivação da requisição.

Permitir incluir funcionários de outras coligadas em movimentação de pessoal

Marcando este parâmetro, é possível incluir funcionários de outras coligadas em movimentação de pessoal pelo processo de Captação (novo processo de seleção).

Permitir excluir funcionários vinculados à requisição de aumento de quadro ou substituição

Marcando este parâmetro, é possível excluir funcionários que foram admitidos através de uma requisição de aumento de quadro ou substituição.

Habilitar o rateio de centros de custos em requisições

Marcando este parâmetro nas requisições de aumento de quadro, substituição, alteração de dados funcionais, transferência, transferência com alteração de dados funcionais e transferência em lote, o sistema possibilitará ao solicitante/aprovador propor rateio de centro de custos para o funcionário ou vaga relacionado à requisição. Esta funcionalidade também se aplica ao RM Portal.

Cód. Tipo Requisição para candidaturas de vagas internas

Informando um tipo de Requisição Geral neste campo, quando um funcionário tentar se candidatar a uma vaga no Banco de Talentos será criada uma Requisição Geral a ser aprovada pelo seu líder.

Se a requisição for aprovada, no Banco de Talentos vai habilitar para o funcionário o botão "Candidatar" para que o funcionário realmente se candidate à vaga, após aprovação do seu líder.

Se a requisição for reprovada, no Banco de Talentos não vai habilitar para o funcionário o botão "Candidatar".

**Observação**: Quando este parâmetro é utilizado o candidato consegue acompanhar, pelo detalhamento da vaga no Banco de Talentos, o andamento dessa solicitação de candidatura.
