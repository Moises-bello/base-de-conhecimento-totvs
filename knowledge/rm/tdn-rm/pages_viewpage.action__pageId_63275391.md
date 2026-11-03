---
content_hash: 1498cfcfe1b5e1e5178e179ab07369563550e064dafcf697d607ccc1b3fbd8bf
fetched_at: '2026-06-29T00:11:05.981931+00:00'
page_id: '63275391'
product: rm
source: tdn-rm
title: Ocultar Gestão de Ferramentas no RM Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=63275391
version: 6
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.XX |
| **Processo** | **:** | RM Portal |
| **Subprocesso** | **:** | Ocultar Gestão de Ferramentas no RM Portal |
| **Data da publicação** | **:** | 05/07/2013 |

**Para** **desabilitar** **o** **menu** **"Ferramentas"** **na** **visão** **das** **gestões** **no RM** **Portal** **após** **o login** **deverá** **ser** **feito** **o seguinte** **processo.**

**Acesse** **o diretório** **"C:\totvs\CorporeRM\Corpore.Net"** **da** **máquina** **onde** **o RM** **Portal está** **instalado.** **Encontre** **o** **arquivo** **"Menu.xml"** **e edite** **o mesmo** **utilizando** **o bloco** **de** **notas (No** **exemplo** **abaixo** **iremos** **utilizar** **o Notpad++).**

**Primeiro deverá ser removido dois comentários existentes no arquivo. Sendo assim remova os comandos <!- -> da opção "Canal RSS" e "GlbTwitter".**

**Após** **as** **alterações** **deverá** **ficar** **da** **seguinte** **forma.**

**Em** **seguida** **deverá** **ser** **aberto** **o** **comentário** **(<!--)** **na** **tag** **"<MenuItem>"** **(Sem** **aspas) que trata da gestão "Ferramentas". O resultado ficará desta forma <!--<MenuItem>.**

**Para finalizar feche o comentário (-->) na tag "</MenuItem>" (Sem aspas). O** **resultado final ficará desta forma </MenuItem>-->**

**Depois** **de** **feita** **as** **alterações** **carregue** **novamente** **a** **tela** **do** **RM** **Portal** **e realize** **o login. Estas** **orientações** **são** **validas** **para** **o portal** **na** **versão** **11.40** **e** **11.50.**   
 **Obs.:** **Pedimos** **atenção** **para** **que** **as** **linhas** **sejam** **corretamente** **comentadas,** **pois** **a** **seleção errada** **em** **alguma** **delas** **acarretará** **erro** **no** **RM** **Portal** **após** **o login** **efetuado.**

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
