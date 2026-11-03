---
content_hash: be5fbd1ee9eb136f66cfa2c9737c4af1cfe6b004a7d84e80b4a1f993e871e9cc
fetched_at: '2026-06-29T00:09:47.660734+00:00'
page_id: '435105038'
product: rm
source: tdn-rm
title: Parâmetro Para Geração de Movimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105038
version: 70
---

**Parâmetro Para Geração de Movimentos**

---

Permite controlar os **[Movimentos](https://tdn.totvs.com/pages/viewpage.action?pageId=423938113)** integrados ao TOTVS Gestão de Estoque, Compras ou Faturamento.

Localizado em : TOTVS Incorporação/ Venda/ Agrupamento de Cadastros/ Básicos/ Parâmetros de Movimento

**Observação**: Esta mesma tela também existe no módulo de alugueis, porém os tipos de geração disponibilizados são diferentes e servem para os processos do módulo de locação. Esta tela é localizada em: TOTVS Incorporação/ Aluguel/ Agrupamento de cadastros/ Cadastros/ Parâmetros de Movimento.

* **Código:** Código Identificador;
* **Tipo de Geração:** Finalidade de utilização do parâmetro. São eles:
  + Movimento de Brinde
  + Movimento de Atendimento
  + Pedido de Venda
  + Movimento de despesas da venda
  + Movimento de Adiantamento
* **Obrigatório:** Identifica se permitirá alterar os dados ao executar o processo de geração do movimento.
* **Descrição:** Descritivo do parâmetro
* **Coligada do Movimento:** Coligada qual pertence o movimento definido no  parâmetro
* **Tipo de Movimento:** Código identificador do tipo de movimento.
* **Produto:** Produto que será incluído no movimento
* **Buscar Filial:** Define se será utilizado do Empreendimento ou do parâmetro. As opções de seleção são:
  + Parâmetro
  + Empreendimento
* **Buscar Local de Estoque:** Define se será utilizado o local de estoque informado no Empreendimento ou o definido neste parâmetro. As opções de seleção são: 
  + Parâmetro
  + Empreendimento (Ao utilizar esta parametrização, a opção abaixo ficará desabilitada, porque o sistema buscará automaticamente o local de estoque dos definido na aba [gestão financeira](https://tdn.totvs.com/pages/viewpage.action?pageId=435105033), desta entidade).
* **Local de Estoque:** Informe o local de estoque para a geração de movimentos. Esta informação não é obrigatória e caso seja parametrizado para buscá-la deste parâmetro, o sistema irá listar para seleção, somente os locais de estoque associados à filial deste parâmetro.

Importante!

\*Para que a informação do campo **Local de Estoque** seja persistida em banco, no cadastro dos Parâmetro Para Geração de Movimentos Vendas, é necessário executar o RM Atualizador com o Patch a partir de 09/08/2024.

* **Filial:** Habilitado para preenchimento se foi selecionada a opção Parâmetro no Buscar Filial
* **Buscar Centro de Custos:** Define se será utilizado do Empreendimento ou do parâmetro. As opções de seleção são:
  + Parâmetro
  + Empreendimento
  + Unidade
  + Não se Aplica
* **Centro de Custos:** Habilitado para preenchimento se foi selecionada a opção Parâmetro no Buscar Centro de Custo

* **Buscar Natureza:** Define se será utilizado do Empreendimento ou do parâmetro. As opções de seleção são:
  + Parâmetro
  + Empreendimento
  + Não se Aplica
* **Natureza Financeira:** Habilitado para preenchimento se foi selecionada a opção Parâmetro no Buscar Natureza

* **Busca Rateio Centro de Custo:** Define se será utilizado do Empreendimento ou do parâmetro. As opções de seleção são:
  + Parâmetro
  + Empreendimento
  + Não se Aplica
* **Centro de Custos:** Habilitado para preenchimento se foi selecionada a opção Parâmetro no Busca Rateio Centro de Custo
* **Buscar Rateio Centro de Custo:** Esta opção permite a definição de onde o sistema buscará o Rateio do Centro de Custa das seguintes opções:
  + **Não se aplica:** Selecione esta opção caso não seja necessário realizar o rateio pelo centro de custo do movimento;
  + **Parâmetro:** Selecione esta opção para informar uma ou mais contas e seus respectivos percentuais de rateio. Ao selecionar esta opção o sistema exibirá um frame logo abaixo com a opção para informar o rateio do centro de custo, conforme demostrado na imagem ao final deste documento;
  + **Empreendimento:** Selecione esta opção para utilizar o rateio já cadastrado na opção *centro de custo*, das *informações de rateio*, da aba **[gestão financeira](https://tdn.totvs.com/pages/viewpage.action?pageId=435105033),** do empreendimento; ou
  + **Subunidade:** Selecione esta opção para utilizar o rateio já cadastrado na opção *rateio centro de custo*, da aba **[identificação](https://tdn.totvs.com/display/LRM/Unidade+-+Anexos+-+Subunidade)**,da subunidade.

* **Histórico:** Define como o histórico será montado. Podem ser utilizados os Mnemônicos para buscar outros dados do sistema para compor o Histórico.
  + Observação: Os Mnemônicos podem ser inseridos clicando com o botão direito dentro do campo de histórico, irá aparecer a lista de mnemônicos que podem ser utilizados, vide abaixo:
    - [BRR] Bairro (Endereço do Empreendimento)
    - [CPL] Complemento (Endereço do Empreendimento)
    - [DSCSUB] Descrição da subunidade
    - [DSCUNI] Descrição da Unidade
    - [LGR] Logradouro (Endereço do Empreendimento)
    - [CLI] Nome do Cliente
    - [NOM] Nome do Empreendimento
    - [NRO] Número (Endereço do Empreendimento)
    - [IM] Inscrição Municipal
    - [END] Endereço
    - [SUB] Número da subunidade
    - [UNI] Número da unidade
    - [VND] Número da venda
    - [CONT] Número do contrato
    - [EMP] Número do empreendimento
    - [TEL] Telefone do Cliente
    - [TLG] Tipo do Logradouro
    - [DIMO] Descrição do Imóvel
    - [DES] Descrição da despesa
