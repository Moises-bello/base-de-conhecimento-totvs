---
article_id: 360047136353
category: RH - Contabilização
content_hash: 6e9b7dd66bea154cccfd2e8bad84d5fa634193be83fc0dae519e6d75a47ff7ab
fetched_at: '2026-06-28T22:43:46.146050+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Informações na tabela SRZ
type: support-article
updated_at: '2021-06-07T13:26:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047136353-RH-Linha-Protheus-GPE-Informa%C3%A7%C3%B5es-na-tabela-SRZ
---

**[Remover as instruções entre colchetes]**  
**Dúvida**Em que momento são gravadas informações na tabela SRZ e como são visualizadas?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**  
A **tabela SRZ** é uma tabela temporária. O preenchimento dessa tabela ocorre somente após o processo de contabilização ou na geração da GPS (relatórios / Periódicos / GPS-GRPS) de modo simultâneo.   
  
No momento da **contabilização**, a tabela é alimentada com as informações de resumo de folha de pagamento (tabela SRD ou SRC), provisão (SRT ou RHT) ou ambos da competência informada, de acordo com a configuração das perguntas da rotina de processamento (GPEM110). Ao **gerar o relatório GPS** , é alimentada com as informações de folha do período selecionado.   
**Importante: Após o cálculo da folha a tabela SRZ não recebe as verbas os resumo de folha.**

**1- Tabela SRZ  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067672433/mceclip4.png)  
​  
2 - Cálculos Férias e Rescisão:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066622894/mceclip1.png)**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066622974/mceclip2.png)  
​  
 ​3 - Tabela SRZ: Note que a tabela SRZ continua vazia.  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067672393/mceclip3.png)  
  
4 - Cálculo de Folha:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067682253/mceclip2.png)**

**​  
5 - Tabela SRZ: sem informações.  
​![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067672433/mceclip4.png)  
  
6 - Cálculo de Provisões: (férias /13º)  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066625054/mceclip6.png)  
​  
7 - No exemplo abaixo , imagem da Tabela SRT (provisões), que recebe as informações da  provisão após o cálculo.   
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066625154/mceclip7.png)  
​  
8 - A Tabela SRZ permanece  sem informações:  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067679613/mceclip8.png)**

**9 - Acessar Miscelânea -> Fechamentos -> Contabilização e efetuar o processamento da contabilização. No exemplo abaixo, utilizaremos a contabilização de Ambas (folha e provisão).  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067680073/mceclip9.png)**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066627454/mceclip0.png)  
  
 ​  
9 - Tabela SRZ montada com os resumos de folha e provisão:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067680233/mceclip1.png)  
​  
  
Importante: São apresentados os valores do resumo de folha e provisão sem a tratativa do lançamento padrão.**
