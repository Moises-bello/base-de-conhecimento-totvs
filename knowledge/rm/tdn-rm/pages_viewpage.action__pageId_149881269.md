---
content_hash: e6e46a6fcea919cf60ccd81865381a4a6a36e59cf1985e190e827b1b775869fc
fetched_at: '2026-06-29T00:05:56.020306+00:00'
page_id: '149881269'
product: rm
source: tdn-rm
title: Dicas para facilitar a importação de PIS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149881269
version: 2
---

**Dicas para facilitar a importação de PIS**

Para otimizar o seu tempo e facilitar os procedimentos em relação ao **PIS EMPRESA**, foi criado o seguinte roteiro de dicas:

**Passo 1:**Instale o programa **SXPIS** fornecido pela C.E.F.

**Passo 2:**  
 Busque na agência conveniada com a empresa, o disquete contendo as informações necessárias para o pagamento do PIS EMPRESA.  
 No disquete terá um arquivo com o formato numérico.   
  **Exemplo:**  
 "12345678.912"   
   
 **Passo 3:**  
 Acesse o programa SXPIS e importe o arquivo:  
   
   
   
 **Passo 4:**  
 Libere os Recursos. Assim, após a "Liberação de Recursos" será gerado dentro do diretório **C:\CAIXA**, um arquivo texto com o mesmo nome do arquivo fornecido pela C.E.F. De acordo com o exemplo mencionado no *passo 2*, o nome seria "12345678.912". Este arquivo é reservado ao uso da empresa e contém os dados dos trabalhadores com pagamento previso para o crédito na folha de pagamento.  
  **Observação :**  
     Após processar a liberação de recursos no SXPIS, será criado no diretório CAIXA um arquivo com o mesmo nome do arquivo trazido da CEF. Esse arquivo deverá ser renomeado, incluindo a extensão .TXT.   
 **Exemplo:**  
     "12345678.912" renomear para "12345678.912.TXT"   
   
   
 **Passo 5:**  
 Em seguida,o usuário deverá acessar o sistema e importar o arquivo "12345678.912" (via módulo IMPORTAÇÃO DE PIS).  
  
   
   
   
 **Observação** :  
 A importação do valor do PIS será processada da seguinte forma para funcionários que tem a MESMA Data de Nascimento e número doPIS:  
 1) Funcionários com chapas distintas (um ativo e um demitido):  
 A importação do evento de CC125 (Pagamento de PIS) se dará na movimentação somente para o funcionário que está na situação de Ativo.   
 2) Funcionários com chapas distintas (os dois registros ativos):  
 A importação do evento de CC125 (Pagamento de PIS) se dará na movimentação somente para um dos funcionários que está na situação de Ativo.  
 3) Funcionários com situação de demitido (demissão no mês, em meses anteriores e próximo mês):  
 A Importação não será realizada e os erros serão registrados no arquivo de Log de Inconsistências.  
 \_GoBack
