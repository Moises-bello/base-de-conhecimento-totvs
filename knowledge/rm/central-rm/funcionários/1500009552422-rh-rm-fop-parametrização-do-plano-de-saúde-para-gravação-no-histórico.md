---
article_id: 1500009552422
category: Funcionários
content_hash: bd70cafc65da6943f9753991c231df446a69aa4f595ba0f185ebfaf874ee8c2c
fetched_at: '2026-06-28T22:47:03.396315+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: RH - RM - FOP -  Parametrização do Plano de Saúde para gravação no histórico
type: support-article
updated_at: '2024-10-11T19:57:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009552422-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-do-Plano-de-Sa%C3%BAde-para-grava%C3%A7%C3%A3o-no-hist%C3%B3rico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:03:50 min  
  
Dúvida**Como cadastrar para importação automática o desconto de Plano de Saúde para o Histórico de Assistência a Saúde.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**1. Foi criada uma nova sub-aba chamada**Histórico Assistência Saúde**, cuja tabela do Banco de Dados é **PFHSTASSMED**. Identifique-a em Administração de Pessoal | Funcionários | Anexo | Históricos | Histórico Assistência Saúde:  
  
*![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014964861/mceclip0.png)*

![](https://tdn.totvs.com/download/attachments/210052115/image2017-7-6%209%3A51%3A0.png?version=1&modificationDate=1499345461000&api=v2)  
  
2. Para que o histórico seja alimentado de forma automática a cada lançamento da folha de pagamento, localize o evento de desconto de assistência médica/odontológica que poderá ou não utilizar o Código de Cálculo 14, e identifique qual a fórmula de valor vinculada a ele:  
  
![](https://tdn.totvs.com/download/attachments/210052115/image2017-7-6%2010%3A5%3A28.png?version=1&modificationDate=1499346329000&api=v2)  
  
3. Será necessário utilizar a variável **SALVAVALDEP** na estrutura da fórmula, de forma que sempre validará quando houver o retorno do valor por beneficiário.

**Exemplo da fórmula para o cálculo realizar preenchimento automático no Histórico de Assistência à Saúde:**

DECL DEP,SOMADEP,SOMAFUN;

SETVAR(DEP,1);

SETVAR(SOMADEP,0);

REPITA

SE TABDEP ('INCASSISTMEDICA' ,'V', DEP)=1 ENTAO

SE NDEPIDADE (DEP,HOJE)<=18

ENTAO SALVAVALDEP(DEP,80);

SETVAR(SOMADEP,SOMADEP+80)

SENAO

SE NDEPIDADE (DEP,HOJE)<=23

ENTAO SALVAVALDEP(DEP,120);

SETVAR(SOMADEP,SOMADEP+120)

SENAO

SALVAVALDEP(DEP,200);  
SETVAR(SOMADEP,SOMADEP+200)

FIMSE FIMSE FIMSE;

SETVAR(DEP,DEP+1) ATE DEP=10;

SE TABCOMPL('ASSISTENCIAMEDICA','S')='S'

ENTAO SE IDADE(HOJE)<=18

ENTAO SALVAVALDEP(0,80);

SETVAR(SOMAFUN,SOMAFUN+120)

SENAO SE IDADE(HOJE)<=23

ENTAO SALVAVALDEP(0,120);

SETVAR(SOMAFUN,SOMAFUN+189)

SENAO

SALVAVALDEP(0,111);

SETVAR(SOMAFUN,SOMAFUN+111)

FIMSE

FIMSE

FIMSE;

SOMADEP+SOMAFUN

Sempre que na fórmula existir a variável **SALVAVALDEP( , )**o sistema irá alimentar automaticamente a tabela **PFHSTASSMED** gravando o lançamento no Histórico de Assistência à Saúde, caso contrário a mesma deverá ser alimentada pelo usuário.

**A variável SALVAVALDEP não altera valores no cálculo, apenas realiza a gravação das informações no cadastro.**

Lembrando que, quando o beneficiário for o funcionário, o número do beneficiário deverá ser 0(zero).  
  
![](https://tdn.totvs.com/download/attachments/210052115/image2017-7-6%2010%3A9%3A35.png?version=1&modificationDate=1499346576000&api=v2)

**Importante**  
Ao realizar as parametrizações para o desconto do evento de assistência saúde com o Código de Cálculo 14 juntamente com uma fórmula com a função SALVAVALDEP o sistema alimenta corretamente o histórico de assistência saúde e envelope, mas se porventura ocorrer a retirada da marcação de incidência em "assistência médica" de algum dependente, após o lançamento dos eventos no envelope e for realizado o recálculo do envelope o sistema calcula o envelope corretamente com o novo valor do evento de Código de Cálculo 14 mas não altera o histórico sendo necessária intervenção manual para ajustes.  
  
**Saiba mais:**[Histórico de Assistência à Saúde](https://tdn.totvs.com/pages/releaseview.action?pageId=210052115)  
[Atualização do Histórico de Assistência Médica no recálculo da função de fórmula SALVAVALDEP](https://tdn.totvs.com/pages/releaseview.action?pageId=742220869)
