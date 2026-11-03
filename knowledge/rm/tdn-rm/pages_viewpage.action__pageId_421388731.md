---
content_hash: a43538900d51efc737f76ca0757d5416d522558be54e4d0c5a6a283e339bbb81
fetched_at: '2026-06-29T00:09:18.612564+00:00'
page_id: '421388731'
product: rm
source: tdn-rm
title: Repasse de lançamentos Financeiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388731
version: 5
---

O Repasse consiste em um ou mais Lançamentos a receber e em aberto gerarem outro(s) Lançamento(s) a pagar a partir de um valor percentual da soma dos valores originais e que será repassado a um determinado Fornecedor.  Para gerar o repasse, selecione o(s) Lançamento(s) desejado(s), Processos /Gerar Repasse: Fornecedor / Nome Fantasia: Selecione o fornecedor no qual será repassado um valor do(s) lançamento(s) selecionado(s).

Percentual

Informe o percentual do valor do(s) lançamento(s) selecionado(s) que será repassado ao fornecedor.

Valor

Informe o valor do(s) lançamento(s) selecionado(s) que será repassado ao fornecedor.

Política de Repasse

Esta política será aplicada na data de vencimento do(s) lançamento(s) a pagar gerados no repasse, ao baixar o(s) lançamento(s) a receber. Existem 2 políticas, para o caso do lançamento ser baixado em dia ou em atraso.

**Exemplo**:

Caso a política de repasse seja preenchida assim:

* Em Dia
* Mesmo dia 0
* Em Atraso
* Após 3 dia 3

Se o lançamento a receber for baixado em dia, a data de vencimento do lançamento a pagar gerado no repasse será a mesma da baixa. Se o lançamento a receber for baixado em atraso, a data de vencimento do lançamento a pagar gerado no repasse será 3 dias após a data da baixa.

Filial

Selecione a Filial para o lançamento de Repasse.

Tipo Documento

Selecione o Tipo de Documento para o Lançamento de Repasse.  
 Clique no ícone Novo Repasse para preencher outros dados do Lançamento de Repasse. Através deste ícone, pode-se gerar mais lançamentos de repasse. Para consultar o Repasse de um Lançamento ou para cancelar um repasse, selecione o Lançamento, Processos / Repasse / Exibir

**Observações:**

No momento da geração do repasse, o Tipo Contábil é apresentado por default como "Não Contábil", podendo ser alterado. . O lançamento gerado pelo repasse só pode ser baixado após a baixa do lançamento gerador do repasse.

Quando o Repasse é gerado por mais de um Lançamento e nem todos os lançamentos forem baixados de uma vez, o valor do(s) lançamento(s) a pagar que terá a baixa autorizada será alterado para um valor proporcional ao percentual do valor baixado e serão gerados um ou mais lançamentos com esta diferença.

Quando houver um cancelamento da baixa de um ou mais lançamentos a receber que geraram lançamentos de repasse, o valor do(s) lançamento(s) a pagar que teve a baixa autorizada será alterado e serão gerados um ou mais lançamentos com esta diferença.

É permitido vincular um adiantamento a um lançamento gerado pelo repasse. Assim, se o cliente decidir efetuar o pagamento do lançamento gerado pelo repasse antes do recebimento, ele poderá gerar um adiantamento baixado e vincular a esse lançamento. Quando o lançamento que gerou o repasse for baixado, o cliente poderá baixar também o lançamento do repasse, que já terá um adiantamento vinculado.

****[Gerar Repasse Automático](http://tdn.totvs.com/x/BC3vGQ)****

Funcionalidade utilizada pela integração com segmento Imobiliário. Para maiores detalhes verificar o Help deste segmento.

Contabilização Repasse Automático Financeiro

Na rotina de repasse automático do financeiro usando como base os contratos de vendas do TIN, ao contabilizar lançamento gerado via Repasse Automático, o sistema poderá buscar os defaults contábeis na sub unidade (TIN), como faz hoje para os próprios lançamentos do TIN.

**Observação.**

A contabilização através do default da sub unidade, se dará apenas para lançamentos com os tipos contábeis "Baixa Contábil" e "A Contabilizar".
