---
article_id: 360057643994
category: RH - Folha de Pagamento
content_hash: b5bb717eb0e1e5f861afc33bfb97dc7af6a51778b70d7507f7f5d7b58c33f35c
fetched_at: '2026-06-28T22:44:15.056424+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Média para afastados por acidente de trabalho e
  doença
type: support-article
updated_at: '2025-08-11T21:06:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057643994-RH-Linha-Protheus-GPE-M%C3%A9dia-para-afastados-por-acidente-de-trabalho-e-doen%C3%A7a
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26337525619735) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Quando funcionário mensalista esta afastado por acidente de trabalho e o campo RCM\_CATMED esta configurado para pagamento de média para mensalistas, a configuração não é respeitada.  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Criação do **mnemônico P\_PDMEDAFA** onde deverá ser informado as verbas que irão compor as médias para pagamento do funcionário afastado. As verbas deverão ser informadas sem separadores, uma seguida da outra:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100069833)

Caso o funcionário pertença a categoria definida no campo Cat.Calc.Med-(RCM\_CATMED) do Tipos de ausências, será calculada a média desses valores considerando a quantidade de meses informada no campo N. Mês C. Med-(RCM\_MESMED). Esse valor será somado a base de FGTS e também na verba utilizada para pagamento do auxilio.

**OBS. As médias serão pagas na mesma verba de ID 0041/ 0042, somadas ao valor dos dias referente ao afastamento.**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100069693)

**Importante:** A média a ser gerada será proporcional aos dias de afastamento pagos pela empresa, de acordo com a seguinte fórmula:  
Total dos valores das verbas definidas no mnemônico / N. Mês C. Med (RCM\_MESMED) / 30 \* Dias pagos de afastamento no período  
Para afastamentos que não possuam pagamento por parte da empresa, ou em meses posteriores a quitação da parte empresa, não haverá a geração dos valores.

**Saiba Mais**

[2941822 DRHPAG-18164 DT Média para afastados por acidente de trabalho](https://tdn.totvs.com/pages/viewpage.action?pageId=387292892)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
