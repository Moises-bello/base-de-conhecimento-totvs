---
content_hash: 6802667847bfe08f36e294712c4ef12244fc6077fec75e14348895a2bec39e48
fetched_at: '2026-06-29T00:09:21.746533+00:00'
page_id: '422545893'
product: rm
source: tdn-rm
title: Apuração INSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545893
version: 4
---

O processo deve ser utilizado para cálculo do INSS que incide sobre serviços contratados em cessão de mão- de- obra ou empreitada.  
 O valor destacado como retenção na nota fiscal, fatura ou recibo será compensado pelo estabelecimento da contratada, quando do recolhimento das contribuições incidentes sobre a folha de pagamento dos segurados empregados e contribuintes individuais.  
 O sistema calculará o imposto devido no período, serão considerados todos os lançamentos de entrada que não estão cancelados ou estornados, neles devem conter o tributo INSS  na pasta "Outros Tributos" informado no item no Lançamento Fiscal.  
 As guias são geradas com base nos lançamentos de Outros Impostos vinculados ao tributo INSS referentes aos lançamentos fiscais de entrada.   
 Estas guias poderão ser alteradas somente se não estiver integrada ao TOTVS Gestão Financeira, caso contrário poderá ser editada somente para consulta.  
 Ao gerar as Guias GPS automaticamente o sistema irá verificar o parâmetro "Gerar GPS Centralizada" caso esta habilitado, o sistema irá verificar todos os lançamentos de todas as Filiais e irá gerar as Guias GPS para todas as Filiais centralizadas na Matriz.  
 Se esse parâmetro não estiver habilitado o sistema irá verificar os lançamentos da Filial Corrente e gerar a Guia GPS.

***Atenção!***Ao gerar a guia com base nos Lançamentos Fiscais (TOTVS Gestão Fiscal), o sistema estará marcando os tributos utilizados com o identificador da guia gerada. Assim, o usuário poderá gerar as guias automaticamente diversas vezes. Somente os tributos ainda não utilizados na geração de guias serão considerados.  
 O sistema preencherá automaticamente o campo Saldo Credor/Devedor, Pasta Outros Dados, do período associado ao tributo, com o total das guias geradas automaticamente (campo Valor Principal) multiplicado por (-1), ou seja, o total das guias é o saldo devedor do período.

***Observação:***Se a coligada tem licença para o TOTVS Gestão Financeira os campos Valor Multa, Valor Juros e Valor Desconto de todos os tipos de guias ficarão desabilitados, visto que estes campos serão atualizados pelo TOTVS Gestão Financeira, no momento da baixa do Lançamento Financeiro correspondente. Se a coligada não tem licença para o TOTVS Gestão Financeira, os campos ficarão habilitados, podendo ser alterados.   
 Após a baixa do de vencimento de fatura relacionado, os valores dos campos multa, juros e desconto da guia serão atualizados.
