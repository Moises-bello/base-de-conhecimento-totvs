---
content_hash: 869fa7ed53a1d131322989a15a98fc6125165720b9284e1db639bbed8dc71d33
fetched_at: '2026-06-29T00:09:34.461864+00:00'
page_id: '425459159'
product: rm
source: tdn-rm
title: Biblioteca - Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459159
version: 9
---

---

Nesta etapa é definido com qual sistema de biblioteca o TOTVS Educacional irá integrar.

**Biblioteca 1/6**

Será possível integrar com o TOTVS Gestão Bibliotecária ou com Pergamum.

Quando integrado com um sistema de biblioteca poderá ser parametrizado se haverá bloqueio de matrícula/mudança de status no período letivo caso o alunos estejam com:

* Empréstimos em atraso na biblioteca;
* Débitos na biblioteca.

Quando o TOTVS Educacional estiver integrado com o Pergamum, será necessário informar:

* Os parâmetros de conexão com Pergamum via Web service com informações de caminho (endereço) e chave de Acesso do Web service .
* Os parâmetros para envio das fotos via FTP para o Pergamum com o caminho, usuário e senha.

Observações

À partir das versões listadas abaixo, o Pergamum deverá estar com a versão mais recente e com os parâmetros abaixo configurados:

* Código da pessoa deve ser parametrizado no Pergamum para utilizar alfanumérico com o tamanho 20.
* Código do departamento deve ser parametrizado no Pergamum para utilizar alfanumérico.

Se estas configurações não estiverem definidas não será possível ativar nem alterar a integração com o Pergamum.

* Versões:
  + 12.1.24.286
  + 12.1.25.247
  + 12.1.26.195
  + 12.1.27.137

**Biblioteca 2/6**

Nesta etapa é informado os parâmetros para acesso ao banco de dados do Pergamum.

Observações

À partir das versões abaixo, estas informações de acesso a banco foram descontinuadas pois a equipe do Pergamum disponibilizou um serviço via webservice que carrega estas informações.

* 12.1.24.285
* 12.1.25.246
* 12.1.26.195
* 12.1.27.130

Data da última atualização dos status de alunos e data da última atualização dos status de funcionários: Quando executado o processo Atualiza status dos alunos e funcionários do Pergamum será armazenado a data em que o processo foi executado com sucesso.

**Biblioteca 3/6**

Aqui é informado as seguintes informações refente a integração entre o TOTVS Educacional e Pergamum:

Código da instituição do Pergamum: vínculo entre a coligada TOTVS e a instituição do Pergamum.

Código categoria para os alunos: será possível estabelecer um código de categoria padrão para todos os alunos de um determinado contexto.

Código categoria para os professores:será único para todos os níveis de ensino de uma mesma filial e será replicada para todos os níveis de ensino desta coligada e filial.

Código categoria para os funcionários: será único para todos os níveis de ensino de uma mesma filial e será replicada para todos os níveis de ensino desta coligada e filial.

Código de situação normal: o usuário está ativo no Pergamum.

Código de situação afastado: o usuário está desativado no Pergamum.

O parâmetro "Criar usuário no Pergamum automaticamente após matrícula do aluno no período letivo",  habilitado permite que o usuário do aluno seja criado automaticamente no Pergamum.  
   
Enviar o domínio com o usuário de rede quando integrado com LDAP na exportação de Usuários.

**Importante:**Para o funcionamento do parâmetro acima é necessário que a integração LDAP esteja habilitada e configurada nos parâmetros globais. O domínio somente será enviado caso o mesmo esteja preenchido no cadastro do Usuário e vinculado à entidade, caso o mesmo não esteja preenchido o domínio não será enviado.  
Além disso, caso o usuário de rede não estiver preenchido, será enviado o usuário RM da entidade.

 Enviar o nome social, quando preenchido, na exportação de usuários - a finalidade deste parâmetro é a de possibilitar o envio do Nome Social, quando o mesmo estiver preenchido no cadastro da Pessoa (Aluno/Professor/Funcionário/Pessoa).

Utilizar estado civil padrão para exportar usuários com estado civil vazio - a finalidade deste parâmetro habilitar a definição de qual será o estado civil padrão das entidades ao exportar/atualizar para o Pergamum caso o mesmo esteja vazio em seu respectivo cadastro.

**Biblioteca 4/6**

Atualizar código da categoria do aluno:

Nunca   
Não será realizado nenhum tipo de atualização.

Após a matrícula no período letivo   
A atualização somente ocorrerá ao matricular o aluno no período letivo em uma situação de matrícula com o item "Desativa usuário no Pergamum" desmarcado.

Após o encerramento do período letivo   
Será disparada automaticamente a atualização das categorias dos usuários do Pergamum relacionados aos alunos. O sistema irá busca todos os alunos matriculados no período letivo, cujo período encerrado esteja parametrizado com o "Período letivo anterior". Exemplo: ao encerrar o período letivo 2018/2 o sistema irá pesquisar o período letivo (ex. 2019/1) que tenha como período letivo anterior 2018/2. Ao localizar, todos os alunos do período letivo encontrado (ex. 2019/1) terão sua categoria alterada no Pergamum.

**Biblioteca 5/6**

No passo atual temos a possibilidade de informarmos qual a chave de integração de Usuários e Alunos e o que fazer no momento de criação de usuário quando o aluno possuir mais de um RA.  
Usuários (Professor/Funcionários/Pessoas) - Poderão ser utilizados os seguintes campos como chave no Pergamum:

Código da Pessoa

CPF

Aluno - Poderão ser utilizados os seguintes campos como chave no Pergamum:

Código da Pessoa

CPF

RA

Caso o usuário possua mais de um Ra cadastrado

Enviar todos os RA do aluno para o Pergamum (Será criado um usuário para cada RA)

Enviar o primeiro RA encontrado (Será criado apenas um usuário)

**Biblioteca 6/6**

Quando for necessário desativar o usuário do Pergamum de um funcionário que foi demitido, poderá definir a ação a ser executada quando ocorrer erro na comunicação com o Pergamum. As ações disponíveis são: Emitir erro impedindo a efetivação da demissão ou permitir a demissão.  
   
Atualizar dados cadastrais automaticamente no Pergamum  
Ao habilitar este parâmetro, todo vez que ocorrer a alteração no cadastro de um aluno, professor, pessoa ou funcionário será atualizado o cadastro do usuário do Pergamum.  
Caso  ocorra erro de comunicação com Pergamum no momento da alteração do cadastro será possível  parametrizar  para Emitir erro impedindo a gravação da alteração ou Permitir a gravação da alteração.
