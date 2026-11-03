---
content_hash: 2a7630ecf3eea7e2c86f7937a7d8491c6657639f2ee286502e09d3d0b3b575a9
fetched_at: '2026-06-29T00:09:19.590041+00:00'
page_id: '422545619'
product: rm
source: tdn-rm
title: Parâmetros da ECF (Identificação)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545619
version: 6
---

Clicando no botão "Parâmetros Contábeis" o sistema abrirá a tela onde os dados serão pré definidos. A primeira informação necessária na parametrização, é se o Totvs Gestão Contábil está Integrado ao módulo TOTVS Gestão Fiscal. Quando esta opção estiver desmarcada o sistema entende que não existe integração com o Fiscal, ou não fazem utilização do Totvs Gestão Fiscal na empresa. Por esse motivo, o período a ser considerado para emissão da Escrituração Contábil Fiscal deverá ser informado manualmente, sendo esta informação de caráter obrigatório. Quando esta opção já estiver marcada, o sistema irá carregar automaticamente os itens 2 (Parametrização da ECF no módulo Totvs Gestão Fiscal) e Item 3 (Período). Essas informações são pertinentes a parametrização ECF, no TOTVS Gestão Fiscal.

O item referente a parametrização do Plano de Contas Paralelo é obrigatório. Deverá ser informado o cadastro do plano de contas onde as contas referenciais se encontram devidamente vinculadas as contábeis.  Ou seja, informar o plano de contas referencial da instituição gestora, referenciando com as respectivas contas do plano de contas da pessoa jurídica. Somente devem ser referenciadas as contas analíticas com natureza de conta igual a 01 (contas de ativo), 02 (contas de passivo), 03 (patrimônio líquido) e 04 (contas de resultado).

Os arquivos texto de Plano de Contas Referencial, disponibilizados pela Receita Federal estarão disponíveis no portal do cliente.  
 Dúvidas na importação de Plano de Contas Paralelo acesse o Help .

Caso no período, a informação de alguma conta contábil foi alterada e desejam que esse histórico de alteração seja enviado para escrituração, a opção "Enviar Histórico de alteração da Conta Contábil" deverá estar marcada. O mesmo ocorre para o centro de custo. Basta marcar o item "Enviar Histórico de alteração do Centro de Custo" que o sistema irá apresentar na ECF as alterações realizadas nesse cadastro.

O item que permite a geração do K355, baseando no saldo das contas de resultado, conforme a apuração realizada pelo processo de transferência de grupos contábeis, é "Utiliza transferência de grupos contábeis para identificar o(s) encerramento(s)". Marcando essa opção, o cálculo é realizado baseado no histórico de fechamento informado no processo de transferência de grupos contábeis. O sistema ainda permite informar o Histórico de Fechamento e a Data de Encerramento manualmente.  
 Com a opção desmarcada, o sistema irá calcular o saldo das contas de resultado com base no período informado, desta forma, irá desconsiderar os lançamentos que estão utilizando histórico de fechamento.  
***Observações*:** O sistema não permitirá que a parametrização contábil da ECF seja salva com a opção acima desmarcada quando, existirem na base de dados um ou mais lançamentos para o período informado, com histórico de fechamento que não esteja sendo utilizado em transferência de grupos contábeis. Isso se faz necessário para evitar conflito na apuração de saldo, visto que o Totvs Gestão Contábil permite o usuário utilizar histórico de fechamento em lançamentos que não são de encerramento.

São consideradas contas de resultado, as contas que estiverem em seu cadastro o campo "Natureza da conta p/ emissão do SPED" classificadas como "Conta de Resultado".  
A transferência de grupos contábeis selecionada deve ser aquela realizada para o ano base da ECF, ou seja, deve estar compreendida entre a data inicial e final apresentada o item 3 (período).
