---
article_id: 20892682356119
category: Banco de Horas
content_hash: 59cb71b21fcc9daefe9692c41a2c7f2e8682d12edfde94d55df5d6214b37d65c
fetched_at: '2026-06-28T22:46:27.731926+00:00'
product: rm
section_id: 1500000835081
source: central-rm
title: RH - RM - PTO - Como lançar saldo parcial do banco de horas diário
type: support-article
updated_at: '2024-12-05T16:42:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20892682356119-RH-RM-PTO-Como-lan%C3%A7ar-saldo-parcial-do-banco-de-horas-di%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20892682328855) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como realizar o processo de lançar o valor parcial do saldo de banco de horas diário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80  
  
**Solução**

Para fazer o lançamento parcial do banco de horas diário, você pode seguir os passos dos vídeos abaixo:

* Parte 1: Este vídeo irá te mostrar como conferir o saldo antes de realizar o processo:
* Parte 2: Aqui você encontrará um tutorial com a parametrização a ser utilizada:     

  Importante: Gostaríamos de ressaltar a importância de não selecionar o parâmetro '**Considere as horas originais que foram compensadas/pagas no banco de horas**' durante o processo. Ao marcá-lo, o sistema irá considerar todo o saldo do banco de horas, incluindo as horas que já foram compensadas ou lançadas em outros períodos. Em caso de necessidade de recálculo do ponto para desfazer a compensação ou lançamento no banco de horas, todo o saldo acumulado desde o início da utilização do banco será desfeito, não apenas o intervalo de datas especificado na rotina.

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21455408135575)
* Parte 3: Esse vídeo vai te mostrar o restante da parametrização e também como ficou o saldo após realizar o processo.   
    
    
  **Saiba Mais**   
  Para maiores informações sobre o processo de Compensação\Lançamento do Banco de horas, acesse a documentação: [Compensação\Lançamento do Banco de Horas - Parâmetros](https://tdn.totvs.com/pages/releaseview.action?pageId=452719612).
