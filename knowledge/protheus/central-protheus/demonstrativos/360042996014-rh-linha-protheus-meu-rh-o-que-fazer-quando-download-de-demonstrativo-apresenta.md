---
article_id: 360042996014
category: DEMONSTRATIVOS
content_hash: e98cd7761daacc33d212ae3041f89b26bb6017d04b0edc6f15ff6ec90cf5fd92
fetched_at: '2026-06-28T22:44:38.465524+00:00'
product: protheus
section_id: 10299629664279
source: central-protheus
title: RH - Linha Protheus - MEU RH - O que fazer quando download de demonstrativo
  apresenta "Falha ao carregar documento PDF"
type: support-article
updated_at: '2026-06-19T18:58:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042996014-RH-Linha-Protheus-MEU-RH-O-que-fazer-quando-download-de-demonstrativo-apresenta-Falha-ao-carregar-documento-PDF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24442857389591) Tempo aproximado para leitura: 00:05:00 min**  
  
**Dúvida**  
O que fazer quando download de demonstrativo apresenta "Falha ao carregar documento PDF"?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**  
Para resolver o problema indicado é necessário seguir **todas as orientações** relacionadas abaixo:  
  
**Observação:** Clientes ***CLOUD*** devem analisar essas informações e solicitar atualização junto ao ***CLOUD***.  
  
1° No appsever.ini onde está configurado seu ambiente do aplicativo na tag **StartPath** a system deve estar com barra invertida no começo e no final conforme exemplo **StartPath=\system\**  
  
**Obs.:** Para ambientes **Linux,** por ser um Sistema Operacional **"*****case sensitive*****",** recomendamos que a pasta informada no "**startpath**" esteja todo em **minúsculo** e deve ser avaliado as propriedades do diretório e dos arquivos baixados, se estão com todas as permissões habilitadas.   
Exemplo do **StartPath=/system/** , para ambientes em Linux utilizar barras invertidas.  
  
2º Atualize o binário do appserver do Meu RH. As versões mais recentes podem ser baixadas de acordo com as configurações do seu Servidor na central de download: **Protheus > TOTVSTEC-FRAMEWORK > APPSERVER**.   
  
3º Certifique-se do seu appserver.ini estar com **Security=1**. Caso tenha problemas para acessar a ferramenta com essa configuração você terá que revisar toda sua configuração do MEU RH.  
  
4° São necessários **arquivos de binário** de impressão diferentes para cada sistema operacional. Esses arquivos devem estar na mesma pasta do appserver e podem ser baixados na central de download: **Protheus > TOTVSTEC-FRAMEWORK > SMARTCLIENT**.   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001862721)  
  
5º **atualização do** ***PRINTER***, em todas as pastas do binário, *appserver* e *smartclient*, tanto ***MASTER*** quanto os ***SLAVES***:  
[Como atualizar o Totvs Printer](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020375912)  
  
**Importante:**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24442870728215)  
  
**Saiba Mais**  
[RH - Linha Protheus - APP MEU RH - O que conferir quando não executa o download demonstrativo de pagamento no App Meu RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042183693)  
[RH - Linha Protheus - MEU RH - Ao baixar o demonstrativo de pagamento em ambiente Linux apresenta erro Fontconfig error: Cannot load default config file](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4439312281879)  
  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
