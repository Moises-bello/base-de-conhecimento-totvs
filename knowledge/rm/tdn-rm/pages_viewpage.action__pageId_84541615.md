---
content_hash: d5be37e7cf13d102d6c3beb97bde3e83f215bdea9d97151611b7f2d10e47c79a
fetched_at: '2026-06-29T00:11:50.836714+00:00'
page_id: '84541615'
product: rm
source: tdn-rm
title: RMFIS00002_Nota Técnica SEF II
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=84541615
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:**11.52 |
| **Processo** | **:** | SEF II |
| **Subprocesso** | **:** | Instruções para a importação do layout e geração da SEF II |
| **Data da publicação** | **:** | 12/07/2013 - atualizada em 11/09/2013 |

**Para a correta geração da rotina é necessário o seguinte ambiente:**

|  |  |  |  |
| --- | --- | --- | --- |
| ***VERSÃO BIBLIOTECA*** | ***PATCH BIBLIOTECA*** | ***ESPECÍFICA BIBLIOTECA*** | ***VERSÃO APLICATIVO*** |
| 11.52 | 11.52.57 | 11.52.57.160 | 11.52.57.14 |

Última versão do layout da rotina na qual pode ser encontrada na central de Downloads seguindo os passos abaixo:

1. Digite, [www.totvs.com/suporte](http://www.totvs.com/suporte)  
2. Faça o login, com seu Email e Senha.  
3. Clique em Download através da barra do menu do Portal do Cliente.  
4 Aplica-se o filtro: [ Linha = RM e Amb/Vers = RM 11.52.57 e Tipo = Apoio]  
5. Pronto! Na grid de download, listará todos os produtos da respectiva série informada.

**Origem dos dados**

A rotina é gerada exclusivamente com dados retirados do produto TOTVS Gestão Fiscal, com exceção dos dados de Inventário de Estoque. Estas informações deverão ser gravadas de forma manual, importação por texto ou escrituradas do TOTVS Gestão de Compras, Estoque e Faturamento.

Alguns registros da rotina solicitam informações dos Tributos (ICMS, IPI e ISSQN) por Item movimentado. Portanto estes deverão estar parametrizados nos Itens do Lançamento Fiscal.

As informações referentes ao Inventário do Estoque são retiradas do TOTVS Gestão de Compras, Estoque e Faturamento. Para a correta geração destas informações todos os processos de geração de saldo de inventário deverão ter sido disparados antes da geração da rotina.

É importante lembrar que os Lotes de Lançamentos Fiscal deverão ter sido liberados e os Períodos de Apuração dos Tributos encerrados antes da geração da rotina.

**Livros atendidos pelo produto RM**

Os livros a serem gerados dependem do perfil do contribuinte. Para saber em qual perfil se enquadra o contribuinte deve entrar em contato com a SEFAZ PE e solicitar esta informação. Ele pode também efetuar o cadastro de sua filial no validador da SEF II e solicitar ao programa que atualize as informações do perfil. Desta forma serão gravados os livros que ele é obrigado a gerar.

**ICMS-LA**

**ICMS-Guias**

**ICMS-RI**

**ICMS-LMC - Gera somente bloco de identificação/encerramento**

**ICMS-RIDF - Gera somente bloco de identificação/encerramento**

**ICMS-RV - Gera somente bloco de identificação/encerramento**

**e-DOC**

**Detalhamento das informações e não aderências na geração da rotina.**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | **LIVRO** |  |
| **BLOCO** | **REGISTRO** | **DESCRIÇÃO** | **LA-ICMS** | **e-DOC** | **GI-ICMS** | **RIDF** | **LMC** | **RI** | **RV** | **GERADO** |
| **0** |  | **ABERTURA, IDENTIFICAÇÃO E REFERÊNCIAS** |  |  |  |  |  |  |  |  |
|  | 0000 | ABERTURA DO ARQUIVO DIGITAL E IDENTIFICAÇÃO DO CONTRIBUINTE | X | X | X | X | X | X | X | **S** |
|  | 0001 | ABERTURA DO BLOCO 0 | X | X | X | X | X | X | X | **S** |
|  | 0005 | DADOS COMPLEMENTARES DO CONTRIBUINTE | X | X | X | X | X | X | X | **S** |
|  | 0025 | BENEFÍCIO FISCAL | X | X | X | X | X | X | X | **S** |
|  | 0030 | PERFIL DO CONTRIBUINTE | X | X | X | X | X | X | X | **S** |
|  | 0100 | CONTABILISTA | X | X | X | X | X | X | X | **S** |
|  | 0150 | TABELA DE CADASTRO DO PARTICIPANTE | X | X | X | X |  | X | X | **S** |
|  | 0175 | ENDEREÇO DOPARTICIPANTE |  | X |  | X |  | X | X | **S** |
|  | 0200 | TABELA DE IDENTIFICAÇÃO DO ITEM |  | X |  |  | X | X |  | **S** |
|  | 0205 | CÓDIGO ANTERIOR DO ITEM |  | X |  |  | X | X |  | **S** |
|  | 0210 | ITEM COMPOSTO OU RELAÇÃO INSUMO/PRODUTO |  | X |  |  |  | X |  | **N** |
|  | 0215 | CORRELAÇÃO COM A TABELA DA ANP |  |  |  |  | X |  |  | **S** |
|  | 0400 | TABELA DE NATUREZA DA OPERAÇÃO/PRESTAÇÃO | X | X |  |  |  |  |  | **S** |
|  | 0450 | TABELA DE INFORMAÇÕES COMPLEMENTARES/REGISTRO DE OBSERVAÇÕES | X | X |  | X | X | X | X | **S** |
|  | 0455 | NORMA REFERENCIADA | X | X |  | X | X | X | X | **S** |
|  | 0460 | DOCUMENTO DE ARRECADAÇÃO REFERENCIADO | X | X |  | X | X | X | X | **S** |
|  | 0465 | DOCUMENTO FISCAL REFERENCIADO | X | X |  | X | X | X | X | **S** |
|  | 0470 | CUPOM FISCAL REFERENCIADO | X | X |  | X | X | X | X | **S** |
|  | 0990 | ENCERRAMENTO DO BLOCO 0 | X | X | X | X | X | X | X | **S** |
| **C** |  | **DOCUMENTOS FISCAIS DO ICMS E DO IPI – MERCADORIAS** |  |  |  |  |  |  |  |  |
|  | C001 | ABERTURA DO BLOCO C |  | X |  |  |  |  |  | **S** |
|  | C020 | DOCUMENTO – NOTA FISCAL (01), NOTA FISCAL DE PRODUTOR (04), E NOTA FISCAL ELETRÔNICA (55) |  | X |  |  |  |  |  | **S** |
|  | C040 | COMPLEMENTO DO DOCUMENTO – ISS |  | X |  |  |  |  |  | **S** |
|  | C300 | ITENS DO DOCUMENTO |  | X |  |  |  |  |  | **S** |
|  | C310 | COMPLEMENTO DO ITEM – ISS |  | X |  |  |  |  |  | **S** |
|  | C550 | DOCUMENTO – NOTA FISCAL DE VENDA A CONSUMIDOR (02) |  | X |  |  |  |  |  | **S** |
|  | C560 | ITENS DO DOCUMENTO |  | X |  |  |  |  |  | **N** |
|  | C600 | DOCUMENTO – CUPOM FISCAL/ICMS (02 e 2D) |  | X |  |  |  |  |  | **N** |
|  | C605 | COMPLEMENTO DO DOCUMENTO – ISS |  | X |  |  |  |  |  | **N** |
|  | C610 | ITENS DO DOCUMENTO |  | X |  |  |  |  |  | **N** |
|  | C615 | COMPLEMENTO DO ITEM – ISS |  | X |  |  |  |  |  | **N** |
|  | C990 | ENCERRAMENTO DO BLOCO C |  | X |  |  |  |  |  | **S** |
| **E** |  | **LIVROS DE REGISTRO DAS OPEARÇÕES DA APURAÇÃO DO ICMES E DO IPI** |  |  |  |  |  |  |  |  |
|  | E001 | ABERTURA DO BLOCO E | X |  |  |  |  |  |  | **S** |
|  | E003 | CAMPOS ADICIONAIS | X |  |  |  |  |  |  | **S** |
|  | E020 | NOTA FISCAL (CÓDIGO 01), NOTA FISCAL DE PRODUTOR (CÓDIGO 04) E NOTA FISCAL ELETRÔNICA (CÓDIGO 55) | X |  |  |  |  |  |  | **S** |
|  | E025 | DETALHE - VALORES PARCIAIS | X |  |  |  |  |  |  | **S** |
|  | E050 | LANÇAMENTO - NOTA FISCAL DE VENDA A CONSUMIDOR (CÓDIGO 02) | X |  |  |  |  |  |  | **S** |
|  | E055 | DETALHE - VALORES PARCIAIS | X |  |  |  |  |  |  | **S** |
|  | E060 | LANÇAMENTO - REDUÇÃO Z/ICMS | X |  |  |  |  |  |  | **S** |
|  | E065 | DETALHE - VALORES PARCIAIS | X |  |  |  |  |  |  | **S** |
|  | E080 | LANÇAMENTO - MAPA-RESUMO DE ECF/ICMS | X |  |  |  |  |  |  | **S** |
|  | E085 | DETALHE – VALORES PARCIAIS | X |  |  |  |  |  |  | **S** |
|  | E100 | LANÇAMENTO - NOTA FISCAL/CONTA DE ENERGIA ELÉTRICA (CÓDIGO 06) OU NOTA FISCAL (CÓDIGO 01 OU CÓDIGO 55) - NAS | X |  |  |  |  |  |  | **S** |
|  | E105 | DETALHES – VALORES PARCIAIS | X |  |  |  |  |  |  | **S** |
|  | E120 | LANÇAMENTO - NOTA FISCAL DE SERVIÇO DE TRANSPORTE (CÓDIGO 07), CONHECIMENTOS DE TRANSPORTE RODOVIÁRIO DE | X |  |  |  |  |  |  | **S** |
|  | E140 | LANÇAMENTO - BILHETES DE PASSAGEM RODOVIÁRIO (CÓDIGO 13), AQUAVIÁRIO (CÓDIGO 14), NOTA DE BAGAGEM (CÓDIGO 15), MANIFESTO DE VÔO (CÓDIGO 30), E FERROVIÁRIO (CÓDIGO 16) | X |  |  |  |  |  |  | **S** |
|  | E300 | APURAÇÃO DO ICMS | X |  |  |  |  |  |  | **N** |
|  | E305 | MAPA – RESUMO DE OPERAÇÕES | X |  |  |  |  |  |  | **N** |
|  | E310 | CONSOLIDAÇÃO POR CFOP DOS VALORES DO ICMS | X |  |  |  |  |  |  | **N** |
|  | E330 | TOTALIZAÇÃO DAS OPERAÇÕES DO ICMS | X |  |  |  |  |  |  | **N** |
|  | E340 | SALDOS DA APURAÇÃO DO ICMS | X |  |  |  |  |  |  | **N** |
|  | E350 | AJUSTES DA APURAÇÃO DO ICMS | X |  |  |  |  |  |  | **N** |
|  | E360 | OBRIGAÇÕES DO ICMS A RECOLHER | X |  |  |  |  |  |  | **N** |
|  | E500 | APURAÇÃO DO IPI (MODELO 8) | X |  |  |  |  |  |  | **N** |
|  | E520 | CONSOLIDACAO POR CFOP DOS VALORES DO IPI | X |  |  |  |  |  |  | **N** |
|  | E525 | TOTALIZAÇÃO DAS OPERAÇÕES DO IPIE | X |  |  |  |  |  |  | **N** |
|  | E540 | SALDOS DA APURAÇÃO DO IPI | X |  |  |  |  |  |  | **N** |
|  | E550 | AJUSTES DA APURAÇÃO DO IPI | X |  |  |  |  |  |  | **N** |
|  | E560 | OBRIGAÇÕES DO IPI A RECOLHER | X |  |  |  |  |  |  | **N** |
|  | E990 | ENCERRAMENTO DO BLOCO E | X |  |  |  |  |  |  | **S** |
| **F** |  | **LIVROS E MAPAS DE REGISTRO DAS OPERAÇÕES DE CONTROLE** |  |  |  |  |  |  |  |  |
|  | F001 | ABERTURA DO BLOCO F |  |  |  | X | X |  | X | **S** |
|  | F020 | REGISTRO DE IMPRESSÃO DE DOCUMENTOS FISCAIS |  |  |  | X |  |  |  | **N** |
|  | F025 | SOLICITAÇÃO PARA IMPRESSÃO |  |  |  | X |  |  |  | **N** |
|  | F030 | DOCUMENTOS SOLICITADOS |  |  |  | X |  |  |  | **N** |
|  | F035 | DOCUMENTOS LIBERADOS |  |  |  | X |  |  |  | **N** |
|  | F200 | LIVRO DE MOVIMENTAÇÃO DE COMBUSTÍVEIS |  |  |  |  | X |  |  | **N** |
|  | F205 | CADASTRO DAS BOMBAS |  |  |  |  | X |  |  | **N** |
|  | F210 | COMBUSTÍVEL COMERCIALIZADO |  |  |  |  | X |  |  | **N** |
|  | F215 | MOVIMENTAÇÃO |  |  |  |  | X |  |  | **N** |
|  | F220 | TANQUE |  |  |  |  | X |  |  | **N** |
|  | F225 | NOTAS FISCAIS |  |  |  |  | X |  |  | **N** |
|  | F230 | ENCERRANTE |  |  |  |  | X |  |  | **N** |
|  | F250 | REGISTRO DE VEÍCULOS |  |  |  |  |  |  | X | **N** |
|  | F255 | MOVIMENTAÇÃO |  |  |  |  |  |  | X | **N** |
|  | F990 | ENCERRAMENTO DO BLOCO F |  |  |  | X | X |  | X | **S** |
| **G** |  | **INFORMAÇÕES ECNÔMICO FISCAIS** |  |  |  |  |  |  |  |  |
|  | G001 | ABERTURA DO BLOCO G |  |  |  |  |  |  |  | **S** |
|  | G020 | GUIA DE INFORMAÇÕES ECONÔMICO-FISCAIS |  |  |  |  |  |  |  | **S** |
|  | G025 | DOCUMENTOS REGISTRADOS |  |  |  |  |  |  |  | **S** |
|  | G030 | CUPONS REGISTRADOS |  |  |  |  |  |  |  | **S** |
|  | G050 | MAPA – RESUMO DE OPERAÇÕES |  |  |  |  |  |  |  | **S** |
|  | G400 | ICMS – CONSOLIDAÇÃO POR CFOP |  |  |  |  |  |  |  | **S** |
|  | G410 | ICMS – TOTALIZAÇÃO DAS OPERAÇÕES |  |  |  |  |  |  |  | **S** |
|  | G420 | ICMS – SALDOS DA APURAÇÃO |  |  |  |  |  |  |  | **S** |
|  | G430 | ICMS – TOTALIZAÇÃO DOS AJUSTES DA APURAÇÃO |  |  |  |  |  |  |  | **S** |
|  | G440 | ICMS – TOTALIZAÇÃO DAS OBRIGAÇÕES E RECOLHER |  |  |  |  |  |  |  | **S** |
|  | G450 | ICMS – TOTALIZAÇÃO DAS OPERAÇÕES INTERESTADUAIS |  |  |  |  |  |  |  | **S** |
|  | G460 | ICMS – SUBTORAIS POR UF |  |  |  |  |  |  |  | **S** |
|  | G990 | ENCERRAMENTO DO BLOCO G |  |  |  |  |  |  |  | **S** |
| **H** |  | **LIVRO DE REGISTRO DO INVENTÁRIO** |  |  |  |  |  |  |  |  |
|  | H001 | ABERTURA DO BLOCO H |  |  |  |  |  |  |  | **S** |
|  | H020 | REGISTRO DE INVENTÁRIO |  |  |  |  |  | X |  | **S** |
|  | H030 | ITENS INVENTARIADOS |  |  |  |  |  | X |  | **S** |
|  | H040 | SUBTOTAIS POR POSSUIDOR/PROPRIETÁRIO |  |  |  |  |  | X |  | **S** |
|  | H050 | SUBTOTAIS POR TIPO DE ITEM |  |  |  |  |  | X |  | **S** |
|  | H060 | SUBTOTAIS POR NCM |  |  |  |  |  | X |  | **S** |
|  | H990 | ENCERRAMENTO DO BLOCO H |  |  |  |  |  | X |  | **S** |
| **8** |  | **INFORMAÇÕES COMPLEMENTARES DA SEFAZ/UF** |  |  |  |  |  |  |  |  |
|  | 8001 | ABERTURA DO BLOCO 8 – DADOS DE PERNAMBUCO |  |  | X |  |  |  |  | **N** |
|  | 8020 | INFORMAÇÕES COMPLEMENTARES – QUADRO DE CÁLCULO DO VALOR ADICIONADO |  |  | X |  |  |  |  | **N** |
|  | 8030 | QVA – DETALHAMENTO POR MUNICÍPIO DAS OPERAÇÕES E PRESTAÇÕES |  |  | X |  |  |  |  | **N** |
|  | 8040 | QVA – AJUSTE DE VALORES POR CFOP |  |  | X |  |  |  |  | **N** |
|  | 8050 | QVA – CÁLCULO DO VALOR ADICIONADO |  |  | X |  |  |  |  | **N** |
|  | 8100 | INFORMAÇÕES COMPLEMENTARES – QUADRO DE AQUISIÇÃO DE BENS |  |  | X |  |  |  |  | **N** |
|  | 8110 | QAB – AQUISIÇÃO DE BENS PARA USO/CONSUMO OU ATIVO FIXO |  |  | X |  |  |  |  | **N** |
|  | 8160 | INFORMAÇÕES COMPLEMENTARES – QUADRO DE CONTROLE DO CRÉDITO ACUMULADO |  |  | X |  |  |  |  | **N** |
|  | 8165 | QCA – CONTROLE DO CRÉDITO ACUMULADO |  |  | X |  |  |  |  | **N** |
|  | 8170 | QCA – CRÉDITO ACUMULADO NO PERÍODO |  |  | X |  |  |  |  | **N** |
|  | 8175 | QCA – UTILIZAÇÃO DE CRÉDITO ACUMULADO |  |  | X |  |  |  |  | **N** |
|  | 8180 | QCA – COMPENSAÇÃO DE DÉBITO |  |  | X |  |  |  |  | **N** |
|  | 8300 | INFORMAÇÕES COMPLEMENTARES – QUADRO DO CONSUMO CONTINUADO |  |  | X |  |  |  |  | **N** |
|  | 8310 | QCC – CONSUMO CONTINUADO |  |  | X |  |  |  |  | **N** |
|  | 8500 | GUIA DE APURAÇÃO DOS INCENTIVOS FISCAIS E FINANCEIROS |  |  | X |  |  |  |  | **N** |
|  | 8505 | BENEFÍCIOS FISCAIS |  |  | X |  |  |  |  | **N** |
|  | 8510 | GIAF – AJUSTES DO BENEFÍCIOS |  |  | X |  |  |  |  | **N** |
|  | 8515 | SUB-APURAÇÕES POR BENEFÍCIO |  |  | X |  |  |  |  | **N** |
|  | 8525 | GIAF – ITEM INCENTIVADO (PI) |  |  | X |  |  |  |  | **N** |
|  | 8530 | GIAF – LANÇAMENTO COM ITEM INCENTIVADO |  |  | X |  |  |  |  | **N** |
|  | 8535 | GIAF - ITENS INCENTIVADOS NO DOCUMENTO |  |  | X |  |  |  |  | **N** |
|  | 8540 | INFORMAÇÕES COMPLEMENTARES DA SEFAZ/UF |  |  | X |  |  |  |  | **N** |
|  | 8545 | GIAF – APURAÇÃO INCENTIVADA |  |  | X |  |  |  |  | **N** |
|  | 8550 | GIAF – CONSOLIDAÇÃO POR CFOP DAS OPERAÇÕES INCENTIVADAS |  |  | X |  |  |  |  | **N** |
|  | 8555 | GIAF – TOTALIZAÇÃO DAS OPERAÇÕES INCENTIVADAS |  |  | X |  |  |  |  | **N** |
|  | 8560 | GIAF – SALDOS DA APURAÇÃO INCENTIVADA |  |  | X |  |  |  |  | **N** |
|  | 8565 | GIAF – AJUSTES DA APURAÇÃO INCENTIVADA |  |  | X |  |  |  |  | **N** |
|  | 8570 | PRODEPE INDÚSTRIA (CRÉDITO PRESUMIDO) |  |  | X |  |  |  |  | **N** |
|  | 8575 | PRODEPE IMPORTAÇÃO (CRÉDITO PRESUMIDO) |  |  | X |  |  |  |  | **N** |
|  | 8580 | PRODEPE IMPORTAÇÃO (DIFERIMENTO NA ENTRADA E CRÉDITO PRESUMIDO NA SAÍDA SUBSEQUENTE) |  |  | X |  |  |  |  | **N** |
|  | 8585 | GIAF 3 – PRODEPE IMPORTAÇÃO (SAÍDAS INTERNAS POR FAIXA DE ALUQUOTA) |  |  | X |  |  |  |  | **N** |
|  | 8590 | GIAF 4 – PRODEPE CENTRAL DE DISTRIBUIÇÃO (ENTRADAS/SAÍDAS) |  |  | X |  |  |  |  | **N** |
|  | 8990 | ENCERRAMENTO DO BLOCO 8 – DADOS PERNAMBUCO |  |  | X |  |  |  |  | **N** |
| **9** |  | **CONTROLE E ENCERRAMENTO DO ARQUIVO DIGITAL** |  |  |  |  |  |  |  |  |
|  | 9001 | ABERTURA DO BLOCO 9 | X | X | X | X | X | X | X | **S** |
| X | 9900 | LINHAS DO ARQUIVO DIGITAL | X | X | X | X | X | X | X | **S** |
|  | 9990 | ENCERRAMENTO DO BLOCO 9 | X | X | X | X | X | X | X | **S** |
|  | 9999 | ENCERRAMETNO DO ARQUIVO DIGITAL | X | X | X | X | X | X | X | **S** |

**Instruções para a geração da rotina.**

A geração da SEF II utiliza uma nova ferramenta desenvolvida pela RM, o Gerador de Saídas, que nas versões futuras possibilitará a customização da origem das informações geradas na rotina fiscal pelo próprio usuário. Até a presente versão somente o módulo de geração da rotina foi disponibilizada. O processo é transparente para o usuário e a única mudança no modo de geração das rotinas é a importação do layout que é enviado em arquivo separado. A seguir serão mostrados os passos para a importação do layout e geração da rotina.

Após atualizar a biblioteca e o aplicativo siga os seguintes passos para importar o layout:

**Criação da categoria do layout**

Acesse o menu Utilitários | SPED PIS/COFINS - Importação| Categoria do layout. Se for apresentada a tela de filtros crie um filtro para retornar todas as categorias ou simplesmente feche a tela.

Clique no botão NOVO e será aberta a tela para a inclusão da categoria. Preencha os campos conforme figura abaixo:

Na guia Perfis da Categoria do Gerador de Saídas insira o perfil ao qual os usuários que terão permissão para gerar a rotina estão associados. Para isto clique no botão novo e na tela apresentada clique no lookup marcado na figura para ser exibida a lista de perfis existentes. Localize o perfil desejado atentando para o campo do código do sistema que neste caso é D – RM Liber. Um duplo clique selecionará o perfil.

Para finalizar clique no botão OK ou SALVAR

**Importação do Layout**

Acesse o menu Utilitários | Gerador de Saídas | Layout. Se for aberta uma tela de filtros crie um filtro para retornar TODOS os registros ou simplesmente feche-a.

Clique no botão PROCESSOS | IMPORTAR LAYOUT.

Na tela que se abrirá clique no botão Adicionar Objetos e aponte para o arquivo de layout recebido e em seguida dê um duplo clique no mesmo.

Selecione o layout importado como na figura abaixo e escolha a opção de gravação para as coligadas. Na guia parâmetros informe a categoria criada anteriormente e clique no botão executar para finalizar a importação.

Sendo apresentada a tela da figura a seguir você obteve êxito na importação do layout

Feche as telas de Categorias e de Layouts.

**Geração da rotina**

Acesse o menu Rotinas Legais | Rotinas Estaduais | Apuração de ICMS – SEF II

Na tela que será apresentada clique em avançar e em seguida clique no lookup  e selecione o layout anteriormente importado.

O arquivo da rotina será gravado no diretório indicado pela seta vermelha.

Clique em avançar para ser apresentada a tela de parâmetros da rotina.

Preencha todos os parâmetros de acordo com o manual da rotina disponibilizado pela SEFAZ-PE e de acordo com o **PERFIL DA EMPRESA, tais informações devem ser verificadas com o Contador da empresa**. Os campos cujo título está em negrito são obrigatórios.

Em seguida clique em Avançar para gerar a rotina. Aguarde o término e submeta o arquivo ao validador fornecido pela SEFAZ-PE

**Para maiores informações:**

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
