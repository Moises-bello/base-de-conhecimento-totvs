---
article_id: 360050971233
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: c47892aded73d64454bcead788136ea770d69c62cac3156e9070507537b2061b
fetched_at: '2026-06-28T22:42:05.269888+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - PIS COFINS Substituição Tributária para Fabricantes de Cigarros
type: support-article
updated_at: '2023-01-04T18:11:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050971233-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-PIS-COFINS-Substitui%C3%A7%C3%A3o-Tribut%C3%A1ria-para-Fabricantes-de-Cigarros
---

**Dúvida**PIS COFINS Substituição Tributária para Fabricantes de Cigarros  
   
 **Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Implementado o tratamento de **Substituição Tributária para PIS e COFINS** para fabricantes e importadores de cigarros e cigarrilhas, considerando o percentual/coeficiente definido pela Receita Federal para este ramo de atividade, sendo adicionado a opção **“Aglutina Obrigação?”** que tem o objetivo de permitir ao usuário aglutinar as informações de duas ou mais filiais por CNPJ + Inscrição Estadual.

Para esta instrução normativa, se a mesma**codificação de produtos** (campo **B1\_COD** do Cadastro de Produtos)  for repetida em mais de uma filial que foi processada de forma aglutinada, **somente o primeiro registro** será enviado.

|  |
| --- |
| **Importante**  A seleção de filiais estará disponível apenas para as filiais dentro do mesmo grupo de empresas corrente.  A nova pergunta **“Aglutina Obrigação?”** somente terá funcionalidade se a pergunta **“Seleciona Filiais?”** estiver configurada com conteúdo igual a “Sim”.  A nova pergunta somente terá funcionalidade para ambientes **dbAccess**.  Quando permitida a seleção de filiais, a janela de seleção de filiais será ordenada por CNPJ + I.E. + I.M. + código da filial.  Para utilizar a aglutinação das informações o cliente deverá consultar seu departamento jurídico para verificar se o seu ramo de atividade permite tal aglutinação.  Para esta funcionalidade, é imprescindível que as tabelas de documentos fiscais (família ‘SF????’) estejam configurados com compartilhamento **EXCLUSIVO** em todos os níveis. |

**Procedimento para Implementação**

Como esse processo trata de uma validação de dados para o SPED Fiscal, os procedimentos de implementação são os mesmos. Portanto, para verificar a necessidade de configurações de parâmetros, dicionários e menus, acesse o Portal do Cliente e consulte o boletim FIS – SPED FISCAL.

1. Copie o arquivo de configuração **DEC5035013.INI** para o diretório **\SYSTEM** (diretório padrão do sistema).

## **Procedimento para Configuração**

1. No **Configurador (SIGACFG)**, acesse **Base de dados/Dicionários/Base de dados**, configure / crie os campos a seguir:

* Tabela **SB1 – Cadastro de Produto**

|  |  |
| --- | --- |
| **Tabela** | SB1 |
| **Campo** | <critério do cliente> |
| **Exemplo** | B1\_PPSSTCG |
| **Tipo** | Numérico |
| **Tamanho** | 8 |
| **Decimais** | 4 |
| **Formato** | @E 999.9999 |
| ***Help*** | Informar o coeficiente de PIS que será utilizado no cálculo da Substituição tributária para fabricantes de cigarros. |

|  |  |
| --- | --- |
| **Tabela** | SB1 |
| **Campo** | <critério do cliente> |
| **Exemplo** | B1\_PCFSTCG |
| **Tipo** | Numérico |
| **Tamanho** | 8 |
| **Decimais** | 4 |
| **Formato** | @E 999.9999 |
| ***Help*** | Informar o coeficiente da COFINS que será utilizado no cálculo da Substituição tributária para fabricantes de cigarros. |

|  |  |
| --- | --- |
| **Tabela** | SB1 |
| **Campo** | <critério do cliente> |
| **Exemplo** | B1\_PUPCCST |
| **Tipo** | Numérico |
| **Tamanho** | 8 |
| **Decimais** | 4 |
| **Formato** | @E 999.9999 |
| ***Help*** | Preço Unitário de venda a varejo para o cálculo de PIS e COFINS por Substituição Tributária. |

Os campos criados na tabela SB1 deverão ser criados também na tabela SS4, para que o Histórico Fiscal seja gravado, contemplando estes campos também. Deverão ser criados com as mesmas propriedades, alterando somente o prefixo do nome, ou seja, ao invés de **B1\_** cria-se com **S4\_**.

**Configuração de TES:**

* Campo **PIS/COFINS (F4\_PISCOF)** igual a 4= Não Considera
* Campo **Cred.PIS/COF (F4\_PISCRED)** igual a 4= Calcula
* Campo **Sit. Trib. PIS (F4\_CSTPIS)** igual a 05
* Campo **Sit. Trib. COF (F4\_CSTCOF)** igual a 05
* Campo **PIS/COF ST (F4\_PSCFST)** igual a 1= Sim
* Campo **Tp Reg (F4\_TPREG)** igual a 2= Cumulativo
* A TES deve estar configurada para gravar no livro (SFT)

No caso de Operação Tributável por Substituição Tributária a Alíquota zero, alguns campos deverão ser alterados com a seguinte configuração:

* **PIS/COFINS (F4\_PISCOF)** igual a 3= Ambos

* **Cred.PIS/COF (F4\_PISCRED)** igual a 3= Não Calcula

* **PIS/COF ST (F4\_PSCFST)** igual a 3= Aliq. Zero

Essa configuração deverá ser feita apenas quando a alíquota aplicável for igual à zero (casos de revenda de produtos sujeitos à substituição tributária).

**Configuração de Produto:**

* Campo **Per. PIS igual (B1\_PPIS)** deve ser igual a 0,65
* Campo **Perc. COFINS (B1\_PCOFINS)** deve ser igual a 3
* Campo Pos. IPI/NCM deve constar um NCM correspondente a cigarros, por exemplo, 2402.20.00
* Crie um campo para informar o percentual de PIS para Substituição Tributária, informe neste campo o valor igual a 3,42 e informe este campo criado manualmente no configurador através parâmetro **MV\_B1CPSST**
* Crie um campo para informar o percentual da COFINS para Substituição Tributária, informe neste campo o valor igual a 2,9169 e informe este campo criado manualmente através configurador no parâmetro **MV\_B1CCFST**
* Crie um campo para informar o preço unitário do cigarro referente à venda a varejo. Este valor unitário é utilizado para obter o valor de venda a varejo, que será utilizado no cálculo da Substituição Tributária do PIS e COFINS. Informe este campo criado manualmente através do configurador no parâmetro **MV\_PUPCCST**

**Configuração da Exceção Fiscal:**

* O valor do preço unitário de venda a varejo do cigarro também poderá ser informado na Exceção Fiscal, no campo **Vl.unitário PIS COFINS/ST****(F7\_PRCUNIC)**. O valor do preço unitário de cigarro informado neste campo terá maior prioridade do que o informado no campo do parâmetro **MV\_PUPCCST**

## **Procedimentos para Utilização**

**Sobre Cigarros e Cigarrilhas – Substituição Tributária**

Para fabricantes e importadores de cigarros/cigarrilhas, o valor das contribuições de PIS e COFINS na condição de contribuintes e substitutos são calculados multiplicando-se o preço de venda do produto no varejo pelos percentuais definidos pela Receita Federal, que são 3,42% para PIS e 2,9169% para COFINS. Segue um exemplo de como será o cálculo:

Uma venda onde o preço unitário de venda no varejo seja R$ 5,00, e quantidade de 10.000 unidades, totalizando um valor de R$ 50.000,00, o cálculo ficará da seguinte forma:

**PIS**

* Base de cálculo do PIS: R$ 50.000,00 \* 3.42 = R$ 171.000,00
* Valor do PIS: R$ 171.000,00 \* 0,65% = R$ 1.111,50

**COFINS**

* Base de cálculo da COFINS: R$ 50.000,00 \* 2,9169 = R$ 145.845,00
* Valor da COFINS: R$ 145.845,00 \* 3% = R$ 4.375,35

Nesta venda, o contribuinte paga R$ 1.111,50 de PIS e R$ 4.375,35 de COFINS, e neste caso de cigarros e cigarrilhas, não há cálculo de PIS e COFINS via apuração, somente via Substituição Tributária.

Com a configuração descrita neste boletim, a nota de saída utilizando Produto e TES configurados será escriturada considerando os percentuais/coeficientes para o ramo de cigarro, e os valores são considerados para o SPED PIS COFINS, lembrando que estes valores estão sujeitas à apuração das contribuições no regime cumulativo.

Os percentuais para cálculo da Substituição Tributária de PIS e COFINS informados no cadastro de produtos são gravados nos campos **Coef.****PIS ST (FT\_COEPSST)** e **Coef. COF ST (FT\_COECFST)**, respectivamente.

O preço unitário utilizado para obter o valor de venda a varejo, é o valor do campo informado no parâmetro **MV\_PUPCCST,**ou o preço informado no campo **Vl.unitário PIS COFINS/ST****(F7\_PRCUNIC)** da Exceção Fiscal, porémcaso não seja informado este valor unitário, a rotina considera o valor unitário da própria operação de venda para o cálculo da Substituição Tributária de PIS e COFINS para este ramo.

## **Decreto 50.350 de 2013**

Conforme Decreto 50.350/2013, o estabelecimento industrial deverá remeter, após qualquer alteração de preços de cigarro, a listagem de preços de venda ao consumidor fixado pelo fabricante, através de um arquivo em formato texto, com *layout*definido no próprio decreto.

Para geração desta listagem, serão considerados o cadastro de produto e o cadastro de exceção fiscal.

A geração deste arquivo tem como pré requisito a versão do ERP ser igual ou superior a **11.80**, pois irá considerar a nova funcionalidade de **Histórico Fiscal** das tabelas SB1 e SF7 para poder gerar este arquivo, ou seja, caso a versão for inferior a **11.80**, o arquivo não será processado. A tabela de histórico do produto SB1 é a SS4, e a tabela de histórico da exceção fiscal SF7 é a SS1.

Para habilitar o tratamento do **Histórico Fiscal**, deverá alterar o parâmetro **MV\_HISTFIS** e colocar .T. para que o histórico fiscal passe a gravar as alterações. Lembrando que esta funcionalidade está disponível somente a partir da versão **11.80.**

O arquivo será processado através de arquivo .ini **DEC5035013.INI**, deverá então ser processado pela rotina de **Instrução Normativas** ( **MATA950**). Ao gerar o arquivo, serão exibidas perguntas para informar produto inicial e produto final que serão considerados no processamento do arquivo. Como no arquivo não existe tratamento de período, ao processar o arquivo, serão consideradas as alíquotas atuais, como pede o decreto, sempre que houver alteração deverá gerar este arquivo com listagem do preço de cigarro.

**Configuração do Cadastro de Produto:**

Para o cadastro de produto, serão considerados os produtos que tenham valor maior que zero no campo criado manualmente e informado no parâmetro **MV\_PUPCCST.**Como o campo com valor de preço no cadastro de produto é criado manualmente, o usuário deverá cadastrar manulamente também na tabela de histórico do produto SS4 o mesmo campo, com as mesmas propriedades, alterando somente o início do nome com S4\_ ao invés de B1\_.

Exemplo: Se foi criado campo **B1\_PUPCCST na SB1**, então deverá criar também o campo **S4\_PUPCCST na SS4**.

Abaixo, *layout* do arquivo com origem das informações quando processar produtos (SB1):

|  |  |  |
| --- | --- | --- |
| 1 | CNPJ | Cadastro SIGAMAT |
| 2 | COD | Código do Produto |
| 3 | GTIN | Não é gerado |
| 4 | DESCR | Descrição do Cadastro de Produto |
| 5 | UF | Conteúdo do parâmetro **MV\_ESTADO** |
| 6 | PRECO | Conteúdo do campo da SB1 informado no parâmetro **MV\_PUPCCST** |
| 7 | INIC\_TAB | Data do Histórico Fiscal, tabela **SS4** |
| 8 | INIC\_TAB ANTERIOR | Data do Histórico Fiscal, tabela **SS4** |

**Configuração da Exceção Fiscal:**

Paraexceção fiscal, serão considerados os lançamentos onde o campo **F7\_PRCUNIC** for maior que zero. O campo correspondente **S1\_PRCUNIC**na tabela de históricoserá criado através do compatibilizador u\_updsigafis. Quando processar lançamentos da Exceção Fiscal, serão considerados todos os produtos atrelados ao grupo de tributação da Exceção Fiscal.

Abaixo, *layout* do arquivo com origem das informações quando processar produtos atrelados ao grupo de tributação da Exceção Fiscal(SF7):

|  |  |  |
| --- | --- | --- |
| 1 | CNPJ | Cadastro SIGAMAT |
| 2 | COD | Código do Produto |
| 3 | GTIN | Não é gerado |
| 4 | DESCR | Descrição do Cadastro de Produto |
| 5 | UF | Conteúdo do campo **F7\_EST** |
| 6 | PRECO | Conteúdo do campo **F7\_PRCUNIC** |
| 7 | INIC\_TAB | Data do Histórico Fiscal, tabela **SS1** |
| 8 | INIC\_TAB ANTERIOR | Data do Histórico Fiscal, tabela **SS1** |

Quando houver exceção fiscal com regra válida para todos os Estados, ou seja, campo F7\_EST igual a “\*\*”, serão geradas informações para todos os Estados (uma linha para cada estado).

Após habilitar o **Histórico Fiscal,**astabelas de histórico não estarão preenchidas, somente serão preenchidas quando houver alguma alteração. Para geraração do arquivo, serão considerados as lançamentos que tem históricos de alteração gravado.

Caso um produto tenha valor do preço informado na SB1 e também na exceção Fiscal, é realizado um filtro para não duplicar registros, considerando código do produto, data inicial e UF.
