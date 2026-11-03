---
content_hash: e4826ff722ec2800f3e44c19168353fff53c87b161f164e479092bacc2ce115e
fetched_at: '2026-06-29T00:12:00.677933+00:00'
page_id: '883660171'
product: rm
source: tdn-rm
title: Guia para Alteração de Foto do Aluno (A partir da 12.1.2502)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=883660171
version: 11
---

### Demonstração

#### Efetuando um upload de uma foto com extensão correta.

#### Efetuando um upload de uma foto com formato inválido.

Permissões Necessárias

Para alterar a foto do aluno, é essencial que você tenha as permissões adequadas em seu perfil de usuário. As ações de remover, adicionar ou trocar a foto dependem dessas permissões.   
  
Configurações por Contexto  
  
A possibilidade de um aluno alterar sua foto depende das configurações específicas do contexto em que está matriculado (coligada, filial, nível de ensino). Um parâmetro configurável por contexto determina se essa funcionalidade está disponível. Certifique-se de que:

* O aluno está matriculado no contexto em questão.
* O contexto permite a alteração de foto.
* Você está ciente do tamanho máximo e dos formatos de imagem aceitos.

Para acessar as configurações .

### Alunos em múltiplos contextos

Permissão Concedida: Se pelo menos um dos contextos permitir a troca de foto e você tiver as permissões necessárias, a alteração pode ser realizada. Mesmo que outros contextos não permitam a troca, a permissão em um contexto é suficiente para proceder.

### Especificações da Imagem

Ao selecionar uma imagem para upload, atente para os seguintes detalhes:

#### Formatos Aceitos

* JPEG
* JPG

Esses formatos garantem compatibilidade com o sistema TOTVS Educacional.

#### Tamanho Máximo

Até 3 MB (3000 KB), imagens que excedam esse tamanho não serão aceitas devido às restrições do sistema.

### Responsável com acesso a vários alunos

O sistema verificará o contexto de cada aluno individualmente.  
As regras de alteração de foto serão aplicadas de acordo com o contexto específico de cada aluno.  
Certifique-se de selecionar o aluno correto antes de iniciar o processo.

### Aluno que também é funcionário

Caso o aluno também seja funcionário, o sistema não permitirá a alteração da sua foto pelo portal, mesmo que possua todas as permissões descritas acima.

### Utilização da Inteligência Artificial para validar a foto

É possível utilizar a **inteligência artificial** para validar (mediante um regra definida) a foto que o usuário esteja fazendo upload, para isso acesse as configurações do portal em .

Com todas as configurações efetuadas, basta o usuário ir ao portal e submeter uma foto, se ela não for válida, conforme regras estipuladas, o portal irá rejeitá-la.

#### Demonstração

##### Efetuado um upload de uma foto válida.

##### Efetuando um upload de uma foto **inválida**
