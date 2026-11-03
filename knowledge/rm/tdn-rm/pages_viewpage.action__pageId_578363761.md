---
content_hash: d6a7df598a3ea6e9e1877c7d7dc2549b5e5a29dc51051b76a7efb6a5a6cbe584
fetched_at: '2026-06-29T00:10:53.299989+00:00'
page_id: '578363761'
product: rm
source: tdn-rm
title: Parâmetros - Gestão de Condomínio - Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=578363761
version: 6
---

## **Prioridade de cobrança do condomínio, quando integrado à locação**

---

Nestes parâmetros iremos definir a prioridade de cobrança das despesas relacionadas ao condomínio durante [fechamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=435104834).   
Há duas opções disponíveis, **Locatário** e **Locador**.

Na versão 12.1.31, foi implementada a opção **Ocupante,** que determina que a cobrança será realizada para o ocupante da subunidade.

Importante: Caso nenhum destes parâmetros estejam configurados o RM não fará a cobrança do condomínio. Será emitida uma mensagem de alerta ao realizar o cálculo do fechamento.

Os responsáveis financeiros serão exibidos logo após a realização do cálculo. Para verificar as cobranças e seus respectivos responsáveis, basta acessar o anexo de histórico de cálculos.

## **Data de emissão dos lançamentos financeiros do Fechamento:**

---

Este parâmetro indica qual é a data que será considerada no momento da geração dos **Lançamentos financeiros do Fechamento**

1. **Início da competência:** É o começo do período financeiro que estamos considerando, geralmente o primeiro dia do mês.
2. **Data de Vencimento:** É a data limite para pagar as contas do condomínio.
3. **Data da geração:** Será a data utilizada para geração dos lançamentos de condomínio (data de hoje).
4. **Último dia da competência:** É o último dia do período financeiro que estamos considerando, geralmente o último dia do mês.
5. **Mês anterior ao vencimento:** É o mês antes do prazo final para pagar as contas.

Importante

Estes parâmetros também serão aplicados para toda a geração de lançamentos de sócio no aluguel complementar, quando existir geração residual.

## **Data de emissão do fechamento de condomínio complementar:**

---

Este parâmetro indica qual é a data que será considerada para **fechamento do condomínio complementa**r e geração das parcelas no sistema.

1. **Início da competência:** É o começo do período financeiro que estamos considerando, geralmente o primeiro dia do mês.
2. **Data de Vencimento:** É a data limite para pagar as contas do condomínio.
3. **Data da geração:** Será a data utilizada para geração dos lançamentos de condomínio (data de hoje).
4. **Último dia da competência:** É o último dia do período financeiro que estamos considerando, geralmente o último dia do mês.
5. **Mês anterior ao vencimento:** É o mês antes do prazo final para pagar as contas.
