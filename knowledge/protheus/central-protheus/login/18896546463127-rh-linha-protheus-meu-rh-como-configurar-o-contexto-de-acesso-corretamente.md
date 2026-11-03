---
article_id: 18896546463127
category: LOGIN
content_hash: 21f18487fb9118bab30abba0151935e6be58968a27e95a79528b0d99ea0450a6
fetched_at: '2026-06-28T22:44:40.471685+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como configurar o contexto de acesso corretamente
type: support-article
updated_at: '2026-06-23T21:19:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18896546463127-RH-Linha-Protheus-MEU-RH-Como-configurar-o-contexto-de-acesso-corretamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18896550503703) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como configurar o contexto de acesso corretamente  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**Para apontar corretamente o contexto de acesso é necessário validar/alterar alguns itens no arquivo de configuração do MEU RH ***APPSERVER.INI*.**Exemplo:  
 **![](https://centraldeatendimento.totvs.com/hc/article_attachments/18896546384279)**O contexto de acesso no appserver.ini é apontado após a "/" na sessão da URL,  
**Exemplo**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18896520688535)  
Neste **exemplo** o contexto de acesso do MEU RH é "30", por padrão na instalação normalmente **é colocado o mesmo valor do grupo de empresa do Protheus**, isso facilita na identificação de cada *URL* no MEU RH que vai corresponder **a um grupo de empresa especifico.**  
  
Existe outro local que deve-se apontar este contexto de acesso para configuração correta do item, para isso, acessar a pasta dos arquivos do portal, a mesma que esta no caminho ***PATH***da *URL* do MEU RH:![](https://centraldeatendimento.totvs.com/hc/article_attachments/18896505119383)  
Acessando este caminho, será possível localizar o arquivo de configuração chamado ***properties.json:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18896561828759)***Neste arquivo, deve-se realizar o apontamento do contexto de acesso, deixando o mesmo conteúdo do que foi colocado no ***APPSERVER.INI*,** porém neste arquivo existe uma estrutura especifica que deve ser respeitada, o contexto deve ser colocado entre aspas duplas e barras: "/contexto/", neste exemplo de configuração do contexto é 30, ficará da seguinte forma:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18896520697367)  
Com estes apontamentos corretos, terá feito com sucesso a configuração correta do contexto de acesso:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18896505130519)  
  
Evitando erros que podem impactar no *login* e *logout* no MEU RH.  
  
**Saiba Mais  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
