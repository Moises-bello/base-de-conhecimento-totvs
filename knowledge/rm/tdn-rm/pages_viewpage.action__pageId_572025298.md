---
content_hash: e5ae69055b5e52b78dff587e8707fdfe98dfdcac578d02a545db01209266a537
fetched_at: '2026-06-29T00:10:52.359417+00:00'
page_id: '572025298'
product: rm
source: tdn-rm
title: Acelerador de Implantação ORCECERTO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=572025298
version: 7
---

Esta funcionalidade do TOTVS Construção Obras e Projetos possibilita que a configuração do ambiente de Integração com a base ORCECERTO seja realizada de forma simples e rápida.

Existem duas formas de acesso ao Acelerador de Implantação:

* Através do menu principal na Aba Projetos/Grupo Parâmetros/Aceleradores de Implantação/Base ORCECERTO:

  + Não é necessário estar no contexto de um projeto para utilizar a funcionalidade.

* Através do próprio processo de "Integrar com base ORCECERTO":
  + A partir daqui o Acelerador será exibido somente se o Login e Senha da ORCECERTO, não estiverem configurados.

Para utilizar a funcionalidade é necessário conceder permissão de acesso ao usuário:

**Detalhes do processo**

* Antes de iniciar o acelerador, serão consultados, na ORCECERTO, quais CNPJs do cadastro de Filial têm licença para utilização do serviço e caso o retorno apresente mais de um CNPJ, o usuário poderá selecionar um deles na tela, e caso tenha apenas um, o mesmo será informado automaticamente:
  + ou
* São três opções que o acelerador disponibiliza para que a configuração possa ser feita:
  + **"Recebeu o usuário e a senha da ORCECERTO?":**  
    - A senha e login serão configurados (incluídos ou alterados) somente na base do TOTVS Construção Obras e Projetos;
    - Apenas o campo para informar a senha estará disponível.
  + **"Vai alterar a senha da ORCECERTO"?:**
    - A senha e login serão alterados na ORCECERTO e na base do TOTVS Construção Obras e Projetos.
    - Os campos para informar a senha atual, a nova senha e confirmar a senha estarão disponíveis.
    - Essa opção somente estará disponível se no TOTVS Construção Obras e Projetos as configurações já tiverem sido feitas.
* Se a configuração for realizada com sucesso, a seguinte tela será exibida:  

  + Clicando na imagem  é possível ver o vídeo da "Integração TOTVS Construção Obras e Projetos com a ORCECERTO" presente no Youtube;
  + A opção "Deseja abrir a Integração com Base ORCECERTO?" somente estará disponível se o acelerador for aberto do menu principal.
* Se algum erro acontecer ao processar a configuração solicitada, o mesmo será apresentado ao final da execução:
* Se a validação de licenças da ORCECERTO não retornar nenhuma assinatura, ao invés de abrir o acelerador, a tela do banner sugerindo a assinatura do pacote ORCECERTO será aberta, onde a partir dela, o usuário poderá ir até a loja da TOTVS e adquirir um dos pacotes ou visitar tutoriais sobre o processo:
