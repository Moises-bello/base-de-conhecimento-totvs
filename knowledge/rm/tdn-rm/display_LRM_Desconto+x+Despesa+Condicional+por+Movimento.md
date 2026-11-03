---
content_hash: fb3a6061912c9d24ebcef381aead601908e146bf6617072c051cad1855ee8d2e
fetched_at: '2026-06-29T00:10:19.157957+00:00'
page_id: '4813098'
product: rm
source: tdn-rm
title: Desconto x Despesa Condicional por Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Desconto+x+Despesa+Condicional+por+Movimento
version: 5
---

BLOCK

Desconto x Despesa Condicional por Movimento

FAQ: **Desconto x Despesa Condicional por Movimento**

Avaliação

* ***Como Fazer***

Como parametrizar o sistema para utilizar Desconto x Despesa Condicional no movimento?

* ***Definição do Processo***

Tem por finalidade calcular valores que serão “condicionais” na movimentação e que não podem compor a base de calculo dos tributos, porém tem que ser considerados no valor contábil do lançamento fiscal e no valor líquido do movimento.

Por se tratar de uma informação “condicional” este valor não pode ser preenchido nos campos **| Desconto – Despesa – Frete – Seguro |**, visto que, os mesmos compõem a base de ICMS incondicionalmente.

É sugerido que utilize um campo complementar ou valor extra para preencher o valor condicional, pois os mesmos não são considerados na escrituração.

Solução

* ***Parametrizações Necessárias - Totvs Gestão de Estoque, Compras e Faturamento***

Acessar **| Cadastro | Campos Complementares | Movimento | Novo |** e cadastrar um campo complementar do tipo “Real”

Acessar **| Cadastro | Fórmula | Inserir |** e cadastrar duas fórmulas:

1ª Fórmula:

Fórmula que retorna o conteúdo do campo complementar. Neste caso específico, será considerado campo complementar com a descrição “Desconto Condicional”.

Ex: TABMOVCOMPL ('DESCCONDICIONAL' , 'V')

2ª Fórmula:

Fórmula que será utilizada para composição do “Valor Líquido do Movimento” considerando o desconto condicional.

Ex: MVB - MDT + MDZ + MFR + MSG - TABMOVCOMPL ('DESCCONDICIONAL' , 'V')

Acessar | **Opções | Parâmetros | RMNucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado. A seguir editar o mesmo e informar:

**Etapa Mov – Valores Financeiros**

- Fórmula do Valor Líquido: referenciar código da 2ª Fórmula inclusa

- Desconto Condicional: referenciar código da 1ª Fórmula inclusa

Importante:

O conteúdo da fórmula **| DESCCOND |** pode ser utilizado tanto para cálculo de despesa condicional, quanto para cálculo do desconto condicional do movimento, desde que, o valor seja o mesmo para ambas situações. O que vai definir o efeito sobre a movimentação é o conteúdo da “Fórmula de Valor Líquido” que poderá somar ou subtrair o valor.

**Etapa Mov – Campos Complementares**

- Selecionar o campo complementar “**Desconto Condicional”** apresentado na coluna **| Campos Complementares Disponíveis |** e passar para coluna **| Campos Complementares Visíveis |**

**Etapa Fis – Natureza**

- Edição : Edita

- Seleção Automática da Natureza: definir tipo de seleção da natureza

\*\*Parametrização específica para geração de lançamentos fiscais\*\*

**Etapa Fis – Escrituração**

- Gerar Escrituração: habilitar

- Tipo Documento Escrituração | Código Default |: informar tipo de documento a ser apresentado no lançamento fiscal

- Tipo do Lançamento Fiscal da Transferência: informar o tipo de lançamento que será gerado a partir desta movimentação

\*\*Parametrização específica para geração de lançamentos fiscais\*\*

**Etapa Fis – Tributação**

Incluir e parametrizar os tributos de forma que atenda aos dados a serem apresentados no movimento

\*\*Parametrização específica para geração de lançamentos fiscais\*\*

* ***Parametrizações Necessárias - Totvs Gestão Fiscal***

Acessar o Totvs Gestão Fiscal em **| Cadastro | Selecionar Filial |** e escolher a filial a ser parametrizada para este fim

Acessar **| Cadastro | Natureza de Operação |**, selecionar natureza a ser utilizada na movimentação e clicar na aba **| ICMS/IPI |**. A seguir deverá habilitar **| Valores Condicionais: Desconto |**

* ***Descrição do Processo***

A inclusão dos movimentos será feita como de costume, de forma que o valor liquido do movimento será menor(considerando o desconto) que a base de cálculo do ICMS considerando a informação preenchida na aba **| Campos Complementares | Desconto Condicional |**.

* ***Informações Adicionais***

- O desconto x despesa condicional pode ser utilizado por item ou por movimento, tendo o mesmo funcionamento. Para termos de utilização no item a fórmula e parametrização tem que ser por “item”.

- As informações de desconto e despesa condicional do movimento são gravadas na tabela **| TMOV |** nos campos | VALORDESCCONDICIONAL - VALORDESPCONDICIONAL |. Os campos em questão são visualizados apenas via “banco de dados”

- As informações de desconto e despesa condicional do item são gravadas na tabela **| TITMMOV |** nos campos VALORDESCCONDICONALITM – VALORDESPCONDICIONALITM |. Os campos em questão são visualizados apenas via “banco de dados”

* ***Escrituração do Movimento***

A escrituração dos movimentos será feita como de costume onde o usuário dever acessar **| Opções | Escrituração de Lançamentos – RMLIBER |** e fazer o filtro das movimentações desejadas.

Depois de concluído processo de escrituração, ao acessar o RMLIBER em **| Cadastro | Manutenção de Lançamentos |** e editar o lançamento fiscal, os dados do desconto condicional serão apresentados na aba **| ICMS/IPI | Valor da Mercadoria | Desconto Condicional / Redução do Produto |**. Esta informação vai compor o “Valor Contábil” do lançamento fiscal.
