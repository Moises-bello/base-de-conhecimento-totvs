---
content_hash: 3ee879602a040339064a1b0a265e545c799708a421ca3aedd20fbd06d82c72cd
fetched_at: '2026-06-29T00:06:16.371661+00:00'
page_id: '212896901'
product: rm
source: tdn-rm
title: TTJVOU_DT_Ferias_Coletivas_Com_Dia_Fracionado
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJVOU_DT_Ferias_Coletivas_Com_Dia_Fracionado
version: 2
---

# FÉRIAS COLETIVAS INFORMANDO DIA FRACIONADO NA DATA FINAL DO PERIODO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Férias Coletivas* |
| **Situação/Requisito:** | *O cadastro das férias coletivas está considerando incorretamente o dia fracionado, quando está marcado o parâmetro "Proporcionais integrais para menos de 1 ano" no Sindicato, o saldo proporcional possui fração, 17.5 dias por exemplo, e o número de dias concedidos é menor que o saldo.*  *Nesta situação, independente de estar marcado ou não o parâmetro "Paga dias de direito fracionados" do Sindicato, a data final do período de férias está sendo cadastrada com meio dia.* |
| **Solução/Implementação:** | *Ajuste no módulo de cadastro de férias coletivas para informar a data final do período com dia fracionado, somente de for marcado o parâmetro "Paga dias de direito fracionados" do Sindicato.*  *O problema só ocorria quando estava marcado o parâmetro "Proporcionais integrais para menos de 1 ano" no Sindicato.* |
| **Chamados   relacionados:** | *TTJVOU* |
| **Versões/Release:** | *11.82.42* |
