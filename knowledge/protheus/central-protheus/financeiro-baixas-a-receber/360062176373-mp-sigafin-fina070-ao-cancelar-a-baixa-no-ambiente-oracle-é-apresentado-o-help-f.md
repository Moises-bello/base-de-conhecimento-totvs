---
article_id: 360062176373
category: Financeiro - Baixas a Receber
content_hash: 16c890119c6372653f73e15e07a5a1c21b7840eb8ec063917bb107ea36bc8cdf
fetched_at: '2026-06-28T22:37:43.824076+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: 'MP - SIGAFIN - FINA070 - Ao cancelar a baixa no ambiente Oracle é apresentado
  o HELP: FINCOMBX devido ao campo E5_SEQ estar divergente'
type: support-article
updated_at: '2025-07-30T17:55:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062176373-MP-SIGAFIN-FINA070-Ao-cancelar-a-baixa-no-ambiente-Oracle-%C3%A9-apresentado-o-HELP-FINCOMBX-devido-ao-campo-E5-SEQ-estar-divergente
---

**Ocorrência**Ao cancelar a baixa pela rotina FINA070 é apresentado o HELP: **FINCOMBX** devido ao campo **E5\_SEQ** estar divergente. (Ambiente Oracle)

**Ambiente**Microsiga Protheus – Financeiro – FINA070 – A partir da versão 12  
  
**Causa**O erro ocorre por deixar a sequência **E5\_SEQ** divergente não sendo possível realiza o cancelamento de uma baixa, acontece devido ao parâmetro **CURSOR\_SHARING** do banco de dados ***ORACLE*** está preenchido com o conteúdo ***FORCE***. Faz com que as literais sejam trocadas para variáveis *Bind*, realiza assim a troca de todas as literais para *Bind*. Deste modo, influencia diretamente no tamanho do campo retornado.   
  
**Solução**Analise com o *DBA* da empresa como está configurado o parâmetro **CURSOR\_SHARING*,*** caso ele esteja com o conteúdo **FORCE**, deverá alterar para o conteúdo **EXACT** para o correto funcionamento do processo. Após realizar o procedimento realizar o *refresh* do ambiente.

**Saiba mais**  
<https://tdn.totvs.com/display/tec/Oracle+Database+19.3+Enterprise>
