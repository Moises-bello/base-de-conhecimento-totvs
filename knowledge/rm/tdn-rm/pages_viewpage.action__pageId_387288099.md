---
content_hash: fea5cb52b27da3b6ff4a421b250e1119db12114f435432388215f2b411d76591
fetched_at: '2026-06-29T00:09:08.320794+00:00'
page_id: '387288099'
product: rm
source: tdn-rm
title: 3523126 FISCAL01-5970 DT - Estorno de Escrituração Migrada - Inconsistência
  na geração do estorno da escrituração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=387288099
version: 5
---

# Validação do período de apuração apresentando inconsistência para tributos com o mesmo tributo base

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Estorno de Escrituração |
| **Situação/Requisito:** | Ao realizar o processo de escrituração migrada ocorre a mensagem abaixo:  Inconsistência Processo de Estorno da Escrituração --------------------------------------------------------------------------------- Erro durante o estorno do Movimento: Data Movimento: 01/08/2018 Número: 444777 Série: U Tipo: 1.2.02 Filial: 1 Motivo: Já foi adicionado um item com a mesma chave. ------------------------------------------------------- |
| **Solução/Implementação:** | Alteração na validação de Período de Apuração no processo de estorno da Escrituração.    1ª Situação:  Possuir o mesmo tributo parametrizado no tipo de movimento, tanto para os tributos do movimento quanto para os tributos do item de movimento.  Neste caso é necessário alterar a parametrização do tipo de movimento e retirar essa duplicidade na parametrização dos tributos.  Ex: Cliente parametrizou o tributo INSSPJ tanto para o movimento quanto para o Item de Movimento. Este tributo, após a liberação da REINF, passou a ser um tributo a ser destacado no item do movimento e não no movimento. Caso o cliente possua este tributo parametrizado no seu tipo de movimento para os tributos do item e para os tributos do movimento, ocorrerá a mensagem de erro "Já foi adicionado um item com a mesma chave.". A solução será editar os parâmetros e retirar o tributo INSSPJ dos parâmetros dos tributos do movimento.    2ª situação:  Ajustado para que seja permitido vários tributos com o mesmo tributo base, desde que os tributos com o mesmo tributo base estejam parametrizados todos nos tributos por item ou nos tributos do movimento na parametrização do tipo de movimento senão ocorrerá o problema da 1ª situação. |
