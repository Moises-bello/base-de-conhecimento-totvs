---
article_id: 1500005269521
category: Financeiro - Contabilização
content_hash: f782ad55acf1e925ede12dcddb25b9b25f7c087e8f5afaf2c438c03869b0a35b
fetched_at: '2026-06-28T22:38:05.316912+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA102 - Help: ENTIDOBRIG'
type: support-article
updated_at: '2022-08-17T23:18:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005269521-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA102-Help-ENTIDOBRIG
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:05:00 min  
  
Ocorrência**No módulo Financeiro, ao tentar realizar contabilização é apresentada a Mensagem abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007309161/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CTBA102 - Todas as versões  
  
**Causa**Esse incidente ocorre mesmo preenchendo o campo relacionado a entidade contábil.  
  
**Solução**

Através da rotina **CTBA020** - verifique no cadastro da conta contábil utilizada no lançamento, se o campo da entidade esta configurado como obrigatório.![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046720233/mceclip0.png)

Através da rotina**CTBA030** verifique se está configurado como obrigatório as entidades. ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046727213/mceclip1.png)

Através da rotina **CTBA040** verifique se está configurado como obrigatório as entidades

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045867354/mceclip2.png)

Verifique se a entidade esta configurada para **controlar saldo** = 1 (Sim), caso não esteja mude para a opção = 1

Acessar módulo **34 contabilidade Gerencial** > **Atualizações** > **Configurações** > **Configurações** **Contábeis (CTBA130).​**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056661313/mceclip0.png)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055793114/mceclip1.png)**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056661353/mceclip2.png)

Necessário que o fontes relacionado ao módulo **Contabilidade Gerencial** estejam atualizados.

**Saiba mais**  
Pacotes atualização  - Contabilidade Gerencial  
[Pacotes de Atualização - Contabilidade Gerencial](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)
