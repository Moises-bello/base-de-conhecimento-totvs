---
article_id: 14847389762583
category: GPE - eSocial - Não Periódicos
content_hash: 22774592da512afea304e7cb56c79a903509106b7604b4e23e3b0489ff56b65b
fetched_at: '2026-06-28T22:45:04.457946+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 - Como ajustar o valor do campo
  RA_CODUNIC com o valor existente no campo C9V_MATRIC
type: support-article
updated_at: '2026-06-16T11:51:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14847389762583-RH-Linha-Protheus-GPE-eSocial-S-2200-Como-ajustar-o-valor-do-campo-RA-CODUNIC-com-o-valor-existente-no-campo-C9V-MATRIC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16589786154903) Tempo aproximado para leitura: 00:06:00min  
  
**Dúvida**  
Como ajustar o valor do campo RA\_CODUNIC com o valor existente no campo C9V\_MATRIC? Como ajustar a matricula esocial no cadastro do funcionário?  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Criamos a rotina **ATUCODUNIC (Atualiza Matricula eSocial)** para ajustar o valor do **campo RA\_CODUNIC** com o valor existente no campo **C9V\_MATRIC**.   
  
A rotina está disponível apenas para cliente que fazem uso do TAF, sendo necessário acessar a central de *downloads* para atualizar o **rdmake ATUCODNIC**. Acesse o *link* a seguir:[**RH Expedição Continua**](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/rh_expedicao_continua)  
  
Após atualização, siga os passos a seguir:

- Usuário informa a filial e matrícula que deve ser processada;  
- Pelo CPF desta matrícula é(são) identificado(s) o(os) registros no TAF que estão ativos;  
- Caso seja identificada diferença na matrícula esocial (RA\_CODUNIC vs C9V\_MATRIC) será apresentada tela para seleção/confirmação do ajuste que será realizado.  
  
Para **criar a rotina no menu**, acesse o SIGACFG:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14845306514327)  
  
Será apresentada uma tela com o objetivo da rotina, o botão abrir redireciona para este documento técnico. Deve-se obrigatoriamente preencher os parâmetros.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14846785945239)  
  
Exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14846799521047)  
  
Será apresentada tela de **confirmação do de/para**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14846850669463)  
  
Será demonstrado ao final do processo, **log geração**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14846867444631)

**Observação:**  
Se durante a pesquisa pelo CPF do funcionário no TAF, for encontrado mais de um registro ativo, como por exemplo em casos de múltiplos vínculos, poderá ser apresentada a relação de matrículas existentes para correta associação. Porém, esta relação apresentará somente os registros que NÃO possuem vínculos na SRA.

**Exemplo de processamento** com esta tela:

- Inicia-se o processamento da matrícula 000001 de CPF X;  
- CPF X possui dois registros no TAF, ambos ativos;  
- Comparamos a matrícula eSocial da matrícula 000001 existente no campo RA\_CODUNIC (Cadastro de Funcionários - GPE) com o existente no campo C9V\_MATRIC (Cadastro do Trabalhador - TAF) destes dois registros e ambos são diferentes;  
- Antes de apresentar as matrículas eSocial da tabela C9V, validamos se estão associadas em outra matrícula do cadastro de funcionários, se não estiverem, o usuário deverá selecionar em tela qual destas matrículas pertence ao funcionário em processamento.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14846946507031)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[Boletim Técnico Atualiza Matricula eSocial](https://tdn.totvs.com/pages/releaseview.action?pageId=758507482)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
