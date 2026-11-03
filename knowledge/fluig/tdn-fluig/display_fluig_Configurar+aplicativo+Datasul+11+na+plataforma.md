---
content_hash: 669f278a232a576817143e4d1f42b83b0e9ed19660cc03132baede603d0e1573
fetched_at: '2026-06-28T21:35:29.399628+00:00'
page_id: '74645702'
product: fluig
source: tdn-fluig
title: Configurar aplicativo Datasul 11 na plataforma
type: documentation
url: https://tdn.totvs.com/display/fluig/Configurar+aplicativo+Datasul+11+na+plataforma
version: 19
---

# Índice

true.\*ndicenone

Atenção!

Devido a necessidade de execução de applets, este recurso não tem seu funcionamento como esperado. Os applets são uma tecnologia depreciada e por este motivo foram descontinuados pelos navegadores no geral.

### Configuração de Aplicativo Datasul 11 no TOTVS Fluig Plataforma

---

Para executar os programas do EMS é necessário configurar o Adapter e Aplicativo.

### Cadastrando o Adapter

---

Primeiro é necessário cadastrar um adapter que utilize o arquivo **Dtsul11Adapter.jar**. Para isso é somente necessário adicionar um novo adapter e no campo **Arquivo JAR** informar:

A funcionalidade **Adapter** está disponível no menu **Painel de Controle**, agrupador **Desenvolvimento**.

### Cadastrando o aplicativo

---

Depois do adapter cadastrado é necessário criar o aplicativo que vai executar o Datasul 11.

Clicar em **Adicionar** e informe o código do aplicativo e descrição, selecione o adapter do Datasul 11 e no campo linha de comando informe qualquer caractere (no caso do exemplo abaixo foi informado um ponto final “.”), pois a tela valida se tem informação no campo *Linha Comando* e caso não tenha nada informado, ela não deixa o usuário adicionar o aplicativo.

No cadastro do aplicativo, também é necessário adicionar cinco parâmetros na tabela **Parâmetros**, para incluir um parâmetro basta clicar no botão **Adicionar**.

Os parâmetros cadastrados devem ser configurados conforme tabela a seguir:

|  |  |  |  |
| --- | --- | --- | --- |
| **Parâmetro** | **Valor** | **Variável por Usuário** | **Formato Senha** |
| **host** | Informar o nome do servidor ou IP | Não | Não |
| **port** | Informar a porta de comunicação com o servidor | Não | Não |
| **user** | Informar o código do usuário do Datasul 11. | Sim | Não |
| **password** | Informar a senha do usuário do Datasul 11. | Sim | Sim |
| **dialect** | Informar o dialeto para exibição das mensagens de erro. Valores possíveis: "PT" (Português), "EN" (Inglês), "ES" (Espanhol) | Opcional. Se não for informado, será assumido o dialeto padrão (PT) | Não |

Nota

Os parâmetros devem estar com o código exatamente como descrito na coluna **Parâmetro** da tabela acima, respeitando maiúsculas e minúsculas.

### Publicando um Aplicativo

---

Para configurar um programa do Datasul 11 será necessário publicar um novo aplicativo abaixo de uma pasta.

 

Deve ser selecionado o aplicativo EMS configurado anteriormente e no campo **Parâmetros** deve ser informado a constante **Program:** mais o caminho do programa Datasul que será executado.

**Exemplo:**

 Publicando o aplicativo será criado o link na pasta selecionada e ao clicar será aberto o programa informado nos parâmetros do aplicativo.

### Configurando os parâmetros variáveis

---

Como alguns parâmetros são variáveis, cada usuário deve acessar as Preferências do Usuário e configurar estes parâmetros.

Por exemplo o dialeto, caso o usuário seja argentino, provavelmente terá preferência pelo dialeto espanhol.

Assim como ele também poderá ter como preferência um determinado usuário no Datasul 11, conforme abaixo:
