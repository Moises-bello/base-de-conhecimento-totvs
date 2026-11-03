---
content_hash: 2cd3c6130d54a08715eccecc6c4b6bd99bd2524b088bed45f23c4a8b9d9ea4a3
fetched_at: '2026-06-29T00:08:47.115760+00:00'
page_id: '318608371'
product: rm
source: tdn-rm
title: Integração RM x Snowden
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=318608371
version: 18
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Esta página tem por objetivo demonstrar como é feita a integração RM x Snowden.

# Como Funciona:

---

      Para utilizar o recurso, antes você deverá permitir acesso ao usuário através do Perfil. Na árvore de perfil clique em: Acesso a Menus → Serviços Globais →  Permissões Globais → Processos → Reportar para TOTVS.

      ***Obs.: Essa permissão deve estar presente na árvore de permissões dos perfis independente do módulo selecionado.***

      Descrição passo a passo de como é o funcionamento do Snowden:

falseInstalação em N camadas (App Server)1º Passo:

Ao ocorrer uma mensagem de erro no sistema, clique no botão **"Reportar para TOTVS"**.

Essa ação irá enviar os dados do erro e uma série de informações para o Snowden que auxiliarão na análise do incidente.

|  |
| --- |

2º Passo:

Na aba "Incidente" o Snowden retornará um número de protocolo e um link, onde as informações enviadas podem ser acessadas.

Ao abrir o ticket para o atendimento e/ou desenvolvimento, basta inserir as informações do protocolo e link. Não haverá necessidade de enviar print ou mensagem de erro, apenas informações adicionais ou forma de simulação

|  |
| --- |

3º Passo:

Ao ocorrer uma mensagem de erro, em que o Snowden já tenha uma solução existente para o incidente, o botão **"Reportar para TOTVS"** será desabilitado e a solução cadastrada será exibida automaticamente na aba de "Solução".

|  |
| --- |

4º Passo:

Quando ocorrer um erro em telas de processo que não seja tratado pelo produto, ou se tratar de uma validação de regra de negócio, a opção **"Reportar para TOTVS"** também será exibida, conforme mostra as imagens abaixo:

|  |
| --- |

|  |
| --- |

falseObservação:

**Para abertura de um ticket o usuário deve seguir as mesmas informações descritas nos passos 1 e 2.**

5º Passo:

Segue abaixo um exemplo da mensagem que será exibida caso o usuário acesse a aba de "Incidente", e o Snowden não tenha nenhuma solução cadastrada para o incidente em sua busca.

|  |
| --- |

6º Passo:

Ao clicar no link retornado pelo Snowden, será exibida uma página com as informações do erro, conforme mostra a imagem abaixo:

|  |
| --- |

Para o usuário final a página contém informações do erro para simples conferência e acompanhamento.

Para o atendimento e/ou desenvolvimento a página conterá informações mais ricas , que contem:

* logs
* Prints das telas em execução;
* Stack traces;
* Rotinas em execução;
* Dados das classes de parâmetros.

falseObservação:

**Nenhum dado sensível ou particular da base de dados será enviada para a TOTVS, somente os dados técnicos para análise de incidentes.**

Importante

Na visão do incidente é possível localizar um link para baixar um arquivo. Este arquivo se trata de um log completo com várias informações técnicas importantes que podem ser visualizadas através da ferramenta **ErrorReportView** que encontra-se no diretório de instalação do RM. Para mais informaçõesacesse:

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.20

false

**Processo:** Integração RM x Snowden

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
