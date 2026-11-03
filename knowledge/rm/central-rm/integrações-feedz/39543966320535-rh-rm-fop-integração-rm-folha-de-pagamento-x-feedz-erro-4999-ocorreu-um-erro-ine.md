---
article_id: 39543966320535
category: Integrações - Feedz
content_hash: ec66e22845a347bea6a184910e07a3a879d377d08d017fd474393d59849a3c7c
fetched_at: '2026-06-28T22:46:41.408747+00:00'
product: rm
section_id: 28212337440791
source: central-rm
title: 'RH - RM - FOP - Integração RM Folha de Pagamento x Feedz - Erro 4999: Ocorreu
  um erro inesperado! > Já existe um registro com este nome.'
type: support-article
updated_at: '2026-04-07T16:18:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39543966320535-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Erro-4999-Ocorreu-um-erro-inesperado-J%C3%A1-existe-um-registro-com-este-nome
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39543966310807) Tempo aproximado para leitura: **00:01:15 min**  
  
**Dúvida**  
Ao realizar o envio de colaboradores do RM para a Feedz, é apresentado a mensagem de erro:  *"Erro na integração com a Feedz código 4999: Ocorreu um erro inesperado! > Já existe um registro com este nome."*  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir da versão 12.1.2310  
  
**Solução**  
Este erro ocorre, quando existem registros como Filiais, Cargos ou departamento que possuem a mesma descrição no nome. Para correção, acesse o módulo **Folha de pagamento | Configurações | Parametrizador | 06.02 - Integrações | 06.02.10 - TOTVS RH | Avaliação e Desempenho.** Selecione a opção **Feedz** e marque os seguintes parâmetros de concatenação:

* Concatenar Descrição do Cargo (Descrição + Código)
* Concatenar Descrição do Departamento (Descrição + Código)
* Concatenar Descrição da Unidade (Descrição + Código
* Concatenar o Código da Coligada no Cargo / Departamento / Unidade / Matrícula

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39543954492439)

Para informações detalhadas sobre os parâmetros, consulte nossa documentação técnica: [Integração RM X Feedz](https://tdn.totvs.com.br/pages/releaseview.action?pageId=785614408#1-1)

**Saiba mais:**

[**RH - RM - FOP - Integração RM Folha de Pagamento x Feedz - Como realizar o envio de colaboradores e associação de líderes**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29903246172695-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Como-realizar-o-envio-de-colaboradores-e-associa%C3%A7%C3%A3o-de-l%C3%ADderes)

[**RH - RM - FOP - Integração RM Folha de Pagamento x Feedz - Erro na integração com a Feedz código XXXX**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29909362246039-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Erro-na-integra%C3%A7%C3%A3o-com-a-Feedz-c%C3%B3digo-XXXX)
