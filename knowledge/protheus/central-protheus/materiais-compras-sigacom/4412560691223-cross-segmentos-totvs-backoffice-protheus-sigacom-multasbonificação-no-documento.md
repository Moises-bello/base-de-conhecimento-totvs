---
article_id: 4412560691223
category: Materiais - Compras (SIGACOM)
content_hash: 994eb65caad3a327156427c74c8d6aa5931eab8650ae85e4a3b950c65adeeef5
fetched_at: '2026-06-28T22:41:20.216761+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Multas/Bonificação
  no Documento de Entrada '
type: support-article
updated_at: '2022-10-26T14:00:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412560691223-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Multas-Bonifica%C3%A7%C3%A3o-no-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02 min** **Dúvida**

Qual o procedimento para gerar multa e bonificação no Documento de Entrada?

**Ambiente**

Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Versão 12

**Solução**

Para utilizar esse recurso, o documento de entrada deve ter origem no **Pedido de Compras** vinculado à medição de contratos; ou seja, é necessário utilizar o procedimento de recebimento de produtos/serviços do Gestão de Contratos, a A multa é avaliada para cada registro, originado a partir de uma medição e empregado na Nota Fiscal de Entrada.

Procedimento :

1. No cadastro Tipos de Contratos, configurar os campos **Multa/Bonif**. e **Mult. Manual**:
2. No cadastro de Fórmulas elaborar duas fórmulas, uma para a condição de aplicação de multa e outra para o valor a ser aplicado.

   Expressão da condição:

     3. No cadastro de Multas/Bonificações configurar a multa a ser aplicada no momento da digitação do documento de entrada.

Para efetuar a inclusão de uma multa/bonificação é necessário empregar duas fórmulas: a de cálculo do valor e a de condição de aplicação.

A multa ou bonificação não é inserida automaticamente, é necessário um aval do operador para que seja aplicada, mesmo que esteja prevista no contrato. Raramente é aplicada sem que ocorra negociação prévia entre as partes envolvidas (fornecedor e cliente).

5. Para avaliar a multa, no momento da digitação do documento de entrada, clicar em **Multas**.

As multas podem ser avaliadas a qualquer momento da etapa de inclusão do documento de entrada, mas recomenda-se que sua avaliação seja efetuada apenas quando todos os dados do documento já estiverem informados. Caso contrário, o Sistema poderá avaliar as multas, baseado em informações incompletas.

6. Como padrão, o Sistema efetuará a reavaliação das multas, toda vez que a janela é carregada. Todas as multas existentes são apresentadas como desmarcadas. Confirmar a aplicação, dando duplo clique sobre a multa desejada.

7. Conferir os dados e confirmar a tela para que o Sistema os aplique. A reavaliação automática, realizada pelo Sistema ao carregar a janela, não considera alterações efetuadas posteriormente, por exemplo, marcar uma multa e confirmá-la é um processo que ocorre já com a janela carregada. Nesse caso, somente ao carregar novamente a janela, a situação atual será apresentada.

8. As multas ou bonificações são efetivamente aplicadas na gravação do documento de entrada. O valor resultante, positivo ou negativo, é considerado como acréscimo ou decréscimo do título a pagar, gerado no financeiro, que será gravado nos campos **Acréscimo** (SE2->E2\_ACRESC) e **Sld. Acresc.** (SE2->E2\_SDACRES).

Saiba mais em  : [Multa e Bonificação](https://tdn.totvs.com/x/US9KEg)
