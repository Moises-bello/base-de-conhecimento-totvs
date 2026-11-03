---
content_hash: c12433d0baaf083cfef5db8d889fdab5c976875a7088c7f7bc4b1a6a057bbed1
fetched_at: '2026-06-29T00:11:28.532895+00:00'
page_id: '731900506'
product: rm
source: tdn-rm
title: Novo Atendimento - Gerar Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Novo+Atendimento+-+Gerar+Atendimento
version: 10
---

Ao acessar a aba de Atendimentos, pelo TCGI, é possível de se Gerar um Atendimento através da funcionalidade Gerar Atendimento, localizada no agrupador Atendimento Revitalizado:

Ao acessar essa funcionalidade, o sistema apresenta uma tela para se preencher os parâmetros do Atendimento que será gerado, a saber:

**Tipo de Atendimento:** Informe ou pesquise o Tipo de Atendimento que será gerado. Este campo é obrigatório e ao clicar no lookup de pesquisa, serão exibidos os [Tipos de Atendimentos](https://tdn.totvs.com/display/LRM/Novo+Atendimento+-+Cadastros+-+Tipo+Atendimento+TCGI) disponíveis;

**Cliente:** Informe ou pesquise o Cliente para o qual este Atendimento será gerado. Este campo também é obrigatório;

Após preencher os campos acima, o sistema apresenta as opções de se abrir o Atendimento para os Contratos de Veda ou para os Contratos de Locação/Aluguel. Conforme a escolha realizada, o sistema apresenta os seguintes campos, que podem ou não ser obrigatórios, conforme a parametrização realizada para o *Tipo de Atendimento*:

* **Aba Venda**

**Venda:** Informe ou pesquise o *Contrato de Venda* ao qual o Cliente informado acima está associado. Este campo pode ser obrigatório, em relação ao Tipo de Atendimento selecionado

**Empreendimento:** Informe o *Empreendimento* para o qual este Atendimento será gerado, sendo que ao preencher o campo *Venda*, este campo é preenchido automaticamente. Novamente, reforçamos que este campo pode ser obrigatório, em relação ao Tipo de Atendimento selecionado;

**Unidade:** Informe a Unidade/Bloco/Quadra para o qual este Atendimento será gerado, sendo que ao preencher o campo *Venda*, este campo é preenchido automaticamente. Novamente, reforçamos que este campo pode ser obrigatório, em relação ao Tipo de Atendimento selecionado;

**Subunidade:** Informe a Subunidade/Apartamento/Lote para o qual este Atendimento será gerado, sendo que ao preencher o campo *Venda*, este campo é preenchido automaticamente. Novamente, reforçamos que este campo pode ser obrigatório, em relação ao Tipo de Atendimento selecionado;

**Tipo de Garantia:** Selecione o Tipo de Garantia/[Cobertura de Garantia](https://tdn.totvs.com/display/LRM/02+-+TCGI+-+Atendimento+-+Tipos+de+Coberturas) que está associado às Entidades acima (Contrato de Venda ou Empreendimento ou Unidade ou Subunidade). Este também campo é obrigatório e ao clicar no lookup de pesquisa, serão exibidos as [Coberturas de Garantias disponíveis em relação às Entidades citadas](https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Anexos+-+Atendimento+ao+Cliente+-+Cobertura+de+Garantia);

**Descrição:** Informe a Descrição para este Atendimento procurando descrever o incidente ou a causa do mesmo de forma mais detalhada o possível, porque esta informação será exibida no Histórico do Atendimento.

Novidade!

A partir do Pacth Específico 12.1.2306.186, é possível de se gerar um Atendimento diretamente para uma venda, a partir do menu de Processos da tela de visão e de edição da venda.

Ao realizar a geração a partir do processo da venda, o sistema preencherá automaticamente os campos Cliente, Venda, Empreendimento, Unidade, Subunidade, com os dados do contexto da venda selecionada.

Facilitando e agilizando ao usuário, a execução deste processo.

Cabe ressaltar que não é possível de se executar este processo em lote, devido ao fato da tela deste processo não comportar múltiplas vendas.

* **Aba Aluguel**

**Contrato de Locação:** Informe ou pesquise o *Contrato de Locação* ao qual o Cliente informado acima está associado. Este campo pode ser obrigatório, em relação ao Tipo de Atendimento selecionado

**Imóvel:** Informe a Descrição do Imóvel para o qual este Atendimento será gerado, sendo que ao preencher o campo *Contrato de Locação*, este campo é preenchido automaticamente. Novamente, reforçamos que este campo pode ser obrigatório, em relação ao Tipo de Atendimento selecionado;

**Título:** Informe um título/assunto para o atendimento a ser gerado. Por padrão, o sistema irá preencher este campo com a descrição do Tipo de Atendimento, cabendo ao usuário alterá-lo, se necessário. A informação preenchida neste campo é apresentada na [Visão de Atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=732660488), na coluna Assunto, que é o padrão utilizado pelo [*TOTVS Aprovações e Atendimentos*](https://tdn.totvs.com/pages/viewpage.action?pageId=198948845).

**Descrição:** Informe a Descrição, de preferência com o máximo de detalhes possível para reportar o motivo da abertura do Atendimento. É importante detalhar da melhor forma a demanda, pois essa informação será o texto de abertura do Atendimento. Este campo é obrigatório, pois ele é utilizado para preencher a primeira interação da guia *Solicitação*, do TAA.

O campos abaixo são dinâmicos em relação à parametrização do *Tipo de Atendimento*. Portanto eles podem ser exibidos para o Usuário ou não:

**Preferência de Período para Visitas:** Neste campo são exibidos os Dias da Semana e/ou os Turnos do Dia, para Atendimento, conforme parametrizado para esse Tipo de Atendimento; e

Botão **Selecione os Arquivos:** Este botão permite que sejam anexados arquivos ao Atendimento, conforme parametrização.

Novidade!

A partir do Release 12.1.2306 e superiores que estejam com os Patch Específicos gerados após , a tela desde processo apresenta o campo abaixo:

* **Preencher campos adicionais no TAA:** Com esta esta opção marcada, ao executar este processo o TCGI abrirá o atendimento criado no TAA, para que o usuário preencha as informações que forem pertinentes ao mesmo. Como por exemplo Campos Complementares, Parâmetros do Atendimento, etc..

Este campo é controlado pela opção [*Preencher campos adicionais no TAA*](https://tdn.totvs.com/pages/viewpage.action?pageId=806780183)dos parâmetros de Atendimento do TCGI.

Não é preciso clicar em 'Avançar Etapas' após inserir os dados adicionais, pois o sistema prossegue automaticamente. Basta clicar em 'OK'.
