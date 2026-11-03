---
article_id: 360016447592
category: BI - Business Intelligence - Crystal-Reports
content_hash: c01408e372a728b048cc9b972e6c3cf4cb1cc4e4341a0dbf29eff8b2350ba69c
fetched_at: '2026-06-28T22:40:29.017605+00:00'
product: protheus
section_id: 1500001548282
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Documentação Crystal
type: support-article
updated_at: '2025-06-18T15:00:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016447592-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Documenta%C3%A7%C3%A3o-Crystal
---

*![](https://jiratdncdncontent.blob.core.windows.net/tdn/icons/time.png)* Tempo aproximado para leitura: **2****minuto****Dúvida**O que é necessário para implantar a integração ***Crystal* x Protheus**?

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – Crystal – Até a versão 11.8  
  
**Solução**

**​Obs.: Crystal Reports foi descontinuado​ ​em ​30 de junho de 2021.  
Para mais informações acesse o [Portal Ciclo de Vida de Software - Calendários](https://suporte.totvs.com/portal/p/10098/ciclodevidacalendarios).**

**Ferramenta recomendada:** [Smart View](https://tdn.totvs.com/pages/releaseview.action?pageId=626926739) 

Com a  Integração Crystal é possível expandir o poder de exibição de informações do Microsiga Protheus®, possibilitando a  utilização de todos os recursos oferecidos pela ferramenta Crystal Reports para a construção de relatórios, além de toda a facilidade oferecida pelo ERP para a parametrização e exibição, como se fossem relatórios-padrão do Sistema. 

**Procedimentos de Configuração**

**Estações de Trabalho:**

|  |  |
| --- | --- |
| • | Execute o instalador Protheus Crystal Integration.msi ou, caso a estação de trabalho já possuo o aplicativo BDE instalado, execute o Protheus Crystal Integration without BDE.msi. Este procedimento instalará os recursos necessários para proporcionar a integração entre o Microsiga Protheus® e o Crystal Reports; |

|  |  |
| --- | --- |
| • | Caso o SmartClient esteja instalado na estação, o arquivo SGCRYS32.EXE deverá ser disponibilizado no diretório de instalação e, para o caso de acesso com o SmartClient Activex, no diretório System32 do Windows. |

|  |  |
| --- | --- |
| • | Crie uma Fonte de Dados ODBC apontando para a base de dados do Microsiga Protheus®. Esta Fonte de Dados deve possuir o mesmo nome em todas as estações. |

|  |  |
| --- | --- |
| • | É possível criar essa Fonte de Dados através do Painel de Controle do Windows® acessando Ferramentas Administrativas > Fontes de Dados (ODBC). Lembrando que o tipo do driver da Fonte de Dados depende do tipo da base de dados (DBF, SQL, SERVER, etc.). Caso você esteja utilizando acesso à uma base DBF, utilize o driver Microsoft Visual FoxPro (caso exista) ou o Microsoft FoxPro Driver, ao invés do Microsoft Dbase Driver. |

 

|  |
| --- |
| Help_button Importante:  A TOTVS não distribui os drivers ODBC para os diferentes Bancos de Dados. Eles são distribuídos pelas empresas que comercializam estes bancos. Assim, caso não possua o driver ODBC para o seu banco, entre em contato com a empresa fornecedora deste Banco de Dados. |

**Servidor Protheus:**

Os procedimentos a seguir devem ser executados no servidor do Microsiga Protheus®, é necessário nível de permissão adequado ao módulo Configurador para criação de itens de menu e perguntas:

|  |  |
| --- | --- |
| • | Coloque todos os relatórios gerados pelo Crystal Reports (\*.rpt) em um só diretório logo abaixo do raiz do Microsiga Protheus®. Este diretório deve ser obrigatoriamente informado no parâmetro MV\_CRYSTAL e deve estar visível em todas as estações que têm acesso aos relatórios do Crystal Reports. |

Exemplo: \CRYSTAL\, que está abaixo do diretório Rootpath do Microsiga Protheus®.

Caso deseje utilizar parâmetros no relatório do Crystal Report da mesma maneira que no Microsiga Protheus® através do cadastro de perguntas, siga os seguintes passos:

|  |  |
| --- | --- |
| 1. | O nome do relatório criado no Crystal Reports deve ter no máximo 6 caracteres. |

|  |  |
| --- | --- |
| 2. | Crie no seu relatório Crystal Reports os parâmetros desejados, associando a eles uma condição de filtro ou uma fórmula; |

|  |  |
| --- | --- |
| 3. | No cadastro de perguntas do Microsiga Protheus® deve ser criada uma pergunta para cada parâmetro do relatório, respeitando as seguintes regras: |

O grupo de perguntas deve ser o nome do relatório sem a extensão.

As perguntas devem ser criadas na mesma ordem de criação dos parâmetros do relatório. Ou seja, as únicas ligações entre as perguntas do Microsiga Protheus® e os parâmetros do relatório são a ORDEM e o GRUPO definidos no cadastro de perguntas do Sistema. Desta forma, o primeiro parâmetro criado no relatório será preenchido pelo conteúdo informado para a pergunta de ordem 01 e assim sucessivamente.

Em instalações do Microsiga Protheus®     com mais de um STARTPATH, caso seja necessário que a geração de relatórios considere os arquivos do STARTPATH do ambiente que estiver em uso:

|  |  |
| --- | --- |
| • | Inclua a chave CRWSTARTPATH em cada ambiente, do arquivo de configuração do servidor, que será utilizado para a geração de relatórios por meio da Integração Crystal. O valor da chave deverá ser o caminho completo para o STARTPATH que esteja sendo utilizado no ambiente. |

|  |  |
| --- | --- |
| • | Veja a sessão Arquivos de Configuração deste documento. |

  
**Saiba Mais:**[Descontinuação - Crystal-Reports](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061924433)  
[Smart View](https://tdn.totvs.com/pages/releaseview.action?pageId=626926739)
