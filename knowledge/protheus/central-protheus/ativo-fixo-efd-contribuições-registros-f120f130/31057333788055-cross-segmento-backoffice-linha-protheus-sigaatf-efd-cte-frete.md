---
article_id: 31057333788055
category: Ativo Fixo - EFD Contribuições - Registros F120/F130
content_hash: 2a15adc41909206f9aea66ad21599c4ed056dd577398b37bb9d597df21f0d6c1
fetched_at: '2026-06-28T22:41:36.182127+00:00'
product: protheus
section_id: 31045161075991
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - EFD - CTE (FRETE)
type: support-article
updated_at: '2025-03-31T18:36:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31057333788055-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-EFD-CTE-FRETE
---

Dúvida:

Quando há necessidade de agregar um frete para uma nota geradora de ativos, posso gerar a apuração EFD para nota CTE gerando um novo ativo?

Ambiente:

Microsiga Protheus - Ativo Fixo - Todas as versões

**Solução**

O ativo é alimentado pelos dados do documento de entrada. Por exemplo:

Ao inserir um documento de entrada de um bem com o valor de R$1.000,00 e uma **TES que atualiza o ativo fixo**, um novo ativo é gerado no módulo 01.

O mesmo ocorre para o CTE. O usuário pode registrar um documento de entrada do tipo "COMPLEMENTO", vinculando a nota geradora do ATF. Nesse caso, o sistema levará os valores para o módulo do ativo fixo, conforme o comportamento definido pelo parâmetro [MV\_AGVLATF](https://tdn.totvs.com/display/public/PROT/DT+Agrega+valor+de+conhecimento+de+frete+e+NF+de+garantia+estendida+em+bens+do+ativo+fixo):

* MV\_AGVLATF = .T. (padrão)

O sistema agrega o valor do bem ao valor do frete.

**Exemplo:** Se o bem original tem o valor de R$1.000,00 e o frete custa R$200,00, o valor total do ativo será atualizado para R$1.200,00.

* MV\_AGVLATF = .F.

O sistema mantém o comportamento legado, gerando um novo bem ao incluir uma CTE com TES que controla ativo. Neste processo, é essencial o uso de uma TES que atualiza o ativo, caso contrario o frete não gerará um novo ativo.  
 

A definição do método de entrada do CTE pode ser adequada de acordo com as regras de negócio da empresa. 

Ao utilizar o parâmetro **MV\_AGVLATF = .T. ,** o retorno da apuração no sistema será a apuração considerando a união consolidada dos valores do **frete** (CTE) e do **bem.**

Ao utilizar o parâmetro **MV\_AGVLATF = .F. ,** o retorno da apuração no sistema será a geração de um novo ativo, com o valor isolado do frete (CTE). Sendo necessário a classificação do bem para processamento da apuração. 

**É importante observar algumas particularidades relacionadas aos ativos gerados a partir do CTE:**

* Conferência das situações tributárias:  
  Certifique-se de que as situações tributárias associadas ao ativo estejam corretamente configuradas. Caso as situações sejam ***não geradoras de crédito***, a apuração pode não ser processada.

O campo determinante para que o sistema execute a apuração com base no cadastro do ativo é o Base PIS/COF (N1\_CBCPIS) =2.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31057318540951)  
 

* Classificação do ativo na aba "Impostos":  
  Verifique se as alíquotas estão sendo preenchidas corretamente.
