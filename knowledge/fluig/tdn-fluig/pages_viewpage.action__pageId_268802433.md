---
content_hash: dc79603c6f03a03d2327a3963acaacbe9f7c92e175b93b57e5243cde92ca9e18
fetched_at: '2026-06-28T21:35:24.041292+00:00'
page_id: '268802433'
product: fluig
source: tdn-fluig
title: BPM 081 - Como exportar processo do Eclipse/TDS de maneira que não apareça
  na lista "Sem Categoria" ?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268802433
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

# Ocorrência

Alterei a categoria do meu processo no Eclipse/TDS, mas ao exportar para o fluig ele aparece na categoria "Sem Categoria".

**Figura 1 - Configuração de nova categoria do diagrama**

**Figura 2 - Processo é exibido na categoria Sem Categoria**

# Causa

Quando o processo possui arquivos literais utilizados para tradução é necessário alterar a categoria também nesses arquivos.   
   
Se a categoria não for alterada em todos eles, as solicitações serão exibidas como **Sem Categoria** no fluig.

# Solução

Acesse o projeto no Eclipse/TDS e navegue pelo **Exportador de Projeto** até a pasta **literals**. Os arquivos possuem a extensão **.properties** com o nome do diagrama e o código do idioma de tradução, por exemplo:

* **diagrama\_en\_US.properties**
* **diagrama\_es.properties**
* **diagrama\_pt\_BR.properties**

Edite os arquivos e confira se a propriedade **process.category** está em branco como no exemplo da imagem abaixo. Se estiver você deve preenchê-la com a mesma categoria informada nas propriedades do diagrama.

Salve as alterações e exporte o projeto novamente.

Acesse as tela de Inicializar Solicitações para confirmar se o processo agora aparece na categoria desejada.

**Figura 3 - Arquivos literais sem categoria**

**Figura 4 - Alteração da categoria no arquivo literal**

**Figura 5 - Exibição do processo na categoria correta**

# Observações

Para saber mais sobre a tradução de processos e os arquivos literais acesse a documentação .
