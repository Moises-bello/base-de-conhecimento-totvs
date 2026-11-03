---
article_id: 12043265811351
category: MDT - Atendimento Médico
content_hash: 35b76a3feb75eee765d6bd861c31e1a5237ba07585be954c01c5341484176918
fetched_at: '2026-06-28T22:44:20.642690+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Como gerar um ASO admissional
type: support-article
updated_at: '2025-09-02T17:45:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12043265811351-RH-Linha-Protheus-MDT-Como-gerar-um-ASO-admissional
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25318812382871) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como gerar um ASO admissional?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Muitas empresas realizam o ASO Admissional para o candidato antes da criação da matrícula. Nessa etapa, é necessário apenas ter uma ficha médica do candidato, que, após avaliação do médico, poderá ser admitido.

Para mais detalhes, consulte o artigo com orientações sobre: [Como gerar o evento S-2220 para candidatos que foram admitidos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412561484055) 

Outra opção é efetuar a admissão do funcionário pelo módulo **SIGAGPE**, que cria automaticamente a ficha médica, conforme explicado no artigo: [Inclusão automática de ficha médica ao realizar admissão do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028379252)  
  
Deve-se verificar se o exame está configurado para ser gerado na admissão. Por exemplo, acesse a rotina **Atualizações > PCMSO > Exames (MDTA020)** e confira se o campo **Admissional** está marcado como **Sim**.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12043553689111)

No cadastro de exames do funcionário, na rotina **Atualizações > PCMSO > Exames do Func. (MDTA120)**, o exame NR7 é um exemplo.

Nesse cadastro, devem estar preenchidos os seguintes campos:

* **Origem**: tipo **Ocupacional**
* **Num. PCMSO**
* **Data Resultado**
* **Natureza**: tipo **Admissional**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12043657201303)

Após realizar os cadastros, deve-se incluir o Atestado ASO. Para isso, acesse a rotina **Atualizações > Atendimento Médico > Atestado ASO (MDTA200)**, clique em **Incluir** e preencha os campos destacados.

O campo **Natureza** deve ser compatível com a natureza informada no exame do funcionário. Também é obrigatório informar o **Médico Responsável**, a **Ficha Médica** e o **Parecer Médico**.

Na parte inferior da tela, há o campo **Exame**, onde será exibido o exame NR7 que possui a mesma natureza do ASO.![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12044175371799)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12044277373975)  
  
Após validar o preenchimento dos campos, deverá salvar o registro e seguir com a Impressão para envio ao TAF, conforme documentação: [Como gerar o ASO para o eSocial evento S-2220 no SIGAMDT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414503676567)

**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
