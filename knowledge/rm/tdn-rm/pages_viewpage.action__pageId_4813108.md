---
content_hash: 048a5ae5adcd6f63b4053bd63e12eb32f0411264630e3e88b90b8ea7e47527c8
fetched_at: '2026-06-29T00:10:19.183197+00:00'
page_id: '4813108'
product: rm
source: tdn-rm
title: Geração de IRRF_PJ para o Totvs Gestão Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813108
version: 7
---

* ***Como Fazer***

Como parametrizar o sistema para gerar IRRF PJ para o Totvs Gestão Fiscal?

* ***Definição do Processo***

Tem por finalidade gerar lançamento fiscal de IRRF\_PJ para o Totvs Gestão Fiscal e a partir do mesmo gerar DARF para o Totvs Gestão Financeira.

É aconselhável que esta integração seja feita através do aplicativo Totvs Gestão Fiscal para evitar que haja divergência entre os valores calculados no Totvs Gestão de Estoque, Compras e Faturamento com a informação calculada automaticamente pelo aplicativo Totvs Gestão Financeira.

Esta divergência de valores pode ocorrer quando o fornecedor trabalha com o conceito de arredondar valores e o cliente utilizar trunca em suas movimentações ou vice versa. Neste caso, ao gerar escrituração o usuário vai definir a “base de cálculo” a ser considerada para o tributo, mas quando o cálculo é feito internamente pelo Totvs Gestão Financeira não pode haver manutenção de dados.

* ***Parametrizações Necessárias - Totvs Gestão de Estoque, Compras e Faturamento***

Acessar **| Cadastro | Tabelas de Tributação | IRRF |** e cadastrar códigos da receita a serem utilizados, preenchendo os campos.

- Código da Receita: informar código da receita considerando dados fornecidos pela receita federal

- Descrição: informar descrição do código da receita em questão

- Alíquota: informar alíquota pertinente código em questão

- Aplicável em: informar Pessoa Jurídica

Acessar **| Cadastro | Tabelas de Tributação | TRIBUTOS |** e cadastrar tributo **| IRPJ |**, onde deve informar:

- Sigla: IRPJ

- Tipo tributo fiscal: IRRF PJ

- Tipo: Variável

- Incidência: se o tributo deve incidir sobre produto x serviços ou ambos

- Buscar Alíquota: Código da Receita

- Código da Receita: informar código da receita incluso anteriormente(Opcional)

**Acessar | Cadastro | Fórmula | Inserir |** e cadastrar fórmula que será utilizada para compor a base de cálculo do IRPJ. Neste caso específico o tributo será referenciado no “movimento” e a base de cálculo vai considerar o “valor bruto” do movimento.

**Exemplo****: MVB**

Acessar | **Opções | Parâmetros | RMNucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado. A seguir editar o mesmo e informar:

**Etapa Fis Tributação – Movimento**

**Tributo**: IRPJ

**Cód.Retenção**: informar o código da receita que deverá ser apresentado na guia a ser gerada(opcional)

**Fórmula da base de cálculo do tributo**: informar o código da fórmula que retorna o conteúdo desejado.

**Procurar alíquota em**: Tributo

T**ributo Base**: IRPJ

Tipo de Recolhimento: informar o tipo de recolhimento pertinente tributo. Esta informação será apresentada no Totvs Gestão Fiscal no momento da escrituração.

Importante:

- O tipo de movimento não deve estar parametrizado na Etapa – Faturamento para gerar “IRRF Automático” para o Totvs Gestão Financeira para evitar duplicidade de informações.

- O código da receita apresentado na aba **| Tributo | IRPJ |** será apresentado no Totvs Gestão Fiscal e será considerado para geração da DARF para o Totvs Gestão Financeira. A informação deste campo vai obedecer hierarquia a seguir:

**Validação feita quando o tributo estiver informado no “Movimento”.**

1ª Hierarquia: o código da receita será apresentado considerando informação preenchida na parametrização do tipo de movimento na etapa **| Fis – Tributação | Tributo | Código da Receita |**

2ª Hierarquia: o código da receita será apresentado considerando informação preenchida em **| Cadastro | Cliente \ Fornecedor | Dados Fiscais | Dados Relacionados ao IRRF | Código da Receita |**

3ª Hierarquia: o código da receita será preenchido manualmente pelo usuário na aba **| Tributos | IRPJ | Código da Receita |**

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

* ***Escrituração do Movimento de IRRFSPJ***

A escrituração dos movimentos será feita como de costume onde o usuário dever acessar **| Opções | Escrituração de Lançamentos – RMLIBER |** e fazer o filtro da nota fiscal desejada.

Depois de concluído processo de escrituração, ao acessar o RMLIBER em **| Cadastro | Manutenção de Lançamentos |** e editar o lançamento fiscal os dados do tributo serão apresentados na aba **| Outros Tributos | IRPJ |**.

Para geração da DARF deverá fazer os procedimentos a seguir:

- Acessar **| Lançamento | Período de Apuração |** fazer filtro do tributo IRPJ e clicar no ícone |  - Encerra Período Fiscal |

- Editar o Período de Apuração em questão na aba **| Outros Dados |** e preencher o campo **| Data Vencimento |**. A seguir acessar a aba **| Guias |** e clicar no ícone **|  - Inserir GPS Automaticamente |** onde será apresentada opção de digitar o código da receita a ser considerado para geração da DARF ou então clicar em **| TODOS |** para que sejam consideradas todos os códigos de regerar para geração da DARF.

As guias serão apresentadas com o ícone |  | de forma que o usuário deverá marcá-las e clicar no ícone **|  - Gerar Lançamento no RMFluxus |** onde serão apresentadas abas **| Identificação e Outros Dados |** para preenchimento dos dados apresentados no lançamento financeiro. A seguir deverá clicar em | Gerar |.

BLOCK

Geração de IRRF\_PJ para o Totvs Gestão Fiscal

FAQ: **Geração de IRRF\_PJ para o Totvs Gestão Fiscal**

Avaliação

* ***Como Fazer***

Como parametrizar o sistema para gerar IRRF PJ para o Totvs Gestão Fiscal?

* ***Definição do Processo***

Tem por finalidade gerar lançamento fiscal de IRRF\_PJ para o Totvs Gestão Fiscal e a partir do mesmo gerar DARF para o Totvs Gestão Financeira.

É aconselhável que esta integração seja feita através do aplicativo Totvs Gestão Fiscal para evitar que haja divergência entre os valores calculados no Totvs Gestão de Estoque, Compras e Faturamento com a informação calculada automaticamente pelo aplicativo Totvs Gestão Financeira.

Esta divergência de valores pode ocorrer quando o fornecedor trabalha com o conceito de arredondar valores e o cliente utilizar trunca em suas movimentações ou vice versa. Neste caso, ao gerar escrituração o usuário vai definir a “base de cálculo” a ser considerada para o tributo, mas quando o cálculo é feito internamente pelo Totvs Gestão Financeira não pode haver manutenção de dados.

Solução

* ***Parametrizações Necessárias - Totvs Gestão de Estoque, Compras e Faturamento***

Acessar **| Cadastro | Tabelas de Tributação | IRRF |** e cadastrar códigos da receita a serem utilizados, preenchendo os campos.

- Código da Receita: informar código da receita considerando dados fornecidos pela receita federal

- Descrição: informar descrição do código da receita em questão

- Alíquota: informar alíquota pertinente código em questão

- Aplicável em: informar Pessoa Jurídica

Acessar **| Cadastro | Tabelas de Tributação | TRIBUTOS |** e cadastrar tributo **| IRPJ |**, onde deve informar:

- Sigla: IRPJ

- Tipo tributo fiscal: IRRF PJ

- Tipo: Variável

- Incidência: se o tributo deve incidir sobre produto x serviços ou ambos

- Buscar Alíquota: Código da Receita

- Código da Receita: informar código da receita incluso anteriormente(Opcional)

**Acessar | Cadastro | Fórmula | Inserir |** e cadastrar fórmula que será utilizada para compor a base de cálculo do IRPJ. Neste caso específico o tributo será referenciado no “movimento” e a base de cálculo vai considerar o “valor bruto” do movimento.

**Exemplo****: MVB**

Acessar | **Opções | Parâmetros | RMNucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado. A seguir editar o mesmo e informar:

**Etapa Fis Tributação – Movimento**

**Tributo**: IRPJ

**Cód.Retenção**: informar o código da receita que deverá ser apresentado na guia a ser gerada(opcional)

**Fórmula da base de cálculo do tributo**: informar o código da fórmula que retorna o conteúdo desejado.

**Procurar alíquota em**: Tributo

T**ributo Base**: IRPJ

Tipo de Recolhimento: informar o tipo de recolhimento pertinente tributo. Esta informação será apresentada no Totvs Gestão Fiscal no momento da escrituração.

Importante:

- O tipo de movimento não deve estar parametrizado na Etapa – Faturamento para gerar “IRRF Automático” para o Totvs Gestão Financeira para evitar duplicidade de informações.

- O código da receita apresentado na aba **| Tributo | IRPJ |** será apresentado no Totvs Gestão Fiscal e será considerado para geração da DARF para o Totvs Gestão Financeira. A informação deste campo vai obedecer hierarquia a seguir:

**Validação feita quando o tributo estiver informado no “Movimento”.**

1ª Hierarquia: o código da receita será apresentado considerando informação preenchida na parametrização do tipo de movimento na etapa **| Fis – Tributação | Tributo | Código da Receita |**

2ª Hierarquia: o código da receita será apresentado considerando informação preenchida em **| Cadastro | Cliente \ Fornecedor | Dados Fiscais | Dados Relacionados ao IRRF | Código da Receita |**

3ª Hierarquia: o código da receita será preenchido manualmente pelo usuário na aba **| Tributos | IRPJ | Código da Receita |**

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

* ***Escrituração do Movimento de IRRFSPJ***

A escrituração dos movimentos será feita como de costume onde o usuário dever acessar **| Opções | Escrituração de Lançamentos – RMLIBER |** e fazer o filtro da nota fiscal desejada.

Depois de concluído processo de escrituração, ao acessar o RMLIBER em **| Cadastro | Manutenção de Lançamentos |** e editar o lançamento fiscal os dados do tributo serão apresentados na aba **| Outros Tributos | IRPJ |**.

Para geração da DARF deverá fazer os procedimentos a seguir:

- Acessar **| Lançamento | Período de Apuração |** fazer filtro do tributo IRPJ e clicar no ícone | [![clip_image002](http://lh6.ggpht.com/_G7KXZLoZDsY/TKtUVEPy28I/AAAAAAAABqY/44vzLEs1LeA/clip_image002_thumb.jpg?imgmax=800 "clip_image002")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtUUZmM_BI/AAAAAAAABqU/bbzdj1UcKQ4/s1600-h/clip_image002%5B3%5D.jpg) - Encerra Período Fiscal |

- Editar o Período de Apuração em questão na aba **| Outros Dados |** e preencher o campo **| Data Vencimento |**. A seguir acessar a aba **| Guias |** e clicar no ícone **| [![clip_image004](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtUWqmFSHI/AAAAAAAABqg/r78U1Ijjotw/clip_image004_thumb.jpg?imgmax=800 "clip_image004")](http://lh4.ggpht.com/_G7KXZLoZDsY/TKtUV12F1iI/AAAAAAAABqc/eaEPmFmgKVw/s1600-h/clip_image004%5B3%5D.jpg) - Inserir GPS Automaticamente |** onde será apresentada opção de digitar o código da receita a ser considerado para geração da DARF ou então clicar em **| TODOS |** para que sejam consideradas todos os códigos de regerar para geração da DARF.

As guias serão apresentadas com o ícone | [![clip_image006](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtUX7I0EVI/AAAAAAAABqo/_pS9FTqISJg/clip_image006_thumb.jpg?imgmax=800 "clip_image006")](http://lh5.ggpht.com/_G7KXZLoZDsY/TKtUXFYNngI/AAAAAAAABqk/LEPqINH42E8/s1600-h/clip_image006%5B3%5D.jpg) | de forma que o usuário deverá marcá-las e clicar no ícone **| [![clip_image008](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtUZm4tWSI/AAAAAAAABqw/SbmSKcsr5c4/clip_image008_thumb.jpg?imgmax=800 "clip_image008")](http://lh3.ggpht.com/_G7KXZLoZDsY/TKtUYvwhsZI/AAAAAAAABqs/3m3NhfAriIs/s1600-h/clip_image008%5B3%5D.jpg) - Gerar Lançamento no RMFluxus |** onde serão apresentadas abas **| Identificação e Outros Dados |** para preenchimento dos dados apresentados no lançamento financeiro. A seguir deverá clicar em | Gerar |.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Rpt/Rpt.Reports.aspx)

**COMUNIDADE **[R@Materiais e Finanças](https://totvs.byyou.com/?space=rmateriais)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015
