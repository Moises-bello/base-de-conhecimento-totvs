---
article_id: 360048781334
category: BI - Business Intelligence - Crystal-Reports
content_hash: fd578c53f352db870844a7aa97993140748f1c42584b7c0236d331a66c43239a
fetched_at: '2026-06-28T22:40:29.028603+00:00'
product: protheus
section_id: 1500001548282
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Problemas comuns no
  Crystal
type: support-article
updated_at: '2022-02-15T18:45:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048781334-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Problemas-comuns-no-Crystal
---

**![](https://jiratdncdncontent.blob.core.windows.net/tdn/icons/time.png)** Tempo aproximado para leitura:**2 minuto**

**Dúvida**Quais problemas posso enfrentar na integração ***Crystal* x Protheus?**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – BI – A partir da versão 11.8  
  
**Solução**Elaboramos uma lista dos problemas mais comuns, que podem ocorrer na integração entre o **Microsiga Protheus®** e **Crystal Reports** e as suas soluções:

**Problema 1:**Ao acessar um relatório Crystal Reports a partir do menu do Microsoft Protheus®, o Sistema apresenta uma tela sem informações, e a barra de progressão (gauge) incompleta.

**Solução:**  
• Certifique-se de que executou a instalação dos Drivers do Crystal e também instalou o Client do Crystal.  
• Verifique se a fonte de dados ODBC utilizado no relatório Crystal Reports foi criado como USER DSN.  
• O nome da fonte de dados é case-sensitive, ou seja, se o relatório foi criado baseado na fonte de dados data, em todas as estações o nome da fonte de dados deve estar grafado em letras maiúsculas.  
  
**Problema 2:**  
Como proceder para acessar o relatório Crystal Reports de dentro de um Rdmake?

**Solução:**  
Releia a explicação acima sobre a função **CallCrys**.

**Problema 3:**  
Ao acessar o relatório através de um **Rdmake** ou, tentar atualizar (refresh) os dados deste relatório dentro do Crystal Reports, o sistema não apresenta as informações. As informações serão apresentadas somente se o sistema for finalizado e os dados atualizados.

**Solução:**  
Antes de acessar o relatório de dentro do **Rdmake** (função CallCrys), execute o comando **COMMIT**.

**Problema 4:**  
Ao tentar executar um relatório baseado em um ODBC para SQL 7.0, ele nada mostra ou o gauge (barra de progressão) para no meio.

**Solução:**  
Verifique no drive ODBC criado para o SQL7 se a opção Change Default DataBase To está marcada, e apontando para o Banco de Dados Correto.

**Problema 5:**  
Como faço para abrir o Sigamat.Emp no relatório?

**Solução:**  
O Driver ODBC não é capaz de abrir o Sigamat.Emp. Utilize os Data Files em vez de ODBC. No Crystal Reports é possível mesclar arquivos abertos com ODBC e com Data Files.

**Problema 6:**  
Minha Tabela DBF tem campo Memo e não consigo abrí-la no Crystal Reports.

**Solução:**  
Para abrir arquivos DBF com campo Memo, é necessário criar o datasource ODBC usando o driver Microsoft FoxPro driver (caso exista e seja versão 3.5x) ou Microsoft Visual FoxPro (caso o sistema seja o Windows 2000/XP).

Abrir o arquivo CRYSINI.INI (localizado no diretório do SGCRYS32.EXE) e incluir a seguinte linha:

VERSION=4

**Problema 7:**  
Ao criar um relatório dentro do Crystal Reports, ao selecionar as tabelas o sistema avisa que a tabela em questão não possui fields, ou ao tentar abrir um relatório criado por outro usuário é apresentada a mensagem de que o arquivo está em uso ou de que não tenho acesso aos dados.

**Solução:**  
Para construir relatórios é preciso ter acesso de escrita no diretório dos dados, caso seja DBF (ADS ou CDX). Este procedimento não é necessário para visualizar o relatório a partir do Crystal Reports.

**Problema 8:**  
O relatório é gerado sem problemas dentro do Crystal Reports, mas quando ele é executado através do Microsiga Protheus® alguns valores não aparecem ou algumas fórmulas não são executadas ou, ainda, o relatório não é exibido.

**Solução:**  
Verifique na estação todas as DLLs chamadas CRPE32.DLL. Deve existir apenas uma na estação, (deve estar no path do Windows) e a versão desta DLL deve ser compatível com a versão do Crystal Reports utilizada. Para verificar a versão, basta verificar as propriedades do arquivo.

**Saiba Mais:  
[MP - BI - Documentação Crystal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016447592)  
 [MP - BI - Relatório Crystal não funciona via Schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025674571)  
[MP - BI - Código de Barras BAR CODE 39 não imprime corretamente dentro do Crystal Reports](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025142772)**
