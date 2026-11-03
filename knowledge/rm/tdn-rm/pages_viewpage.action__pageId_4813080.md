---
content_hash: 7cd5ccc77a1b870b8d132857bf4d4e835f2178ebfaf1c8305ff1e87decccb7f1
fetched_at: '2026-06-29T00:10:19.131568+00:00'
page_id: '4813080'
product: rm
source: tdn-rm
title: Geração de PIS, COFINS e CSLL Automático para o Totvs Gestão Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813080
version: 9
---

BLOCK

Geração de PIS\_COFINS\_CSLL Automático para o Totvs Gestão Financeira

FAQ: **Geração de PIS COFINS CSLL Automático para o Totvs Gestão Financeira**

Avaliação

* ***Como Fazer***

Como parametrizar o sistema para gerar PIS/COFINS/CSLL Automático para o Totvs Gestão Financeira?

* ***Definição do Processo***

Tem por finalidade gerar lançamento automático dos tributos **PIS – COFINS – CSLL** para o Totvs Gestão Financeira obedecendo cumulatividade de 5.000,00 mensal determinada na Lei 10.925. Os tributos em questão têm como fato gerador a “baixa” do lançamento financeiro, ou seja, a emissão de cheque, remessa bancária ou a própria baixa.

Solução

* ***Parametrizações Necessárias - Totvs Gestão Financeira***

Acessar **| Opções | Parâmetros | RMFluxus | Avançar > | Contas a Pagar |** e parametrizar as opções a seguir:

***Etapa Geração de Retenções***

- Origem Defaults das Tabelas | Origem das Tabelas: Lançamento Original

- Fornecedor: informar o código do cli\for a ser apresentado no lançamento financeiro de PIS\COFINS\CSLL

- Tipo de Documento: informar o código que deverá ser apresentado no lançamento financeiro de PIS\COFINS\CSLL

- Histórico do lançamento de tributo gerado: informar um histórico default que será apresentado no financeiro de PIS\COFINS\CSLL (Opcional)

- Usar Cumulatividade de Retenções (Lei 10.925): Habilitar

Importante:

- Os lançamentos serão gerados obedecendo código do fornecedor e tipo de documento parametrizados no Totvs Gestão Financeira

- A cumulatividade do lançamento financeiro vai considerar: emissão de cheque, remessa bancária, baixa do lançamento

- O fato gerador do tributo será a baixa do lançamento financeiro

- O lançamento será gerado apenas para fornecedor da categoria “Pessoa Jurídica”

- Será considerada cumulatividade dos tributos **PIS\COFINS\CSLL** a partir do momento que a parametrização citada for feita, ou seja, os lançamentos já inclusos não serão considerados conforme mensagem apresentada no Totvs Gestão Financeira.

[![clip_image002](http://lh5.ggpht.com/_G7KXZLoZDsY/TKszD-_-EyI/AAAAAAAABpI/svm1P9o_Bmk/clip_image002_thumb%5B1%5D.jpg?imgmax=800 "clip_image002")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKsy-MJ8N7I/AAAAAAAABpE/nPJmkAGbhGM/s1600-h/clip_image002%5B4%5D.jpg)

\*\*mensagem de advertência\*\*

- Ao desabilitar o parâmetro **| Usar Cumulatividade de Retenções (Lei 10.925) |** os dados de retenção dos lançamentos já inclusos serão apagados conforme mensagem apresentada no Totvs Gestão Financeira.

[![clip_image004](http://lh4.ggpht.com/_G7KXZLoZDsY/TKszGBHkGnI/AAAAAAAABpQ/vYroLdqpZjA/clip_image004_thumb%5B1%5D.jpg?imgmax=800 "clip_image004")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKszFmxmsNI/AAAAAAAABpM/FzwAUsB9Srs/s1600-h/clip_image004%5B4%5D.jpg)

\*\*mensagem de advertência\*\*

* ***Parametrizações Necessárias - Totvs Gestão de Estoque, Compras e Faturamento***

Acessar **| Cadastro | Tabelas de Tributação | IRRF |** e cadastrar códigos da receita a serem utilizados, preenchendo os campos.

- Código da Receita: informar código da receita considerando dados fornecidos pela receita federal

- Descrição: informar descrição do código da receita em questão

- Alíquota: informar alíquota pertinente código em questão

- Aplicável em: informar Pessoa Jurídica

Acessar **| Cadastro | Tabelas de Tributação | TRIBUTOS | Incluir |.** O usuário pode fazer o cadastro dos tributos | **PIS-COFINS-CSLL** | individualmente ou cadastrar apenas um tributo considerando alíquota de 4,65%.

**Importante****:**

Serão apresentadas duas formas de cadastro dos tributos, porém a parametrização em questão vai considerar tributo com alíquota de 4,65%.

Cadastro do tributo considerando 4,65%

Sigla: PCC(fica a cargo do usuário)

Tipo tributo fiscal: Contrib. Social RF

Tipo: Fixo

Incidência: se o tributo deve incidir sobre produto x serviços ou ambos

Buscar Alíquota: Tributo

Alíquota: 4,65%

Código da Receita: informar código da receita incluso anteriormente(Opcional)

Cadastro dos tributos individualmente

**Sigla****: PIS**

Tipo tributo fiscal: PIS-RF

Tipo: Fixo

Incidência: se o tributo deve incidir sobre produto x serviços ou ambos

Buscar Alíquota: Tributo

Alíquota: 0,65%

Código da Receita: informar código da receita incluso anteriormente(Opcional)

**Sigla****: COFINS**

Tipo tributo fiscal: COFINS-RF

Tipo: Fixo

Incidência: se o tributo deve incidir sobre produto x serviços ou ambos

Buscar Alíquota: Tributo

Alíquota: 3%

Código da Receita: informar código da receita incluso anteriormente(Opcional)

**Sigla****: CSLL**

Tipo tributo fiscal: CSLL-RF

Tipo: Fixo

Incidência: se o tributo deve incidir sobre produto x serviços ou ambos

Buscar Alíquota: Tributo

Alíquota: 1%

Código da Receita: informar código da receita incluso anteriormente(Opcional)

Acessar **| Cadastro | Fórmula | Incluir |** e cadastrar fórmula que será utilizada para calcular base de cálculo dos tributos em questão. Neste caso específico o tributo será referenciado no movimento e vai utilizar o “valor bruto” na base de cálculo.

Exemplo:

MVB

Acessar | **Opções | Parâmetros | RMNucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado. A seguir editar o mesmo e informar:

**Etapa Fis Tributação – Movimento**

**Tributo**: PCC

**Cód.Retenção**: informar o código da receita que deverá ser apresentado no lançamento

**Fórmula da base de cálculo do tributo**: informar código da fórmula que retorna o conteúdo desejado.

**Procurar alíquota em**: Tributo

T**ributo Base**: PCC

**Etapa Fin – Faturamento**

Fatura o movimento: Habilita

Fatura na Inclusão: Habilita

Tipo de Geração: Edita

Tipo de Documento Gerado: Outros

Tipo de Documento Duplicata: informar local de onde será buscado tipo de documento a ser considerado para este fim. Se escolher a opção “Utiliza do Tipo de Movimento” será apresentado campo **| Tipo de Documento Duplicata Default** | para informar o tipo de documento, caso contrário será consistido código do tipo de documento informado no cadastro do cliente \ fornecedor preenchido no movimento.

Tipo de Documento Duplicada Default: informar o tipo de documento que será utilizado neste tipo de movimento

Numeração do Lançamento: informar se deseja utilizar “número do movimento + sequencial” ou apenas “sequência”

- Informar código da “Fórmula de Valor a Ratear” que determina o valor do lançamento financeiro a ser gerado no Totvs Gestão Financeira. O fato gerador dos tributos retidos na fonte é a baixa, não sendo aconselhável que o valor afete o conteúdo da “Fórmula de Valor a Ratear” para evitar que as retenções dos tributos sejam consideradas em duplicidade no financeiro.

* ***Descrição do Processo***

A inclusão dos movimentos será feita como de costume onde ao acessar a aba **| Tributos |** do movimento serão apresentados dados do tributo PCC(utilizado como exemplo).

A seguir ao clicar duas vezes sobre a opção **| Contas a Pagar |** e editar o lançamento financeiro, serão apresentadas informações do tributo na aba **| Valores | Impostos \ Tributos | Tributos | PCC |**.

A retenção dos tributos será feita no Totvs Gestão Financeira no momento da baixa do lançamento, sendo considerado para termos de cumulatividade: Emissão de Cheque – Remessa Bancária – Baixa. Ao baixar os lançamentos no Totvs Gestão Financeira o valor da retenção será considerado no lançamento apenas quando atingir o valor de 5.000,00 no mês para o fornecedor onde foi inclusa movimentação x lançamento.

Desta forma, será baixado valor bruto do lançamento financeiro até atingir o teto de 5.000,00 no mês, a partir daí o valor dos tributos PIS\_COFINS\_CSLL serão deduzidos das próximas baixas realizadas para o fornecedor, fazendo com que seja gerado lançamento para os mesmos.

* ***Informações Adicionais***

- O Totvs Gestão Financeira gera retenção de PIS\_COFINS\_CSLL apenas para lançamentos a pagar.

- A cumulatividade será feita apenas para movimentações e lançamentos inclusos depois de definida parametrização no Totvs Gestão Financeira.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Rpt/Rpt.Reports.aspx)

**COMUNIDADE **[R@Materiais e Finanças](https://totvs.byyou.com/?space=rmateriais)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015
