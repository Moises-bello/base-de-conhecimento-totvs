---
content_hash: 4c4bdeac08085d398a4cd7862eb60539dddc551b106229b245b018d22466781b
fetched_at: '2026-06-29T00:10:19.052892+00:00'
page_id: '4813046'
product: rm
source: tdn-rm
title: Compra de Imobilizado
type: documentation
url: https://tdn.totvs.com/display/LRM/Compra+de+Imobilizado
version: 6
---

BLOCK

Compra de Imobilizado

FAQ: **Compra de Imobilizado**

Avaliação

* ***Como Fazer***

Como parametrizar o sistema para fazer integração patrimonial de movimentos de compra de imobilizado?

* ***Definição do Processo***

Tem por finalidade exportar os dados do movimento incluso no Totvs Gestão de Estoque, Compras e Faturamento para o aplicativo Totvs Gestão Patrimonial, evitando assim, que os itens tenham que ser digitados novamente.

Para isto é necessário que o Totvs Gestão de Estoque, Compras e Faturamento tenha sido previamente parametrizado, observando que, toda rotina de integração e informações a serem consideradas serão definidas no Totvs Gestão Patrimonial durante a importação dos dados.

Solução

* ***Parametrizações Necessárias - Totvs Gestão de Estoque, Compras e Faturamento***

Acessar **| Cadastro | Produto |** editar o item a ser referenciado na movimentação e acessar a aba **| Integração |** onde deve informar:

- Grupo de Contas: exigido para utilização no momento da contabilização da depreciação

- Grupo de Bens: determina maior flexibilidade na classificação do código do bem na integração com o Totvs Gestão Patrimonial

Importante:

O grupo de bens pode ser preenchido no cadastro do produto ou buscado da informação preenchida no grupo de contas no momento da integração com o Totvs Gestão Patrimonial.

Acessar **| Cadastro | Fórmula | Inserir |** e cadastrar fórmula a ser utilizada para composição do valor do bem

Exemplo:

KPU

Importante:

- A fórmula em questão só pode ter variáveis de itens pelo fato da informação ser gravada na tabela **| TITMMOV |** e ser considerada na importação dos bens no Totvs Gestão Patrimonial. Antes de definir o conteúdo da fórmula é necessário que seja averiguada forma de integração dos dados no Totvs Gestão Patrimonial, visto que, cada quantidade do item de movimento pode ser considerado como um “bem” ou então a quantidade integral.

**Obs**: No exemplo acima, está sendo considerada cada quantidade do item como sendo um “bem” individualmente.

- O usuário não é obrigado a parametrizar o tipo de movimento para utilizar “Fórmula de Valor do Bem”, mas se escolher esta opção na integração com o Totvs Gestão Patrimonial e a informação não tiver sido gravada na inclusão do item o valor do bem ficará “zerado” e o processo de integração não serão concluído.

- Os dados da fórmula de valor do bem são gravados na tabela **| TITMMOV |** no campo **|** **VALORBEM** **|** na inclusão do item, ou seja, se o parâmetro for habilitado depois de incluir os itens do movimento é necessário que os mesmos sejam “regravados” para atualizar a informação do campo.

Acessar | **Opções | Parâmetros | RMNucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado. A seguir editar o mesmo e informar:

**Etapa Patrimônio**

- Integrar RMBONUM: Compra de Imobilizado

- Localização (Compra Ativo Imobilizado): informar se deseja preencher a localização do bem na inclusão do movimento ou não

- Fórmula Valor do Bem: caso o usuário queira considerar a informação deste campo na integração com o Totvs Gestão Patrimonial deve ser referenciada fórmula que retorne este valor.

Importante:

- Não é obrigatório que o tipo de movimento esteja parametrizado para afetar saldo em estoque.

- Ao habilitar a edição de **| Localização |** será apresentada aba **| Integração |** no item de movimento para que seja preenchida localização do item em questão.

* ***Descrição do Processo***

A movimentação será inclusa como de costume e todo processo de integração será feito no aplicativo Totvs Gestão Patrimonial.

* ***Processo de integração no Totvs Gestão Patrimonial***

Acessar **| Utilitários | Integrações de Sistemas | Integração com o RMNucleus |** onde deve informar:

**Aba – Opções de Seleção**

Fazer o filtro da movimentação a ser inclusa preenchendo os campos | Data – Filial – Número de Nota – Fornecedor – Tipo de Movimento |

**Aba – Opções de Integração**

Cada opção selecionada terá uma funcionalidade no processo de integração do bem, sendo de total responsabilidade do usuário a utilização das mesmas.

- Incluir bem mantendo as quantidades informadas na Nota Fiscal: tem como funcionalidade definir se a quantidade do item incluso no Totvs Gestão de Estoque, Compras e Faturamento será desmembrado no momento da integração ou não. Ao marcar este campo será gravado um bem com a quantidade “integral” informada na nota fiscal, caso contrário a quantidade será desmembrada sendo gerado um cadastro de bem para cada quantidade da nota fiscal.

- Emitir mensagem a cada nota do modo de inclusão de bens: permite que seja feita integração de parte dos bens utilizando a opção acima habilitada e outra parte não. Ao marcar esta opção e fazer integração será apresentada mensagem nota a nota sobre o modo de integração desejado.

- Gerar código do bem e do patrimônio automaticamente: o sistema irá gerar o código de patrimônio e o código do bem automaticamente respeitando sempre o grupo default de bens cadastrado no Grupo de Contas vinculado ao produto, caso contrário é necessário que seja informado código de patrimônio e código de bem para todos os bens que forem integrados.

- Considera a falta do grupo de contas como erro: funciona como uma segurança para realização da integração com o Totvs Gestão Patrimonial sem erros. Ao marcar esta opção será feita validação se os itens da nota fiscal a ser integrada estão com os grupos de contas cadastrados e a ausência desta informação será tratada como “erro”.

- Não integrar bens com valor mínimo exigido por lei (394,13 UFIR’s): ao marcar esta opção o sistema não irá integrar bens com valor inferior ao exigido por lei.

- Gerar o código do bem a partir do grupo de bens definido no produto: ao marcar esta opção o Totvs Gestão Patrimonial vai gravar o bem com o código informado no Totvs Gestão de Estoque, Compras e Faturamento em | Cadastro | Produto | Integração | Patrimonial | Grupo de Bens | desconsiderando assim a informação preenchida no Grupo de Contas Contábeis.

**Aba – Tipo dos Itens**

Cada opção selecionada terá uma funcionalidade no processo de integração do bem, sendo de total responsabilidade do usuário a utilização das mesmas. Deve ser selecionada forma de integração de data, valor e descrição do bem a ser incluso no Totvs Gestão Patrimonial, considerando informações já preenchidas na inclusão do item de movimento e parametrização do tipo de movimento no Totvs Gestão de Estoque, Compras e Faturamento.

- Tipo de Data: informar qual data preenchida no Totvs Gestão de Estoque, Compras e Faturamento será considerada na inclusão do bem no Totvs Gestão Patrimonial.

- Tipo de Valor: informar qual valor preenchido no Totvs Gestão de Estoque, Compras e Faturamento será considerado na inclusão do bem no Totvs Gestão Patrimonial. Cada opção apresentada vai considerar uma informação:

**Preço unitário**: será considerado “preço unitário” preenchido no item de movimento da nota fiscal

**Valor unitário**: será considerado “valor unitário” do item de movimento da nota fiscal. Esta informação é obtida através do conteúdo da fórmula de valor financeiro preenchida no Totvs Gestão de Estoque, Compras e Faturamento no parâmetro do tipo de movimento na etapa | Estoque – Fórmula de Valor Financeiro | \ quantidade do item

**Valor Financeiro**: será considerado “valor financeiro” do item de movimento da nota fiscal. Esta informação é obtida através do conteúdo da fórmula de valor financeiro preenchida no Totvs Gestão de Estoque, Compras e Faturamento no parâmetro do tipo de movimento na etapa | Estoque – Fórmula de Valor Financeiro |

**Formula de Valor do Bem**: será selecionado conteúdo definido na “fórmula de valor do bem” parametrizada no tipo de movimento na aba **| Patrimônio | Fórmula de Valor do Bem |**.

Importante:

Se os campos acima estiverem vazios ou a fórmula não retornar nenhum valor o campo “Valor” ficará vazio.

- Descrição do Bem: informar qual informação preenchida no produto x item do movimento será apresentada no Totvs Gestão Patrimonial na integração do bem. Cada opção apresentada vai considerar uma informação:

**Nome Fantasia**: considera informação preenchida no Totvs Gestão de Estoque, Compras e Faturamento | Cadastro | Produto | Identificação | Nome Fantasia |

**Descrição do Produto**: considera informação preenchida no Totvs Gestão de Estoque, Compras e Faturamento em | Cadastro | Produto | Detalhes | Descrição |

**Histórico do Item**: considera informação preenchida no histórico do item de movimento

**Nome Fantasia do Produto + Histórico do Item**: considera informação preenchida no Totvs Gestão de Estoque, Compras e Faturamento em | Cadastro | Produto | Identificação | Nome Fantasia | mais informação preenchida no histórico do item de movimento

**Descrição do Produto + Histórico do Item**: considera informação preenchida no Totvs Gestão de Estoque, Compras e Faturamento em | Cadastro | Produto | Detalhes | Descrição | mais informação preenchida no histórico do item de movimento

**Aba – Outros Dados**

Nesta aba serão definidos dados de centro de custo, departamento, rateio e tipo de documento a serem inclusos no Totvs Gestão Patrimonial considerando informações já preenchidas na inclusão do item no Totvs Gestão de Estoque, Compras e Faturamento

Depois de feito filtro das informações que deverão ser consideradas no Totvs Gestão de Estoque, Compras e Faturamento e importadas no Totvs Gestão Patrimonial deverá clicar em **| OK |**. Ao executar o processo será gravado histórico no arquivo | LOGBN | dentro do diretório **| CORPORERM\RMBONUM |**.

Para visualizar os bens importados deve acessar **| Cadastro | Bens | Completo |** e fazer filtro do código desejado.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Rpt/Rpt.Reports.aspx)

**COMUNIDADE **[R@Materiais e Finanças](https://totvs.byyou.com/?space=rmateriais)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015
