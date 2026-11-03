---
article_id: 40407927568151
category: REQUISIÇÕES
content_hash: 28224e6aafaa3b284dcc45eb68122f19c2edb8faaa38a9410431481eef47115e
fetched_at: '2026-06-28T22:44:37.531934+00:00'
product: protheus
section_id: 10299632459799
source: central-protheus
title: RH - Linha Protheus - Meu RH - Erro ao salvar anexo na rotina TCFA040 ao aprovar
  ou reprovar a requisição
type: support-article
updated_at: '2026-05-12T13:11:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40407927568151-RH-Linha-Protheus-Meu-RH-Erro-ao-salvar-anexo-na-rotina-TCFA040-ao-aprovar-ou-reprovar-a-requisi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40407927548439) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Quando a Equipe de RH vai aprovar uma requisição via rotina TCFA040, nos módulos SIGAGPE ou SIGAPON, o erro abaixo ocorre.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40407927550615)  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Causa**  
Este erro é proveniente de uma inconsistência na biblioteca ***webapp.dll*** **que consta nas pastas do** ***bin/appserver*****.**  
  
**Solução**  
Disponibilizados nos links abaixo os arquivos atualizados do ***webapp.dll***, já contendo a correção para a inconsistência reportada. O arquivo é o responsável direto pelo erro apresentado.  
  
A equipe de Desenvolvimento do binário *AppServer* disponibilizou nova versão da DLL:  
  
**Windows:**  
<https://build.tech.totvs.com.br/webapp/panthera_onca/builds/10.1.4-RC6/webapp-10.1.4-RC6-windows-x64-release.zip>  
  
**Linux:**  
<https://build.tech.totvs.com.br/webapp/panthera_onca/builds/10.1.4-RC6/webapp-10.1.4-RC6-linux-x64-release.tar.gz>  
  
Executar os procedimentos abaixo:

* Paralisar os serviços de todos os *AppServers* (*Master* e *Slaves*);
* Substituir o arquivo ***webapp.dll*** em todos os ambientes;
* Reiniciar os serviços após a substituição.

Com a DLL atualizada, a inconsistência na gravação não deverá mais ocorrer.  
  
Adicionalmente, recomenda-se, sempre que possível, a atualização do binário *AppServer*, *LIB* e *DBAccess* para versões atuais.  
  
Ressalta-se que, conforme validado, a origem específica do erro está no arquivo ***webapp.dll***.  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
