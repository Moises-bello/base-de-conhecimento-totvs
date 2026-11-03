---
article_id: 13511579283351
category: Folha Mensal
content_hash: 62ae21c4f03aeeb9a96429dcc933088101806dd10f7e63585ab56c9b50378227
fetched_at: '2026-06-28T22:46:58.245551+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Parâmetros Locais: Consulta da tabela GUSRPAR'
type: support-article
updated_at: '2026-02-11T20:51:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13511579283351-RH-RM-FOP-Par%C3%A2metros-Locais-Consulta-da-tabela-GUSRPAR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:26 min  
  
Dúvida**  
Como realizar consulta de qual parâmetro local o usuário está utilizando?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**A tabela que armazena as informações do parâmetro local é GUSRPAR, uma tabela que armazena algumas informações temporárias dos usuários.  
  
Dessa forma, para buscar os parâmetros locais, deverá usar a seguinte consulta:  
  
SELECT \* FROM GUSRPAR WHERE CODSISTEMA='P' AND CODUSUARIO='***XXX***'  
  
*Onde **XXX** deverá informar o usuário do sistema desejado.* **![](https://totvssuporte.zendesk.com/attachments/token/nKAyEI9HMQPX9RjIxTQB8p4Uh/?name=image.png)**Ao realizar a consulta, deverá copiar o campo PREFERENCIAS e colar em um arquivo word ou notpad,  
e então conseguirá visualizar os parâmetros locais daquele usuário em específico.  
  
Consulta:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13511447875607)  
Sistema:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13511574961431)  
  
**Saiba Mais**  
[RH - RM - FOP - Erro: Parâmetros locais ativado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004523231-RH-RM-FOP-Erro-Par%C3%A2metros-locais-ativado)
