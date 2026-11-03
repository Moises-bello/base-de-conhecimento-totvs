---
article_id: 360010397312
category: Banco de talentos
content_hash: c1e3766d768ae7d3666a95aebb4c89a3bc1499016340ac2b47f733c149e770f0
fetched_at: '2026-06-28T22:47:16.113824+00:00'
product: rm
section_id: 1500000834901
source: central-rm
title: RH - RM - RHU - Customizar a tela do Banco de Talentos - Alterar a logo e as
  cores
type: support-article
updated_at: '2026-05-29T20:03:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010397312-RH-RM-RHU-Customizar-a-tela-do-Banco-de-Talentos-Alterar-a-logo-e-as-cores
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16034693369751) Tempo aproximado para leitura: 00:00:30 min**  
  
**Dúvida**  
Como alterar a logo e as cores do Banco de Talentos?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas – A partir da versão 12.1.9  
  
**Solução**  
Para customização da logo do Banco de Talentos, siga os passos abaixo:   
  
1. Acesse o local de armazenamento de arquivos, onde o portal do Banco de talentos está instalado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30968625989527)

2. Acesse o arquivo ***'img'*** localizado na pasta '*C:\TOTVS\CorporeRM\FrameHTML\RM\Rhu-BancoTalentos\framework\assets*. Este arquivo contém as imagens padronizadas que são apresentadas no Banco de talentos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30968658350999)

Nesta pasta, é possível alterar as imagens apresentadas por outras, conforme preferência, para personalização. Para que as imagens sejam substituídas, deverão ajustar a descrição de cada imagem, por exemplo *rm\_rhu\_logo\_empresa.png* deve passar a ser *rm\_rhu\_logo\_empresa\_antiga.png* para que a nova imagem da logo fique com a descrição *rm\_rhu\_logo\_empresa.png*.  
  
***>> Esta ação deve ser realizada para qualquer outra imagem que deseja alterar.***  
  
3. Acesse a pasta ***'img'*** do arquivo ***'custom'*** localizado na pasta '*C:\TOTVS\Corpore\FrameHTML\RM\Rhu-BancoTalentos\framework\assets\custom*. Nesta pasta, já existirá uma imagem padrão como logo, entretanto para alteração deverá ajustar a descrição desta imagem para outra que difere da imagem da logo que querem que colocar. A nova logo deverá possuir a seguinte descrição: *rm\_rhu\_logomarca-sample.png.*  
  
**Para customização das cores do Banco de Talentos, siga os passos abaixo:**  
  
1. Ainda no arquivo ***'custom'*** localizado na pasta '*C:\TOTVS\Corpore\FrameHTML\RM\Rhu-BancoTalentos\framework\assets\custom*, acesse a pasta '***css'***.   
  
Para fazer uma nova personalização deve-se criar um arquivo com o nome ***"rm\_rhu\_layout\_personalizado.css"***(não deve ser utilizado outro nome). Nesta pasta, existirá um arquivo de personalização exemplo com o nome ***"rm\_rhu\_layout\_personalizado-sample.css"***. Poderá utilizar este para realizar as modificações das cores, mas ao concluir deve renomear o arquivo para '***rm\_rhu\_layout\_personalizado.css'***.  
  
Uma vez criado estes arquivos, o sistema detectará automaticamente a existência de uma nova identidade visual e carregará automaticamente no sistema.  
  
Lembrando que as cores em css podem ser declaradas de três maneiras:  
- Pelo nome em inglês (ex: red, blue, green, White)  
- Pelo código hexadecimal (ex: #FFFFFF, #C74F7O, #0c7c21)  
- Pelos valores RGB (ex: rgb(255, 0, 0), rgb(100%, 0%, 0%))  
  
>> Podem ser utilizadas imagens do tipo .jpg, .gif, e .png. Não há um tamanho específico para as imagens, mas por padrão as imagens que são utilizadas pela TOTVS possui as seguintes dimensões:  
  
- Logo: 130 x 52 pixels  
  
**Importante**  
Após realizar tais modificações, reinicie o servidor IIS onde o Banco de Talentos está instalado e limpem o cache no navegador utilizado para acesso.  
  
**Saiba Mais**  
Para maiores informações, acesse:

- [Customização do Banco de Talentos](https://tdn.totvs.com/display/public/LRM/DT_Personalizacao_do_Banco_de_Talentos)

- [RH - RM - RHU - Customização da tela do Banco de Talentos - Alterar os Banners](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8553925502615)
