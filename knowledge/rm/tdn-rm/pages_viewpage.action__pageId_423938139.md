---
content_hash: 7abdd8bbe7a5f152b78922ac7166f2ba70a2903c829464217bd49aa3e0abddc8
fetched_at: '2026-06-29T00:09:25.415289+00:00'
page_id: '423938139'
product: rm
source: tdn-rm
title: Importação/Exportação de Tabelas de Estoque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938139
version: 5
---

As Tabelas de Estoque são as cinco [Tabelas de Classificação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938751) que podem ser parametrizadas, cadastradas e vinculadas a produtos, fabricantes, movimentos e itens de movimento, para serem utilizadas como uma classificação complementar.   
 Através da Exportação/Importação é possível extrair informações dessas tabelas que estiverem cadastradas na base de dados para um arquivo texto (.txt), assim como importar para o sistema, dados de outras bases de dados ou sistemas legados.

**Exportação**

O recurso de Exportação de Tabelas de Estoque está disponíveis através do TOTVS Business Conector. Para a utilização destes processos é necessário importar os layouts através do Gerador de Saída | Layout | Importar Layout. O Layout a ser importado "ESTLAY0015 - Exportação de Tabelas de Estoque - V1.TotvsGen" ou "ESTLAY0016 - Exportação de Tabelas de Estoque - V2.TotvsGen" se encontra na pasta de Objetos Gerenciais (C:\Totvs\CorporeRM\ObjetosGerenciais\Layout - caminho padrão ao instalar a Biblioteca RM , o qual pode variar de acordo com a escolha no momento da instalação).   
 Depois de realizar a importação do Layout, deve -se selecionar o mesmo e executar o processo "Geração de Saídas". Após a execução do processo o arquivo texto é gerado no diretório de destino informado.  
 O arquivo gerado na exportação tem como base as   de estoque (TTB1, TTB2, TTB3, TTB4, TTB5).  
 Para cada tabela é gerada uma linha identificada pelo valor fixo referente à tabela de classificação: Por exemplo, a tabela de classificação 1 tem o valor fixo "T1" em sua marca de início, seguido dos dados referentes à tabela de classificação, e assim por diante para cada tabela de classificação de estoque.  
    
  **Importação**

Para realizar a importação de Tabelas de Estoque é necessário incluir um novo conceito através do TOTVS Business Conector | Conceito, tecla CRTL + botão Incluir ou através do processo "Importar Conceito".   
O Conceito a ser importado "CONEST0011 - Importação Tabelas de Estoque - V1.concept" ou "CONEST0012 - Importação Tabelas de Estoque - V2.concept" se encontra na pasta Objetos Gerenciais (C:\Totvs\CorporeRM\ObjetosGerenciais\Conceito - caminho padrão ao instalar a Biblioteca RM, o qual pode variar de acordo com a escolha no momento da instalação).  
Após a inclusão, deve-se o conceito e selecionar o arquivo texto a ser importado através da opção "Tabela de Estoque", botão Editar. Após salvar as configurações, selecione o conceito e execute o processo "Processar Novo Conceito".  
Após a execução do processamento do Conceito, os dados das [Tabelas de Classificação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938751) de estoque (TTB1, TTB2, TTB3, TTB4, TTB5) são atualizados de acordo com os dados contidos no arquivo texto de importação informado dentro do Conceito.

**Layout do Arquivo Texto (.txt)**

O layout do arquivo texto é o mesmo tanto na exportação via [Gerador de Saídas](http://tdn.totvs.com/pages/viewpage.action?pageId=237383341) como na importação via [Conceito](http://tdn.totvs.com/display/LRM/Conceito+-+Como+parametrizar), sendo possível utilizar a Versão de Layout 1 (V1) ou a Versão de Layout 2 (V2), conforme abaixo:  
    
  **Layout V1**  
    
 **Tabela de Estoque 1 (TTB1)**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo do Campo** | **Descrição** |
| Marca de Início | 2 | 1 | CARACTER | T1 |
| CODTB1FAT | 10 | 3 | CARACTER | Código Tabela de Classificação 1 Produto |
| DESCRICAO | 40 | 13 | CARACTER | Descrição |
| COMISSAO | 10 | 53 | VALOR | Comissão |
| CAMPOLIVRE | 20 | 63 | CARACTER | Campo Livre |

**Tabela de Estoque 2 (TTB2)**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo do Campo** | **Descrição** |
| Marca de Início | 2 | 1 | CARACTER | T2 |
| CODTB2FAT | 10 | 3 | CARACTER | Código Tabela de Classificação 2 Produto |
| DESCRICAO | 40 | 13 | CARACTER | Descrição |
| COMISSAO | 10 | 53 | VALOR | Comissão |
| CAMPOLIVRE | 20 | 63 | CARACTER | Campo Livre |

**Tabela de Estoque 3 (TTB3)**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo do Campo** | **Descrição** |
| Marca de Início | 2 | 1 | CARACTER | T3 |
| CODTB3FAT | 10 | 3 | CARACTER | Código Tabela de Classificação 3 Produto |
| DESCRICAO | 40 | 13 | CARACTER | Descrição |
| COMISSAO | 10 | 53 | VALOR | Comissão |
| CAMPOLIVRE | 20 | 63 | CARACTER | Campo Livre |

**Tabela de Estoque 4 (TTB4)**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo do Campo** | **Descrição** |
| Marca de Início | 2 | 1 | CARACTER | T4 |
| CODTB3FAT | 10 | 3 | CARACTER | Código Tabela de Classificação 4 Produto |
| DESCRICAO | 40 | 13 | CARACTER | Descrição |
| COMISSAO | 10 | 53 | VALOR | Comissão |
| CAMPOLIVRE | 20 | 63 | CARACTER | Campo Livre |

**Tabela de Estoque 5 (TTB5)**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo do Campo** | **Descrição** |
| Marca de Início | 2 | 1 | CARACTER | T5 |
| CODTB3FAT | 10 | 3 | CARACTER | Código Tabela de Classificação 5 Produto |
| DESCRICAO | 40 | 13 | CARACTER | Descrição |
| COMISSAO | 10 | 53 | VALOR | Comissão |
| CAMPOLIVRE | 20 | 63 | CARACTER | Campo Livre |

**Layout V2**  
    
 **Tabela de Estoque 1 (TTB1)**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo do Campo** | **Descrição** |
| Marca de Início | 2 | 1 | CARACTER | T1 |
| CODTB1FAT | 10 | 3 | CARACTER | Código Tabela de Classificação 1 Produto |
| DESCRICAO | 100 | 13 | CARACTER | Descrição |
| COMISSAO | 20 | 113 | VALOR | Comissão |
| CAMPOLIVRE | 20 | 133 | CARACTER | Campo Livre |

**Tabela de Estoque 2 (TTB2)**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo do Campo** | **Descrição** |
| Marca de Início | 2 | 1 | CARACTER | T2 |
| CODTB1FAT | 10 | 3 | CARACTER | Código Tabela de Classificação 2 Produto |
| DESCRICAO | 100 | 13 | CARACTER | Descrição |
| COMISSAO | 20 | 113 | VALOR | Comissão |
| CAMPOLIVRE | 20 | 133 | CARACTER | Campo Livre |

**Tabela de Estoque 3 (TTB3)**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo do Campo** | **Descrição** |
| Marca de Início | 2 | 1 | CARACTER | T3 |
| CODTB1FAT | 10 | 3 | CARACTER | Código Tabela de Classificação 3 Produto |
| DESCRICAO | 100 | 13 | CARACTER | Descrição |
| COMISSAO | 20 | 113 | VALOR | Comissão |
| CAMPOLIVRE | 20 | 133 | CARACTER | Campo Livre |

**Tabela de Estoque 4 (TTB4)**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo do Campo** | **Descrição** |
| Marca de Início | 2 | 1 | CARACTER | T4 |
| CODTB1FAT | 10 | 3 | CARACTER | Código Tabela de Classificação 4 Produto |
| DESCRICAO | 100 | 13 | CARACTER | Descrição |
| COMISSAO | 20 | 113 | VALOR | Comissão |
| CAMPOLIVRE | 20 | 133 | CARACTER | Campo Livre |

**Tabela de Estoque 5 (TTB5)**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Campo** | **Tamanho** | **Posição Inicial** | **Tipo do Campo** | **Descrição** |
| Marca de Início | 2 | 1 | CARACTER | T5 |
| CODTB1FAT | 10 | 3 | CARACTER | Código Tabela de Classificação 5 Produto |
| DESCRICAO | 100 | 13 | CARACTER | Descrição |
| COMISSAO | 20 | 113 | VALOR | Comissão |
| CAMPOLIVRE | 20 | 133 | CARACTER | Campo Livre |

***Atenção!*** No caso da importação, o processo é realizado pelo módulo Integração | Conceito. E para a exportação pelo módulo Integração | Gerador de Saídas para as exportações.
