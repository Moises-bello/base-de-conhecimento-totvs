---
article_id: 31053188510231
category: Ativo Fixo - EFD Contribuições - Registros F120/F130
content_hash: 82a2c457fb8f34504e44cd83be1a24cb503cedd95dc16a37bea13cf7f8b3fbd6
fetched_at: '2026-06-28T22:41:36.202127+00:00'
product: protheus
section_id: 31045161075991
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - EFD - Preenchimento
  valor de exclusão
type: support-article
updated_at: '2025-05-09T18:30:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31053188510231-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-EFD-Preenchimento-valor-de-exclus%C3%A3o
---

**Dúvida:** Ao realizar a apuração utilizando a rotina FISA001, o sistema está preenchendo o campo de valor de exclusão

**Ambiente:**

Microsiga Protheus - Ativo Fixo - Todas as versões

**Solução:**

Com a atualização na **legislação 14.592/2023**, até 30 de Abril de 2023, o contribuinte poderia optar por não excluir o ICMS para o ativo imobilizado. No entanto, a partir de 1º de maio de 2023, todos os bens adquiridos deverão gerar o valor de exclusão em suas apurações, conforme exigido pela nova legislação.

O campo que determinará a geração e cálculo do valor, está contido na **TES** de entrada (F4\_CREDICM) 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31053188495511)

O campo responsável pela geração e cálculo do valor de exclusão está presente na **TES de entrada**.

Ao utilizar o campo **CRED ICM = NÃO**, o sistema processará automaticamente os valores de exclusão na apuração do **EFD**, seguindo a seguinte fórmula:

**CL2\_VLEXCL = D1\_VALICM / D1\_QUANT \* N4\_TXDEPR**

O valor gerado será obrigatoriamente baseado nos dados do documento de entrada, conforme previsto na legislação. Dessa forma, para ativos que **não possuem integração com a nota fiscal de entrada**, os valores **não poderão ser gerados**.

Caso seja necessário impedir o cálculo do valor de exclusão, o campo **CRED ICM (F4\_CREDICM)** deve estar configurado como **SIM**. No entanto, é importante ressaltar que essa adequação pode impactar ativos que utilizam a mesma TES, além de afetar outros módulos, como Fiscal, Estoque e Compras. O comportamento desse campo deve seguir as regras de negócio de cada cliente.

A **TOTVS** **não recomenda** a modificação desse campo para itens que já estão em uso. A orientação ideal é a criação e utilização de **uma nova TES de entrada** para garantir o correto tratamento fiscal e evitar impactos em processos já estabelecidos.
