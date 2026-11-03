---
article_id: 4405646277527
category: TAF - eSocial - Configuração
content_hash: 8ad2ca52fffc7173422ab79a116d96783c0f7c9e4f6adf7f09d5413d478e321a
fetched_at: '2026-06-28T22:45:14.356560+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - Como proteger dados sensíveis
  de acordo com a LGPD no TAF
type: support-article
updated_at: '2026-06-23T20:56:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405646277527-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-proteger-dados-sens%C3%ADveis-de-acordo-com-a-LGPD-no-TAF
---

**Dúvida**Como proteger os dados sensíveis de acordo com a LGPD no TAF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - À partir da release 12.1.33  
  
**Solução**1 - Para verificar quais são os dados sensíveis e proteger estas informações de acordo com o LGPD, verifiquem os dois TDN's abaixo:

```
Legislação:  
- https://tdn.totvs.com/display/public/PROT/Controle+de+dados+protegidos+-+Protheus+12  
  
Procedimentos  
-  https://tdn.totvs.com/pages/viewpage.action?pageId=525797274
```

2 - Para restringir acesso das rotinas no TAF para o e-Social, verifique a documentação abaixo para que usuários ou grupos de usuários não tenham acesso as rotinas no sistema:  
[Automação Fiscal - Configuração - Como criar permissão de acesso nas rotinas do TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4435459223191)

3 - Caso precise validar os nomes dos campos para dados sensíveis no TAF, acesse a rotina desejada e clique no botão incluir ou alterar, e clique em cima do campo do dado sensível e pressione a tecla F1 para validar o nome do campo.

Na imagem abaixo, dei um exemplo da rotina de cadastro de Folha de Pagamento, o nome do campo do trabalhador é a C91\_NOME. A tabela PAI é a C91XX0 onde XX é referente ao grupo de empresas cadastrado no TAF:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4638463969559)
