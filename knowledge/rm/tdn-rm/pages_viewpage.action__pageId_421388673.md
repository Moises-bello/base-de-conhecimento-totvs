---
content_hash: 8bcf2913bece81b93465d0fd4935204432515cd0093667216e27e411528e75b1
fetched_at: '2026-06-29T00:09:18.119758+00:00'
page_id: '421388673'
product: rm
source: tdn-rm
title: Devolução
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388673
version: 3
---

É uma operação que consiste em compensar um valor devolvido ao baixar outros Lançamentos Financeiros. O processo "Devolução" envolve Lançamento financeiro "comum" e o Lançamento de Devolução, cujo tipo de documento tem classificação específica. Ambos deverão ser vinculados para que seja realizada a compensação no momento da baixa.

**Pré-requisito**

Tipo de Documento classificado com "Devolução" . Utilizar eventos contábeis associado à Tabela Opcional ou a Tipo de Documento (para automatizar a Contabilização). . A Classificação do Cliente/Fornecedor (pasta identificação do cadastro do Clifor) deverá ser Ambos.

**Procedimento**

1. Incluir um Lançamento Financeiro "a Pagar" (exemplo: compra da mercadoria) com tipo de documento classificado com "Sem classificação". Este Lançamento será denominado "comum".
2. Incluir um Lançamento Financeiro "a receber" com tipo de documento classificado com "Devolução". Denominaremos Lançamento de devolução.

Para que o processo de baixa realize a compensação entre os Lançamentos, é necessário:

* Editar a tela de Vínculos que é exibida no momento da Baixa ou através do menu Processo/Vínculos.
* Selecionar o Lançamento referente à Devolução\* .
* Concluir o vínculo através do botão específico.
* Seta acima vincula, seta abaixo desvincula.

Ao baixar o Lançamento comum, será exibida uma tela para que seja estabelecido o vínculo e posterior compensação na Baixa do Lançamento. O vinculo poderá ser estabelecido também pela visão de Lançamento, Processos/Vínculos.

**Observação**

É permitido vincular vários Lançamentos de devolução pelo valor total ou parcial. Caso a opção seja vincular apenas parte da devolução (informando o valor a ser vinculado no campo "Vinculo Selecionado"), no Lançamento de devolução ficará armazenado o "Valor Disponível", que poderá ser utilizado em outra operação.

Não será permitido a geração de Borderô de pagamento para lançamentos com valor líquido igual a 0 (zero), com data de referencia a sua data de vencimento.  
 Após o vínculo, no processo de baixa será feita a compensação entre o valor a ser baixado e o valor devolvido.

Exemplo:

Valor do Lançamento comum: ............ R$10.000,00

Valor da Devolução: .......................... R$ 4.000,00

Valor baixado: .................................. R$ 6.000,00

**Efeitos**

O Lançamento ficará com status de Baixado. . Será gerado o respectivo item de Baixa (Anexos/Baixas do Lançamento). . O Lançamento de devolução será baixado automaticamente. . O registro de extrato será equivalente ao valor baixado. . Será gravado no lote contábil específico, a contabilização conforme os Eventos Contábeis utilizados no processo.

**Observação**

Ao cancelar a baixa do Lançamento comum será cancelada a baixa do(s) lançamento(s) de devolução  automaticamente, porém será mantido o vinculo, que poderá ser desfeito na próxima baixa ou através do menu: Processo/Vínculos.

**Outra possibilidade**

Vinculo entre Lançamento de Devolução com valor igual ao valor do Lançamento comum .

* O valor baixado será zero.
* Não gerará registro no extrato de Caixa.
