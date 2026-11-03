---
content_hash: 4c4127be35ff00a47c050f24262e370d664e6630f9e5d1b89c5863c07a28261a
fetched_at: '2026-06-29T00:12:00.040621+00:00'
page_id: '878912532'
product: rm
source: tdn-rm
title: Upload de materiais
type: documentation
url: https://tdn.totvs.com/display/LRM/Upload+de+materiais
version: 5
---

Nessa página, o professor terá a visão geral da gestão de documentos vinculados e a serem vinculados nas Turmas/disciplinas. Além disso, o professor contará com o Filtro, onde será possível otimizar a visualização da consulta dos documentos que já foram incluídos e vinculados na turma/disciplinas.

Permissão de acesso

Para acessar a funcionalidade, o perfil do professor deverá ter a permissão em: **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Upload de materiais.**

Parametrização de armazenamento

Para acessar a funcionalidade, será necessário realizar informar as extensões permitidas e o tamanho máximo do arquivo em: **Configurações | Parâmetros | RM Portal |RM Portal | Geral | Portal - Geral 3/15**

Tamanho de arquivo configurado no IIS

A configuração do iis determina o tamanho máximo de arquivo aceito e prevalece sobre a configuração do rm, deve avaliar o tamanho máximo de conteúdo permitido, para configurar esse parâmetro no iis deve seguir os seguintes passos:

* Abrir o Gerenciador do IIS.
* Selecione o site que você deseja configurar.
* Certifique-se de estar na Visualização de Recursos pelo botão na parte inferior do gerenciador.
* Selecione Filtragem de Solicitações e abra-a clicando duas vezes no ícone. O painel Filtragem de Solicitações é exibido.
* No painel Ações no lado direito da tela, clique no link Editar configurações de recursos.... A janela Editar configurações de filtragem de solicitação é exibida.
* Na seção Limites de solicitação, insira o tamanho máximo de conteúdo permitido apropriado (Bytes) e clique no botão OK.
* Reinicie o IIS.
Extensões de arquivos permitidas

Caso o campo "Extensões de arquivos permitidas" esteja vazio, o sistema irá permitir **todas** as extensões possíveis.

Tipo de materiais

Para que seja possível inserir o material é necessário possuir ao menos um tipo de material cadastrado. **Esta funcionalidade não foi migrada, portanto é feita no Portal Corpore.Net**

Para acessar a funcionalidade, o perfil do professor deverá ter a permissão em: **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Administração| Tipos de materiais.**

Cadastro de tipo de materiais no portal Corpore.Net

No Corpore.Net será possível **realizar a manipulação dos dados de "Tipo de materiais"**. Para acessar a funcionalidade **Administração | Tipos de materiais**

Incluir arquivo

Para incluir arquivo, o professor, deverá clicar no botão: **+** (incluir)

Ao clicar nesse botão, o professor será redirecionando para uma nova tela, onde deverá informar: descrição do material **\***,  tipo de Material **\***, a data de expiração e o arquivo.

> **\***  São campos obrigatórios a serem informados pelo professor no momento da inclusão do novo arquivo.

Em seguida, clicar no botão: 'Salvar' (no topo da tela)

Após inserir as informações, clicar no botão: Salvar, o TOTVS Educa Mobile irá apresentar uma mensagem, que o material foi incluído com sucesso.

Realizar download

Na página principal, o professor deverá clicar sobre o documento que em seguida será realizado o download.

Editar arquivo

Para "Editar" o arquivo, o professor deverá realizar o processo através do Novo portal do professor ou pelo Corpore.Net.

Excluir arquivo

Para excluir o arquivo, o professor professor poderá selecionar um ou mais material, mesmo que o mesmo esteja compartilhado à uma turma/disciplina.

Para realizar o processo, o professor deverá selecionar um ou mais material, e clicar no botão: Excluir ( Disponível no topo da tela) . Caso o material esteja compartilhado com uma Turma/disciplina, o portal irá emitir uma mensagem alertado que o(s) materal(is) está(ão) vinculado(s) a uma turma/disciplina.

Ao clicar no botão: Confirmar, o(s) matarial(is) será(ão) removido(s) conforme a apresentação da mensagem abaixo.

Compartilhar os arquivos nas turmas/disciplinas

Para compartilhar o arquivo, é necessário selecionar o(s) arquivo(s) e clicar no ícone: Compartilhar.

Ao clicar no botão compartilhar, o sistema irá abrir nova tela, onde será listado a relação de turmas/disciplinas que o professor leciona.

O Professor tem a opção de selecionar um ou todas as turma/disciplinas desejada e em seguida, clicar no botão salvar.

Após clicar no botão: Salvar, o portal irá apresentar uma mensagem informando que o arquivo foi compartilhado com sucesso.

       

Remover compartilhamento de material

Para remover os arquivos pontualmente, o professor deverá expandir a visualização através do ícone:  onde são listados a relação de turmas/disciplinas vinculadas.

   

Será apresentado o botão: "Desassociar",  onde é necessário selecionar uma ou todas as turma/disciplinas listadas, e clicar no mesmo para que o "descompartilhamento" seja realizado.
