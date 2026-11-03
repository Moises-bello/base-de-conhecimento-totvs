---
content_hash: 62b575b1c0235b1e48a10ab7e243799b4e8a2bf28f8d1669f889f686a2036192
fetched_at: '2026-06-29T00:10:57.170010+00:00'
page_id: '59441813'
product: rm
source: tdn-rm
title: Ativação do Log de auditoria – MDI (RM.EXE)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=59441813
version: 9
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework                       **Versão:**11.50 |
| **Processo** | **:** | Log de Auditoria |
| **Subprocesso** | **:** | Ativação do Log de auditoria |
| **Data da publicação** | **:** | 10/03/2015 |

**Introdução**

O LOG de auditoria é composto por uma série de Triggers que são habilitadas no banco. Podemos selecionar tabelas e campos para auditoria.   
 Com ele podemos obter um histórico de todas as inclusões/alterações/exclusões que ocorreram nos campos selecionados para serem auditados pelo LOG.   
 Quando selecionamos um campo/tabela para auditoria, automaticamente habilitamos a trigger referente a esta tabela.   
 Quando o campo marcado sofre uma ação (inclusão/alteração/exclusão), a trigger é disparada e grava na tabela de LOG dados sobre o autor da ação e valores alterados.   
  
**Parametrizando o LOG**

1. **No RM.exe acessar o contexto Serviços Globais | Aba Administração | Ícone Log de Auditoria (Configurações).**

**Importante**: Marcar a opção "LOG ATIVO" para que o processo possa ser iniciado.

  2. Ao selecionar a opção "Log" o sistema apresentará os processos realizados nos campos que foram auditados.   
   
        
   
   
    3. Ao realizar consulta pelo banco de dados na tabela **ZLOG** será possível visualizar os mesmos dados dos campos auditados. Lembrando que a tabela ***ZLOG*** é responsável por gravar estas informações.   
 ***OBS:*** *O mesmo procede para banco de dados ORACLE.*

   

**Informações Adicionais:**

Quanto mais campos e tabelas forem auditados, mais recursos de hardware (servidor) são necessários.  
Se o LOG for usado com critério, não haverá degradação de performance.   
A perda de performance vai depender de dois fatores inversamente proporcionais:  
*O* *quanto* *de* *nossos* *processos* *estamos* *auditando* X *O* *quanto* *de* *Recursos* *de* *Máquina* *temos disponível*  
Quando falamos em performance temos que nos atentar a algumas regras que devem ser cuidadosamente analisadas.  
Devemos marcar somente os campos que realmente têm necessidade de auditoria.  
Por exemplo, se marcarmos o campo Salário ta tabela PFUNC, este campo não sofre alterações a todo momento. Não há impacto sobre performance.  
Ao contrário, se marcarmos um campo de uma tabela sofre alterações constantes, por exemplo, valor original da tabela de Lançamentos, suponhamos que o cliente processa em média 200 lançamentos por dia... isso **"pode"** ocasionar perda de performance, pois a trigger estará sendo executada a todo momento. É importante salientar que não há como afirmar que haverá perda de performance, pois vários fatores contribuem para isso como configuração de máquina e rede. Quanto mais "parrudo" o servidor for, menos impactos teremos na performance.  
Temos relatos de clientes que auditam tabelas que sofrem alterações constantes e nem por isso perderam performance. Porém, sabemos que seu ambiente é hiperdimensionado.   
Um mau exemplo de utilização do Log seria marcar sem critério todos os campos da várias tabelas, isso fará com que o sistema grave a todo o momento informações na tabela de LOG, acarretaria em uma massa de dados muito grande dificultando, inclusive, a leitura destes registros.   
OBS: O Log é armazenado no banco pelo número de dias parametrizado pelo usuário. Se informado  
20 dias, a tabela mantém os registros dos últimos 20 dias. Vale ressaltar que dependendo da quantidade de campos auditados e dias para armazenamento, a tabela de LOG pode assumir proporções gigantescas que podem interferir no gerenciamento do SGDB.   
**O** **mais importante** **é ter** **critério** **e selecionar** **para** **Log somente** **o** **que é necessário.**

**Obs.: Em SGBD's Oracle é necessária a concessão de algumas permissões específicas para utilização das mesmas.**

**Quando este permissionamento não é realizado as triggers não são criadas e os registros na ZLOG não são inseridos. Veja como conceder as permissões para SGBD Oracle no link abaixo:**

Para identificar se o log de auditoria está ativo, consulte a tabela **ZLOGPARAMS**, coluna **LOGATIVO**, considere **S** para Sim e **N** para Não.

Caso o Log esteja ativo, para consultar as informações armazenadas referente ao log de auditoria consulte a tabela **ZLOG**.

Para identificar os campos auditados, consulte a tabela **ZLOGCAMPOS**.

A limpeza de registros na tabela **ZLOG** ocorre quando é gerado o relatório de Log (Log de Auditoria - Log).

**Dessa forma, o  processo de limpeza é realizado de acordo com a parametrização do campo Nº de Dias do Log.**

O processo deve ser realizado manualmente, ou seja, para realizar a limpeza, faz-se necessária a geração do relatório para disparar o processo.

Já existe um chamado aberto para análise de Sugestão de Melhoria para tornar o processo de limpeza de registros da tabela **ZLOG** automático.

Para maiores informações:

Consulte o [Wikihelp](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.LogAuditoria.aspx) TOTVS.

**COMUNIDADE** [@FRAMEWORK](https://totvs.byyou.com/?space=rframework)

**Canais de Atendimento:**

**Telefônico:** 4003-0015 escolhendo as opções 02 – dois (Software), 02 – dois (Suporte Técnico), 03 – três (RM), 09 – nove (Demais Áreas), 04 – quatro (BI) e 03 – três (Gerador de Relatórios e Planilha);

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)
