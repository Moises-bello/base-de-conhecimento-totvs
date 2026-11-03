---
article_id: 40065914922647
category: RH - Cadastros
content_hash: fe31b13f7442ce762e2a1f19bb2b28c81fa51d6e2e5d824d7f4962098da00a0e
fetched_at: '2026-06-28T22:43:25.942106+00:00'
product: protheus
section_id: 360010781894
source: central-protheus
title: RH - Linha Protheus - GPE - O que verificar quando o GPEWORD não funciona
type: support-article
updated_at: '2026-06-25T11:08:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40065914922647-RH-Linha-Protheus-GPE-O-que-verificar-quando-o-GPEWORD-n%C3%A3o-funciona
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40065914913687) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
O que verificar quando o GPEWORD não funciona  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Sugerimos realizar os processo abaixo caso não esteja conseguindo gerar documentos na rotina GPEWORD:

**1.** Na pergunta **"Arquivo Word"** insira o arquivo novamente e dê um **tab** para que o sistema valide o arquivo.  
Lembrando que nessa pergunta deve ser inserido o arquivo modelo/word contendo as variáveis do gpeword e o arquivo deve possuir extensão **.dot** ou**.dotx**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40095339169175)  
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40095339170199)

**2.** Na pergunta **"Arquivo Saida"** **não** deve ser selecionado o arquivo modelo/word (extensão .dot/.dotx) novamente. Deve ser selecionado apenas o local onde o documento gerado será salvo, **atribuindo um nome ao documento com .doc.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40095339170839)

**3.** Se o problema persistir, sugerimos realizar a limpeza do profile de usuário e após a limpeza, **preencher todos os parâmetros** da rotina novamente, mesmo que tenham algum conteúdo.   
[Framework - Linha Protheus - Manutenção de Profile de Usuários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025097012-Framework-Linha-Protheus-Manuten%C3%A7%C3%A3o-de-Profile-de-Usu%C3%A1rios)

4. Confira também se o grupo de perguntas está conforme o padrão:  
**Módulo Configurador (SIGACFG)/ Base de Dados/ Dicionário/ Base de Dados/ Perguntas**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40835167930391)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40835184538135)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40835184538775)

**Saiba Mais**  
[RH - Linha Protheus - GPE - Rdmake GPEWORD para customização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/39956154957847-RH-Linha-Protheus-GPE-Rdmake-GPEWORD-para-customiza%C3%A7%C3%A3o)  
[RH - Linha Protheus - GPE - Configuração para Impressão de Documentos no Word (GPEWORD)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021565472-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-para-Impress%C3%A3o-de-Documentos-no-Word-GPEWORD)  
[RH - Linha Protheus - GPE - GPEWORD apresenta mensagem: HELP NO\_IX - Funçao de usuario nao esta compilada no repositorio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18328524772375-RH-Linha-Protheus-GPE-GPEWORD-apresenta-mensagem-HELP-NO-IX-Fun%C3%A7ao-de-usuario-nao-esta-compilada-no-repositorio)
