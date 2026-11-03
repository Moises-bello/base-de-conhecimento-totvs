---
content_hash: d1f5a6eb39436367b58f02ab932043833245654d15724c467d72256d3b6c2b63
fetched_at: '2026-06-29T00:09:29.083284+00:00'
page_id: '423938802'
product: rm
source: tdn-rm
title: Registros Bloco K260 e K265
type: documentation
url: https://tdn.totvs.com/display/LRM/Registros+Bloco+K260+e+K265
version: 2
---

O reprocessamento permite o apontamento do reprocesso industrial e assim foram incluídos novos registros no Bloco K, que foram divididas em dois registros:

* **K260 – Reprocessamento de Produto/Insumo**: Esse registro informa o produto que será reprocessado ou que foi reprocessado no período de apuração do registro K100 – Período de Apuração do ICMS/IPI, ou seja, informa os produtos que serão retirados do estoque para o devido reprocessamento;
* **K265 – Reprocessamento – Mercadorias Consumidas e/ou Retornadas**: Nesse registro é informado o consumo de mercadoria e/ou o retorno de mercadoria ao estoque, ocorrido no reprocessamento de produto/insumo informado no Registro K260 – Reprocessamento de Produto/Insumo – Produtos Acabados/Insumos, ou seja, esse registro trata da quantidade de insumos utilizados no reprocessamento, bem como do retorno de sobras, quando for o caso.

No TOTVS Gestão do Planejamento e Controle da Produção para a geração do processo de reprocessamento foi criado o campo 'Ordem é de Reprocessamento?'. Esse campo é apresentado na tela de identificação da Ordem de Produção e na criação da mesma ele vem desmarcado por default. Então para que a ordem de produção seja de Reprocessamento, o campo deve ser marcado.  
Se o usuário não for supervisor, o único status que não poderá marcar o campo é o Concluído. Porém com autorização de um usuário supervisor ele conseguirá.   
Já no caso do usuário supervisor pode marcar o campo independente do status da ordem de produção.   
O status Concluído é o status que será levado em consideração para enviar os dados para os registros do bloco K.   
O processo da ordem de produção não sofre nenhuma alteração e deve ser efetuado normalmente. Será gerado os registros K260 e K265 das Ordens de Produção com o status "concluída" e cuja data de conclusão esteja compreendida entre as datas inicial e final do período de apuração do SPED Fiscal (bloco K100).

Informações Adicionais

* [Bloco K - Controle da Produção e do Estoque (versão 2.0.22)](http://tdn.totvs.com/pages/releaseview.action?pageId=392502657)
* [Bloco K](http://tdn.totvs.com/display/LRM/SPED+Fiscal+-+Bloco+K)
* [Bloco K - Registro K260 e K265](http://tdn.totvs.com/display/LRM/TWBTG2+DT+Bloco+K+-+Registros+K260+e+K265)
