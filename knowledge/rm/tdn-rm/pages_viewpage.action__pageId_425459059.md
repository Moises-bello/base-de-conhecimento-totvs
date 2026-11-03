---
content_hash: 9993c2f017aefbeae242f4cf846cdb75e742adcc511fa63bc0678f0b1468a423
fetched_at: '2026-06-29T00:09:33.817191+00:00'
page_id: '425459059'
product: rm
source: tdn-rm
title: Integração com Totvs Gestão de Pessoas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459059
version: 2
---

**Integração com Totvs Gestão de Pessoas**

---

O TOTVS Aprovações e Atendimento realiza integração com o Totvs Gestão de Pessoas na realização de aprovação de requisições, como por exemplo: aumento de quadro de funcionários, desligamento, treinamentos entre outros.   
**Desenvolvimento/Procedimento**   
1. Criar um tipo de atendimento.   
2. Criar uma etapa e indicar que será a primeira etapa de um possível fluxo.  
3. Criar um grupo de atendimento e vincular o tipo de atendimento criado a esse grupo.  
4. Criar as outras etapas e em seguida o fluxo de etapa.  
OBS: Em todos os procedimentos a caixa "Ativar Fluxo de tarefa" deverá estar marcada para que o procedimento funcione.  
5. Pronto. O tipo de atendimento está criado e vinculado ao grupo de atendimento que será utilizado na integração com o Vitae. Agora temos que acessar o RM Vitae e realizar a parametrização necessária.   
Acesse: Opções / Parâmetros / RM Vitae / Tipos de requisição  
6. Criar o tipo de requisição desejado ou editar uma já existente do sistema (aumento de quadro, desligamento, transferência, etc) e informar o tipo de atendimento e grupo de atendimento que foi criado no TOTVS Aprovações e Atendimento para utilização dessa integração.   
7. Devemos alterar o mapeamento do fluxo indicando qual será o status da requisição do Vitae em cada etapa do atendimento do Totvs Gestão de Relacionamento com o Cliente.   
OBS: é obrigatório ter um parecer com o status Aprovado. O restante pode ficar em andamento e reprovado, de acordo com a regra de negócio do cliente.  
Acesse: Opções / Parâmetros / RM Vitae / Tipos de requisição | Mapeamento do fluxo | Status do parecer  
**Descrição do Processo**  
• A integração entre o Vitae e o TOTVS Aprovações e Atendimento consiste em ter uma aprovação de requisições de variados tipos. No momento que a requisição está sendo criada, um atendimento é inserido no TOTVS Aprovações e Atendimento. O status do atendimento do TOTVS Aprovações e Atendimento e da requisição do Vitae são independentes, por exemplo: posso ter uma requisição aprovada com o atendimento em andamento. É recomendado que o status do parecer deve seguir o mesmo status do atendimento. Por exemplo: na etapa 3 o atendimento será concluído, logo alteramos o status do parecer no RM Vitae, referente a essa etapa, para Aprovado e assim por diante.  
Veja o passo a passo, com informações de tela em nosso blog.

|  |  |
| --- | --- |
|  | Recursos Adicionais |

---

[Blog - Integração Totvs Gestão de Pessoas](http://totvsconnect.blogspot.com/2010/11/integracao-com-o-totvs-gestao-de)
