---
article_id: 360049493314
category: IMPLANTAÇÃO
content_hash: 1588b0e3748e6a3cfe89a044d6947aae3e9e35d4ea3eb910c7344eaedf9e0342
fetched_at: '2026-06-28T22:44:33.406659+00:00'
product: protheus
section_id: 10299929290007
source: central-protheus
title: RH - Linha Protheus - MEU RH - Qual deve ser o conteúdo do arquivo PROPERTIES.JSON
type: support-article
updated_at: '2026-06-19T14:02:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049493314-RH-Linha-Protheus-MEU-RH-Qual-deve-ser-o-conte%C3%BAdo-do-arquivo-PROPERTIES-JSON
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30645948998935) Tempo aproximado para leitura: 00:05:00 min**  
  
**Dúvida**  
Qual deve ser o conteúdo do arquivo PROPERTIES.JSON?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
O conteúdo do **PROPERTIES.JSON** é único por endereço de acesso e deve estar configurado de acordo com as informações do seu **APPSERVER.INI.**  
  
A configuração do PROPERTIES.JSON está descritas passo a passo na [**Documentação de referências sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421), essa FAQ foi criada para auxiliar aqueles com problema na configuração indicando como realizar a manutenção diretamente no arquivo informado.  
  
O arquivo **PROPERTIES.JSON** pode ser baixado na Central de downloads conforme link abaixo. Caso esteja configurando o **MEU RH** a primeira vez, o **PROPERTIES.JSON** precisa ser renomeado de **PROPERTIES\_EXEMPLO** para **PROPERTIES** antes de ser colocado dentro da pasta com os arquivos do Portal no ambiente.  
  
[**RH - Linha Protheus - MEU RH - Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)  
  
![properties.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/9144020329239)  
  
O **PROPERTIES.JSON** deve estar na mesma pasta onde estão os demais arquivos do **Portal MEU RH (arquivo anexo ao final deste documento).** Ele segue um **formato padrão** e não pode sofrer alterações fora do indicado, onde deve ser preenchido entre as **" " (duas aspas duplas)** conforme demonstrado abaixo, caso contrário poderá ter problemas no acesso ao MEU RH via navegador ou aplicativo do celular.  
  
**1º Passo:** Verifique o "Path" (caminho) informado no endereço de acesso no APPSERVERl.INI, caso tenha mais de um endereço deve haver mais de um arquivos do portal MEU RH e consequentemente mais de um PROPERTIES.JSON, ou seja, cada endereço tem seu próprio "Path" (caminho) com o PROPERTIES.JSON apontando para ele.  
  
**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075442313)**  
  
**2º Passo:** A **"baseUrl"** do arquivo PROPETIES.JSON deve conter HTTP ou HTTPS. No exemplo acima foi configurado somente o HTTP no qual será utilizado para acessar - **http://.**  
  
Na sequência deve conter o endereço de acesso, pode ser um endereço externo, porém, para acesso externo deve ser analisado com a Infraestrutura interna da Empresa. No exemplo foi utilizado um IP interno - **192.168.0.4.**  
  
Na sequência deve conter **' : '** **(dois pontos)** seguido da porta do **REST**, a mesma informada na chave **HTTPREST** do **APPSERVER.INI.** No exemplo foi utilizada a porta = **6661.**  
  
Em seguida deve conter '**/**' (barra) mais o conteúdo da chave **URL** abaixo da chave **HTTPENV**, neste caso pode haver mais de um quando tem mais de um endereço utilizando o mesmo **REST**, cuidado com letras maiúsculas e minúsculas (*case-sensitive*). No exemplo fica dessa forma -> **/restT2.**  
  
Ou seja: **"http://192.168.0.4:6661/restT2"**.  
  
**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074274094)**  
  
**3º Passo:**A tag **"rootContext"** do arquivo **PROPETIES.JSON** deve conter '**/**' (barra) mais uma informação específica de acordo com a chave **PrepareIn** do **APPSERVER.INI** e depois outra '**/**' (barra). No exemplo fica - **/T2/.**  
  
**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075443533)**  
  
**IMPORTANTE:** Em muitos casos de erro o problema está no preenchimento da configuração da Chave ROOTCONTEXT, no caso dos exemplos acima, a configuração foi feita somente para o meu grupo '**T2**', sendo assim, em todo local que ver '**T2**' é menção ao meu GRUPO de Empresas do SIGAMAT, se no seu ambiente o GRUPO for '**01**', substitua a informação '**T2**' por '**01**'.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9144409206167)  
  
Caso mesmo assim tenha algum problema no acesso ao MEU RH verifique o artigo abaixo e, se necessário abra um chamado ao Suporte encaminhando as evidências relacionadas no referido artigo:  
  
**Obs.: Segue em anexo ao final este artigo uma cópia do arquivo properties.json já renomeado.**  
  
[**RH - Linha Protheus - MEU RH - O que fazer quando não consigo acessar o MEU RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050238493)  
  
**ATENÇÃO:** Certifique-se sempre de estar com seu ambiente atualizado, pois são disponibilizados periodicamente atualizações com melhorias e correções no MEU RH.  
  
[**RH - Linha Protheus - MEU RH - Pacote de acumulado do RH no Portal de Cliente**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007189282)  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
