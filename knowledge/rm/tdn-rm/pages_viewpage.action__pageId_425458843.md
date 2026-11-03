---
content_hash: 430d9bd4da9606c8cc150dec4f0ce05b78a057997c3ee28cda47c97820977d2d
fetched_at: '2026-06-29T00:09:32.412979+00:00'
page_id: '425458843'
product: rm
source: tdn-rm
title: Módulo Cliente Online (Web)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458843
version: 2
---

**Módulo Cliente On Line (Web)**    
O Módulo de Cliente On Line é um recurso que permite o acompanhamento e o gerenciamento das requisições. Através dele, o controle das informações é ampliado e facilitado. É possível  abrir novas solicitações, acrescentar textos na discussão, anexar arquivos, aprovar e/ou desaprovar entendimentos, verificar o histórico de etapas além de consultar solicitações ( pendentes, andamento, concluída, cancelada).  
Todos os tipos de clientes: Cliente, Pessoa, Aluno, Professor e Prospect  ( referente as respectivas tabelas FCFO, PPESSOA, SALUNO, SPROFESSOR, HPROSPECT) podem acessar o módulo de cliente on line desde que possuam um usuário pré-cadastrado e a permissão liberada no perfil.  
Para acessar, utilize o portal informando o usuário e a senha. Vale ressaltar que os clientes do tipo pessoa, aluno e professor já possuíam um usuário associado da tabela GUSUARIO, os tipos Prospect e Cliente (FCFO) foram associados a um usuário (foi disponibilizado o campo para interligar). Essa associação foi feita também para os contatos do Prospect e para os Clientes (FCFO).  
E será realizado uma busca em todas as tabelas envolvidas, tendo como parâmetro o código do usuário logado. No caso do Prospect e o Cliente\*, primeiramente é verificado se existe um contato associado, em caso negativo o sistema busca do próprio cadastro.  
Para pleno funcionamento do recurso é necessário configurar um atendente nos parâmetros gerais do sistema, visto que para realizar as movimentações o atendente informado será utilizado.  
Após efetuar o acesso, o cliente é direcionado diretamente ao módulo. Na visão de atendimentos cliente on line está disponível os filtros pré-definidos para facilitar a visualização dos registros.  
**Todos:**   Retorna todos os atendimentos do cliente logado.   
   
**Sob minha responsabilidade:** Retorna os registros que estão aguardando alguma ação do cliente. (Atenção.: a solicitação pode não estar em inserida no fluxo de atendimento ou retornou para análise/ações).  
   
**Aguardando retorno:**   Retorna os registros que não estão sob a responsabilidade do cliente. Os mesmos são apresentados somente leitura, com exceção do campo Discussão que sempre está disponível para inserções. Apenas o processo para incluir arquivos anexos estará disponível, os demais processos e ações estarão bloqueados até que o atendimento volte a responsabilidade do cliente.  
   
**Concluídos:**   Retorna todos os atendimentos que estiverem com a situação de concluído. Eles também não podem sofrer alterações e estarão sob modo somente leitura.  
   
**Cancelados:**   Retorna todos os atendimentos que estiverem com a situação de cancelado. Eles não podem sofrer alterações e estarão sob o somente leitura.  
   
Para garantir a segurança do sistema, é possível bloquear os tipos de atendimentos, através do anexo "Bloquear Tipo de Atendimento" no perfil do usuário, para que seja visualizado apenas os tipos que realmente forem necessários para o dia-a-dia no trabalho, impedindo assim o uso incorreto das informações.  
Ao incluir um novo atendimento, é obrigatório o preenchimento do Grupo e do Tipo para que o mesmo possa entrar em um fluxo de trabalho e seguir a movimentação desejada. Alguns campos são de preenchimento obrigatório para permitir que o atendimento possa seguir o fluxo de trabalho.   
Os parâmetros referentes ao tipo de atendimento informado na abertura do atendimento serão apresentados e será possível realizar configurações para torná-los obrigatórios, invisíveis ou somente leitura. Basta parametrizar em cada etapa do tipo de atendimento.  
   
Com o preenchimento de todos os campos para encaminhar o atendimento ao atendente responsável basta clicar no botão Salvar/Solicitar e informar a condição e o motivo de repasse.  
O atendimento será analisado e encaminhado com a possível solução ou com questionamentos na aba de discussão para posterior continuidade.  
Para facilitar a explicação ou exemplificação do que foi solicitado, os arquivos anexos podem ser utilizados. A *priori* somente a inclusão estará disponível. Este recurso tende a aumentar a compreensão do problema que será detalhado no entendimento pelo atendente responsável pela solução do atendimento. O entendimento pode ser aprovado ou reprovado pelo cliente. Cada etapa que o atendimento percorrer será gravado no histórico de etapas, onde é possível visualizar informações sobre a etapa atual e as etapas anteriores pelo qual o atendimento já passou.  
Uma solicitação (atendimento) realizada incorretamente pode ser cancelada e posteriormente excluída do sistema. Esta situação pode ocorrer devido a um engano ou duplicidade de atendimentos. Vale ressalatar que somente administradores do sistema possuem tal permissão e somente atendimentos sobre a responsabilidade do cliente podem ser cancelados.   
**Observação**  
O controle da visibilidade dos parâmetros do atendimento no Módulo de Cliente Online ocorre de forma independente aos parâmetros comuns (Aba Campos Invisíveis), ou seja, a configuração dos Campos Invisíveis não interfere na parametrização dos Campos Invisíveis Cliente Online e vice-versa. Para o restante dos campos Somente Leitura, Obrigatório, Necessário da Etapa Anterior,  o atendimento e o Módulo de Cliente Online irão continuar compartilhando o mesmo local de configuração no tipo de atendimento.

|  |  |
| --- | --- |
|  | Demais Recursos |

[  
Integração com Educacional - Abertura de Atendimentos|Integração Educacional - Abertura de Atendimentos] Pesquisa FAQ/Dica Pesquisa de Atendimentos
