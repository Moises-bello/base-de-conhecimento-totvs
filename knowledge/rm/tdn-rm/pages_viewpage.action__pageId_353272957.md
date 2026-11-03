---
content_hash: d082bc53262fb4049975ffe66a85ed3b77bb85f7de829c89f8b3b1035406fea1
fetched_at: '2026-06-29T00:08:57.089524+00:00'
page_id: '353272957'
product: rm
source: tdn-rm
title: Reajuste permitir ignorar Deflação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353272957
version: 2
---

Atualmente o sistema sempre aplica o reajuste conforme variação do índice encontrada mesmo que seja negativa.

Para atender ao mercado deve ser criado o parâmetro por Coligada e Contrato de Locação para indicar se "Ignora Deflação", por default, na criação do campo sempre fica desmarcado mantendo assim o comportamento atual do sistema.

O Parâmetro da Coligada serve como default para a inclusão de novos contratos de locação mas permite que o usuário altere contrato a contrato.

Ao processar o reajuste o sistema deve verificar o parâmetro do contrato de locação e se estiver Null deve ser considerado o que estiver parametrizado na Coligada.

Originalmente a deflação era verificada por mês, com este parâmetro criou-se a possibilidade da deflação ser validada dentro do período configurado para a correção, ou seja, se este parâmetro estiver marcado e a periodicidade do reajuste for maior que mensal, por exemplo semestral, a variação será calculada para os seis meses, e se essa variação de seis meses for deflacionária (negativa), então ela será ignorada. Isso é para evitar que dentro dos seis meses, ocorra uma deflação em um mês e posteriormente, ainda dentro dos seis meses, ocorra inflação que supere a deflação anterior, anulando-a dentro do período.
