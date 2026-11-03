---
content_hash: 89c75aa33fb4457af0c36e54b2e7b984e36ae4eeb77f1fdf31b86ea3d61a27a4
fetched_at: '2026-06-29T00:10:19.244756+00:00'
page_id: '4813138'
product: rm
source: tdn-rm
title: Devolução de Vendas de Mercadorias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813138
version: 6
---

BLOCK

Devolução de Vendas de Mercadorias

FAQ: **Devolução de Vendas de Mercadorias**

Avaliação

* ***Como Fazer***

Como parametrizar o sistema para fazer devolução de venda de mercadoria?

* ***Definição do Processo***

A devolução de mercadoria se refere anulação de um procedimento de venda realizado junto á um cliente. A devolução pode ser feita considerando todos os itens do movimento ou parte deles, onde será afetado tanto o saldo financeiro quanto o saldo físico.

A movimentação de devolução é inclusa através do processo de “cópia por referência” onde não é necessário redigitar os dados do item x movimento, visto que, será feito filtro do movimento a ser devolvido(movimento de origem) e será criado relacionamento entre eles.

Movimentos de devolução de venda devem ser inclusos em movimentos do tipo 1.2.XX ou 1.3.XX, visto que, terá o efeito inverso á movimentação de inclusão que foi feita no tipo de movimento 2.2.XX(diminui estoque).

Solução

* ***Parametrizações Necessárias - Totvs Gestão de Estoque, Compras e Faturamento***

Acessar | **Cadastro | Tabelas Auxiliares | Tipo de Documento |** e incluir tipo de documento específico para este fim, onde deverá informar | **Classificação : Devolução |** e **| Pagar ou Receber: A pagar e A receber |**.

Acessar | **Opções | Parâmetros | RMNucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado. A seguir editar tipo de movimento 1.2.XX a ser parametrizado para este fim e informar:

Se tratando de movimento de devolução de venda podem existir duas situações onde a nota fiscal pode ter sido emitida para um cliente que é “pessoa física” e não poderá emitir nota de devolução, ou para o cliente “pessoa jurídica” onde deve ser parametrizado:

Cliente Pessoa Física

**Etapa Mov – Emitente / Destinatário**

- Emitente: Empresa

- Edição da Filial de Emissão: informar “Edita” para permitir que o usuário preencha os dados da filial, ou “Mostra” se quiser deixar um default preenchido

- Edição do Local de Emissão: informar “Edita” para permitir que o usuário preencha os dados da filial, ou “Mostra” se quiser deixar um default preenchido

- Destinatário: Cliente

- Edição do Cliente \ Fornecedor: Edita

Cliente Pessoa Jurídica

**Etapa Mov – Emitente / Destinatário**

- Emitente: Cliente

- Edição da Filial de Emissão: informar “Edita” para permitir que o usuário preencha os dados da filial, ou “Mostra” se quiser deixar um default preenchido

- Edição do Local de Emissão: informar “Edita” para permitir que o usuário preencha os dados da filial, ou “Mostra” se quiser deixar um default preenchido

- Destinatário: Empresa

Importante:

O exemplo em questão vai considerar o cliente “Pessoa Jurídica”.

**Etapa Mov – Datas**

- Data do Movimento Default: informar qual será a data considerada para afetar estoque e apresentação dos dados da ficha física financeira.

Exemplo:

Se for informado “Data Emissão” significa que as movimentações vão afetar estoque de acordo com a data de emissão apresentada na inclusão do movimento.

**Etapa Mov – Outros Dados**

- Usar Cópia de Movimento por Referência: Habilitar

- Motivo de Referência: 5 – Devolução de Venda de Mercadorias

**Etapa Item – Lote/Grade/Num.Série**

- Aceita Número de Série: Habilitado

- Editar Grade Numerada: Habilitado

- Consiste lote : Habilitado |

- Status de Lote Movimentados: marcar os status de lotes que poderão ser utilizados neste tipo de movimento

\*\* A parametrização acima é obrigatória para tipos de movimentos que afetam Saldo2\*\*

**Etapa Estoque**

- Efeito sobre Saldo Físico – Saldo Atual: Aumenta

- Saldo Financeiro - Efeito sobre Saldo Atual: Aumenta

- Buscar Custo no Movimento Relacionado: Habilitar

Importante:

- O saldo Atual está sendo habilitado para aumentar o saldo em estoque porque a movimentação de venda inclusa anteriormente diminui o saldo do produto em estoque

- Por se tratar de uma movimentação de devolução o custo de entrada da mercadoria geralmente é o mesmo da movimentação de saída para que a informação financeira não fique distinta. Para isto deve estar habilitada opção **| Buscar custo no movimento relacionado |** de forma que, o custo do produto no movimento de devolução seja o mesmo custo apresentado na movimentação de venda relacionado á esta devolução. Neste caso, o estoque será afetado considerando **| Quantidade do movimento x Fator de conversão da unidade x Valor do custo buscado no movimento relacionado |**.

**Etapa Fin – Condições de Pagamento**

Edita Condição de Pagamento: Edita

\*\* A parametrização acima é obrigatória para o tipo de movimento que gera financeiro\*\*

**Etapa Fin – Faturamento**

Fatura o movimento: Habilita

Fatura na Inclusão: Habilita

Tipo de Geração: Edita

Tipo de Documento Gerado: Outros

Tipo de Documento Duplicata: informar local de onde será buscado tipo de documento a ser considerado para este fim. Se escolher a opção “Utiliza do Tipo de Movimento” será apresentado campo **| Tipo de Documento Duplicata Default** | para informar o tipo de documento, caso contrário será consistido código do tipo de documento informado no cadastro do cliente \ fornecedor preenchido no movimento.

Tipo de Documento Duplicada Default: informar o tipo de documento que será utilizado neste tipo de movimento.

Numeração do Lançamento: informar se deseja utilizar “número do movimento + sequencial” ou apenas “sequência”

\*\* A parametrização acima é obrigatória para o tipo de movimento que gera financeiro\*\*

**Etapa Fis- Escrituração**

- Gerar Escrituração: Habilitar

- Tipo de Documento Escrituração: informar o tipo de documento que deve ser apresentado no Totvs Gestão Fiscal

- Tipo do Lançamento Fiscal da Transferência: Entrada

\*\* A parametrização acima é obrigatória para o tipo de movimento que vai gerar escrituração\*\*

* ***Parametrizações Necessárias - Totvs Gestão Fiscal***

Acessar **| Utilitários | Selecionar Filial |** e escolher a filial onde a movimentação será inclusa.

Acessar **| Cadastro | Natureza de Operação | Cadastro de Natureza de Operação |** onde deverá incluir duas naturezas compatíveis com os dados das movimentações a serem inclusas.

- Uma Natureza Fiscal de Entrada Transferência de dentro ou fora do Estado (de acordo com a necessidade da operação)

- Uma Natureza Fiscal de Saída Transferência para dentro ou fora do Estado (de acordo com a necessidade da operação)

Depois de incluir as naturezas, deve editar natureza de operação de saída que será utilizada na devolução e acessar a aba **| Outros Dados |** onde deve informar:

- Tipo: Devolução

* ***Descrição do Processo***

O usuário deverá acessar movimento parametrizado para este fim e clicar no menu **| Movimentos | Gerar Mov. por Referência |** onde será aberta tela | [![clip_image002](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtsRsCXZwI/AAAAAAAABww/4BgFrLHG7rk/clip_image002_thumb.jpg?imgmax=800 "clip_image002")](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtsQZepwdI/AAAAAAAABws/3lmYdgchC9c/s1600-h/clip_image002%5B3%5D.jpg) |. Nesta tela o usuário deve clicar em **| Avançar |** e fazer filtro da movimentação que deseja devolver.

Depois de feito filtro deverá marcar o movimento e clicar em **| Avançar |** para visualizar os itens pertinentes ao mesmo. Neste momento o usuário deve marcar os itens que deseja devolver e clicar em **| Avançar |** novamente para concluir o processo de cópia por referência.

A seguir os dados serão apresentados no movimento de devolução podendo ser alterado pelo usuário se necessário. A devolução pode ser feita sobre a quantidade integral do item ou não.

* ***Informações Adicionais***

- Para visualizar o relacionamento entre o movimento de origem e de destino deve acessar o movimento de devolução(destino) e clicar na aba **| Cópia por Referência |** onde vai visualizar todas informações do movimento de origem. Para visualizar os dados de devolução através do movimento de origem, deve selecionar o mesmo e clicar no ícone **| [![clip_image004](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtsTC85SkI/AAAAAAAABw4/D2HdNhaTcaE/clip_image004_thumb.jpg?imgmax=800 "clip_image004")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtsSFMreII/AAAAAAAABw0/SOKuuYYRv0E/s1600-h/clip_image004%5B3%5D.jpg) - Rastreamento de Movimentos |** onde será apresentada aba **| Devolução |** com as informações do movimento de destino.

- O relacionamento entre os movimentos envolvidos ficam gravados na tabela **| TMOVRELAC |** onde o idmov do movimento de origem(venda) é apresentado como **| IDMOVDESTINO |**

* ***Escrituração do Movimento***

O processo de escrituração será feita como de costume onde devem ser inclusos dois lotes com os tipos de movimentos de venda e devolução. Primeiro tem que ser escriturado movimento de Nota Fiscal para depois escriturar a devolução vinculada ao mesmo.

* ***Vínculo do Lançamento de Devolução com Lançamento de Nota Fiscal***

Depois de inclusas movimentações é necessário que vincule o lançamento á pagar com a devolução para que o lançamento seja baixado com o valor correto.

Este vínculo pode ser feito no **Totvs Gestão de Estoque, Compras e Faturamento** onde o usuário deverá selecionar o movimento de venda 2.2.XX e clicar no menu **| Movimentos | Vincular Devolução |** onde será aberta tela | [![clip_image006](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtsUlbvVbI/AAAAAAAABxA/fSWqAwfPnHY/clip_image006_thumb.jpg?imgmax=800 "clip_image006")](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtsTmDwiZI/AAAAAAAABw8/bP67_S-ZeQ4/s1600-h/clip_image006%5B3%5D.jpg) | com os lançamentos de devolução para serem vinculados.

A seguir deverá clicar no ícone | [![clip_image008](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtsWUYWCaI/AAAAAAAABxI/glIammm8JGE/clip_image008_thumb.jpg?imgmax=800 "clip_image008")](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtsVVmBTYI/AAAAAAAABxE/fWNHNgD3NOM/s1600-h/clip_image008%5B3%5D.jpg) | marcar lançamento que será considerado, habilitar opção **| Vincular Lançamentos Financeiros |** e clicar em **| OK |** onde será aberta tela | [![clip_image010](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtsYNcPSBI/AAAAAAAABxQ/mGZo3Jw8qFA/clip_image010_thumb.jpg?imgmax=800 "clip_image010")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtsXaOOp3I/AAAAAAAABxM/6_3J4EN3rjc/s1600-h/clip_image010%5B4%5D.jpg) | para relacionar os movimentos. Na tela em questão deverá marcar o lançamento apresentado em | [![clip_image012](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtsbXSouII/AAAAAAAABxY/XGEZrE_xRhU/clip_image012_thumb.jpg?imgmax=800 "clip_image012")](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtsYlWcURI/AAAAAAAABxU/avx-9iVMXP0/s1600-h/clip_image012%5B4%5D.jpg) | e clicar no ícone | [![clip_image014](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtsd5UoeEI/AAAAAAAABxg/qmpiR1pcSL4/clip_image014_thumb.jpg?imgmax=800 "clip_image014")](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtsdPxW6GI/AAAAAAAABxc/rMBEcEvbB98/s1600-h/clip_image014%5B4%5D.jpg) - Vincula o lançamento selecionado | ou | [![clip_image016](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtsfbXdhaI/AAAAAAAABxo/TAcWy9gQE3M/clip_image016_thumb.jpg?imgmax=800 "clip_image016")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtsekl-oDI/AAAAAAAABxk/wmGaUEM4MyE/s1600-h/clip_image016%5B4%5D.jpg) - Vincular Todos |, de forma que o lançamento passará a ser apresentado em | [![clip_image018](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtshkdWplI/AAAAAAAABxw/BUSdcaQsuSA/clip_image018_thumb.jpg?imgmax=800 "clip_image018")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtsgW-OUbI/AAAAAAAABxs/slMbEqEgFFI/s1600-h/clip_image018%5B4%5D.jpg) | e ao clicar em **| OK |** o vínculo terá sido feito.

Para fazer este processo através do **Totvs Gestão Financeira** deverá selecionar o movimento de compra e acessar o menu | Operações | Vincular | Lançamento á Devolução | onde será aberta tela | [![](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtsjmZILRI/AAAAAAAABx4/_TMumdhoEm0/clip_image010%5B1%5D_thumb.jpg?imgmax=800 "clip_image010[1]")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtsiBwVHRI/AAAAAAAABx0/RjeMSKb2f8U/s1600-h/clip_image010%5B1%5D%5B2%5D.jpg) | para relacionar os movimentos. Na tela em questão deverá marcar o lançamento apresentado em | [![](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtsnWQ18pI/AAAAAAAAByA/RZCWFa4KzAE/clip_image012%5B1%5D_thumb.jpg?imgmax=800 "clip_image012[1]")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtsldcMV_I/AAAAAAAABx8/Z_lt2Jb_mVI/s1600-h/clip_image012%5B1%5D%5B2%5D.jpg) | e clicar no ícone | [![](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtspGxeZVI/AAAAAAAAByI/2PPhJAPbvyI/clip_image014%5B1%5D_thumb.jpg?imgmax=800 "clip_image014[1]")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtsoBEz0OI/AAAAAAAAByE/aEQqCxSyCCM/s1600-h/clip_image014%5B1%5D%5B2%5D.jpg) - Vincula o lançamento selecionado | ou | [![](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtsqiIiLTI/AAAAAAAAByQ/5UP9JkfwWjQ/clip_image016%5B1%5D_thumb.jpg?imgmax=800 "clip_image016[1]")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtsphH7tcI/AAAAAAAAByM/1meLrKNbaug/s1600-h/clip_image016%5B1%5D%5B2%5D.jpg) - Vincular Todos |, de forma que o lançamento passará a ser apresentado em | [![](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtss9Q7onI/AAAAAAAAByY/h8YHgVoWk_Q/clip_image018%5B1%5D_thumb.jpg?imgmax=800 "clip_image018[1]")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtsr9a6u3I/AAAAAAAAByU/tqJCEt9H7-o/s1600-h/clip_image018%5B1%5D%5B2%5D.jpg) | e ao clicar em **| OK |** o vínculo terá sido feito.

Depois de feito vínculo entre o lançamento e a devolução deverá selecionar o lançamento a pagar no Totvs Gestão Financeira e clicar no ícone **| [![clip_image020](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtsurFkOLI/AAAAAAAAByg/U_0SWZujBu4/clip_image020_thumb.jpg?imgmax=800 "clip_image020")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtstog75LI/AAAAAAAAByc/ALJ3iOivwgo/s1600-h/clip_image020%5B3%5D.jpg) - Baixar Lançamento |** de forma que na aba **| Baixa |** será apresentado **| Valor Bruto – Valor Devolução = Valor da Baixa |**.

Se o valor do lançamento a pagar for maior ou igual ao valor do lançamento de devolução “ambos” serão baixados automaticamente. Se o valor do lançamento a pagar for menor que o valor do lançamento de devolução o lançamento de devolução vinculado inicialmente será baixado e apresentada tela | [![clip_image022](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtsv7sKLvI/AAAAAAAAByo/eyPsIRQS8vw/clip_image022_thumb.jpg?imgmax=800 "clip_image022")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtsvEf_1iI/AAAAAAAAByk/Zq_uVOOd9Rg/s1600-h/clip_image022%5B3%5D.jpg) | para informar “Data Venc. Parcela” com o valor pendente de devolução a ser vinculado.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Rpt/Rpt.Reports.aspx)

**COMUNIDADE **[R@Materiais e Finanças](https://totvs.byyou.com/?space=rmateriais)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015
