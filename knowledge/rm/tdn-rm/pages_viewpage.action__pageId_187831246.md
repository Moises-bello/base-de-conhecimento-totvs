---
content_hash: 97bda91d11cc63c53bf8e62a89d50346f353314e60ffd732c1736015f0e77813
fetched_at: '2026-06-29T00:05:58.800500+00:00'
page_id: '187831246'
product: rm
source: tdn-rm
title: RMFIS00001_12.001 - Importação Layout ECF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=187831246
version: 10
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão:** 11.82.38/12.1.4 |
| **Processo** | **:** | Escrituração Contábil Fiscal -  ECF |
| **Subprocesso** | **:** | Importação do Layout |
| **Data da publicação** | **:** | 18/05/2015 |

\**A geração da rotina ECF já está disponível na versão 12.1.5. IMPORTANTE: Na versão 12 não é necessário a execução do script (ExecSql.RMLIBER.ECF.TotvsScript.zip).*

A Escrituração Contábil Fiscal (ECF) substituiu a Declaração de Informações Econômico-Fiscais da Pessoa Jurídica (DIPJ), a partir do ano-calendário 2014. A rotina foi implementada no ambiente da 11.82.38 e da 12.1.5, últimas versões disponíveis.

Este documento([FAQ em Vídeo](http://tdn.totvs.com/pages/viewpage.action?pageId=189306951)) tem como objetivo orientá-lo na importação do layout, para geração da rotina ECF.

***Parametrização Necessária***

---

**Permissões:**

Libere as devidas permissões do Perfil do Usuário para ter acesso aos seguintes menus:

**Gestão Fiscal | Obrigações Acessórias | Rotinas Fiscais | Gerador Saídas**

**Gestão Fiscal | Obrigações Acessórias | Rotinas Fiscais | Gerador Saídas | Inserir, Excluir e Editar**

**Categoria do Layout**

Crie a Categoria para o Layout através do Menu:

Módulo Integração → **Integração | Gerador de Saídas | Categoria**. Essa Categoria define a segurança da rotina. Para ter acesso à rotina é preciso que a Categoria esteja associada ao Perfil do usuário.

**Importante:** Não se esqueça de associar o Perfil à Categoria criada. Caso o Perfil não seja associado, o usuário não conseguirá selecionar o Layout para geração.

**Importação**:

Realize o processo de Importação através do Menu:

**Obrigações Acessórias | Gerador de Saídas -> Processos -> Importar Layout**: Na tela seguinte, clique no botão "Adicionar Objetos" e selecione o arquivo baixado no pacote ECF.zip, disponível no portal: "ECF.TotvsGen".

* Selecione  a opção "**Todas Coligadas**" no quadro  '**Seleção de Coligada**'
* Selecione o Objeto "**Layout ECF**", na aba Parâmetros, informe a Categoria criada previamente
* Clique em "**Executar**".

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
