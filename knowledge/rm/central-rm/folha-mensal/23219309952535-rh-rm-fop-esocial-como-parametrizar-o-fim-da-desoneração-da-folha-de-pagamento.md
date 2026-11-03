---
article_id: 23219309952535
category: Folha Mensal
content_hash: 68d18e28e0d66e8aae23b7d4a2c3dd6d2a4375511a89afd79f45d10bbd67e021
fetched_at: '2026-06-28T22:46:58.161881+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - eSocial - Como parametrizar o fim da desoneração da folha de
  pagamento
type: support-article
updated_at: '2024-06-17T14:11:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23219309952535-RH-RM-FOP-eSocial-Como-parametrizar-o-fim-da-desonera%C3%A7%C3%A3o-da-folha-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23219309928471) Tempo aproximado para leitura: **00:02:39 min****Dúvida**Como parametrizar o fim da desoneração da folha de pagamento?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes processos:

* **ESOCIAL**

1. Para o ajustar a informação no governo, será necessário enviar o S-1000 com a devida alteração. Para tal, acesse **eSocial | Informações do Empregador** e altere o campo do **Indicativo de Desoneração da Folha**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23363301483927)

2. Será gerado um S-1000 com a informação da alteração. Ajuste a competência para o mês 04/2024 e, após, faça a geração do XML;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23363301486871)

3. Envie o S-1000 ao governo e, após ele ser aceito pelo RET, envie o S-1299 (**não envie o S-1280 neste caso**). Se o S-1299 (do período de apuração 04/2024), já tenha sido enviado ao governo com a informação da desoneração , será necessário r**eabrir o período** através do [S-1298](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5676190571799-RH-RM-FOP-eSocial-Como-realizar-a-reabertura-da-folha-de-pagamento-no-eSocial-utilizando-o-evento-S-1298), **excluir o S-1280 através do [S-3000](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034224074-RH-RM-FOP-eSocial-Utiliza%C3%A7%C3%A3o-do-S-3000-para-exclus%C3%A3o-de-eventos)** e, após enviar novamente o [S-1299](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6268527168919-RH-RM-FOP-eSocial-Como-gerar-o-evento-S-1299-ap%C3%B3s-a-reabertura-do-per%C3%ADodo#:~:text=1.%20Acesse%20o%20menu%20eSocial%20%7C%20Gerar%20XML,o%20final%20para%20concluir%20a%20gera%C3%A7%C3%A3o%20do%20XML.).

Abaixo, pergunta 10.37 da [FAQ](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes#11--seguran-a-e-sa-de-do-trabalhador) liberada pele eSocial:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23341818900119)

* **FOLHA ANALÍTICA**

1. Para que a desoneração não seja incluída na Folha Analítica, é necessário acessar a parametrização do relatório na aba **Folha Mensal | Folha Analítica** e informar o percentual de 20% no campo **%Empresa**, conforme exemplo abaixo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23219319403543)

2. Além disso, caso a empresa utilize **Parâmetros específicos da coligada**, o mesmo percentual deverá ser informado conforme o campo **%Empresa** da imagem a seguir;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23219319406487)

**Importante**A alíquota padrão do INSS (Instituto Nacional do Seguro Social) paga pelas empresas sobre a folha de pagamento é geralmente 20%. No entanto, **existem algumas variações e condições especiais** que podem alterar essa porcentagem. É necessário que seja informado no campo **%Empresa**, o percentual que é **utilizado pela sua Instituição**. Verifique todo o processo de parametrização [CLICANDO AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010863672-RM-FOP-Parametriza%C3%A7%C3%A3o-do-INSS-empresa-na-folha-anal%C3%ADtica).

* **ENCARGOS**

1. Para que a desoneração não seja incluída no **Encargo**, é necessário acessar na aba **Encargos |  Cadastro | Encargos** e informar o percentual de 20%, ou conforme a necessidade da empresa, no campo **Porcentagem** como no exemplo abaixo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23220184966807)

2. Caso o encargo seja do tipo **A - Calculado por formula** é necessário ajustar a estrutura da fórmula para que a mesma considere o devido percentual.

**Saiba mais**Para mais informações sobre os encargos, acesse:  
     - [RH - RM - FOP - Geração do encargo TIPO 3 Base: incidência de INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14470625288215-RH-RM-FOP-Gera%C3%A7%C3%A3o-do-encargo-TIPO-3-Base-incid%C3%AAncia-de-INSS)

Para mais informações sobre como desonerar uma empresa no eSocial , acesse:  
     - [RH - RM - FOP - eSocial - Como desonerar uma empresa no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028307112-RH-RM-FOP-eSocial-Como-desonerar-uma-empresa-no-eSocial)  
     - [Desoneração da Folha de Pagamento - Nota de esclarecimento RFB - TOTVS](https://www.totvs.com/blog/fiscal-clientes/desoneracao-da-folha-de-pagamento-nota-de-esclarecimento-rfb/?utm_source=whatsapp&utm_medium=-&utm_campaign=rh&utm_term=gsp&utm_content=-)
