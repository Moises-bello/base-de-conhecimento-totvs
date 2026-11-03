---
article_id: 28740734105879
category: Meu RH - Ponto
content_hash: 806de7b764f43dc0d1600e0d7feaa99fe050acd43520cfbe6554d759a4092dea
fetched_at: '2026-06-28T22:47:30.272118+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: RH - RM - Meu RH - Por que a geolocalização no Meu RH via Web é menos precisa?
type: support-article
updated_at: '2026-01-16T17:11:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28740734105879-RH-RM-Meu-RH-Por-que-a-geolocaliza%C3%A7%C3%A3o-no-Meu-RH-via-Web-%C3%A9-menos-precisa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28740739733911) Tempo aproximado para leitura: **00:06:00 min**  
  
**Dúvida**  
Por que a geolocalização no Meu RH via Web retorna uma localização bem distante do real?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Solução**

A marcação de ponto no **Meu RH via Web** não conta com a opção de "GPS físico", disponível no **aplicativo Meu RH** para smartphones. Essa tecnologia, exclusiva dos dispositivos móveis, permite maior precisão na localização. Por outro lado, a geolocalização via Web utiliza as funcionalidades **do navegador para estimar a localização do usuário** com base em dados como endereço IP, sinais de GPS compartilhados e redes Wi-Fi próximas, resultando em uma precisão apenas **aproximada**.  
  
Os serviços de geolocalização baseados em **IP** fornecem apenas uma **estimativa da localização**, com precisão que varia de 95%-99% em nível de país, 55%-80% em nível regional e 50%-75% em nível de cidade. Pelo navegador, a margem de erro pode chegar a um raio de até 100 km, dependendo da região.

**Se a localização obtida for muito imprecisa ou indicar outro país, siga as recomendações abaixo:**

* **Utilize navegadores homologados:** Certifique-se de que está utilizando um [navegador compatível com o Meu RH](https://tdn.totvs.com/display/NPR/Navegadores+homologados). Navegadores não homologados, como o BRAVE, podem alterar a localização para outro estado ou país devido ao seu método de acesso.
* **Evite o uso de VPN ou redes com proxy:** Conexões por VPN ou redes com proxy (como o CloudFlare) podem alterar o IP para um local diferente, resultando em geolocalização incorreta. Prefira redes Wi-Fi ou 4G próximas ao local de uso.
* **Atualize a página:** Caso a localização obtida esteja imprecisa, recarregue a página (F5) para forçar o navegador a buscar uma nova posição.
* **Considere desativar a geolocalização no navegador:** Se a empresa não tiver regras que exijam o uso de geolocalização, é possível desabilitá-la. No Chrome, [siga as configurações específicas para isso.](https://support.google.com/chrome/answer/114662?hl=pt-BR&ref_topic=7439724&sjid=18397520010085324945-SA&co=GENIE.Platform%3DDesktop&oco=1)
* **Prefira o aplicativo móvel:** Para maior precisão, utilize o aplicativo Meu RH em smartphones, que conta com GPS físico.
* **Limitações da geolocalização pelo navegador:** O serviço utiliza IPs e algoritmos HTML5, resultando em uma precisão aproximada, Por exemplo, ao acessar o Meu RH e acessar a marcação por geolocalização e buscou uma localização de 5KM aproximado, ao acessar o Portal do Uber ou Portal do IFOOD obterá a mesma localização.

Caso ainda tenha dúvidas sobre a localização, recomendamos consultar a [documentação completa elaborada pelo nosso time de Produto.](https://tdn.totvs.com/pages/viewpage.action?pageId=516629620) Ela aborda detalhadamente o funcionamento da geolocalização no Meu RH e inclui uma seção de perguntas frequentes (FAQ) com respostas às principais dúvidas.
