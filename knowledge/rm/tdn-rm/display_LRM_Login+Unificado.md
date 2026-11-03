---
content_hash: c06dcb52a527408dd48968230b191f0f98c616c32d7dfdeb4656934067620958
fetched_at: '2026-06-29T00:06:25.437588+00:00'
page_id: '224397390'
product: rm
source: tdn-rm
title: Login Unificado
type: documentation
url: https://tdn.totvs.com/display/LRM/Login+Unificado
version: 134
---

# Experiência 1 - Login Unificado ( Single Sign-On )

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 11.82.42 , 12.1.0 |
| **Ambiente:** | MDI | RM.exe |
| **Passo a passo:** | **Objetivo:**  O Objetivo deste documento é ensinar a configurar o login unificado e explicar como funciona.  **Introdução:**  O Login Unificado é uma forma de autenticação no sistema utilizando as credenciais de outro aplicativo como referência. Atenção A ligação entre os usuários do IDENTITY e do RM é realizada através do e-mail.  Exemplo:  Usuário do Identity : [mestre@totvs.com.br](mailto:mestre@totvs.com.br)  Usuário no RM deve possuir o e-mail: [mestre@totvs.com.br](mailto:mestre@totvs.com.br)  **Como Configurar:**  Para configurar o login unificado é necessário executar a funcionalidade "Fluig OnClick". Para mais informações acesse [Fluig OnClick](http://tdn.totvs.com/x/3b5bDQ).  Após realizar a configuração, é necessário escolher qual o tipo de integração que deseja utilizar, pois o Fluig OnClick configura por padrão a opção de integração "Opcional".  Para mais informações sobre tipo de integração acesso o link [Tipos de Integração](http://tdn.totvs.com/x/AMlbDQ).  **Funcionamento:**  **800600** |
| **Observações:** | Observação Em casos de emergência que é necessário desativar a integração através do RM e o tipo de integração estiver como **Obrigatória** ou **Somente SSO Obrigatória**. É necessário adicionar à execução do RM o argumento /admin, onde será possível logar no RM com um usuário supervisor. |

divs
