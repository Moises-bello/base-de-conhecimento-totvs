---
content_hash: a96867cdd61d3a8f35c18f5f811856ea44151da931640486779439141d5b8976
fetched_at: '2026-06-29T00:11:38.355734+00:00'
page_id: '784771846'
product: rm
source: tdn-rm
title: TCGI - Comissão - Equipe/Imobiliária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=784771846
version: 2
---

A partir do Release 12.1.2310, na Comissão, a criação da **Equipe/Imobiliária** permite que sejam pagas comissões com taxas diferentes entre a empresa e a imobiliária parceira, ou até mesmo com equipes diferentes.

Estas Equipes/Imobiliárias podem ser associadas às [Modalidades de Equipe da Comissão](https://tdn.totvs.com/display/LRM/Modalidade+de+Equipe), que por sua vez, podem ser associadas aos [Imóveis](https://tdn.totvs.com/pages/viewpage.action?pageId=773518068) que estão disponíveis para venda.

**Exemplo de configuração de Modalidade por Equipe/Imobiliária:**

Tenho uma empresa que deseja pagar comissão para os seus corretores próprios, gerentes e supervisores de uma maneira, para os seus parceiros de imobiliária de outra, e até com alguma diferenciação por estados da federação. Neste cenário pode-se realizar a configuração da seguinte maneira:

| Modalidade - Equipe Própria MG | Modalidade - Equipe Imobiliária MG | Modalidade - Equipe Própria SP | Modalidade - Equipe Imobiliária SP |
| --- | --- | --- | --- |
| 1. Corretor 2%; 2. Supervisor 0,5%; 3. Gerente 0,25% | 1. Imobiliária 2%; 2. Supervisor 0,5%; 3. Gerente 0,25% | 1. Corretor 2,5%; 2. Supervisor 0,6%; 3. Gerente 0,3% | 1. Imobiliária 3%; 2. Supervisor 0,6%; 3. Gerente 0,3% |

**O sistema utiliza a seguinte Ordem de Prioridade de busca de modalidade por Equipe/Imobiliária**

1. Modalidade, Empreendimento, Bloco/Quadra, Apto/Lote, Equipe/Imobiliária
2. Modalidade, Empreendimento, Bloco/Quadra, Apto/Lote,
3. Modalidade, Empreendimento, Bloco/Quadra, Equipe/Imobiliária
4. Modalidade, Empreendimento, Bloco/Quadra,
5. Modalidade, Empreendimento, Equipe/Imobiliária
6. Modalidade, Empreendimento
7. Modalidade, Equipe/Imobiliária
8. Modalidade

Foi criado um parâmetro Geral  em Contrato => comissão => comissão, para obrigar o preenchimento da equipe/imobiliária na geração da comissão
