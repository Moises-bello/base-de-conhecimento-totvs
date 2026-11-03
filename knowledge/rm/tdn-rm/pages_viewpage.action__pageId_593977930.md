---
content_hash: 75a7332b3b2ebbd14eb004001e8512a06733f66b298846bf1da8808918012c70
fetched_at: '2026-06-29T00:10:57.014625+00:00'
page_id: '593977930'
product: rm
source: tdn-rm
title: Linkedin - Publicação em redes sociais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=593977930
version: 10
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

      Demonstrar como é realizada uma publicação nas redes sociais (Linkedin) através do RM.

ATENÇÃO

Conforme a documentação oficial do Linkedin, <https://docs.microsoft.com/en-us/linkedin/compliance/>, ocorreram alterações na utilização de sua integração que precisará de nova implementação. Portanto estaremos realizando avaliações e novos estudos, para possível nova integração com o serviço.

Estaremos realizando avaliações e novos estudos, para possível nova integração com o serviço, o que poderá acarretar em uma reestruturação da integração.

**02. EXEMPLO DE UTILIZAÇÃO**

      Em nosso exemplo vamos mandar uma mensagem teste para o Linkedin, para isso é necessário que seja acessado o site "<https://www.linkedin.com/developers/>".

      Após acessar sua conta, é necessário criar um no **App**, pois o utilizaremos para como meio de configuração posteriormente. Após criado, acessamos a página de **Products,** nela iremos adicionar as permissões que o App criado terá sobre a conta:

Agora selecionaremos os produtos **Share on LinkedIn**e **Sign In with LinkedIn**:

Agora acessamos a página **Auth**. Nela estão contidas as chaves "**Client ID**" e "**Client Secret**" que utilizaremos para integração com o RM.

      Em seguida é necessário realizar login no RM e acessar "Serviços Globais | Ambiente | Parâmetros | Parâmetros Globais" aba "Redes Sociais" e preencher os campos "**App Key do LinkedIn**" e "**S****ecret Key do****LinkedIn**" com as chaves geradas pelo App criado anteriormente.

      Feita a configuração, acesse "Gestão | Contas | Contas Individuais" e clique para incluir um novo registro, em seguida realize o preenchimentos dos campos obrigatórios e clicado em "**Obter Credenciais**".

      Após criação do cadastro, é necessário executar o processo "**Enviar Campanha de Comunicação Avulsa**", verifique que a mensagem encaminhada é cadastrada em seu mural (Conta do LinkedIn) corretamente.

OBS

A Url de Redirecionamento deverá ser a do google <https://www.google.com.br/>, porque ainda não foi exposto uma url de redirecionamento oficial.

Porém, caso o aplicativo seja para utilizar com o , nesta etapa, você deverá informar a as URI’s de redirecionamento do OAuth válidos.

Por exemplo:

* Para o portal do aluno de teste, nós poderíamos informar um endereço baseado em “localhost”, pois o Portal do Aluno de exemplo encontra-se na mesma máquina em que é feito a configuração (definimos o endereço: <http://localhost:8080/web/app/edu/PortalEducacional/>).
* Para o portal que está configurado com SSL informe o endereço correto de redirecionamento. (Neste exemplo usamos: <https://testeframe.com.br/RM12122/Login.aspx>)
