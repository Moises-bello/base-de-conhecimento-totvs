---
content_hash: 5dbf7a0a28655ce36e28d771f0dbdfbe20919d09a98bb49fbb4edd28fc43bd2f
fetched_at: '2026-06-29T00:10:21.673813+00:00'
page_id: '490994356'
product: rm
source: tdn-rm
title: Auto-Filtro no Lookup
type: documentation
url: https://tdn.totvs.com/display/LRM/Auto-Filtro+no+Lookup
version: 13
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

      O Auto-Filtro no Lookup tem por função, realizar uma busca filtrada no campo para lookup, através do que é descrito pelo usuário nos campos definidos na caixa de pesquisa.

**02. EXEMPLO DE UTILIZAÇÃO**

      No exemplo abaixo será utilizado as tabelas PFUNC e PSECAO.

      Na tela de "Formulário" do metadados foi criado um tipo de controle "Caixa de Pesquisa" para o campo "CHAPA". Em seguida foi selecionado como fonte de dados a action                "FopFuncAction", e no campo de relacionamento foi adicionado os campos "SECAO", "FUNCAO" e "CHAPA".

      No campo descrição da fonte de dados foi selecionado o campo "Chapa" e no Auto-Filtro do Lookup o parâmetro foi deixado como "Ativado".

      Após realizado as configurações necessárias, gere e acesse o projeto.

      Ao criar um registro é possível realizar filtros (tendo um ganho na performance) através dos campos criados na caixa de seleção anteriormente. Vejo no exemplo abaixo que o            filtro foi realizado através do campo "SECAO", buscando somente os funcionários que pertencem a seção "01.02". Ao realizar a pesquisa no campo de lookup (CHAPA) esse              filtro é aplicado corretamente.

      Quando o parâmetro do Auto-Filtro estiver desativado o filtro não é aplicado, todos os registros são tragos na busca. Exemplo abaixo:

false

Metadados utilizado no exemplo deste documento:
