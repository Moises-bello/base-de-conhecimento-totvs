---
content_hash: 061c003f48084619544e3098f30c956458af1704472ec0bd9abb3373869598d6
fetched_at: '2026-06-29T00:05:57.897374+00:00'
page_id: '185729929'
product: rm
source: tdn-rm
title: CAT 79/2003 - Geração da rotina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185729929
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.82.3x / 12.1.x |
| **Processo** | **:** | Apuração de ICMS - CAT 79/2003 - Energia Elétrica e Telecomunicações |
| **Subprocesso** | **:** | Geração da rotina estadual |
| **Data da publicação** | **:** | 11/02/2015 |

O sistema irá gerar a rotina estadual, CAT 79/2003, com base nos lançamentos fiscais de Energia Elétrica e Telecomunicações, para o estado de São Paulo.

**Parametrização**

Primeiramente, devemos conferir o local onde o sistema salvará os arquivos gerados pela rotina. O *Diretório de Arquivos Temporários(***Opções|Parâmetros|Gerais/Tabelas**  
**-> Rotinas Legais -> Etapa 1***).* Serão selecionados todos os documentos fiscais de Saída, nos quais, o código de modelo do documento(Tipo de Documento |Aba - Dados Adicionais)estão de acordo com as operações de Energia Elétrica e Telecomunicações(06, 21 e 22).

**Tela de Geração**

Na tela de geração da rotina(**Rotinas Legais | Estaduais | Apuração de ICMS -> São Paulo  - CAT 79/2003...**) devem ser informados os seguintes dados obrigatórios: Filial, Período/Intervalo de Geração e a Situação do Arquivo(Normal ou Substituto). Informe também a Rotina Fiscal, previamente cadastrada, contendo os *Valores Campos x Rotinas*, como Tipo de Ligação, Tipo de Utilização, Grupo de tensão e etc.

Selecione o parâmetro *Calcular Código de Autenticação Digital do Documento Fiscal*, caso o Lançamento não esteja com este campo calculado.

**Arquivos Gerados**

Após a execução do processo, os arquivos *Mestre* de Documentos Fiscais, Itens dos lançamentos e Destinatários de Documentos Fiscais serão salvos na pasta do diretório temporário. Os arquivos são gerados conforme nomenclatura descrita na Legislação  da CAT 79/2003.

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.Liber.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
