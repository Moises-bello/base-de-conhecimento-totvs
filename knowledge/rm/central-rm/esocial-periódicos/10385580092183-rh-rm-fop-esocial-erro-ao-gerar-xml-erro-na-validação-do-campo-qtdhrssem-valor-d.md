---
article_id: 10385580092183
category: esocial - Periódicos
content_hash: b615de36ab815017f5a205522b59c296fc650544868f841918b74c7c6bb04131
fetched_at: '2026-06-28T22:47:09.320854+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar XML: Erro na validação do campo ''qtdHrsSem'':
  Valor deve ser maior que zero'
type: support-article
updated_at: '2024-06-14T11:47:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10385580092183-RH-RM-FOP-eSocial-Erro-ao-gerar-XML-Erro-na-valida%C3%A7%C3%A3o-do-campo-qtdHrsSem-Valor-deve-ser-maior-que-zero
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24166767059863)Tempo aproximado para leitura:**00:01:00 min****Ocorrência**  
Ao realizar a geração do XML dos eventos **S-2200**, **S-2206** é apresentado a seguinte mensagem de erro **Erro na validação do campo 'qtdHrsSem': Valor deve ser maior que zero.  
  
Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**O erro ocorre geralmente quando o campo **Número de Horas** no cadastro do funcionário pode estar zerado ou o **Tipo de Jornada e-Social** não está condizente com o horário cadastrado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10385010977431)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10385062814103)

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesso o cadastro do funcionário **Administração de Pessoal | Funcionário;**1.1. Acesse a aba **Salário/Jornada** no cadastro do funcionário e edite o **Horário;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24166751266967)

1.2. Certifique que o campo **Número de Horas** do horário esteja preenchido. Caso não esteja, verifique na aba **Jornada** se existe jornada informadas para o horário em questão. Também valide na aba esocial o tipo de jornada eSocial;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24166767074839)

2. Ainda no cadastro do horário, verifique na aba **eSocial** o campo **Tipo de jornada e-Social**;  
2.1. Se tiver informado os tipos 3 ou 9, acesse o menu **Configurações | Parametrizador | eSocial | Configurações Gerais 3/7**;  
2.2. Caso o parâmetro **Considerar jornada mensal do funcionário para cálculo da média de horas da Jornada semanal****(Tipo da Jornada: 3 e 9)**esteja marcado, deve ser preenchido o campo **Divisor da Jornada Mensal** ou **Fórmula do Divisor da Jornada Mensal.**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24166751282199)

**Saiba mais**Para outras informações, acesse:[- O campo 'tpJornada' do registro 'horContratual' é obrigatório e não está preenchido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005166742-RH-RM-FOP-eSocial-Erro-O-campo-tpJornada-do-registro-horContratual-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido?source=search)
