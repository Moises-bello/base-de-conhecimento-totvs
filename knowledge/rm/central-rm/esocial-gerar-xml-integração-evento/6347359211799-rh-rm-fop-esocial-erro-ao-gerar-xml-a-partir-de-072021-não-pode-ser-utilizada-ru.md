---
article_id: 6347359211799
category: eSocial - Gerar XML/ Integração Evento
content_hash: 47299c3ed15fa4116eae8cfcc3913d82684f5de681b1b3622239e75459c28a46
fetched_at: '2026-06-28T22:47:12.223565+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar XML: A partir de 07/2021 não pode
  ser utilizada rubrica cuja natRubr em S-1010 seja igual a [1801, 9220]'
type: support-article
updated_at: '2024-06-26T15:02:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6347359211799-RH-RM-FOP-eSocial-Erro-ao-gerar-XML-A-partir-de-07-2021-n%C3%A3o-pode-ser-utilizada-rubrica-cuja-natRubr-em-S-1010-seja-igual-a-1801-9220
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24446228051351) Tempo aproximado para leitura: **00:02:30 min****Ocorrência**Ao gerar o XML S-1200, S-1202, S-2299 ou S-2399 é apresentada a mensagem **Erro evento 'xxxx': A partir de 07/2021 não pode ser utilizada rubrica cuja natRubr em S-1010 seja igual a [1801, 9220].**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6346366711191)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões.  
  
**Causa**O erro ocorre quando a natureza de rubrica enviada através da *tag* **natRubr** do S-1010 está com **validade expirada** ou o**código está incorreto**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24446228059159)

Desde o dia 23/05/2022 passou a ser obrigatório o envio dos eventos no Leiaute Simplificado S-1.0. Neste Leiaute, algumas naturezas de rubricas constam como expiradas, conforme Anexo I do Leiaute S-1.0. Exemplo:

![](https://totvssuporte.zendesk.com/attachments/token/tW0P24UlblToM7PFhrlZsHyeh/?name=inline553504782.png)​​​​

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Deve-se acessar a **Tabela 03 - Natureza das Rubricas da Folha de Pagamento**, e consultar quais os códigos de natureza válidos.  Os que possuem  data de término de vigência na coluna **Término** estarão expirados. 

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6347173589783)

2. Em seguida, acesse **Folha de Pagamento | Administração de Pessoal | Eventos** e localize o evento correspondente e informe a Natureza da Rubrica eSocial desejada;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6374036718359)

3. Após, acesse o menu **eSocial | Fila de Eventos** e faça a edição do gatilho S-1010 gerado para o evento. Ajuste o campo **Competência** com o mês e ano igual ou anterior ao período de apuração que esteja enviando a folha/rescisão, para que a *tag* iniValid gere corretamente a informação de data:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6375205850647)

4. Gere o XML novamente e envie ao eSocial.  
  
**Importante**  
A TOTVS não orienta qual natureza de rubrica deve ser informadas nas verbas, ficando tal escolha a cargo da própria empresa.   
  
**Saiba Mais**Para saber mais consulte os links abaixo:

* [Documentação Técnica - eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)
* [Onde informar a natureza de rubrica eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403023133719)
