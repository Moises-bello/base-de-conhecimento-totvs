---
article_id: 360017811471
category: NFe - Nota Fiscal Eletrônica
content_hash: e46db709c16956c02540417bffc79373cf06dd6e613f94ae4e7e13c8f6b1046c
fetched_at: '2026-06-28T22:40:05.309724+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 806 Rejeição: Operação
  com ICMS-ST sem informação do CEST'
type: support-article
updated_at: '2025-07-28T18:56:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017811471-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-806-Rejei%C3%A7%C3%A3o-Opera%C3%A7%C3%A3o-com-ICMS-ST-sem-informa%C3%A7%C3%A3o-do-CEST
---

**Dúvida**Como solucionar a rejeição abaixo:

806 Rejeição: Operação com ICMS-ST sem informação do CEST ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Ao utilizar as situações tributárias: **10, 30, 60, 70, 90, 201, 202, 203, 500 e 900** é obrigatório gerar o **CEST.**  
  
  
1- Se a situação tributária estiver correta preencher no cadastro de produto o **CEST "B1\_CEST" na aba outros:  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/TGDup0LEbSoXPhHYHl1pUHqXC/?name=inline478942701.png)​**  
2- Após isso, **exclua a nota e gere novamente.**3- Caso a situação tributária do ICMS esteja errada alterar no campo do TES campo no TES **F4\_SITTRIB** deve estar preenchido **Sit. trib. ICM diferente de 10, 30, 60, 70, 90**

![](https://totvssuporte.zendesk.com/attachments/token/v5tWGe5MHFcRlcP3zxkv0S1PH/?name=inline-1526359182.png)

4- Após isso, exclua a nota e gere novamente se for utilizar o mesmo pedido digite novamente o TES para alteração da **situação tributária do ICMS no pedido.**

* **Impressão no Danfe:**

O CEST é gerado **apenas no XML.**

Não existe até o momento um layout da Sefaz para que seja apresentada a informação do CEST, ou seja, não foi criado um novo campo no Danfe, e não há nenhuma informação na nota técnica sobre a obrigatoriedade de mensagem.

Caso seja uma solicitação da Sefaz do seu estado, poderá utilizar um padrão para gerar a mensagem em informações complementares, como exemplo **C5\_MENNOTA.**

* **Saiba mais:**

A rejeição é gerada apenas para as situações tributárias, **10, 30, 60, 70, 90, 201, 202, 203, 500 e 900.**

Porém, caso esteja preenchido no cadastro de produto será gerado **para as demais situações tributárias.**

Caso não possa retirar do cadastro de produto para **situações tributárias diferentes 10, 30, 60, 70, 90, 201, 202, 203, 500 e 900**

Para que o XML e o Danfe atenda sua necessidade há**três opções de processos** a ser seguido:  
  
1- Primeira opção pode ser customizado o **NFESEFAZ .**  
  
[MP - NFE - Documentos Eletrônicos NFe / NFSe / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493-MP-NFE-Documentos-Eletr%C3%B4nicos-NFe-NFSe-MDFe-MDe-?source=search)  
  
**Rdmake disponível no link acima.**  
  
2- Segunda opção pode ser aberto melhoria na Central Colaborativa:  
  
[***Central Colaborativa TOTVS.***](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)  
**Para saber como criar uma sugestão de melhoria clique [*AQUI.*](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics)**  
  
  
3- Terceira opção para que seja atendido no padrão é necessário que a empresa tenha alguma **legislação na qual informe a obrigatoriedade** de gerar conforme deseja.  
  
Havendo a legislação abra um ticket no suporte e nos encaminhe que será compartilhado junto a consultoria tributária da TOTVS e posteriormente ao produto.

* Caso seja necessário, acrescentar ***um novo código de NCM, realizar o procedimento abaixo:***

[https://tdn.totvs.com/pages/releaseview.action?pageId=260014602](Clique%20Aqui)
