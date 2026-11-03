---
article_id: 4408150146071
category: Gestão de Distribuição (SIGAOMS)
content_hash: fec71eebdba59f9573ac8d8d0c3bfb45e0538d18e39f7e1c6ed02a9be1ae1080
fetched_at: '2026-06-28T22:45:49.552364+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: 'Logística - Linha Protheus - OMS - Cadastro de Janela de Entregas - OMSA350 '
type: support-article
updated_at: '2023-10-16T13:09:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408150146071-Log%C3%ADstica-Linha-Protheus-OMS-Cadastro-de-Janela-de-Entregas-OMSA350
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18298985993879) Tempo aproximado para leitura: **00:03:12 min****Dúvida**Como utilizar o **Cadastro de Janela de Entregas - OMSA350**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**A rotina **OMSA350** permite que seja elaborado um calendário para vínculo com clientes ou setores, com o objetivo de auxiliar na montagem da carga. Desta forma, as **Zonas**, **Rotas** e **Setores** com restrições na **data de entrega não são apresentados para marcação na montagem da carga**, quando o parâmetro **MV\_ROTATV** estiver ativo. Outra possibilidade é, pela utilização da ação **Seq. Ent.** no momento da montagem, **visualizar os Pedidos com restrição** por meio da visualização do **status Vermelho**, indicando a **restrição por calendário**.  
  
O calendário do **tipo semanal** visa a definição por dias semana. Por exemplo **segunda-feira, terça-feira**, **quarta-feira**, **entre outros**. O calendário do **tipo mensal** permitirá selecionar dias específicos. Por exemplo **01, 02, entre outros, que se aplicarão a todos os meses**. A frequência semanal ou mensal definida no calendário deve ser configurada para apresentar as particularidades que um determinando cliente tem em alguns dias da semana ou alguns dias do mês.  
  
Abaixo descrevemos um exemplo de utilização:  
  
**1**. Parâmetro **MV\_ROTATV** preenchido igual a **1**  
  
**2. Indicar Quais Setores Serão Atendidos em Quais Dias da Semana**  
Acesse o programa **OMSA350** e informe qual a frequência semanal desejada. Exemplo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408224776855)

![calendario.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408224732951)

**3. Acesse Atualizações/Roteirização/Setores por Zona - OMSA080**: informe o código de calendário no campo **DA6\_CODCAL** **000002** para os setores que serão atendidos na **Segunda-feira e Quarta-feira.** Em nosso exemplo vamos informar somente no **Setor 1**:

**![setores_por_zona.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408225298583)**

**4**.Considerando a data base do Sistema em **10/09/2021 - Sexta-feira**, como o calendário está configurado para entregas na **Segunda-feira e Quarta-feira**, os pedidos dos clientes do **Setor 1 da Zona 0000030** não serão demonstrados para a seleção na rotina de **Montagem de Carga - OMSA200**:

![montagem_carga_1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408230583063)

Veja que estando com a data base do Sistema em **13/09/2021 - Segunda-feira**, os os pedidos dos clientes do **Setor 1 da Zona 0000030** são demonstrados para a seleção na rotina **OMSA200**:

**![montagem_2.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408231065623)**

**Importante**  
O parâmetro **MV\_ROTATV**, indica se a roteirização do **TOTVS OMS - Order Management System** deve analisar mais de uma condição na roteirização. Quando configurado como **1**, fará com que a rotina **Montagem de Carga - OMSA200** considere as restrições de calendário para definir se as **Zonas**, **Rotas** e **Setores** serão apresentadas para seleção. Lembrando que a data de entrega da carga é considerada, por padrão a data atual do Sistema.  
  
**Saiba mais**A documentação detalhada da rotina com outros exemplos de parametrizações pode ser acessada no *link:*: [Cadastro de Janela de Entregas - OMSA350](https://tdn.totvs.com/pages/viewpage.action?pageId=569489314)
