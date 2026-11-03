---
article_id: 360050358653
category: PONTO ELETRÔNICO
content_hash: 013161054da1f07a95a7158a6c73de4e3a4ba7bd458b9aadd604cca381e4b56a
fetched_at: '2026-06-28T22:44:36.779717+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como habilito a Localização da rotina Relógio
  (Geolocalização)
type: support-article
updated_at: '2026-06-16T17:55:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050358653-RH-Linha-Protheus-MEU-RH-Como-habilito-a-Localiza%C3%A7%C3%A3o-da-rotina-Rel%C3%B3gio-Geolocaliza%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30646657606167) Tempo aproximado para leitura: 00:05:00 min**  
  
**Dúvida**  
Como habilito a Localização da rotina Relógio (Geolocalização)?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
Para habilitar a Localização da rotina Relógio (Geolocalização) você deve utilizar os [**navegadores homologados**](https://tdn.totvs.com/display/public/NPR/Navegadores+homologados) do computador ou o APP MEU RH em aparelhos celulares com os [**sistemas operacionais homologados**](https://tdn.totvs.com/display/public/NPR/0.2++Linha+Protheus).  
  
[**RH - Linha Protheus - MEU RH - Requisitos para utilizar o APP Meu RH.**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024773993)  
  
Também é necessário que verifique se seu ambiente atende as configurações indicadas nos artigos abaixo:

* [**9.0 Relógio Batidas Remotas - Portaria 373/2011**](https://tdn.totvs.com/pages/releaseview.action?pageId=334338837)
* [**Utilização da geolocalização no aplicativo MeuRH**](https://tdn.totvs.com/pages/releaseview.action?pageId=516629620)

**Dúvidas frequentes:**  
**O que fazer quando a rotina Relógio (Geolocalização) não demonstra a Localização?**  
Normalmente isso ocorre por falta da implementação dos certificados **HTTPS/SSL** no servidor, de acordo com o [**Boletim Técnico**](https://tdn.totvs.com/pages/releaseview.action?pageId=334338837) isso é um requisito necessário para esse tipo de marcação.  
  
Para configuração do **HTTPS/SSL** verifique as informações do artigo abaixo:  
[**RH - Linha Protheus - MEU RH - Como configurar o SSL/HTTPS para o MEU RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042649133)  
  
Alguns aparelhos celulares compartilham a localização do aparelho mesmo com o endereço configurado como "**HTTP**", porém, por exemplo, no navegador Chrome a opção de habilitar a localização fica bloqueada quando o endereço acessado utiliza a configuração "**HTTP**".  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074566114)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074566154)  
  
O problema também pode ocorrer devido estar desabilitado a localização no Navegador ou no Aparelho Celular, para verificar como habilitar essas informações entre em contato com o Suporte do Navegador ou do Sistema operacional de seu aparelho celular.  
  
**É necessário ter configuração do HTTPS/SLL ou a marcação funciona com configuração HTTP?**  
De acordo com o [**Boletim Técnico**](https://tdn.totvs.com/pages/releaseview.action?pageId=334338837) é um requisito a implementação dos certificados **HTTPS/SSL** no servidor.  
  
Com a configuração "**HTTP**" é possível registrar a marcação, porém o sistema não vai gravar as informações de **Latitude e Longitude** na Tabela de Movimentação das Marcações (SP8), operacionalmente no Sistema não há problema.  
  
**![Geolocaliza__o_via_navegador.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/30646657610903)**  
  
**O que fazer quando a localização está errada no APP ou no Navegador?**  
A localização é algo fornecido pelo aparelho celular ou Navegador do seu computador, o MEU RH simplesmente grava essa informação, nessa situação você pode testar a localização em outros aplicativos e sites e, se necessário, entre em contato com o Suporte do Navegador ou do Sistema operacional de seu aparelho celular.  
  
Em alguns cenários, o mapa demora alguns segundos para carregar. Tanto a demora na localização quanto sua precisão podem variar devido a conexão da operadora que fornece a conexão de internet, da localização da antena, da região, da configuração do Wifi, utilização de VPN, repetidores de sinal Wifi, entre outros.  
  
Temos um caso mapeado em que a localização do celular está com o GPS **"desabilitado"** e quando acesso a geolocalização ela manda "**habilitar**" a localização, nesse cenário a primeira localização que é trazida, ás vezes, é o local da antena de repetição de sinal da operadora, porém basta recarregar o mapa ou abrir e fechar a opção de geolocalização que ele retorna para o endereço correto.  
  
![Geolocaliza__o_endere_o_errado.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360075776533)  
  
Com relação ao endereço e a questão do bairro, seu aparelho é quem informa sua localização e isso pode trazer informações diferentes em cada operadora, segue o exemplo de um endereço:  
  
No site dos Correios na pesquisa de CEP é informado o bairro Chácara Canta Galo.  
  
![](https://totvssuporte.zendesk.com/attachments/token/yNaPT6HCVs0DL1VDD0ryXe9qN/?name=inline1294957846.png)​  
  
No Google MAPS é apresentado o bairro como Jardim Barbacena, que é bem próximo, mas não está correto.  
  
![](https://totvssuporte.zendesk.com/attachments/token/yTAy0jqabd9BncU9gaaDrlB04/?name=inline-1551195669.png)​  
  
No Mapas do IPHONE a rua é apresentado com o nome de ESTRADA, aqui não traz o bairro.  
  
​![](https://totvssuporte.zendesk.com/attachments/token/laPeT1ieNNPDPACCdpFeBeC3S/?name=WhatsApp+Image+2020-04-29+at+08.08.58.jpeg)​​​​  
  
No APP MEU RH via Android o bairro é Vila Viviana, é uma subdivisão de bairro na região, mas não é o mesmo dos Correios, a localização também não é rua Maracatu, porém a divisão de ruas do condomínio não é oficial, então ele traz a rua mais próxima.  
  
![](https://totvssuporte.zendesk.com/attachments/token/t1nOugedrlmRjLCKlW0cLmcZ7/?name=WhatsApp+Image+2020-04-29+at+08.15.43.jpeg)  
  
No APP MEU RH via IOS do IPHONE 8, o bairro também é Vila Viviana.  
  
![](https://totvssuporte.zendesk.com/attachments/token/sb81F3MJpc8YcYvrMRrIpbpZ4/?name=WhatsApp+Image+2020-04-29+at+08.08.59.jpeg)  
  
Para mais informações sobre a rotina Relógio (Geolocalização) acesse o artigo abaixo:  
[**RH - Linha Protheus - MEU RH - Como registrar a marcação de Ponto através da rotina Relógio (Geolocalização)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050355093)  
  
**ATENÇÃO:** Certifique-se sempre de estar com seu ambiente atualizado, pois são disponibilizados periodicamente atualizações com melhorias e correções no MEU RH.  
[**RH - Linha Protheus - MEU RH - Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)  
[**RH - Linha Protheus - MEU RH - Pacote de acumulado do RH no Portal de Cliente**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015741848)  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
