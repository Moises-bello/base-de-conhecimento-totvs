---
content_hash: 2046c42dd50c7a869945c842367e3e5bb28a0052e7e35d76acfc92179275fe71
fetched_at: '2026-06-29T00:05:58.428261+00:00'
page_id: '185761600'
product: rm
source: tdn-rm
title: Log de Auditoria
type: documentation
url: https://tdn.totvs.com/display/LRM/Log+de+Auditoria
version: 13
---

**Introdução**

---

        O Log de auditoria é composto por uma séria de Triggers que são habilitadas no banco. Podemos selecionar tabelas e campos para auditar.

        Com ele podemos obter um histórico de todas as inclusões, alterações e exclusões que ocorreram nos campos escolhidos para serem auditados. Quando escolhemos um campo/tabela para auditar, automaticamente é habilitado no banco de dados uma trigger referente a escolhida. Quando houver transações que utiliza o campo escolhido, a trigger é disparada e grava na tabela de Log (**ZLOG**) os dados sobre o autor, da ação tomada sobre os valores alterados.

# ****Como funciona****

---

**1)** Acesse o contexto , logo após, **Administração** **|** Configuração | **Log de auditoria -> Configurações.**

**2)** Após o acesso, será aberto a tela de configurações do Log, como mostra abaixo:

**Observações:**

* É importante que no campo:  esteja marcado para que seja auditado.
* No campo:   Significa, que o número de dias que o usuário informar neste campo, é a quantidade de dias que serão armazenados as informações do log de auditoria, no banco de dados. Ou seja, se o usuário informa 10, como no exemplo, serão armazenados todas as informações dos últimos 10 dias. É importante lembrar que, dependendo da quantidade de campos selecionados pelo usuário para ser auditado, a tabela de log (**ZLOG**) pode assumir grandes proporções que podem interferir no gerenciamento do banco de dados.

**3)** Após ter **ativado o log** e configurado o **N° de dias do log**, selecione o(s) aplicativo(s) mais o(s) campo(s) que serão auditados, como mostra no exemplo abaixo:

**Observação:**

* É importante lembrar que, quanto mais campos forem selecionados para serem auditados, mais recursos do seu servidor (hardware) serão consumidos.

        **4)**É possível também, selecionar processos que poderão não ser auditadas pelo log de auditoria. Para isso clique na guia **Exceções**, como mostra na imagem abaixo:

        

        **4.1)** Logo após, clique em **Adicionar**. Será aberto uma janela para que seja escolhido quais processos que não serão controlados pelo Log. Como mostra a imagem abaixo:

        

       

**5)** Após fazer todas as configurações, é possível consultar a situação do log de auditoria pelo banco de dados na tabela **ZLOG**ou diretamente no sistema. Para verificar através do sistema, clique em **Log de Auditoria | Configurações**, como mostra a imagem abaixo:

        

        **5.1)**Após o acesso, será aberto a tela com a situação do log de auditoria de acordo com os campos marcados nas configurações.

        

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

Para identificar se o log de auditoria está ativo, consulte a tabela**ZLOGPARAMS**, coluna**LOGATIVO**, considere **S** para Sim e **N** para Não.

Caso o Log esteja ativo, para consultar as informações armazenadas referente ao log de auditoria consulte a tabela **ZLOG**.

Para identificar os campos auditados, consulte a tabela **ZLOGCAMPOS**.

A limpeza de registros na tabela **ZLOG** ocorre quando é gerado o relatório de Log (Log de Auditoria - Log).

**Dessa forma, o  processo de limpeza é realizado de acordo com a parametrização do campo Nº de Dias do Log.**

O processo deve ser realizado manualmente, ou seja, para realizar a limpeza, faz-se necessária a geração do relatório para disparar o processo.

Já existe um chamado aberto para análise de Sugestão de Melhoria para tornar o processo de limpeza de registros da tabela **ZLOG** automático.

 

---

**Observação:**

* Em SGBD's Oracle é necessário a concessão de algumas permissões específicas para utilização das mesmas. Quando este permissionamento não é realizado as triggers não são criadas e os registros na ZLOG não são inseridos. Veja como conceder as permissões para SGBD Oracle no link abaixo:

**[Solucionando Erro: Log de auditoria não grava os dados auditados na tabela ZLOG (Oracle)](http://tdn.totvs.com/pages/viewpage.action?pageId=63864849)**

---

Para maiores informações:

****[@FRAMEWORK](http://fluig.totvs.com/portal/p/10097/subject/rframework)****

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)

|  |  |
| --- | --- |
| **Produto** | Framework |
| **Versão** | 12.1.4 |
| **Processo** | Log de Auditoria |
| **Subprocesso** | Ativação do Log de auditoria |

|  |  |
| --- | --- |
| Status do Documento: | Produção |
| Data: | 28/04/2015 |
| Versão: | 12.1.4 |
| Versão Anterior: | 12.1.3 |
| Autores: |  |
