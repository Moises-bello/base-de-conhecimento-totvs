---
article_id: 17011174941335
category: GPE - eSocial - Não Periódicos
content_hash: 376a24e443b0d32d30a5589c09fc6bbc7a598809cc35138b71c8c907cb17c407
fetched_at: '2026-06-28T22:45:05.977282+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - S-2200 - Como preencher as Informações complementares
  relacionadas ao aprendiz
type: support-article
updated_at: '2026-06-16T13:34:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17011174941335-RH-Linha-Protheus-GPE-S-2200-Como-preencher-as-Informa%C3%A7%C3%B5es-complementares-relacionadas-ao-aprendiz
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17011188429207) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como enviar no evento S-2200 as Informações relacionadas ao aprendiz?  
**Codigo da ocorrência: 8** - Localização: /eSocial/evtAdmissao/vinculo/infoRegimeTrab/infoCeletista  
Descrição: Grupo 'Informacoes relacionadas ao aprendiz' deve ser preenchido.  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para atender o leiaute vigente, os eventos S-2200/S-2205/S-2206 no caso de contratação/alteração de jovem aprendiz, deve ser gerado contendo as informações abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20822204917911)  
  
No sistema foi criada a **tabela RU2** para armazenar os dados da rotina **Informações Complementares do Menor Aprendiz.**  
  
Após confirmar a admissão do aprendiz, será demonstrada a tela a seguir:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17010865474839)  
  
Ao confirmar a tela acima, o sistema mostrará a rotina de Informações Complementares do Menor Aprendiz, para que possa ser informado o Indicativo de Modalidade de Contratação, Tipo de Inscrição, Número de Inscrição, CNPJ Entidade Qualificadora e CNPJ Atividades Praticas.  
  
Caso não seja preenchido no momento da admissão, é possível acessar a rotina através do caminho **Atualizações - Funcionários - Alterar - Outras Ações - Inf. Compl. Menor Aprendiz**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23129415084055)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23129415100567)**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23129452881559)  
  
Para o preenchimento correto das informações, verifique sempre as validações de cada campo conforme leiaute vigente do eSocial: <https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-02-2024-rev-29-10-2024/index.html#2200_vinculo_infoRegimeTrab_infoCeletista_aprend>   
  
Com essa alteração, não serão mais utilizados os campos  Tipo de Inscrição (RA\_TIPCTA) e Número de Inscrição (RA\_PLAPRE) presentes no cadastro de Funcionários, estes serão inclusive alterados como 'Não usados' após atualização de dicionário e passam a ser utilizados os campos Tipo de Inscrição (**RU2\_TPINSC**) e Número de Inscrição (**RU2\_NUMINS**), obrigatórios quando o Tipo de Contratação é igual a **2-Contratação Indireta**.

O conteúdo destes campos deverão ser carregados para tabela RU2 - Informações Complementares do Menor Aprendiz e acessados pelo novo cadastro.

O objetivo da alteração é, além de atender ao eSocial, centralizar as informações em uma tabela específica para dados de Aprendiz.  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[Boletim Técnico Tabela Aprendiz](https://tdn.totvs.com/display/public/PROT/DRHROTPRT-11318+DT+eSocial+-+Tabela+Menor+Aprendiz)  
[Boletim Técnico Tela Inf. Complementares Menor Aprendiz](https://tdn.totvs.com/display/public/PROT/DRHROTPRT-11320+DT+eSocial+-+Tela+Inf.+Complementares+Menor+Aprendiz)  
[RH - Linha Protheus - GPE - S-2200 - Rdmake ATURU2 para informações complementares do aprendiz](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17034467395607-RH-Linha-Protheus-GPE-S-2200-Rdmake-ATURU2-para-informa%C3%A7%C3%B5es-complementares-do-aprendiz)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
