---
article_id: 32792869776663
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 2c7bd41cd84a1e2bb19079aa74d853fd3377ed0d80fa7befedee25b294aa631a
fetched_at: '2026-06-28T22:37:21.699906+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Conceito dos Títulos
  Provisórios (PR) gerados no Gestão de Contratos
type: support-article
updated_at: '2026-06-15T13:41:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32792869776663-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Conceito-dos-T%C3%ADtulos-Provis%C3%B3rios-PR-gerados-no-Gest%C3%A3o-de-Contratos
---

No módulo Gestão de Contratos do Protheus, títulos provisórios (PR) são gerados para parcelas do cronograma financeiro ao tornar o contrato vigente, enquanto essas parcelas não são medidas. Após a medição, são criados documentos efetivos (Pedidos ou Títulos Financeiros) e os títulos PR correspondentes são excluídos. Medições parciais geram um novo título PR para o saldo restante. Os títulos PR não se relacionam aos itens da planilha, apenas ao montante e parcelas do cronograma.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32792878897431) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Qual o Conceito dos Títulos Provisórios (PR) gerados no Gestão de Contratos

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

No módulo de Gestão de Contratos para os Contratos que possuem Cronograma Financeiro, são gerados títulos "PR" referente às parcelas desse Cronograma incluido para o contrato. Eles são gerados ao tornar o contrato Vigente, quando com o parâmetro "**MV\_CNPROVI** = **S"**. Pelo conceito do módulo, esses títulos são existentes apenas enquanto estas parcelas do Cronograma não são medidas.

Quando são realizadas a medições e estas são encerradas são gerados no encerramento da medição os documentos efetivos desta parcela do cronograma que foi medida, podendo este documento efetivo gerado ser um Pedido (de Compra ou de Venda a depender se o contrato é de um tipo ou do outro) ou um Titulo Financeiro a Pagar ou a Receber [a depender também se o contrato é de Compra (a Pagar) ou de Venda (a receber)], e o título PR da parcela medido é excluido.

Abaixo artigo que reporta onde definir se será gerado Pedido ou Título na medição do contrato:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como configurar o Gestão de Contratos para gerar Títulos Financeiros ou Pedidos no encerramento da medição ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037188314-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-configurar-o-Gest%C3%A3o-de-Contratos-para-gerar-T%C3%ADtulos-Financeiros-ou-Pedidos-no-encerramento-da-medi%C3%A7%C3%A3o)

Caso seja feita uma medição parcial da parcela do cronograma, ao ser encerrada a medição, o título referente à parcela é excluido, e é gerado um outro título "PR" com o valor do saldo restante da parcela que ficou ainda para ser medido.

Por padrão, o módulo não possui uma funcionalidade ou parametrização para não serem excluidos os titulos PR referente às parcelas do Cronograma Financeiro quando é realizado o encerramento das medições das parcelas.

***Obs:***

Por conceito do módulo, os títulos "PR" não possuem relacionamento aos itens existentes na planilha do contrato, mas sim apenas ao montante e às parcelas do Cronograma Financeiro que é incluido para a planilha do contrato.

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como desativar a geração de títulos provisórios na mudança de situação do contrato ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018381871-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-desativar-a-gera%C3%A7%C3%A3o-de-t%C3%ADtulos-provis%C3%B3rios-na-mudan%C3%A7a-de-situa%C3%A7%C3%A3o-do-contrato)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - É possível excluir o Título Provisório (PR) gerado no Financeiro pelo Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028358612-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-%C3%89-poss%C3%ADvel-excluir-o-T%C3%ADtulo-Provis%C3%B3rio-PR-gerado-no-Financeiro-pelo-Gest%C3%A3o-de-Contratos)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - É possivel Baixar ou Movimentar no módulo Financeiro um Titulo Provisório do Cronograma Financeiro gerado pelo Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406264645143-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-%C3%89-possivel-Baixar-ou-Movimentar-no-m%C3%B3dulo-Financeiro-um-Titulo-Provis%C3%B3rio-do-Cronograma-Financeiro-gerado-pelo-Gest%C3%A3o-de-Contratos)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Alterar numeração sequencial dos títulos provisórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407740093463-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Alterar-numera%C3%A7%C3%A3o-sequencial-dos-t%C3%ADtulos-provis%C3%B3rios)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
