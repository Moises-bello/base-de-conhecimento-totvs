---
article_id: 29772075860119
category: SIGAEST - MOVIMENTAÇÕES
content_hash: fb50d14f6d96187c06496016053cd0f285edca004765405907a1259d29ced432
fetched_at: '2026-06-28T22:38:54.271185+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - A103VALOR O valor
  total do item a ser devolvido é maior que o saldo disponível no poder de terceiros
type: support-article
updated_at: '2025-03-12T12:28:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29772075860119-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-A103VALOR-O-valor-total-do-item-a-ser-devolvido-%C3%A9-maior-que-o-saldo-dispon%C3%ADvel-no-poder-de-terceiros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29772059422999) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao devolveu saldo de terceiros ocorre o help A103VALOR, saldo é maior que o disponivel de tecerios.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Deve-se efetuar exatamente o valor da remessa.

**Quando o help A103VALOR exibir a seguinte mensagem:**

***"O valor total do item a ser devolvido é maior que o saldo disponível no poder de terceiros."***

Essa mensagem vai ocorrer no momento da devolução de um item pertencente a terceiros, indicando que o **valor da devolução ultrapassa o saldo disponível** para aquele item dentro do controle de saldos de terceiros.

Isso acontece porque, no controle de saldos de terceiros, o valor total das devoluções não pode ultrapassar o valor original da remessa. Isso significa que qualquer movimentação de devolução deve respeitar os limites definidos **pelo saldo da remessa de origem.**

**Os principais fatores que podem levar a essa mensagem:**

1. **Devolução superior ao saldo da remessa:** O sistema verifica se o valor a ser devolvido é maior do que o saldo existente da remessa.
2. **Divergência nos valores unitários:** Se a devolução for registrada com um valor unitário diferente da remessa original, pode ocorrer uma discrepância no saldo total.
3. **Movimentações manuais no saldo:** Caso tenham sido realizadas movimentações manuais no saldo de terceiros, isso pode gerar inconsistências.
4. **Remessa original com saldo zerado ou insuficiente:** Se a remessa original já foi consumida de alguma forma, e não há saldo disponível para devolução.

**Porque existe esse controle:**

O controle de saldos de terceiros é essencial para manter a integridade das informações de movimentação de materiais e assegurar que as devoluções respeitem as remessas originais. A obrigatoriedade de manter o mesmo saldo da remessa se baseia em alguns pontos:

1. **Rastreabilidade e Auditoria:** Para garantir que todos os itens enviados e devolvidos estejam devidamente contabilizados, evitando inconsistências fiscais e financeiras.
2. **Prevenção de Estoques Negativos:** Se não houvesse esse controle, seria possível devolver mais do que foi recebido, gerando distorções no estoque.
3. **Alinhamento com Obrigações Legais e Fiscais:** A remessa de terceiros muitas vezes está vinculada a documentos fiscais específicos, sendo necessário respeitar os valores registrados para evitar inconsistências com a Receita Federal ou outros órgãos reguladores.

**Saiba mais:**

*[Guia de Referência do Bloco K - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=235589625)*

*[Link para download do Guia Prático da Escrituração Fiscal Digital - EFD na última versão](http://sped.rfb.gov.br/pasta/show/1573)*

*[MP - SIGAEST- Como definir um tipo de produto que não seja padrão do sistema para que seja considerado no Bloco K (K200)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033136554-MP-SIGAEST-Como-definir-um-tipo-de-produto-que-n%C3%A3o-seja-padr%C3%A3o-do-sistema-para-que-seja-considerado-no-Bloco-K-K200-?source=search)*

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
