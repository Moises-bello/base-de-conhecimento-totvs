---
content_hash: ead7ea78a447627adebf39089e1058cd29d5145660d0715b893f7d430d1d17e7
fetched_at: '2026-06-29T00:09:19.449024+00:00'
page_id: '421391585'
product: rm
source: tdn-rm
title: Como realizar o processo de validação do evento S-1200 x Envelope
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421391585
version: 26
---

# Objetivo:

---

O objetivo deste documento é informar o funcionamento da validação do evento S-1200 com as informações do envelope.

---

Este relatório irá comparar os eventos existentes no envelope de pagamento com os eventos do XML S-1200.

Para habilitar este menu devemos dar permissão para o usuário através Serviços Globais/ Segurança/ Perfil /Fila de eventos/Validar 1200 com Envelope

### Exemplo I :

   Selecionar um funcionário na fila de eventos e marcar "Ver toda comparação".

Envelope

    

  XML:

     

  Resultado do relatório:

   O sistema retornou em **preto** os valores que não tiveram diferença**,** em **laranja** os avisos**.**

Retirando o evento **0082**  do envelope.

  Neste exemplo o evento 0082 foi retirado do envelope e continua no XML.

Ver toda comparação com erros ( Envelope sem o evento 0082)

 O sistema retornou em **preto** os valores que não tiveram diferença**,** em **laranja** os avisos e  **vermelho**os erros.

**Exemplo II:**

Mostrar o que existem no envelope e **NÃO** existem no xml e mostrar registros com erro.

  Incluído o evento com o código  "Hora" no envelope .

Neste exemplo o evento "Hora" não existe no XML.

O sistema retornou a mensagem informando que o registro não foi gerado no XML.

Sabendo que existem registros no envelope que não estão no XML ao selecionar **"mostrar registros com aviso"** será demonstrada apenas os avisos .

**Exemplo III:**

Mostrar registros que existem no XML e  não existem no envelope.

 No envelope foi retirado o evento de código "HORA"

No XML temos o evento "HORA"

Gerando o relatório.

Importante:

Esse relatório utilizará as tabelas definidas a seguir no processo de comparação:

* Quando "Utiliza Tomador de Serviço" estiver marcado , será considerada a tabela PFMOVTOMADOR, caso contrário, será  PFFINANC.
* Quando o cálculo for por  "Dissídio ", será considerada a tabela PFVERBASDIS, caso contrário, será  PFFINANC.
falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.22.112 |
| 12.1.21.145 |
| 12.1.20.404 |

falsefalse

**Status: Pendente**

false

**Data:**

false

**Autor:**
