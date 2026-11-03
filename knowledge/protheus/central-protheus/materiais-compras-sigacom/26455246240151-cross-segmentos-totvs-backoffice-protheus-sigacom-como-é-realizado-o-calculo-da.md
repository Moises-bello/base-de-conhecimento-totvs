---
article_id: 26455246240151
category: Materiais - Compras (SIGACOM)
content_hash: 156f6dfe5e047a95c8c62d7910c4797b6adcff0481483b6f90821e7e5aadeee7
fetched_at: '2026-06-28T22:41:15.815314+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é realizado o
  Calculo da Sugestão de Compras?
type: support-article
updated_at: '2024-09-18T13:59:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26455246240151-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-realizado-o-Calculo-da-Sugest%C3%A3o-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26455246227991) Tempo aproximado para leitura: **00:01:SS min** **Dúvida**

Como é realizado o Calculo da Sugestão de Compras?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12  
  
**Solução**

O conceito da rotina Sugestão de Compra é gerar sugestões com base no cálculo da demanda e nas movimentações dos produtos ao longo de dois meses. Para que a demanda seja calculada corretamente, é necessário que o produto tenha movimentações em pelo menos dois meses, permitindo assim a obtenção da média de consumo.

Além disso, utilizando o exemplo de geração de demanda para três meses, a rotina de Gerar Demanda deve ser executada mês a mês. Após a geração da demanda para os três meses, a sugestão de compra deve ser realizada.

**Exemplo ao Gerar a Sugestão de Compras :**

Dias para sugestão = 120 ( Normalmente se aplica 30 dias, ou seja, é a quantidade a ser provisionada para um mês. No caso, foi colocado 120 dias. Significa que vai fazer 120:30=4. Esse valor (4) vezes (x) o valor da demanda? será o valor gerado na Sugestão de Compra. Se o valor da demanda for 20 em um mês, a quantidade da SC será 20x4=80 peças na SC.

Tendência = aConsumo[nAtual-1]+( aConsumo[nAtual-1]-aConsumo[nAtual-2] ) –> Esta fórmula é baseada em estudos econômicos – ver no manual as outras fórmulas para Sazonalidade e etc.

Tendência = 15 + 15 - 10

Tendência = 20

aConsumo= Array de 120 posições – significa que podemos fazer para até 120 meses

Class custo ? = Todos

Tipo preço = Preço de Venda

ABC venda custo = CA (Aqui pode-se colocar \*(Asterisco) para considerar todas as classificações)

• Importado = N

• Grupo de = <branco>

• Grupo até = 9999

• Produto de = <branco>

• Produto até = 999999

Confirmar a execução da rotina.

O Sistema gera um registro para o produto.

Saiba mais em :

[Processo de Sugestão de Compras](https://tdn.totvs.com/pages/releaseview.action?pageId=229147298)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
