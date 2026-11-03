---
content_hash: 3fbb322bab827bc47a9f89a3d0b2adfe7bc03316475b9bd18595494279dfe3e2
fetched_at: '2026-06-29T00:09:33.908004+00:00'
page_id: '425459079'
product: rm
source: tdn-rm
title: Grupo de Atendentes
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupo+de+Atendentes
version: 3
---

**Grupo de Atendentes**   
Esta tela permite o cadastro de grupo de atendentes.   
Através do cadastro é possível controlar:  
 Identificação   
Nesta janela você define a identificação do grupo de atendentes e o esquema de repasse de atendimento para esse grupo. O esquema de repasse é a forma como o atendimento vai ser repassado e para qual atendente do grupo.   
Siga os próximos passos:  
Código do Grupo  
Nesse campo, o sistema preenche automaticamente o número identificador do grupo de atendentes. O número identificador inserido pelo sistema é único para cada grupo. Esse campo é desabilitado para edição.   
Inativo  
Esta opção permitirá excluir todas as permissões de repasses dos atendentes vinculados ao grupo em questão.  
Grupo  
Preencha nesse campo a descrição do nome do grupo de atendentes. Esse campo é de preenchimento obrigatório, ou seja, o sistema só permite que o grupo seja salvo se esse campo estiver preenchido.   
**Tipo de repasse**  
Você pode selecionar qual o tipo de repasse será utilizado para o grupo que está sendo cadastrado.   
**Para um atendente fixo do grupo**  
Selecione esta opção caso apenas um atende do grupo seja o responsável pelo recebimento do atendimento, ou seja, os atendimentos repassados vão ser encaminhados para um atendente fixo.   
Ao selecionar essa opção, será necessário informar o Atendente que receberá as ocorrências.  
**Atenção**  
O sistema exibe o nome dos atendentes que estão ativos no TOTVS Aprovações e Atendimento e se ele for um funcionário, seu status no RM Labore deve ser diferente de D - Demitido.  
Caso os campos acima não sejam preenchidos, o sistema exibe uma tela com uma mensagem informando sobre a necessidade do preenchimento dos campos.   
**Por um rodízio entre os atendentes do grupo**  
Selecione esta opção caso você deseja que os atendimentos sejam repassados de acordo com um rodízio entre os atendentes do grupo. Os atendimentos são encaminhados a cada instante para um atendente do grupo até que todos recebam atendimentos. No momento que todos os atendentes já receberam atendimentos, o sistema recomeça a repassar seguindo o rodízio. Dessa forma, todos os atendentes do grupo recebem a mesma quantidade de atendimentos.   
**Para o atendente do grupo com o menor número de atendimentos**  
Selecione esta opção caso você deseja que o sistema envie os atendimentos para o atendente do grupo que possui a menor quantidade de atendimentos na pasta pendente. O sistema valida no momento de repassar o atendimento para o grupo, qual dos atendentes possui a menor quantidade de atendimentos na pasta pendente e repassa o atendimento para ele. Em todos os momentos que o repasse é executado para esse grupo o sistema realiza a validação.   
**Atenção**  
Caso sejam selecionadas as opções: Por um rodízio entre os atendentes do grupo e Para o atendente do grupo com o menor número de atendimentos, é necessário que sejam definidos os atendentes do grupo na pasta Atendentes do grupo.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Esquema de Repasse  Atendentes do Grupo
