---
content_hash: ab27afe429f46359b9109fc77b7265bdf896d36b8c5f28a60ae646ff27ae9dff
fetched_at: '2026-06-29T00:11:45.809185+00:00'
page_id: '821582226'
product: rm
source: tdn-rm
title: Firebase Crashlytics - Logs de erros do aplicativo
type: documentation
url: https://tdn.totvs.com/display/LRM/Firebase+Crashlytics+-+Logs+de+erros+do+aplicativo
version: 15
---

## **CONTEÚDO**

1. **VISÃO GERAL**
2. **TELA**
3. **DESCRIÇÃO DE FUNCIONAMENTO**

## **01. VISÃO GERAL**

O Meu eduCONNECT integrou o Firebase Crashlytics como parte de seu processo de desenvolvimento e manutenção.  
Esta ferramenta permite a identificação e solução proativa de problemas que possam impactar a experiência do usuário, garantindo assim um desempenho consistente e confiável.  
Erros no aplicativo poderão ser monitorados com parâmetros e filtros configuráveis.  
Para maiores informações sobre o Firebase Crashlytics clique [aqui](https://firebase.google.com/docs/crashlytics?hl=pt-br).

## **02. TELA**

| Visão geral - Console do Firebase |
| --- |
| Painel - Firebase Crashlytics |

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Firebase Remote Config | Configurações remotas do aplicativo |
| Firebase Analytics | Análise do comportamento dos usuários do aplicativo |

## **03.** **DESCRIÇÃO DE FUNCIONAMENTO**

**Acessar o console de gerenciamento do Firebase:**

Deverá ser acessado o console de gerenciamento do Firebase e selecionado o projeto a ser analisado:   
<https://console.firebase.google.com/>

**Habilitar o funcionamento do Crashlytics nas configurações remotas do aplicativo (Firebase Remote Config)**

Para que os erros do aplicativo sejam listados pelo Firebase Crashlytics, o mesmo deverá ter a respectiva configuração remota habilitada no Firebase Remote Config.

Para habilitar o funcionamento do Crashlytics, a opção "**enable\_crashlytics**" do Firebase Remote Config deverá estar setada para "**true**", conforme abaixo:

**Observação:**

Caso tenha que alterar o valor de "**enable\_crashlytics**", deverá ser alterada também a data de sincronismo "**sync\_date**" e as alterações publicadas.  
Caso tenha dúvidas na utilização do Remote Config, clique .  
Após habilitar o Crashlytics nas configurações remotas, o log de erros começará a ser mostrado.

Ao clicar na respectiva linha referente ao log de erro, será exibido um detalhamento do log com a pilha de chamadas por padrão (Stacktrace):

**Detalhamento mostrando algumas chaves com possibilidade de se consultar o GUID e o código do usuário:**

**Mais informações de registros de log:**

**Dados mais detalhados sobre o dispositivo que emitiu o erro e o usuário:**

**Dados poderão ser filtrados ao clicar no botão de filtros:**

**Erros conhecidos poderão ser pesquisados:**

Atenção

Após habilitar o Crashlytics nas configurações remotas (Firebase Remote Config), existe um tempo de 12 horas para que as alterações surtam efeito.
