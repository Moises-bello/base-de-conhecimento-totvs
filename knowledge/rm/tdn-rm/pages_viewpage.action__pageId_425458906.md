---
content_hash: e6458695659defb59defffb83af1f518e8768a918f077049cf451160dbd8dcdb
fetched_at: '2026-06-29T00:09:32.710610+00:00'
page_id: '425458906'
product: rm
source: tdn-rm
title: Integração TOTVS Educacional com BackOffice Protheus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458906
version: 10
---

---

**TOTVS Educacional**  
   
O TOTVS Educacional, permite a instituição de ensino iniciar seus trabalhos depois da captação de alunos, sendo montado uma estrutura curricular, para serem ofertadas aos alunos e professores. Cadastram-se cursos, disciplinas, matrizes curriculares para depois ofertá-las aos alunos nos períodos letivos, turmas etc. Depois da estrutura curricular montada e ofertada, a instituição de ensino poderá realizar a matrícula de seus alunos e dar permissão aos seus professores para registrarem as notas e faltas dos alunos. Iniciado o período letivo de uma instituição de ensino, algumas rotinas são realizadas com frequência, tais como: Transferência de alunos, atividades extracurriculares, avaliação institucional, emissão de certificados/diplomas, solicitação de recursos/instalações, alocação de salas e etc. Para essas rotinas relacionadas a estrutura acadêmica, damos o nome de movimentação acadêmica. Outro ponto de movimentação na instituição de ensino, são os processos que acontecem na tesouraria e/ou financeiro. Nessa etapa, são cadastrados os planos de pagamentos, parcelas, bolsas, geração de lançamentos, boletos de pagamentos e etc. Faz parte do fluxo processual do TOTVS Educacional as integrações com outros sistemas/módulos como Gestão de Relacionamento com Clientes, Folha de pagamento, Gestão Bibliotecária, Gestão Financeira entre outros.  
   
   
**TOTVS Educacional x BackOffice Protheus ( Integração )**  
   
A  integração entre os sistemas TOTVS Educacional e o BackOffice do Protheus, utilizando mensageria única. A integração atual é realizada por tabelas intermediarias, sendo os módulos da linha RM realizando consulta em determinadas tabelas do módulo do Protheus. Este cenário necessita uma nova conexão para que a linha RM possa consumir informações na base do Protheus. Sendo assim, considerando o cenário atual, possuímos diversas situações onde são usados sistemas de linhas diferentes em nossos clientes e para facilitar e agilizar a utilização por nossos clientes, essa integração será rescrita utilizando mensageria única.  
Nessa integração alguns parâmetros da integração financeira não serão habilitados, como por exemplo "Cancelar Remessa automaticamente ao regerar o lançamento financeiro quando o boleto estiver com status Remetido ou Registrado", já que as ações em cima dos lançamentos gerados para esses casos devem ser realizadas no ambiente Protheus.

**Entidades Acadêmicas x Cadastro Pessoas ( Protheus )**  
Se a integração estiver ativa, todo aluno cadastrado no Educacional deverá ter o seu correspondente no cadastro de pessoas do Protheus. Ao alterar ou excluir um cadastro do aluno, as alterações devem ser refletidas no seu cadastro no Protheus. Ao realizar uma exclusão de um aluno será verificado se a pessoa do aluno está vinculada a alguma outra entidade no Educacional, como pesquisador ou participante das bancas de TCC e/ou estágio e para esses casos a mensagem de exclusão de pessoa não será enviada. A mensagem de exclusão de pessoa será enviada para o Protheus, somente quando a pessoa da entidade educacional não estiver vinculada a nenhum outra.  
   
**Definição de Mensagem Única – TotvsMessage**  
   
Durante o processo de consolidação de marcas, iniciado pela TOTVS, várias empresas diferentes forma adquiridas e com elas vários produtos passaram a compor o portfólio de ofertas disponível aos clientes. Esta expansão de ofertas permitiu que clientes de uma marca, antes limitados pelas opções com aquela "etiqueta", pudessem agora compor o seu ambiente de TI, utilizando produtos de origens diferentes (Ex.: TOTVS Educacional + BackOffice Protheus). Com o objetivo de padronizar as integrações com os produtos TOTVS, foi definido uma nova diretriz para os projetos de integração: A de que todos os produtos TOTVS devam trabalhar com uma mensagem XML única, evitando desta forma, o processo de transformação de mensagens.  
 

Veja Também

---

[TOTVS Educacional x BackOffice Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=497923390)
