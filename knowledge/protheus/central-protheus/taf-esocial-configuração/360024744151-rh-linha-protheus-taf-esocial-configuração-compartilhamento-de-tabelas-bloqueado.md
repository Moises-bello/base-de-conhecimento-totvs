---
article_id: 360024744151
category: TAF - eSocial - Configuração
content_hash: a8d5ecaf10f22d0797a88ea80d51b2ac1c8c8c90ab4f0a8c7e7d771890451409
fetched_at: '2026-06-28T22:45:14.510287+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - Compartilhamento de tabelas
  bloqueado
type: support-article
updated_at: '2026-06-25T11:16:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024744151-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Compartilhamento-de-tabelas-bloqueado
---

**ATENÇÃO, CASO SEJA NECESSÁRIO O COMPARTILHAMENTO DE TABELAS, O NOSSO SUPORTE NÃO ATUA NA DEMANDA SENDO NECESSÁRIO ATUAÇÃO DE UM CONSULTOR *IN LOCO* NA EMPRESA. ESTE MATERIAL É INFORMATIVO REFERENTE AO BLOQUEIO DO COMPARTILHAMENTO DE TABELAS.  
  
CASO QUEIRAM COMPARTILHAR AS TABELAS COM A BASE POPULADA, RECOMENDO QUE CHEQUEM SE A TABELA CORRERÁ O RISCO DE TEREM REGISTROS DUPLICADOS:**

[MP - FRAME - CheckDupl: Verificação de Duplicidade de Registros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025732213)

**Ocorrência**Bloqueio no compartilhamento de tabelas realizado a partir da LIB versão 20181015  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Configuração - Todas as versões  
  
**Causa**Para evitar a alteração do **compartilhamento da tabela** entre empresas quando a tabela já possui registros, o que pode gerar inconsistência de dados, foi implementada uma trava no Configurador que faz com que os campos **Ac. Filial**, **Ac. Unidade** e **Ac. Empresa** fiquem bloqueados para alteração quando a tabela já estiver alimentada, evitando a alteração do seu **tipo de compartilhamento**. A alteração só poderá ser feita em **tabelas vazias**.

**Exemplo de tela:**

# Tabela SA3 vazia, campos "Ac" liberados  
Configurador > Base de Dados > Dicionário > Bases de Dados > Tabela SA3  
  
![](http://tdn.totvs.com/download/attachments/412886207/2018-09-18_559.png?version=1&modificationDate=1537274740943&api=v2)

# Tabela SA3 alimentada, campos "Ac" bloqueados  
Configurador > Base de Dados > Dicionário > Bases de Dados > Tabela SA3  
  
![](http://tdn.totvs.com/download/attachments/412886207/2018-09-18_560.png?version=1&modificationDate=1537274740907&api=v2)

**Solução**Para realizar o compartilhamento de tabelas após o bloqueio, deve-se realizar os seguintes procedimentos:

1. Acesse o programa **APSDU**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023030092)

2. Em seguida, acesse o menu **Arquivo > Abrir > Driver: Top Connect (TOPCONN)**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023062471)

3. Após confirmar, será apresentada a caixa para informar a tabela a ser aberta, e neste exemplo, será aberta a tabela C8R do Grupo de Empresa 99, ou seja, a tabela C8R990:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26677194228631)

4. Ao confirmar, a tabela C8R990 será aberta, conforme segue:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26677161298455)

5. Após abertura da tabela, faremos primeiramente o backup dos seus dados, a partir do menu **Útil > Copiar Para**. Será aberta a tela a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26677194260759)

6. Em **(Caminho)\Arquivo**, clique no botão ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023062891) para selecionar o diretório a ser salvo o backup, que por padrão apresentará a estrutura abaixo do diretório **system** do TAF/Protheus:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023030652)

7. Após seleção do diretório, clique no botão OK para confirmar o **backup**. Será apresentada a mensagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26677161305751)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023064591)

8. No diretório selecionado, serão gerados os arquivos de backup, de acordo com a ilustração abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26677194263959)

9. Após o término do backup, deve-se esvaziar a tabela para que seja possível realizar o seu compartilhamento. Para isso, ainda com a tabela aberta, acesse o menu **Útil > Zap**.

Será apresentada a pergunta abaixo, onde pode-se confirmar para realizar o delete físico dos registros da tabela, conforme demonstrado abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023031572)

Tabela C8R990 é apresentada vazia ao fundo, após conclusão da instrução **Zap**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26677161312023)

10. Com a tabela vazia, podemos acessar o programa **SIGACFG** - **Configurador**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023064971)

11. No **Configurador**, acesse o menu **Base de Dados > Dicionário > Bases de Dados**, e será apresentada a tela a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023032932)

12. Clique ao lado direito na opção **Dicionário de Dados**, para que sejam listadas as tabelas do seu banco de dados, e em seguida, no botão ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023065231), para que seja aberta a caixa para informar o nome da tabela a ter o seu compartilhamento alterado, conforme segue:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023065311)

13. Em **Procurar por:** digite o nome da tabela, neste exemplo, C8R, e clique em Buscar. A tabela C8R será a primeira a ser exibida na lista de tabelas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26677194270615)

14. Clique no botão ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023033412), e será apresentada a tela a seguir, que nos permitirá fazer a alteração do compartilhamento da tabela C8R:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26677161320727)

15. Após alteração do compartilhamento da tabela C8R nos 3 níveis, para que o conteúdo desta tabela fique disponível para todas as filiais, clique no botão ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023065951):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26677161325975)

16. Na tela a seguir, clique no botão ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023066031)para efetivar a alteração do compartilhamento da tabela C8R. A seguir, serão demonstradas algumas informações referente a **alteração do compartilhamento**, como as tabelas que serão afetadas e terão o seu compartilhamento também alterado para garantir a integridade do TAF/Protheus:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023067891)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023067931)

17. Ao clicar em **Finalizar**, no passo anterior, a alteração será efetivada e o compartilhamento estará alterado.

18. Após este passo, deve-se retornar ao programa **APSDU** e abrir a tabela C8R, conforme segue:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26677194285975)

20. Com a tabela aberta, acesse o menu **Útil > Append From**. Será aberta a tela a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26677194289047)

21. Em **(Caminho)\Arquivo**, clique no botão ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023062891) e selecione o diretório e o arquivo de backup gerado anteriormente. Ao final, clique no botão **Abrir**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26677161344407)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26677194301719)

22. Clique no botão **OK**, e desta forma, os dados salvos serão restaurados, conforme segue:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26677161350423)

23. Como a tabela teve o seu compartilhamento alterado para Compartilhado nos 3 níveis, o conteúdo do campo C8R\_FILIAL deve ficar vazio. Para isso, acesse o menu Útil > Substituir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26677161358999)

24. Para que o conteúdo do campo C8R\_FILIAL fique vazio em toda a tabela, basta informar "" (duas aspas duplas) no campo **Com:** e clicar no botão **OK**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26677194324887)

Com isso, o conteúdo do campo C8R\_FILIAL ficará vazio, de acordo com o tipo de compartilhamento **Compartilhado** nos 3 níveis:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26677161373207)

**Observações:**

* O preenchimento do campo **\_FILIAL** da tabela alterada deverá ser realizado de acordo com o compartilhamento selecionado, pois é através deste campo que será identificado para quais empresas, unidades de negócio e filiais o acesso ao registro ficará disponível, ocasionando problemas de integridade de dados caso não seja preenchido da forma correta;

* Caso necessite realizar a alteração do compartilhamento de tabelas do TAF após já ter realizado movimentações nas tabelas, é **altamente recomendável** a presença de um analista in loco para a realização dos procedimentos de acordo com a análise prévia de sua estrutura empresarial.
