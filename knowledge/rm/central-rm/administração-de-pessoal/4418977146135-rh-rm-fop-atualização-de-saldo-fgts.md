---
article_id: 4418977146135
category: Administração de Pessoal
content_hash: a69f1cb0b17eea1636d1f522b4e5417547e23978a49ec82debe5f9a5392b7df7
fetched_at: '2026-06-28T22:47:01.385957+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Atualização de Saldo FGTS
type: support-article
updated_at: '2025-01-07T18:15:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418977146135-RH-RM-FOP-Atualiza%C3%A7%C3%A3o-de-Saldo-FGTS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22849400617367)**Tempo aproximado para leitura**: 00:02:00 min**

**Dúvida**  
Como Atualizar Saldo do FGTS?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para Atualizar o Saldo FGTS siga esses passos.

**1**. Deve-se acessar o caminho **Administração Pessoal | Cadastros Globais | Moedas e índices** e criar uma moeda com as especificações abaixo.

![](https://totvssuporte.zendesk.com/attachments/token/bvqghPSup6xO2Q0ytrqUY09Zw/?name=image.png)

**2**. Feita a criação da moeda, deve-se acessar o caminho **Administração de Pessoal | Cadastros Globais | Cotações**. Lá serão informados, mensalmente, os fatores de atualização do saldo de FGTS.   
A cotação deverá ser criada observando-se as especificações abaixo:

![](https://totvssuporte.zendesk.com/attachments/token/AClFMr4uWeJDL2yGwTezAxqm1/?name=image.png)

A data do índice deve ser sempre o primeiro dia da competência anterior a competência atual. Para entender melhor, segue abaixo uma breve explanação de como o sistema efetua o cálculo de atualização.

**LOG DE EXECUÇÃO DO PROCESSO DE ATUALIZAÇÃO DE FGTS**  
**### ## ######## ## ######## ## ########### ## ####**  
**»» Funcionário 23252: Meire Luci**  
**»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»**  
**Mês referência: 1/2023 Valor Depósito Incluído: 240,00**  
**»»»» Saldo Competência 0,00 Valor para correção:0,00 \* 0,0000 = 0,00 Total depositado no mês: 240,00**   
**»»»» Saldo Corrigido na competência 1/2023: 0,00**

**»»»»»» FGTS Recalculado para funcionário de chapa: 23252**  
**Data: 01/01/2023 Saldo FGTS na ECF: 240,00 Saldo para fins rescisórios: 240,00**

A cotação será cadastrada mês a mês **um registro por competência** de acordo com a liberação do mesmo no site da Caixa Econômica Federal.

**3**. Feito o cadastramento da Moeda e a respectiva Cotação, deve-se entrar em contato com a Caixa Econômica Federal para conseguir o ultimo extrato com o respectivo saldo de FGTS do funcionário com a data do dia 10 da competência anterior.

Esses dados serão utilizados para alimentar o cadastro do funcionário, na pasta **Rotinas mensais/Anuais**, subpasta **FGTS/SEFIP.** Na competência de implantação dessa rotina, esses dados deverão ser digitados e, após o término dos cadastros, a rotina fará essa atualização.

![](https://totvssuporte.zendesk.com/attachments/token/7dsas2eJDS11fno1qOhgNIou6/?name=image.png)

**4**. Com a base parametrizada, a rotina poderá ser processada em **Administração de Pessoal | Alterações cadastrais | Atualização do Saldo de FGTS** . 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11541909733271)

Pode-se fazer a seleção de funcionário e, posteriormente, em **executar**. Dessa forma o processo se finaliza, sendo executado novamente somente na próxima competência.

**Saiba Mais**[Como Fazer- Atualização Saldo FGTS](https://tdn.totvs.com/pages/releaseview.action?pageId=185760122)  
[Atualização Saldo FGTS](https://tdn.totvs.com/pages/releaseview.action?pageId=452718953)  
[Recálculo do Saldo de FGTS](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452718752)
