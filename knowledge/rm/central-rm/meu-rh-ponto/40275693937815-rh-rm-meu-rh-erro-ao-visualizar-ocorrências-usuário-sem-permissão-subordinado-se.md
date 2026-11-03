---
article_id: 40275693937815
category: Meu RH - Ponto
content_hash: d81f3c48cfc37720d79b914a061295aa968395db6aaaa9b3a09aaba638147e42
fetched_at: '2026-06-28T22:47:30.211779+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: 'RH - RM - Meu RH - Erro ao visualizar ocorrências: "Usuário sem permissão,
  subordinado sem grupo de quiosque ou subordinado que não utiliza banco de horas"'
type: support-article
updated_at: '2026-05-06T19:17:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40275693937815-RH-RM-Meu-RH-Erro-ao-visualizar-ocorr%C3%AAncias-Usu%C3%A1rio-sem-permiss%C3%A3o-subordinado-sem-grupo-de-quiosque-ou-subordinado-que-n%C3%A3o-utiliza-banco-de-horas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40275693921815) Tempo aproximado para leitura: **00:02:15 min**  
  
**Dúvida**  
Ao acessar a rotina Visualizar Ocorrências no Meu RH, após selecionar uma ocorrência e clicar em "Pagar/descontar", é exibida a mensagem de erro: *"Erro ao executar o processo. Possíveis causas: usuário sem permissão, subordinado sem grupo de quiosque ou subordinado que não utiliza banco de horas. Entre em contato com o administrador do sistema."*

*![](https://centraldeatendimento.totvs.com/hc/article_attachments/40275709145495)*  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir do release 12.1.2310  
  
**Solução**  
Este erro ocorre, porque a funcionalidade de Pagar/Descontar ocorrências no Meu RH é vinculada à utilização de Banco de Horas. Se o parâmetro de utilização não estiver ativo no sindicato do funcionário (subordinado), o sistema retorna esta mensagem de erro.

Para corrigir o comportamento, realize os seguintes passos:

1. Acesse no módulo de **Automação de Ponto,**o menu **Configurações | Parametrizador**. Ao abrir o assistente, clique em avançar e selecione o processo**08.02 - Sindicato** e edite o sindicato do funcionário. Avance até a etapa **Banco de Horas** e marque o campo "**Utiliza banco de horas**" e em "Tipo de banco de horas", selecione o tipo **Período** ou **Diário** conforme o desejado.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40281398803863)

   Para informações detalhadas sobre esta parametrização, consulte:  
   [RH - RM - PTO - Como configurar o banco de horas por período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017559512-RH-RM-PTO-Como-configurar-o-banco-de-horas-por-per%C3%ADodo)  
   [RH - RM - PTO - Como configurar o banco de Horas diário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045154114-RH-RM-PTO-Como-configurar-o-banco-de-Horas-di%C3%A1rio)
2. Acesse em **Automação de Ponto: Cadastros** > **Funcionários**, abra o cadastro do funcionário e no campo **Código do Grupo de Quiosque**, vincule um grupo caso ainda não esteja preenchido.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40275693923991)

Após realizar estas parametrizações, será possível utilizar está funcionalidade no Meu RH.

**Saiba Mais**

[**RH - RM - Meu RH - Como funciona Visualizar ocorrências**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403613012375-RH-RM-Meu-RH-Como-funciona-Visualizar-ocorr%C3%AAncias)
