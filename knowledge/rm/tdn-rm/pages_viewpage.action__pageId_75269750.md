---
content_hash: 3d1664567b7f7c908ac60973cbadcc97be12111970a31240d1df437f5ddda39d
fetched_at: '2026-06-29T00:11:32.967729+00:00'
page_id: '75269750'
product: rm
source: tdn-rm
title: Ativação do Log de Auditoria
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=75269750
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework                       **Versão:**11.xx |
| **Processo** | **:** | Log de Auditoria |
| **Subprocesso** | **:** | Ativação do Log de auditoria |
| **Data da publicação** | **:** | 18/09/2013 |

**Introdução**

**1.** **Log de auditoria**

O LOG de auditoria é composto por uma série de Triggers que são habilitadas no banco. Podemos selecionar tabelas e campos para auditoria.  
 Com ele podemos obter um histórico de todas as Inclusões/alterações/exclusões que ocorreram nos campos  
 selecionados para serem auditados pelo LOG.  
 Quando selecionamos um campo/tabela para auditoria automaticamente habilitamos a trigger referente a  
 esta tabela.  
 Quando o campo marcado sofre uma ação (inclusão/alteração/exclusão) a trigger é disparada e grava na tabela de LOG dados sobre o autor da ação e valores alterados.   
   
   
 **Desenvolvimento/Procedimento**

**1.1.** **Instalador**

O instalador do Log de auditoria é disponibilizado pelo suporte mediante a solicitação

**Obs.:** Este log somente será habilitado caso o usuário seja usuário mestre no sistema possuindo habilidades para alteração de perfil.

**Instalando:** Na primeira tela é exibido o assistente para instalação (Clicar em avançar).

Informar nome do usuário e organização (Clicar em avançar para continuar a instalação)

Será direcionado o diretório para instalação.

Clicar em concluir para finalizar a instalação.

Na pasta Log será apresentado o plugin RMSPLog.CRM, o mesmo deverá ser copiado para a pasta que irá controlar o LOG de auditoria (Como exemplo, utilizaremos o RM Portal)

Na Pasta que irá controlar o Log de auditoria, o arquivo CRM deverá estar incluído conforme orientações anteriores.

Habilitar no perfil deste usuário o menu referente à customização.

No menu customização será disponibilizada a opção Customização habilitada.

Selecionar os aplicativos e os campos que serão auditados. Abaixo, segue exemplo do aplicativo RM Portal com os campos habilitados que serão auditados.

Importante: Marcar a opção "LOG ATIVO" para que o processo possa ser iniciado.

Após executar consultas na tabela ZLOG, verifica-se que os dados alterados são gravados nesta tabela para conferências.

Todos os campos auditados inserem dados nesta tabela (ZLOG) ao serem alterados no sistema por algum usuário.

**Informações Adicionais:**

Quanto mais campos e tabelas forem auditados, mais recursos de hardware (servidor) são necessários.  
 Se o LOG for usado com critério, não haverá degradação de performance.   
 A perda de performance vai depender de dois fatores inversamente proporcionais:  
 *O* *quanto* *de* *nossos* *processos* *estamos* *auditando* X *O* *quanto* *de* *Recursos* *de* *Máquina* *temos disponível*  
 Quando falamos em performance temos que nos atentar a algumas regras que devem ser cuidadosamente analisadas.  
 Devemos marcar somente os campos que realmente têm necessidade de auditoria.  
 Por exemplo, se marcarmos o campo Salário ta tabela PFUNC, este campo não sofre alterações a todo momento. Não há impacto sobre performance.  
 Ao contrário, se marcarmos um campo de uma tabela sofre alterações constantes, por exemplo, valor original da tabela de Lançamentos, suponhamos que o cliente processa em média 200 lançamentos por dia... isso **"pode"** ocasionar perda de performance, pois a trigger estará sendo executada a todo momento. É importante salientar que não há como afirmar que haverá perda de performance, pois vários fatores contribuem para isso como configuração de máquina e rede. Quanto mais "parrudo" o servidor for, menos impactos teremos na performance.  
 Temos relatos de clientes que auditam tabelas que sofrem alterações constantes e nem por isso perderam performance. Porém, sabemos que seu ambiente é hiperdimensionado.   
 Um mau exemplo de utilização do Log seria marcar sem critério todos os campos da várias tabelas, isso fará com que o sistema grave a todo o momento informações na tabela de LOG, acarretaria em uma massa de dados muito grande dificultando, inclusive, a leitura destes registros.   
 OBS: O Log é armazenado no banco pelo número de dias parametrizado pelo usuário. Se informado  
 20 dias, a tabela mantém os registros dos últimos 20 dias. Vale ressaltar que dependendo da quantidade de campos auditados e dias para armazenamento, a tabela de LOG pode assumir proporções gigantescas que podem interferir no gerenciamento do SGDB.   
 **O** **mais importante** **é ter** **critério** **e selecionar** **para** **Log somente** **o** **que é necessário.**

Para maiores informações:

Consulte o [Wikihelp](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.LogAuditoria.aspx) TOTVS.

**COMUNIDADE** [@FRAMEWORK](https://totvs.byyou.com/?space=rframework)

**Canais de Atendimento:**

**Telefônico:** 4003-0015 escolhendo as opções 02 – dois (Software), 02 – dois (Suporte Técnico), 03 – três (RM), 09 – nove (Demais Áreas), 04 – quatro (BI) e 03 – três (Gerador de Relatórios e Planilha);

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)
