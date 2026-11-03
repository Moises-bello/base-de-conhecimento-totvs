---
content_hash: deccdd14d8b93844760c8b01d4cc95c9f87eed355651eb7a75c9fdcbaf357a1a
fetched_at: '2026-06-29T00:09:58.956772+00:00'
page_id: '452718262'
product: rm
source: tdn-rm
title: Gerar Gatilhos em Lotes
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+Gatilhos+em+Lotes
version: 8
---

Este processo tem como objetivo permitir a geração de múltiplos gatilhos para os eventos do eSocial de forma prática e automatizada. Ele é executado por meio do seguinte caminho no sistema: Folha de Pagamento | eSocial | Outros Processos | Gerar Gatilhos em Lotes.

Com este recurso, é possível gerar novos gatilhos com base em filtros aplicados, conforme a **“Data de Alteração”** informada, sem a necessidade de acessar cada registro individualmente.

---

**Parâmetro "Dissídio" e Campo "Data Efetiva"**

* Ao marcar o parâmetro **“Dissídio”**, o sistema habilita o campo **"Data Efetiva"**.
* Esse campo deve ser preenchido pelo usuário quando houver alterações salariais motivadas por dissídio coletivo.
* Com essas informações, o sistema irá gerar gatilhos do evento S-2206 com a Data Efetiva devidamente preenchida, garantindo que o envio ao eSocial ocorra com os dados corretos de vigência.

---

**Parâmetro "Gerar Gatilho para Final do Contrato"**

* Quando este parâmetro estiver selecionado, o sistema irá gerar **apenas gatilhos do evento S-2206**, com base na **Data Final do Contrato** registrada no cadastro do funcionário.
* O gatilho será criado para o dia seguinte ao término do contrato, considerando o campo: Cadastros | Funcionários | Aba Registros | Dados do Contrato.  
  🔹 Campo: `Data Final do Contrato (PFUNC.FIMPRAZOCONTR)`

⚠️ **Atenção**

1. 1. * Se o parâmetro **"Gerar Gatilho para Final do Contrato"** estiver marcado, o sistema gerará exclusivamente gatilhos para o evento S-2206.  
        Caso o usuário selecione qualquer outro evento, será exibida a seguinte mensagem de alerta:
      * Serão considerados apenas os contratos com término dentro da competência selecionada no momento da geração.  
        Términos de contrato fora do período informado não terão gatilhos gerados.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

S-2206 Alteração de Contrato de Trabalho
