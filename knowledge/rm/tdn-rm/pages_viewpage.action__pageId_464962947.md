---
content_hash: 4a65788ddb0d1c366ac07d196fa3c3374681579cd77e7b8cb2910d6f082277b9
fetched_at: '2026-06-29T00:10:15.364960+00:00'
page_id: '464962947'
product: rm
source: tdn-rm
title: 3594614 FISCAL01-8069 DT Escrituração - Erro Escrituração Fiscal de Movimentos
  de Saida Utilizando SubSerie
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=464962947
version: 4
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Escrituração |
| Ticket: | 5141948 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-8069 |

**02. SITUAÇÃO/REQUISITO**

Ao utilizar uma subsérie com 4 caracteres no movimento, no momento de escriturar o sistema está retornando a mensagem abaixo:

\***"String or binary data would be truncated"e truncated"**\*

\***Ao verificar o campo DLAF.SUBSERIE o tamanho do campo só está permitindo 3 caracteres.**\*

**03. SOLUÇÃO**

Ajuste na série e subsérie aumentando o campo para 20 dígitos.

Foi ajustado as seguintes tabelas:

DATIVO, DATIVOCOMPONENTE, DCTEDOC, DCTEDOCHISTORICO, DCTRC, DCTRCHISTORICO, DDISPOSITIVOEXTRAVIADO, DITMAIDF, DLAF, DLAFHISTORICO, DLDCNF, DNFTERCEIROS, DNFTERCEIROSHISTORICO , DPARAMETROS.

**Esta implementação foi realizada oficialmente na versão 12.1.24. Para as versões 12.1.23 e 12.1.22 é necessário executar o script LI.2019.03\_01IMPORTANTE!**

div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
