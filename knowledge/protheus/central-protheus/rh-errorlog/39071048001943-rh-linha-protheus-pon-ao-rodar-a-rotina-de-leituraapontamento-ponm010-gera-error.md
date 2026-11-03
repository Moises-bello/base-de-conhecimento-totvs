---
article_id: 39071048001943
category: RH - Error.log
content_hash: ad5b889f39b65ff60f33b38b6dadaf816b895e2c47c7cc0d7242ae49690edca6
fetched_at: '2026-06-28T22:44:49.524008+00:00'
product: protheus
section_id: 32419193161751
source: central-protheus
title: 'RH - Linha Protheus - PON - Ao rodar a rotina de Leitura/Apontamento (PONM010),
  gera error log: array out of bounds ( 4 of 3 ) on PUTAPONTARES(PONXAPO.PRX)'
type: support-article
updated_at: '2026-03-16T19:51:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39071048001943-RH-Linha-Protheus-PON-Ao-rodar-a-rotina-de-Leitura-Apontamento-PONM010-gera-error-log-array-out-of-bounds-4-of-3-on-PUTAPONTARES-PONXAPO-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39071047959447) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
*Error log* ao rodar a rotina de **Leitura/Apontamento (PONM010)**: ***array out of bounds*** **( 4** ***of*** **3 )** ***on*** **PUTAPONTARES(PONXAPO.PRX)**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para correção do erro gerado, será necessário seguir os passos abaixo:  
**1.** Verifique se existe a **tabela 20 e** todos os identificadores de calculo, essa tabela é gravada na **SX5**;

**2. V**erifique em sua tabela principal [SX5](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014074932-RH-Linha-Protheus-PON-O-que-verificar-quando-gerada-a-mensagem-Este-evento-n%C3%A3o-se-encontra-cadastrado-no-sistema-Tabela-20), se no campo X5\_FILIAL existe alguma filial preenchida, no padrão não existem filiais preenchidas, verifique se não está preenchido somente para uma filial (essa situação também pode ser um problema).  
  
**Saiba mais**  
[Tabela 20- SX5](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014074932-RH-Linha-Protheus-PON-O-que-verificar-quando-gerada-a-mensagem-Este-evento-n%C3%A3o-se-encontra-cadastrado-no-sistema-Tabela-20)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
