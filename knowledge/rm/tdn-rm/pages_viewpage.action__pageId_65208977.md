---
content_hash: 6042d05f58c3c39fa49f90b2ffc071e69550d9761df2e7bdf37c8595f960eda5
fetched_at: '2026-06-29T00:11:12.281927+00:00'
page_id: '65208977'
product: rm
source: tdn-rm
title: RMFIS00006_Sintegra - Arquivo Eletrônico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=65208977
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.52 |
| **Processo** | **:** | Rotinas Estaduais - Arquivos Eletrônicos |
| **Subprocesso** | **:** | Sintegra |
| **Data da publicação** | **:** | 05/07/2013 |

O objetivo deste documento é apresentar a geração do arquivo eletrônico do **SINTEGRA**, comum a todos os Estados do Brasil. A rotina do **SINTEGRA** é gerado através do menu **Rotinas Legais / Rotinas/Estaduais / SINTEGRA.**

 

Preencha as informações solicitadas na tela da rotina e acordo com o objetivo do arquivo.

**Atenção para o preenchimento do Convênio!**

Utilize sempre o último convênio que contém as últimas alterações de layout determinadas pelo Fisco, exceto, é claro, sob orientação contrária de sua Unidade de Federação. O arquivo será gerado com o nome *default* **“REGISTRO.TXT”**, mas, você pode alterá-lo se assim o desejar.

O arquivo será gravado no diretório de arquivos temporários informado nos parâmetros. Toda a geração da rotina é baseada no Código do Modelo do Documento informado no Cadastro do Tipo de Documento, pasta Dados Adicionais. Portanto, muita atenção no preenchimento desse campo.

O próprio Manual disponibilizado pelos Estados descreve quais Modelos de Documento devem ser informados em cada um dos Registros. Os erros mais comuns que ocorrem na validação do arquivo dizem respeito à cadastros e/ou informações incorretas nos lançamentos fiscais. 

Por exemplo: 

+ Série inválida – informe a série correta no lançamento fiscal.
+ CFOP de transporte informado no Registro 50 – neste caso, o código do modelo do documento informado não corresponde a uma operação de transporte. Ajuste o Cadastro do Tipo de Documento.
+ Falta de Registro 54 para registro 50 – informe a situação tributária do ICMS no Cadastro da Natureza.

**Informações Adicionais**

Para mais informações sobre a geração do arquivo, consulte o nosso Help.

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
