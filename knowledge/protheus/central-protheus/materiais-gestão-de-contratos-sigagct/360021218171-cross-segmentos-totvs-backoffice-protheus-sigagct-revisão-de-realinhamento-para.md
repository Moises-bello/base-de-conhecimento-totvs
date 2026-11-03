---
article_id: 360021218171
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 68125f4bbcca97f9d1bdc060137627793cd6e840d1d720d35e6b606281fc4d69
fetched_at: '2026-06-28T22:37:24.120567+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Revisão de Realinhamento
  para alterar os Valores Unitários dos itens do Contrato
type: support-article
updated_at: '2025-12-26T20:10:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021218171-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Revis%C3%A3o-de-Realinhamento-para-alterar-os-Valores-Unit%C3%A1rios-dos-itens-do-Contrato
---

**Dúvida**  
Como realizar Manualmente o Realinhamento/Alteração dos Valores Unitários dos itens de um Contrato ?  
  
**Ambiente**  
Protheus - Gestão de Contratos - Release 12.1.17

**Solução**

Nesse Tipo de Revisão permite alterar o valor dos itens do contrato de acordo com um novo valor unitário negociado com o fornecedor ou cliente. O valor é informado manualmente pelo usuário em Revisão.

Os itens que possuem medição realizada são mantidos como histórico, porém, o sistema gera uma cópia contendo o saldo não medido de cada item com o valor reajustado.

O sistema calcula o novo valor do contrato na execução da revisão. Caso existam cronogramas, eles devem ser reajustados manualmente, por meio da rotina Cronogramas, antes da aprovação da revisão.

Para solucionar essa dúvida, realize os seguintes passos:

1. Cadastre um tipo de Revisão conforme abaixo:

```
Tipo 3 = Realinhamento
Modo = Ambos 
Espécie = Preço
```

2. Ajuste o valor unitário de um item da planilha para + ou- do valor original:

```
Neste momento o Sistema dividirá o item da planilha caso haja medições efetuadas.
Obs: A nova linha contempla o valor Reajustado.
```

Neste caso do item que ja possui alguma medição, o item com o valor original fica com a "Quantidade" com o que já foi medido neste valor unitário original.

E o novo Item criado/dividido é gerado com o novo valor unitário reajustado e com a quantidade com o "saldo não medido" que estava no item anterior do valor original.

3. No Cronograma Financeiro, ajuste o Valor Previsto das parcelas não medidas com o novo valor (de modo que o Montante de Cronograma fique igual ao novo Valor Total de Contrato), confirme a tela e aprove a revisão.

**Obs:**

Para zerar o saldo de contrato **planilha de serviço** ,  com medição parcial encerrada, segue orientações abaixo:

**Planilha de Serviços**

Como a quantidade do item da planilha de serviço está atrelada a quantidade de parcelas, e na medição, a quantidade sempre será 01, se necessitar zerar o saldo da planilha de apenas 01 parcela no cronograma financeiro e com uma medição parcial encerrada, **este processo poderá ser feito somente com a revisão de Realinhamento.**

Para isto há 02 opções:

A) Alterar o valor do item para 0. O sistema criará um novo item com valor e quantidade zerada e atualizará o saldo da planilha com o valor medido;

B) No tipo do contrato ou tipo de planilha, alterar o campo Realinha Medição = SIM. Alterar o valor unitário do item com o valor medido e, consequentemente, alterar o valor da parcela no cronograma financeiro.

***Saiba Mais:***

[MP - SIGAGCT - Quais são os tipos de Revisão disponíveis, para revisar contratos no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034587334-MP-SIGAGCT-Tipos-de-Revis%C3%A3o)

[Tipos de Revisões de Contrato - CNTA010](https://tdn.totvs.com/pages/releaseview.action?pageId=224447795)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
