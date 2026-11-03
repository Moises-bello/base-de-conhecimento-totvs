---
content_hash: 18cfb3cb4d8201dc2813f8370d15f9efa0c0242c0fdabd2aa9648471cbc54885
fetched_at: '2026-06-29T00:06:21.294864+00:00'
page_id: '223168016'
product: rm
source: tdn-rm
title: DT_Coordenador_fazer_upload_materiais
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Coordenador_fazer_upload_materiais
version: 124
---

# Coordenador fazer upload materiais

# Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS* |
| **Módulo:** | *Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Associação de turma/disciplina | Associação de turma/disciplina a materiais |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Upload de materiais | Upload de materiais (professor) | | Upload de materiais | Upload de materiais (secretaria) | | Comissão coordenadora | Comissão coordenadora de matriz aplicada | |
| **Cadastros Iniciais:** | *Conceder permissão ao usuário do portal ao item de segurança “Associação de material – Comissão Coordenadora”.*  *Realizar o vínculo do usuário do portal com a matriz aplicada, anexo comissão coordenadora.* |
| **Requisito (ISSUE):** | PCREQ-8852 |
| **País(es):** | *Brasil* |
| **Tabelas Utilizadas:** | SWEBMATERIALSEC, SWEBMATERIALTURMADISC, STURMADISC, SCOORDENADOR |
| **Versões/Release:** | *12.1.9* |

## Descrição

Apresentar a nova funcionalidade de associação de materiais por participantes da comissão coordenadora – coordenador, assistente de curso, entre outros.

# Coordenador fazer upload materiais

 O coordenador de curso deverá ser cadastrado junto a matriz aplicada pelo cadastro de comissão coordenadora.

Após ser gerado o usuário de acesso ao coordenador e concedidas as devidas permissões, estará disponível no Portal do TOTVS Educacional, menu Professor, a opção de “Upload de Materiais”.

A funcionalidade de “Upload de Materiais” foi alterada para permitir a associação do material a todas as turmas/disciplinas de um período letivo, curso, série/habilitação ou disciplinas.

### **Associação de material**

**Permissão de acesso**

Foi criado um item de permissão de acesso ao menu, de nome “Associação de material – Comissão Coordenadora” (Cadastro de Perfil de Acesso > Educacional > Acesso aos menus > Outras permissões > RM Portal > Portal > Professor > Upload de Materiais > Associação de material – Comissão Coordenadora”).

Ao selecionar o botão “Associar turma”, usuários do Portal com permissão ao item citado anteriormente, seja do contexto do Ensino Básico ou Superior, visualizarão todos os cursos, séries, disciplinas e turmas/disciplinas relacionadas a matriz aplicada das quais são coordenadores.

Não será solicitado um contexto para o coordenador nesse caso, pois o sistema já será capaz de identificar todos os cursos/séries ou habilitações/turmas/disciplinas e disponibilizá-las de forma organizada.

**Coordenador - Professor**

Coordenadores que também possuem acesso de professor, visualizarão todos os períodos letivos (que não estejam encerrados e visíveis no Portal), cursos/séries ou habilitações/turmas/disciplinas vinculadas aos seus papéis.

Caso o professor não tenha a permissão de acesso supracitada, será visualizada apenas os dados das entidades citadas que o professor estiver vinculado.

**Seleção das entidades**

Após o usuário do sistema selecionar a opção “Associar turma”, citada acima, será aberta uma nova janela interna à página para a seleção de qual entidade poderá ser associada.

Baseado no usuário do Portal, serão disponibilizados os períodos letivos, cursos, séries/habilitação, disciplinas e turmas/disciplinas nas quais o usuário está como coordenador.

Não será feito nenhuma distinção do usuário devido ao cargo associado no cadastro de comissão coordenadora. Qualquer restrição deverá ser feita exclusivamente pelo perfil de acesso aos menus.

Os dados das entidades estarão dispostos no formato de árvore de registros (*treeview*), e com opção de seleção para cada nível, exemplo:

* Período Letivo – Código Período Letivo (SPLETIVO)
* Curso – Código e Nome do Curso (SCURSO)
* Série ou Habilitação – Código e Nome (SHABILITACAO)
* Disciplina – Código da Disciplina e Nome da Disciplina (SDISCIPLINA)
* Turma/Disciplina – Código da turma disciplina (STURMADISC)

Caso o usuário do sistema marque a opção para Curso, ao clicar no botão associar, o sistema irá disponibilizar o material para cada turma/disciplina daquele curso, o mesmo para Série/Habilitação, Disciplina.

O vínculo do material continuará sendo feito entre os registros da tabela de material “SWEBMATERIALSEC” e os registros das turmas/disciplinas “SWEBMATERIALTURMADISC”, isso se faz necessário, para manter a compatibilidade com a funcionalidade existente de “Upload de Material” pelo professor.

Na visão de upload de materiais, abaixo de cada material serão listadas as turmas/disciplinas associadas àquele material, com a opção de exclusão. Estará disponível uma nova opção de exclusão das turmas/disciplinas selecionadas vinculadas ao arquivo.

**Restrições**

Serão visualizados apenas as turmas/disciplinas ativas, de períodos letivos que **não** estejam encerrados, disponíveis no portal, vinculados a mesma matriz aplicada que o usuário do sistema pelo cadastro de comissão coordenadora.

**Exclusão do vínculo de turmas/disciplinas com Arquivos**

Acima da lista de turmas/disciplinas vinculadas ao material foi incluído o botão de “Desassociar Turmas” para cada material. Para cada registro selecionado será feito a exclusão.

divs
