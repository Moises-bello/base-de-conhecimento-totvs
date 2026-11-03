---
article_id: 11336908428695
category: esocial - Processos
content_hash: 1f8f33d3d834dac4a8ed9ecb2c85d157b855dcf187978b6cbfa7764a7fe663fe
fetched_at: '2026-06-28T22:47:08.356300+00:00'
product: rm
section_id: 1500000834441
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro na integração com o TAF: O valor ''xxxxx''
  informado na tag CPF somado ao valor ''xxxxx'' informado na tag Matricula é uma
  chave composta '
type: support-article
updated_at: '2024-06-27T18:02:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11336908428695-RH-RM-FOP-eSocial-Erro-na-integra%C3%A7%C3%A3o-com-o-TAF-O-valor-xxxxx-informado-na-tag-CPF-somado-ao-valor-xxxxx-informado-na-tag-Matricula-%C3%A9-uma-chave-composta
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao integrar eventos com o TAF, retorna a mensagem **O valor 'xxxxx' informado na tag CPF somado ao valor 'xxxxx' informado na tag Matricula é uma chave composta e a sua combinação não corresponde a nenhum registro do cadastro na base de dados.**   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas versões  
  
**Causa**O erro ocorre quando no cadastro do trabalhador consta a Matrícula eSocial preenchida no RM, porém o  evento S-2300 foi encaminhado para o eSocial no Leiaute 2.5 sem esse dado ou quando, para algumas Categorias não é obrigatório o envio do registro S-2300. Sendo assim, o evento em questão, deverá ser enviado ao eSocial sem Matricula também.  
  
**Solução**Para correção da ocorrência favor realizar as validações abaixo:  
1. Acesse o ambiente do Governo e certifique-se que S-2300 cadastramento inicial não possui **Matricula eSocial** ou não foi enviado;  
2. Caso o evento não exista ou não possua **Matricula eSocial**, deverá retira-la do cadastro de funcionário via banco de dados pelo o seu DBA. Para consultar, acesse **Administração de Pessoal | Funcionários** e consulte o campo Matricula eSocial;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11482484337047)

3. Após ajustes, poderá gerar o XML e envia-lo ao eSocial.
