---
article_id: 360047032774
category: Comércio Exterior - Easy Export Control - Tabelas
content_hash: 2dbfbbd0f8a060e15eacbf81f678ec797b1dd5eed66763ccd8de66c5c62e592d
fetched_at: '2026-06-28T22:37:01.413763+00:00'
product: protheus
section_id: 1500001549222
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Condição de pagamento
type: support-article
updated_at: '2026-02-25T11:44:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047032774-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Condi%C3%A7%C3%A3o-de-pagamento
---

**Dúvida**  
Como realizar o cadastro de condição de pagamento?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões.  
  
**Solução**  
As condições de pagamento identificam a forma de recebimento dos valores faturados e exportados. Esta tabela apresenta três tipos de Condições de Pagamento para as mercadorias exportadas:  
**À vista:** recebimento único do valor com vencimento na Data de Embarque.  
**Normal:** recebimento único do valor com data de vencimento de 1 a 899 dias a contar da data de embarque.  
**Parcelado:** destinado a parcelamento do valor em até 10 parcelas, aceitando apenas parcelas com data de vencimento depois da data de embarque (maiores que zero).

**Importante:** No módulo *Easy Export Contol* a condição de pagamento é utilizada apenas para as parcelas que não são de adiantamento, portanto será utilizada apenas para parcelas à vista, a prazo ou parcelados, com vencimento igual ou maior que a data de embarque.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069318573)

Como realizar o cadastro de condição:

1. Selecione o menu Atualizações\Tabelas\Cond.Pgtos.  
2. Clique na opção Incluir e informe os seguintes dados:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068197714)  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068197774)  
3. Caso a condição seja do tipo “Parcelado”, o sistema preencherá automaticamente o campo "No. de Dias" com o valor 901 e será necessário definir os percentuais e prazos de cada parcela, utilizando os campos disponíveis na pasta Parcelas. Para condições do tipo “Normal” estes campos estarão desabilitados. Para condições “A Vista”, o sistema preencherá automaticamente o campo "No. de Dias" com o valor -1, indicando que o desembolso ocorrerá no momento do embarque. Lembrando que somente são aceitos parcelas com vencimento a partir da data de embarque.  
4. Para inserir a descrição da condição de pagamento em outro idioma, em Outras Ações \ Incluir e informe Idioma e Texto.  
5. Confira os dados e clique sobre o botão Confirmar para gravar a descrição no idioma e Confirmar novamente para efetivar a gravação da condição de pagamento.  
  
**Importante:** Caso o módulo *Easy Export Control* esteja integrado com o módulo de Faturamento, será necessário preencher o campo “C.PagtoSiga”, relacionado os cadastros de condição de pagamento.

Mais informações: [Condições de Pagamentos (EECAT130 - SIGAEEC)](https://tdn.totvs.com/pages/releaseview.action?pageId=312157729)
