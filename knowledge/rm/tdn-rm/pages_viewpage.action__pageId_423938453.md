---
content_hash: 1b35423cd6e20e5d159e13db4ac7674adfd6186db743ef0b655d7abe734bdbea
fetched_at: '2026-06-29T00:09:27.203096+00:00'
page_id: '423938453'
product: rm
source: tdn-rm
title: Importação de Informações para o RAS 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938453
version: 5
---

Este processo possibilita ao usuário realizar a importação das informações que irão compor o RAS.

* **Informação a ser importada:** Aqui o usuário escolhe qual a informação que será importada. Existem três opções:

         - Identificadores dos itens do RAS / Reconhecimento inicial;  
         - Realizações dos itens do RAS;  
         - Detalhamento do RAS.   
   
A importação será realizada através de arquivo de texto.txt que deve ser estruturado conforme um layout pré-definido.

* **Delimitador de Campos:** As informações deste arquivo devem ser separadas por um caractere que irá representar o separador, e como default o sistema define como separador o ";", mas este separador poderá ser alterada pelo usuário durante a execução do processo.
* **Campo do identificador do item que será considerado como chave?:**O usuário deverá definir qual campo do Item do RAS será considerado como chave para localizar informações já cadastradas no banco de dados, isto se faz necessário quando é realizado uma importação na qual o sistema deverá apenas alterar um registro já cadastrado. Exemplo: importação de um arquivo com informações referentes a realizações do item. Existem duas opções para escolha do usuário:

         - Identificador do item do RAS;  
         - Código do Patrimônio.  
   
**LAYOUTS PARA PARAMETRIZAÇÃO**

- Identificadores dos itens do RAS / Reconhecimento inicial:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Observação** | **Tamanho** | **Obrigatório** |
| **1** | Código do Patrimônio |  | 10 | X |
| **2** | Identificador do Item |  | 30 | X |
| **3** | Descrição do Item |  | 50 | X |
| **4** | CNPJ da Investida |  | 20 |  |
| **5** | Data do Reconhecimento Inicial | Formato DD/MM/YYYY | 10 |  |
| **6** | Valor do Reconhecimento Inicial |  |  |  |
| **7** | Indicador do Valor | D ou C | 1 |  |
| **8** | Quantidade |  | 10 |  |

- Realizações dos itens do RAS:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Observação** | **Tamanho** | **Obrigatório** |
| **1** | Código do Patrimônio |  | 10 | X |
| **2** | Identificador do Item |  | 30 | X |
| **3** | Data da Realização | Formato DD/MM/YYYY | 10 | X |
| **4** | Valor da Realização |  |  | X |
| **5** | Indicador do Valor da Realização | D ou C | 1 | X |
| **6** | Complemento |  | 50 |  |

- Detalhamento do RAS:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Observação** | **Tamanho** | **Obrigatório** |
| **1** | Código do Patrimônio |  | 10 | X |
| **2** | Identificador do Item |  | 30 | X |
| **3** | Código da Subconta | A conta deve estar como uma Subconta correlata no sistema. | 40 |  |
| **4** | Código do C. Custo |  | 25 |  |
| **5** | Valor a Débito na Subconta |  |  |  |
| **6** | Valor a Crédito na Subconta |  |  |  |
| **7** | Identificador da Partida | Caso seja informado a partida, a mesma deve estar cadastrada na sistema , caso contrário, após a importação o usuário poderá editar o detalhamento e informar a partida manualmente. |  |  |
| **8** | Identificador do Detalhamento | D ou C |  | x |

Veja também
