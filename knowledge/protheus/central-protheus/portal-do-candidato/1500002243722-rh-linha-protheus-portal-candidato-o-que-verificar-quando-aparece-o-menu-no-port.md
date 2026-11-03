---
article_id: 1500002243722
category: Portal do Candidato
content_hash: 4a3945c80df6b12ac65e6ef7cce5d4b5b8f982d4aa29f662ba82e4d2f8d5ade7
fetched_at: '2026-06-28T22:42:57.895022+00:00'
product: protheus
section_id: 360005048093
source: central-protheus
title: RH - Linha Protheus - PORTAL CANDIDATO - O que verificar quando aparece o Menu
  no Portal do Candidato e ao selecionar alguma opção do menu não carrega as opções
  dos sub menus
type: support-article
updated_at: '2025-05-05T11:37:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002243722-RH-Linha-Protheus-PORTAL-CANDIDATO-O-que-verificar-quando-aparece-o-Menu-no-Portal-do-Candidato-e-ao-selecionar-alguma-op%C3%A7%C3%A3o-do-menu-n%C3%A3o-carrega-as-op%C3%A7%C3%B5es-dos-sub-menus
---

**Dúvida**O que verificar quando aparece o Menu no Portal do Candidato e ao selecionar alguma opção do menu não carrega as opções dos sub menus?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Portal do Candidato - Todas as versões  
  
**Solução**Verifique se a opção do **Menu** está **bloqueada**, de fato quando um item do Menu é bloqueado, ele não será apresentado e automaticamente nenhuma opção abaixo dele será habilitada no portal. Para certificar-se que a opção não está bloqueada consulte as documentações abaixo.  
  
[MP - PORTAL GCH - Como bloquear um menu no portal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045656933%C2%A0)  
[MP - PORTAL GCH - Como bloquear um sub menu no portal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045109554)  
  
Importante estar com os arquivos de portal atualizados, para saber como atualizar clique [aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044250613-MP-PORTAL-GCH-Como-Atualizar-os-arquivos-do-Portal)  
  
Através do **SRVWIZARD**, sempre que criamos um **Módulo WEB** em nosso exemplo, para a instancia do **(Portal do Candidato - PC),** é criado automaticamente uma pasta com o nome utilizado contendo todos os arquivos e funções java script, que serão utilizados no portal, em alguns casos esses arquivos podem corromper. Esta pasta é criada na seguinte estrutura **protheus\_data/Web.**  
  
No meu exemplo cadastrei o portal do candidato com o nome **pc,** portanto foi criado a pasta exatamente com o mesmo nome.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103085173)  
  
Criou a pasta com o mesmo nome apontado na instancia.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100914874)  
  
Dentro da pasta contem arquivos importantes para uso do portal.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002022682)

Para correção do problema oriento:  
  
**1.** Realizar a exclusão do cadastro da sua instancia **Portal do Candidato,** conforme exemplo abaixo.  
 **![LQlOZILo0s.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002077521)  
  
2.** Reinicie o serviço e certifique-se que a pasta não existe mais em sua estrutura **protheus\_data/Web.** **![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100915994)  
  
3.** Suba o serviço do portal e cadastre novamente sua configuração para instancia Portal do Candidato, no exemplo abaixo estou utilizando dados genéricos, realize a configuração conforme o IP e dados da empresa. Caso tenha dúvidas nesta configuração orienta a avaliar a documentação clicando [aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=267806134), e se persistirem as dúvidas acione o suporte do FrameWork para esclarecimentos.  
  
![F3KoaDeLfD.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002024242)  
 **4.** Suba o serviço e realize o acesso ao portal, utilize a tecla **F12** para mapear a consulta no portal e certificar que esta sendo possível acessar as pastas e arquivos relacionados, para correta apresentação dos menus do portal.  
  
Exemplo:  
![r0d9E7H0D3.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360103087073)

**Verifique se, a *tag PrepareIn* está com conteúdo GRUPO DE EMPRESA,FILIAL**  
Para o Portal do Candidato, que é desenvolvido em *SOAP*, **os *Web Services* precisam ser carregadas em todas as filiais**, ou seja, para preparar o ambiente, o *PrepareIn* é **obrigatório** que esteja com essa configuração.  
  
Se o *PrepareIn* estiver *ALL* ou somente com o código do Grupo de Empresa, **os menus não serão demonstrados.**

****IMPORTANTE**  
**SECURITY=0** são aplicadas somente até o *release* 12.2310 do Protheus.  
Para o *release* 12.2410 em diante, é obrigatório o uso do **SECURITY=1.**Deve ser configurado conforme acima mas com **SECURITY=1.**Para versão 2410 em diante é obrigatório aplicar a documentação abaixo:  
[Configuração portais GCH com autenticação **SECURITY=1**](https://tdn.totvs.com/pages/releaseview.action?pageId=563435668)  
  
Saiba Mais**[Artigos sobre Portal do Candidato](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048093-RH-Portal-do-Candidato)
