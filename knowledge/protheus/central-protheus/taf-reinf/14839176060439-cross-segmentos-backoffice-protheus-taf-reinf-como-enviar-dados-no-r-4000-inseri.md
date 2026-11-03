---
article_id: 14839176060439
category: TAF - REINF
content_hash: b28b4855660ec13cc76b6d5f769ddfc47cc1058b6dccb067fb179b3613ab7c0a
fetched_at: '2026-06-28T22:41:33.490903+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF -  Como enviar dados no
  R-4000 inseridos antes da atualização do sistema?
type: support-article
updated_at: '2024-04-17T18:57:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14839176060439-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-enviar-dados-no-R-4000-inseridos-antes-da-atualiza%C3%A7%C3%A3o-do-sistema
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min****Dúvida** Como enviar dados no R-4000 inseridos antes da atualização do sistema?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12.  
  
**Solução**

Caso alguma das informações solicitadas nos eventos da serie R-4000 tenham sido inseridas no Protheus **antes da atualização do ambiente para a EFD Reinf 2.1** deve ser feito uma das opções abaixo:

* Incluir a informação novamente no sistema atendendo as pré-condições necessárias para o envio dos eventos R-4000
* Lançar os dados diretamente no TAF

Caso for optado por inserir os dados no TAF, seguem abaixo alguns cenários possíveis para auxiliar no procedimento:

**Cenário 1**

A nota de entrada foi incluída na rotina (**MATA103**)  antes da atualização para o REINF 2.1.1, ou seja, sem vinculo com a "**Natureza de Rendimento**" e dentro do período de vigência os eventos R-4000. Possui retenção de IRRF na (emissão) e PIS, COFINS e CSLL com fato gerador no pagamento. Posteriormente foi feita a baixa do título a pagar.

Como no momento da inclusão do título (via Documento de Entrada) não houve o vinculo com a(s) natureza(s) de rendimento, os dados das retenções não foram gravados na tabela **FKW.** No momento da baixa, consequentemente não foi gravada a tabela **FKY**, e dessa forma os movimentos não são integrados  através  Extrator Fiscal (EXTFISXTAF) para o TAF.

Para este cenário é recomendado  inserir os dados do pagamento no TAF de acordo com as etapas abaixo:

1. Inserir a nota fiscal na rotina Documentos de entrada no TAF (**TAFA062**)   ;

2. Inserir o título/fatura na rotina Cadastro de Recibo/fatura (**TAFA448** ) com a retenção do IRRF;

3. Inserir o pagamento do título/fatura na rotina Pagamentos das parcelas  da fatura/ recibo (**TAFA535**)  com as retenções do PIS, COFINS e CSLL;

**Importante:**

 Caso a situação acima ocorra com um título a pagar que não tenha sido originado de um Documento de Entrada, basta pular a etapa 1 do procedimento acima.

**Cenário 2**

O Documento de saída (**MATA461**) foi inserido no sistema antes da atualização do REINF 2.1.1 e dentro do período de vigência, possuindo auto retenção do IRRF (gera TX no contas a pagar). Ou seja, não possui o vinculo com a "Natureza de Rendimento", mas deve estar no evento R-4080.

Para inserir os dados do pagamento no TAF, cadastre as informações  da auto retenção no recebimento na rotina Pagamentos a beneficiários (**TAFA542**) . Se essa situação ocorrer com um título a receber sem vinculo com o Documento de Saída, o procedimento no TAF é o mesmo.
