---
article_id: 360059770253
category: RH - Error.log
content_hash: 4976ee38a96b0ed67e59998470e86647bf4ee58e267abc70526a3e6a7ad377db
fetched_at: '2026-06-28T22:44:49.560656+00:00'
product: protheus
section_id: 32419193161751
source: central-protheus
title: 'RH - Linha Protheus - PON - Ao realizar a Leitura e Apontamento das Marcações,
  é gerado Error Log - argument #1 error, expected N->U, function padr on PUTMARCACOES(PONXFUN.PRX)'
type: support-article
updated_at: '2025-06-18T14:14:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059770253-RH-Linha-Protheus-PON-Ao-realizar-a-Leitura-e-Apontamento-das-Marca%C3%A7%C3%B5es-%C3%A9-gerado-Error-Log-argument-1-error-expected-N-U-function-padr-on-PUTMARCACOES-PONXFUN-PRX
---

**Ocorrência**Ao realizar a **Leitura e Apontamento das Marcações** através da rotina **PONM010,** é gerado *Error Log*: ***argument* #1 *error*, *expected* N->U, *function padr on* PUTMARCACOES(PONXFUN.PRX)****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**O erro ocorre quando os campos **P8\_LATITU** e **P8\_LONGIT**, ambos da tabela **SP8**, estão fora do **dicionário/ordenação padrão** da TOTVS.   
  
**Solução**Para solucionar o erro, é necessário que os campos **P8\_LATITU** e **P8\_LONGIT** da tabela **SP8** fiquem na **estrutura** do **dicionário padrão** conforme exemplo abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098177074)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100431473)  
  
A **ordem dos campos** devem estar **dentro do padrão da TOTVS**, conforme exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14328027569175)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14328071878679)  
  
**Saiba Mais:**Pacote de Expedição Contínua do Gestão de Pessoal: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>  
Manual do Ponto Eletrônico: <https://tdn.totvs.com/pages/releaseview.action?pageId=630823373>
