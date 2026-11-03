---
content_hash: 7688f65a60f942987e23548866b86fd09fead8ed44602665b9a39d5a52b6c837
fetched_at: '2026-06-28T21:35:21.799492+00:00'
page_id: '234455771'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Importar e exportar páginas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=234455771
version: 52
---

.\*ndice

# Falando de importar e exportar páginas...

---

Por meio deste recurso é possível exportar uma página ou um conjunto de páginas que podem ser, posteriormente importadas no TOTVS Fluig Plataforma ou exportadas de um [servidor](http://tdn.totvs.com/x/jYtJF) para o outro sem a necessidade de baixar arquivos.

Com esse recurso é possível, por exemplo, a estruturação de uma página - com *widgets*, segurança, *layout* entre outros - e a realização de testes, verificando as funcionalidades e a navegação em um ambiente de testes. Posteriormente, exportando toda a estrutura do ambiente de testes, é possível replicá-la no ambiente de produção por meio da importação, o que diminui o esforço e, consequentemente, o custo, visto que não será necessário replicar tudo o que foi criado no ambiente de testes manualmente para o ambiente oficial.

Para exportação, são apresentadas somente as páginas editáveis em uma estrutura no formato de árvore na qual elas podem ser assinaladas. Ao assinalar uma página filha, a página pai é automaticamente assinalada também, garantindo assim, que seja mantida a estrutura original na exportação. O mesmo ocorre ao assinalar uma página pai, suas filhas também serão assinaladas automaticamente e exportadas.

Sempre será exportada a última versão da página selecionada.

Para a exportação automática de páginas entre servidores é necessário criar anteriormente uma chave Oauth e um usuário Aplicativo no servidor de destino, para que seja possível realizar o cadastro deste servidor na plataforma. Saiba mais em [Servidores.](http://tdn.totvs.com/x/jYtJF)

Ao realizar a importação de uma ou mais páginas, as mesmas são publicadas automaticamente logo após a importação, ou seja, já estarão visíveis aos demais usuários.

Importante!

Uma página somente pode ser exportada e importada entre ambientes do TOTVS Fluig que estejam na mesma atualização.

## Exportar páginas via *download*

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Personalização**.

**03**. Clique em  **Importar e exportar páginas**.

**04.** Na estrutura apresentada, assinale as páginas que serão exportadas.

#f2f2f2#f2f2f2

São apresentadas apenas as páginas editáveis. Páginas pais e filhas são sempre exportadas juntas para garantir que a estrutura original seja mantida, não é possível exportar apenas uma página pai ou apenas uma página filha.

Imagens do ECM adicionadas em páginas a partir do *widget* Editor de conteúdo não serão exportadas.

**05.** Clique em**Exportar páginas.**

**06.** Selecione ***Download* das páginas/artefatos.**

**07.** Clique em **Exportar**.

#f2f2f2#f2f2f2

Será gerado um arquivo compactado contendo os itens solicitados na exportação.

## Importar páginas

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Personalização**.

**03**. Clique em  **Importar e exportar páginas**.

**04.** Clique em **Importar**.

**05.** Selecione o arquivo compactado que contém as páginas a serem importadas.

**06.** Clique em **Confirmar Importação**.

Importante!

O procedimento de importar páginas é necessário apenas para exportações via *download*.

## Exportar páginas via servidores

---

https://www.youtube.com/watch?v=GEpWD61D4wwtruevideo-filledAssista ao vídeo#0897E9INLINE

800450

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Personalização**.

**03**. Clique em  **Importar e exportar páginas**.

**04.** Na estrutura apresentada, assinale as páginas que serão exportadas.

#f2f2f2#f2f2f2

São apresentadas apenas as páginas editáveis. Páginas pais e filhas são sempre exportadas juntas para garantir que a estrutura original seja mantida e não é possível exportá-las de forma independente.

Imagens do ECM adicionadas em páginas a partir do *widget* Editor de conteúdo não serão exportadas.

**05.** Clique em **Exportar páginas.**

**06.** Selecione **Enviar para outro Servidor.**

**07.** Selecione o servidor desejado.

#f2f2f2#f2f2f2

Os servidores precisam ser previamente cadastrados na plataforma para aparecerem na lista. Para saber mais sobre o cadastro de servidores confira a [documentação](http://tdn.totvs.com/x/jYtJF).

**08.** Clique em **Exportar.**

#f2f2f2#f2f2f2

Ao clicar em **Exportar**, as páginas selecionadas anteriormente são enviadas para publicação no servidor de destino.

Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
