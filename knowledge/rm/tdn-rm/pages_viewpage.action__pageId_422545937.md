---
content_hash: 078315c6ac6189c223ba4dd7ec2783c067b3d8ac4ef2c70b7166f6d0fbfb851e
fetched_at: '2026-06-29T00:09:21.977770+00:00'
page_id: '422545937'
product: rm
source: tdn-rm
title: Bloco K - Saldos das Contas Contábeis e Referenciais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545937
version: 4
---

Este Bloco é composto pelos registros:

BLOCOKleftK155 K155 

**Detalhes dos Saldos Contábeis (Depois do Encerramento do Resultado do Período)**

O sistema deverá gerar os detalhes dos saldos contábeis Iniciais, finais, totais de Débito e totais de Crédito das contas patrimoniais (Ativo, Passivo e Patrimônio Líquido) depois do encerramento, levando em consideração o período informado no registro K030.

K355 K355 

**Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento**

O sistema deverá gerar os saldos finais das contas de resultado antes do encerramento. Para este cálculo o sistema irá aplicar a regra estabelecida no item "Utiliza transferência de grupos contábeis para identificar o(s) encerramento(s)" e "Transferência de Grupos Contábeis".  
Observações Registros K155 e K355:

1. Quando o sistema estiver parametrizado para considerar a conta gerencial como centro de custo a quebra será realizada pelas contas gerenciais, ou seja, o sistema irá processar as informações considerando os rateios.
2. Lançamentos que são classificados como fiscais para o envio do FCONT não serão levados em considerados no processamento deste registro.
3. Quando o sistema estiver parametrizado para não enviar o centro de custo para o SPED, o sistema vai processar o lançamento contábil que tenha o centro de custo, no entanto o campo centro de custo será enviado em branco.
