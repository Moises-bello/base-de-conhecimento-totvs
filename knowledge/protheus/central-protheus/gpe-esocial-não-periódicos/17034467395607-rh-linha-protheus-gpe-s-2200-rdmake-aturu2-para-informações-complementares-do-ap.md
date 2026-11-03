---
article_id: 17034467395607
category: GPE - eSocial - Não Periódicos
content_hash: 1a9e635cf797099c3f170c62c952a07738c016d5e4c4b559a918630b94308377
fetched_at: '2026-06-28T22:45:05.985875+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - S-2200 - Rdmake ATURU2 para informações complementares
  do aprendiz
type: support-article
updated_at: '2026-06-16T11:25:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17034467395607-RH-Linha-Protheus-GPE-S-2200-Rdmake-ATURU2-para-informa%C3%A7%C3%B5es-complementares-do-aprendiz
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17034451435927) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como incluir informações na tabela RU2 (informações complementares menor aprendiz, utilizando o *rdmake* ATURU2?  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Criado o RDMAKE **ATURU2** que permitirá que os dados de Menor Aprendiz (campos Tipo de Inscrição - RA\_PLAPRE - e Número de Inscrição RA\_TIPCTA) sejam cadastrados separadamente do cadastro de Funcionários.  
  
Não serão mais utilizados os campos Tipo de Inscrição (RA\_TIPCTA) e Número de Inscrição (RA\_PLAPRE) presentes no cadastro de Funcionários - estes serão inclusive alterados como **Não usados** após atualização de dicionário e passam a ser utilizados os campos Tipo de Inscrição (**RU2\_TPINSC**) e Número de Inscrição (**RU2\_NUMINS**), **obrigatórios** quando o Tipo de Contratação é igual a **2-Contratação Indireta**.  
  
O conteúdo destes campos deverão ser carregados para tabela RU2 - Informações Complementares do Menor Aprendiz e acessados pelo novo cadastro.  
  
O objetivo da alteração é, além de atender ao eSocial, centralizar as informações em uma tabela específica para dados de Aprendiz.  
  
No  módulo Configurador, criar um novo item de menu com uso do *rdmake***ATURU2**, conforme abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17034177029271)  
  
Será apresentada uma tela com o objetivo da rotina, o botão abrir redireciona para este documento técnico.  
![image2023-7-17_16-20-31.png](https://tdn.totvs.com/download/attachments/777915746/image2023-7-17_16-20-31.png?version=1&modificationDate=1689621849163&api=v2)  
Será apresentada uma pergunta ao usuário se ele deseja que no *Log* de Ocorrências também sejam impressões os dados de Menor Aprendiz que já foram incluídos na tabela RU2:  
![image2023-7-17_16-20-51.png](https://tdn.totvs.com/download/attachments/777915746/image2023-7-17_16-20-51.png?version=1&modificationDate=1689621849037&api=v2)

Ao final do processo, é gerado o *Log* de Ocorrências:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17034382813719)

**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[Boletim técnico Rdmake Menor Aprendiz](https://tdn.totvs.com/display/public/PROT/DRHROTPRT-11322+DT+eSocial+rdmake+Menor+Aprendiz)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
