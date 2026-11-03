---
article_id: 1500003494441
category: Contabilidade Gerencial - Amarrações
content_hash: 5e4f24e41403f2b1a03c49ba9f170f80836ab55b6a558d7c7dba29f2648bc269
fetched_at: '2026-06-28T22:41:05.753353+00:00'
product: protheus
section_id: 1500001548302
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA020/CTBA025 - Facilitador
  de amarração do Plano de contas com o Plano de contas Referencial (CVD)
type: support-article
updated_at: '2025-07-31T12:06:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003494441-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA020-CTBA025-Facilitador-de-amarra%C3%A7%C3%A3o-do-Plano-de-contas-com-o-Plano-de-contas-Referencial-CVD
---

**Dúvida**Facilitador (DE/PARA) de amarração do Plano de contas (CT1) e o Plano de contas Referencial (CVD).  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 12.  
  
**Solução**

Se a conta contábil não possuir relação com a tabela CVD o sistema não cria uma amarração automática entre estas tabelas.

Ao realizar a 'efetivação de revisão' o registro da tabela CVD somente será atualizado com um registro de amarração "automática"  se a conta contábil(CT1) possuir amarração prévia com a tabela CVD.

 Pré requisito para que o sistema realizar amarração automática :

* Deve ser realizado uma amarração manual para o primeiro plano de conta referencial importado para o sistema .
* Para os próximos plano referenciais o sistema irá considerar a amarração já existente para relacionar o novo plano referencial

Rotina de plano de contas referencial + Outras ações + Incluir Versões + copiar

![](https://totvssuporte.zendesk.com/attachments/token/OPqCECr9ZYRyNaXnj386KOJb2/?name=inline-41677789.png)

Irá ser criado uma nova versão do Plano referencial (legenda Rosa- Revisão), onde o cadastro poderá ser alterado ou incluir novas contas referenciais.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003644762)

Após o ajuste, deverá  "Efetivar Revisão" (outras ações + efetivar revisão)

Será demonstrados quais contas estão sem amarração (CVD):

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003651602)

Porém não impedirá que a nova versão do plano referencial seja criada:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003700201)

A vantagem desse processamento é que a amarração será feita automaticamente (CVD), porem é necessário já existir uma amarração para que o sistema tenha como base de relacionamento.

Outro questão é que a nova amarração gera apenas uma linha, caso tenha mais de um centro de custo devera ser feito o mapeamento manual.

Consultar o Plano de contas (CTBA020),

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003664162)

**Veja mais :**

[Relacionar plano referencial com o plano de contas](http://tdn.totvs.com/display/PROT/ER_PCREQ-4987_Plano_de_Contas_Referencial_Comparativo "Seguir el enlace")
