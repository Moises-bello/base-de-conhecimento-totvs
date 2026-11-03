---
article_id: 360035868054
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 4e1fc320fb7db3000f5f367f701fbb00cf062d89b07e99544f17d13ad29c2e1e
fetched_at: '2026-06-28T22:40:48.969885+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: MP-SIGACTB - ECF Parâmetro Critério de reconhecimento de receitas para leiaute
  2
type: support-article
updated_at: '2021-04-28T22:11:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035868054-MP-SIGACTB-ECF-Par%C3%A2metro-Crit%C3%A9rio-de-reconhecimento-de-receitas-para-leiaute-2
---

**Dúvida**

Ao gerar o arquivo da ECF para o Leiaute 2.0 o sistema não habilita a pergunta "Critério de reconhecimento de receitas".

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047732273/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047732313/mceclip2.png)

**Ambiente**

Microsiga Protheus - Contabilidade – A partir da versão 11.80.  
  
  
**Solução**

Verifique no manual da receita  quanto ao parâmetro "**IND\_REC\_RECEITA** = Critério de reconhecimento de receitas para empresas tributadas pelo Lucro Presumido (Art. 215, § 9º, Instrução Normativa RFB nº 1.700/**2017**".  
  
Manual **Layout 5** :[Clique aqui.](http://sped.rfb.gov.br/estatico/84/62D84C440E97164D123ABE283B1308D53BC17A/Manual_de_Orienta%c3%a7%c3%a3o_da_ECF_Fevereiro_2019.pdf)

No layout 5, o parâmetro IND\_REC\_RECEITA é apresentado 3 vezes:  
  
1º Pag 64;  
  
![](https://totvssuporte.zendesk.com/attachments/token/vTT01sXRuFbd5I6f6dEkRIcqT/?name=inline-2100327089.png)​  
  
2º Pag 304;  
  
![](https://totvssuporte.zendesk.com/attachments/token/di2A8SOkFDpoBUZSMYtTuZRKi/?name=inline-326402513.png)​  
  
3º Pag 311;  
  
![](https://totvssuporte.zendesk.com/attachments/token/h88OBo2yJzimP6KnlyX3kMnXd/?name=inline-1892053882.png)​  
  
  
Manual **Layout 2** : [Clique aqui](http://sped.rfb.gov.br/estatico/E4/59375201A26CCD5E1D10CDD5E7D2E9C6587D3D/Manual_de_Orienta%c3%a7%c3%a3o_da_ECF_Junho_2016.pdf)  
  
Veja que no **layout 2** o parâmetro **IND\_REC\_RECEITA** não é apresentado nenhuma vez :  
  
![](https://totvssuporte.zendesk.com/attachments/token/gQzfZPcKD3JmpSpSB3GAh5rom/?name=inline225701849.png)

Diante disso verifique junto a receita se o parâmetro deve ser informado para o layout 2.

Saiba Mais :

[MP-SIGACTB - ECF - VALIDAÇÃO 14- IND\_REC\_RECEITA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008385052-MP-SIGACTB-ECF-VALIDA%C3%87%C3%83O-14-IND-REC-RECEITA?source=search)

[MP - SIGACTB - ECF - Bloco Q](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007125451-MP-SIGACTB-ECF-Bloco-Q?source=search)
