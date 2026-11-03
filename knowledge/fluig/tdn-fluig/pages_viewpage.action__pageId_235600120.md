---
content_hash: 5b640aef166965615c7ab0736fb93017e2a3ca5652093013b5b1f0dffd46195a
fetched_at: '2026-06-28T21:35:22.455294+00:00'
page_id: '235600120'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Configurar widget Slideshow
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235600120
version: 16
---

.\*ndice

# Falando de configurar *widget Slideshow*...

---

A configuração do *widget Slideshow* permite definir o local de onde serão exibidas as imagens e as configurações necessárias para a integração.

Esse *widget* pode ser visualizado no aplicativo móvel da plataforma.

Importante!

Para que esse *widget* seja exibido na lista de *widgets* disponíveis para páginas, primeiramente é necessário obter o artefato Kit Intranet do diretório [Git](https://git.fluig.com/projects/SAMPLES/repos/kit-intranet/browse). Depois, é necessário importar o artefato em . Após efetuados esses procedimentos, o *widget* estará disponível para utilização.

Mais informações podem ser obtidas em [Kit Intranet](http://tdn.totvs.com/x/nbBICw).

## Configurar *widget* *Slideshow*

---

**01.** Depois de incluir o *widget* na página em edição, defina as configurações desejadas para ele.

#f2f2f2#f2f2f2

As informações solicitadas são:

**Este *widget* se integra com**Tipo de integração a partir do qual o widget buscará as imagens para exibição. As opções disponíveis são:

* **Instagram**: quando selecionada, determina que serão exibidas imagens de uma conta do Instagram. Consulte a documentação [Configurar Instagram no widget Slideshow](http://tdn.totvs.com/x/zGNKE) para obter informações sobre como realizar a integração;

* **Uma pasta**: quando selecionada, determina que serão exibidas imagens de uma pasta da plataforma.

**Estender imagens**Quando assinalada, determina que as imagens irão ocupar toda a área do *widget*. Dependendo da resolução da imagem, esta opção pode deixar a exibição distorcida. A altura máxima suportada é de 400 *pixels*, enquanto a largura dependerá da tela do monitor do usuário.

**Redimensionar**Quando assinalada, Enquadra imagens com tamanho maior que o disponível no Slideshow para evitar que sejam exibidas apenas parcialmente no *widget*.

**Gerar novo token de acesso**Quando acionado, redireciona o usuário para o portal do desenvolvedor do Instagram, onde o procedimento de geração de token deve ser realizado. Consulte a documentação [Configurar Instagram no widget Slideshow](http://tdn.totvs.com/x/zGNKE) para obter informações sobre como realizar a integração.

**Diretório dentro do Fluig**Local da plataforma onde se encontra a pasta da qual as imagens serão exibidas. Acionar **Diretório ECM** para selecionar o local.

**Mostrar título nas imagens**Quando assinalado, determina que o nome de cada imagem também será exibido.

**02.** Clique em **Salvar**.

#f2f2f2#f2f2f2

Para que as alterações realizadas na configuração do *widget* sejam apresentadas aos usuários, é necessário publicar a página na qual ele está localizado. Mais informações sobre a publicação de páginas podem ser obtidas em  e .

Fique atento!

Esta documentação é válida a partir da **atualização 1.5.10**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
