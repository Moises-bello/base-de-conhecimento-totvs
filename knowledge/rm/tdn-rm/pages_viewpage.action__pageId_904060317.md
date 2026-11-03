---
content_hash: 418f94656a083072a2b821d669bc7185fc9cf405703df7922a3838c7e60d4080
fetched_at: '2026-06-29T00:12:02.779736+00:00'
page_id: '904060317'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Web - Portal do Cliente Locação - PDC
  - Atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=904060317
version: 9
---

---

### 🔑 1. Acesso e Permissão para o Usuário

No primeiro momento, será necessário conceder a permissão ao usuário através do cadastro de perfis no Acesso a Menus:

* `Gestão de Imóveis (Portal) \ Cliente \ Atendimento`

### 🖥️ 2. Interface e Parâmetros

Ao acessar a opção de Atendimento, o PDC apresenta ao usuário as seguintes informações:

#### 🔍 Seleção de Contexto

* **Empreendimento:**
* **Contrato:**

### 📥 3. Painel para Nova Solicitação de Atendimento

*(Localizado à esquerda da tela)*

* **Selecione o Imóvel:** O cliente deve selecionar o Imóvel para o qual ele deseja abrir atendimento. **[Campo Obrigatório]**
* **Selecione o Tipo de Atendimento:** O Cliente deve selecionar o [tipo de atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=641160309#NovoAtendimento--2120360178) mais adequado à solicitação do atendimento. **[Campo Obrigatório]**

#### 📝 Detalhes do Atendimento

*(Localizado à esquerda da tela, logo abaixo do painel acima)*

* **Título:** O Cliente deve informar o título/assunto do atendimento. É recomendável que ele seja preenchido com um assunto pertinente, para que o mesmo seja localizado facilmente no painel de histórico do atendimento detalhado ao final deste documento. **[Campo Opcional]**
* **Descrição:** Este campo é para que o Cliente possa descrever os detalhes da solicitação criada. **[Campo Obrigatório]**
* **Envio de Arquivo:** Caso o tipo de atendimento selecionado permita, o Cliente poderá ou será obrigado a enviar arquivos para o atendimento criado.

  + **Botão Selecionar Arquivos:** Para os tipos de atendimento em que é permitido o envio de arquivos, este botão será habilitado. É permitido o envio dos arquivos com as extensões abaixo:

    - **Extensões de imagens:** JPG, JPEG, PNG, BMP, GIF;
    - **Extensões de documentos:** TXT, DOC, DOCX, XLS, XLSX, PDF, DWG.
  + **Exclusão de Anexos:** Caso seja anexado algum arquivo por engano, o Cliente pode utilizar o botão para excluir este arquivo que fica localizado logo abaixo, à direita da barra de progresso do envio deste arquivo.
  + **Limite de Tamanho:** O limite de tamanho do envio de arquivos é definido no parâmetro [*Geral*](https://tdn.totvs.com/pages/viewpage.action?pageId=731881683) do TCGI e nos parâmetros de [*Arquivos Anexos ao Atendimento*](https://tdn.totvs.com/pages/viewpage.action?pageId=425458436)  do TAA.

#### ⚙️ Botões de Ação do Painel

* **Botão Limpar:** Permite limpar as informações preenchidas nos campos acima, caso o Cliente julgue necessário.
* **Botão Salvar:** Salva e envia o atendimento no TCGI. Após acionado, o sistema exibirá o atendimento criado no painel de histórico de atendimento, detalhado abaixo.

### ⏳ 4. Painel de Histórico de Atendimento

*(Localizado à esquerda desta visão)*

#### 🗂️ Agrupador por Título do Atendimento

* **Protocolo:** É o protocolo deste atendimento no TCGI.
* **Imóvel:** É o imóvel para o qual este atendimento foi criado.
* **Data de Atendimento:** É a data na qual este atendimento foi criado.
* **Situação do Atendimento:** É a situação na qual este atendimento se encontra. Estas situações são peculiares a cada tipo de atendimento e são parametrizadas no TAA.

#### ⚙️ Ações do Histórico

* **Botão Visualizar Atendimento:** Através deste botão pode-se visualizar os detalhes do atendimento e interagir no mesmo.
* **Botão de Anexos do Atendimento:** Esta opção lista os anexos do atendimento para visualização e conferência.
* **Botão Carregar Mais Resultados:** Esta opção carrega mais atendimentos para exibição na listagem.
