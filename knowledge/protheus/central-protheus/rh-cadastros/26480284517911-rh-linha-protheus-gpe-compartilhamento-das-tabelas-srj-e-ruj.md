---
article_id: 26480284517911
category: RH - Cadastros
content_hash: a9e9e03b431104b20cef0a1895af8f4ab7246defa499b03b7e709ee98eaa3ec4
fetched_at: '2026-06-28T22:43:25.899083+00:00'
product: protheus
section_id: 360010781894
source: central-protheus
title: RH - Linha Protheus - GPE - Compartilhamento das tabelas SRJ e RUJ
type: support-article
updated_at: '2026-06-24T19:57:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26480284517911-RH-Linha-Protheus-GPE-Compartilhamento-das-tabelas-SRJ-e-RUJ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26480301177239) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao acessar o **Cadastro de Funções,** é apresentada a mensagem: **O compartilhamento das tabelas SRJ e RUJ estão diferentes. Altere o compartilhamento da tabela RUJ para que fique igual ao da SRJ.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26480284492055)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da release 12.1.2310  
  
**Causa**O compartilhamento das tabelas **SRJ** e **RUJ** **estão diferentes,** mas **obrigatoriamente** precisam ser **iguais.**  
  
**Solução**Para ajustar o compartilhamento das tabelas acesse o ambiente **Configurador (SIGACFG)** com senha de administrador e selecione no menu **Base de Dados/ Dicionário/ Base de Dados.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30255262819479)  
  
Na lateral esquerda, expanda as opções clicando em seta para baixo, e selecione a opção Dicionário de Dados.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30255294359959)  
  
No ícone da **Lupa,** busque pela tabela **SRJ** e **RUJ,**e clique em Editar (ícone com folha de papel e lápis).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30255262822295)

O compartilhamento das duas devem ser **iguais,** conforme exemplo abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30255262823191)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30255262824471)  
  
Depois de ajustar o compartilhamento, clique no ícone **Confirmar** em verde.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30255294369047)  
  
E para finalizar a alteração, clique em **Atualizar** dicionário de dados.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30255262827287)  
  
O Sistema apresentará uma tela de confirmação com as **alterações realizadas.** Clique em **seguir** até que o processo seja **finalizado** com sucesso.

**Importante:** As configurações podem variar de acordo com a gestão corporativa de cada empresa, então o exemplo acima de compartilhamento não é uma regra.  
Para que o Sistema permita concluir a alteração é necessário que seja feito em modo exclusivo (sem nenhum usuário logado no Sistema).

**Saiba Mais:**[Cálculo de Adicionais por Função](https://tdn.totvs.com/pages/viewpage.action?pageId=799276835)  
[RH - Linha Protheus - GPE - Cadastro de Função](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050007454-RH-Linha-Protheus-GPE-Cadastro-de-fun%C3%A7%C3%A3o)
