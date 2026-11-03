---
content_hash: 9d50850399e578c02287dd6ce7016ba0bea1d47e4510fd5258ee76a1b9fee60e
fetched_at: '2026-06-28T21:35:22.446154+00:00'
page_id: '235600036'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Configurar widget Aniversariantes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235600036
version: 17
---

.\*ndice

# Falando de configurar *widget* Aniversariantes...

---

A configuração do *widget* Aniversariantes permite definir o local de onde serão exibidos os aniversariantes e as configurações necessárias para a integração, bem como se deve ou não ser exibido no aplicativo móvel.

Por padrão o *widget* apresenta dois aniversariantes e carrega mais dois cada vez que o botão **Carregar mais** é acionado. Apenas aniversariantes do mês atual são exibidos.

Esse *widget* pode ser visualizado no aplicativo móvel da plataforma.

Importante!

Para que esse *widget* seja exibido na lista de *widgets* disponíveis para páginas, primeiramente é necessário obter o artefato Kit Intranet do diretório [Git](https://git.fluig.com/projects/SAMPLES/repos/kit-intranet/browse). Depois, é necessário importar o artefato em . Após efetuados esses procedimentos, o *widget* estará disponível para utilização.

Mais informações podem ser obtidas em [Kit Intranet](http://tdn.totvs.com/x/nbBICw).

## Configurar *widget* Aniversariantes

---

**01.** Depois de incluir o *widget* na página em edição, defina as configurações desejadas para ele.

#f2f2f2#f2f2f2

As informações solicitadas são:

**Habilitar no aplicativo *mobile***Quando acionado, habilita/desabilita a exibição do *widget* no aplicativo móvel. Esse ícone está localizado no canto superior direito do *widget*, ao lado de **Editar permissão**.

**Este *widget* se integra com**Tipo de integração a partir do qual o widget buscará os aniversariantes para exibição. As opções disponíveis são:

* **Um formulário**: quando selecionada, determina que serão exibidos os aniversariantes provenientes de um formulário integrado ao *widget*. Mais informações podem ser obtidas em [Integrando *widget* com formulários/*datasets*](http://tdn.totvs.com/pages/releaseview.action?pageId=185739337);

* **RM**: quando selecionada, determina que serão exibidos os aniversariantes provenientes do TOTVS RM.

***Link* do servidor**Endereço IP e porta do serviço TBC do TOTVS RM – no formato [http://host:porta](http://hostporta) – do qual os aniversariantes serão exibidos. Esse campo somente é apresentado quando a opção de integração escolhida for "RM".

***Login***Login de acesso ao serviço no TOTVS RM. Esse campo somente é apresentado quando a opção de integração escolhida for "RM".

**Senha**Senha de acesso ao serviço no TOTVS RM. Esse campo somente é apresentado quando a opção de integração escolhida for "RM".

**02.** Clique em **Salvar**.

Para que as alterações realizadas na configuração do *widget* sejam apresentadas aos usuários, é necessário publicar a página na qual ele está localizado. Mais informações sobre a publicação de páginas podem ser obtidas em  e .

Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
