---
article_id: 39748574248215
category: Folha Mensal
content_hash: 2a06a2aea702361b5ce0d920931e1f5686d266598da97ab877e5b0c4f35f9f28
fetched_at: '2026-06-28T22:46:57.932668+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Calculo de Benefício de Funcionário: Erro de Benefício obrigatório
  não lançado'
type: support-article
updated_at: '2026-04-15T12:05:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39748574248215-RH-RM-FOP-Calculo-de-Benef%C3%ADcio-de-Funcion%C3%A1rio-Erro-de-Benef%C3%ADcio-obrigat%C3%B3rio-n%C3%A3o-lan%C3%A7ado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39748534924695) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como resolver a mensagem de erro "Um ou mais benefícios foram encontrados como Benefícios obrigatórios" no processo de Calculo de Benefício de Funcionário   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Quando esta opção está habilitada, o sistema passa a exigir que o respectivo benefício seja obrigatoriamente lançado no Gestão de Pessoas. Na ausência desse lançamento, o cálculo não poderá ser processado, resultando na mensagem apresentada.  
   
Diante desse contexto, para a correta tratativa do cenário, é fundamental inicialmente validar se o benefício em questão deveria, de fato, ter sido lançado. Abaixo seguem as orientações conforme cada situação:  
   
**Caso 1 – O benefício deveria ter sido lançado:**  
  
Nesse cenário, é necessário acessar o caminho:  
**Gestão de Pessoas | Valorização | Processos | Vinculação**, e identificar qual benefício do funcionário está com a opção **“Benefício Obrigatório”** marcada.

Para identificar qual benefício está configurado com a opção **“Benefício Obrigatório”** marcada, é necessário acessar o processo de vinculação e editar os cadastros de benefícios do funcionário. Durante a edição, a referida opção será exibida, permitindo sua correta identificação, conforme exemplificado a segui

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39748534925719)

[RH - RM - RHU - Realizar a vinculação de benefícios para os funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036132313-RH-RM-RHU-Realizar-a-vincula%C3%A7%C3%A3o-de-benef%C3%ADcios-para-os-funcion%C3%A1rios)

Após a identificação, deverá ser realizado o lançamento do benefício conforme a documentação abaixo:  
   
[RH - RM - RHU - Realizar o lançamento de benefícios para os funcionários e/ou dependentes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035960374-RH-RM-RHU-Realizar-o-lan%C3%A7amento-de-benef%C3%ADcios-para-os-funcion%C3%A1rios-e-ou-dependentes)  
   
**Caso 2 – O benefício não deveria ser obrigatório:**  
  
Nesse caso, será necessário acessar o processo de vinculação e excluir o benefício que está configurado com a opção **“Benefício Obrigatório”** marcada.  
Na sequência, o benefício deverá ser cadastrado novamente, garantindo que, neste novo cadastro, a referida opção permaneça desmarcada.

**Saiba mais:**

[RH - RM - RHU - Dúvidas frequentes: Benefícios e Remuneração Variável](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23502971115287-RH-RM-RHU-D%C3%BAvidas-frequentes-Benef%C3%ADcios-e-Remunera%C3%A7%C3%A3o-Vari%C3%A1vel)
