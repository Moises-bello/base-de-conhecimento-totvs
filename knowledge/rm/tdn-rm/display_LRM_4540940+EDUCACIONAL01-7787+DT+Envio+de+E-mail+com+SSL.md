---
content_hash: 7942da675629675acc387c052803e4439911bec75337ae719f2b217432d954b4
fetched_at: '2026-06-29T00:09:58.461840+00:00'
page_id: '452700215'
product: rm
source: tdn-rm
title: 4540940 EDUCACIONAL01-7787 DT Envio de E-mail com SSL
type: documentation
url: https://tdn.totvs.com/display/LRM/4540940+EDUCACIONAL01-7787+DT+Envio+de+E-mail+com+SSL
version: 1
---

# ENVIO DE E-MAIL COM SSL

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Educacional |
| **Função:** | Envio de E-mail |
| **Situação/Requisito:** | Ao tentar enviar e-mail de inscrição no anexo Candidatos da Prova ocorre o erro: "O certificado remoto é inválido, de acordo com o procedimento de validação" |
| **Solução/Implementação:** | A rotina de envio de e-mail foi alterada para preencher o parâmetro de validação do certificado se estiver nulo, pois ele está ficando nulo quando o sistema é rodado com jobRunner. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
