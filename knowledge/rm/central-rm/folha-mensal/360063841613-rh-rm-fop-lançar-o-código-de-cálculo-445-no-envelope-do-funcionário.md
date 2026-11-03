---
article_id: 360063841613
category: Folha Mensal
content_hash: 97c4149c23fbf30e491e03f9d3d51ea05d058d642df9c67d3e9c8d4a92a9fea7
fetched_at: '2026-06-28T22:46:59.427137+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Lançar o código de cálculo 445 no envelope do funcionário
type: support-article
updated_at: '2023-02-17T14:50:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063841613-RH-RM-FOP-Lan%C3%A7ar-o-c%C3%B3digo-de-c%C3%A1lculo-445-no-envelope-do-funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:04:35 min  
  
Dúvida**Como lançar o código de cálculo 445 no envelope do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Durante os primeiros quinze dias do afastamento da atividade por motivo de doença comum, doença ocupacional ou acidente do trabalho, cabe à empresa pagar ao segurado empregado o seu salário integral. Porém, a contribuição previdenciária patronal, a contribuição de terceiros e o SAT/RAT não incidem sobre esta importância paga pelo empregador referente a esses quinze primeiros dias que antecedem o benefício de auxílio-doença. De acordo com Jurisprudência consolidada do STJ, [Parecer SEI Nº 16120/2020/ME](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes/#7-23----29-12-2020----parecer-sei-n--16120-2020-me--como-deve-ser-tratada-a-incid-ncia-tribut-ria-nos-15-primeiros-dias-de-afastamento-que-antecedem-o-benef-cio-de-aux-lio-doen-a-), ficaram estabelecidos os critérios para cálculo do atestado médico que antecede ao Afastamento Previdenciário. Para atender a esta demanda, foi criado o código de cálculo 445.  
  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1-  Acessar: **Configurações | Parametrizador | Folha normal | Afastamento** e marcar a flag  **Lança evento de atestado médico via grupo de eventos**  concluir a parametrização, sair do sistema e logar novamente  
  
![](https://totvssuporte.zendesk.com/attachments/token/PKJm4HLjPVk8yJ4FcCIC2kUV6/?name=inline1012591735.png)  
  
**2-** Inserir o evento de atestado médico **Código de Cálculo 145** no grupo de eventos utilizado com o comportamento **ADICIONAR**![](https://totvssuporte.zendesk.com/attachments/token/rCJpcRNRmujDsRIgdIpAIn7oo/?name=inline1794069406.png)  
  
3- **Cadastrar o atestado** do funcionário com data início e sem data fim, conforme o parecer [PARECER SEI Nº 16120/2020/ME](https://www.gov.br/pgfn/pt-br/assuntos/legislacao-e-normas/documentos-portaria-502/parecer-sei-16120-atualizado.pdf)  
  
![](https://totvssuporte.zendesk.com/attachments/token/veAbz23UR2JtkoPFrAgLYhjXQ/?name=inline-779158591.png)  
  
Histórico de afastamento:  
  
![](https://totvssuporte.zendesk.com/attachments/token/NVAzn2C4CdCAEna2vg6LYInlQ/?name=inline783037913.png)  
  
4- **Lançar a folha do funcionário**. No envelope, será lançado o evento de atestado com código de cálculo 145. Portanto, a tratativa será substituir o evento com código de cálculo 145 pelo evento com código de cálculo 445 manualmente.  
  
![](https://totvssuporte.zendesk.com/attachments/token/SpizMTbeKAsKN3Ow0IbSJ0yWb/?name=inline-2062737254.png)  
  
 Substituindo o evento  
  
![](https://totvssuporte.zendesk.com/attachments/token/Ttr8YKLqvGJc6hAoE8ZOhbgia/?name=inline230568710.png)

Perceba que o valor calculado para o evento prevalecerá, portanto não é necessário alterar o valor. Em seguida, **clique em salvar e recalcule o envelope**. Desta forma o código de cálculo 445 ficará descrito no envelope do funcionário.  
  
**Importante**

* [PARECER SEI Nº 16120/2020/ME](https://www.gov.br/pgfn/pt-br/assuntos/legislacao-e-normas/documentos-portaria-502/parecer-sei-16120-atualizado.pdf) = Essa alteração é a aplicação do parecer da PGFN da não incidência de INSS Patronal (20% + RAT + Terceiros) **nos primeiros 15 dias de atestado**, quando houver, em seguida o afastamento previdenciário, seja por auxílio doença ou acidente de trabalho.
* Só impacta para os empregadores que tem empregados com atestados de mais de 15 dias no mês e não são optantes do Simples (com exceção do anexo IV).
* Essa não incidência de CPP nos primeiros 15 dias de atestado em caso de afastamento previdenciário é retroativo à comp. 11/2020.
* Esta não incidência de CPP é sobre a importância paga pelo empregador ao empregado nos 15 (quinze) primeiros dias que antecedem o auxílio doença ou acidente trabalho, ou seja, somente se na sequência houver afastamento previdenciário, não se refere a simples atestados menores de 15 dias.
* Em muitos casos daqui pra frente você pode precisar retificar a GFIP e/ou eSocial em função de no momento de lançar o atestado não saber se ele será ou não convertido em um afastamento de fato, já que é a perícia do INSS que define isso.

Em resumo, o evento com código de cálculo 445 só será lançado no envelope do funcionário se houver afastamento pela previdência acima de 15 dias. Para casos com até 14 dias, prevalece o código de cálculo 145 normalmente.  
  
**Saiba Mais**

[RM - FOP - Lançar evento de atestado médico para o envelope de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9218239867927-RM-FOP-Lan%C3%A7ar-evento-de-atestado-m%C3%A9dico-para-o-envelope-de-pagamento?source=search)

[Código de Cálculo 445 - Atestado médico com incidência somente segurado](https://tdn.totvs.com/pages/releaseview.action?pageId=589761956)

[Folha de Pagamento - Atestado médico com incidência somente segurado (CC445)](https://tdn.totvs.com/pages/releaseview.action?pageId=590618716#1-62563949)  
[RM - FOP - Atestado Médico Parecer SEI Nº 16120/2020/ME - 15 primeiros Dias (CC445)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060801754-RM-FOP-Atestado-M%C3%A9dico-Parecer-SEI-N%C2%BA-16120-2020-ME-15-primeiros-Dias-CC445-?source=search)
