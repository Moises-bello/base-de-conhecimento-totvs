---
content_hash: 939a008fdda8be70739b5f1b8e8424ea134c9d647fcbfe91095b357537c83b7e
fetched_at: '2026-06-29T00:06:16.388960+00:00'
page_id: '212897144'
product: rm
source: tdn-rm
title: TTPGX2_DT_Ferias_Coletivas_Com_Dia_Fracionado
type: documentation
url: https://tdn.totvs.com/display/LRM/TTPGX2_DT_Ferias_Coletivas_Com_Dia_Fracionado
version: 1
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
| **Chamados   relacionados:** | *TTPGX2* |
| **Versões/Release:** | *12.1.9* |
