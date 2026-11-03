---
content_hash: 2802205928ea037a78bf5e46162c375c75e9b2aff890f3a9e54dbababcb1e3a3
fetched_at: '2026-06-29T00:09:35.418617+00:00'
page_id: '425459347'
product: rm
source: tdn-rm
title: Transformação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459347
version: 2
---

**Transformação**

---

O recurso Transformação é destinado à inclusão de mensagens de transformação (XSLT) utilizadas nas integrações dos produtos de origens diferentes, como por exemplo a integração BackOffice Protheus x Totvs Obras e Projetos.  
    
 Com o objetivo de padronizar as integrações com os produtos TOTVS, foi definida uma nova diretriz para os projetos de integração: A de que todos os produtos TOTVS devam trabalhar com uma mensagem XML única, evitando desta forma o processo de transformação de mensagens.   
    
 Esta mensagem única definida deve ser convertida para o modelo da Linha RM ou vice-versa. Com isso, é necessário armazenar os XMLs responsáveis pelas transformações destas mensagens, que são os XSLTs (uma linguagem de marcação XML usada para transformar documentos XML).  
    
  **Informações técnicas**  
     
 A tabela HCTRANSFORMACAO é utilizada para armazenar os dados referentes aos XMLs e os XLSTs. Seguem descrições dos campos da tabela.  
  

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| DataServer | Lista de Dataserver que serão utilizados para manipulas os dados da mensagem padrão |
| Id | Identificador do registro de transformação |
| Versão | Versão da mensagem |
| XSLT Saída | Mensagem de conversão para o modelo padrão |
| XSLT Entrada | Mensagem de conversão para o modelo RM |
| XSD | Estrutura da mensagem padrão |

   
 A visão é composta pelas abas:

* **Identificação:** Possui campos para identificação do dado a ser transformado.

São eles:

* **Data Server**
* **ID**
* **Versão**
* **XSLT Saída**
* **XSLT Entrada**
* **XSD**
* **XSLT Saída:** Apresenta o texto XSLT de Saída.
* **XSLT Entrada:** Apresenta o texto XSLT de Entrada.
* **XSD:** Apresenta o texto XSD correspondente.

   
 **Descrição dos parâmetros de Atividade**

* **Nome:** Nome da atividade, de caráter de organização da Fórmula Visual.
* **Descrição:** Breve descrição sobre a utilidade da atividade no contexto da Fórmula Visual.
* **DataSet:** DataSet com as informações de entrada da atividade.
* **TransactionID:** Id da transformação a ser utilizada pela atividade.
