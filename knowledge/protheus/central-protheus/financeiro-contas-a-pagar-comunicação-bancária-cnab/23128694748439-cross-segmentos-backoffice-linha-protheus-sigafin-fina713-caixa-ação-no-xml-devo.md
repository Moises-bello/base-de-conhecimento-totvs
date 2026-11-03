---
article_id: 23128694748439
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: eeb8583ae558406a97b3339b15f2253dc36156bdb0194f67bd504b0150ce674f
fetched_at: '2026-06-28T22:37:56.309358+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Caixa - Ação
  no XML Devolver x Protestar
type: support-article
updated_at: '2024-04-29T17:04:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23128694748439-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Caixa-A%C3%A7%C3%A3o-no-XML-Devolver-x-Protestar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23128679918999) Tempo aproximado para leitura: **00:05:00min** **Dúvida**Como configurar a quantidade de dias para devolução ou protesto do boleto do banco Caixa transmitido via API(FINA713)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - A partir da release 12.1.33  
  
**Solução**Especificamente para o Banco Caixa, caso queira utilizar a ação **DEVOLVER**, deve deixar o conteúdo do campo **EE\_DIASPRT (campo dos parâmetros de banco) 2 ou 0**.  
Caso queira **DEVOLVER** o boleto com mais dias, deve alterar o **EE\_DIASPRT**, porém, a ação enviada para o banco no XML será **PROTESTAR** ao invés de **DEVOLVER**.  
Este é o funcionamento padrão e como foi desenvolvido para o Banco Caixa, diferente de outros bancos que possui a configuração de devolução separada utiliza o campo **EE\_DIASREC**. O Banco Caixa valida somente o campo**EE\_DIASPRT.**  
**Saiba mais:**[Caixa Econômica Federal - Configuração Boletos - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=652406360)
