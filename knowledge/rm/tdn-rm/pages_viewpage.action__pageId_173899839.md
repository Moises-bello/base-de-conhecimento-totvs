---
content_hash: 3383e8c29e443078c713f6d3941bbff8be936aa002614e64d48bc3c1cfc5affc
fetched_at: '2026-06-29T00:05:57.621805+00:00'
page_id: '173899839'
product: rm
source: tdn-rm
title: Como Fazer - Aumentar o número máximo de registros na visão de Lançamentos
  no RM Liber
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=173899839
version: 1
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | TOTVS Gestão Fiscal – **Versão:** 11.82 |
| **Processo** | : | Lançamentos Fiscais |
| **Subprocesso** | : | Aumentar o número máximo de registros na visão de Lançamentos |
| **Data da publicação** | : | 24/11/2014 |

**Introdução**   
 Processo para aumentar o número máximo de registros na visão de Lançamentos do TOTVS Gestão Fiscal.

**Desenvolvimento/Procedimento:**

• No RM LIBER.exe - Acesse "Cadastros" / "Segurança" / "Administrativa" / "Servidores de Aplicação" Selecione a opção "Incluir"

• Caso esteja usando a nova MDI - RM.EXE , acesse a opção Serviços Globais

• Na guia Serviços, acesse a opção Servidores de Aplicação

• De acordo com os prints abaixo, clique no botão "ID do Server:" e pesquise pelas seguintes descrições:

-Para Lançamentos de Entrada ID SERVER = FisLanFiscalEntradaData

-Para Lançamentos de Saída ID SERVER = FisLanFiscalSaidaData

• Informe o Número máximo de Registros desejado conforme exemplo abaixo e clique em "OK".

• Após isso, faça Logout\Login, e ao acessar a tela de lançamentos será exibido o número registros que foi definido. 

Para maiores informações:

Icon

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

<http://fluig.totvs.com/portal/p/10097/subject/rfiscal>  

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
