---
article_id: 14635265382551
category: MDT - Laudos
content_hash: 5f6e10278ec5475a454d2da418586f03b5a97061eabe80097de6571d2bc8ea44
fetched_at: '2026-06-28T22:44:26.434012+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Qual conceito e interpretação dos campos cadastrais
  da rotina de Laudos
type: support-article
updated_at: '2024-07-04T12:26:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14635265382551-RH-Linha-Protheus-MDT-Qual-conceito-e-interpreta%C3%A7%C3%A3o-dos-campos-cadastrais-da-rotina-de-Laudos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24649883253783) Tempo aproximado para leitura: **00:06:00 min** **Dúvida**Qual conceito e interpretação dos campos cadastrais da rotina de Laudos?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**A rotina de Laudos (**MDTA210**) permite desenvolver a estrutura que servirá como base para impressão dos Laudos Legais necessários para a área de Medicina e Segurança do Trabalho, tais como o **PPRA**, **PCMSO**e etc.   
É importante destacar que nesta rotina se dará o cadastro das estruturas, sendo que as informações contidas nos mesmo serão extraídas de diversos lugares do sistema, de maneira a simplificar a impressão destas.  
Tem o objetivo de descrever a estrutura a ser utilizada na impressão dos Laudos Ambientais, de acordo com o seu tipo (**Tipos de Laudos**), e com isto, relacionar com os demais registros do sistema para impressão das informações necessárias para a área de Medicina e Segurança do Trabalho.

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| **Laudo (TO0\_LAUDO)** | Código (ou nome) para identificação do laudo.  **Obs**.: Não é disponível para alterações.  Exemplo: PPRA18 |
| **Nome Laudo (TO0\_NOME)** | Nome para identificação do laudo.  Exemplo: LAUDO DE PPRA 2018 |
| **Data Início (TO0\_DTINIC)** | Permite a inserção de uma data referente ao dia/mês/ano de inicio da vigência de um laudo. Esta data corresponde ao começo da elaboração do laudo, desde de suas primeiras medições e levantamentos dos conteúdos.  Exemplo: 01/01/2018 |
| **Data Final (TO0\_DTFIM)** | Permite a inserção de uma data referente ao dia/mês/ano de fim, efetivo, da vigência de um laudo. Finalização de todos os monitoramentos e cadastros do laudo.  Exemplo: 01/01/2019 |
| **Data Valid. (TO0\_DTVALI)** | Permite a inserção de uma data referente ao dia/mês/ano de fim, efetivo, da vigência de um laudo. Estabelece um limite de vigência, informando que o laudo deixa de ser válido quando a data informada for ultrapassada.  Exemplo: 01/01/2019 |
| **Cliente (TO0\_CLIENT)** | Permite a seleção de um código de cliente para o qual foi realizado o Laudo.  Por meio deste código é possível a obtenção de dados como: endereço, cidade entre outros dados que serão apresentados no laudo.  Exemplo: INDCAS |
| **Loja (TO0\_LOJA)** | Campo que apresenta a loja do cliente informado previamente.  Exemplo: IC |
| **Nome Cliente (TO0\_NOMECL)** | Campo que apresenta o nome do cliente informado previamente.  Exemplo: INDÚSTRIAS CASCAVEL |
| **Grau Risco (TO0\_GRISCO)** | Apenas números podem ser informados neste campo sendo eles: 1, 2, 3 ou 4.  O número informado indica o Grau de Risco onde, 1 representa o grau mínimo e 4 o grau máximo, conforme Classificação Nacional de Atividades Econômicas.  Exemplo: 2 |

|  |  |
| --- | --- |
| **Qtde Funcion (TO0\_QTDFUN)** | Permite a inserção de uma numeração referente a quantidade total de funcionários que trabalham no estabelecimento onde foi realizado os diagnósticos para criação do laudo.  Exemplo: 250 |
| **Objetivo (TO0\_ OBJETI)** | Campo que permite informar qual o objetivo principal do laudo.  Exemplo: IDENTIFICAR OS RISCOS PRESENTES NO LOCAL |
| **Tp. Elab. (TO0\_TIPELA)** | Indica se responsável, pela elaboração do laudo, será provindo da tabela QAA, de Responsáveis/Usuários (para o módulo de **SIGASGA** - Gestão Ambiental), ou da tabela TMK de Usuários do SESMT (para o módulo de **SIGAMDT** - Medicina e Segurança do Trabalho). Exemplo: 2 - SESMT |
| **Res. Elab. (TO0\_CODUSU)** | Campo que permite informar o código do responsável pela elaboração do laudo com base no **Tp. Elab.** (**TO0\_TIPELA**), informado previamente.  Exemplo: FULANO. |
| **Nome (TO0\_NUMUSU)** | Campo responsável pela inserção do Código do Termo de Responsabilidade que será impresso na parte final do Laudo. A informação a ser selecionada neste campo deve estar previamente cadastrada na tabela de **Termos** **de Responsabilidade**(**TMZ**) da rotina **MDTA235**.  Exemplo: 000001 |
| **Documento (TO0\_DOCTO)** | Campo que identifica um documento que será relacionado a este laudo.  A informação a ser selecionada neste campo deve estar previamente cadastrada na tabela de **Documentos**(**QDH**) da rotina **QDOA050**.  Exemplo: Diagnóstico de Riscos e Agentes |
| **Revisão (TO0\_RV)** | Neste campo é possível informar um valor sequencial que diz respeito à revisão atual da documentação.  Exemplo: 4 |
| **Tipo Laudo (TO0\_TIPREL)** | Este campo possui extrema importância para o laudo e seu respectivo conteúdo.  Os tipos de laudos estão presentes na seguinte FAQ: **[Tipos de Laudos](https://tdn.totvs.com/x/ID2LFQ).**  O conteúdo presente na aba de Conteúdo Laudo será disponibilizado a partir do tipo de laudo selecionado. Cada laudo possui suas respectivas informações e o usuário irá decidir, a partir delas, o que deve ser realmente apresentado no conteúdo do laudo.  Exemplo: PPRA |
| **Centro Custo (TO0\_CC)** | Campo que indica qual o código do Centro de Custo no qual o laudo será elaborado.  Este campo apresenta registros provindos da tabela (**CTT**) de Centro de Custos (**CTBA180**)..  Exemplo: PROD |
| **Descrição (TO0\_NOMCC)** | Campo que apresenta a descrição do Centro de Custos selecionado previamente.  Exemplo: PRODUÇÃO |

|  |  |
| --- | --- |
| **Finalidade (TO0\_FINALI)** | Por meio deste campo, é possível indicar a finalidade do laudo a ser cadastrado. Dentre os valores disponíveis estão: 1 - Insalubre, 2 - Periculosidade ou 3 - Outros. Exemplo: Insalubre |
| **Tipo Aprov. (TO0\_TIPAPR)** | Campo que indica qual o tipo de usuário que será responsável pela aprovação do laudo. Os tipos disponíveis são: 1 - Usuário (provindo da tabela **QAA** da rotina **QAXA010**) e 2 - Funcionário (provindo da tabela **SRA** da rotina **GPEA010**). Exemplo: 2 - Funcionário |
| **Aprovador (TO0\_APROVA)** | Aqui será informado o código do aprovador. Este aprovador poderá ser um Usuário ou um Funcionário, esta configuração dependerá do valor informado no campo **Tipo Aprov**. (**TO0\_TIPAPR**).  Exemplo: 000001 |
| **Nome Aprov. (TO0\_NOMAPR)** | Campo que apresenta o nome do aprovador selecionado previamente.  Exemplo: FULANO TESTE |
| **Atividade (TO0\_ATIVID)** | Campo que permite informar o código da atividade industrial a ser apresentada no laudo. Os registros provindos deste campo dizem respeito a tabela de **Tarefa** **Industrial** (**TAR**).  Exemplo: 000001 |
| **Descrição (TO0\_DESATI)** | Campo que apresenta a descrição da tarefa selecionada previamente.  Exemplo: LIMPEZA DE RESÍDUOS PRESENTES NO MAQUINÁRIO. |

Acompanhe documentação completa: [Laudos (MDTA210 - SIGAMDT)](https://tdn.totvs.com/pages/releaseview.action?pageId=379313384)  
 **Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
