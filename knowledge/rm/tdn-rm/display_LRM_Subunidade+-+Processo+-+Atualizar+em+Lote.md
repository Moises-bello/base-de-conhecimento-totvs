---
content_hash: ae81c482d31752ee5b9d3a1e4b6c7d66ad31b1181e2ebcbe8fb2b6d38706be89
fetched_at: '2026-06-29T00:09:47.208020+00:00'
page_id: '435104986'
product: rm
source: tdn-rm
title: Subunidade - Processo - Atualizar em Lote
type: documentation
url: https://tdn.totvs.com/display/LRM/Subunidade+-+Processo+-+Atualizar+em+Lote
version: 8
---

Ao executar este processo, poderemos alterar para todas as Subunidades que foram selecionadas na visão.

Ele está acessível através do menu de Processos da visão de Subunidades e ao abrir esta tela, o sistema apresenta 3 etapas que podem ser parametrizadas conforme as informações a serem atualizadas:

Reforçamos que as informações preenchidas neste processo serão atualizadas em comum, para todas as subunidades selecionadas na execução do mesmo.

**Dados Gerais Subunidade:** Nesta etapa são tratados as opções abaixo:

**Gerar subunidade de forma:** defina como será gerada a numeração das subunidades pelo sistema.

Incremental: todas as subunidades serão geradas com uma numeração sequencial;

Incremental por andar: as subunidades serão geradas com a numeração incremental de acordo com o andar ao qual ela pertence

**Quantidade de subunidade:** informe a quantidade de subunidade a serem geradas por este processo;

**Começar de:** informe a numeração inicial da primeira subunidade a ser gerada;

**Quantidade por andar:** informe a quantidade de subunidades por andar;

**Intervalo:** informe o intervalo de geração entre as subunidades;

**Quantidade andares:** informe a quantidade de andares;

**Previsão subunidade:** informe um texto descritivo para as subunidades;

**Situação após geração:** informe a [situação](https://tdn.totvs.com/pages/viewpage.action?pageId=435105411) no qual a subunidade será gerada para os cenários abaixo:

Situação para venda e Situação para aluguel;

**Buscar valores padrão de subunidade:** caso queira copiar os dados de uma subunidade já existente informe-a aqui.

**Informações Gerais** neste agrupador podem ser tratadas as seguintes informações cujas descrições detalhadas podem ser consultados no [cadastro da subunidade](https://tdn.totvs.com/display/LRM/Unidade+-+Anexo+-+Subunidade):

**Peso, Fração Ideal, Valor Avaliado**;

**Dados de Loteamento:** informe os dados abaixo, que forem comuns às subunidades selecionadas neste processo:

Frente (m), Confrontação Frente, Nulo;

Fundo (m), Confrontação Fundo, Nulo:

Lado esquerdo (m), Confrontação Lado esquerdo, Nulo; e

Lado direito (m), Confrontação Lado direito, Nulo;

**Dados de Edificação:** informe os dados abaixo, que forem comuns às subunidades selecionadas neste processo:

Área, Área comum (m2), Área privativa (m2), Área terraço (m2), Área total (m2), Área outros (m2).

**Data de entrega;**

**Data habite-se;**

**Descritivo registro;**

**Condomínio:** caso as subunidades selecionadas façam parte de um condomínio, informe os dados que forem comuns à elas:

Imóvel próprio; Imóvel ocupado, Cliente/Fornecedor proprietário, Modelo de garantia, e Modelo de subunidade.

Os campos "Imóvel próprio" e "Imóvel ocupado" serão inicialmente exibidos no estado indeterminado (caixa toda preenchida), que não altera o valor dos campos nos registros selecionados.

Não será possível alterar em lote os campos "Situação Venda" e "Situação Aluguel" caso a subunidade já esteja associada a uma venda.

**Endereço:** Nesta etapa são tratados as opções abaixo, devendo ser preenchidas as informações que serão comuns às subunidades selecionadas:

**Atualizar endereço Subunidade:**

Não: os campos relativos aos dados do endereço não são habilitados para edição;

Sim, manual: os campos relativos aos dados do endereço são habilitados para edição;

Sim, com o endereço do Empreendimento: os campos relativos aos dados do endereço não são habilitados para edição, uma vez que o sistema utilizará dos dados do endereço do empreendimento.

**Atualizar PIS/COFINS**

Não: as informações não serão atualizadas;

Sim, com o PIS/CONFINS do Empreendimento: os dados do PIS/CONFINS serão atualizados nas subunidades selecionadas no início deste processo, com as informações preenchidas para o empreendimento;

Aplicar fração ideal: o sistema aplicará a fração ideal de cada subunidade selecionada para o PIS/CONFINS.

**Atualizar característica:** informe as [características](https://tdn.totvs.com/pages/viewpage.action?pageId=435104886) que forem comuns às subunidades selecionadas.

**IPTU/Registro:** Nesta etapa são tratados as opções abaixo:

**Atualizar controle de IPTU/Registro:** preencha as informações que forem comuns às subunidades selecionadas. As opções são:

Código cartório, Código prefeitura, Inscrição municipal, Área terreno, Área construída e Valor venal.

**Atualizar dados da Registradora:** preencha as informações que forem comuns às subunidades selecionadas. A descrição detalhada destes campos está disponível na página de cadastro das informações do [CERC para as subunidades](https://tdn.totvs.com/pages/viewpage.action?pageId=736191253). As opções são:

Tipo registradora, Tipo imóvel, Tipo fração ideal, Nro. do Pavimento, Tipo gravame/ônus, Nro. da averbação/ônus e Tipo de classificação.
