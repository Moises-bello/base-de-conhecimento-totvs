---
content_hash: 55efdf9d9853f0e3a0da890598cdf34718f00e90025501c3160ee7757fad960a
fetched_at: '2026-06-29T00:09:14.714129+00:00'
page_id: '421385237'
product: rm
source: tdn-rm
title: Exportação de Ciclos de Transporte
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385237
version: 3
---

---

O processo de exportação de Ciclos de Transporte é realizado a partir de um WebService disponibilizado no TOTVS Obras e Projetos. Ele receberá uma requisição do coletor móvel, irá processar, formatar e retornar ao coletor todos os dados do Ciclo de Transporte disponíveis no TOP em formato XML.

**Atenção:**

* Para que a sincronização dos dados ocorra devem existir Ciclos de Transporte cadastrados no TOTVS Obras e Projetos e prontos para o apontamento;
* Para realizar a exportação de Ciclos de Transporte o usuário faz login no coletor móvel, que verifica necessidade de atualização dos dados. O aplicativo do coletor acessa um método do WebService informando parâmetros (no formato XML) como coligada, usuário/senha, identificador do coletor, etc. Os dados informados pelo usuário são validados e se existirem Ciclos de Transporte disponíveis eles serão exportados para o coletor. Após o final do processo e retorno das informações ao coletor móvel, será gerado um log da integração. Caso ocorra erro na sincronização, além de enviar os erros para a tabela de log´s, será encaminhado e-mail a um endereço (ou grupo) previamente parametrizado.
