---
article_id: 360016010332
category: RH - Folha de Pagamento
content_hash: 73b40dd9ccf707710bd186b75e791bdd8cb6d6d8e1e5b4585cd09f7f4c61ef70
fetched_at: '2026-06-28T22:44:12.079007+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de horas extras e DSR rateados automaticamente
  através da rotina de lançamentos mensais
type: support-article
updated_at: '2025-07-23T17:01:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016010332-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-horas-extras-e-DSR-rateados-automaticamente-atrav%C3%A9s-da-rotina-de-lan%C3%A7amentos-mensais
---

#### time.png Tempo aproximado para leitura: **00:02:30 min**

**Dúvida**Como efetuar o cálculo de horas extras e DSR rateados automaticamente através da rotina de lançamentos mensais?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução**Esse texto, trata do rateio automático de horas extras e DSR, **sem inclusão na programação de rateio** e **rateado de acordo com o rateio do salário mensal**.Para solucionar essa dúvida, realize os seguintes passos:  
  
**1**. Será necessário ativar o Mnemônico **P\_LRATINFO**, deixando o conteúdo como: .T.

- Atualizações/ Definições de cálculo / Mnemônicos  
  
![101.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360011934311)

**Obs:** Se o mnemônico P\_LRATINFO estiver como .F., não rateará a verba e calculará a verba de acordo com o centro de custo que foi informado.  
  
**2**. Verificar configuração das seguintes verbas:

- Salário : Rateio C. Cto = BASE.  
  
![100.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360011936172)  
  
- Horas extras: Rateio C. Cto = SIM.  
  
![102.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360011936412)  
  
- DSR: Rateio C. Cto = SIM.  
  
![103.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360011934571)

**3**. Em seguida as verbas de salário (ID **0031)** devem ser **rateadas** de acordo com os **dias de alocação** do funcionário em **cada centro de custo.**  
  
Já as horas extras podem ser lançadas em sua **totalidade.** Lembrando que o lançamento sendo efetuado desta forma, as horas extras serão **divididas** de acordo com a **proporcionalidade** dos **dias trabalhados** no centro de custo **informado** com a verba de ID **0031.**  
  
- Para lançamento, acesso no menu **Atualizações > Lançamentos > Por funcionário.** Selecione o funcionário e clique em Incluir.  
  
![105.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360011935051)  
  
Caso queira visualizar o cálculo do rateio do funcionário após lançamento para verificar a funcionalidade da rotina em **Outras ações > Gravar  > Calcular lançamento(F6) > Consultar cálculo**:  
  
![106.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360011936792)  
  
**4**. No cálculo realizado as verbas de **Horas Extras** e **DSR** já serão calculadas de acordo com rateio de salário. Segue exemplo após cálculo:  
  
![107.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360011936992)

**Saiba Mais**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
