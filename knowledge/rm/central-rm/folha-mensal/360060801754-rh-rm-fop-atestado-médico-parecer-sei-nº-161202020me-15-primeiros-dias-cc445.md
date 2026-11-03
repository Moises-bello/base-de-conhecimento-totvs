---
article_id: 360060801754
category: Folha Mensal
content_hash: 6ec53267af25cfd57caf8f3e2fc48ba33d58b41e8fb68924d98a7fcc82066073
fetched_at: '2026-06-28T22:46:59.440905+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP -  Atestado Médico Parecer SEI Nº 16120/2020/ME - 15 primeiros
  Dias (CC445)
type: support-article
updated_at: '2026-05-12T13:32:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060801754-RH-RM-FOP-Atestado-M%C3%A9dico-Parecer-SEI-N%C2%BA-16120-2020-ME-15-primeiros-Dias-CC445
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:06:20 min****Dúvida**Como fazer no sistema o lançamento do atestado com a incidência somente segurado conforme consta no PARECER SEI Nº 16120/2020/ME?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**Durante os primeiros quinze dias do afastamento da atividade por motivo de doença comum, doença ocupacional ou acidente do trabalho, cabe à empresa pagar ao segurado empregado o seu salário integral, porém a contribuição previdenciária patronal, a contribuição de terceiros e o SAT/RAT não incidem sobre esta importância paga pelo empregador referente a esses quinze primeiros dias que antecedem o benefício de auxílio-doença, de acordo com Jurisprudência consolidada do STJ, [Parecer SEI Nº 16120/2020/ME](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes/#7-23----29-12-2020----parecer-sei-n--16120-2020-me--como-deve-ser-tratada-a-incid-ncia-tribut-ria-nos-15-primeiros-dias-de-afastamento-que-antecedem-o-benef-cio-de-aux-lio-doen-a-), ficaram estabelecidos os critérios para cálculo do atestado médico que antecede ao Afastamento Previdenciário.  
  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Deverá ser criado um evento com CC445. Para isso, acesse: **Administração de Pessoal | Eventos | Eventos.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9554405686551)**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9554853819799)  
  
2. Os eventos com códigos de cálculos de [Atestado médico com incidência somente segurado- CC445,](https://tdn.totvs.com/pages/viewpage.action?pageId=589761956) não deverão ter incidências de INSS marcado, conforme imagem abaixo:  
  
 ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9554952881687)  
  
Este evento deverá ser lançado manualmente no envelope de pagamento, para que o CC445 esteja disponível, será necessário realizar algum recálculo ou cálculo de eventos. Poderá executar qualquer processo de cálculo, como por exemplo, o processo **Executa Recálculo***.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9555102351895)*3. Cadastre o afastamento sem data de retorno ou com mais de 15 dias como consequência gerando o afastamento previdenciário.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9555200080791)  
  
4. Em casos de o cliente se encontrar nessa situação, foi criado o CC445, para que cliente consiga lançar o evento para fins obrigatórios e em caso de relatórios, como [Sefip](https://tdn.totvs.com/pages/editpage.action?pageId=590043088).  
  
Em situações que precisarem, basta criar o CC445 conforme descrito anteriormente, lembrando que esse evento deve ser lançado **manualmente**, o evento deve ser lançado em substituição ao CC145.  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9555476312215)  
  
**Glossário  
SAT**- Seguro de Acidente do Trabalho  
**RAT**- Riscos Ambientais do Trabalho  
**CPP**- Contribuição Patronal Previdenciária  
**GFIP**- Guia de Recolhimento do Fundo de Garantia por Tempo de Serviço e Informações à Previdência Social  
**STJ**- Superior Tribunal de Justiça  
**PGFN**- Procuradoria Geral da Fazenda Nacional  
**SEFIP-** Sistema Empresa de Recolhimento do FGTS e Informações à Previdência Social   
  
**Importante**

* Essa alteração é a aplicação do parecer da PGFN da não incidência de INSS Patronal - 20% + RAT + Terceiros - nos primeiros 15 dias de atestado, quando houver, em seguida o afastamento previdenciário, seja por auxílio doença ou acidente de trabalho.
* Só impacta para os empregadores que tem empregados com atestados de mais de 15 dias corridos e não são optantes do Simples - com exceção do anexo IV- .
* Essa não incidência de CPP nos primeiros 15 dias de atestado em caso de afastamento previdenciário é retroativo à comp. 11/2020.
* Esta não incidência de CPP é sobre a importância paga pelo empregador ao empregado nos 15 -quinze - primeiros dias que antecedem o auxílio doença ou acidente trabalho, ou seja, somente se na sequência houver afastamento previdenciário, não se refere a simples atestados menores de 15 dias.
* Em muitos casos daqui pra frente você pode precisar retificar a GFIP e/ou eSocial em função de no momento de lançar o atestado não saber se ele será ou não convertido em um afastamento de fato, já que é a perícia do INSS que define isso.

**Saiba Mais**  
[Não Incidência da Contribuição Previdenciária nos Primeiros 15 dias de Atestado que Antecedem ao Afastamento Previdenciário](https://tdn.totvs.com/pages/releaseview.action?pageId=590021388)
