---
article_id: 9782107686167
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 25a170cfaa76c0c3c2c83f9efe70d1f94b851609eda4d042fc583156a1f68a2a
fetched_at: '2026-06-28T22:37:55.159322+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - CNAB - Como atualizar
  campo E5_AUTBCO no retorno CNAB
type: support-article
updated_at: '2022-11-03T20:52:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9782107686167-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Como-atualizar-campo-E5-AUTBCO-no-retorno-CNAB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como atualizar campo E5\_AUTBCO no retorno CNAB?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Para tratar o retorno do **CNAB** com a autenticação no pagamento e atualizar o campo **E5\_AUTBCO**, é necessário estruturar o layout de retorno e utilizar as variáveis **SEGMENTO** e **AUTENTICACAO** no registro de detalhe do **segmento Z**.  
Autenticação Bancária faz parte do Registro detalhe do **bloco Z posição 79 a 103 possui 25 dígitos** alfanumérico, o campo referente no Protheus **E5\_AUTBCO** segue essa legislação por esse motivo o campo tem essa quantidade de caracteres fixo justamente para proteger de erros onde e bloqueado para aumento de tamanho.

Contudo uma opção pode ser considerada que é a utilização do ponto de entrada **F430VAR** que tem como finalidade tratar os dados para baixa CNAB.  
[F430VAR - Permite manipulação das Variáveis Private durante a baixa CNAB (Pagar)](https://tdn.totvs.com/pages/releaseview.action?pageId=641447402)  
  
**Saiba mais**  
[Segmento Z –Autenticação do pagamento](https://tdn.totvs.com/display/public/PROT/FIN0018_CNAB_Segmento_Z_autenticacao_do_pagamento)
