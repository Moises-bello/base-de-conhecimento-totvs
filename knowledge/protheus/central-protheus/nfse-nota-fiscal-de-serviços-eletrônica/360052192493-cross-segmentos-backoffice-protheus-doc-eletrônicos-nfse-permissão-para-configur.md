---
article_id: 360052192493
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: e74540b134a3c4dbaf984dc8944d41960b9e2c891801d06a26bc698e2c82c035
fetched_at: '2026-06-28T22:39:57.623137+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Permissão
  para Configuração do Certificado Digital (FISA022)
type: support-article
updated_at: '2021-11-23T18:23:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052192493-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Permiss%C3%A3o-para-Configura%C3%A7%C3%A3o-do-Certificado-Digital-FISA022
---

**Dúvida**Como limitar o acesso do Wizard.config da rotina **FISA022** por **TIPO**de usuário?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.

**Solução**A rotina FISA022 teve a recente inclusão do parâmetro MV\_ADMNFSE, **onde somente os usuários do Grupo de Administradores poderão ter acesso completo ao Wizard.cfg.**  
Nele é definido níveis de permissão para o acesso às configurações do Wizard.cfg e/ou Configuração do Certificado Digital.  
  
Detalhes do parâmetro:  
  
**Nome da Variável:**MV\_ADMNFSE  
  
**Tipo:** Lógico  
 **Descrição:** Habilita a opção de usuários não-Administradores configurarem o Wizard de Configuração para NFS-e.  
 **Conteúdo:** **.T.** = Apenas usuários do grupo de Administradores podem acessar o Wizard.cfg;  
ou  
**.F.** = Usuários não-Administradores podem acessar o Wizard de Configuração; **Conteúdo Padrão:** .F.  
  
Exemplos:

Se o usuário não-Administrador não possuir permissão para acessar o Wizard de Configuração, uma mensagem será exibida indicando o acesso negado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413951642647/mceclip0.png)  
  
Se o usuário não-Administrador possuir permissão para acessar o Wizard de Configuração, o mesmo poderá alterar todas as configurações dentro da Rotina

Observação  
**\***Esse ajuste está disponível no fonte FISA022 igual ou superior a data de **23 de Novembro de 2021**.
