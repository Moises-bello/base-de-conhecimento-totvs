---
content_hash: 0d5d252d48c01851054507711a4f826981f60d1ed78ebab0552312b26dd0bd79
fetched_at: '2026-06-29T00:08:05.915100+00:00'
page_id: '236422396'
product: rm
source: tdn-rm
title: ER_EDUEDU001-2_Consulta_Inscritos_em_Vagas_Empresa
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_EDUEDU001-2_Consulta_Inscritos_em_Vagas_Empresa
version: 124
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Consulta de Inscritos em Vagas da Empresa** | | | |
| **Produto** | TOTVS Gestão Educacional | **Módulo** | EDU |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | EDUEDU001 | **IRM1** | EDUEDU001-1 |
| **Requisito1** | EDUEDU001-2 | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### Objetivo

O objetivo da nova funcionalidade é possibilitar que a empresa consiga consultar os candidatos que se inscreveram para as vagas que estão sendo ofertadas por ela.

### Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Vagas | [Alteração] | RM Portal | Empresa | Estágio/Emprego | Vagas | - |

A nova funcionalidade permitirá que as empresas consigam consultar os candidatos que já estão inscritos nas vagas ofertadas por ela.

Serão criadas permissões de acesso para permitir que a empresa consulte e/ou edite os candidatos inscritos nas vagas, conforme Figura 1.

Permissões:

* Acompanhamento de inscritos  
  Permitirá ao usuário da empresa visualizar as informações do candidato mas sem poder realizar nenhuma alteração.
* Editar parecer dos candidatos inscritos  
  Permitirá editar o campo de parecer para cada candidato inscrito. Só estará disponível caso o usuário tenha permissão de consultar os candidatos inscritos.
* Editar status dos candidatos inscritos  
  Permitirá editar o campo status para cada candidato inscrito. Só estará disponível caso o usuário tenha permissão de consultar os candidatos inscritos.
* Visualizar arquivos anexados pelo candidato inscrito  
  Permitirá visualizar os arquivos que foram anexados pelo candidato no momento da inscrição. Só estará disponível caso o usuário tenha permissão de consultar os candidatos inscritos.

Será criada uma nova tela de "Acompanhamento de inscritos, disponível no menu de Empresa | Estágio/Emprego | Acompanhamento Inscritos, para permitir a visualização, de acordo com as permissões, dos candidatos inscritos nas vagas, conforme Figura 2.

Os campos de "Status" e "Parecer" estarão disponíveis de acordo com a parametrização definida. Caso o usuário tenha permissão apenas para consultar os dados, os campos ficaram desabilitados no agrupador "Dados do candidato".

Assim que o usuário realizar a avaliação dos documentos, e caso tenha permissão para editar os dados do candidato, ele poderá alterar o status para  "Selecionado", definir um parecer e clicar no botão "salvar" para cada um dos candidatos. Isso se faz necessário pois o usuário precisa realizar a avaliação dos documentos de cada um dos candidatos.

Possíveis Status:

* Inscrito  
  Status inicial do candidato, é definido no momento em que o canditado faz sua inscrição na vaga.
* Selecionado  
  Status utilizado pela empresa para definir que o candidato foi selecionado para participar do processo de seleção.
* Em Avaliação  
  Status utilizado para definir que o candidato ainda está em processo de avaliação.

PS: Sempre que o status da vaga, no cadastro de vagas, for alterado para "Preenchida" os candidatos que tiverem o status de "Inscrito" ou "Em Avaliação" serão automaticamente alterados para "Preenchida", para indicar que o processo de seleção dessa vaga já foi concluído. Para mais detalhes ver documentação do cadastro de vagas e candidatos à vaga.

### Protótipo de Tela

Figura 1

Figura 2

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
