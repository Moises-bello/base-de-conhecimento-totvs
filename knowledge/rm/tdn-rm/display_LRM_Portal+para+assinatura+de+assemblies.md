---
content_hash: f73149a94bf0708c48106411c1489dad903092676b7419735a5a949e0bab0921
fetched_at: '2026-06-29T00:08:36.110142+00:00'
page_id: '284355666'
product: rm
source: tdn-rm
title: Portal para assinatura de assemblies
type: documentation
url: https://tdn.totvs.com/display/LRM/Portal+para+assinatura+de+assemblies
version: 6
---

Este manual tem como objetivo auxiliar no processo de assinatura digital de pacotes de assemblies TOTVS (DLLs e EXEs).

Segue abaixo o passo a passo do processo de assinatura via portal:

1. Acesse o portal <http://engenhariabh.bh01.local/TotvsSign/> ou [http://engenhariabh/TotvsSign/](http://engenhariabh.bh01.local/TotvsSign/) ou [http://10.171.32.33/TotvsSign/](http://10.171.32.33/TotvsSign/Account/Login?ReturnUrl=%2FTotvsSign%2FSign)
2. Faça o seu registro através do link "Registrar", conforme abaixo:
3. Você receberá um link para ativação do seu registro. Após a confirmação, continue nos passos abaixo.
4. Reúna todos os arquivos que deseja assinar, lembrando que todos os arquivos precisam ter a extensão .exe ou .dll.
5. Compacte os arquivos, obtendo assim um único arquivo zip.
6. Faça o login no portal, conforme imagem abaixo:
7. Acesse o menu "Assinaturas" e em seguida "Solicitar novo pacote", conforme abaixo:
8. Envie o pacote compactado e informe todos os campos solicitados, conforme abaixo:
9. Ao concluir o portal te redirecionará para a tela de assinaturas novamente. Nessa tela você visualiza todas as suas solicitações e seus respectivos dados, incluindo o status atual do processo.
10. Quando o status estiver como "Success", basta fazer o download das DLLs, através do link "Download".
11. Para visualizar a assinatura dos arquivos, basta descompactar o pacote baixado e acessar as propriedades de qualquer arquivo, conforme abaixo:
12. Pronto, seu pacote pode ser distribuído.

**Lembre-se que o envio de DLLs avulsas para o cliente podem prejudicar seu ambiente, logo este processo deve ser feito com cautela em qualquer situação, principalmente quando o cliente utilizar Deploy Granular.**

**Atc,**

**Framework.**
