---
content_hash: 3e7482f9c7ccabe21df051e2a82a2ef76efb9efc429cbf1a9022f7114310ce46
fetched_at: '2026-06-29T00:08:15.489374+00:00'
page_id: '244741802'
product: rm
source: tdn-rm
title: Recaptcha
type: documentation
url: https://tdn.totvs.com/display/LRM/Recaptcha
version: 7
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Informar sobre a utilização do recaptcha na execução do Mashups Totvs.

# Execução:

---

        Alguns sites consumidos pelo serviço de Mashup utilizam um recurso de controle do Google chamado Recaptcha. O recaptcha é utilizado para que o site consiga limitar o acesso a seu conteúdo para que somente pessoas "reais" consigam acessar determinadas informações. Para isso ele utiliza artifícios baseados em imagens que são apresentadas ao usuário que deverá identificar determinadas condições.

        Quando um site que utiliza este recurso for consumido pelo Mashup, serão apresentadas imagens que deverão ser informadas pelo usuário através do clique sobre a imagem exposta pelo Mashup.

        Por exemplo:

        Neste caso, os quadros que possuem placas de rua deverão ser selecionados conforme apresentado na imagem e em seguida o processo deverá ser avançado. esse processo poderá se repetir indeterminadamente.

        Como o mecanismo do RECAPTCHA pode alterar as imagens após elas serem informadas, o Mashup irá continuar a exibir novamente a imagem até que o parâmetro da imagem não seja mais informado. Ou seja, quando não houver mais nenhuma imagem correspondente a pergunta ou que todas as imagens selecionadas sejam referentes a mesma.

        Exemplo:

        Neste caso, quando não existir mais nenhum quadro que possua "carros" o processo poderá ser avançado. Caso as imagens não sejam validadas corretamente um novo recaptcha será exibido.

Importante

        Quando existe um usuário logado no browser "Google Chrome", as ações executadas no recaptcha do Mashup tendem a ser mais rápidas, entretanto por se tratar de um ferramenta externa, não temos o controle da quantidade de vezes em que o recaptcha será exigido ao usuário. Abaixo, um exemplo de usuário logado ao browser "Google Chrome". Para mais detalhes de como logar no browser contate o suporte do browser ou clique no link a seguir: [Fazer login ou sair do Google Chrome](https://support.google.com/chrome/answer/185277?co=GENIE.Platform%3DDesktop&hl=pt-BR)

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Recaptcha

falsefalse

**Status:** Finalizado

false

**Data:** 22/01/2018

false

**Autores:**
