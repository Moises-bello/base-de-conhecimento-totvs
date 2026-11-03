---
article_id: 1500001636782
category: Configurações
content_hash: 1b089f760245b654a01cc34126e881b569698fef87fa8c20da788b1fb57198b2
fetched_at: '2026-06-28T22:46:49.582450+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - Utiliza Histórico de compra de Vale Transporte
type: support-article
updated_at: '2022-05-17T14:50:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001636782-RH-RM-FOP-Utiliza-Hist%C3%B3rico-de-compra-de-Vale-Transporte
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:30 min****Dúvida**Como utilizo o parâmetro do Vale Transporte **Utiliza Histórico de compra de Vale Transporte**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
1. Para ativar o parâmetro, acesse **Configurações | Parametrizador | Folha Normal | Vale transporte | Utiliza Histórico de Compra de Vale Transporte**: ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001560921/mceclip0.png)  
  
Depois de atualizar a flag, é necessário sair e entrar no sistema novamente para a devida atualização do campo.  
  
2. Com este parâmetro marcado, é habilitado o menu **Gerar Compra de Vale Transporte** que fica em **Folha Mensal | Processos | Lançamentos**:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102570753/mceclip1.png)  
  
Informar os dados necessários e executar:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001507542/mceclip2.png)  
  
**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001507562/mceclip3.png)**3. Lançamento da Folha Mensal através do Grupo de Eventos com o parâmetro 'Lançar Vale Transporte' marcado:  
  
**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001507722/mceclip6.png)****![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001507662/mceclip4.png)**Através desse processo, é possível Gerar a Compra de Vale Transporte e o valor Calculado é armazenado no histórico de compra de vale transporte associado ao funcionário. Quando é feito o lançamento da Folha Mensal através do grupo de eventos com o parâmetro **Lançar Vale Transporte** marcado, será considerado o valor gerado nesse processo de compra de vale transporte para o lançamento dos eventos de Código de Cálculo 32 e 104, e não será considerado as informações do cadastro do funcionário.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102571253/mceclip5.png)  
  
**Importante**Caso o parâmetro esteja marcado, mas não foi executado o processo de compra de vale transporte, no lançamento do grupo de eventos com o parâmetro marcado **Lançar Vale Transporte**, será considerado os parâmetros informados no cadastro de funcionários. O cálculo de desconto de vale transporte, evento de código de cálculo 6, irá considerar o salário e/ou eventos lançados que incidem em vale transporte e, a partir do valor encontrado é lançado no envelope de pagamento do funcionário até o limite do valor de entrega de vale transporte.  
  
**Saiba mais**  
[Gerar Compra de Vale Transporte](https://tdn.totvs.com/display/public/LRM/Gerar+Compra+de+Vale+Transporte#:~:text=Para%20realizar%20a%20compra%20de,compra%20e%20executar%20o%20processo.)
