---
article_id: 13337933005591
category: RH - Funcionários
content_hash: c73e6171213974b5733445fc95903b8ccc5cef4f47749517235656e336bf9899
fetched_at: '2026-06-28T22:43:27.555584+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Como criar o filtro para Controle de Acesso de
  Usuários para impressão da ficha de registro
type: support-article
updated_at: '2025-09-12T19:19:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13337933005591-RH-Linha-Protheus-GPE-Como-criar-o-filtro-para-Controle-de-Acesso-de-Usu%C3%A1rios-para-impress%C3%A3o-da-ficha-de-registro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32644511560727) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como criar o filtro para Controle de Acesso de Usuários para impressão da ficha de registro?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - Todas as versões  
  
**Solução**Para criar uma restrição para impressão da ficha de registro, seja por usuário ou por grupo de usuários, pode ser usada a rotina **Controle de Acesso de usuário**, realize os seguintes passos descritos abaixo:  
  
**1.** Acesse a rotina **Controle de Acesso de Usuário** pelo caminho >**Atualizações > Cadastros > Controle de Acesso de Usuário** e clique em **Incluir.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13343444794391)

**2.** **Preencha** os campos **conforme a definição de restrição desejada:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13344611601687)

Campos para preenchimento:

**Grupo Usuari (RW\_GRUPO)**= Grupo que deseja fazer a restrição  
**Id Usuário (RW\_IDUSER)** = Id do usuário, o código do usuário que deseja fazer a restição  
**Arquivo (RW\_ALIAS)** = Tabela que deseja realizar o filtro  
**Processo (RW\_PROCESS)** = Nome do processo para o filtro  
**Descrição (RW\_DESCRI)** = Nome do processo que será utilizado o filtro  
**Filtro Brows (RW\_FILBROW)** = Filtre a expressão desejada para delimitar o acesso que será apresentado ao acessar a rotina  
**Filtro Relat (RW\_FILREL)** = Filtre a expressão desejada para delimitar na impressão do relatório **Validação (RW\_VALID)** = Preencha com a expressão utilizada nos filtros anteriores para validação

Nesse exemplo foi realizado 2 configurações para a usuária:

Processo **GPEA260** referente a rotina **Ficha de Registro**, permitindo acesso somente nos centros de custos 001 e 002

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13343972744343)

Processo **GPER460** referente a **Impressão da Ficha de Registro** permitindo impressão somente nos centro de custos 001 e 002

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13343972022551)

**3.** Após realizar as definições dos filtros na rotina Controle de Acesso Usuários. O usuário terá acesso no Browser conforme os filtros definidos, e ao realizar o processo de impressão da ficha, o sistema fará somente dos funcionários que estão cadastrados conforme a definição do filtro. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13344072326935)

**Observação:** Mesmo definindo o filtro no Controle de Acesso Usuário, ao realizar o preenchimento dos parâmetros para impressão do relatório, será apresentado todos os centros de custos cadastrados no sistema, pois esse campo é abastecido pela tabela CTT.   
A tabela CTT é de domínio da controladoria, sendo assim a rotina de Controle de Acessos não tem controle sobre esta tabela. Mas o relatório não será impresso mesmo se selecionado outro centro de custos que não esteja no filtro.  

[Controle de acessos do usuário (GPEA270 - SIGAGPE - V12)](https://tdn.totvs.com/pages/viewpage.action?pageId=435115342)

[Filtro do Relatório (GPEA270 - SIGAGPE - V12)](https://tdn.totvs.com/pages/viewpage.action?pageId=435115374)

[Filtro Browse (GPEA270 - SIGAGPE - V12)](https://tdn.totvs.com/pages/viewpage.action?pageId=435115372)

**Saiba Mais**[RH - Linha Protheus - GPE - Como bloquear uma rotina do SIGAGPE via configurador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11227180231191-RH-Linha-Protheus-GPE-Como-bloquear-uma-rotina-do-SIGAGPE-via-configurador?source=search)  
[RH - Linha Protheus - GPE - Restringir acesso de usuário a determinada rotina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059006033-RH-Linha-Protheus-GPE-Restringir-acesso-de-usu%C3%A1rio-a-determinada-rotina?source=search)  
[RH - Linha Protheus - GPE - Como restringir o acesso do usuário à alteração de campo específico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052716514-RH-Linha-Protheus-GPE-Como-restringir-o-acesso-do-usu%C3%A1rio-%C3%A0-altera%C3%A7%C3%A3o-de-campo-espec%C3%ADfico?source=search)  
[RH - Linha Protheus - GPE - Como permitir que um usuário tenha acesso apenas a Funcionários Demitidos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057151373-RH-Linha-Protheus-GPE-Como-permitir-que-um-usu%C3%A1rio-tenha-acesso-apenas-a-Funcion%C3%A1rios-Demitidos?source=search)
