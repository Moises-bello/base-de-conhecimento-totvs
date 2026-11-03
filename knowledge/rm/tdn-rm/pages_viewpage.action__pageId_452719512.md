---
content_hash: c5d80bea658c65a69e07f898eb8f0684a5e8295ce667831052c4e3f73278607e
fetched_at: '2026-06-29T00:10:08.111669+00:00'
page_id: '452719512'
product: rm
source: tdn-rm
title: Importação de Fornecimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719512
version: 80
---

**Importação de Fornecimento**

Importar via SQL ou arquivo TXT para o RM os EPIs emprestados de sistema externo.

**Arquivo texto**

Ao selecionar arquivo texto será aberto o campo para busca apenas de arquivo do tipo texto. O arquivo texto deverá atender às seguintes regras:

* Conter os seguintes campos separados por ponto e virgula ( ; ):  
                CODCOLIGADA;CODEPI;IDLOTE;DATAEMPRESTIMO;   
                CHAPA;QTD;CA;DATAVALIDADE;DATAVALIDADECA;   
                IDEPIEXTERNO;DURABILIDADE;DTDURABILIDADE;
* Tipo e tamanho dos campos

  |  |  |  |
  | --- | --- | --- |
  | CODCOLIGADA | int | não nulo |
  | CODEPI | string(10) | não nulo |
  | IDLOTE | int | não nulo |
  | DATAEMPRESTIMO | datetime | não nulo |
  | CHAPA | string(16) | não nulo |
  | QTD | int | não nulo |
  | CA | string(30) |  |
  | DATAVALIDADE | datetime |  |
  | DATAVALIDADECA | datetime |  |
  | IDEPIEXTERNO | string(255) | não nulo |
  | DURABILIDADE | int |  |
  | DTDURABILIDADE | datetime |  |
* Formatos aceitos para campos de data:  
      DD/MM/AAAA  
      AAAA-MM-DD

Exemplo de um arquivo válido com 3 fornecimentos:  
1;EPI01;123;22/11/2017;123;1;abc123;01/01/2018;01/01/2018;asdfg123;1;01/01/2018;  
1;EPI02;123;23/11/2017;456;1;abc123;01/01/2018;01/01/2018;asdfg123;0;;  
1;EPI5;123;23/11/2017;489;1;;;;asdfg123;;;  
   
   
**Consulta SQL**   
   
Ao selecionar o processo para realizar via consulta SQL, caso no parametrizador já tenha uma consulta SQL padrão informada, automaticamente o processo irá carregá-la. Caso desejar uma outra consulta pode ser selecionada.   
   
A consulta deverá atender às seguintes regras:

* Retornar os seguintes campos:  
     
                CODCOLIGADA, CODEPI, IDLOTE, DATAEMPRESTIMO,   
                CHAPA, QTD, CA, DATAVALIDADE, DATAVALIDADECA,    
                IDEPIEXTERNO, DURABILIDADE, DTDURABILIDADE, IDEMPRESTIMO
* Conter estes 4 parâmetros nesta ordem:  
     
                :CODCOLIGADA   
                :CHAPA  
                :DTINICIO   
                :DTFINAL
