---
article_id: 360004939872
category: RH - Cadastros
content_hash: 5c49dca6d34f530b943e1224b550bfb81eb6ccdde74d7864c04af8dffc29b42e
fetched_at: '2026-06-28T22:44:52.840419+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como efetuar o arredondamentos das horas de DSR
type: support-article
updated_at: '2026-01-23T16:00:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004939872-RH-Linha-Protheus-PON-Como-efetuar-o-arredondamentos-das-horas-de-DSR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31903579046295)** **Tempo aproximado para leitura:****00:01:00 min**  
  
**Dúvida**  
Como realizar a configuração do cadastro de arredondamento das horas para desconto do DSR?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
O cadastro de **Arredondamento** pode ser utilizado para tratar verbas como **DSR** e **FALTAS** (mais utilizados) que podem ser considerados como 8 horas diárias ou 7,33 (7,20) conforme CLT que exige o limite de horas de 220 mensais e 44 semanais.  
  
**1-** Na rotina de **Arredondamento**, em **Atualizações> Cadastro do Ponto> Arredondamento**, pode ser informado o **turno** caso haja algum em especifico para uma regra, ou deixar em branco como demonstra abaixo para ser considerado para todas regras/funcionários.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37886102076567)  
  
  
**2-** Informar o tipo de **arredondamento** que deseja realizar e como deseja arredondar este valor.  
Essa configuração se faz necessário para que a apuração do DSR seja semanal, pois irá considerar como base de cálculo das horas 7,20 horas e não 8 horas conforme a carga horária do funcionário.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37886102081047)  
  
  
**3-** Os campos abaixo precisa ser preenchido para definir a partir **De** quantos minutos/horas **Ate** quantas minutos/horas será considerado para gerar o evento de desconto de DSR:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37886102081815)  
  
  
  
**Saiba mais:**  
[RH - Linha Protheus - PON - Como utilizar o arredondamento do Cálculo das Horas de DSR e das Faltas Utilizando o parâmetro MV\_ARRINTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011378111-RH-Linha-Protheus-PON-Como-utilizar-o-arredondamento-do-C%C3%A1lculo-das-Horas-de-DSR-e-das-Faltas-Utilizando-o-par%C3%A2metro-MV-ARRINTE)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
