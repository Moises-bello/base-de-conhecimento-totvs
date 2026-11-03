---
article_id: 360035158373
category: Configurador
content_hash: f7d2d8812532653ada83e484bda58694a21375a7fe2a8c9dd475d369af46b712
fetched_at: '2026-06-28T22:42:19.059804+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Fórmulas - Segurança no Cadastro
type: support-article
updated_at: '2024-05-08T11:50:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035158373-Framework-Linha-Protheus-F%C3%B3rmulas-Seguran%C3%A7a-no-Cadastro
---

**Dúvida**Qual a regra na criação de fórmulas?  
   
 **Ambiente**Protheus - Configurador - A partir da versão 11  
  
**Solução**O **Cadastro de Fórmulas** que existe no menu das rotinas permite que sejam cadastradas algumas fórmulas que podem ser chamadas posteriormente via customização. Algumas fórmulas, como Strings com parenteses, cálculos matemáticos, chamadas de variáveis, tem sua execução liberada no cadastro de Fórmulas. Contudo, por uma questão de segurança, a chamada de Funções compiladas no RPO somente podem ser cadastradas com a autorização do usuário Administrador do Protheus.  
  
Ao tentar criar uma fórmula com uma chamada de Função, se estiver logado com o usuário Administrador, será exibida uma mensagem informando que a **expressão já se enquadra nos requisitos de segurança**, pedindo apenas para autorizar a expressão (clicando em Sim).  
  
![image2019-6-19_14-30-36.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045020914)  
  
Porém, ao tentar criar uma fórmula com uma chamada de **Função**, estando logado com um usuário comum (não Administrador), será exibida uma mensagem de **Solicitação de acesso de Administrador**, onde haverá um campo de usuário e senha, que deve ser preenchido pelo Administrador para **liberar** a criação da fórmula.  
  
![Im2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045021074)
