---
content_hash: 832b08fcd64adb3a7e5efdc6ad6c2b6e7013bbd9c43b260ca32d760945300f09
fetched_at: '2026-06-28T21:35:22.138222+00:00'
page_id: '235325440'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Recortar e colar pasta ou documento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235325440
version: 27
---

# Falando de recortar e colar pasta ou documento...

---

A plataforma permite que documentos sejam movidos de uma pasta para outra independentemente do volume relacionado às pastas origem e destino. Porém, a pasta destino não pode ser uma que possui aprovadores.

Já a movimentação de subpastas e formulários é possível somente quando o volume relacionado à pasta destino é idêntico ao volume relacionado à pasta/formulário origem ou quando a pasta origem é a principal (*root*) de um volume. Essa restrição é necessária porque este recurso transfere fisicamente os arquivos para o volume da pasta destino e, em casos extremos de grande quantidade de arquivos ou arquivos muito grandes, o tempo para transferência pode se esgotar (*time out*), ocasionando inconsistências na movimentação.

A plataforma não permite mover pastas com controle de cotas pois, ao habilitar esse controle, é possível definir um valor de cota para cada pasta, e ao mover poderiam ser geradas inconsistências, caso o usuário tente mover uma pasta com um valor maior para uma com valor menor.

## Recortar e colar pasta ou documento

---

Para que a movimentação de uma pasta seja permitida, a pasta destino não pode ter aprovação configurada. O usuário precisa ter permissão de gravação na pasta de origem e na pasta de destino.

******[Visualize o passo a passo](http://tdn.totvs.com/download/attachments/235325440/recortar%20e%20colar%20documento.gif?version=1&modificationDate=1519153630688&api=v2)******

****01.****Acesse o local onde as pastas e documentos a serem movimentados estão publicados. 

**02.** Selecione as pastas e documentos e clique na **Recortar**, localizado na barra de ações da parte superior esquerda da janela.

**03**. Acesse a pasta destino desejada para a qual será movido.

**04.** Clique em **Colar**, localizado na barra de ações da parte superior esquerda da janela.

#f2f2f2#f2f2f2Ao clicar em **Colar**, a pasta ou o documento é movido fisicamente para o local destino e uma mensagem confirmando a publicação é exibida.Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
