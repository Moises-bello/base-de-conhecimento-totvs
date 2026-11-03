---
content_hash: e96c6cdfd1fad2a4ffa661db184f1e89bfe7f8f625031a97a8412ff95d73ef15
fetched_at: '2026-06-29T00:10:19.086702+00:00'
page_id: '4813062'
product: rm
source: tdn-rm
title: Geração de Boleto Bancário através do RMNucleus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813062
version: 6
---

BLOCK

Geração de Boleto Bancário através do RMNucleus

FAQ: **Geração de Boleto Bancário através do RMNucleus**

Avaliação

* ***Como Fazer***

Como parametrizar o sistema para gerar Boleto Bancário para o Totvs Gestão Financeira?

* ***Definição do Processo***

Tem por finalidade a geração automática de código de barras (boleto) através do Totvs Gestão de Estoque, Compras e Faturamento para o Totvs Gestão Financeira, fazendo com que o lançamento financeiro será gravado com esta informação preenchida.

O sistema considera a última informação gerada no Totvs Gestão Financeira + 1, ou seja, se a última informação gerada no Totvs Gestão Financeira foi “000000XX” será gerado no Totvs Gestão de Estoque, Compras e Faturamento o número “000000XY”. Vale salientar que para gerar boleta bancária através do Totvs Gestão de Estoque, Compras e Faturamento é necessário que exista um remessa de cobrança cadastrada corretamente.

Solução

* ***Parametrizações Necessárias - Totvs Gestão Financeira***

Acessar **| Opções | Parâmetros | RMFluxus | Contas a Receber |** e parametrizar:

**Etapa Cobrança Eletrônica**

- Usar Cobrança Eletrônica: habilitar

Acessar **| Cadastro | Bancos e Agências |** e parametrizar as opções:

Aba **| Banco | Incluir |** e cadastrar as informações do banco.

Selecionar o banco em questão e acessar **| Anexos | Layout Bancário |** onde deverá preencher as informações de retorno de cobrança. O conteúdo de cada campo é obtido junto ao layout de cada banco.

Ainda no cadastro de Banco clicar em **| Anexo | Agência | Incluir |** onde deverá preencher as informações pertinentes ao banco em questão

Acessar **| Cadastro | Conta Corrente |** e informar:

**Identificação – Incluir**: fazer o cadastro da conta corrente pertinente ao banco e agência já cadastrados anteriormente. Neste cadastro devem ser preenchidos dados da aba **| Identificação |** e a seguir **| Dados Adicionais |** que serão considerados para geração do nosso número e consequentemente do boleto.

Importante:

Depois de feita inclusão da conta corrente, deverá acessar novamente **| Cadastro | Bancos e Agências |** e editar o banco em questão. A seguir editar a agência, clicar em **| Anexos | Conta Corrente |** para que as informações sejam vinculadas.

* ***Parametrizações Necessárias - Totvs Gestão de Estoque, Compras e Faturamento***

Acessar | **Cadastro | Tabelas Auxiliares | Tipo de Documento |** e incluir tipo de documento específico para este fim. A seguir acessar aba **| Dados Adicionais | Espécie CNAB |** e preencher código fornecido pelo banco onde a cobrança será efetuada. Esta informação pode ser obtida no manual de cobrança do banco em questão.

Acessar | **Opções | Parâmetros | RMNucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado. A seguir editar o mesmo e informar:

**Etapa Mov Impressão**

- Relatórios | Do Movimento | Ação ao Cadastrar Movimento: Imprime Manual com Edição

- Imprimir Boleto: habilitar

**Etapa Fin – Faturamento**

Fatura o movimento: Habilita

Fatura na Inclusão: Habilita

Tipo de Geração: Edita

Tipo de Documento Gerado: Outros

Tipo de Documento Duplicata: informar local de onde será buscado tipo de documento a ser considerado para este fim. Se escolher a opção “Utiliza do Tipo de Movimento” será apresentado campo **| Tipo de Documento Duplicata Default** | para informar o tipo de documento, caso contrário será consistido código do tipo de documento informado no cadastro do cliente \ fornecedor preenchido no movimento.

Tipo de Documento Duplicada Default: informar o tipo de documento que será utilizado neste tipo de movimento

Numeração do Lançamento: informar se deseja utilizar “número do movimento + sequencial” ou apenas “sequência”

**Conta Caixa**

Edita no Movimento: A informação desta conta caixa será considerada para geração dos dados da boleta bancária.

**Gerar Lançamentos:** A Receber |

* ***Descrição do Processo***

A movimentação será inclusa como de costume, onde o usuário deve acessar aba **| Cabeçalho |** e informar “conta caixa” a ser considerada para geração do código de barras x boleto.

A seguir selecionar o movimento pela visão e clicar no ícone **| Imprimir Documentos |** onde deverá selecionar o layout de relatório a ser utilizado para impressão da nota e do boleto. Assim que o usuário escolher o **| Tipo de Relatório |** e **| Formato do Relatório |** deverá clicar na opção **| Imprimir |** onde será aberta outra tela para escolher agência pertinente geração da boleta e se desejado informar o nosso numero.

Exemplo:

Tipo de Relatório: Movimento Formato de Relatório: X.XXX

[![clip_image002](http://lh6.ggpht.com/_G7KXZLoZDsY/TKssFWpRocI/AAAAAAAABoY/U4x8AHgCPsk/clip_image002_thumb%5B1%5D.jpg?imgmax=800 "clip_image002")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKssEv67qgI/AAAAAAAABoU/X7GCFfq_L_w/s1600-h/clip_image002%5B4%5D.jpg)[![clip_image004](http://lh3.ggpht.com/_G7KXZLoZDsY/TKssIeUKpsI/AAAAAAAABog/_gopz7HCDcY/clip_image004_thumb%5B1%5D.jpg?imgmax=800 "clip_image004")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKssGpqOtXI/AAAAAAAABoc/LDhZvUYRVA4/s1600-h/clip_image004%5B4%5D.jpg)

Depois de gerar o relatório, ao editar o movimento o mesmo será apresentado com a mensagem **| Existem boletos emitidos para os seus lançamentos |** na visão de movimentos. Para visualizar os dados da cobrança deverá acessar o menu **| Faturamento |** editar o lançamento, clicar na aba **| Integração Bancária |**.

Ao editar o lançamento financeiro no Totvs Gestão Financeira os dados de “Integração Bancária” estarão preenchidos podendo ser gerada “Remessa de Cobrança” ou não, ficando a cargo do usuário.

* ***Informações Adicionais***

- Para gerar boleto através do Totvs Gestão de Estoque, Compras e Faturamento é necessário que já tenha sido gerado pelo menos uma remessa bancária para que seja obedecido sequencial

- Os dados para preenchida da aba **| Integração Bancária |** vão considerar as parametrizações feitas anteriormente no Totvs Gestão Financeira

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Rpt/Rpt.Reports.aspx)

**COMUNIDADE **[R@Materiais e Finanças](https://totvs.byyou.com/?space=rmateriais)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015
