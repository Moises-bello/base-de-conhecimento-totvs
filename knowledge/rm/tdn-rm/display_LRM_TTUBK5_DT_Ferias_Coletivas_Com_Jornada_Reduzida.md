---
content_hash: 844da0dffced7d66cec258540250981fa4c826763b4396e0f2543639563b9d48
fetched_at: '2026-06-29T00:06:19.587396+00:00'
page_id: '219699790'
product: rm
source: tdn-rm
title: TTUBK5_DT_Ferias_Coletivas_Com_Jornada_Reduzida
type: documentation
url: https://tdn.totvs.com/display/LRM/TTUBK5_DT_Ferias_Coletivas_Com_Jornada_Reduzida
version: 1
---

# FÉRIAS COLETIVAS PARA FUNCIONÁRIOS COM JORNADA REDUZIDA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Férias Coletivas* |
| **Situação/Requisito:** | *No cadastro de férias coletivas para funcionário de mais de 50 anos com jornada reduzida, está sendo desconsiderado o valor informado no campo Dias de Direito (jornada reduzida) dos parâmetros do cadastro, e lançando 30 dias de férias para o funcionário.* |
| **Solução/Implementação:** | *Ajuste no cadastro de férias coletivas para funcionário com mais de 50 anos com jornada reduzida, quando não está marcado o parâmetro "Permite partir férias para funcionários com mais de 50 anos", do Sindicato.*  *Neste caso, se o número de dias concedidos de férias coletivas for menor que o saldo da jornada reduzida, será lançado o total de dias do saldo.*  *Se for concedido um número maior que o saldo da jornada reduzida, será considerado os dias concedidos.* |
| **Chamados   relacionados:** | *TTUBK5* |
| **Versões/Release:** | *12.1.9* |
