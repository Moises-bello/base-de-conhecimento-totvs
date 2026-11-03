---
article_id: 23529495758871
category: Treinamento (SIGATRM)
content_hash: 17f000a061de6d3be5a3cdb379e1233a80749dd131a88d7abd4bd6b729b06358
fetched_at: '2026-06-28T22:43:02.516618+00:00'
product: protheus
section_id: 206971527
source: central-protheus
title: RH - Linha Protheus - TRM - Ao clicar na rotina de Relatórios Personalizáveis,
  por que o usuário logado no Protheus não possui acesso
type: support-article
updated_at: '2024-05-16T18:18:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23529495758871-RH-Linha-Protheus-TRM-Ao-clicar-na-rotina-de-Relat%C3%B3rios-Personaliz%C3%A1veis-por-que-o-usu%C3%A1rio-logado-no-Protheus-n%C3%A3o-possui-acesso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23529495726359) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Ao clicar na rotina de Relatórios Personalizáveis, por que o usuário logado no Protheus não possui acesso  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - SIGATRM - Todas as versões  
  
**Solução**No módulo **26 do Protheus - SIGATRM**, há uma rotina no menu de Relatórios que permite, a criação de **relatórios personalizáveis via Protheus Report**.  
  
O caminho fica em **Miscelânea > Relatório TOTVS**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23529534665751)  
  
Se ao clicar na rotina, vier com este alerta abaixo, **o acesso será negado:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23529534668183)  
  
Par correção, **acessar o módulo SIGACFG > Configurador e, na rotina Usuários > Senhas > Usuários**, alterar o login deste funcionário logado no Protheus.  
  
Clicar na aba **Restrições de Acesso** e depois em **Acessos**, localizando a **permissão 152 e habilita-la**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23529534673303)  
  
Assim, reinicie o serviço do *Appserver* e o usuário que irá logar novamente, **terá acesso à esta rotina do módulo SIGATRM**, **ou em qualquer outro módulo do Protheus.**  
  
Importante frisar que, se este usuário do Configurador, **pertencer a um Grupo de Acesso**, a permissão também **precisará também ser alterada na rotina de Grupos**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23529534676759)  
  
**Saiba Mais**  
Consulte as *FAQs* sobre Treinamento no *link* abaixo:  
[Artigos RH - Treinamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971527-RH-Treinamento)
