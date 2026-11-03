---
content_hash: b446a4ddeaf66205688894eaabe8f1d774223dbb36c1f336d5f12c72e89ba302
fetched_at: '2026-06-29T00:09:23.802747+00:00'
page_id: '422546131'
product: rm
source: tdn-rm
title: Situação Estoque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546131
version: 3
---

* **Parâmetros do Processo**

Diretório de Leitura dos Arquivos XML: informe o diretório onde se encontram os arquivos XML a serem importados. No momento da importação todos os arquivos XML do diretório serão lidos, portanto, ao realizar o processo, no diretório só devem constar os arquivos do tipo a ser lido (Estoque Próprio ou Estoque Terceiros), não é possível a execução do processo para os tipos diferentes ao mesmo tempo.

* **Estoque Próprio**

Modelo de XML: <?xml version="1.0" encoding="utf-8"?>  
<DocumentElement>   
<ESTOQUE>   
<CODCOLIGADA>X</CODCOLIGADA>   
<CODFILIAL>X</CODFILIAL>   
<CODLOC>X</CODLOC>   
<DATAMOVIMENTO>AAAA-MM-DDT00:00:00</DATAMOVIMENTO> <CODIGOPRD>XX.XX</CODIGOPRD>   
<SALDOMOV>X</SALDOMOV>   
<TOTALMOV>X,XX</TOTALMOV> <TOTALMOVAJUSTADOITEM>X,XX</TOTALMOVAJUSTADOITEM> <CUSTOMEDMOV>X,XX</CUSTOMEDMOV>   
</ESTOQUE>   
</DocumentElement>

CODLOC: Código do Local de Estoque   
SALDOMOV: Saldo do produto   
TOTALMOV: Valor total do produto em estoque TOTALMOVAJUSTADOITEM: Informar o valor do item utilizando os critérios previstos na legislação do Imposto de Renda, especificamente artigos 292 a 297 do RIR/99 – Decreto nº 3.000/99 CUSTOMEDMOV: Custo médio do produto

* **Estoque Terceiros**

Para importação do xml é necessário marcar o check "Estoque Terceiros" na interface do processo e no xml foram acrescentados os campos Codigo do Cliente/Fornecedor, Coligada do Cliente/Fornecedor e Tipo do Estoque.

<?xml version="1.0" encoding="utf-8"?>   
<DocumentElement>   
 <ESTOQUE>   
 <CODCOLIGADA> X </CODCOLIGADA>   
 <CODFILIAL> X </CODFILIAL>   
 <CODLOC> X </CODLOC>   
 <CODCOLCFO>X</CODCOLCFO>   
 <CODCFO>XXXXXXX</CODCFO>   
 <TIPOESTOQUE>X</TIPOESTOQUE>   
 <DATAMOVIMENTO> AAAA-MM-DDT00:00:00</DATAMOVIMENTO> <CODIGOPRD> XX.XX </CODIGOPRD>   
 <SALDOMOV>X</SALDOMOV>   
 <TOTALMOV> X,XX </TOTALMOV> <TOTALMOVAJUSTADOITEM>X,XX</TOTALMOVAJUSTADOITEM> <CUSTOMEDMOV> X,XX </CUSTOMEDMOV>   
 </ESTOQUE>   
</DocumentElement>

**CODCFO**: Código do Cliente / Fornecedor   
**CODCOLCFO**: Coligada do Cliente/Fornecedor   
**TIPOESTOQUE**: Tipo do Estoque

* **Validações:**

***Observação***: Caso o usuário não tenha permissão, pela Segurança estendida por filial, em algumas das filiais indicadas no arquivo será emitida mensagem de erro e a importação não será realizada com sucesso.

* Cliente/Fornecedor deve estar cadastrado na base e "ativo".
* Tipo de Estoque deve ter os valores 1 (De Terceiros) ou 2 (Com Terceiros).  
   Os valores do tipo de estoque devem ser informados como acima e não como estão no manual do contribuinte, visto que esses valores são invertidos no sistema.  
  ***Atenção*:** O custo unitário é calculado como TOTAL/SALDO, porque para o RM Liber e para o Fisco não existe o conceito de Local de Estoque, apenas de Filial. Dessa forma, para achar o valor unitário, é somado o valor total em todos os locais da filial e dividido pelo somatório dos saldos, exemplo:

| Filial | Local | Salto | Total |
| --- | --- | --- | --- |
| 1 | 01 | 10 | 100 |
| 1 | 02 | 20 | 50 |

**Resultado**: O valor unitário nessa filial será (100 + 50) / (10 + 20) = 150 / 30 = 5  
***Observação*:** O separador decimal informado no XML deve ser o mesmo parametrizado na máquina, como ponto (.) ou vírgula (,).

Sobrepor registro de estoque: marcando esta opção, o sistema atualizará os dados já importados. Não marcando este flag, a alteração será ignorada.  
 Incluir Local de Estoque: para clientes que não possuem TOTVS Gestão de Compras, Estoque e Faturamento, foi disponibilizada a opção de incluir automaticamente no sistema o Local de Estoque informado no XML.  
 Estoque Terceiros: Permite a entrada de dados de estoque de/com terceiros.    
***ATENÇÃO!!!*** O menu Obrigações Acessórias| SPED Fiscal | Situação Estoque, só estará visível através da habilitação do parâmetro geral do TOTVS Gestão de Compras, Estoque e Faturamento "Controla Estoque Fiscal", que não está disponível para alteração. O usuário que desejar utilizar essa funcionalidade deverá entrar em contato com o Suporte Técnico para as devidas orientações.
