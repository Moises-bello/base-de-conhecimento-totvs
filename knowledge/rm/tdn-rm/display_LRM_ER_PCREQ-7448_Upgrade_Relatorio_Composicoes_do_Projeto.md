---
content_hash: 31ff93a3f4a8d1993cb2652466d1c3ce19f36268242d34266658797e4f546b62
fetched_at: '2026-06-29T00:06:11.416154+00:00'
page_id: '203768729'
product: rm
source: tdn-rm
title: ER_PCREQ-7448_Upgrade_Relatorio_Composicoes_do_Projeto
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-7448_Upgrade_Relatorio_Composicoes_do_Projeto
version: 34
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão de Obras e Projetos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP008 | **IRM1** | PCREQ-7447 |
| **Requisito1** | PCREQ-7448 | **Subtarefa1** | PDR\_CP\_TOP008-62 |
| **Chamado2** | - | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | - |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Migração dos relatórios de Composições do Projeto utilizando o RM Reports.

## Definição da Regra de Negócio

Os relatórios de composição que serão migrados da antiga MDI (executável RMSolum.exe) para a nova na MDI, são os seguintes:

Relatórios Baseados no Gerador: 

* Composição de Custo Unitário Utilizadas no Projeto
* Composição Por Produção Utilizadas no Projeto

Relatórios de Modelo Fixo: 

* Planilha de Composição Analítica por Tarefas Considerando BDI Diferenciado
* Planilha de Composição Analítica por Tarefas Considerando BDI Diferenciado Separado
* Planilhas de Composição Analíticas de Custos Unitários
* Planilhas de Composição Analíticas de Preços Unitários por Produção
* Planilha Analítica de CPUs por Tarefas com Descr. Composição Auxiliar
* Planilha Analítica de CPUs por Tarefas com Descr. Composição Auxiliar ao final

Para que seja possível a importação dos relatórios na nova MDI, os relatórios serão disponibilizados através de arquivos de importação, e poderão ser importados através do RMReports.

Através da tela abaixo, os arquivos de importação dos relatórios (Ex.: Composição de Custo Unitário Utilizadas no Projeto) são selecionados e importados.

Após importados, podem ser visualizados em**Relatórios >> Composições >>Composições do Projeto.**

#### Restrições

* Estes relatórios são padrão no sistema e por questão de segurança o usuário não poderá editar ou excluí-los,   
  porém será possível duplicá-lo criando cópias, e assim editar e customizar estas cópias, de acordo com a necessidade.

#### Filtros

* Por cenário e tipo de planilha.
* Tarefa inicial e final.

#### Localização do Relatório

Interna: RM/Documentos/Prj-Projetos/Relatórios/Relatorios Migrados

Clientes: Pasta "Objetos Gerenciais" localizada no diretório de instalação do Produto.

Importante

Para que um relatório seja gerado pelo Menu Relatórios -> Composições -> Composições do projeto, o mesmo tem que ser do tipo Composições do Projeto e deve-se utilizar em um dos detalhes (Banda) do relatório a tabela de Insumos/Composições do Projeto (MRELRECURSO).

É recomendado calcular o projeto antes de gerar os relatórios.

Os valores dos totalizadores dos relatórios, por questões de arredondamento (uma vez que os relatórios não utilizam as casas decimas definidas nos parâmetros de projeto), podem apresentar valores aceitavelmente um pouco maiores ou menores.

### Protótipo de Tela

#### **Protótipo 01 – Tela de filtros e geração do relatório**

#### ****Protótipo 02 – Composição por Produção****

Este relatório exibe as composições do tipo Produção separando seus recursos pelo Grupo DNIT (Equipamentos, Materiais, Mão de Obra e Transporte). Ao final é mostrado um totalizador para cada grupo além da Produção da Equipe e o Custo Unitário da Execução.

#### **Protótipo 03 – Composição de Custo Unitário**

Este relatório exibe as composições do tipo CPU (Custo Unitário) separadas pelo grupo DNIT (Equipamentos, Materiais, Mão de Obra e Transporte).

#### Protótipo 04 - Planilha de composição analítica por tarefas considerando BDI diferenciado

Este é o primeiro dos relatórios de modelo fixo que será migrado. Ele, como o próprio nome diz, exibirá uma planilha com as composições utilizadas no projeto por tarefa considerando BDI diferenciado. Ele será gerado da mesma forma que os outros relatórios do gerador e possuirá os mesmo filtros descritos no item anterior.

Este relatório, na versão anterior (Gerador antigo) possui dois filtros que não serão mais apresentados na tela de geração do relatório, pois o novo gerador (RM Reports) possui funcionalidades que suprem esses filtros. Abaixo segue uma tabela com os filtros e as medidas tomadas para atenderem ao novo gerador de relatórios.

|  |  |
| --- | --- |
| **Filtro** | **Nova característica** |
| Ordenação por código da tarefa ou descrição | O novo gerador possui esta funcionalidade. O relatório padrão será ordenado pelo código da tarefa. Para mudá-lo, abra o template do relatório, clique no Detalhe da tarefa e selecione “Ordenação”. |
| Aprensentar o BDI Diferenciado Separado | Para atender a este filtro foi criado um outro template (Planilha de composição analítica por Tarefas com BDI Dif. Separado) onde neste são apresentados o BDI diferenciado junto aos totalizadores ao invés de aplicá-lo em cada coeficiente dos recurso da composição. |

Abaixo um exemplo deste relatório e logo mais com o BDI Diferenciado Separado.

Repare que o servente da Composição 000002 - Escavação para blocos o BDI Diferenciado é aplicado no coeficiente do mesmo no primeiro relatório, já com o BDI Diferenciado separado o coeficiente é mantido e o BDI Diferenciado é mostrado junto com os totalizadores da Composição no segundo relatório.

#### Protótipo 05 - Planilha de composição analítica de preços unitários por produção

Este é o segundo dos relatórios de modelo fixo que será migrado. Ele exibirá uma planilha analítica com as composições de preços unitários por produção utilizadas no projeto agrupadas pelo grupo DNER. Ele será gerado da mesma forma que os outros relatórios do gerador e possuirá os mesmo filtros descritos no item anterior.

Abaixo um exemplo deste relatório:

Protótipo 4: Planilha de composição analítica de preços unitários

#### Protótipo 06 - Planilha de composição analítica de custo unitários

Este é o terceiro dos relatórios de modelo fixo que será migrado. Ele exibirá uma planilha analítica com as composições de custos unitários utilizadas no projeto agrupadas pelo grupo de custo. Ele será gerado da mesma forma que os outros relatórios do gerador e possuirá os mesmo filtros descritos no item anterior.

Abaixo um exemplo deste relatório:

Protótipo 5: Planilha de composição de custos unitários

#### Protótipo 07 - Planilha analítica de CPUs por tarefas com descr. Composição auxiliar

Este é o quarto dos relatórios de modelo fixo que será migrado. Ele exibirá uma planilha analítica com as composições de preços unitários e suas composições auxiliares recursivas utilizadas no projeto por tarefas. Ele será gerado da mesma forma que os outros relatórios do gerador e possuirá os mesmo filtros descritos no item anterior.

Este relatório, na versão do Delphi possui alguns filtros que não serão mais apresentados na tela de geração do relatório, pois o novo gerador (RM Reports) possui funcionalidades que suprem esses filtros. Abaixo segue uma tabela com os filtros e as medidas tomadas para atenderem ao novo gerador de relatórios.

|  |  |
| --- | --- |
| **Filtro** | **Nova característica** |
| Ordenação por código da tarefa ou descrição | O novo gerador possui esta funcionalidade. O relatório padrão será ordenado pelo código da tarefa. Para mudá-lo, abra o template do relatório, clique no Detalhe da tarefa e selecione “Ordenação”. |
| Imprimir composições repetidas | O novo gerador também possui esta funcionalidade. Para isso insira um cabeçalho no Detalhe de tarefa para agupá-la pela composição. |
| Imprimir composições ao final | Para atender a este filtro foi criado um outro template (04.009.1 - Planilha Analítica de CPUs por Tarefas com Descr. Composição Auxiliar ao final) onde neste são impressos as composições auxiliares ao final do relatório. Os dados são os mesmos de ambos os relatórios, porém as composições auxliares no primeiro são exibidas logo após a sua composição pai e no segundo são exibidas ao final do relatório. |
| Data do relatório | O novo gerador possui um campo para a data do relatório. |
| Aba Texto para cabeçalho e rodapé. | Pode ser inserido um cabeçalho e rodapé do relatório com texto padrão no template do relatório pelo RM Reports. |

Com a dinâmica oferecida pelo RM Reports o usuário pode modificar o relatório para atender aos filtros acima ou a qualquer customização que o quera fazer. Para isso, crie uma cópia do relatório usando o processo de mesmo nome na guia Gestão do menu principal e o modifique a sua maneira ou comece um novo relatório que achar interessante.

Para atender a recursividade que este relatório necessita foi criado o SQL recursivo e inserido como sentença SQL no novo gerador. O primeiro SQL funciona no SQL Server e no Oracle 11g+, porém não é suportado no Oracle 10g. Para o Oracle 10g foi criada uma segunda sentença e consequentemente um outro template para o relatório. Segue as sentenças criadas abaixo:

**Sentença SQL Server e Oracle 11g (CMPAUXRECURSIVE):**

**WITH** **FUNCCMPAUX**(CODCOLIGADA, IDPRJ, IDREC, IDCMP, IDCMPFILHA, IDCMP2, IDCMPFILHA2, NIVEL)

**AS** (**SELECT** MRECCMP.CODCOLIGADA,

                MRECCMP.IDPRJ,

                MRECCMP.IDREC,

                MRECCMP.IDCMP,

                MRECCMP.IDCMPFILHA,

                MRECCMP.IDCMP,

                MRECCMP.IDCMPFILHA,

                1

**FROM** **MRECCMP** (**NOLOCK**)

**WHERE** MRECCMP.ATIVO = 1

**AND** MRECCMP.IDCMPFILHA **IS** **NOT NULL**

**UNION ALL**

**SELECT** MRECCMP.CODCOLIGADA,

                MRECCMP.IDPRJ,

                FUNCCMPAUX.IDREC,

                MRECCMP.IDCMP,

                MRECCMP.IDCMPFILHA,

                FUNCCMPAUX.IDCMP2,

                FUNCCMPAUX.IDCMPFILHA2,

                FUNCCMPAUX.NIVEL + 1

**FROM** **MRECCMP** (**NOLOCK**)

**JOIN** FUNCCMPAUX

**ON** FUNCCMPAUX.CODCOLIGADA = MRECCMP.CODCOLIGADA

**AND** FUNCCMPAUX.IDPRJ = MRECCMP.IDPRJ

**AND** FUNCCMPAUX.IDCMP = MRECCMP.IDCMPFILHA

**WHERE** MRECCMP.ATIVO = 1

**AND** MRECCMP.IDCMPFILHA = funcCmpAux.IDCMP)

**SELECT** MCMP.CODCMP,

       MCMP.DESCCMP,

       FUNCCMPAUX.NIVEL,

       FUNCCMPAUX.IDCMP2,

       FUNCCMPAUX.IDCMPFILHA2,

       MRECCMP.\*

**FROM** FUNCCMPAUX

**JOIN** **MRECCMP** (**NOLOCK**)

**ON** MRECCMP.IDREC = FUNCCMPAUX.IDREC

**AND** MRECCMP.CODCOLIGADA = FUNCCMPAUX.CODCOLIGADA

**AND** MRECCMP.IDPRJ = FUNCCMPAUX.IDPRJ

**JOIN** **MCMP** (**NOLOCK**)

**ON** MCMP.IDCMP = MRECCMP.IDCMPFILHA

**AND** MCMP.CODCOLIGADA = MRECCMP.CODCOLIGADA

**AND** MCMP.IDPRJ = MRECCMP.IDPRJ

**WHERE** FUNCCMPAUX.CODCOLIGADA = :P\_CODCOLIGADA

**AND** FUNCCMPAUX.IDPRJ = :P\_IDPRJ

**AND** FUNCCMPAUX.IDCMP = :P\_IDRECURSO

**ORDER  BY** FUNCCMPAUX.NIVEL

**Sentença Oracle 10g (CMPAUXRECURSIVE):**

**SELECT** MCMP.CODCMP,

       MCMP.DESCCMP,

       MRECCMP.\*,

**LEVEL**

**FROM** **MRECCMP** (NOLOCK)

**JOIN** **MCMP** (NOLOCK)

**ON** MCMP.IDCMP = MRECCMP.IDCMPFILHA

**AND** MCMP.CODCOLIGADA = MRECCMP.CODCOLIGADA

**AND** MCMP.IDPRJ = MRECCMP.IDPRJ

**WHERE** MRECCMP.CODCOLIGADA = :P\_CODCOLIGADA

**AND** MRECCMP.IDPRJ = :P\_IDPRJ

**AND** MRECCMP.ATIVO = 1

**AND** MRECCMP.IDCMPFILHA **IS** **NOT NULL**

**START WITH** MRECCMP.IDCMP = :P\_IDRECURSO

**CONNECT BY PRIOR** MRECCMP.IDCMPFILHA = MRECCMP.IDCMP

**ORDER  BY LEVEL**

As variáveis: P\_CODCOLIGADA, P\_IDPRJ e P\_IDRECURSO, são setadas pelo Detalhe pai do relatório que neste caso é a tabela MRELRECURSO.

Para obter os recursos das composições auxiliares retornadas pelas sentenças SQL acima, foi criado uma outra sentença onde a variável P\_IDCMPFILHA2 (SQL Server  e Oracle 11g), P\_IDCMPFILHA (Oracle 10g) é o identificador da composição auxiliar retornada pela sentença pai. Segue as sentenças abaixo:

**SQL Server e Oracle 11g (RECCMPAUXRECURSIVE):**

**SELECT** \*

**FROM** **MRECCMP** (**NOLOCK**)

**WHERE** MRECCMP.IDCMP = :P\_IDCMPFILHA2

**Oracle 10g (RECCMPAUXRECURSIVE)****:**

**SELECT** \*

**FROM** **MRECCMP** (NOLOCK)

**WHERE** MRECCMP.IDCMP = :P\_IDCMPFILHA

O código das sentenças (CMPAUXRECURSIVE e RECCMPAUXRECURSIVE) não podem ser alterados, pois cada um será o DataMember (membro de dados) do Detalhe que ele será inserido. Se estes nomes foream alterados podem ocorrer problemas ao gerar o relatório.

Abaixo um exemplo deste relatório:

Protótipo 6: Composição de preços unitários

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
