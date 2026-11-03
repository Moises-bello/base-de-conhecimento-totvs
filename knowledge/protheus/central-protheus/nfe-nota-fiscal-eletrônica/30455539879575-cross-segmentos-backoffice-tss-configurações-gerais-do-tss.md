---
article_id: 30455539879575
category: NFe - Nota Fiscal Eletrônica
content_hash: 79a922b4695d07b1dc5295b7d5abb150519d49eefb7d9837e36a008e261ff242
fetched_at: '2026-06-28T22:40:07.226897+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice TSS -Configurações Gerais do TSS.
type: support-article
updated_at: '2025-03-17T12:14:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30455539879575-Cross-Segmentos-Backoffice-TSS-Configura%C3%A7%C3%B5es-Gerais-do-TSS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30455563929239) Tempo aproximado para leitura: 00**:03:00min****Dúvida**Como configurar gerar o Client Id e Client Secret

Como adequar o usuário ou grupo de usuários para atender a Lei Geral de Proteção de Dados?

**Ambiente**

Cross Segmentos - TSS - a partir da versão 12

**Solução**

As credenciais basicamente são Client Id e Client Secret, que poderão ser informados nos campos Client Id e Cli. Secret, respectivamente, na aba Credencial TSS.

Dependendo da gestão das credenciais do TSS, poderá ser cadastrado uma credencial para uma unidade/filial ou para N unidade/filial.

Abaixo iremos demonstrar como é realizado a configuração de uma credencial para duas unidades/filiais.

Passo a Passo:

1 - Acessar smartclient do TSS e na tela inicial escolher ou digitar TSS MONITOR:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30455539858839)

Nos campos usuários e senha deve ser informado:

Usuário: ADMIN  
Senha: ADMIN  
  
Caso a senha padrão tenha sido alterada é necessário verificar com o administrador do sistema.

2 - Ao acessar o ambiente, selecionar Configuração>Credenciais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30455563931927)

3 - Após confirmar, a próxima tela será apresentada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30455563932439)

Marcar o registro e clicar na opção "Gerar Secret", na próxima tela será apresentado o Client Id e Client Secret, que deverão ser informados na rotina do ERP
