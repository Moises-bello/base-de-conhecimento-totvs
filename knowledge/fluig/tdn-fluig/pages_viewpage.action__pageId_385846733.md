---
content_hash: d0362efdbce6a8779a4eb3a2622486668b01b6fd9be6868c0d38b1846a894583
fetched_at: '2026-06-28T21:35:26.639511+00:00'
page_id: '385846733'
product: fluig
source: tdn-fluig
title: ARQ - Por que ocorre problema ao exportar BIRT formato PDF?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=385846733
version: 7
---

true.\*ndicenone

**Produto:**

**Versão:** Independente da versão da plataforma o problema ocorre em servidores Linux®.

## Ocorrência

Durante análise, identificamos que a fonte Calibri, é um produto proprietário da Microsoft®, projetado para substituir o clássico Times New Roman, a partir de 2007. Para baixá-lo da internet e usá-lo é necessário ter uma licença de uso.

A maioria das documentações pesquisadas, cita o uso apenas nos sistemas operacionais MAC OS e MS Windows.   
  
Existe a possibilidade de copiar os arquivos TTF da fonte Calibri e instalá-las no servidor linux, mas isto é pouco recomendável, pois existe a possibilidade de gerar um problema jurídico para o cliente.   
  
Segue algumas fontes que divagam sobre licenciamento ao utilizar a fonte Calibri em servidores Linux®.   
  
[https://www.hardware.com.br/comunidade/fonte-times/807197/](https://www.hardware.com.br/comunidade/fonte-times/807197/ "Follow link")

[https://docs.microsoft.com/pt-br/typography/truetype/](https://docs.microsoft.com/pt-br/typography/truetype/ "Follow link") 

## Causa

Quando é exportado um relatório Birt para arquivo PDF, uma fonte que está configurada como Calibri fica como Times New Roman. Porém, isto só ocorre quando a plataforma está instalada em um servidor Linux®, no Windows® funciona normalmente.

## Solução

false11Solução 1

Fizemos alguns testes com o SO Linux Ubuntu 18.04 LTS 64 bits, e acabei por encontrar uma fonte semelhante, praticamente idêntica ao Calibri. Trata-se da fonte Carlito, de propriedade da Google, cuja licença é OFL(Open Font License é uma licença de uso livre e de código aberto elaborada pela SIL International especificamente para o uso por fontes tipográficas de computador).   
  
Dentro do server Linux e utilizando a fonte Carlito, o resultado foi idêntico ao uso do Calibri no MS Windows.   
  
Carlito --> equivalente a Calibri   
Caladea --> equivalente a Cambria   
Segue algumas sugestões de instalação e links úteis.   
  
[https://fontlibrary.org/en/font/carlito](https://fontlibrary.org/en/font/carlito "Follow link")   
  
Para Linux com sistema de pacotes Debian:   
  
apt-get update   
apt-get install fonts-crosextra-carlito fonts-crosextra-caladea   
fc-cache -v -r   
[https://wiki.debian.org/SubstitutingCalibriAndCambriaFonts](https://wiki.debian.org/SubstitutingCalibriAndCambriaFonts "Follow link")   
  
Para Linux com sistema de pacotes RPM:   
  
yum install google-crosextra-carlito-fonts   
[https://centos.pkgs.org/7/centos-x86\_64/google-crosextra-carlito-fonts-1.103-0.2.20130920.el7.noarch.rpm.html](https://centos.pkgs.org/7/centos-x86_64/google-crosextra-carlito-fonts-1.103-0.2.20130920.el7.noarch.rpm.html "Follow link")

2Solução 2

Uma outra sugestão é utilizar um pacote para linux (ttf-mscorefonts), criado pela Microsoft, para uso de cliente final com as seguintes fontes TTF da Microsoft:   
  
[http://mscorefonts2.sourceforge.net/](http://mscorefonts2.sourceforge.net/ "Follow link")

[https://en.wikipedia.org/wiki/Core\_fonts\_for\_the\_Web](https://en.wikipedia.org/wiki/Core_fonts_for_the_Web "Follow link")

| As fontes são: |
| --- |
| Andale Mono |
| Arial Black |
| Arial (Bold, Italic, Bold Italic) |
| Comic Sans MS (Bold) |
| Courier New (Bold, Italic, Bold Italic) |
| Georgia (Bold, Italic, Bold Italic) |
| Impact |
| Times New Roman (Bold, Italic, Bold Italic) |
| Trebuchet (Bold, Italic, Bold Italic) |
| Verdana (Bold, Italic, Bold Italic) |
| Webdings |

Este pacote ao ser instalado, exibe um acordo de licença do usuário final (EULA). Após clicar em Ok, a EULA é aceita pelo usuário e os referidos fontes podem ser consumidos de maneira legal.
