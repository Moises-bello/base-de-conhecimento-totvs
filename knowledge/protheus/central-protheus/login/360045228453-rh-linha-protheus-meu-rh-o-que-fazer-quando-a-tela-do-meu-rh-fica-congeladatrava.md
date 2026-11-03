---
article_id: 360045228453
category: LOGIN
content_hash: 5c0ab1251f88e973dd927ecbd512405bd7e1d72a06931d59ee316b82c183c448
fetched_at: '2026-06-28T22:44:40.654022+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - O que fazer quando a tela do MEU RH fica Congelada/Travada/Branca
  ao acessá-lo via Navegador ou APP
type: support-article
updated_at: '2026-06-23T21:13:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045228453-RH-Linha-Protheus-MEU-RH-O-que-fazer-quando-a-tela-do-MEU-RH-fica-Congelada-Travada-Branca-ao-acess%C3%A1-lo-via-Navegador-ou-APP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33788792006935) Tempo aproximado para leitura: 00:03:00 min****Dúvida**O que fazer quando a tela do MEU RH fica Congelada/Travada/Branca ao acessá-lo via Navegador ou APP?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – Todas às versões  
  
**Solução**Verifique se ao logar via MEU RH ocorre a seguinte autenticação em seu **APPSERVER**:  
**[RH - Linha Protheus - MEU RH - Como gerar o Console.log para análise de erros do MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416746889751)**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7656277694103)​  
  
**1º CASO:** Se ocorrer a autenticação e a tela fica Congelada/Travada/Branca no MEU RH, para que este problema seja corrigido, a TOTVS disponibilizou os seguintes passos:

1. Atualizar os arquivos “PORTAL MEU RH”:  
   **[RH - Linha Protheus - MEU RH - Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)**
2. Aplicar a última atualização de expedição RH no RPO do ambiente do MEU RH;  
   **[RH - Linha Protheus - MEU RH - Pacote de acumulado do RH no Portal de Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007189282)**
3. Instalar novamente o APP de acordo com as lojas da *APPLE* e *ANDROID*;
4. Limpe o *cache* do navegador e/ou do celular:  
   [Clique aqui para saber como limpar o Cache de aparelhos Android](https://support.google.com/accounts/answer/32050?co=GENIE.Platform%3DAndroid&hl=pt-BR);  
   [Clique aqui para saber como limpar o Cache de aparelhos iPhone (IOS)](https://support.apple.com/pt-br/HT201265);
5. Inserir a chave “Compression” na *seção* “HTTP” do **APPSERVER.INI**;  
     
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062245553)
6. Caso esteja utilizando o MEU RH em acesso externo, verifique o Firewall de sua Empresa, pois em muitos casos o Firewall impede o acesso e, por mais que ocorra a autenticação, o LOGIN via APP não é executado;
7. Caso tenha migrado de release, certifique-se de atualizar os arquivos do portal MEU RH e ajustar o arquivo **PROPERTIES.JSON**.  
   **[RH - Linha Protheus - MEU RH - Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)**

**2º CASO:** Se não ocorrer a autenticação e fique uma tela Congelada/Travada/Branca no MEU RH, siga as orientações do artigo abaixo, pois pode ser algum problema na *URL*:  
  
Documento de Referência MEU RH: [**Passo 5: Acessando o portal e app**](https://tdn.totvs.com/display/public/NPR/Passo+5%3A+Acessando+o+portal+e+app)  
Também sugiro que valide a sua configuração dos arquivos indicados no artigo abaixo, conforme mencionado, pode ser um problema na *URL*, ela tem um padrão muito específico, qualquer caractere errado e/ou espaço pode ocasionar erro.  
**[RH - Linha Protheus - MEU RH - Como configurar o APPSERVER.INI, PROPERTIES.JSON e URL do QRCODE para acesso ao MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044715514)  
  
Importante:** Além das orientações citadas acima, sempre manter **LIB e Binários** atualizados com as versões mais recentes disponíveis no Portal.  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)
