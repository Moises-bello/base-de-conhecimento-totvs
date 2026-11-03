---
content_hash: 94fd108e909ac442931160acb447a63f1216ae395fab7060e55912f866185b0c
fetched_at: '2026-06-29T00:09:24.698803+00:00'
page_id: '423938000'
product: rm
source: tdn-rm
title: Importação de Contagem via Arquivo Texto - Inventário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938000
version: 3
---

Para utilizar o processo de Importação de Contagem via arquivo texto para o [inventário](http://tdn.totvs.com/pages/viewpage.action?pageId=423937977) é necessário incluir um novo conceito através do TOTVS Business Conector |  [Conceito](http://tdn.totvs.com/display/LRM/Conceito+-+Como+parametrizar), tecla CRTL + botão Incluir ou através do processo "Importar Conceito".   
 O Conceito a ser importado "CONEST0010 - Importação de Contagem de Concentracionário" se encontra na pasta Objetos Gerenciais (C:\Totvs\CorporeRM\ObjetosGerenciais\Conceito - caminho padrão ao instalar a Biblioteca RM, o qual pode variar de acordo com a escolha no momento da instalação).  
 Após a inclusão, edite o conceito e selecione o arquivo texto a ser importado através da opção "Contagem de Inventário", botão Editar. Após salvar as configurações, selecione o conceito e execute o processo "Processar Novo Conceito".

**Somar Contagens de Itens Repetidos**

Ao executar o processo "Processar Novo Conceito" é apresentada a opção "Deseja somar as contagens em caso de itens repetidos?", ao marcar o checkbox nessa etapa, se existirem itens repetidos no arquivo texto, ou seja, mais de uma linha com os mesmos dados, as contagens serão somadas para o itens iguais.  
 Importante: Nesse caso, se já houver alguma informação previamente cadastrada no Item do Inventário, as quantidades do arquivo serão somadas as quantidades já informadas no Inventário.    
 Caso a opção "Somar as contagens em caso de itens repetidos" não esteja marcada, o sistema vai considerar apenas a última contagem informada no arquivo de importação.

**Layout de importação do arquivo texto de contagem**

|  |  |  |  |
| --- | --- | --- | --- |
| CAMPO | POSIÇÃO | TAMANHO | TIPO |
| CODCOLIGADA | 1 | 5 | SMALLINT |
| CODINVENTARIO | 6 | 15 | VARCHAR |
| CODIGOPRD | 21 | 30 | VARCHAR |
| CODFILIAL | 51 | 5 | SMALLINT |
| CODLOC | 56 | 15 | VARCHAR |
| CONTAGEM1 | 71 | 15 | NUMERO (10.4) |
| CONTAGEM2 | 86 | 15 | NUMERO (10.4) |
| CONTAGEM3 | 101 | 15 | NUMERO (10.4) |
| GERARACERTO | 116 | 1 | SMALLINT |
| GRADE | 117 | 20 | VARCHAR |
| IDENTIFICADOR GRADE | 137 | 5 | NUMERO |
| NUMERO LOTE | 142 | 50 | VARCHAR |
| CODIGO BARRA | 192 | 60 | VARCHAR |
| NUMERO SERIE | 252 | 30 | VARCHAR |

***Observações*:**

* Para realizar a importação através do código de barra do produto é necessário que o código do produto não seja informado no layout.
* Os campos do tipo VARCHAR são preenchidos com brancos após a informação da esquerda para a direita.
* Os campos dos tipos SMALLINT e NUMBER são preenchidos com brancos antes da informação da esquerda para a direita.
* Os campos NUMBER devem ter o ponto como separador decimal e não a vírgula. Ex: o número 10 deverá estar preenchido como 10.0000 e não como 10,0000.
* O campo GERAACERTO poderá conter somente os valores:
  + 1: o item de inventário terá o campo GERAACERTO marcado.
  + 0: o item de inventário não terá o campo GERAACERTO marcado.

***Atenção!*** No caso da importação, o processo é realizado pelo módulo Integração | Conceito. E para a exportação pelo módulo Integração | Gerador de Saídas para as exportações.
