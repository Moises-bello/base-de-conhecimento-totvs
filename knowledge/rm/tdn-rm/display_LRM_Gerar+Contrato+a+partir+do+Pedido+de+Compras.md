---
content_hash: 10e403b5e687e00b3bc55f81835bdbb222fb1df7710a129f3ebf2801ea5f71ca
fetched_at: '2026-06-29T00:06:11.709171+00:00'
page_id: '203769938'
product: rm
source: tdn-rm
title: Gerar Contrato a partir do Pedido de Compras
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+Contrato+a+partir+do+Pedido+de+Compras
version: 5
---

**Visão Geral**

Esse processo foi elaborado para gerar contrato a partir de um pedido de compra incluído através da cotação ou criado manualmente.

**Principais Campos e Parâmetros**

 Para utilizar o recurso de **Gerar Contrato**é necessário habilitar a permissão **Gerar Contrato**  para o tipo de movimento que irá executar o processo no anexo **Permissão por Tipo de Movimento** do cadastro de Usuários no Módulo de Serviços Globais.

Para atender as condições desse processo o tipo de movimento deve ser parametrizado da seguinte forma:

1. O movimento deve ser do tipo 1.1.XX e estar parametrizado como **Pedido de Compra** na **Etapa 49 -  Compra/Venda – Outros Dados Tipo de movimento de Compra**.
2. O tipo de movimento não poderá afetar estoque (nenhum saldo) na **Etapa 39 - Estoque - Estoque 1/3**
3. Não poderá afetar o orçamento na **Etapa 45 - Orçamento**
4. O parâmetro **Gerar Contrato** deverá ser marcado,**Etapa 51 – Contratos e marcar a opção Gera Contrato.** Esse parâmetro será responsável por habilitar no menu de Processos da visão do movimento o assistente de Geração de Contrato(s).

**Procedimento** 

Na visão do tipo de movimento parametrizado para Gerar Contrato selecione o movimento e execute o Processo Gerar Contrato.  
A tela de Edição do Contrato é apresentada com todos os dados carregados do movimento, para que as informações pertinentes ao Contrato sejam informadas.  
Caso necessário, é possível agrupar os itens por Cliente/Fornecedor marcando a opção Agrupar por Cliente/Fornecedor no Assistente de Geração de Contratos.   
Ao salvar o contrato, o pedido de compras ficará "Recebido".  
Será criado o relacionamento entre o movimento e o contrato gerado através da tabela TITMCNTMOVRELAC. Esse relacionamento permitirá a rastreabilidade do movimento que deu origem ao contrato e vice-versa.   
A visualização desse relacionamento acontece apenas através da tabela não existindo interface para consulta.

***Observações*:**

**Exclusão do Contrato Gerado por Ordem de Compra:** reabertura da ordem de compra após a exclusão do contrato ainda está em estudo pois não existe uma forma de identificar a quantidade a ser retornada para esse movimento, visto que, o contrato pode ter sofrido alterações tais como: movimentos gerados por medição ou periodicidade. Por esse motivo será colocada crítica impedindo que o usuário exclua um contrato gerado por ordem de compra. Esse contrato só poderá ser cancelado.

**Cancelamento do Contrato Gerado por Ordem de Compra:** Ao efetuar o cancelamento de um contrato gerado por ordem de compra não será feita alteração no status do movimento de origem. Isso acontece pois o contrato pode ser “descancelado” e essa característica dificulta o tratamento do movimento de origem.

Informações Adicionais

* [Gerar Contrato a Paritur do Pedido de Compras](http://tdn.totvs.com/display/LRM/DT_Gerar_Contrato_a_Partir_do_Pedido_de_Compras)
