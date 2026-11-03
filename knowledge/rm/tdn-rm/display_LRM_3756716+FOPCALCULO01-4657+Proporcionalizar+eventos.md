---
content_hash: dc8eb01860a4695208cc9ffe6e42b549288b8c6d40bea0d6a3c2c002ff7e43da
fetched_at: '2026-06-29T00:09:12.143777+00:00'
page_id: '415715171'
product: rm
source: tdn-rm
title: 3756716 FOPCALCULO01-4657 Proporcionalizar eventos
type: documentation
url: https://tdn.totvs.com/display/LRM/3756716+FOPCALCULO01-4657+Proporcionalizar+eventos
version: 2
---

# Proporcionalizar eventos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Envelope de Pagamento |
| **Situação/Requisito:** | No sistema há uma flag “Considera divisor pelo número de dias do mês na remuneração da admissão e demissão” em: “Configurações > Parametrizador > Folha Normal > Cálculo” que hoje tem efeito no evento de código de cálculo 2. Porém é solicitado que como a própria flag diz seja considerado para todos eventos que compõe a “remuneração” do funcionário o mês, não apenas o saldo de salário. |
| **Solução/Implementação:** | Considera o parâmetro "Considera divisor pelo número de dias do mês na remuneração da Admissão e Demissão" em todos os eventos proporcionalizados devido a admissão/demissão. |
| **Tickets relacionados:** | 3756716; 3815314 |
