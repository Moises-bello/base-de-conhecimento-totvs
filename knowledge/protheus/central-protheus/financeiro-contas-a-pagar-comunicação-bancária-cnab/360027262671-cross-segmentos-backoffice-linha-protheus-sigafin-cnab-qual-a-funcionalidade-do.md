---
article_id: 360027262671
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 6f96cf79bfa15696f40791c29fcf2e8b43911061158fee090579d318c9b3cd48
fetched_at: '2026-06-28T22:37:55.359110+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - Qual a funcionalidade
  do parâmetro: MV_BXCNAB'
type: support-article
updated_at: '2026-04-13T12:14:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027262671-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Qual-a-funcionalidade-do-par%C3%A2metro-MV-BXCNAB
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21067006647447)**Tempo aproximado para leitura: **00:05:00min**  
  
**Dúvida**  
Qual a funcionalidade do parâmetro: **MV\_BXCNAB**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CNAB - Todas as versões  
  
**Solução**  
O parâmetro: **MV\_BXCNAB**, possui a funcionalidade de realizar a gravação do registro totalizador da tabela **SE5** que gere o movimento bancário no **retorno de cobrança / pagamento (FINA200/FINA430)**.  
  
**Exemplo:**  
Um arquivo de retorno com 10 títulos que devem ser baixados. Caso o parâmetro: **MV\_BXCNAB** estiver com **conteúdo N**, será gravado 10 registros na tabela **SE5** com conteúdo no campo **E5\_TIPODOC=VL**, ou seja, cada registro gerou movimento bancário e apresentará no **Extrato Bancário**(FINR470) e na **Conciliação Bancária**(FINA380) sendo necessário conciliar cada registro.  
  
Realizado o retorno **CNAB** do mesmo arquivo, mas com o parâmetro: **MV\_BXCNAB=S.** Será gravado 11 registros na tabela **SE5**. Onde os 10 registros serão gravados com conteúdo: **E5\_TIPODOC=BA**, não gera movimento bancário. Mas o registro 11 será gravado com **E5\_TIPODOC=VL**, com o valor totalizador gera movimento bancário. Apresenta no relatório **Extrato Bancário**(FINR470) o valor total soma os 10 registros e consequentemente  na **Conciliação Bancária** será conciliado o valor totalizador.

Para taxa ou despesa bancária (exemplo: cobrança de impressão de boleto que o banco faz para o cliente) irá funcionar da mesma forma acima, aglutinando ou não dependendo do parâmetro.

**Importante:**  
A funcionalidade desse parâmetro é validado nas rotinas **FINA090**, **FINA091**, **FINA110**, **FINA200** e **FINA430.** A despesa bancária somente é gerada através das rotinas FINA200 e FINA430.

Saiba Mais:

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - FINA110 gerando movimento individualizado mesmo com MV\_BXCNAB ativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/39671850533527-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA110-gerando-movimento-individualizado-mesmo-com-MV-BXCNAB-ativo)
