---
article_id: 1500007991422
category: LOGIN
content_hash: 4017d2798f870f3bdcd0449e739d33111727fbc9090d346ef1da7ef8292ac2c7
fetched_at: '2026-06-28T22:44:40.569834+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - Para qual e-mail é enviado a redefinição de
  senha ao selecionar a opção "Esqueceu a senha" no MEU RH
type: support-article
updated_at: '2026-06-18T19:26:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007991422-RH-Linha-Protheus-MEU-RH-Para-qual-e-mail-%C3%A9-enviado-a-redefini%C3%A7%C3%A3o-de-senha-ao-selecionar-a-op%C3%A7%C3%A3o-Esqueceu-a-senha-no-MEU-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24769491138327) Tempo aproximado para leitura: 00:01:00 min****Dúvida**Para qual e-mail é enviado a redefinição de senha ao selecionar a opção "Esqueceu a senha" no MEU RH?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**1. No MEU RH quando é selecionado a opção "Esqueceu a Senha", será solicitado o Usuário, que no padrão é o CPF, e o E-mail que deve ser o mesmo cadastrado no Funcionário (SRA) e no Participante (RD0)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30630624934039)  
  
2. Após confirmar, será enviado o e-mail de redefinição de senha para o e-mail que esta configurado na RD0 campo RD0\_EMAIL, esse campo por padrão utiliza o DE/PARA do campo RA\_EMAIL.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011542562)  
  
3. O relacionamento dos campos da SRA e RD0 é realizado através do arquivo MSRELRDZ que se encontra na pasta system do Protheus, a tabela de relacionamento entre esses cadastros é a RDZ.  
  
[RH - Linha Protheus - APD - Como conferir relacionamento do funcionário com o participante](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024677334-RH-Linha-Protheus-APD-Como-conferir-relacionamento-do-funcion%C3%A1rio-com-o-participante?source=search)  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)  
[RH - Linha Protheus - MEU RH - Como configurar o Esqueceu a Senha do MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052543934-RH-Linha-Protheus-MEU-RH-Como-configurar-o-Esqueceu-a-Senha-do-MEU-RH?source=search)  
[RH - Linha Protheus - MEU RH - Envio do "esqueceu a senha" quando se utiliza SSL/certificado digital](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052412773-RH-Linha-Protheus-MEU-RH-Envio-do-esqueceu-a-senha-quando-se-utiliza-SSL-certificado-digital?source=search)
