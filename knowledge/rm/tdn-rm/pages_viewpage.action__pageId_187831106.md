---
content_hash: 2e4b4c5a6cd85381571c02cc89e07c657f0645e188bdd70a0b2023b0f37fe2f5
fetched_at: '2026-06-29T00:05:58.793420+00:00'
page_id: '187831106'
product: rm
source: tdn-rm
title: RMFIS00001_08.001 - Importação - Tabelas Dinâmicas ECF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=187831106
version: 12
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.82.38/12.1.4 |
| **Processo** | **:** | Escrituração Contábil Fiscal - Tabelas Dinâmicas |
| **Subprocesso** | **:** | Importação |
| **Data da publicação** | **:** | 18/05/2015 |

\**A geração da rotina ECF já está disponível na versão 12.1.5. IMPORTANTE: Na versão 12 não é necessário a execução do script (ExecSql.RMLIBER.ECF.TotvsScript.zip).*

A Escrituração Contábil Fiscal (ECF) substituiu a Declaração de Informações Econômico-Fiscais da Pessoa Jurídica (DIPJ), a partir do ano-calendário 2014. A rotina foi implementada no ambiente da 11.82.38 e da 12.1.5, últimas versões disponíveis.

O objetivo deste documento([FAQ em Vídeo](http://tdn.totvs.com/pages/viewpage.action?pageId=189302136)) é oferecer orientações sobre importação das **Tabelas Dinâmicas** utilizadas na geração da rotina **ECF**.

***Regras Gerais***

As Tabelas Dinâmicas serão vinculadas ao Evento Tributário e posteriormente geradas na ECF. As tabelas a serem listadas, serão apresentadas conforme a forma de tributação selecionada e pasta (**Grupo**) que o usuário está parametrizando.

***Parametrização Necessária***

---

Baixe as Tabelas para importação no sistema TOTVS Gestão Fiscal. Acesse a [Central de Download](https://suporte.totvs.com/download): No campo de **Pesquisar**(*caixa de busca)* **digite ou cole** a descrição: **TABELAS\_DINAMICAS-ECF\_**. Após pesquisar, será apresesentado o arquivo ***Tabelas\_Dinamicas\_ECF.zip.*** Faça o Download.

**Importação do Arquivo**

Para importação das tabelas dinâmicas é necessário abrir o sistema **RM** →TOTVS Gestão Fiscal, acessar o menu: **Obrigações Acessórias | Federais | ECF | Tabela Dinâmica. Importante:** Lembrando que o Script do ECF deve ser executado anteriormente(**EXECSQL.RMLIBER.ECF.TOTVSSCRIPT.ZIP -  [FAQ Executar Script](http://tdn.totvs.com/display/public/rm/Executor+de+Scripts+RM))**

Após abrir a janela de Tabela Dinâmica, acesse menu: **Processos | Importação Tabela Dinâmica – ECF** | *Selecionar o arquivo correspondente ao regime da empresa* **| Executar**.

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

Para mais informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)

**COMUNIDADE **[R@Fiscal](http://fluig.totvs.com/portal/p/10097/subject/rfiscal)****

**Canais de Atendimento:**

**Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
