---
article_id: 4411512839191
category: Escrita Fiscal - Impostos - ISS
content_hash: 46b99925321d9603b8c5441b93f011a9baf2d9c87c5b66c5118e23248d1005e5
fetched_at: '2026-06-28T22:39:35.189412+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Apuração de ISS por
  município
type: support-article
updated_at: '2021-10-26T13:32:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411512839191-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Apura%C3%A7%C3%A3o-de-ISS-por-munic%C3%ADpio
---

**Dúvida**Como configurar apuração de ISS por município  
  
**Ambiente**Protheus - Pedido de Venda - A partir da versão 11.80  
  
**Solução**

Realizada implementação na rotina de **Apuração de ISSQN** **Qualquer Natureza** **(MATA954)**por Município, que possibilita realizar o procedimento de controle de Notas Fiscais de Entrada e seus respectivos Projetos/EDT/Tarefa, para utilização futura de valores no Abatimento de Subempreitadas e Materiais.

Na emissão da Nota Fiscal de Saída é realizada a amarração com as respectivas Notas de Entrada, utilizando os abatimentos disponíveis e posteriormente a Apuração do ISSQN por Município.

Adicionada melhoria permitindo a consolidação de filiais, realizando a apuração de várias filiais no sistema, sem necessitar estar dentro de uma faixa lógica de dados (de/até), protegendo o cliente de gerar equivocadamente informações indevidas, pois bloqueia a seleção de filiais no sistema que não atendam ao critério.

Para atendimento a esta funcionalidade, foi criada a pergunta **“Seleciona Filiais?”**, e para consistir as filiais que pertencem a um mesmo CNPJ + IM, foi criada a pergunta **“Valida seleção por CNPJ+IM?”**. Com essas funcionalidades habilitadas, o sistema permitirá que, com somente uma filial selecionada, a seleção das demais seja feita automaticamente, bastando responder “Adicionar” na tela de consolidação.

#### Importante

* A seleção de filiais estará disponível apenas para as filiais dentro do mesmo grupo de empresas corrente.
* O parâmetro **MV\_CONSCGC**é considerado no processamento desta rotina. Dessa forma, para empresas que forem processar diferentes CNPJ Raíz (oito primeiros dígitos), é necessário verificar se o parâmetro está criado e se o conteúdo lógico é diferente de verdadeiro (.T.) .
* A seleção de filiais com controle de aglutinação por **CNPJ + IM** somente terá funcionalidade para ambientes dbAccess. Neste ambiente, as perguntas **“Considera Filial?”**, **“Filial De?”** e **“Filial Até?”** não tem funcionalidade.
* Quando utilizada a opção de seleção de filiais,  a **janela de seleção de filiais** será ordenada por CNPJ + I.E. + I.M. + Código da Filial.
* Para que o sistema não aglutine as informações é sugerido utilizar a pergunta **“Seleciona Filiais?”** com o conteúdo **“Não”**, sendo considerada somente a filial corrente.
* Para utilizar a aglutinação de informações, o cliente deverá consultar seu departamento jurídico para verificar se o seu ramo de atividade permite tal aglutinação.

## **Procedimentos para Implementação**

Para viabilizar essa melhoria, é necessário aplicar o pacote de atualizações (*Patch*) deste chamado.

## Procedimentos para Configuração

1. No **Configurador (SIGACFG)** acesse **Ambientes/Cadastros/Parâmetros (CFGX017)**. Configure o(s) parâmetro(s) a seguir:

|  |  |
| --- | --- |
| Nome da Variável | MV\_ISSXMUN |
| Tipo | Lógico |
| Conteúdo | .T. |
| Descrição | Tratamento de ISS por Município:  .T. = Habilitado e .F. = Desabilitado. |

|  |  |
| --- | --- |
| Nome da Variável | MV\_TABABAT |
| Tipo | Caracter |
| Conteúdo | SD3 |
| Descrição | Tabela de buscas das informações dos Abatimentos, SD1 – Itens das NF de Entrada de Entrada e SD3 - Movimentações Internas. |

|  |  |
| --- | --- |
| Nome da Variável | MV\_DESCISS |
| Tipo | Lógico |
| Conteúdo | .F. |
| Descrição | Informa ao sistema se o ISS devera ser descontado do valor do titulo financeiro caso o cliente for responsável pelo recolhimento. |

|  |  |
| --- | --- |
| Nome da Variável | MV\_TPABISS |
| Tipo | Caracter |
| Conteúdo | 2 |
| Descrição | Se parâmetro igual a 1 indica se será efetuado um desconto na duplicata quando o cliente recolhe ISS se igual a 2 será gerado um titulo de abatimento. |

| Nome da Variável | MV\_ISSAJU |
| --- | --- |
| Tipo | Caracter |
| Conteúdo | Em branco |
| Descrição | Informar os códigos de Municípios que serão utilizados no quadro dos Ajustes decorrente ao ISQN retido na fonte. |
| Exemplo | 5300108 |

|  |  |
| --- | --- |
| Nome da Variável | MV\_DEDISS |
| Tipo | Caracter |
| Conteúdo | 1 |
| Descrição | Define o momento do tratamento da dedução do ISS (Na baixa ou emissão do título).  1= Na baixa ; 2= Na emissão. |

|  |  |
| --- | --- |
| Nome da Variável | MV\_1DUPREF |
| Tipo | Caracter |
| Conteúdo | Em branco |
| Descrição | Campo ou dado a ser gravado no prefixo do titulo. Quando o mesmo for gerado automaticamente pelo modulo de faturamento. |
| Exemplo | SF2->F2\_SERIE |

|  |  |
| --- | --- |
| Nome da Variável | MV\_ISS |
| Tipo | Caracter |
| Conteúdo | "ISS" |
| Descrição | Natureza utilizada para Imposto s/Serviço |

#### Importante

O parâmetro **MV\_TABABAT** define em qual tabela de **Itens Notas Fiscais de Entrada (SD1)** ou **Movimentações Internas****(SD3)** será utilizada para iniciar as buscas de Notas Fiscais de Entradas.

|  |  |
| --- | --- |
| Nome da Variável | MV\_MUNIC |
| Tipo | Caracter |
| Conteúdo | "MUNIC" |
| Descrição | Fornecedor padrão para geração dos títulos de ISS do próprio município. |

 

Importante

Normalmente o fornecedor cadastrado neste parâmetro é a prefeitura do município.

|  |  |
| --- | --- |
| Nome da Variável | MV\_FPADISS |
| Tipo | Caracter |
| Conteúdo | MUNIC;00 |
| Descrição | Fornecedor padrão a ser considerado na pasta “Por Município - Saídas” caso o município para o qual o ISS é devido não possa ser identificado pela tabela CE1. |

 

Este parâmetro possui duas opções de preenchimento:

* **Informar Apenas o Código do Fornecedor**  
    
    
  ***Exemplo: PREFEITURA***  
  Caso o parâmetro seja preenchido desta forma, o campo **A2\_LOJA** no cadastro do fornecedor informado deverá ser, obrigatoriamente, preenchido com "00" (dois dígitos), independentemente do tamanho do campo LOJA utilizado. Ou seja, mesmo se o tamanho do campo loja for diferente de 2, a loja deste fornecedor deverá ser "00".

* **Informar Código e Loja do Fornecedor**  
    
    
  ***Exemplo: PREFEITURA;01***  
    
  Caso o parâmetro seja preenchido desta forma, é obrigatório que o código e a loja sejam separados por **";" (ponto e vírgula)** conforme o exemplo acima. Desta forma é possível utilizar qualquer loja, independentemente do tamanho do campo, desde que seja informada corretamente. **Obs:**Não é necessária nenhuma outra configuração para habilitar a utilização do separador. A simples utilização do caracter ";" no parâmetro já indicará que não deverá ser utilizada a loja padrão.

| Em ambos os casos o fornecedor informado neste parâmetro deve estar previamente cadastrado na tabela SA2 e ter seus campos de UF (**A2\_EST**) e município (**A2\_COD\_MUN**) preenchidos corretamente do município que será utilizado para apuração do ISS "o mesmo da sua filial da empresa cadastrada no cadastro de filial". |
| --- |

**Itens Notas Fiscais de Entrada (SD1)**

O Sistema considera que todas as notas de entrada movimentadas na data **De** e **Até** da Medição do Serviço foram empregadas e compõem o valor do faturamento.

**Movimentações Internas (SD3)**

É necessário a implementação do controle de Estoque, todos os Produtos e Serviços adquiridos deveram movimentar Estoque, e controle de Lotes.

#### Importante

A implementação de Lotes deve ser realizada através de Lotes Automáticos, não ficando a cargo do Usuário o preenchimento do mesmo.

**Integração Gestão de Projetos (SIGAPMS)**

Com a integração da **Gestão de Projetos (SIGAPMS)** habilitada é necessário efetuar a Amarração Nota Fiscal de Entrada x Projeto x Quantidade que pode ser realizada em dois momentos no Protheus®:

1. **Nota Fiscal de Entrada:** Identificando o Projeto/Tarefa que o Insumo/Serviço foi apropriado. Este procedimento pode ser realizado com o Parâmetro **MV\_TABABAT** = SD1 ou SD3.
2. **Requisição ao Estoque:** Se no momento da geração da Nota Fiscal de Entrada os itens não foram apropriados, uma Requisição (Movimentos Internos) pode ser realizada e neste momento deve-se amarrar o Produto, Quantidade, Lote, Projeto e Tarefa. Este procedimento pode ser realizado com o Parâmetro **MV\_TABABAT** = SD3.

#### Importante

As informações que são importadas do **Gestão de Projetos (SIGAPMS)** para o **Faturamento (SIGAFAT)** são as contidas nos campos: **Código do Projeto (C6\_PROJPMS),** **Código da EDT (C6\_EDTPMS)**e **Código da Tarefa (C6\_TASKPMS)**.

**Integração com TOTVS Obras e Projetos (TOP)**

Se a Integração com o **TOTVS Obras e Projetos (TOP)**estiver habilitada, os Pedidos de Venda serão gerados automaticamente no módulo de **Faturamento (SIGAFAT)** do Protheus®, Solicitação de Compra e Requisições ao Estoque. Para mais detalhes, consulte **Integração PROTHEUS x RM SOLUM** no [TDN - TOTVS Developer Network](https://tdn.totvs.com/display/home/TDN+-+TOTVS+Developer+Network)a partir da versão 11.50.

1. No **Configurador (SIGACFG)** acesse **Ambientes/Cadastro/Menu (CFGX013)**. Informe a nova opção de menu do **Livros Fiscais (SIGAFIS)** conforme instruções a seguir:

| Menu | Atualizações |
| --- | --- |
| Submenu | Cadastros |
| Nome da Rotina | Alíquotas do ISS |
| Programa | FISA052 |
| Módulo | 09 |
| Tipo | 01 |
| Tabelas | CE1 |

| Menu | Atualizações |
| --- | --- |
| Submenu | Cadastros |
| Nome da Rotina | Entradas x Saídas |
| Programa | FISA053 |
| Módulo | 09 |
| Tipo | 01 |
| Tabelas | CE2 |

## Procedimentos para Utilização

**Cadastro de Municípios:**

1. No **Livros Fiscais (SIGAFIS)** acesse **Atualizações/Cadastros/Municípios (FISA010)**. Todos os Municípios são carregados automaticamente de acordo com tabela do IBGE.
2. Foram inseridos quatro novos campos para o controle do ISSQN. Neste cadastro são informadas as características de arrecadação do Município (Se aceita deduções e se o Tomador de Serviços está obrigado a realizar dedução Fixa). Seguem abaixo:
3. **Ded. Mat (CC2\_MDEDMA)** – Se o Município aceita Dedução de Material Empregado;
4. **Ded. Ser (CC2\_MDEDSR)** – Se o Município aceita Dedução de Sub-Empreitadas;
5. **% D. Material (CC2\_PERMAT)** – Para o caso de Dedução Fixa informe o percentual de Dedução estabelecido para Material;
6. **%D. Serviços (CC2\_PERSER)** – Para o caso de Dedução Fixa informe o percentual de Dedução estabelecido para Serviços;
7. **Dia Rec ISS (CC2\_DTRECO)** – Informe o dia de recolhimento do ISSQN para ser utilizada no Título gerado no Financeiro.

**Cadastro de Alíquotas do ISS:**

1. No **Livros Fiscais (SIGAFIS)** acesse **Atualizações/Cadastros/Alíquotas do ISS (FISA052)** e selecione a opção **Incluir**.
2. Este cadastro informa as particularidades de cada Município referentes ao ISSQN. A tabela **Alíquotas do ISS (CE1)** foi dividida em cabeçalho e Itens para facilitar a digitação de todos os Produtos relacionados ao Município;
3. Para o cadastro de Cabeçalho informe os campos (1 para 1):
4. **UF Município (CE1\_ESTISS)** – Com o Estado que o Município pertence;
5. **Cod. Mun. (CE1\_CMUNISS)** – Com o Código de Município IBGE;
6. **Município (CE1\_MUNISS)** – Descrição do Município;
7. **Mun. Retem? (CE1\_RETISS)** – Com a informação se o Município Retem o ISSQN;
8. **Retenção (CE1\_RMUISS)** – Com a informação se o Município Retem o ISSQN **1 – Dentro**, **2 – Fora** e **3 – Ambos**;
9. **Forne. ISS (CE1\_FORISS)** – Com o Fornecedor do ISS que será utilizado na geração do Título a Pagar e no Pedido de Vendas;
10. **Loja (CE1\_LOJISS)** – Com a Loja do Fornecedor.
    1. Para o cadastro de Itens informe os campos (1 para vários):
    2. **Cod. Serviço (CE1\_CODISS)** – Com o Código de Serviço do ISSQN;
    3. **Alíq. do ISS (CE1\_ALIQISS)** – Com a Alíquota do ISSQN;
    4. **C. Ser. Toma (CE1\_CTOISS)** – Com o Código de Serviço do Tomador de Serviço;
    5. **C. Ser. Pres (CE1\_CPRISS)** –  Com o Código de Serviço do Prestador de Serviço;
    6. **Cod. Produto (CE1\_PROISS)** – Com o Código do Produto;
    7. **Des. Produto (CE1\_DESPRO)** – Descrição do Produto.

#### Importante

Para o preenchimento do Fornecedor de ISS, é imprescindível que as informações deste fornecedor (normalmente a prefeitura a que será devido o ISS) estejam devidamente preenchidas no cadastro de Fornecedores (**SA2**), com atenção aos campos **A2\_COD\_MUN** e **A2\_MUN**, que serão utilizados no detalhamento da Apuração de ISS.

**Notas Fiscais de Entrada:**

1. No **Compras (SIGACOM)** acesse **Atualizações/Movimentos/Documento de Entrada (MATA103)**.
2. Posicione o cursor em um produto e clique em **Incluir**.
3. Incluir nota Fiscal de Entrada, informando os campos **Produto (D1\_COD)**, **Tipo Entrada (D1\_TES)** e outros campos acompanhando o *Status* da entrada na pasta **Apuração ISS/INSS (MATA103),**os cadastros de **Municípios do IBGE (CC2)** e **Alíquotas do ISS (CE1)** impactam na geração destas informações.
4. Para informar abatimentos preencha os campos **Abatim. ISS (D1\_ABATISS)** e **Abat. Mat. (D1\_ABATMAT),**no caso de Dedução Fixa os valores serão calculados automaticamente de acordo com a tabela de **Municípios do IBGE (CC2)**.
5. Confira os dados e confirme.

#### Importante

Se houver integração com o módulo de **Gestão de Projetos (SIGAPMS)** informe o Projeto, Tarefa e Quantidade através do botão **Gerenciamento de Projetos**.

Para preenchimento dos campos referente ao INSS Apurado no folder Apuração ISS/INSS na linha de INSS Apuração, referente aos campos Recolhido e Serviços, devem ser preenchidos os campos **Valor Abatimento / INSS (D1\_ABATINS)** e **Abat. INSS (D1\_AVLINSS)**Subcontratada.

**Pedido de Venda:**

1. No **Faturamento (SIGAFAT)** acesse **Atualizações/Pedidos/Pedidos de Venda (MATA410)**.
2. Posicione o cursor em um produto e clique em **Incluir**.
3. Digite **Pedido de Venda**, com atenção aos seguintes campos:
4. **Forn. ISS (C5\_FORNISS)** – Com o código do Fornecedor do ISS (Prefeitura);
5. **Mun. Prest. (C5\_MUNPRES)** – Com o código do Município de Prestação do Serviço\*;
6. **UF Prestação (C5\_ESTPRES)** – Com a sigla da Unidade Federativa;
7. **Cod. Projeto (C6\_PROJPMS) –**Com o código do Projeto\*\*;
8. **Cod. EDT (C6\_EDTPMS) –**Com a EDT do Projeto\*\*;
9. **Cod. Tarefa (C6\_TASKPMS) –**Com o código da Tarefa do Projeto\*\*.

#### Importante

Caso Exista integração com o Sistema **TOTVS Obras e Projetos (TOP)**, o campo  será preenchido através da geração automática do Pedido de Venda, vindo da Medição de Serviços.

Caso Exista integração com o módulo de **Gestão de Projetos (SIGAPMS)**.

1. Para amarração das Notas Fiscais de Entrada clique em  **Abat. ISS,**informando a **Data De** e **Data Até** para seleção das Notas Fiscais de Entrada.

#### Importante

O parâmetro **MV\_TABABAT** define em qual tabela de **Itens Notas Fiscais de Entrada (SD1)** **ou Movimentações Internas (SD3)** será utilizada para iniciar as buscas de Notas Fiscais de Entradas.

Para utilizar a tabela **Movimentações Internas****(SD3)** é necessário à implementação do controle de Lotes e será necessário no momento da Requisição, informar o Documento de Entrada que originou a Requisição, com a integração da  **Gestão de Projetos (SIGAPMS)** habilitada. Esta configuração é efetuada no momento de geração da nota fiscal de Entrada. A amarração de Projeto e Tarefas é necessária para identificar as Entradas de cada Projeto e Tarefa.

Para a definição do Município e Estado do Pedido de Venda, através dos campos **Exe. Serviço (B1\_MEPLES)** que é definido nos itens do Pedido de Venda, para o correto funcionamento será considerado a configuração do Produto do primeiro item do Pedido de Venda.

Se a nota fiscal de saída que teve amarração com notas fiscais de entrada for excluída, o vínculo será desfeito após alteração do Pedido de Vendas, clicando no botão **Abat.ISS** e desmarcando as notas selecionadas. Desta forma serão deletadas as informações da tabela Entradas x Saídas (CE2).

**Recolhimento de ISS e Natureza**

Verificar quem é o responsável pelo recolhimento do ISS. Caso seja o cliente **A1\_RECISS**ou não, informar a Natureza no Cliente ou Fornecedor **A1\_NATUREZ** e/ou **A2\_NATUREZ** preenchendo o campo **ED\_CALCISS.**A TES - Tipos de Entradas e Saídas devem conter o campo **F4\_DUPLIC = SIM**para gerar o titulo a Pagar ou a Receber.

**Apuração do ISS**

1. No módulo **Livros Fiscais (SIGAFIS)** acesse **Miscelânea/Apurações/ISS (MATA954)**.
2. Observe o preenchimento dos parâmetros conforme instruções a seguir:

**Mês De Apuração?**

Informe o mês de referência para a apuração do imposto.

**Ano da Apuração?**

Informe o ano de referência para a apuração do imposto.

**Livro Selecionado?**

Informe o número do livro a ser utilizado na apuração, ou informe ‘\*’ (asterisco) para considerar todos.

**Apuração?**

Informe o tipo de apuração desejado, podendo ser: **Decendial, Quinzenal, Mensal, Semestral e Anual.**

**Período?**

Informe o período de apuração desejado, podendo ser: **Primeiro, Segundo e Terceiro.**

**Arq. Período Anterior?**

Informe o nome do arquivo com a apuração de ISS do período anterior relativo a esta rotina de apuração.

**Moeda do Título?**

Informe o código relativo ao tipo de moeda do sistema.

**Gera Título?**

Informe se deseja gerar título de imposto nesta rotina.

**Exibe lançamento contábil?**

Escolha Sim para gerar os lançamentos contábeis, caso contrário escolha Não.

**Considera Filiais?**

Informe se deseja considerar as filiais que serão aglutinadas ou se considera somente a filial logada.

Este parâmetro está *DESABILITADO* para uso em ambientes dbAcess.

Para ambiente xBase, escolha SIM para que o sistema considere as filiais De/Até nos parâmetros abaixo.

**Da Filial?**

Escolha o código da filial de Início para a geração do arquivo.

*Este parâmetro está DESABILITADO para  uso em ambiente dbAccess.*

**Até Filial?**

Escolha o código da filial de término  para a geração do arquivo.

*Este parâmetro está DESABILITADO para  uso em ambiente dbAccess.*

**Gera Guia de Recolhimento?**

Escolha Sim para gerar a guia de recolhimento, caso contrário escolha a opção Não.

**Utiliza Tabela Progressiva?**

Escolha **Sim** para utilizar a tabela progressiva, caso contrário escolha a opção **Não**.

**Seleciona Filiais?**

Determina se apresenta uma tela posterior a confirmação de execução da rotina, para que seja possível selecionar algumas filiais para processamento ou filiais que componham um grupo que não obedeça à ordem sequencial, e por isso não podem ser indicadas num intervalo **de/até**, como, por exemplo, gerar o arquivo das filiais 01, 05, 10 e 13. As filiais aqui selecionadas serão calculadas e agrupadas por CNPJ + Inscrição Municipal, e somente será permitido selecionar filiais que componham esse critério.

**Valida seleção por CNPJ + I.M.?**

Este parâmetro permite utilizar a rotina bloqueando as seleções de CNPJ completo + Inscrição Municipal caso alguma filial já tenha sido selecionada, evitando assim gerar informações indevidas neste processo. Com o parâmetro ativado é possível selecionar uma única filial e solicitar ao sistema que aglutine as demais, que atendam ao critério de CNPJ + I.M.

**Pasta Por Municípios – Saídas**

Nesta pasta é possível verificar os valores apurados para cada município onde ocorreram prestações. É importante observar que, caso os campos **município** e **descrição**sejam apresentados **em branco,**significa que o sistema não foi capaz de identificar o município para o qual aquele valor de ISS é devido.

Nestes casos, existem dois procedimentos a seguir:

a.)     Verificar o preenchimento da tabela CE1 e os fornecedores informados no campo **CE1\_FORISS**. A apuração é feita com base nos campos de UF e município cadastrados nestes fornecedores. É importante que os cadastros sejam efetuados de forma coerente para que a apuração seja realizada corretamente.

b.)     Verificar o preenchimento do parâmetro **MV\_FPADISS**.

**Importante:**

Na aba " "Por Município - Saída", na apuração do ISS, será gerada da seguinte forma:

1 - Caso o campo C5\_FORNISS esteja preenchido no pedido de venda, esse fornecedor será utilizado na geração do titulo de ISS no contas a pagar e as informações do Código  e descrição do Município, informados neste fornecedor, serão levados para a aba "Por Município - Saída".

2 - Caso o campo C5\_FORNISS não seja preenchido, o sistema irá considerar o código do fornecedor cadastrado no parâmetro MV\_MUNIC para a geração do titulo no contas a pagar e as informações do Código  e descrição do Município, informados neste fornecedor, serão levados para a aba "Por Município - Saída".

3 - Caso não seja gerado titulo para o pedido de venda em questão (Gera Duplicata = Não), o sistema verificará o Fornecedor informado no campo C5\_FORNISS para o preenchimento da aba "Por Município - Saída".

Caso o campo C5\_FORNISS não seja preenchido, o sistema irá considerar o código do fornecedor informado no parâmetro MV\_FPADISS

#### Importante

Caso a apuração seja confirmada com valores não classificados em nenhum município, **não serão gerados títulos e/ou guias de recolhimento daquele valor** devido ao fato de não ser possível obter um fornecedor para os títulos. Ao confirmar a apuração é exibida uma mensagem na tela informando sobre esta restrição. Os demais títulos e guias de recolhimento serão gerados normalmente.

**Parâmetro MV\_MUNIC**

Este parâmetro será considerado caso **não tenha havido nenhuma prestação dentro do município** e, mesmo assim, houver valores a recolher provenientes de outras fontes. Caso contrário, o título será gerado seguindo a mesma lógica dos demais, ou seja, para o fornecedor definido na tabela CE1.

1. Dê um duplo clique na linha desejada. É possível ver o detalhamento das notas de Entrada associadas.
2. Na pasta **Informações Complementares**, digite as informações referentes à Compensação de ISS. Essas informações serão utilizadas na geração no Registro B465 do Ato Cotepe 35.
3. Confira os dados e **confirme**.

**Entradas e Saídas**

1. No **Livros Fiscais (SIGAFIS)** acesse **Atualizações/Cadastros/Entradas x Saídas (FISA053)**.
2. É possível visualizar todas as amarrações realizadas no **Pedido de Venda (MATA410)**, detalhando as Notas de Entrada que foram utilizadas como abatimentos na geração do ISSQN.
3. Filtrando as informações (Ex.: Por Pedido de Venda) o usuário poderá imprimir relatório dos itens selecionados.

**Retenção de ISS por Município**

Tratando-se de local de retenção, os serviços podem ser classificados de duas maneiras: **EP** (Município do Estabelecimento do Prestador) ou **LES** (Município de Execução do Serviço). Esta configuração é feita no campo B1\_MEPLES. O sistema, então, passará a considerar a(s) regra(s) definida(s) no **Cadastro de Alíquotas do ISS (detalhado na seção de mesmo nome neste documento)**para efetuar os cálculos.

#### Importante

O parâmetro MV\_ISSXMUN deve ser configurado como **(.T.)** para habilitar este controle.

**Notas Fiscais de Entrada**

**Regra de Produto LES – ISSQN devido no local da execução do serviço.**

Para o Produto **LES** (B1\_MEPLES = 2) o usuário deverá informar o estado e código do município de prestação de serviço (SF1->F1\_ESTPRES+SF1->F1\_INCISS) no momento da digitação da NF para encontrar a regra da alíquota do ISS (CE1).

A retenção do ISS considera a configuração dos campos CE1\_RETISS e CE1\_RMUISS, da seguinte maneira:

**Regra para retenção Dentro do Município:**

**CE1->CE1\_RETISS = 1 (Sim) e CE1->CE1\_RMUISS = 1-Dentro.**

Executa a retenção do ISS para o fornecedor (CE1->CE1\_FORISS+CE1->CE1\_LOJISS) se o município do Fornecedor (A2\_EST+A2\_CODMUN) for **igual** ao município da execução do serviço (SF1->F1\_ESTPRES+SF1->F1\_INCISS).

**Regra para retenção Fora do Município:**

| **CE1->CE1\_RETISS = 1 (Sim) e CE1->CE1\_RMUISS = 2-Fora.** |
| --- |

Executa a retenção do ISS para o fornecedor (CE1->CE1\_FORISS+CE1->CE1\_LOJISS) se o município do Fornecedor (A2\_EST+A2\_CODMUN) for **diferente** do município da Execução do serviço (SF1->F1\_ESTPRES+SF1->F1\_INCISS).

**Regra para retenção Dentro e Fora do Município:**

| **CE1->CE1\_RETISS = 1 (Sim) e CE1->CE1\_RMUISS = 3-Ambos.** |
| --- |

Executa a retenção do ISS para o fornecedor (CE1->CE1\_FORISS+CE1->CE1\_LOJISS) se o município do fornecedor (A2\_EST+A2\_CODMUN) for **igual ou diferente** do município da execução do serviço (SF1->F1\_ESTPRE+SF1->F1\_INCISS).

**Regra de Produto EP – ISSQN devido no Estabelecimento do Prestador.**

Para o Produto **EP** (B1\_MEPLES = 1) o município considerado na pesquisa da tabela CE1 para encontrar a regra da alíquota do ISS será o cadastrado na Filial (SIGAMAT).

A retenção do ISS considera a configuração dos campos CE1\_RETISS e CE1\_RMUISS, da seguinte maneira:

**Regra para retenção Dentro do Município:**

| **CE1->CE1\_RETISS = 1 (Sim) e CE1->CE1\_RMUISS = 1-Dentro.** |
| --- |

Executa a retenção do ISS para o fornecedor (CE1->CE1\_FORISS+CE1->CE1\_LOJISS) se o município do fornecedor (A2\_EST+A2\_CODMUN) for **igual** ao município da filial **(SIGAMAT.EMP)**.

**Regra para retenção Fora do Município:**

| **CE1->CE1\_RETISS = 1 (Sim) e CE1->CE1\_RMUISS = 2-Fora.** |
| --- |

Executa a retenção do ISS para o fornecedor (CE1->CE1\_FORISS+CE1->CE1\_LOJISS) se o município do fornecedor (A2\_EST+A2\_CODMUN) for **diferente** do município da filial **(SIGAMAT.EMP).**

**Regra para retenção Dentro e Fora do Município:**

| **CE1->CE1\_RETISS = 1 (Sim) e CE1->CE1\_RMUISS = 3-Ambos.** |
| --- |

Executa a retenção do ISS para o fornecedor (CE1->CE1\_FORISS+CE1->CE1\_LOJISS) se o município do fornecedor (A2\_EST+A2\_CODMUN) for **igual ou diferente** do município da filial **(SIGAMAT.EMP)**.

**Notas Fiscais de Saída:**

**Regra de Produto LES – ISSQN devido no local da execução do serviço.**

Considera o município informado nos campos **C5\_ESTPRES + C5\_MUNPRES** para pesquisar a alíquota do ISS e município do **SIGAMAT** para buscar o código do serviço da prestação**(CE1->CE1\_CPRISS)** na tabela CE1.

**Regra de Produto EP – ISSQN devido no Estabelecimento do Prestador.**

Considera o município do **SIGAMAT** para pesquisar a alíquota do ISS e o código do serviço da prestação **(CE1->CE1\_CPRISS)** na tabela CE1.
