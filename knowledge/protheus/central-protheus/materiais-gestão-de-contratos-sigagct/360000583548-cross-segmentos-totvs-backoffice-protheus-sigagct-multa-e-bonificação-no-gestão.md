---
article_id: 360000583548
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: d640d1b3e0403bb448050fc6fbdaf1a35ba71e4d9d3856d0dbf229592233433d
fetched_at: '2026-06-28T22:37:20.073461+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Multa e Bonificação
  no Gestão de Contratos
type: support-article
updated_at: '2026-04-20T19:21:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000583548-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Multa-e-Bonifica%C3%A7%C3%A3o-no-Gest%C3%A3o-de-Contratos
---

**Dúvida**

Multa e Bonificação no Gestão de Contratos

**Ambiente**  
Microsiga Protheus – A partir da versão 11.80.  
  
**Solução**

No módulo de **Gestão de Contratos**, é possível incluir **Multa e Bonificação** ao Contrato? Quais os procedimentos para inclusão de valores de **multa e bonificação** ao **contrato**?

Multas na rotina de Contrato do módulo do Gestão de Contratos, são valores que podem ser acrescidos ou descontados no valor final das medições de contrato em virtude da quebra de alguma cláusula contratual ou em decorrência de algum fato ocorrido e previamente acordado entre as partes do contrato.

Assim, todas as multas de um contrato deverão ser cadastradas na rotina pertinente e posteriormente associadas ao contrato na aba Multas/Bonificações através da rotina de Contratos. Somente através deste vínculo as multas poderão ser aplicadas nas medições do contrato.

Multas/Bonificações permite associar/visualizar as multas e/ou bonificações que foram negociadas no contrato e que poderão ser aplicadas durante medição ou recebimento (conforme tipo de contrato). Vale lembrar que dependendo da configuração do campo **Mult. Manual no cadastro de Tipo de Contrato** somente as multas e/ou bonificações nesta pasta indicadas poderão ser aplicadas.

Em Contratos de Compras, as **Multas** são descontos e **Bonificações** são valores que podem ser acrescidos ou descontados no valor final das medições de contrato em virtude da quebra de alguma cláusula contratual ou em decorrência de algum fato ocorrido e previamente acordado entre as partes do contrato.

Em Contratos de Vendas, as **Multas** são valores que podem ser acrescidos, e **Bonificações** são descontos.

Para a aplicação de multas e bonificações, o ambiente de Gestão de Contratos disponibiliza o cadastro de Multas e Bonificações, onde as condições para aplicação da multa/bonificação bem como a definição do valor a ser acrescido/descontado serão definidos através de fórmulas.

Assim, todas as multas e bonificações de um contrato deverão ser cadastradas nesta rotina e posteriormente associadas ao contrato na aba Multas/Bonificações através da rotina de Contratos. Somente através deste vínculo as multas e bonificações poderão ser aplicadas nas medições do contrato.

Caso o contrato permita a aplicação de multas e bonificações na medição (conforme tipo de contrato) e caso seja necessário aplicar um valor de multa e/ou bonificação durante a inclusão de uma medição, deve-se utilizar a opção Multas na interface de inclusão.

Na interface de seleção de multas e bonificações serão exibidas todas as multas e bonificações previstas pelo contrato (cadastradas na aba Multas/Bonificações do contrato). Deverão ser selecionadas quais multas e bonificações serão aplicadas a medição em questão.

Na mesma interface existe ainda a possibilidade de inclusão manual de um valor de multa/bonificação, desde que o contrato permita a inclusão manual de multas e bonificações (conforme tipo de contrato). Para isto deve-se acionar o botão Adicionar e informar a descrição da multa/bonificação, o valor, o tipo (se multa ou bonificação) e se este valor irá interferir no pedido a ser gerado.

Ao confirmar a seleção, para cada multas e bonificações pré-cadastrados, o Sistema irá processar a fórmula de validação para verificar se a multa/bonificação deverá ser aplicada. Em caso de retorno positivo, será executada a fórmula para definição do valor da multa/bonificação.

Ao final, a somatória dos valores, incluindo multas e bonificações manuais, serão distribuídos no rodapé da medição nos campos Multas e Bonificações e serão acrescidos e somados no total da medição.

***Saiba Mais:***

[Multa e Bonificação ao Contrato](https://tdn.totvs.com/display/PROT/GCT0079_Multa_Bonificacao_Contrato_GCT)

[MP - SIGAGCT - Formas de geração da Multa ou Bonificação em pedidos de compra ou venda gerado por medição - Parâmetro MV\_MULTMED](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028877851)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
