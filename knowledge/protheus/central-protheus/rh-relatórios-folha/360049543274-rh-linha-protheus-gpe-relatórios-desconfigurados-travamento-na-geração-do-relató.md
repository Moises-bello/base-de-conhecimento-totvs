---
article_id: 360049543274
category: RH - Relatórios Folha
content_hash: 7fc1a5f5df84ec82d7d15fa157a8ac86b6ca3c80c3eb29eb33aabb066b337899
fetched_at: '2026-06-28T22:43:17.608292+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Relatórios desconfigurados, travamento na geração
  do relatório ou impressão sem apresentar o relatório em tela para filtro de impressões
type: support-article
updated_at: '2024-08-23T01:21:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049543274-RH-Linha-Protheus-GPE-Relat%C3%B3rios-desconfigurados-travamento-na-gera%C3%A7%C3%A3o-do-relat%C3%B3rio-ou-impress%C3%A3o-sem-apresentar-o-relat%C3%B3rio-em-tela-para-filtro-de-impress%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25842015752343) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Relatórios GPE desconfigurados, travamento na geração do relatório ou impressão sem apresentar o relatório em tela para filtro de impressões.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
**1.** Atualize o  SmartClient;

**2.** Atualize o Appserver;

**3.** Caso apresente uma mensagem de diretório incorreto ou erro na gravação local/servidor, acesse o Configurador (Cadastro de usuário / Restrição de acesso/ Acessos e verifique os acessos **111, 112, 121 e 122.****Obs:** Deve-se conceder o acesso conforme a necessidade do usuário.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074451354)  
  
Também no perfil do usuário acesse parametrização e verifique se o caminho do diretório de impressão esta configurado corretamente:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075652073)

4. Para  geração de relatórios não personalizáveis que são impressos diretamente sem apresentar a tela de visualização do relatório ou com as mesmas informações de um relatório gerado anteriormente:   
**Faça um backup da pasta por questão de segurança e em seguida delete os arquivos temporário da estação do usuário.** Na primeira impressão após deletar os arquivos, **solicite ao usuário selecionar as opções corretas de impressão** e verifique se o problema persiste.

**Saber mais:**

[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)
