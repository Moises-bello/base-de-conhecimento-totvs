---
content_hash: b2ee81d8c4cd8e086119643e9d56ae10cdc003db84368acb29d20142e059a79a
fetched_at: '2026-06-29T00:10:19.167375+00:00'
page_id: '4813104'
product: rm
source: tdn-rm
title: Geração de INSS_PJ para o Totvs Gestão Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813104
version: 7
---

BLOCK

Geração de INSS\_PJ para o Totvs Gestão Fiscal

FAQ: **Geração de INSS\_PJ para o Totvs Gestão Fiscal**

Avaliação

* ***Como Fazer***

Como parametrizar o sistema para gerar INSS PJ para o Totvs Gestão Fiscal?

* ***Definição do Processo***

Tem por finalidade gerar lançamento fiscal de INSS\_PJ para o Totvs Gestão Fiscal e a partir do mesmo gerar DARF para o Totvs Gestão Financeira.

Este processo tem que ser feito através do Totvs Gestão Fiscal pelo fato do Totvs Gestão Financeira não aceitar lançamento de INSS Pessoa Jurídica.

Solução

* ***Parametrizações Necessárias - Totvs Gestão de Estoque, Compras e Faturamento***

Acessar **| Cadastro | Tabelas de Tributação | IRRF |** e cadastrar códigos da receita a serem utilizados, preenchendo os campos.

- Código da Receita: informar código da receita considerando dados fornecidos pela receita federal

- Descrição: informar descrição do código da receita em questão

- Alíquota: informar alíquota pertinente código em questão

- Aplicável em: informar Pessoa Jurídica

Acessar **| Cadastro | Tabelas de Tributação | TRIBUTOS |** e cadastrar tributo **| INSSPJ |**, onde deve informar:

- Sigla: INSSPJ

- Tipo tributo fiscal: INSS

- Tipo: Variável

- Incidência: se o tributo deve incidir sobre produto x serviços ou ambos

- Buscar Alíquota: Código da Receita

- Código da Receita: informar código da receita incluso anteriormente(Opcional)

**Acessar | Cadastro | Fórmula | Inserir |** e cadastrar fórmula que será utilizada para compor a base de cálculo do INSS/PJ. Neste caso específico o tributo será referenciado no “movimento” e a base de cálculo vai considerar o “valor bruto” do movimento.

**Exemplo: MVB**

Importante:

Se a base de cálculo do tributo INSSPJ tiver que considerar algum percentual de redução, o usuário deverá preencher esta informação em **| Cadastro | Tabelas de Tributação | INSSPJ | Percentual de Redução |** e acrescentar no conteúdo da fórmula de base de cálculo utilizada para este fim.

Acessar | **Opções | Parâmetros | RMNucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado. A seguir editar o mesmo e informar:

**Etapa Fis Tributação – Movimento**

**Tributo**: INSSPJ

**Cód.Retenção**: informar o código da receita que deverá ser apresentado na guia a ser gerada(opcional)

**Fórmula da base de cálculo do tributo**: informar código da fórmula que retorna o conteúdo desejado.

**Procurar alíquota em**: Tributo

T**ributo Base**: INSSPJ

Importante:

- O tipo de movimento não pode estar parametrizado na Etapa – Faturamento para gerar “INSS Automático” para o Totvs Gestão Financeira, visto que, se trata de uma movimentação de “Pessoa Jurídica”.

- O código da receita apresentado na aba **| Tributo | INSSPJ |** será apresentado no Totvs Gestão Fiscal e será considerado para geração da DARF para o Totvs Gestão Financeira. O conteúdo deste campo vai obedecer hierarquia a seguir:

**Validação feita quando o tributo estiver informado no “Movimento”.**

1ª Hierarquia: o código da receita será apresentado considerando informação preenchida na parametrização do tipo de movimento na etapa **| Fis – Tributação | Tributo | Código da Receita |**

2ª Hierarquia: o código da receita será apresentado considerando informação preenchida em **| Cadastro | Cliente \ Fornecedor | Dados Fiscais | Dados Relacionados ao IRRF | Código da Receita |**

3ª Hierarquia: o código da receita será preenchido manualmente pelo usuário na aba **| Tributos | INSSPJ | Código da Receita |**

**Validação feita quando o tributo estiver informado no “Item de Movimento”.**

1ª Hierarquia: o código da receita será apresentado considerando informação preenchida na parametrização do tipo de movimento na etapa **| Fis – Tributação | Tributo | Código da Receita |**

2ª Hierarquia: o código da receita será apresentado considerando informação preenchida em **| Cadastro | Produto | Anexos | Clientes \ Fornecedores |**, onde deverá editar o fornecedor referenciado no movimento e preencher em **| IRRF/INSS | Código da Receita |**

3ª Hierarquia: o código da receita será apresentado considerando informação preenchida em | **Cadastro | Produto | Anexos | Dados Fiscais do Produto | Código da Receita |**

4ª Hierarquia: o código da receita será apresentado considerando informação preenchida em **| Cadastro | Cliente \ Fornecedor | Dados Fiscais | Dados Relacionados ao IRRF | Código da Receita |**

5ª Hierarquia: o código da receita será preenchido manualmente pelo usuário na aba **| Tributos | INSSPJ | Código da Receita |**

**Etapa Fis- Escrituração**

- Gerar Escrituração: Habilitar

- Tipo de Documento Escrituração: informar tipo de documento que deve ser apresentado no Totvs Gestão Fiscal

\*\*Parametrização específica para geração de lançamentos fiscais\*\*

* ***Descrição do Processo***

A inclusão dos movimentos será feita como de costume não havendo necessidade de preencher nenhuma informação específica.

* ***Escrituração do Movimento de INSSPJ***

A escrituração dos movimentos será feita como de costume onde o usuário dever acessar **| Opções | Escrituração de Lançamentos – RMLIBER |** e fazer o filtro da nota fiscal desejada.

Depois de concluído processo de escrituração, ao acessar o RMLIBER em **| Cadastro | Manutenção de Lançamentos |** e editar o lançamento fiscal os dados do tributo serão apresentados na aba **| Outros Tributos | INSSPJ |**.

Para geração da DARF deverá fazer os procedimentos a seguir:

- Acessar **| Lançamento | Período de Apuração |** fazer filtro do tributo INSSPJ e clicar no ícone | [![clip_image002](http://lh4.ggpht.com/_G7KXZLoZDsY/TKs_7VhP7eI/AAAAAAAABp4/sFJsFmTEdYE/clip_image002_thumb.jpg?imgmax=800 "clip_image002")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKs_5cxvDbI/AAAAAAAABp0/jjHMyVEvlaU/s1600-h/clip_image002%5B3%5D.jpg) - Encerra Período Fiscal |

- Editar o Período de Apuração em questão na aba **| Outros Dados |** e preencher o campo **| Data Vencimento |**. A seguir acessar a aba **| Guias |** onde deverá clicar no ícone **| [![clip_image004](http://lh5.ggpht.com/_G7KXZLoZDsY/TKs_88P6NZI/AAAAAAAABqA/4nd2mwHw3FA/clip_image004_thumb.jpg?imgmax=800 "clip_image004")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKs_76b4bYI/AAAAAAAABp8/EMBQK_Dax_8/s1600-h/clip_image004%5B3%5D.jpg) - Inserir GPS Automaticamente |** de forma que serão apresentados lançamentos de INSSPJ inclusos dentro deste período por “Código da Receita” que serão visualizados no Totvs Gestão Fiscal como “Código Pagamento”.

As guias serão apresentadas com o ícone | [![clip_image006](http://lh4.ggpht.com/_G7KXZLoZDsY/TKs_-QrjMPI/AAAAAAAABqI/MTO4OSQwtlA/clip_image006_thumb.jpg?imgmax=800 "clip_image006")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKs_9nq7OiI/AAAAAAAABqE/oCRscwnq4yE/s1600-h/clip_image006%5B3%5D.jpg) | de forma que o usuário deverá marcá-las e clicar no ícone **| [![clip_image008](http://lh3.ggpht.com/_G7KXZLoZDsY/TKs__9NoNJI/AAAAAAAABqQ/U6CWv29HZJc/clip_image008_thumb.jpg?imgmax=800 "clip_image008")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKs__OeE4kI/AAAAAAAABqM/NX9M7UCl6-w/s1600-h/clip_image008%5B3%5D.jpg) - Gerar Lançamento no RMFluxus |** onde serão apresentadas abas **| Identificação e Outros Dados |** para preenchimento dos dados apresentados no lançamento financeiro. A seguir deverá clicar em | Gerar |.

Para maiores informações:

**COMUNIDADE **[R@Materiais e Finanças](https://totvs.byyou.com/?space=rmateriais)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015
