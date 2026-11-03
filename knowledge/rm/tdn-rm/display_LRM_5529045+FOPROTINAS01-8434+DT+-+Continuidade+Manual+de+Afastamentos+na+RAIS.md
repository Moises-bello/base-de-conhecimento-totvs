---
content_hash: d5b67dfb0435fc17399a97cf5fac3975e34fdf82638d02cbfe4c790d49edd6c9
fetched_at: '2026-06-29T00:10:21.890807+00:00'
page_id: '494803638'
product: rm
source: tdn-rm
title: 5529045 FOPROTINAS01-8434 DT - Continuidade Manual de Afastamentos na RAIS
type: documentation
url: https://tdn.totvs.com/display/LRM/5529045+FOPROTINAS01-8434+DT+-+Continuidade+Manual+de+Afastamentos+na+RAIS
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Recursos Humanos |
| Módulo: | Folha de Pagamento |
| Função: | RAIS |
| Ticket: | 5529045 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FOPROTINAS01-8434 |

## **02. SITUAÇÃO/REQUISITO**

O parâmetro "Habilita controle manual de continuidade de afastamentos com atestado médico" (Configurações >> Parâmetros >> Parametrizador >> Folha de Pagamento >> Folha Normal >> Afastamento - ) não estava sendo contemplado na geração da RAIS. Assim, mesmo que o cliente optasse pelo controle manual da continuidade de afastamentos, marcando o parâmetro, a RAIS verificava a continuidade automática de afastamentos.

## **03. SOLUÇÃO**

O processo de geração da RAIS foi adaptado para contemplar o parâmetro "Habilita controle manual de continuidade de afastamentos com atestado médico". Assim, quando o parâmetro estiver marcado, a continuidade de afastamentos passa a ser verificada através do campo "Dt. Inicial da Continuidade de Aft." (). Quando o parâmetro estiver desmarcado, é feita a verificação automática de continuidade, que ocorre quando os afastamentos possuem o mesmo motivo. Em ambos os casos, deve ser respeitada a carência para que afastamentos sejam considerados continuidade um do outro (parâmetro "Dias de carência para afastamentos com atestado médico" - Configurações >> Parâmetros >> Parametrizador >> Folha de Pagamento >> Folha Normal >> Afastamento - ). Essa carência é sempre verificada em relação ao afastamento imediatamente anterior da sequência de continuidade.

Exemplo:

Dias de carência para afastamentos com atestado médico = 60

Com o controle automático, nenhum afastamento seria considerado continuidade do outro na RAIS, pois são de motivos diferentes, mesmo que o intervalo do fim de um ao começo do outro respeite a carência.

Já com o controle manual, o segundo e terceiro afastamentos seriam continuidade do primeiro, uma vez que o campo de data inicial da continuidade de afastamentos de ambos aponta para o primeiro e a carência entre o primeiro e o segundo e entre o segundo e terceiro afastamentos é respeitada.

| Data Inicial | Data Final | Tipo | Motivo | Data Inicial da Continuidade de Afastamento |
| --- | --- | --- | --- | --- |
| 01/05/2019 | 15/05/2019 | T - Acidente de trabalho | 2 | - |
| 03/06/2019 | 12/06/2019 | P - Afastamento pela previdência | 3 | 01/05/2019 |
| 17/06/2019 | 19/06/2019 | P - Afastamento pela previdência | 5 | 01/05/2019 |

## **04. DEMAIS INFORMAÇÕES**

Outras ações/ações relacionadas 

**Independente de o parâmetro estar marcado ou não, deve ser respeitada a carência para que afastamentos sejam considerados continuidade um do outro (parâmetro "Dias de carência para afastamentos com atestado médico"). Essa carência é sempre verificada em relação ao afastamento imediatamente anterior da sequência de continuidade.IMPORTANTE!**

## **05. ASSUNTOS RELACIONADOS**


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
