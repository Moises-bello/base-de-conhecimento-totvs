---
content_hash: 4de0568f340ba855e0533b00d147d75aa020e27d8623483e5540f1d7d69cbe4c
fetched_at: '2026-06-29T00:08:25.661923+00:00'
page_id: '270921743'
product: rm
source: tdn-rm
title: RMEDU00006_Upload de Materiais
type: documentation
url: https://tdn.totvs.com/display/LRM/RMEDU00006_Upload+de+Materiais
version: 8
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Educacional |
| **Versões:** | 12.1.14 |
| **Passo a passo:** | Upload de Materiais |

TOTVS Educacional

Configurações | Parâmetros

Configurações | Parâmetros | RM Portal | RM Portal – Gerais

Informar parâmetros para utilização da funcionalidade

Portal – Geral 4/8

Arquivos

1 – Informar onde o arquivo será salvo após Upload

**Para que o sistema grave o arquivo no diretório do servidor, baste que o grupo de usuários do IIS tenha acesso de leitura e gravação no diretório, sem a necessidade de permissão para o usuário TODOS.  
O grupo de usuários do IIS muda de acordo com a versão do mesmo, conforme descrito no link link: [https://support.microsoft.com/pt-br/help/981949/description-of-default-permissions-and-user-rights-for-iis-7-0-and-lat](https://www.google.com/url?q=https://support.microsoft.com/pt-br/help/981949/description-of-default-permissions-and-user-rights-for-iis-7-0-and-lat&sa=D&source=hangouts&ust=1567080722204000&usg=AFQjCNHTLn27jMVdFJnoqi_CB2wCw-YosA)  
  
IIS 6.0 o grupo é o IIS\_WPG  
IIS 7.0 o grupo é o IIS\_IUSRS  
  
Na máquina de teste, em que o IIS é o 7.0, bastou que fosse concedida a permissão de leitura e gravação para o grupo de usuários IIS\_IUSRS  
Dessa forma, a obrigatoriedade de liberação para TODOS não é necessária, melhorando a segurança dos dados (arquivos) e informações de alunos e professores.**

imagem.

Segurança da pasta

Na utilização do ambiente local (Duas Camadas) todas as informações devem ser inseridas acessando o servidor onde o Portal estiver instalado.

Na utilização de “N” (Três ou mais) camadas as informações podem ser inseridas em qualquer servidor (host ou app) desde que o diretório esteja acessível pelo servidor de Host.

2 – Salvar tamanho máximo de Armazenamento

Informar o tamanho máximo do arquivo por usuário

3 – Extensões de arquivos permitidas

Informar as extensões de arquivos permitidas para armazenamento

Exemplo:

Docx;Pdf;Ppt;rar;zip;

4 – Observar parâmetro "Visualizar apenas materiais de disciplinas com status"

Marcando o parâmetro os arquivos são visíveis apenas para alunos que tenha a situação de matricula na disciplina com o parâmetro marcado.

Ensino Superior

Ensino Básico

Serviços Globais

Configuração de Perfis para acesso ao portal (Alunos – Professores)

Perfil do Professor

Segurança | Perfil

Selecionar Perfil do Professor

Atentar-se para o sistema ... (Educacional)

Validação das permissões do perfil para utilização da funcionalidade pelos professores

As opções abaixo definem o que o professor pode fazer no menu Upload de Matérias

O menu Administração é de extrema importância, neste menu que liberamos os tipos de materiais e o público alvo, tal cadastro é realizado uma única vez.

Os tipos de materiais são obrigatórios para utilização da funcionalidade

Cadastrar os tipos de materiais

Após configurações do Perfil acessar o portal com o usuário com as permissões necessários para acessar o contexto Educacional e criar os tipos de matérias, deve ser realizado por usuário com permissão no contexto acadêmico e menus no perfil liberados para acesso.

Selecionar a opção Educacional

Selecionar a opção Administração

Tipos de matérias | Incluir

Os materiais podem ser direcionados para Alunos, Professores e Todos, recomendamos que sejam criados um tipo cara cada público alvo, assim os acessos aos materiais postados ficam restritos ao seu público alvo.

Perfil do Aluno

Segurança | Perfil

Selecionar Perfil do Aluno

Liberar permissão nos menus específicos para a funcionalidade

Arquivos da instituição são arquivos postados sem relacionamento com turmas disciplinas

Arquivos por Turma disciplina são arquivos vinculados a turmas disciplinas.

Inclusão do Material no Portal (Professor)

Upload de Materiais

Incluir materiais para um público alvos especifico (Alunos)

Selecionar a opção Educacional

Professor | Upload de Materiais | Incluir

Descrição, nome dado a material postado

Tipo de Material, público alvo

Data de Expiração, é possível definir uma data de validade para o material, deixando a data em branco é material é valido sempre.

Seleção do Arquivo

Material postado

Vincular material a Turma disciplina

Material associado a turma disciplina

Existindo a necessidade de desassociação do material, selecionar o item e clicar no botão “Desassociar Turma”

Visualização do Material (Alunos)

Acessar o Portal com o Usuário Aluno

Educacional

Arq. por disciplina (Download)
