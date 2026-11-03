---
content_hash: a3479c798de92ba9a6d331b839cefe5986733d476ad232d687857c0981fcd823
fetched_at: '2026-06-29T00:09:24.084545+00:00'
page_id: '423937885'
product: rm
source: tdn-rm
title: Exportação Instrução Normativa 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937885
version: 5
---

Através processo de Exportação de Instrução Normativa serão gerados arquivos que deverão ser apresentados a Receita Federal em cumprimento as normas 068/95, 86/2002 e 89/2003.  
 Para a utilização deste recurso será necessário importar o layout através do [TOTVS Business Conector](http://tdn.totvs.com/display/LRM/Novo+Conceito+TOTVS+Business+Conector) | [Gerador de Saída](http://tdn.totvs.com/pages/viewpage.action?pageId=425459363), selecione o layout e clique em Processos | Geração de Saídas.    
No assistente de Geração de Saídas deverão ser preenchidos os seguintes parâmetros:

**Tipos de operação:** Estoque, Inventário e Listagem

**Período Inicial e Período Final:** deverão ser obrigatoriamente preenchidos para geração de Estoque.

**Data Inventário:** deverá ser obrigatoriamente preenchido para geração do arquivo de Inventário.

I**nstrução Normativa:** Selecione a instrução normativa pela qual deverão ser gerados os arquivos.

**Filial:** Escolha a filial que o sistema deverá buscar os dados para gerar os arquivos.

**Meio Magnético:** Informe de que maneira serão entregues os arquivos. As opções são: Disco Flex. 51/4, Disco Flex. 31/2, Outros.

**Equipamento:** Qual o nome do Fabricante e modelo do equipamento utilizado para gerar os arquivos.

**Densidade Gravação:** Qual a densidade da gravação. Deve-se utilizar sempre discos de densidade alta.

**Sistema Operacional:** Informe o nome da versão e utilitário de gravação.

**Gera Dump:**  Serão gerados os 30 primeiros e 30 últimos registros de cada arquivo exportado.  
  
 Após preencher os parâmetros para geração de saída, clique em Executar. Serão gerados os seguintes arquivos.

* **Estoque:** ESTOQUE.TXT  - Arquivo de Controle de Estoque.
* **Inventario:** INVENTAR.TXT - Arquivo de Registro de Inventário
* **Listagem:** LISTAGEM.TXT

**Arquivos de DUMP:**

* D1ESTOQU.TXT - Dump dos 30 primeiros registros do arquivo ESTOQUE.TXT
* D2ESTOQU.TXT - Dump dos 30 últimos registros do arquivo ESTOQUE.TXT
* D1INVENT.TXT - Dump dos 30 primeiros registros do arquivo INVENTAR.TXT
* D2INVENT.TXT - Dump dos 30 últimos registros do arquivo INVENTAR

***Observação*:**Os arquivos contendo Entradas, Saídas e Cadastros serão exportados através do [TOTVS Gestão Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=198948859).

***Atenção!*** No caso da importação, o processo é realizado pelo módulo Integração | Conceito. E para a exportação pelo módulo Integração | Gerador de Saídas para as exportações.

Informações Adicionais

* [Boletim Técnico -](http://tdn.totvs.com/download/attachments/185734021/MOV_BT_Importa%C3%A7%C3%A3o%20de%20Movimentos_BRA_PCREQ-2461.pdf?version=1&modificationDate=1424884082000&api=v2) [Exportação Instrução Normativa](http://tdn.totvs.com/pages/viewpage.action?pageId=423937885)
