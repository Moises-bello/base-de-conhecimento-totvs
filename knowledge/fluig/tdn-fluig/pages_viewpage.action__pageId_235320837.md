---
content_hash: f9a1637d24551ba35775e21e95fe2ba900625479aeeac9fc2b61863a20e78668
fetched_at: '2026-06-28T21:35:22.107782+00:00'
page_id: '235320837'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Controle de cotas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235320837
version: 32
---

.\*ndice

# Falando de controle de cotas...

---

Esse recurso permite definir um tamanho padrão de armazenamento que as pastas da plataforma podem ter, bem como para a pasta particular dos usuários. E vem desabilitado por padrão.

As cotas definidas aqui são padrão. Porém, é possível definir valores específicos por pasta e por usuário. Para pastas, é possível definir um valor para cada uma alterando suas propriedades. Nesse caso, as cotas seguem a hierarquia de pastas, ou seja, as pastas filhas de uma pasta herdarão sua cota e todas as publicações efetuadas, tanto na pasta pai quanto nas filhas, consomem espaço da cota da pasta pai. Para atribuir cotas específicas para as pastas filhas, é necessário que a cota da pasta pai seja ilimitada (valor 0), assim como para atribuir cota de armazenamento para uma pasta que possui filhas com cota definida, é necessário alterar a cota das filhas para ilimitada. Para a pasta Meus documentos também é possível definir um valor diferente do padrão para cada usuário diretamente no cadastro de .

É possível definir se a publicação será ou não bloqueada quando a pasta atingir seu tamanho máximo permitido.

Também é possível visualizar um relatório contendo informações sobre cada pasta, sua cota, o total utilizado e o total disponível para utilização.

## Habilitar controle de cotas

---

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Parâmetros técnicos**.

**03**. Clique em  **Controle de cotas**.

**04.** Defina as informações solicitadas.

#f2f2f2#f2f2f2

As informações solicitadas são:

**Habilitar controle de cotas**  
Quando habilitado, determina que é possível definir um limite de tamanho para as pastas. Nesse caso, o botão é apresentado com o indicativo **ON**, informando que o recurso está ativo. Quando acionado para desabilitar o recurso, o botão é apresentado com o indicativo **OFF**, informando que o recurso está desabilitado.

**Bloquear publicação ao atingir o limite de cota**  
Quando assinalado, determina que a publicação na pasta será bloqueada quando ela atingir o seu tamanho máximo pré-definido.

**Cota padrão pasta (0 para ilimitado)**  
Tamanho máximo padrão que as pastas da plataforma podem ter. Esse valor pode ser alterado nas propriedades de cada pasta, sendo possível definir um valor específico para cada uma. Quando uma pasta possui pastas filhas, essas herdarão o seu limite de tamanho e as publicações efetuadas, tanto na pasta pai quanto nas filhas, consomem espaço da cota da pasta pai.  
Para atribuir cotas específicas para as pastas filhas, é necessário que a cota da pasta pai seja ilimitada (valor 0), assim como para atribuir cota de armazenamento para uma pasta que possui filhas com cota definida, é necessário alterar a cota das filhas para ilimitada.

**Cota padrão meus documentos (0 para ilimitado)**  
Tamanho máximo padrão permitido para a pasta pessoal – Meus documentos – dos usuários. Esse valor pode ser alterado para um valor específico para cada usuário no cadastro de usuários. A configuração do controle de cotas feita na pasta Meus Documentos vale automaticamente para as subpastas criadas pelo próprio usuário.

**05.** Clique em **Salvar**.

#f2f2f2#f2f2f2

Após habilitar o controle de cotas, caso alguma pasta esteja ocupando tamanho próximo ou estourando o limite definido, quem administra a plataforma irá receber uma notificação referente a cada pasta nessa situação, desde que a notificação esteja habilitada nas .

trueimageVeja a imagem#0897E9INLINE

## Ver cotas utilizadas

---

Para efetuar essa ação, é necessário que o controle de cotas esteja ativo.

**01.** No menu principal, clique em  **Painel de controle**.

**02**. Localize o agrupador **Parâmetros técnicos**.

**03**. Clique em  **Controle de cotas**.

**04**. Clique em **Visualizar relatório**.

#f2f2f2#f2f2f2

Uma nova tela será apresentada, trazendo a cota e o espaço disponível e utilizado das pastas da plataforma.

trueimageVeja a imagem#0897E9INLINE

É importante salientar que o relatório apresentado não leva em consideração o espaço utilizado pelos itens (pastas e documentos) que estão na lixeira dos usuários. E também não considera a pasta Meus documentos.

Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
