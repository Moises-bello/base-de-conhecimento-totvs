---
content_hash: a2849d4903668721209df05261cbab586050e734553caea849e5df63a2f22cb1
fetched_at: '2026-06-29T00:11:06.080305+00:00'
page_id: '63275490'
product: rm
source: tdn-rm
title: Reiniciar contagem de páginas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=63275490
version: 18
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.XX |
| **Processo** | **:** | Relatório .Net |
| **Subprocesso** | **:** | Reiniciar contagem de páginas |
| **Data da publicação** | **:** | 05/07/2013 |

**Para que** **você** **possa configurar o** **seu relatório** **para que** **o mesmo reinicie** **a contagem de páginas de** **acordo com a quebra o relatório deverá atender** **a alguns requisitos.**

**No exemplo abaixo** **estarei** **exemplificando a informação utilizando informações da PFUNC (campos** **PFUNC****.****CODFILIAL,** **PFUNC.CHAPA e** **PFUNC.NOME já inclusos no grupo Detalhe)** **tendo a quebra e** **reinicio da contagem de** **páginas a cada nova FILIAL.**

**No grupo detalhe que se deseja a quebra deverá ser incluso um cabeçalho do detalhe para este contendo as informações desejadas. No exemplo inserimos os campos GFILIAL.NOME e PFUNC.CODFILIAL.**

**Ainda no "Cabeçaho do Detalhe" configure a quebra da página pelo código da Filial. Para realizar a quebra de página selecione o grupo "Cabeçalho do Detalhe". Tecle F4, irá carregar as propriedades do grupo. Encontre nas propriedades a opção "Comportamento | Ordenação/Quebra". Na tela seguinte clique na opção "ADD" e escolha o campo "Código da Filial".**

**Ainda nas propriedades "Comportamento"** **altere** **o valor da opção** **"Repetir a cada página" para** **"Sim".**

**No próximo passo inclua um grupo "Rodapé do Detalhe"** **na estrutura do relatório.** **Para incluir** **o "Rodapé do Detalhe"** **clique** **com o** **botão direito** **sobre** **o grupo "Detalhe"** **e** **escolha os sub-menus "Inserir Seção | Rodapé** **do Detalhe".**

**Selecione** **o grupo "Rodapé** **do Detalhe"** **o tecle** **F4. Nas propriedades do grupo encontre** **a propriedade** **"Comportamento |** **Quebra de** **página" e** **altere** **o seu valor para "Depois da Seção".**

**Por último selecione** **o campo** **"Informações da Página",** **tecle** **F4.** **Nas propriedades "Comportamento | Seção Corrente" do campo altere o valor para "Cabeçalhododetalhe1".**

**Depois de feita** **estas configurações ao gerar o relatório sempre** **que** **a quebra por filial** **for realizada o relatório irá reiniciar a contagem de** **páginas. Segue abaixo** **exemplo do relatório gerado:**

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
