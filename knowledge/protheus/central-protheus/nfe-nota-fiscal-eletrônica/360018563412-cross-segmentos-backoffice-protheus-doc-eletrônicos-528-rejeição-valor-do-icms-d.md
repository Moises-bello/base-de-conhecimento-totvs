---
article_id: 360018563412
category: NFe - Nota Fiscal Eletrônica
content_hash: f89e68254ea6db8a2aeb99fdadfcc6647b159a44b6d4f51f9d73d124b53de303
fetched_at: '2026-06-28T22:40:05.093801+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 528 Rejeição :
  Valor do ICMS difere do produto BC e Alíquota'
type: support-article
updated_at: '2024-07-01T19:21:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018563412-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-528-Rejei%C3%A7%C3%A3o-Valor-do-ICMS-difere-do-produto-BC-e-Al%C3%ADquota
---

**Dúvida**Como solucionar a rejeição ?

528 Rejeição : Valor do ICMS difere do produto BC e Alíquota

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução:**

**Quando a nota não é de complemento a Sefaz espera que o valor do ICMS esteja conforme o calculo abaixo:**

<VBC> / 100 = Resultado

Resultado \* <PICMS> = <VICMS>

* **Saiba mais:**

O campo da TAG VBC  que verificamos para este cálculo é da tabela **CD2 o campo CD2\_BC / 100 (Nota de entrada ou saída)**

* **Caso seja nota de complemento:**

O correto para que ao transmitir para a Sefaz não gere a rejeição é a TAG deve ser FINNFE = 2  
  
Verifique se no XML está gerando FINNFE = 1, caso esteja  a nota não foi referenciada corretamente.  
  
![](https://totvssuporte.zendesk.com/attachments/token/xnmzUG73dPHZItCWluJPADer9/?name=inline-366753178.png)​

1. Verificar se a nota foi **referenciada ao documento**de origem corretamente:

D2\_ITEMORI, D2\_SERIORI, D2\_NFORI **(nota de saída)**

![referecia_nt_saida.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15438154833687)

D1\_ITEMORI, D1\_SERIORI, D1\_NFORI **(nota de entrada)**

**![referecia_nt_entrada.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15438143267351)**

**Importante:**

Lembrando que a nota só é **referenciada no XML** caso exista no sistema.

Se a mesma for referenciada manualmente deve se preencher os campos **NF . Ori , Serie Ori e Item Ori** .   
  
Se for preenchido automaticamente pelo gatilho **F4 (Nota de saída) ou F7 (Nota entrada)** os campos são alimentados automaticamente.

* **Saiba mais:**

**Conforme o link abaixo:**  
  
  
[MP - FIS - Complemento de ICMS/IPI na Devolução de Compra](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018778952)  
O sistema hoje tem um tratamento **paliativo para fazer esse tipo de operação,** no qual realmente o **código do cliente de do fornecedor** precisa ser exatamente o mesmo **para que não gere a rejeição 528/ 328.**  
  
Além disso,**a nota de origem precisa existir no sistema, a nota precisa ser referenciada corretamente  e o CFOP**da nota**não pode estar**no parâmetro **MV\_DEVCFOP.**

É importante lembrar que é necessário verificar**junto a Sefaz se realmente é essa operação que deve ser realizada**, ou se deve ser realizado o **cancelamento da nota.**  
  
  
**Para alterar a forma atendida pela legislação hoje:**  
  
1- Pode ser customizados o **NFESEFAZ .**

<https://suporte.totvs.com/portal/p/10098/download?e=1083729>  
  
**Rdmake disponível no link acima.**  
  
2- Segunda opção pode ser aberto melhoria na Central Colaborativa:  
  
[***Central Colaborativa TOTVS.***](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)  
**Para saber como criar uma sugestão de melhoria clique [*AQUI.*](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics)**  
  
  
3- Para que seja atendido no padrão é necessário que a empresa tenha alguma legislação na qual informe a obrigatoriedade de gerar conforme deseja.  
  
Havendo a legislação abra um ticket no suporte e nos encaminhe que será**compartilhado junto a consultoria tributária da TOTVS** e posteriormente ao produto.

**Obs:** **Caso o valor do ICMS esteja destacando o mesmo valor da base do ICMS, verifique se o campo F4\_TRFICM esta igual sim, altera para não e gere a nota do zero.**
