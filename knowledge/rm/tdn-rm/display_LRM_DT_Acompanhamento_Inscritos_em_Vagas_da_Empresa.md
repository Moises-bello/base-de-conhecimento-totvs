---
content_hash: aea310247f79b00bf78c68b4fb93e9282b75ca7477bc81c3d93c9b5cf1e6205b
fetched_at: '2026-06-29T00:08:09.001277+00:00'
page_id: '239018787'
product: rm
source: tdn-rm
title: DT_Acompanhamento_Inscritos_em_Vagas_da_Empresa
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Acompanhamento_Inscritos_em_Vagas_da_Empresa
version: 119
---

# Acompanhamento de inscritos em vagas da empresa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Acompanhamento de Inscritos* | *Acompanhamento de inscritos em vagas da empresa* | |  |  | |
| **Cadastros Iniciais:** | *Cadastro de Empresa, Cadastro de Vagas, Cadastro de Candidatos à Vaga* |
| **Requisito (ISSUE):** | EDUEDU001-2 |
| **País(es):** | *Todos* |

## Descrição

O objetivo da nova funcionalidade é possibilitar que a empresa consiga consultar os candidatos que se inscreveram para as vagas que estão sendo ofertadas por ela.

## Procedimento para Utilização

A nova funcionalidade permite que as empresas consigam consultar os candidatos que já estão inscritos nas vagas ofertadas por ela.

Foram criadas permissões de acesso para permitir que a empresa consulte e/ou edite os candidatos inscritos nas vagas.

Permissões:

* Acompanhamento de inscritos  
  Permitirá ao usuário da empresa visualizar as informações do candidato mas sem poder realizar nenhuma alteração.
* Editar parecer dos candidatos inscritos  
  Permitirá editar o campo de parecer para cada candidato inscrito. Só estará disponível caso o usuário tenha permissão de consultar os candidatos inscritos.
* Editar status dos candidatos inscritos  
  Permitirá editar o campo status para cada candidato inscrito. Só estará disponível caso o usuário tenha permissão de consultar os candidatos inscritos.
* Visualizar arquivos anexados pelo candidato inscrito  
  Permitirá visualizar os arquivos que foram anexados pelo candidato no momento da inscrição. Só estará disponível caso o usuário tenha permissão de consultar os candidatos inscritos.

Foi criada uma nova tela de "Acompanhamento de inscritos", disponível no menu de "Empresa | Estágio/Emprego | Acompanhamento Inscritos" do Portal, para permitir a visualização, de acordo com as permissões, dos candidatos inscritos nas vagas.

Os campos de "Status" e "Parecer" estarão disponíveis de acordo com a parametrização definida. Caso o usuário tenha permissão apenas para consultar os dados, os campos ficaram desabilitados no agrupador "Dados do candidato".

Assim que o usuário realizar a avaliação dos documentos anexados pelo candidato, e caso tenha permissão para editar os dados, ele poderá alterar o status para  "Selecionado", definir um parecer e clicar no botão "salvar" para cada um dos candidatos. Isso se faz necessário pois o usuário precisa realizar a avaliação dos documentos de cada um dos candidatos.

Possíveis Status:

* Inscrito  
  Status inicial do candidato, é definido no momento em que o candidato faz sua inscrição na vaga.
* Selecionado  
  Status utilizado pela empresa para definir que o candidato foi selecionado para participar do processo de seleção.
* Em Avaliação  
  Status utilizado para definir que o candidato ainda está em processo de avaliação.

PS: Sempre que o status da vaga, no cadastro de vagas, for alterado para "Preenchida" os candidatos que tiverem o status de "Inscrito" ou "Em Avaliação" serão automaticamente alterados para "Preenchida", para indicar que o processo de seleção dessa vaga já foi concluído. Para mais detalhes ver documentação do cadastro de vagas e candidatos à vaga.

divs
