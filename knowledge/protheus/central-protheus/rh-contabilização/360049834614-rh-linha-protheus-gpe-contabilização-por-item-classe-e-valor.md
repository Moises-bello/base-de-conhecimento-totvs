---
article_id: 360049834614
category: RH - Contabilização
content_hash: edd2b283d69ea155bc3f412c79afa93996196eb99db6b92684e62532bbd3da0c
fetched_at: '2026-06-28T22:43:45.957247+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Contabilização por item classe e valor
type: support-article
updated_at: '2025-07-21T18:24:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049834614-RH-Linha-Protheus-GPE-Contabiliza%C3%A7%C3%A3o-por-item-classe-e-valor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17790976329751) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Contabilização por item classe e valor?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
**1.** Ativar o parâmetro **MV\_ITMCLVL**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076528553)

Mais informações:  
[MP - GPE - Criação do parâmetro MV\_ITMCLVL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020271991-MP-GPE-Cria%C3%A7%C3%A3o-do-par%C3%A2metro-MV-ITMCLVL-?source=search)  
  
**2.** No cadastro de novos funcionários, o campo ficará habilitado para inclusão da Classe valor e Item:   
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076534053)

**Importante:** Para os funcionários já cadastrados sem os campos Item e Classe Valor informados, será necessário efetuar transferência e incluir a informação nos campos Item / Classe Valor:![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076575933)

A transferência pode ser efetuado em lote:![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076576173)  
  
**3.** Nos lançamentos por funcionário, é possível efetuar um lançamento com um item, classe valor diferente do cadastro do funcionário  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076534273)

**4.**Após o cálculo da folha de pagamento, a contabilização seguirá as informações de acordo com os lançamentos em folha:   
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076534333)

**5.** A tabela SRZ também será montada com as colunas RZ\_ITEM e RZ\_CLVL  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075370414)

**6.** Configuração do lançamento padrão para validar o item , Classe Valor ou Ambos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17792798008983)

**7.** Contabilização   
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075369894)

**Importante:**  
O cálculo de folha deve ser realizado com o cadastro\transferência  do ITEM , CLASSE VALOR , de modo que já exista na folha conforme instrução 4 deste documento. Todo o processo de contabilização será espelho da movimentação que ocorrer em folha de pagamento. 

**Saber Mais:**

[RH - Linha Protheus - GPE - Contabilização da provisão de baixas de rescisão, baixa de férias e baixa de transferência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8809989489303-RH-Linha-Protheus-GPE-Contabiliza%C3%A7%C3%A3o-da-provis%C3%A3o-de-baixas-de-rescis%C3%A3o-baixa-de-f%C3%A9rias-e-baixa-de-transfer%C3%AAncia-?source=search)

[RH - Linha Protheus - GPE - Como realizar a contabilização online de títulos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019903992-RH-Linha-Protheus-GPE-Como-realizar-a-contabiliza%C3%A7%C3%A3o-online-de-t%C3%ADtulos?source=search)
