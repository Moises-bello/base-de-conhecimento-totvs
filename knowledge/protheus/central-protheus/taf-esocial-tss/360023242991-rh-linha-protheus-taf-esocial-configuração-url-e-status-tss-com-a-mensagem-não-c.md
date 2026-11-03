---
article_id: 360023242991
category: TAF - eSocial -TSS
content_hash: 40f6e86f3dcb048ab706034947a51d529a98e69b5c15c948e477ff213b16a922
fetched_at: '2026-06-28T22:45:21.945211+00:00'
product: protheus
section_id: 1500001536761
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - URL e Status TSS com a
  mensagem "Não Conectado"
type: support-article
updated_at: '2026-06-26T12:08:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023242991-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-URL-e-Status-TSS-com-a-mensagem-N%C3%A3o-Conectado
---

**Dúvida**Em Informações do TSS na rotina de Diagnóstico, as opções URL TSS e Status TSS ficam com o valor "Não Conectado".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23690563923223)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF -Todas as versões

**Solução**Para correção do TSS não conectado no diagnóstico, seguir as instruções abaixo:

1. Será necessário abrir SIGACFG:
2. Base de Dados/Dicionário/Base de Dados/Parâmetro
3. Localizar o parâmetro MV\_TAFSURL

​![](https://atendimento.totvs.com/attachments/token/HAUlVSHt0LdZtxdbJ9aDJfLwH/?name=inline650841403.png)​  
  
Selecionar o parâmetro e clicar em editar:  
![](https://atendimento.totvs.com/attachments/token/6uiUfZ07uG3yPMzStzROibjcD/?name=inline-2014719819.png)​  
  
​  
Preencha com sua URL :  
![](https://atendimento.totvs.com/attachments/token/mPIt2ddfEbS6s9oCNXOPmtCZp/?name=inline-1001084364.png)​  
Apertar na porta para salvar e sair  
![](https://atendimento.totvs.com/attachments/token/e3hBcRRoQn7N6PSkGfnxrbg9s/?name=inline-1752736607.png)
