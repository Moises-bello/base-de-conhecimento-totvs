---
article_id: 360024872752
category: Configurador
content_hash: a68f25011151c8663f25dea24e4fc2cf1ba16a14dc2f9d70630427de76f2a0a3
fetched_at: '2026-06-28T22:42:19.264222+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Rotinas de Log e Auditoria
type: support-article
updated_at: '2024-05-08T11:57:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024872752-Framework-Linha-Protheus-Rotinas-de-Log-e-Auditoria
---

**Dúvida**  
Quais são as rotinas de auditoria que o Protheus disponibiliza?  
  
**Ambiente**  
Protheus - Configurador - A partir da versão 11  
  
**Solução**  
O Protheus possui algumas rotinas que permitem efetuar logs e auditoria do sistema. Abaixo listaremos as opções.

|  |
| --- |
| Aviso: Os relatórios dos logs de auditoria só passam a exibir informações que foram incluídas/alteradas/excluídas **após** a configuração do recurso. Eventos anteriores não são exibidos no relatório. |

**EMBEDDED AUDIT TRAIL**O serviço **Embedded Audit Trail** tem o objetivo de auditar as atividades realizadas pelos usuários do Protheus no banco de dados. Suas premissas são:  
- Alto desempenho  
- Facilidade de configuração  
- Simplicidade de operação  
- Segurança  
  
Para a documentação completa de configuração do **Embedded Audit Trail**, acesse os links abaixo:<http://tdn.totvs.com/display/PROT/Configurar+Embedded+Audit+Trail>  
  
**LOG DE REGISTROS**-CFGX025  
  
Faz a auditoria dos **registros** de uma tabela, mostrando o último usuário que alterou/incluiu um registro nessa tabela, a data e também se o registro foi excluído.  
Para ativar  
**P12/P11:** Campos \_USERLGI e \_USERLGA na tabela.   
1. Acesse a tabela que terá os registros auditados, pelo Configurador > Base de Dados > Dicionário > Bases de Dados, em **Campos**, clique no último botão **Campos Reservados**.   
  
![](http://tdn.totvs.com/download/attachments/271849522/LOG_01.png?version=1&modificationDate=1487874557000&api=v2)

2. Marque a caixinha **Log de Inclusão** e clique em **Finalizar**  
  
![](http://tdn.totvs.com/download/attachments/271849522/LOG_02.png?version=1&modificationDate=1487874557000&api=v2)

3. Abra novamente os **Campos Reservados**, marque a caixinha **Log de Alteração** e clique em **Finalizar**  
  
![](http://tdn.totvs.com/download/attachments/271849522/LOG_03.png?version=1&modificationDate=1487874557000&api=v2)

4. Na tela da listagem de Campos, clique em **Confirmar**, e na tela da listagem de tabelas clique em **Atualizar base de dados**  
  
![](http://tdn.totvs.com/download/attachments/271849522/LOG_04.png?version=1&modificationDate=1487874557000&api=v2)  
  
  
5. Vá avançando até **Finalizar**. Ao término, essa tabela já estará com os registros sendo auditados.  
  
  
**Para acessar o relatório**  
**P12**: É necessário adicionar manualmente a rotina **CFGX025** ao menu do Configurador  
- Para informações de como incluir um item de menu, consulte este link: <http://tdn.totvs.com/pages/viewpage.action?pageId=271164329>  
  
![](http://tdn.totvs.com/download/attachments/271849522/LOG_05.png?version=1&modificationDate=1487874557000&api=v2)  
  
  
**P11**: Configurador > Usuário > Auditoria > Log de Registros  
  
1. Após acessar a rotina pelo menu, selecione a tabela em que você ativou os campos \_USERLGI e \_USERLGA. É preciso que tenha sido feita alguma inclusão ou alteração de registro na tabela após a configuração do recurso para que o relatório seja exibido.  
  
![](http://tdn.totvs.com/download/attachments/271849522/LOG_06.png?version=1&modificationDate=1487874557000&api=v2)  
  
2. Na tela seguinte, selecione o registro e clique em **Visualizar**. Será exibida a janela do Log do Registro.  
  
![](http://tdn.totvs.com/download/attachments/271849522/LOG_07.png?version=1&modificationDate=1487874557000&api=v2)

---

**LOG DE CAMPOS** - CFGX052  
  
Possibilita configurar a auditoria para **campos** individualmente.  
Para ativar  
**P12**: É necessário adicionar manualmente a rotina **CFGX052** ao menu do Configurador  
Para informações de como incluir um item de menu, consulte este link: <http://tdn.totvs.com/pages/viewpage.action?pageId=271164329>  
  
![](http://tdn.totvs.com/download/attachments/271849522/LOG_08.png?version=1&modificationDate=1487874557000&api=v2)

**P11**: Configurador > Usuário > Auditoria > **Config. Log Audit**  
  
1. Após acessar a rotina pelo menu, clique no botão **Incluir**  
![](http://tdn.totvs.com/download/attachments/271849522/LOG_09.png?version=1&modificationDate=1487874557000&api=v2)  
  
2. Em **Tabela**, digite o nome da tabela que terá campo(s) auditado(s)  
3. Em **Campo**, digite o nome do campo que será auditado (para adicionar campos, pressione a seta para baixo do teclado)  
4. Clique em **Operação**, clique em **Outras Ações** (Ações Relacionadas) e selecione **Selecionar tipo de LOG**  
  
![](http://tdn.totvs.com/download/attachments/271849522/LOG_10.png?version=1&modificationDate=1487874557000&api=v2)  
  
5. Na janela **Tipo de LOG**, é possível selecionar quais opções serão auditadas no campo selecionado: Inclusão / Alteração / Exclusão. Há também opções de **Tipo de Atualização**, segue abaixo o detalhamento de cada uma delas:  
\* Atualizar o campo selecionado: configura a opção de Inclusão, Alteração e/ou Exclusão para o campo que estava selecionado ao clicar no botão **Selecionar tipo de LOG**  
\* Atualizar somente campos não preenchidos: configura a opção de Inclusão, Alteração e/ou Exclusão para os campos que não tiverem ainda nenhuma configuração já feita  
\* Atualizar todos os campos: configura a opção de Inclusão, Alteração e/ou Exclusão para todos os campos que estiverem listados na tela de **Configuração de LOG de campos**  
  
![](http://tdn.totvs.com/download/attachments/271849522/LOG_11.png?version=1&modificationDate=1487874557000&api=v2)  
  
6. Após terminar a configuração, clique em **Confirmar****Para acessar o relatório**  
**P12:** É necessário adicionar manualmente a rotina CFGX053 ao menu do Configurador  
- Para informações de como incluir um item de menu, consulte este link: <http://tdn.totvs.com/pages/viewpage.action?pageId=271164329>  
  
![](http://tdn.totvs.com/download/attachments/271849522/LOG_12.png?version=1&modificationDate=1487874557000&api=v2)  
  
  
**P11:** Configurador > Usuário > Auditoria > Consulta Log Audit

1. Após acessar a rotina pelo menu, na janela que será apresentada, clique em **Param.**  
2. Na tela de **Parâmetros**, preencha os dados da tabela, usuário e data que deseja visualizar, e clique em **OK**, depois **OK** novamente  
  
![](http://tdn.totvs.com/download/attachments/271849522/LOG_13.png?version=1&modificationDate=1487874557000&api=v2)  
  
3. Será apresentada uma tela com as informações da tabela, operação que foi efetuada, usuário, data e hora.  
  
![](http://tdn.totvs.com/download/attachments/271849522/LOG_14.png?version=1&modificationDate=1487874557000&api=v2)

---

**RASTRO DE AUDITORIA**![](http://tdn.totvs.com/download/attachments/271849522/LOG_15.png?version=1&modificationDate=1487874557000&api=v2)

**Consulta Auditoria** - Auditoria de Usuários - APCFGR50  
Faz a auditoria da rejeição a tentativa dos usuários de acesso a recursos bloqueados. Por exemplo, a tentativa de acesso a uma rotina bloqueada por Privilégios.  
Para ativar: Configurador > Usuário > Senhas > Política > Aba Outros > Regras de Auditoria > Auditar atualizações no dicionário de dados = Sim  
Para acessar o relatório: Configurador > Base de Dados > Auditoria > Consulta Auditoria (no P11 é necessário criar um item no menu do Configurador para a rotina APCFGR50)  
  
**Relatório de Auditoria** - Rastro de Auditoria (ou Auditoria Usuário - Rastro de Usuário no P11) - APCFGR10  
Faz a auditoria de alterações feitas nos usuários no Configurador, mostrando o usuário que sofreu alteração, usuário que fez alteração, data e hora, valor anterior e valor atualizado, etc.  
Para ativar: Configurador > Usuário > Senhas > Política > Aba Outros > Regras de Auditoria > Auditar atualizações no cadastro de usuário = Sim  
Para acessar o relatório: Configurador > Base de Dados > Auditoria > Relatório de Auditoria (ou Auditoria Usuário no P11)  
  
**Auditoria Dicionário** - Rastro de Dicionário - APCFGR20  
Faz a auditoria de atualizações no dicionário de dados feitas pelo Configurador, mostrando as informações anteriores e as atualizadas, a tabela, campo, usuário que fez a alteração, etc.  
Para ativar: Configurador > Usuário > Senhas > Política > Aba Outros > Regras de Auditoria > Auditar atualizações no dicionário de dados = Sim  
Para acessar o relatório: Configurador > Base de Dados > Auditoria > Auditoria Dicionário  
  
**Situação de Usuários** - Rastro do Usuário - APCFGR30  
Faz a auditoria da situação dos usuários no sistema, mostrando se eles estão ativos ou inativos, a data da criação do usuário, data da última alteração e o usuário que fez a alteração.  
Para ativar: Configurador > Usuário > Senhas > Política > Aba Outros > Regras de Auditoria > Auditar atualizações no cadastro de usuário = Sim  
Para acessar o relatório: Configurador > Base de Dados > Auditoria > Situação de Usuários  
  
**Log de Acesso** - Rastro de Acesso - APCFGR40  
Faz a auditoria do Log In e LogOut dos usuários, mostrando a data, horário e endereço IP dos mesmos.  
Para ativar: Configurador > Usuário > Senhas > Política > Aba Outros > Regras de Auditoria > Auditar autenticação/Acesso = Sim  
Para acessar o relatório: Configurador > Base de Dados > Auditoria > Log de Acesso
