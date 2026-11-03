---
article_id: 39663133726615
category: Folha Mensal
content_hash: 062a55535bfede31e6cccd782a844c3ac618add948d5829b8ec6be7e5dffb672
fetched_at: '2026-06-28T22:46:57.940436+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Analítica: Desconsiderar base de INSS 13º salário no
  cálculo de INSS Empresa'
type: support-article
updated_at: '2026-04-10T19:42:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39663133726615-RH-RM-FOP-Folha-Anal%C3%ADtica-Desconsiderar-base-de-INSS-13%C2%BA-sal%C3%A1rio-no-c%C3%A1lculo-de-INSS-Empresa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39663167552535) Tempo aproximado para leitura: **00:02:34 min**  
  
**Dúvida**  
Como parametrizar o sistema para que o valor da base de INSS do 13º salário não seja considerado no campo INSS Empresa do relatório de Folha Analítica em empresas optantes pela desoneração da folha de pagamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Não existe um parâmetro nativo na Folha Analítica para desconsiderar automaticamente o 13º salário no cálculo do INSS Empresa. Com a adoção do eSocial, a conferência de valores patronais deve ser realizada obrigatoriamente através do Relatório de Conferência de INSS Patronal, que segue as regras de agrupamento e arredondamento do Governo.

A Folha Analítica tem por objetivo apresentar valores e bases de cálculo individuais dos funcionários, não sendo a ferramenta oficial para validação de encargos patronais após a implementação do eSocial.

Caso o usuário opte por manter a visualização destes valores no relatório de Folha Analítica para fins de conferência interna, deverá realizar uma customização através do uso de fórmulas.

1. Acesse o menu **Administração de Pessoal | Fórmulas** e crie uma nova sentença para compor o cálculo desejado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39663133693335)

2. A fórmula deve ser estruturada para somar a base do INSS normal e, caso necessário, utilizar a função de Acumulador para incluir bases de eventos pagos a autônomos e diretores, desconsiderando os valores de 13º salário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39663133695767)

3. Após criar e salvar a fórmula, acesse a rotina **Folha Mensal | Folha Analítica** para realizar a geração do relatório;

4. No campo destinado ao cálculo do INSS Empresa, vincule a fórmula customizada conforme as orientações de parametrização do relatório:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39663167556119)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39663133698071)

5. Gere o relatório novamente para validar a exibição dos valores conforme a regra de negócio da empresa.

**Saiba Mais**

[RM - RM - FOP - Folha Analítica: Parametrização de Fórmulas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015423792-RH-RM-FOP-Folha-Anal%C3%ADtica-Parametriza%C3%A7%C3%A3o-de-F%C3%B3rmulas)

[RH - RM - FOP - eSocial - Middleware: Relatório de Conferência de INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407770756247-RH-RM-FOP-eSocial-Middleware-Relat%C3%B3rio-de-Confer%C3%AAncia-de-INSS)
