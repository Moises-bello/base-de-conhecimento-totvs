---
content_hash: a36e39b458c8c43aa6c7829f37f6c26415ebf2b90bf6ca3a8814193dbd28043c
fetched_at: '2026-06-29T00:10:58.914067+00:00'
page_id: '607590852'
product: rm
source: tdn-rm
title: TOTVS Assinatura Eletrônica - Processo de Integração de relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=607590852
version: 8
---

Através do no menu “Assinatura eletrônica | Integração | Processo de integração de relatórios” será realizada a execução da geração de um grupo de relatório e sua integração com o sistema TOTVS Assinatura Eletrônica.

Nesta tela o usuário poderá gravar perfis para geração, facilitando assim o preenchimento dos campos necessários para execução.

**Seleção de funcionários**

O usuário poderá realizar a seleção de funcionários com base na quebra de seção ou através de seleção de funcionários de acordo com situações, tipos de funcionários ou forma de recebimentos.

**Seleção de relatório**

O usuário deverá selecionar um grupo de relatório parametrizado através do cadastro de “Tipos de relatórios”, sendo esse cadastro prévio responsável para que o processo possa identificar as informações a serem processadas.

Caso o grupo de relatório selecionado possua mais de um relatório configurado, cada relatório será considerado como um documento a ser integrado.

Grupos disponíveis

Somente serão exibidos os grupos de relatórios que estiverem ativos.

**Regras para geração e envio dos relatórios**

Considerar regras do cadastro do tipo de relatório

Essa é a opção padrão para geração do relatório, onde serão consideradas as regras parametrizadas para o relatório, como data do aviso ou data do pagamento.

A opção **Enviar sob demanda (disparo manual)** permite que as regras específicas do tipo de relatório (Aviso de férias ou Recibo de Férias) sejam desconsideradas sendo considerada a seleção realizada na tela do processo.

Enviar sob demanda está associada a regra Não validar essa informação no cadastro de tipo de relatório.

**Período -**Ao selecionar essa opção o usuário pode definir um intervalo de datas para localização dos funcionários, sendo selecionados os funcionários que possuírem férias cadastradas que atendam o critério de data de pagamento para o recibo de férias e data do aviso para o aviso de férias.

**Não integrar documento caso o mesmo já tenha sido integrado anteriormente (evita duplicidade)**

Essa opção permite que um mesmo documento não seja integrado mais de uma vez para o mesmo funcionário. Ao ser executada a validação o sistema identificará se para o Grupo de Relatório selecionado o funcionário já possui um documento integrado com um dos seguintes status: Pendente de assinatura, Assinado Parcialmente, Assinado, Pendente de Aprovação ou Erro na aprovação, como mesma chave (para aviso de férias chave de identificação das férias, para o tipo outros Coligada e Chapa).

Ao avançar a etapa, será exibida uma prévia dos funcionários que serão considerados para a integração. O usuário poderá selecionar um ou mais registros específicos para o processamento. Caso não seja selecionado nenhum registro serão considerados todos os registros.

Importante

1 - Caso o processo seja agendado para execução recorrente não devem ser selecionados registros na grade de seleção, pois de acordo com a data de geração a seleção retornará registros diferentes.

2 – Atualmente o recurso de job recorrente não está habilitado para realizar a integração automática.

Ao clicar em “Executar” será exibida uma tela para que o usuário realize o login no sistema TOTVS Assinatura Eletrônica, responsável por criar um canal de comunicação para realização da integração. Esse login será solicitado a primeira vez e terá uma validade de 8 horas. Caso o processo seja executado novamente nesse intervalo o sistema validará se a autenticação não expirou e não solicitará novo login, caso tenha expirado ou não tenha sido realizado ele solicitará novo login.

### Vídeo

80%80%
