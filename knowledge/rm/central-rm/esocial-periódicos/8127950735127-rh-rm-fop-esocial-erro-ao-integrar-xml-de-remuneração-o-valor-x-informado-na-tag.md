---
article_id: 8127950735127
category: esocial - Periódicos
content_hash: 41c99530a5a8aa09d5ac31d391040d1045f4590f2eabf80adb7093d9800f6a7e
fetched_at: '2026-06-28T22:47:09.332258+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao integrar XML de remuneração: O valor ''X''
  informado na tag ideTabRubr não existe na base de dados'
type: support-article
updated_at: '2024-12-18T15:29:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8127950735127-RH-RM-FOP-eSocial-Erro-ao-integrar-XML-de-remunera%C3%A7%C3%A3o-O-valor-X-informado-na-tag-ideTabRubr-n%C3%A3o-existe-na-base-de-dados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**  Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Ao integrar com o TAF eventos de remuneração (S-1200 / S-1202 / S-1207 / S-2299 / S-2300) o sistema apresenta o erro **O valor 'X' informado na tag ideTabRubr não existe na base de dados**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8127778470935/mceclip0.png)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro ocorre quando a *tag* **ideTabRubr** informada no XML possui um valor diferente do identificador de rubricada cadastrado no TAF. Por padrão, o RM registra essa informação com o código da coligada corrente.  
  
**Solução**  
Para ajuste, siga a seguintes orientações:

1. No **TOTVS Automação Fiscal** (TAF), acesse o menu **Atualizações | Eventos e-Social | Tabelas | Identificadores de Rubricas**;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8127850116631/mceclip1.png)

2. Verifique se o valor informado no campo **Código do ERP** é o mesmo que o da *tag* **ideTabRubr** presente no  XML. Se o valor for diferente, o TAF irá rejeitar o evento;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075204014/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075204474/mceclip2.png)

4. Sendo necessário o ajuste no TAF, gere novamente o XML em seu ERP e integre com o TAF após correção.  
  
**Saiba mais**  
Para mais informações, acesse:  
     - [TAF - Integrações - O valor 'X' informado na tag ideTabRubr não existe na base de dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020487912)
