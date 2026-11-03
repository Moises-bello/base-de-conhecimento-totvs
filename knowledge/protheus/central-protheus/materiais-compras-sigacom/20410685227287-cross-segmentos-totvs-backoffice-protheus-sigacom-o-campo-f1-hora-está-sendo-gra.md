---
article_id: 20410685227287
category: Materiais - Compras (SIGACOM)
content_hash: eb481c3ffe1a7029aa37429b8e9c0aaf74688cb1372df68d8f9b3888b74308e8
fetched_at: '2026-06-28T22:41:12.959762+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: "Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - \t O campo F1_HORA\
  \ está sendo gravado com o horário incorreto."
type: support-article
updated_at: '2024-01-08T17:44:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20410685227287-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-campo-F1-HORA-est%C3%A1-sendo-gravado-com-o-hor%C3%A1rio-incorreto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20410685198359) Tempo aproximado para leitura: **00H05 min****Ocorrência**

"Problema de Registro: Campo F1\_HORA Gravando Horário Incorreto no Documento de Entrada"

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - A partir da Versão 12  
  
**Solução**

Deve-se configurar os parâmetros MV\_HORANFE e MV\_HORARMT.

**MV\_HORANFE**

Utilizado para gravar o campo **Hora** no momento da inclusão do documento de entrada.

.T. = Grava

.F. = Não grava a hora

**MV\_HORARMT**

Define qual horário será gravado no campo F1\_HORA

* MV\_HORARMT = 1
  + Gravar na nota o horário registrado na máquina em que está acessando o **Smartclient**
* MV\_HORARMT = 2
  + Gravar na nota a hora que está registrado **no servidor onde está instalado o Protheus**

**Obs:**Se estiver armazenada no DataCenter da TOTVS, validar junto ao Cloud se o horário do servidor está devidamente ajustado. Caso a Base esteja em servidor próprio, verificar se o servidor está com o horário correto a ser gravado no campo F1\_HORA

* MV\_HORARMT = 3
  + Gravar na nota o horário do servidor, mas adaptar ao fuso horário de cada Filial.

**Obs:**Esta opção é utilizada APENAS para empresas que emitem em uma mesma máquina NFs para diversas Filiais, em que, uma possui fuso horário diferente da outra.

Horário de fuso será calculado utilizando UF da filial logada (M0\_ESTENT) - FwTimeUF

Criar / ajustar os parâmetros MV\_HVERAOI e MV\_HVERAOF conforme boletim técnico:

[MV\_HVERAOI e MV\_HVERAOF - Documentos de Entrada e Saída](https://tdn.totvs.com/pages/releaseview.action?pageId=189316246)

Os parâmetros devem estar como modo compartilhado e registrar neles as datas de Inicio e Final do horário de Verão respectivamente.

O preenchimento é na ordem inversa, exemplo: 20151018

Importante

Tendo realizado as devidas configurações, deve-se excluir o Documento de Entrada e realizar novamente a entrada do documento, para então, gravar o campo F1\_HORA corretamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20410695887383)

***Saiba Mais :***

*[PCOM12076 - Documento de Entrada - Gravação F1\_HORA](https://tdn.totvs.com.br/pages/releaseview.action?pageId=818456857)*

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
