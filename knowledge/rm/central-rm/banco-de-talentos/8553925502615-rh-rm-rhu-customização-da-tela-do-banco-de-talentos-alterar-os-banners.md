---
article_id: 8553925502615
category: Banco de talentos
content_hash: 5d2989002e915964f8f2651cf96ce6e90fc00965206580ad5afcc6408254792e
fetched_at: '2026-06-28T22:47:16.077007+00:00'
product: rm
section_id: 1500000834901
source: central-rm
title: RH - RM - RHU - Customização da tela do Banco de Talentos - Alterar os Banners
type: support-article
updated_at: '2025-01-09T12:31:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8553925502615-RH-RM-RHU-Customiza%C3%A7%C3%A3o-da-tela-do-Banco-de-Talentos-Alterar-os-Banners
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15864083367703) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como alterar os banners do banco de talentos ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas – A partir da versão **12.1.9** e superiores  
  
**Solução**Siga os passos abaixo para personalizar os banners do Banco de Talentos.  
   
1. Acesse o local de armazenamento de arquivos, onde o portal do Banco de talentos está instalado:  
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26719245441303)  
  
2. Acesse o arquivo **home-services.js** localizado na pasta 'C:\TOTVS\CorporeRM\FrameHTML\RM\Rhu-BancoTalentos\html\home\home-services.js'. Este arquivo contém as definições do banner que é apresentado no Banco de talentos.  
   
Nele é possível definir as propriedades de cada item a ser exibido no banner como: imagem (image), título (title) e text (descrição). Como pode ser verificado na imagem abaixo, adicionamos um novo item com propriedades customizadas. Os demais itens podem ser apagadas ou modificadas a necessidade de personalização.  
   
![](https://totvssuporte.zendesk.com/attachments/token/2JCYn8cUimzIxGUFBy5HxIcSP/?name=inline371901188.png)  
   
>> Lembre-se de verificar a extensão da imagem informada no arquivo **home-services.js** localizado na pasta “**FrameHTML\RM\Rhu-BancoTalentos\html\home\home-services.js**”, ela precisa ser a mesma da imagem salva na pasta.  
   
>> Podem ser utilizadas imagens do tipo .jpg, .gif, e .png. Não há um tamanho específico para as imagens, mas por padrão as imagens que são utilizadas pela TOTVS possui as seguintes dimensões:  
   
- Logo: 130 x 52 pixels  
- Imagens do banner: 1650 x 528 pixels  
   
**Importante:** *Após realizar tais modificações, reinicie o servidor IIS onde o Banco de Talentos está instalado e limpem o cache no navegador utilizado para acesso.***Saiba Mais:**

Para maiores informações, acesse:

- [Customização da tela do Banco de Talentos / Currículo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010397312-TOTVS-RH-Linha-RM-RHU-Customiza%C3%A7%C3%A3o-da-tela-do-Banco-de-Talentos-Curr%C3%ADculo)
