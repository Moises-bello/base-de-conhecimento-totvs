---
article_id: 360039466294
category: GPE - eSocial - Não Periódicos
content_hash: e56900cdf10262371d2c3a65577929d34d9c4783111963a8e6508daaba68595d
fetched_at: '2026-06-28T22:45:04.494296+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 - Como executar o rdmake UPDCODUNIC,
  para correção de matriculas duplicadas no TAF
type: support-article
updated_at: '2026-06-16T13:34:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039466294-RH-Linha-Protheus-GPE-eSocial-S-2200-Como-executar-o-rdmake-UPDCODUNIC-para-corre%C3%A7%C3%A3o-de-matriculas-duplicadas-no-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41262126108311) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como executar o rdmake **UPDCODUNIC**, para correção de matriculas duplicadas no TAF?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
Para a utilização da rotina, deve existir compilado no RPO o rdmake **UPDCODUNIC** e deve ser efetuado a alteração no menu do módulo Gestão de Pessoal, efetuando a inclusão do menu como função de **usuário.**  
  
[MP - GPE - Como excluir ou incluir rotinas no menu?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013342191)  
  
Caso não tenha o rdmake no RPO ele pode ser encontra na página de downloads como [RDMAKES\_RH](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RDMAKES_RH)  
  
Para executar o *rdmake* que foi compilado em seu ambiente, realize o procedimento abaixo para ajuste da informação:   
  
**Passo 1:** Acesse a rotina criada (print de exemplo): 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053014113)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052114114)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053014233)  
  
Note que ao emitir o relatório, foi apresentado que existem dois CPF’s diferentes com o mesmo número de matrícula. A rotina fará automaticamente esta validação em seu ambiente.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053014353)  
  
**Passo 2:**Ao sair do relatório emitido, será apresentada a mensagem abaixo para correção:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052114334)  
  
**Passo 3:**O sistema emite a mensagem do registro do funcionário que deverá ser **Excluído** **Manualmente** do TAF (apenas no TAF). E realizará a alteração da **Matrícula eSocial** (RA\_CODUNIC) do funcionário no **Cadastro de funcionários** (SRA). Para a nova matricula (RA\_CODUNIC) será gerado de forma automática o S-2200 no TAF:   
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052114434)  
  
Observação: Caso um dos funcionário já esteja transmitido ao esocial e no TAF esteja com número de protocolo, a matrícula do mesmo não será alterada. Apenas haverá alteração no funcionário que possui duplicidade de matrícula e ainda não foi enviado ao TAF e ao governo.  
  
**Artigos Relacionados:**  
[RH - Linha Protheus - GPE - eSocial - S-2200 - Matrícula duplicada no cadastro do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034699694-RH-Linha-Protheus-GPE-eSocial-S-2200-Matr%C3%ADcula-duplicada-no-cadastro-do-funcion%C3%A1rio)  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Perguntas frequentes FGTS Digital](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)  
  
Para conhecimento dos eventos futuros, acessa a nossa página [*TOTVS Informa*](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos".
