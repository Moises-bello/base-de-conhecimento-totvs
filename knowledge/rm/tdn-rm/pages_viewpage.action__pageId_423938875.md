---
content_hash: 50489aad09d844d78178df7d02fbb895c9488d1c5ef4a705e9038168ae02372e
fetched_at: '2026-06-29T00:09:29.314204+00:00'
page_id: '423938875'
product: rm
source: tdn-rm
title: Recebimento Automático de CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938875
version: 10
---

A fim de tornar o processo de integração do Totvs Colaboração 2.0 mais automatizado e completo, foi implementada a criação automática de um movimento de CT-e. Para isso, o usuário deverá criar uma ordem de compra e depois faturá-la, inserindo o XML de retorno do fornecedor, onde ao incluir esse XML o sistema irá criar um movimento de "Recebimento de Materiais" com todas as informações retornadas pelo XML. O processo deverá seguir as seguintes regras para o correto funcionamento da importação do XML e criação do movimento automático pelo sistema.

**Regras Gerais**

* Para criação automática do movimento, é necessário que exista pelo menos um tipo movimento de entrada (Recebimento de materiais) parametrizado para Recebimento de CT-e;
* A criação automática do movimento deverá ser parametrizável por filial  e por tipo de movimento, uma vez que o cliente pode possuir mais de um tipo de movimento para recebimento de CT-e;
* O sistema deverá encontrar a Natureza de Operação inversa para inclusão do movimento de entrada, baseada na Natureza de saída enviada no arquivo XML pelo fornecedor;
* O processo de criação do movimento deverá ocorrer após a validação do arquivo .XML, conforme ocorre atualmente;
* Caso a criação automática do movimento não seja possível devido à falta de alguma informação obrigatória para o sistema, este deverá possibilitar o ajuste da informação faltante na inclusão do movimento, sem a necessidade de preenchimento de todas as informações, conforme ocorre atualmente;
* Para identificação dos casos citados acima, deverá ser criado um novo status na importação do arquivo.XML, indicando que o mesmo está válido, mas que o sistema não conseguiu incluí-lo por algum motivo;
* Todas as validações/consistências executadas na criação manual do movimento devem ser também executadas na criação automática do CT-e;
* Em caso de **exclusão** do movimento de CT-e criado, o .XML em questão deve ser desvinculado ao movimento, e voltar ao status anterior à  inclusão, para que seja possível vinculá-lo à um novo movimento;
* Em caso de **cancelamento** do movimento de CT-e criado, o .XML não poderá ser mais utilizado, uma vez que o cancelamento é enviado e solicitado diretamente à SEFAZ.

**Tributos passíveis de integração com o movimento que será criado:**

* ICMS
* IBS (MUN E UF)
* CBS

O sistema valida o xml para integração desses tributos ao movimento, para que o processo seja concluído com sucesso se faz necessário que os tributos estejam parametrizados no tipo de movimento e que estejam presentes no cadastro de tributos.

---
