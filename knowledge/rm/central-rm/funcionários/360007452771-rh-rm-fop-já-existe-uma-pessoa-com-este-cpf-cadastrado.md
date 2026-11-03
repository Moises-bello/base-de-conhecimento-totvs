---
article_id: 360007452771
category: Funcionários
content_hash: c2e398fc105c6acb6c95c4d9efe0bd9602a4a14c86777d4ccfa99638d71c4617
fetched_at: '2026-06-28T22:47:04.244466+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: RH - RM - FOP - Já existe uma pessoa com este CPF cadastrado
type: support-article
updated_at: '2025-01-16T19:46:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007452771-RH-RM-FOP-J%C3%A1-existe-uma-pessoa-com-este-CPF-cadastrado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:50 min  
  
Ocorrência**No cadastro de funcionários o sistema retorna o erro: **Já existe na base uma ou mais pessoas com este CPF Cadastrado. Favor confirmar se não se trata da mesma pessoa. Caso seja a mesma pessoa, verifique a possibilidade de usar os dados desta pessoa**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**O erro acima ocorre ao efetuar um novo cadastro de funcionário que possua o mesmo CPF de uma pessoa cadastrada na tabela PPESSOA. Pode acontecer, por exemplo, ao admitir um funcionário que esteja sendo recontratado ou ao admitir uma segunda chapa para uma mesma pessoa.  
  
**Solução**Para solucionar esta situação será necessário utilizar a ferramenta **Localizar pessoa** ao realizar o cadastro deste funcionário.  
  
1. Ao efetuar o cadastro de um novo funcionário, acesse **Identificação | Localizar pessoa / Registro Preliminar**:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029566432/mceclip0.png)  
  
2. Digite o CPF ou o nome do funcionário que estiver cadastrando e em seguida **Localizar**. Selecione o funcionário e clique em OK.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029567572/mceclip1.png)  
  
**Importante**  
Ao efetuar os passos acima, alguns dados do funcionário já serão preenchidos automaticamente e o erro não será apresentado ao salvar o novo cadastro.  
  
**Importante**Se existir duas ou mais pessoas com este CPF, será necessário unificar as pessoas.  
Para unificar estas pessoas, siga os passos:  
1. Acesse o menu **Executar**;  
2. Localize e execute a rotina **Pessoas**;  
3. Localize por um dado em comum, por exemplo: nome, data de nascimento;  
4. Selecione as pessoas que possuem essas informações em comum;  
5. Vá em **Processos | Unificar pessoas**.  
  
Para mais informações sobre a unificação de pessoas, veja o [Como realizar o processo de unificar pessoas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014630691-TOTVS-RH-Linha-RM-RHU-Como-realizar-o-processo-de-unificar-pessoas).
