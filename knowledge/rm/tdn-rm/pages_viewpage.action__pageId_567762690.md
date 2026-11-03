---
content_hash: 19462c3840776b0fd856208abbac471651f2adf4aa87a3a67e5af98a4b85d0f6
fetched_at: '2026-06-29T00:10:51.445424+00:00'
page_id: '567762690'
product: rm
source: tdn-rm
title: TOTVS GESTÃO Hospitalar > Unidade de Diagnóstico > Laudos e resultados > Status
  Liberar Exame
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=567762690
version: 3
---

Se o Parâmetro Geral > Aba Prontuário Eletrônico > Assinar laudo digitalmente estiver DESMARCADO OU o Status Corrente for igual a C.

Então o Laudo passa para o Status L:

Assinar Digital do Exame

**Assinar Digital do Exame**

Ao realizar a liberação do exame, caso o parâmetro Assinar Laudo Digitalmente estiver marcado logo após que o novo status for salvo, será verificado os seguintes pontos para incluir a Assinatura.

O Exame deve ter um cadastro de Métodos e Parâmetros Ativo: Para isso você deve acessar o Menu *Cadastros/Métodos e Parâmetros de Exame*

*Para exames do tipo Imagem é necessário que a opção **“Utiliza Laudo Pré-impresso”,** essa opção pode ser definida no Menu Cadastros/Exames e Serviços.*

Caso essa configuração estiver configurada conforme o texto acima, o relatório será definido como laboratorial. Tanto os exames de imagem e laboratorial, caso não seja informado um código para o relatório, será utilizado os parâmetros Relatório Laudo de Imagem/ Relatório Laudo de Laboratorial definidos nos Parâmetros Gerais.
