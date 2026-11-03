---
article_id: 41461914735767
category: TOTVS RH (Linha RM)
content_hash: 7b30a3b965f992db25d336e5850418eea1f0841301d0e0145999fd8453483a04
fetched_at: '2026-06-28T22:46:21.754038+00:00'
product: rm
section_id: 360011673474
source: central-rm
title: RH - RM - FOP - Lote contábil da Folha de Pagamento gerado em duplicidade na
  Contabilidade
type: support-article
updated_at: '2026-06-24T18:17:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41461914735767-RH-RM-FOP-Lote-cont%C3%A1bil-da-Folha-de-Pagamento-gerado-em-duplicidade-na-Contabilidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41461914718743) Tempo aproximado para leitura: **00:01:05 min**  
  
**Dúvida**  
No módulo **Folha de Pagamento,** por que um lote contábil gerado pela Folha de Pagamento está chegando duplicado na Contabilidade, apresentando dois registros com o mesmo identificador (ID)?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - Todas as versões  
  
**Solução**  
Quando um lote contábil da Folha de Pagamento é identificado em duplicidade na Contabilidade, é necessário validar se houve alguma inconsistência durante o processo de integração ou se o lote foi integrado mais de uma vez.

Nesses casos, recomenda-se realizar a exclusão do lote contábil gerado incorretamente e efetuar uma nova integração, garantindo a consistência das informações entre os módulos.  
  
**Passos**

* Identifique o lote que se encontra duplicado na Contabilidade.
* Valide se os lançamentos possuem o mesmo identificador e origem na Folha de Pagamento.
* Realize a exclusão do lote contábil conforme procedimento documentado.
* Gere novamente o lote contábil na Folha de Pagamento.
* Efetue uma nova integração para a Contabilidade.
* Valide se o lote foi integrado apenas uma vez e se os valores estão consistentes.

**Importante**  
Antes de realizar qualquer exclusão, recomenda-se que o processo seja validado pela equipe responsável pela Contabilidade, garantindo que o lote duplicado não tenha sido utilizado em processos posteriores.

Caso a duplicidade persista após a exclusão e nova integração, será necessário abrir um chamado junto ao Suporte TOTVS para análise detalhada do cenário.  
  
**Saiba mais**  
[RH - RM - FOP - Exclusão de lote contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001533881-RH-RM-FOP-Exclus%C3%A3o-de-lote-cont%C3%A1bil)
