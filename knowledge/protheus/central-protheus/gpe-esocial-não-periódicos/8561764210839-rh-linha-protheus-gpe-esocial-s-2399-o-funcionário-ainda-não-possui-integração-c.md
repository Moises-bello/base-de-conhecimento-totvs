---
article_id: 8561764210839
category: GPE - eSocial - Não Periódicos
content_hash: be1132da8828ea046e73bfa88bee9717d8b77e7cd15b79dcd3dacfe7a0bf32e1
fetched_at: '2026-06-28T22:45:05.949782+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2399 - O funcionário ainda não possui
  integração com o TAF. Realize a sua integração para poder gerar a rescisão. A rescisão
  não será efetivada
type: support-article
updated_at: '2026-06-16T12:51:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8561764210839-RH-Linha-Protheus-GPE-eSocial-S-2399-O-funcion%C3%A1rio-ainda-n%C3%A3o-possui-integra%C3%A7%C3%A3o-com-o-TAF-Realize-a-sua-integra%C3%A7%C3%A3o-para-poder-gerar-a-rescis%C3%A3o-A-rescis%C3%A3o-n%C3%A3o-ser%C3%A1-efetivada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18984054488471) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao calcular a rescisão, é apresentada mensagem para o estagiário: **O Funcionário ainda não possui integração com o TAF**. Realize a sua integração para poder gerar a rescisão. Como corrigir?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Eixstem casos para trabalhadores sem vinculo, onde foi preenchido o campo **RA\_DESCEP** indevidamente com conteúdo **1**, ou seja, quando este campo esta preenchido o sistema irá **validar** a **matricula** no campo **C9V\_MATTSV**, pois no leiaute S-1.0 é obrigatório a matricula.  
  
Caso seu campo **RA\_DESCEP esteja com conteúdo 1** e **C9V\_MATTSV vazio**, ou inverso, será necessário **aplicar o pacote** abaixo que foi disponibilizado para correção e **executar o rdmake ATUDESCEP** conforme artigo: [RH - Linha Protheus - GPE - eSocial - Funcionalidade do rdmake ATUDESCEP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8559365211543) para ajustar o RA\_DESCEP.  
  
O **inverso** **também** **deve** **ser** **corrigido**, onde há numero de matricula no campo C9V\_MATTSV porém o campo da SRA, RA\_DESCEP está com 0(zero) ou vazio.  
  
Para verificar a matricula (**C9V\_MATTSV**) do Trabalhador Sem Vinculo no módulo 84, acesse o menu: **Atualizações > Eventos eSocial > Trabalhador >** **Cadastro Trabalhador**:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8664720076311)  
  
Para verificar o campo **Contr. Mat. TSV** (RA\_DESCEP), acesse o módulo 07 em: **Atualizações > Funcionários > Funcionários**:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8664781140375)  
  
O rdmake **ATUDESCEP** está disponível no pacote de expedição continua, na pasta **rdmake**:   
[Atualizações de Arquivos fontes RH Expedição Continua](https://suporte.totvs.com/portal/p/10098/download?e=1070590#all/all/all/search/rh_expedicao_continua)  
  
O campo pode ter 3 formas de preenchimento, 0 indica que não matricula não compõe chave, 1 para compor e quando está em branco assume o valor 0 (zero).  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
