---
article_id: 12234628544151
category: Férias
content_hash: 4738cbb3bcb740e64f440ae30e5f66c42922e149adad874a5ff7bf7ed0f269c1
fetched_at: '2026-06-28T22:46:56.210662+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: RH - RM - FOP - Licença remunerada para funcionário com mais de um ano de empresa
type: support-article
updated_at: '2024-09-16T18:49:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12234628544151-RH-RM-FOP-Licen%C3%A7a-remunerada-para-funcion%C3%A1rio-com-mais-de-um-ano-de-empresa
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17548755009047)**Tempo aproximado para leitura:**00:03:01 min  
  
Dúvida**  
Como realizar lançamento de licença remunerada para funcionários com mais de 1 ano de empresa?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para conceder aos funcionários com mais de um ano de empresa, afastamento por licença remunerada, é necessário incluir fórmulas de valor e referência.  
Alterar a situação do funcionário para R; 

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12234506530967)**

Acessar o grupo de eventos e informar o evento de licença remunerada no item "eventos do grupo" e lançar a folha, consequentemente, vai lançar a licença remunerada.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12234532005783)   
  
Para que o sistema pague o valor equivalente a data do cadastramento da licença ( o evento é tipo dia e provento), deve-se **CADASTRAR UMA FÓRMULA DE REFERÊNCIA;**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12234545461783)**

Para que retorne somente os dias restantes do mês atual e na próxima competência os dias que faltam ( dentro do evento de licença remunerada ), para que tragam os valores a partir do início da licença remunerada.   
  
Após virar competência, voltar o funcionário para ativo e acessar: Férias | acerta período aquisitivo, com essa rotina, o mesmo terá o seu período aquisitivo alterado, caso essa licença ultrapasse 30 dias.  
  
**Observação Importante:**  
Para que não ocorra divergência de informações e/ou risco de realizar o processo indevido, recomendo realizar este procedimento primeiro em base de teste. Após certificar sua efetividade realizá-lo em ambiente de produção mediante a backup de segurança.  
  
**Saiba Mais**[Afastamento (Licença) - Remunerada x Não Remunerada](https://tdn.totvs.com/pages/viewpage.action?pageId=625937322)
