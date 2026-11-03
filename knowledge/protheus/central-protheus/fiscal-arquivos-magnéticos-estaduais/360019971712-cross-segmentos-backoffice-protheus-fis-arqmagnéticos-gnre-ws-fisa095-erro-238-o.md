---
article_id: 360019971712
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 148276cbd8e77e6c6097f5194adc65d17b73a727428e6d068d081abfd2e0b482
fetched_at: '2026-06-28T22:42:11.712052+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GNRE WS - FISA095
  - ERRO 238 - O CAMPO EXTRA 'CHAVE DE ACESSO DA NFE OU DO CTE' DEVE SER INFORMADO
type: support-article
updated_at: '2024-05-03T19:13:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019971712-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GNRE-WS-FISA095-ERRO-238-O-CAMPO-EXTRA-CHAVE-DE-ACESSO-DA-NFE-OU-DO-CTE-DEVE-SER-INFORMADO
---

**Ocorrência**No módulo **Livros Fiscais**, ao tentar transmitir as **guias da GNRE**é apresentada a mensagem **'CHAVE DE ACESSO DA NFE OU DO CTE'...etc.**  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Causa**Esse incidente ocorre, pois deve-se realizar a sincronização do TSS com a receita acessando a rotina da GNREWS(FISA095) > menu ações relacionadas > Inf extras > sincronizar.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Para ambiente de produção realize a sincronização de acordo com o estado e código da receita da guia, conforme passo a passo abaixo:  
  
**Sincronização:**Em **Ações Relacionadas** clique em **Sincronizar.**Obs.: é necessário obter o TSS ativo para realizar esta sincronização.   
  
![](http://tdn.totvs.com/download/attachments/235314998/image2016-4-1%2018%3A9%3A47.png?version=1&modificationDate=1459541479000&api=v2)  
  
![](http://tdn.totvs.com/download/attachments/235314998/image2016-4-1%2018%3A9%3A57.png?version=1&modificationDate=1459541489000&api=v2)    
  
 ![](http://tdn.totvs.com/download/attachments/235314998/image2016-4-1%2018%3A10%3A19.png?version=1&modificationDate=1459541511000&api=v2)  
  
Verifique que a atualização da tabela é realizada com sucesso.  
  
2. Para ambiente de homologação importe a tabela de códigos de informação extras conforme o passo abaixo:  
  
\* Através da rotina GNRE WS (**FISA095**) acesse : Ações **Relacionadas** / **Inf. Extras**:  
  
Na primeira utilização da rotina a tela será apresentada da seguinte maneira:  
  
![](http://tdn.totvs.com/download/attachments/235314998/image2016-4-1%2018%3A2%3A53.png?version=1&modificationDate=1459541066000&api=v2)  
  
Nesta rotina é possível realizar a importação do arquivo .csv que contém informações extras do ambiente de homologação, porém para obter o cadastro atualizado e de produção é necessário realizar a Sincronização através do TSS exemplificado nos próximos passos.

**Importação tabela de Homologação – Clique em Ações Relacionadas / Importação.**  
![](http://tdn.totvs.com/download/attachments/235314998/image2016-4-1%2018%3A5%3A17.png?version=1&modificationDate=1459541209000&api=v2)  
  
Informe o caminho onde encontra-se o arquivo .csv:  
  
 ![](http://tdn.totvs.com/download/attachments/235314998/image2016-4-1%2018%3A5%3A56.png?version=1&modificationDate=1459541248000&api=v2)

Obs.: A tabela que deve ser importada, encontra-se no final da página.

Conclusão da importação da tabela:  
  
 ![](http://tdn.totvs.com/download/attachments/235314998/image2016-4-1%2018%3A6%3A46.png?version=1&modificationDate=1459541299000&api=v2)  
  
 ![](http://tdn.totvs.com/download/attachments/235314998/image2016-4-1%2018%3A7%3A12.png?version=1&modificationDate=1459541324000&api=v2)  
  
Documentação oficial de Cadastro de Informações Extras referente à GNRE WS:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=700503940>
