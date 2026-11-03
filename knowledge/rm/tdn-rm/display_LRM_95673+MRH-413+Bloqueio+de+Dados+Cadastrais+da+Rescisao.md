---
content_hash: e28c0c1b0c0aa5a3ba6d98a0826a27981eb9e67588e00637de9befa9fc15687b
fetched_at: '2026-06-29T00:08:30.363898+00:00'
page_id: '272426614'
product: rm
source: tdn-rm
title: 95673 MRH-413 Bloqueio de Dados Cadastrais da Rescisao
type: documentation
url: https://tdn.totvs.com/display/LRM/95673+MRH-413+Bloqueio+de+Dados+Cadastrais+da+Rescisao
version: 110
---

# Rescisão

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Folha de Pagamento. |
| **Função:** | Edição de Dados Cadastrais da Rescisão. |
| **Situação/Requisito:** | Controle para gerenciar o bloqueio de dados cadastrais da rescisão a fim de impedir alteração nos dados da rescisão não autorizadas. |
| **Solução/Implementação:** | Foi criado um controle para gerenciar o bloqueio de dados cadastrais da rescisão. Sendo acionado em Folha de pagamento / Rescisão / Restrições Cadastrais.        Foi criado uma tabela que irá controlar o bloqueio e desbloqueio para cada funcionário demitido. Denominada PFRESCDESBLOQUEADA.     A tabela terá os campos CODCOLIGADA e CHAPA.     Os funcionários que estiverem cadastrados na tabela PFRESCDESBLOQUEADA estarão com o cadastro de rescisão desbloqueado, permitindo assim edição nos dados cadastrais da rescisão.        O Gerenciamento é ativado quando marcar o parâmetro "Ativar controle de bloqueio de dados cadastrais da rescisão" em Parametrizador / Folha de Pagamento / Rescisão / Restrições Cadastrais.        Quando o parâmetro é marcado as rescisões nas competências anteriores serão bloqueadas para edição automaticamente. As rescisões na competência atual e futura permanecerão liberadas.     Quando o parâmetro é Desmarcado o sistema libera para edição todos os dados cadastrais da rescisão para todos os funcionários.     O Marcar e desmarcar parâmetro não irá alterar os dados registrados na tabela PFRESCDESBLOQUEADA.        O sistema dispõe dos seguintes módulos para gerenciar o controle de bloqueio para os dados cadastrais da rescisão, a saber:      * Visão de todos os      funcionários demitidos desbloqueados para edição dos dados cadastrais da      rescisão; * Processo auxiliado por      assistente para desbloquear “N” funcionários; * Processo para bloquear      os funcionários selecionados na visão; ( Exclusão ) * Bloqueio automático na      liberação de competência; * Todos os módulos acima serão ativados ou os seus comportamentos alterados somente se o parâmetro "Ativar controle de bloqueio de dados cadastrais da rescisão" estiver marcado.         O Gerenciamento para bloqueio dos dados cadastrais da rescisão será independente do controle de bloqueio de período.     Os dados cadastrais da rescisão só estarão liberados para alteração se:     1) O controle de bloqueio dos dados cadastrais da rescisão estiver desbloqueado; E     2) O controle de bloqueio do período estiver desbloqueado.     Sendo assim basta um deste controles estar bloqueado que os dados cadastrais da rescisão não poderão ser alterados.        Ao preencher uma rescisão na competência atual ou futura estará automaticamente desbloqueada. O sistema irá incluir o funcionário automaticamente na tabela PFRESCDESBLOQUEADA.        Ao liberar competência todos os Demitidos na competência atual terão os dados cadastrais da rescisão bloqueados para edição, além dos Demitidos em competências anteriores que tenham sido desbloqueados.        No cadastro da rescisão ao tentar alterar qualquer dado de uma rescisão que esteja com seu cadastro bloqueado o sistema irá emitir a mensagem: "Os dados cadastrais para esta rescisão estão bloqueados."        No Cancelamento da Rescisão será apresentado o aviso: " Funcionário {0} está com os dados cadastrais da rescisão bloqueado. Seus Dados não foram Alterados." para cada funcionário que tenha sido bloqueado os dados cadastrais da rescisão.        Na Rescisão Coletiva será apresentado o aviso: " Funcionário {0} está com os dados cadastrais da rescisão bloqueado. Seus Dados não foram Alterados." para cada funcionário que tenha sido bloqueado os dados cadastrais da rescisão.        No cadastro de funcionário mudando da situação "D" para "A" o sistema zera automaticamente os dados da rescisão não observando o controle de bloqueio de dados cadastrais da rescisão.        Rescisão complementar continua com o mesmo comportamento alterando a data do último movimento. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | 95673 |
| **Requisito:** |  |

divs
