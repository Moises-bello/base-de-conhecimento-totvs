---
content_hash: d22fbcda8ea5c36f4b9631731483d0375409c155792d87a9b93139369cfcbdbb
fetched_at: '2026-06-29T00:05:58.519371+00:00'
page_id: '187535610'
product: rm
source: tdn-rm
title: RMFIS00010_02 - ECF na Linha RM
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00010_02+-+ECF+na+Linha+RM
version: 26
---

1562947116574\_-155673497

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão:** 11.82.38/12.1.4 |
| **Processo** | **:** | ECF - Escrituração Contábil Fiscal |
| **Subprocesso** | **:** | Parametrização e Geração |
| **Data da publicação** | **:** | 08/05/2015 |

\**A geração da rotina ECF já está disponível na versão 12.1.5. IMPORTANTE: Na versão 12 não é necessário a execução do script (ExecSql.RMLIBER.ECF.TotvsScript.zip).*

A Escrituração Contábil Fiscal (ECF) substituiu a Declaração de Informações Econômico-Fiscais da Pessoa Jurídica (DIPJ), a partir do ano-calendário 2014. A rotina foi implementada no ambiente da 11.82.38 e da 12.1.5, últimas versões disponíveis. **Sendo imprescindível a integração entre os sistemas RM Liber e RM Saldus.**

**Ambiente -> Parâmetros -> TOTVS Gestão Fiscal -> 03. 05 - Integração ->  - 03.05.01  Integração Contábil Ativa**

***Parametrização Necessária / Pré-requisitos***

É essencial que seja executado na base de dados,  o script *Script ExecSql.RMLIBER.ECF.TotvsScript.zip([FAQ de auxílio para Executar o Script](http://tdn.totvs.com/display/public/rm/Executor+de+Scripts+RM))*, disponibilizado no Portal do Cliente. Importe as *Tabelas Dinâmicas([FAQ de auxílio para Importar as Tabelas Dinâmicas](http://tdn.totvs.com/pages/viewpage.action?pageId=187831106))* e o *Layout da ECF( [FAQ de auxílio para Importação do Layout](http://tdn.totvs.com/pages/viewpage.action?pageId=187831246))*. Eventos Tributários e Plano de Contas Paralelo, devem estar devidamente cadastrados.

Os artefatos acima, estão disponíveis na Central de Downloads. Segue instruções:

 Acesse  [Central de Download](https://suporte.totvs.com/download)   
 Faça o login, com seu e-mail e senha. (O login de senha deverá ser do usuário cadastrado da empresa em questão). **Linha**: RM clique no link “Todos”

Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna do grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada. **Dica**: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" do grid de download, digitando o nome(**copie e cole**) do arquivo ou parte do mesmo para pesquisa/download.

* ExecSql.RMLIBER.ECF.TotvsScript.zip;
* [TABELAS\_DINAMICAS-ECF\_](https://suporte.totvs.com/download#0)
* [LAYOUT\_ECF\_11.82.ZIP](https://suporte.totvs.com/download#0) / [LAYOUT\_ECF\_12.1.ZIP](https://suporte.totvs.com/download#0)

**Links de referência:**

---

* **Executor de Scripts: <http://tdn.totvs.com/display/public/rm/Executor+de+Scripts+RM>**
* **ECF - Escrituração Contábil Fiscal: <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx>**
* **Parâmetros: <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.AnexoFilialParametrosECF.aspx>**
* **Plano de contas paralelo: <http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.planoContaParalelo.aspx>**
* **Livro de Apuração do Lucro Real (LALUR)Parte B: <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ParteBLalur.aspx>**
* **Evento Tributário: http: //[wikihelp.totvs.com.br/WikiHelp/FIS/FIS.EventosTributarios.aspx](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.EventosTributarios.aspx)**
* **Tabela Dinâmica: <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.TabelaDin%C3%A2mica.aspx>**
* **Informações Complementares: <http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx>**
* **Estrutura do Arquivo: <http://wikihelp.totvs.com.br/WikiHelp/FIS/Fis.EstruturaArquivoECF.aspx>**

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)

**COMUNIDADE **[R@Fiscal](http://fluig.totvs.com/portal/p/10097/subject/rfiscal)****

**Canais de Atendimento:**

**Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
