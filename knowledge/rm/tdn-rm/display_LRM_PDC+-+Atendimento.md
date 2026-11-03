---
content_hash: 4099e483c9a1a743d8786cd2c0cc1b643ccd6aad58cff1601da207a4a7f2708d
fetched_at: '2026-06-29T00:11:39.921469+00:00'
page_id: '791203128'
product: rm
source: tdn-rm
title: PDC - Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/PDC+-+Atendimento
version: 3
---

Ao acessar a opção de **Atendimento**, o PDC apresenta ao usuário as ao seguintes informações:

Seleção de Contexto:

* Empreendimento:
* Contrato:

O painel para **Nova Solicitação de Atendimento** está localizado à esquerda da tela:

* **Selecione o Imóvel:** O cliente deve selecionar o Imóvel para o qual ele deseja abrir atendimento. Este campo é obrigatório;
* **Selecione o Tipo de Atendimento:** O Cliente deve selecionar o [tipo de atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=641160309#NovoAtendimento--2120360178) mais adequado à solicitação do atendimento. Este campo é obrigatório;

O painel de **Detalhes do Atendimento** também está localizado à esquerda da tela, logo abaixo do painel acima:

* **Título:** O Cliente deve informar o título/assunto do atendimento. Este campo é opcional, mas é recomendável que ele seja preenchido com um assunto pertinente, para que o mesmo seja localizado facilmente no painel de *histórico do atendimento* detalhado ao final deste documento;
* **Descrição:** Este campo é para que o Cliente possa descrever os detalhes da solicitação criada. Este campo é obrigatório;
* **Envio de Arquivo:** Caso o tipo de atendimento selecionado permita, o Cliente poderá ou será obrigado a enviar arquivos para a o atendimento criado;
  + Botão **Selecionar Arquivos**: Para os tipos de atendimento em que são permitidos o envio de arquivos, este botão será habilitado. É permitido o envido dos arquivos com as extensões abaixo:  
    - Extensões de imagens: **JPG, JPEG, PNG, BMP, GIF**;
    - Extensões de documentos: **TXT, DOC, DOCX, XLS, XLSX, PDF,** **DWG**.

Caso seja anexado algum arquivo por engano, o Cliente pode utilizar o botão para excluir este arquivo que fica localizado logo abaixo, à direita da barra de progresso do envio deste arquivo.

O limite de tamanho do envio de arquivos é definido no parâmetro [*Geral*](https://tdn.totvs.com/pages/viewpage.action?pageId=731881683) do TCGI e nos parâmetro de [*Arquivos Anexos ao Atendimento*](https://tdn.totvs.com/pages/viewpage.action?pageId=425458436) do TAA.

Botão **Limpar**: Este botão permite limpar as informações preenchidas nos campos acima caso o Cliente julgue necessário;

Botão **Salvar**: Este botão salva e envia o atendimento no TCGI. Após acionado, o sistema exibirá o atendimento criado no painel de *histórico de atendimento*, destalhado mais abaixo.

O painel de **Histórico de Atendimento** está localizado à esquerda desta visão:

Agrupador por **Título** do atendimento:

* **Protocolo:** É o protocolo deste atendimento no TCGI;
* **Imóvel:** É o imóvel para o qual este atendimento foi criado;
* **Data de Atendimento:** É a data no qual este atendimento foi criado;
* **Situação do Atendimento:** É a situação na qual este atendimento de encontra. Estas situações são peculiares a cada tipo de atendimento e são parametrizadas no TAA;
* Botão **Visualizar** Atendimento: Através deste botão pode-se visualizar os detalhes do atendimento e interagir no mesmo;
* Botão de **Anexos** do Atendimento: Esta opção lista os anexos do atendimento para visualização e conferência;
* Botão **Carregar Mais Resultados**: Esta opção carrega mais atendimentos para exibição na listagem.
