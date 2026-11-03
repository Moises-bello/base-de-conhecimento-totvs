---
content_hash: 6f378b8042ef726d04b266a3879be122b55819e0f053f51a2cb292a3bfadfc23
fetched_at: '2026-06-29T00:10:58.229712+00:00'
page_id: '604524077'
product: rm
source: tdn-rm
title: Aluguel - Funil de Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Aluguel+-+Funil+de+Atendimento
version: 34
---

#FF9900Introdução

Ao selecionar o menu de funil de atendimento, serão exibidos todas as propostas de aluguel cadastradas no portal pelo corretor logado.

Esta funcionalidade permite também buscar propostas que estejam em andamento, facilitando a visualização do status das mesmas.

#FF9900Procedimentos para utilização 

##### **Agenda do corretor**

---

Para utilizar esta funcionalidade é necessário cadastrar os compromisso no Portal de Imóveis, na opção *Corretores > Compromissos,*

Todos os compromissos cadastrados para o corretor serão demonstrados no funil de atendimento, bem como a data, hora e os detalhes referentes ao compromisso, como mostra a figura:

##### **Jornada do cliente**

---

Função existente logo abaixo da agenda do corretor, onde serão exibidos todos os contratos que foram cadastrados no portal.

Na sessão **Novo** teremos a informação dos contratos cadastrados para locatários salvos recentemente na plataforma (Leads) e na coluna **Jornada,** serão exibidos os contratos que receberam algum atendimento ou clientes que fizeram alguma proposta de aluguel.

**Colunas:** Leads, Atendimento, Proposta, Contratos

Abaixo segue uma breve descrição sobre as colunas presentes no funil de atendimento:

* **Novo:** 
  + **Leads**: Exibição de Pessoas cadastradas recentemente na plataforma marcada como Leads.
* **Jornada:** 
  + **Atendimento**: Pessoas que já tiveram algum ação com o corretor, por exemplo realização de atendimento ao locatário.
  + **Proposta:**São todas as propostas cadastradas pelo corretor no Portal de Aluguel.
  + **Contratos**: São todos os contratos cadastrados pelo corretor no Portal de Aluguel.

Para definir em quais colunas as propostas serão exibidas, será necessário marcar a opção **"****Visível na página de Propostas"** ou **"Visível na página de Contratos"**, que fica localizada no backend do Portal de Imóveis no menu Situação Proposta (Aluguel).

##### **Opções presentes nos Cards do funil de atendimento**

---

* **Termômetro:** Onde será possível visualizar como está o andamento da proposta;
* **Simular:** Quando a proposta se encontra na coluna de "Propostas" ou "Contratos" o clique no botão simular irá levar o usuário para e edição da proposta. O botão simular quando clicado nas colunas de Atendimento ou Lead irá levar o usuário para a busca de imóveis, com o Lead já preenchido durante a etapa de criação da proposta.
* **Anexar Documento:** Ao clicar no ícone de Anexar documentos, poderemos, anexar os documentos faltantes ou substituir documentos que tenham sido enviados anteriormente. Será aberta a [interface de upload de documentos.](https://tdn.totvs.com/display/LRM/Aluguel+-+Simular+Proposta)
* **Ações:** Ao clicar no botão de ações, exemplificado no ícone ao lado, o corretor será apresentado com um menu onde serão mostradas as ações pertinentes àquela proposta. Vale lembrar que estas ações devem ser habilitadas de antemão pelo corretor no menu de situação da proposta (aluguel) no backend do Portal de Imóveis.

Dentro do menu Ações será possível realizar as seguintes tarefas:

**Imprimir:** Ao acessar esta funcionalidade será possível imprimir o relatório do contrato, esta opção é exibida nas colunas de clientes com propostas ou contratos, caso exista relatório parametrizado no RM, caso não tenha, será necessário cadastrar o relatório e associá-lo ao modelo de contrato selecionado na proposta.

**Contratos: Assinatura Eletrônica:**Essa opção estará disponível no menu de ações após realizar o sincronismo dos parâmetros de conexão do TOTVS Assinatura Eletrônica no backend do Portal de Imóveis. As informações de acesso para o TOTVS Assinatura Eletrônica são configuradas no RM, em Parâmetros Globais / Integração com TOTVS Assinatura Eletrônica.

Para maiores detalhes desta integração [consulte o link aqui.](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=562963400)

Ao clicar na opção de **Contratos: Assinatura Eletrônica,** o corretor então será apresentado com a tela de acesso do TAE. Ao realizar o acesso com sucesso, a tela fechará automaticamente e o usuário será direcionado para a visão de assinatura eletrônica, onde o corretor poderá associar os documentos ou um relatório, bem como definir os responsáveis assinantes ou validadores.

**Gestão da Assinatura:** Ao acessar esse menu, o usuário será redirecionado ao menu de [Status das Assinaturas,](https://tdn.totvs.com/display/LRM/Aluguel+-+Status+das+assinaturas) diretamente filtrado com os documentos pertinentes ao contrato.

**Avançar da proposta:**Quando o corretor deseja realizar uma ação de acordo com o padrão do Portal de Imóveis-vendas.

* **Editar:** Ao clicar no botão de editar , será possível editar os dados da proposta já salva anteriormente, como o nome do locatário, modelo de contrato, datas e o número do contrato.

##### **Busca através do funil**

---

Para realizar a busca o usuário poderá digitar diretamente no campo busca dados pertinentes às propostas, como Pessoa, Número de Celular, E-mail e Número do contrato.  
Importante: Caso deseje realizar uma busca com mais de um dado, por exemplo e-mail e celular, a pesquisa deverá ser separada por ponto e vírgula, como mostra a imagem abaixo, procurando por duas Pessoas distintas:

**Filtro por situação**

---

O sistema também permitirá realizar um filtro, onde somente as situações escolhidas deverão ser apresentadas. Como exemplificado na imagem abaixo, somente as situações no status de "Proposta" serão apresentadas:
