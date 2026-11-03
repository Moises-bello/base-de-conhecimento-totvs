---
content_hash: 20d34bd2c63edda18c50465a919fc94cfee3a357f2042eb0a2d4db20921bb87b
fetched_at: '2026-06-29T00:09:20.126939+00:00'
page_id: '422545673'
product: rm
source: tdn-rm
title: Gerar Débitos de Entradas Diferidas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545673
version: 3
---

Este processo só estará visível para filiais que controlarem Unidades de Negócio e o respectivo parâmetro estiver habilitado. Aplicável somente ao Tributo ICMS.

* **Informações do Cálculo**

Totaliza-se o valor de (Quantidade \* Preço) - Desconto + Despesa + Frete + Seguro dos itens dos lançamentos de entrada da coligada, filial e período de geração do processo que possuam o status Normal.  
 Sobre o valor conseguido aplica-se a alíquota interna do produto no estado da filial corrente. Somente itens cujo produto possua uma alíquota interna informada nos seus dados fiscais para o estado e a filial corrente serão selecionados no cálculo.  
 Com o valor encontrado será criado um lançamento de Outros Débitos e subtipo Não se Aplica.
