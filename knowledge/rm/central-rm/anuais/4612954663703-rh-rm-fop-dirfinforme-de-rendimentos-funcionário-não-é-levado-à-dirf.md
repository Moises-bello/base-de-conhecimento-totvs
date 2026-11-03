---
article_id: 4612954663703
category: Anuais
content_hash: 2b63e88dad163ec692efbb09dbcfc51afc89814ede2862c148ca29bb692d0224
fetched_at: '2026-06-28T22:46:51.084544+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP - DIRF/Informe de Rendimentos: Funcionário não é levado à DIRF'
type: support-article
updated_at: '2025-01-07T18:17:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4612954663703-RH-RM-FOP-DIRF-Informe-de-Rendimentos-Funcion%C3%A1rio-n%C3%A3o-%C3%A9-levado-%C3%A0-DIRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21491942318231) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Por que o funcionário não é levado no arquivo da DIRF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Existem alguns motivos que podem fazer o funcionário não ser levado no arquivo da DIRF. Abaixo, seguem algumas situações para conferir:  
  
**Seleção de Funcionários:**Na rotina da DIRF/Informe de Rendimentos, tanto na primeira tela da rotina quanto nos parâmetros específicos da coligada, a seleção de funcionários deve atender à Situação, Tipo e Recebimento dos funcionários que devem ser levados à DIRF:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4612422530199)  
  
**Filtro de Seleção:**Nos parâmetros específicos da coligada, também na rotina da DIRF/Informe de Rendimentos, além da seleção de funcionários conforme citado no item acima, pode haver a aplicação de um Filtro de Seleção. Verifique se não é o caso de o filtro estar inibindo o funcionário identificado a ser levado para a DIRF:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4612469051543)**Não haver incidência em IR:**Caso os eventos que fazem o pagamento ao funcionário não tenham incidência em IR/Informe de Rendimentos:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4612799585303)  
  
**Autônomo/Diretor com vínculo incorreto:**Será validado o código de categoria eSocial . Segue abaixo informações da nova regra para o DIRF 2024 - Ano base 2023.

**Regra Atual**

**Código de receita 0588:** quando a categoria do eSocial for igual a: 201, 202, 701, 711, 712, 731, 734, 738, 741, 751, 771 ou 781.

**Código de Receita 3533:** Quando tiver marcado o campo **DIRF - Informar remuneração no Cód. da Receita 3533** (pfunc.CODIGORECEITA3533). 

**Código de Receita 3562:** Código criado para declaração dos rendimentos referente a PLR (Participação nos Lucros ou Resultados). 

**Código de Receita:1889:** Código criado para declaração dos Rendimentos Recebidos Acumuladamente. 

**Código de Receita 0561:** Quando não atender as categorias do eSocial do código de receita 0588 e nem os critérios dos códigos de receita **3533, 3562 e 1889**

**Saiba mais**  
Se por algum motivo o funcionário identificado ainda não for levado à DIRF, considere consultar nossa documentação de Perguntas e Respostas:  
[RH - RM - FOP - DIRF/Informe de Rendimentos: Perguntas e Respostas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415220890903-RH-RM-FOP-DIRF-Informe-de-Rendimentos-Perguntas-e-Respostas-2022)
