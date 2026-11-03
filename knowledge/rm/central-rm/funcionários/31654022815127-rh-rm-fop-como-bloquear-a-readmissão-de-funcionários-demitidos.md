---
article_id: 31654022815127
category: Funcionários
content_hash: 28fa8e7a1043d99beb86a07beeb49ba23ae82082b90403c4e8f06683f0965a81
fetched_at: '2026-06-28T22:47:03.141614+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: RH - RM - FOP - Como bloquear a readmissão de funcionários demitidos?
type: support-article
updated_at: '2025-04-25T01:01:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31654022815127-RH-RM-FOP-Como-bloquear-a-readmiss%C3%A3o-de-funcion%C3%A1rios-demitidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31654031777943) Tempo aproximado para leitura: **00:01:40 min** **Dúvida**Como realizar o cadastro da admissão de funcionários no RM?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para que o funcionário seja bloqueado para readmissão, basta realizar a configuração através de um campo complementar de funcionários conforme exemplo abaixo:

**Passo 1** - **Criar um campo complementar de funcionários em Administração de Pessoal | Campos Complementares | Funcionários.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31654022790295)

**Passo 2** - Acessar o cadastro do funcionário "DEMITIDO" e informar SIM no campo complementar criado no Passo 1.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31654022791063)

**Passo 3** - Criar uma fórmula de cálculo conforme exemplo abaixo em Administração de Pessoal | Fórmulas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31654031779863)

**Passo 4:** Acesse o Parametrizador da Folha de Pagamento em: Configurações > Parametrizador > Funcionário > Restrições Cadastrais.

Em seguida, informe a fórmula criada no Passo 3 no campo **"Fórmula para Validar Readmissão".**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31654022794135)

**Passo 5:** Por fim, acesse o menu Administração de Pessoal e execute o processo de Readmissão de Funcionários. Após a finalização, o log do processo indicará a quantidade de registros que foram bloqueados pela fórmula aplicada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31654031781271)

**Comunicado Importante:** A configuração e a fórmula utilizada na construção desse material são de exemplo. Caso seja necessário aplicar uma lógica mais específica para sua operação, entre em contato com nosso time de consultoria.

**Saiba Mais:**  
[Readmissão de Funcionários](https://tdn.totvs.com.br/pages/releaseview.action?pageId=667373225#1-2)
