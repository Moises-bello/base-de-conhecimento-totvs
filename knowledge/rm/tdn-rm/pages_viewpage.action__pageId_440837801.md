---
content_hash: 352c60b62da9f2be920a4b0fe1be17f891ccd5a8db724d39d1fe8ba54220a092
fetched_at: '2026-06-29T00:09:53.146116+00:00'
page_id: '440837801'
product: rm
source: tdn-rm
title: 4486341 FOPCALCULO01-5450 Férias Coletivas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=440837801
version: 1
---

# Férias Coletivas

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Plataforma RH |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Férias Coletivas |
| **Situação/Requisito:** | Quando lançamos férias coletivas para funcionários que estão em situação 'F', o sistema está incluindo o gozo dentro de um período aquisitivo já contemplado com os 30 dias, independente se o parâmetro 'Permite antecipação de dias de férias do próximo período aquisitivo' do está marcado ou não. Com parâmetro marcado, liberando as férias é criado novo período aquisitivo, porém, os dados da aba antecipação de férias não são preenchidos e os dias de férias já contemplados não são abatidos no novo período aquisitivo. |
| **Solução/Implementação:** | Correção na validação de saldo de férias para calcular férias coletivas aos funcionários na situação em que a flag "'Permite antecipação de dias de férias do próximo período aquisitivo" do sindicato esteja marcada. |
| **Tickets relacionados:** | 4486341 |
