---
content_hash: 71311755498ce9e1a21b52b00487aa89643c48384e72042635bf14e248e1bce1
fetched_at: '2026-06-29T00:08:57.679544+00:00'
page_id: '354466801'
product: rm
source: tdn-rm
title: Criação de WebParts RM Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=354466801
version: 27
---

# Neste módulo iremos mostrar a correta parametrização para criar WebPart no Portal RM

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 12.1.18 e Superiores |
| **Ocorrência:** | Configurando WebParts no Portal RM |
| **Ambiente:** | RM Portal - Nova MDI |
| **Passo a passo:** | **1 - Permissão de Acesso** Para que procedimento possa ser realizado usuário deve ter as seguintes permissões no sistema  **1.1 - Através da MDI acessar o contesto “Serviços Globais”;**     ---   **1.2 - Acessar o menu “Perfis”;**     ---   **1.3 - Selecionar o contexto “Gestão de Conteúdo” e editar perfil associado ao usuário;**     ---   **1.4 - Acessar a aba “Acesso a Menus” e liberar o menu “06.02.07 – Aqui você poderá administrar as WebParts Disponíveis para Personalização”;**     ---   **2 - Cadastro de Usuário para criação do WebPart**  Um usuário (vamos considerar que seja o "mestre") que será o responsável por definir as configurações dos WebParts, ou seja, o "mestre" tem que ter um perfil que permita configurar os WebParts.  Edite o arquivo "Web.config" que fica no diretório "C:\totvs\CorporeRM\Corpore.Net", e insira as linhas em negrito do texto na TAG "webParts", que ficará assim:    <webParts>  <personalization>  **<authorization>**  **<allow users="mestre" verbs="enterSharedScope" />**  **</authorization>**  <providers>  <add name="PrtAspNetTextFilePersonalizationProvider" type="RM.Prt.Utils.TextFilePersonalizationProvider, RM.Prt.Utils.Client"/>  </providers>  </personalization>  </webParts> Observação **OBS:** Isto determina que o usuário "mestre", neste caso, será o responsável por definir as configurações de WebParts que serão utilizadas por todos os outros usuários.   ---   **3 - Cadastro WebPart**  **3.1 - Através do Portal acessar o menu “Portal”**       ---   **3.2 - Através do menu portal acessar a opção “Portal | Administrar”**     ---   **3.3 - Acessar a opção “WebParts” e adicionar novo registro**      ---  **3.3.1 - Na aba “Identificação” preencher informações conforme WebPart da empresa**     ---   **3.3.2 - Na aba “Filtro” preencher informações para definir quais usuários da empresa serão apresentados as noticias**   Observação **OBS: Para cadastro de localidade deve sempre utilizar o ultimo registro da arvore de cadastro**   ---   **3.3.3 - Preenchendo todas as informações basta salvar e fechar registro**     ---   **3.4 - Acessar a opção “Portal | Principal”**     ---   **3.4.1 - Selecionar a opção “Personalizar”**   ---   **3.4.2 - Selecionar a WebParts que foi criada, indicar local na página que será apresentado e clicar em adicionar.**    **Após adicionar noticia será apresentada no local da página indicado.**   ---   **3.4.3 - Selecionar a opção “Fechar e salvar”**   ---   **4 - Permissão do Web Part Criado**  **Após cadastro da Web Part será criado o menu nas permissões do sistema. O mesmo deve ser liberado para que seja apresentado para todos usuários**  **4.1 -** **Selecionar o contexto “Gestão de Conteúdo” e editar perfil associado à usuário**     ---   **4.2 -** **Acessar a aba “Acesso a Menus” e liberar o menu “05.02.01.01 – Visualizar Web Parts”**      ---   **5 – Aplicação no portal**  **Com registro salvo basta acessar a opção “Portal | Página Principal” que noticia será apresentada para usuários**      **Antes do registro salvo**  **Depois do Registro Salvo**    **6 – Web Part Preenchimento Manual**  **Existe também a possibilidade de configurar um controle customizado, utilizando a WebPart do tipo Preenchimento Manual****, caso os controles padrões do sistema não atenderem as necessidades. Neste caso indicamos entrar em contato com Fábrica de Software RM e solicitar um orçamento.** |
|  |  |
