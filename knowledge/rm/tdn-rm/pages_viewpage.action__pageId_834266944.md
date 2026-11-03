---
content_hash: 4975dcf95c397bcd76781a0631be3663140a1fd6426763e16bdc60ba1fecf515
fetched_at: '2026-06-29T00:11:49.490512+00:00'
page_id: '834266944'
product: rm
source: tdn-rm
title: Envio e Consulta dos Eventos (CT-e)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=834266944
version: 2
---

## **Envio**

O processo de envio dos eventos consiste na conversão dos dados informados nos eventos disponíveis em XML e o envio destes à SEFAZ do Contribuinte.  
Atualmente para o Conhecimento de Transporte Eletrônico é possível enviar 3 tipos de eventos através do ERP RM, sendo eles: Cancelamento, Carta de Correção e o Registro de Multimodal.

* Para emitir qualquer um destes eventos, siga os seguintes processos:
* Carregue o RM e selecione o processo Gestão de Compras, Estoque e Faturamento;
* Vá até o menu Vendas e no Menu Faturamento escolha a opção Conhecimento de Transporte Eletrônico (CT-e);
* Crie um filtro a sua escolha ou execute um filtro pré-existente;
* Selecione um CT-e autorizado para associar ao evento que será enviado, acesse o botão Processos e escolha a opção Enviar Evento.

**Cancelamento:** O CT-e poderá ser cancelado dentro do prazo de 24 horas após a sua autorização. É necessário informar um texto informando o motivo deste cancelamento cujo tamanho deverá ter no mínimo 15 caracteres. Ao executar o processo, o TSS irá transmitir o XML para a Sefaz do Emitente com os parâmetros específicos para o Cancelamento. Após a execução o ERP automaticamente irá alterar o status do CT-e para "Evento Pendente".

**Carta de Correção:** A Carta de Correção é um evento que permite corrigir algumas informações que foram geradas incorretamente na autorização do CT-e. Todavia, informações que afetem os cálculos do XML, como valores e tributos não podem ser alterados via carta de correção. Para realizar a emissão, informe o Grupo de Alteração (Grupo da tag que será alterada), Campo (A tag em si que terá o valor afetado) e o Valor Alteração (Informação atual - Corrigida).  
Este é um evento online, ou seja, não gera qualquer relatório para impressão do usuário. Após a autorização, o evento ficará vinculado ao CT-e, sendo possível realizar a consulta através do [Portal da Sefaz](https://www.cte.fazenda.gov.br/portal/consultaRecaptcha.aspx?tipoConsulta=resumo&tipoConteudo=cktLvUUKqh0=).  
Após a execução o ERP automaticamente irá alterar o status do CT-e para "Evento Pendente".

**Registro do Multimodal:** Caso o CT-e esteja em uma operação com mais de 2 meios de transporte, é necessário realizar o Registro do Multimodal. Para realizar a emissão deste evento, é necessário preencher o Registro e o Número do Documento.   
Após a execução o ERP automaticamente irá alterar o status do MDF-e para "Evento Pendente".

## **Consulta**

Após o envio dos eventos, o CT-e ficará com o Status de Evento Pendente, sendo necessário realizar a consulta para validar o retorno da Sefaz. Para realizar a consulta, basta selecionar o CT-e desejado e acessar o menu Processos > Consultar Evento. Caso a Sefaz retorne a autorização destes eventos, o CT-e ficará com o Status de Cancelado para caso o evento tenha sido o cancelamento e autorizado para os outros dois tipos de evento.   
Vale ainda destacar que no caso do cancelamento, o movimento também será cancelado automaticamente caso a Sefaz autorize o evento.
