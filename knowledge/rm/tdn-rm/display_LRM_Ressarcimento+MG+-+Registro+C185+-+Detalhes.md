---
content_hash: 140091ee54dd468cd1019c7912a52caea12b37638dfe7e115040c2ea1ce95dac
fetched_at: '2026-06-29T00:11:35.904886+00:00'
page_id: '768412942'
product: rm
source: tdn-rm
title: Ressarcimento MG - Registro C185 - Detalhes
type: documentation
url: https://tdn.totvs.com/display/LRM/Ressarcimento+MG+-+Registro+C185+-+Detalhes
version: 15
---

#f5f5f5#363636noneC185 - Exemplos campo 12Atenção: Fórmula utilizada

O sistema utiliza a seguinte fórmula para calcular o valor médio unitário nos **campos 12, 13 e 14 do registro C185.**  
((Quantidade da primeira compra **x** Valor do ICMS da primeira compra) **+** (Quantidade da segunda compra **x** Valor do ICMS da segunda compra)) **÷** (Quantidade da primeira compra **+** Quantidade da segunda compra)

**01. Exemplos**

* **Cenário 1:**  
    
  Entrada de produto, código 07.99, em mês anterior a geração da rotina, quantidade 7, aplicando a fórmula:  
  ((7 x 100) + (0 x 0)) **÷** (7 + 0) = 100 conforme imagem abaixo:

imagem

* **Cenário 2:**  
    
  Entrada de produto, código 07.99, em mês anterior a geração da rotina, quantidade 7 e 3 quantidades com lançamento de entrada no mês de geração da rotina, aplicando a fórmula:   
  ((7 x 100) + (3 x 500)) **÷** (7 + 3) = 220, conforme imagem abaixo:

imagem
