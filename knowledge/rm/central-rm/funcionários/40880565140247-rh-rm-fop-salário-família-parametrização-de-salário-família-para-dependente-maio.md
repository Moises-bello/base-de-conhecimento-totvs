---
article_id: 40880565140247
category: Funcionários
content_hash: f263f8055038d90d686293a89bef5b141bd97ff027517da256c076fd1e7bd655
fetched_at: '2026-06-28T22:47:03.119141+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: 'RH - RM - FOP - Salário Família: Parametrização de Salário Família para dependente
  maior de 14 anos deficiente'
type: support-article
updated_at: '2026-06-01T16:21:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40880565140247-RH-RM-FOP-Sal%C3%A1rio-Fam%C3%ADlia-Parametriza%C3%A7%C3%A3o-de-Sal%C3%A1rio-Fam%C3%ADlia-para-dependente-maior-de-14-anos-deficiente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40880565131799) Tempo aproximado para leitura: **00:01:29 min**  
  
**Dúvida**  
Como parametrizar o RM  para manter o pagamento do benefício de Salário Família para um dependente que possui idade superior a 14 anos, mediante a comprovação de laudo de deficiência/invalidez?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**  
Para que o sistema continue calculando e pagando o Salário Família para dependentes com idade superior a 14 anos que sejam inválidos, é necessário ajustar o grau de parentesco no cadastro do dependente. O sistema valida essa condição específica para manter o direito ao benefício sem o limitador de idade cronológica.

1. Acesse o cadastro do funcionário e vá até a aba Dependentes. Em seguida, selecione o dependente desejado e clique em Editar, conforme o exemplo da imagem abaixo: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40880562028439)

2. Localize o campo **Grau de Parentesco**. Altere a opção preenchida para o código **3** (que corresponde à classificação de dependente inválido/filho inválido):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40880565132951)

3. Salve as alterações. Realize um novo cálculo da folha de pagamento para validar que o benefício voltará a ser pago normalmente.

**Saiba Mais:**

[TDN: Dependentes](https://tdn.totvs.com/display/public/LRM/Dependentes)

[RH - RM - FOP - Salario Família: Como é concedido o pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12323698142615-RH-RM-FOP-Salario-Fam%C3%ADlia-Como-%C3%A9-concedido-o-pagamento)
