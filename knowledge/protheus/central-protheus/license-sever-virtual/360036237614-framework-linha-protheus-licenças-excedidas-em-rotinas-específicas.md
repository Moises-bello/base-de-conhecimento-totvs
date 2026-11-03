---
article_id: 360036237614
category: License Sever Virtual
content_hash: 4dba3a04c4bf5834b6d47f30fd6546698f8fe01838269cd0cd0d35b30e9385db
fetched_at: '2026-06-28T22:42:20.060835+00:00'
product: protheus
section_id: 360000075428
source: central-protheus
title: Framework - Linha Protheus - LICENÇAS EXCEDIDAS EM ROTINAS ESPECÍFICAS
type: support-article
updated_at: '2026-01-26T19:46:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036237614-Framework-Linha-Protheus-LICEN%C3%87AS-EXCEDIDAS-EM-ROTINAS-ESPEC%C3%8DFICAS
---

**OCORRÊNCIA**  
Ao abrir uma rotina (browser, relatórios ou integração) específica, é exibido o erro abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047398494)  
Contudo ao acessar qualquer outra rotina do mesmo módulo, a mensagem não é exibida.  
  
**AMBIENTE**  
Protheus – Configurador – A partir da versão 11.8  
  
**CAUSA**  
Este erro ocorre devido ao registro incorreto do módulo no Cadastro de Menus (CFGX013.prw).  
  
**SOLUÇÃO**

1. Acesse o Cadastro de Menus no Configurador (SIGACFG/Ambiente/Cadastros/Menus):  
   ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048287433)
2. Desmarque a opção "Todos os menus":  
   ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047398954)
3. Selecione apenas o módulo que contém o relatório:  
   ![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048287613)
4. Clique em "Ok":  
   ![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048287653)
5. Na nova tela, clique em "Adicionar >>":  
   ![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048287753)
6. Selecione o item referente a sua rotina e em seguida clique em "Detalhes":  
   ![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048287793)
7. Certifique-se que o módulo informado na caixa de combinações "Módulo" é igual ao módulo do .XNU acessado (neste caso está divergente):  
   ![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048287913)
